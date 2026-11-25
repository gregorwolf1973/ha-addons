#!/usr/bin/env python3
"""Holt aktive Add-ons aus den Einzel-Repos in diesen Store.

Nur Standardbibliothek. Anonym (GitHub raw/API, GHCR). Idempotent.
Ein Add-on wird nur übernommen, wenn das Image der Version in GHCR für
alle in `arch` gelisteten Architekturen existiert.
"""
import json
import os
import re
import shutil
import sys
import tempfile
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OWNER = "gregorwolf1973"
# Einzelne Dateien, die übernommen werden (fehlende werden übersprungen)
FILES = ["config.yaml", "config.json", "README.md", "DOCS.md", "CHANGELOG.md",
         "icon.png", "logo.png"]
MANIFEST_ACCEPT = ", ".join([
    "application/vnd.oci.image.index.v1+json",
    "application/vnd.oci.image.manifest.v1+json",
    "application/vnd.docker.distribution.manifest.list.v2+json",
    "application/vnd.docker.distribution.manifest.v2+json",
])


def http(url, method="GET", headers=None):
    """Gibt (Status, Bytes) zurück; 404 -> (404, b'')."""
    h = {"User-Agent": "ha-addons-sync"}
    h.update(headers or {})
    req = urllib.request.Request(url, method=method, headers=h)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        if e.code in (404, 401, 403):
            return e.code, b""
        raise


def top_level(text, key):
    """Liest ein Feld der obersten Ebene aus config.yaml (ohne yaml-Modul)."""
    m = re.search(r"^%s:\s*(.*)$" % re.escape(key), text, re.M)
    if not m:
        return None
    return m.group(1).strip().strip("\"'")


def parse_config(name, data):
    text = data.decode("utf-8")
    if name.endswith(".json"):
        c = json.loads(text)
        return {k: c.get(k) for k in ("name", "version", "image", "description")}, \
            [str(a) for a in c.get("arch", [])]
    info = {k: top_level(text, k) for k in ("name", "version", "image", "description")}
    m = re.search(r"^arch:[ \t]*\n((?:[ \t]+-[ \t]*\S+[ \t]*\n)+)", text + "\n", re.M)
    if m:
        archs = re.findall(r"-\s*(\S+)", m.group(1))
    else:  # Inline-Form: arch: [a, b]
        m = re.search(r"^arch:\s*\[(.*)\]", text, re.M)
        archs = [a.strip().strip("\"'") for a in m.group(1).split(",")] if m else []
    return info, [a.strip("\"'") for a in archs]


def image_exists(image, version):
    """HEAD auf das Manifest bei GHCR (anonymer Pull-Token)."""
    host, _, name = image.partition("/")
    if host != "ghcr.io":
        return None  # unbekannte Registry: nicht prüfbar
    st, body = http("https://ghcr.io/token?scope=repository:%s:pull" % name)
    if st != 200:
        return False
    token = json.loads(body)["token"]
    st, _ = http("https://ghcr.io/v2/%s/manifests/%s" % (name, version), "HEAD",
                 {"Authorization": "Bearer " + token, "Accept": MANIFEST_ACCEPT})
    return st == 200


def fetch_addon(a, dest):
    """Lädt alle Dateien in dest; gibt (info, archs) zurück oder None."""
    raw = "https://raw.githubusercontent.com/%s/%s/HEAD/%s" % (OWNER, a["repo"], a["path"])
    cfg = None
    for f in FILES:
        st, data = http(raw + "/" + f)
        if st == 200:
            with open(os.path.join(dest, f), "wb") as fh:
                fh.write(data)
            if f.startswith("config."):
                cfg = cfg or parse_config(f, data)
    # translations/* über die GitHub-API auflisten (anonym, 60 Anfragen/h)
    st, body = http("https://api.github.com/repos/%s/%s/contents/%s/translations"
                    % (OWNER, a["repo"], a["path"]))
    if st == 200:
        os.makedirs(os.path.join(dest, "translations"), exist_ok=True)
        for e in json.loads(body):
            if e.get("type") == "file":
                s2, d2 = http(e["download_url"])
                if s2 == 200:
                    with open(os.path.join(dest, "translations", e["name"]), "wb") as fh:
                        fh.write(d2)
    return cfg


def table(addons):
    rows = ["| Add-on | Description | Version | Architectures | Source |",
            "| --- | --- | --- | --- | --- |"]
    for a in addons:
        try:
            with open(os.path.join(ROOT, a["slug"], "meta.json")) as fh:
                m = json.load(fh)
        except OSError:
            continue
        desc = (m.get("description") or "").replace("|", "/")
        rows.append("| %s | %s | %s | %s | [%s](https://github.com/%s/%s) |" % (
            m["name"], desc, m["version"], ", ".join(m["arch"]), a["repo"], OWNER, a["repo"]))
    return "\n".join(rows)


def main():
    with open(os.path.join(ROOT, "addons.json")) as fh:
        addons = json.load(fh)["addons"]
    warnings = 0
    for a in addons:
        if not a.get("aktiv"):
            continue
        slug = a["slug"]
        tmp = tempfile.mkdtemp(prefix="sync-")
        try:
            cfg = fetch_addon(a, tmp)
            if not cfg:
                print("WARN %s: no config found upstream, keeping old version" % slug)
                warnings += 1
                continue
            info, archs = cfg
            version, image = info["version"], info["image"]
            if not version or not image or not archs:
                print("WARN %s: config lacks version/image/arch, keeping old version" % slug)
                warnings += 1
                continue
            missing = [x for x in archs
                       if not image_exists(image.replace("{arch}", x), version)]
            if missing:
                print("WARN %s %s: image missing for %s, keeping old version"
                      % (slug, version, ", ".join(missing)))
                warnings += 1
                continue
            # Metadaten für die Tabelle ablegen (liegt außerhalb des Add-on-Ordners nicht nötig)
            with open(os.path.join(tmp, "meta.json"), "w") as fh:
                json.dump({"name": info["name"], "description": info["description"],
                           "version": version, "arch": archs}, fh, ensure_ascii=False)
            target = os.path.join(ROOT, slug)
            old = None
            if os.path.exists(os.path.join(target, "meta.json")):
                with open(os.path.join(target, "meta.json")) as fh:
                    old = json.load(fh).get("version")
            shutil.rmtree(target, ignore_errors=True)
            shutil.copytree(tmp, target)
            print("OK   %s %s%s" % (slug, version, "" if old == version else " (was %s)" % old))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    # Tabelle in README zwischen den Markern ersetzen
    path = os.path.join(ROOT, "README.md")
    with open(path) as fh:
        text = fh.read()
    new = re.sub(r"(<!-- ADDONS:START -->\n).*?(<!-- ADDONS:END -->)",
                 lambda m: m.group(1) + table(addons) + "\n" + m.group(2), text, flags=re.S)
    if new != text:
        with open(path, "w") as fh:
            fh.write(new)
    return 0


if __name__ == "__main__":
    sys.exit(main())
