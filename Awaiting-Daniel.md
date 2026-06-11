# Awaiting Daniel

Decisions and actions only Daniel can take.

- [ ] **Enable GitHub Pages** — repo Settings → Pages → deploy from `main` / root; custom domain `www.nfceh.org`. (Sandbox can't reach the GitHub settings API.)
- [ ] **Run `bash download-assets.sh`** from a local clone while the Wix plan is active — pulls team photos, logo, heart graphic, and the Homelessness Sunday flyer PDF into `assets/`; commit them. (Clears the 26 G7 asset warnings.)
- [ ] **Favicon family** — generate from one ≥512px transparent logo master (favicon.png 192, -32, -180, .ico). Current favicon is a placeholder logo copy.
- [ ] **DNS cutover timing** — when ready: drop TTL to 5 min, wait 24h, then apex A/AAAA records + `www` CNAME → `dvs-dnl.github.io` (playbook §3). Keep Wix 2–4 weeks as rollback.
- [ ] **Domain email** — decide forwarding for info@nfceh.org / daniel@nfceh.org (registrar forwarding or Cloudflare Email Routing); MX records must survive cutover.
- [ ] **GA4 outbound-click events** — approve adding register_church / newsletter_signup / donate_click / flyer_download event tracking (small JS addition, Claude can do it on request).
- [ ] **Delete the stale `.git` folder** in `Website Rebuild/site/` on the Mac (sandbox lock-file artifact; harmless but dead weight).
- [ ] **Orchestrator registration** — when autonomous publishing is wanted, add this repo to `~/Documents/Claude/All Project Updater/registry.yaml`.
