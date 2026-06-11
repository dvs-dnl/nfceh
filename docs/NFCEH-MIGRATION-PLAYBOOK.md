# NFCEH Migration Playbook — Wix → Static HTML on GitHub Pages

**Purpose:** The single operating doc for the nfceh.org migration. Distilled from three house blueprints — `BRAND-LAUNCH-BLUEPRINT.md` (portfolio stack + DNS/launch sequence), `CLAUDE-CODE-SHIP-BLUEPRINT.md` (ship discipline + verification), and `trailmanual-blueprint.md` (static-on-Pages architecture + gate system) — and mapped onto NFCEH's actual state as of June 10, 2026.

**Current state:** The static site is already built at `Website Rebuild/site/` (14 pages, brand system, GA tag `G-5YTZMH6E01` on every page, CNAME/sitemap/robots/404 included). This playbook governs how it ships, how it's protected from regressions, and how it operates afterward.

---

## 1. Architecture decisions (settled — don't relitigate)

These were learned the hard way across four prior brands. NFCEH inherits the conclusions:

- **Static HTML on GitHub Pages. No CMS, no Wix, no WordPress, no build step.** The repo IS the deployment; push-to-live is under 90 seconds; recurring cost is the domain renewal only. Every brand that started on a CMS mental model paid to unwind it.
- **The static constraint shapes features.** No server means no forms and no server-side redirects. NFCEH is already shaped for this: newsletter/registration → Mailchimp, donations → Pushpay, store → Printful. Every CTA is a link. Keep it that way.
- **One folder = one URL.** `about/index.html` → `nfceh.org/about/`. Every page is an `index.html` in a directory. Never break this convention.
- **Files Claude can read and write are the whole authoring system.** No admin UI, no API brokering. This is what makes scheduled/autonomous content work later.

## 2. Repo setup (Day 0)

- [ ] Create repo `dvs-dnl/nfceh` (public).
- [ ] First commit contains, at root: the contents of `Website Rebuild/site/` plus:
  - `CNAME` — already in the site folder: one line, `www.nfceh.org`, no protocol, no trailing slash. **Get it right once and never touch it again** (Common Ladder burned 4 commits on CNAME churn).
  - `.nojekyll` — empty file at root. Without it, GitHub runs Jekyll and silently drops any underscore-prefixed file. Cheap insurance; silent when missing. *(Added to the site folder alongside this playbook.)*
  - `.gitignore` — `.DS_Store`, `*.bak`, `__pycache__/`, and the credentials file pattern. Add it before the second commit, not after the history needs cleaning.
- [ ] **Never commit a GitHub token to any tracked file.** Token lives at `~/Documents/Claude/.credentials/github-config.json` (already exists; expires 2027-05-19). Pushes use the `GIT_ASKPASS` helper pattern per `SECRETS-POLICY.md` — the `https://TOKEN@github.com/...` URL embed is banned after the 2026-05-29 leak incident.
- [ ] Settings → Pages → Deploy from branch `main`, folder `/ (root)`, custom domain `www.nfceh.org`.

**Branching:** the padmission model (work → staging → prod) is for an app with a test suite. NFCEH is a small static site: **single `main` branch + pre-push gates** is the house pattern for content brands (TrailManual, Common Ladder, autovetting all run this way).

## 3. DNS cutover (the only genuinely risky step)

Sequence matters. The site must be live on Pages **before** DNS moves, and Wix stays alive as rollback.

1. **24+ hours before cutover:** in the current DNS panel, drop TTL on the records you'll change to 5 minutes.
2. Push the full site to the repo; verify it renders at `dvs-dnl.github.io/nfceh` (or the Pages preview URL).
3. Set DNS:
   - Apex `@`: four A records → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - Apex `@`: four AAAA records → `2606:50c0:8000::153`, `:8001::153`, `:8002::153`, `:8003::153`
   - `www`: CNAME → `dvs-dnl.github.io`
   - Verify the authoritative list at the GitHub Pages docs first — the IPs have shifted historically. Confirm with `dig www.nfceh.org +short` after propagation.
   - **Keep MX records** if/when domain email (info@nfceh.org) is configured.
4. HTTPS cert provisions in 10–60 minutes after DNS resolves. **Only then** check "Enforce HTTPS." Enforcing early shows visitors cert warnings.
5. **Leave the Wix subscription running 2–4 weeks** as rollback. Before cancelling:
   - [ ] Run `download-assets.sh` (already written) — pulls all images + the Homelessness Sunday flyer PDF from wixstatic URLs that die at cancellation.
   - [ ] Export any Wix contact/form data.
6. Re-verify the domain in Google Search Console (the Wix verification meta tag is carried over in the site head; DNS-verify as backup) and submit `https://www.nfceh.org/sitemap.xml`.

**URL preservation:** every real Wix URL is mirrored in the new structure (`/about`, `/about/leadership`, `/about/participating-churches`, `/homelessness-sunday`, `/join`, `/donate`, `/blog`, `/learn`). GitHub Pages can't do server-side 301s; dropped junk pages (`/news`, `/events`, `/collections`, `/blank-2`, `/blank-5`) fall through to the branded `404.html`, which offers next steps. That's acceptable — none have SEO equity worth a meta-refresh shim.

## 4. Design system rules

- **One stylesheet.** `styles.css` is the single source of chrome. **No per-page `<style>` blocks that override header/nav/footer rules** — this is the regression class that broke autovetting's pinpoint page (same selectors, drifted values, page never actually linked the shared file). Page-specific tweaks via inline `style=""` on content elements are tolerable; chrome overrides are not.
- **Absolute paths everywhere** (`/styles.css`, `/assets/images/...`). Pages live at varying depths; relative paths break below the first level. (Consequence: local preview needs `python3 -m http.server`, not double-clicked files. Document this for anyone touching the repo — it's in the README.)
- **Brand tokens are law.** Colors only from the hex list (#469596 teal, #25C1E0 blue, #BEE5EA light blue, #EEAF4F amber, #F9E2C1 cream, #231F20 ink) as CSS variables. IBM Plex Sans body, Playfair Display editorial. Don't approximate; don't introduce new hexes outside `styles.css`.
- **WCAG pairs only** for text: Dark Teal on White, Bright Blue on White, Near Black on Amber, White on Dark Teal, Near Black on Teal. Light Blue is never body text on white/cream. (Common Ladder shipped 8 inline violations of its equivalent rule before gating it.)
- **Favicon family** (from one ≥512px transparent master): `favicon.svg` if available, `favicon.png` (192), `favicon-32.png`, `favicon-180.png` (apple-touch), `favicon.ico` at root. Currently a logo copy stands in — generate the real family before launch.
- **Design changes happen in `styles.css` + the page template, then propagate.** Never patch one page's chrome by hand.

## 5. SEO / AEO architecture

- **Canonical tag on every page** — already in place. (TrailManual backfilled 154 pages; NFCEH starts clean.)
- **Sitemap must always match reality.** `sitemap.xml` is hand-maintained; every new page = a `<url>` entry in the same commit. If the page count grows past ~25, generate the sitemap from the file tree instead.
- **`robots.txt`** allows all + Sitemap line — done.
- **Structured data:** `BlogPosting` JSON-LD on every post (cornerstone has it); consider `Organization` schema on the homepage with logo + sameAs social links.
- **AEO writing structure for all blog content** (this is how AI answer engines decide what to quote): lede sets stakes in 2–3 sentences → **direct answer stated plainly within the first 3 paragraphs** → explanation and nuance → what to do next → related internal links. The cornerstone post already follows this arc; hold every satellite post ("What Is a Continuum of Care?", "Why Charity Alone Cannot End Homelessness") to it.
- **Hub-and-spoke internal linking:** the cornerstone is the hub; every satellite links back to it and the hub links out to satellites as they publish. A hub that doesn't link its spokes delivers half its value. Internal links per the SEO Canon placement checklist (keyword in title, intro, subheading, conclusion).
- **OG/Twitter cards on every page** — done; og:image is the logo at an absolute URL. After changing OG tags post-launch, remember social platforms cache previews per-URL; stale previews are cache, not bugs.

## 6. Analytics (GA4)

- **One measurement ID, sitewide, forever: `G-5YTZMH6E01`.** Stray IDs from copy-paste are how analytics splits silently — TrailManual ran 8 pages on a wrong ID for an untracked window; autovetting had a stray legacy ID for weeks. This is gate #1.
- Snippet lives in `<head>` of every page (already true), and in the shared page template so new pages inherit it.
- **Instrument the high-value paths at template time, not later.** NFCEH's named events:
  - `register_church` — clicks to mailchi.mp/nfceh/homelessness-sunday (the #1 conversion: Road-to-500)
  - `newsletter_signup` — clicks to the main Mailchimp landing page
  - `donate_click` — clicks out to Pushpay
  - `flyer_download` — the Homelessness Sunday flyer PDF
  - `open_post` — blog post opens
  Outbound clicks need a small `gtag('event', ...)` handler on those anchors since conversion completes off-site.
- Verify events in GA4 DebugView before calling launch done.

## 7. The gate system (pre-push quality control)

Every gate below maps to a real production incident on a sibling site. Build `scripts/gate-check.py` + a `pre-push` hook + `install-hooks.sh` (lift from the T23/T24 playbook scaffolds / autovetting's 27-gate script, strip what doesn't apply). **Install the hook before the second commit** — gates added in week 12 cost whatever shipped in weeks 1–11.

**Universal gates (every site in the portfolio):**

| # | Gate | Incident it prevents |
|---|---|---|
| G1 | GA ID consistency — only `G-5YTZMH6E01` anywhere | split analytics (TrailManual, autovetting) |
| G2 | Canonical tag present on every page | 154-page backfill (TrailManual) |
| G3 | Exactly one `<h1>` per page | SEO/a11y drift |
| G4 | Nav hrefs identical across all pages | 3-link vs 5-link nav drift (autovetting) |
| G5 | Footer signature identical across all pages | four footer variants (autovetting) |
| G6 | Every page links `/styles.css`; no per-page chrome `<style>` overrides | pinpoint-page chrome breakage (autovetting) |
| G7 | All internal hrefs/srcs resolve to files in the repo | orphan content — a third of autovetting's checklists were unreachable |
| G8 | `target="_blank"` always paired with `rel="noopener"` | tabnabbing — 14 unprotected links (Common Ladder) |
| G9 | JS syntax: no apostrophe-in-single-quote strings, no missing array commas | silently dead IIFEs (autovetting, twice) |
| G10 | Every `<img>` has alt (empty alt allowed only on decorative) | a11y regression class |
| G11 | Sitemap entries ↔ pages on disk match both directions | sitemap drift |
| G12 | No secrets — run `scan_for_secrets.py`; refuse on non-zero | the 2026-05-29 token leak |

**NFCEH-specific brand gates:**

| # | Gate | Rule source |
|---|---|---|
| N1 | Banned phrases: "the homeless", "vagrants", "street people" → must be "people experiencing homelessness" / "unhoused neighbors" | person-first language, brand canon |
| N2 | "Building Together" never appears (signature phrase is "Forward Together") | coalition messaging canon |
| N3 | Mission statement, where present, is verbatim with **END** in caps | messaging canon |
| N4 | No HOUSE-framework references (Hear/Offer/Unite/Strengthen/Expand as a model) | retired June 2026 |
| N5 | WCAG text-color: light blue `#BEE5EA` never as text on white/cream; amber as text only on ink | brand contrast matrix |
| N6 | Date check: "October 11, 2026" (never May 2) | postponement |

**When to add a gate:** a bug that's a *class* ships → gate it. A one-off typo → just fix it. When a gate misses something it should have caught, add the gate **and** review why the others missed it.

## 8. Ship discipline (every change, forever)

The loop, from the padmission engagement, adapted to static:

```
explore → implement → verify-in-browser → gate-check → commit (one per change) → push → report with caveats
```

- **Explore before touching.** Read the page and its siblings; never invent structure that already exists.
- **Verify means a real render, not a clean diff.** `curl`/grep confirms wiring; an actual browser render (or headless screenshot) confirms design. "The combo that never lies: structural grep confirms wiring; a screenshot confirms design."
- **One commit per logical change**, clear subject + why in the body. **Never `git add -A`** — stage explicitly by path; unrelated untracked files are not yours to sweep in.
- **Rename = update every reference including the slug.** No server 301s on Pages, so changing a published URL needs a meta-refresh stub page at the old path — better: don't rename published URLs.
- **Don't invent facts.** Missing stat, date, or name → clearly-marked placeholder, flagged in the report. (The 771,480 PIT figure on the homepage is sourced; keep the source line.)
- **Confirm destructive actions against reality first** — before deleting any asset, grep for live references.
- **Sandbox hygiene:** the cowork sandbox can leave `.git/index.lock` files; push recipes start with `find .git -name "*.lock" -delete`.

## 9. Content pipeline (blog operations)

**Adding a post (the recipe — every step, every time):**

1. `blog/<slug>/index.html` from the existing post template (copy the cornerstone's file).
2. Update: `<title>`, meta description, canonical, OG tags, JSON-LD (`headline`, `author`, `datePublished`, `description`).
3. Tag by Type: **Cornerstone / Educate / Action / Foundational** (not HOUSE).
4. Add the `.post-card` to `blog/index.html`.
5. Add the `<url>` to `sitemap.xml`.
6. Internal links: link the hub (cornerstone) and any relevant satellites; check the SEO Canon keyword-placement checklist (title, intro, subheading, conclusion).
7. Voice integrity check before commit: reflective not promotional; experiential insight present; no exaggerated claims; calm analytical tone; person-first language throughout.
8. Gate-check → commit → push.

**Scaling later (the TrailManual pattern, when ready):** a `content/topic-queue.md` drained by a scheduled overnight writer task. Two non-negotiables from hard experience: **paste brand-voice rules verbatim into the task's SKILL.md** (banned words, signature phrases, person-first list — reference-by-link drifts), and human-review the queue's quality periodically. NFCEH already runs 4 scheduled tasks; register the repo in the All Project Updater `registry.yaml` when autonomous pushing is wanted, and the hourly orchestrator + `TASKS.md → Ready` convention takes over.

**Operational files to add at repo root (empty is fine, day one):**
- `TASKS.md` — In flight / Ready to deploy / Done (last 10)
- `Awaiting-Daniel.md` — every decision the system surfaces, in one known place
- `CLAUDE.md` — operating brief for fresh sessions: brand rules verbatim, file structure, deploy workflow, gate list, "October 11, 2026," banned words

## 10. Launch checklist (NFCEH-specific, in order)

**Done already:**
- [x] 14 pages built on brand system, validated (links, single h1, GA on all pages)
- [x] CNAME, sitemap.xml, robots.txt, 404.html, README
- [x] GA4 ID `G-5YTZMH6E01` sitewide
- [x] Canonical + OG on every page; BlogPosting schema on cornerstone
- [x] Real privacy + accessibility pages (Wix versions were unedited templates)
- [x] `download-assets.sh` written
- [x] `.nojekyll` added to site folder

**Remaining, in order:**
1. [ ] Run `download-assets.sh` while Wix is live; review images; generate the favicon family from the logo master
2. [ ] Local preview (`python3 -m http.server`) — every page, mobile width too
3. [ ] Add `scripts/gate-check.py` + pre-push hook (§7) + `CLAUDE.md`, `TASKS.md`, `Awaiting-Daniel.md`
4. [ ] Add GA4 outbound-click events (§6)
5. [ ] Create `dvs-dnl/nfceh`, push, enable Pages, verify preview URL
6. [ ] Drop DNS TTL to 5 min; wait 24h
7. [ ] DNS cutover (§3); verify HTTPS; enforce HTTPS
8. [ ] GA4 DebugView: events firing
9. [ ] Search Console: re-verify, submit sitemap
10. [ ] Real-device mobile pass on the live domain
11. [ ] Keep Wix 2–4 weeks; then export anything remaining and cancel
12. [ ] Register repo in orchestrator `registry.yaml` (when autonomous publishing is wanted)

## 11. Token & ops lifecycle

- GitHub PAT at `~/Documents/Claude/.credentials/github-config.json`, expires **2027-05-19** — calendar reminder 30 days prior; don't discover expiry via a broken push.
- Rotation = one-line update in the credentials file; nothing in the repo changes.
- If a token ever appears in a commit: rotate immediately (GitHub auto-revokes scanned tokens, but assume it was copied first).
- Email: the open question from the portfolio. Mailchimp landing pages carry signups for now; configure `info@nfceh.org` / `daniel@nfceh.org` forwarding at the DNS provider (free via registrar or Cloudflare Email Routing) — MX records must survive the cutover.
- Forms: unresolved portfolio-wide. If NFCEH ever needs on-site lead capture beyond Mailchimp links, that forces the Formspree/Netlify-Functions decision — defer until needed.

---

*Companion docs: `BRAND-LAUNCH-BLUEPRINT.md` (portfolio stack), `CLAUDE-CODE-SHIP-BLUEPRINT.md` (ship discipline), `trailmanual-blueprint.md` (static architecture + gates), `nfceh_site_crawl_documentation.md` (what the Wix site contained), `Website Rebuild/site/README.md` (repo-level instructions).*
