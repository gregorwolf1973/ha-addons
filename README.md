# Gregor Wolf – Home Assistant Add-ons

[![Buy me a coffee](https://img.shields.io/badge/Buy%20me%20a%20coffee-FFDD00?logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/gregorwolf1973) [![Liberapay](https://img.shields.io/badge/Liberapay-donate-F6C915?logo=liberapay&logoColor=black)](https://liberapay.com/Gregor_Wolf/donate)

A single add-on store for my Home Assistant add-ons. The code stays in the
individual repositories (linked in the table below); this store is updated
automatically from them, and only with versions whose pre-built images are
already published.

[![Add repository to my Home Assistant](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fgregorwolf1973%2Fha-addons)

Or add it manually: *Settings → Add-ons → Add-on Store → ⋮ → Repositories* and enter
`https://github.com/gregorwolf1973/ha-addons`.

## Existing installations

Add-ons installed from the individual repositories keep working and keep
receiving updates there. Moving to this store means installing the add-on again
from here (the store is a different repository, so Home Assistant treats it as
a new add-on). Back up the add-on's data first.

## Add-ons

<!-- ADDONS:START -->
| Add-on | Description | Version | Architectures | Source |
| --- | --- | --- | --- | --- |
| Startpanel | Dashboard showing all Home Assistant addons with icons and quick access links | 0.36 | aarch64, amd64, armhf, armv7, i386 | [addon-startpanel](https://github.com/gregorwolf1973/addon-startpanel) |
| Chat Server | Selbstgehosteter Messenger mit Gruppen, Dateiversand und Push-Benachrichtigungen | 0.48.1 | aarch64, amd64 | [chat-server-addon](https://github.com/gregorwolf1973/chat-server-addon) |
| Chromium Light Browser | Lightweight Chromium in the sidebar - starts on demand and sleeps when idle | 0.2.5 | aarch64, amd64 | [Chromium_light_browser](https://github.com/gregorwolf1973/Chromium_light_browser) |
| ClamAV Antivirus | ClamAV-based antivirus scanner for Home Assistant with web GUI, scheduled scans, quarantine and HA notifications | 1.0.14 | aarch64, amd64, armv7 | [clamav-hassio-addon](https://github.com/gregorwolf1973/clamav-hassio-addon) |
| Cloudflare Route Manager | Manage Cloudflare DNS records and tunnel routes from Home Assistant; adds Cloudflare IPs to trusted_proxies automatically | 1.0.6 | aarch64, amd64, armv7 | [cloudflare-routes-addon](https://github.com/gregorwolf1973/cloudflare-routes-addon) |
| CrowdSec Cloudflare Bouncer | Enforces CrowdSec decisions at Cloudflare (Workers + KV) - blocks attackers at the Cloudflare edge, even behind a tunnel | 0.1.5 | aarch64, amd64, armv7 | [crowdsec-cloudflare-bouncer-addon](https://github.com/gregorwolf1973/crowdsec-cloudflare-bouncer-addon) |
| CrowdSec Dashboard | Web UI to view and manage CrowdSec bans and alerts | 1.4.4 | aarch64, amd64, armv7 | [crowdsec-dashboard-addon](https://github.com/gregorwolf1973/crowdsec-dashboard-addon) |
| Simple NAS | Simple NAS with Samba shares and web GUI for drive management | 3.23.2 | aarch64, amd64, armv7 | [EasyNas-HASSIO-Addon](https://github.com/gregorwolf1973/EasyNas-HASSIO-Addon) |
| Fotoarchiv | Photo and video library: timeline, world map, face recognition, plain-language search, in-file editing | 0.66.2 | aarch64, amd64 | [fotoarchiv-addon](https://github.com/gregorwolf1973/fotoarchiv-addon) |
| FritzBox & HA Metrics Exporter | Pushes FritzBox (TR-064) and Home Assistant metrics to InfluxDB 1.x | 0.3.3 | aarch64, amd64, armv7 | [fritz-network-addon](https://github.com/gregorwolf1973/fritz-network-addon) |
| FritzBox Network | Network topology visualizer for FritzBox - all network devices as an interactive force graph | 1.0.22 | aarch64, amd64, armv7 | [fritz-network-addon](https://github.com/gregorwolf1973/fritz-network-addon) |
| Guacamole Stable | Apache Guacamole 1.5.5 mit FreeRDP 2.11 - HTML5 Remote Desktop Gateway (RDP/VNC/SSH) | 1.1.0 | aarch64, amd64 | [guacamole-stable-addon](https://github.com/gregorwolf1973/guacamole-stable-addon) |
| German TV Panel | Free German TV channels (ARD, ZDF, Arte, ...) as a sidebar panel in Home Assistant. | 1.0.7 | aarch64, amd64, armv7 | [ha-addon-german-tv](https://github.com/gregorwolf1973/ha-addon-german-tv) |
| HA Guardian | Brute-force protection for Home Assistant – monitors logs and auto-bans attacking IPs via ip_bans.yaml (application layer) with optional network-level blocking | 1.30.1 | amd64, aarch64, armv7, armhf, i386 | [ha-guardian](https://github.com/gregorwolf1973/ha-guardian) |
| Hardware Monitor | Live overview of hardware resources: CPU, RAM, disks, network and top processes | 2.7.1 | aarch64, amd64, armv7 | [hardware-monitor-addon](https://github.com/gregorwolf1973/hardware-monitor-addon) |
| DokuWiki | DokuWiki running as a Home Assistant Add-on | 1.0.7 | aarch64, amd64 | [Hassioadon_Dokuwiki](https://github.com/gregorwolf1973/Hassioadon_Dokuwiki) |
| Heimdall | Heimdall Application Dashboard for Home Assistant | 2.8.1 | aarch64, amd64 | [Hassio_Heimdall](https://github.com/gregorwolf1973/Hassio_Heimdall) |
| LibrePhotos | Self-hosted photo management with AI face recognition and automatic classification | 0.14 | amd64, aarch64 | [LibrePhotos-HASSIO-Addon](https://github.com/gregorwolf1973/LibrePhotos-HASSIO-Addon) |
| Mailwächter | Überwacht das Gmail-Postfach per IMAP IDLE, prüft jede neue Mail auf Betrug und verschiebt gefährliche Mails | 0.2.0 | aarch64, amd64 | [mailwaechter-addon](https://github.com/gregorwolf1973/mailwaechter-addon) |
| OnionShare | Share & receive files, host websites and chat anonymously via Tor | 0.1.4 | aarch64, amd64 | [onionshare-addon](https://github.com/gregorwolf1973/onionshare-addon) |
| PictureView | Security camera image viewer with timeline and optional auto-delete | 0.13 | aarch64, amd64, armv7 | [PictureView](https://github.com/gregorwolf1973/PictureView) |
| Recon | Network Scanner - IP/Port scanning with Nmap, WLAN scanning with iw | 1.5.11 | aarch64, amd64 | [Racon-addon](https://github.com/gregorwolf1973/Racon-addon) |
| Seafile | Self-hosted file sync and sharing — Seafile server with built-in MariaDB | 0.2.12 | amd64, aarch64 | [seafile-hassio-addon](https://github.com/gregorwolf1973/seafile-hassio-addon) |
| SnappyMail | Simple, modern & fast web-based email client. Supports multiple accounts including Gmail. | 1.5.0 | aarch64, amd64, armv7 | [snappymail-addon](https://github.com/gregorwolf1973/snappymail-addon) |
| Türöffner | Haustür per Handy öffnen – eigene Zugänge für Freunde mit Passwort, 2FA (Pflicht oder freiwillig) und Passkey, Freigabe durch dich. Für die Familie zusätzlich Warmwasser aufheizen, Staubsauger steuern, Livebild der Kamera, Pollenflug, Standorte der Familie, Hausdienst-Plan mit Anruf am Morgen und Gäste-WLAN per QR-Code | 0.17.0 | aarch64, amd64 | [tuer-oeffner-addon](https://github.com/gregorwolf1973/tuer-oeffner-addon) |
<!-- ADDONS:END -->

More add-ons will be added to this store step by step.

## Support

If you find these add-ons useful, you can [buy me a coffee](https://www.buymeacoffee.com/gregorwolf1973) ☕ or donate via [Liberapay](https://liberapay.com/Gregor_Wolf/donate).
