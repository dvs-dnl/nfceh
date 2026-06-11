# CLAUDE.md — nfceh.org

Operating brief for any session touching this repo. Read before changing anything.

## What this is

The static website for the National Faith Coalition to End Homelessness (NFCEH),
served by GitHub Pages at **www.nfceh.org** (repo: `dvs-dnl/nfceh`, branch `main`,
no build step — the repo is the site). Migrated from Wix June 2026.

## Hard rules

1. **Run the gates before every push:** `python3 scripts/gate-check.py`. Exit 1 = do not push. After cloning, run `bash scripts/install-hooks.sh` once so pushes gate automatically.
2. **Never hand-edit `sitemap.xml`** — run `python3 scripts/generate-sitemap.py` after adding/removing a page.
3. **One commit per logical change. Never `git add -A`** — stage explicitly by path.
4. **No secrets in this repo, ever.** GitHub token lives at `~/Documents/Claude/.credentials/github-config.json` (expires 2027-05-19); push via GIT_ASKPASS pattern only.
5. **One stylesheet.** All chrome (header/nav/footer) lives in `/styles.css`. No per-page `<style>` overrides of chrome selectors (gated).
6. **One GA4 ID sitewide: `G-5YTZMH6E01`** (gated). Snippet in `<head>` of every page.
7. **Every page = a folder with `index.html`**, root-relative paths, canonical tag, exactly one `<h1>`, OG tags.
8. Don't invent facts, stats, dates, or names. Placeholders must be flagged.

## Brand rules (verbatim — gated where possible)

- **Mission statement, verbatim where used:** "Our goal is to bring churches and faith-based organizations into shared learning, work, and advocacy — guided by best practices to END homelessness in America." The word **END** is always ALL CAPS where formatting allows.
- **Signature phrase: "Forward Together."** "Building Together" is NOT a brand phrase — never use it.
- **Person-first language always:** "people experiencing homelessness" or "unhoused neighbors." Never "the homeless," "vagrants," "street people."
- **The Church** capitalized = universal body of believers; lowercase "church" = a specific congregation.
- **The HOUSE framework (Hear/Offer/Unite/Strengthen/Expand) was retired June 2026.** Do not reintroduce it. Blog posts are tagged by Type: Cornerstone / Educate / Action / Foundational.
- **Homelessness Sunday is October 11, 2026** (postponed from May 2 — never reference the old date).
- Colors only from the brand tokens in `styles.css` (#469596 teal, #25C1E0 blue, #BEE5EA light blue, #EEAF4F amber, #F9E2C1 cream, #231F20 ink). Light blue is never text on white/cream. Typography: IBM Plex Sans (body/UI), Playfair Display (editorial moments).
- Voice: thoughtful practitioner — calm, measured, invitational, never accusatory. No "simple/easy/just"-style minimizing. Coalition-wide copy stays non-sectarian; Anabaptist framing is blog-only.
- Image alt text: describe what's depicted without editorializing; person-first.

## Key integrations (all external — this site has no backend)

- Newsletter signup: https://mailchi.mp/nfceh/national-faith-coalition-to-end-homelessness
- Homelessness Sunday registration: https://mailchi.mp/nfceh/homelessness-sunday
- Donations: Pushpay via Crosswinds Church (501c3 fiscal sponsor) — link in /donate/
- Store: https://nfceh.printful.me

## Workflows

- **Add a blog post:** copy the cornerstone post's `index.html` → new `blog/<slug>/` folder → update title/meta/canonical/JSON-LD/content → add `.post-card` to `blog/index.html` → `generate-sitemap.py` → `gate-check.py` → commit.
- **Add a page:** folder + `index.html` from an existing page → keep header/footer byte-identical (gated) → sitemap → gates → commit.
- **Push from the Cowork sandbox:** the mounted folder can't hold a working `.git` (lock-file issue) — copy site to a temp dir, init/commit there, push with GIT_ASKPASS. See docs/NFCEH-MIGRATION-PLAYBOOK.md §8.

## Docs

- `docs/NFCEH-MIGRATION-PLAYBOOK.md` — the migration/operations playbook (gates, DNS cutover, launch checklist)
- `docs/nfceh_site_crawl_documentation.md` — what the old Wix site contained (content provenance)
- `TASKS.md` — In flight / Ready to deploy / Done
- `Awaiting-Daniel.md` — decisions waiting on Daniel
