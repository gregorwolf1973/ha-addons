# Phase 2: pre-built images for the remaining add-ons

The store only lists add-ons whose image already exists on GHCR. Each source
repository therefore needs to build and publish its image, using the reusable
workflow of this repository.

## 1. Workflow in the source repository

`.github/workflows/build.yaml` (adjust the path and the image name):

```yaml
name: Build
on:
  push:
    branches: [main]
    paths: ["<addon-folder>/**"]
  workflow_dispatch:
jobs:
  build:
    permissions: {contents: read, packages: write}
    uses: gregorwolf1973/ha-addons/.github/workflows/build-addon.yaml@main
    with: {addon: "<addon-folder>", image: "ghcr.io/gregorwolf1973/{arch}-addon-<slug>"}
```

Optional input `archs` (JSON list, default `["aarch64","amd64"]`); `armv7` is built via QEMU.
The architectures must match the `arch:` list in `config.yaml`.

## 2. `config.yaml` of the add-on

```yaml
version: "1.2.3"        # bump for every release; the image tag is this version
image: ghcr.io/gregorwolf1973/{arch}-addon-<slug>
arch:
  - aarch64
  - amd64
```

The `Dockerfile` should start with `ARG BUILD_FROM` / `FROM ${BUILD_FROM}`. The base
image per architecture is read from `build.yaml` (`build_from:`) in the add-on folder.

## 3. Activate in the store

1. Make the GHCR package public (package settings → visibility), otherwise the
   store check and Home Assistant cannot pull it anonymously.
2. Set `"aktiv": true` for the add-on in `addons.json`.
3. Run the *Sync add-ons* workflow (or wait for the next 30-minute run).
