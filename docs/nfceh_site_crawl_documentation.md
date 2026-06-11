# nfceh.org — Full Site Crawl Documentation

**Crawled:** June 10, 2026
**Current platform:** Wix (meta-generator: Wix.com Website Builder)
**Canonical domain:** https://www.nfceh.org (nfceh.org redirects to www)
**Purpose:** Complete inventory for rebuilding the site as static HTML hosted on GitHub Pages with NFCEH DNS pointed at the repo.

---

## 1. Site Map (from pages-sitemap.xml, lastmod 2026-05-21)

| URL | Page | Status |
|---|---|---|
| `/` | Home | Live, real content |
| `/about` | About Us | Live, real content |
| `/about/leadership` | Leadership | Live — near-duplicate of /about |
| `/about/participating-churches` | Participating Churches | Live, real content (23 churches) |
| `/homelessness-sunday` | Homelessness Sunday | Live, real content |
| `/join` | Join Us | Live, real content |
| `/donate` | Donate | Live, real content |
| `/learn` | HOUSE Model | Live — mostly images, thin content |
| `/blog` | Blog index | Live — intro copy, **zero posts published** |
| `/news` | Updates | Wix template filler — not real content |
| `/events` | Events | Wix placeholder events ("Event Title", Sep 12) |
| `/collections` | Store collections | Wix store boilerplate, broken/empty |
| `/privacy` | Privacy Policy | **Unedited Wix template** (placeholder text) |
| `/accessibility` | Accessibility Statement | **Unedited Wix template** (placeholder text) |
| `/blank-2` | — | Redirects to /donate |
| `/blank-5` | — | Linked from /about "Join Us" button (likely → /join) |
| `/event-details/event-title[-1,-3]` | Event detail pages | Placeholder events, skip in rebuild |

**Rebuild recommendation:** carry over 8 real pages (Home, About, Leadership, Participating Churches, Homelessness Sunday, Join, Donate, Blog). Drop /news, /events, /collections (Wix filler). Replace /privacy and /accessibility with real written policies (current ones are embarrassing unedited templates — flagged as live-site bugs). Decide whether /learn survives, since the HOUSE model was retired in June 2026.

---

## 2. Global Elements (every page)

### Header / Navigation
- Logo (links to home): "NFCEH Inverted Logo2.png" — inverted logo in header
- Nav structure:
  - **About Us** (/about)
    - Participating Churches (/about/participating-churches)
    - Leadership (/about/leadership)
  - **Homelessness Sunday** (/homelessness-sunday)
  - **Join Us** (/join)
    - Sign Up → https://mailchi.mp/nfceh/national-faith-coalition-to-end-homelessness
  - **Donate** (/donate)
  - **Store** → http://nfceh.printful.me (external, Printful)
- Mobile: hamburger "Menu"/"Close" pattern
- NOTE: /about and /about/leadership use an older/simpler nav variant (Home, About Us, Join Us, Donate) — inconsistency on the live site; standardize in rebuild.

### Footer
- "© 2026 by NFCEH.org All Rights Reserved."
- "Get Our Newsletter" → https://mailchi.mp/nfceh/national-faith-coalition-to-end-homelessness
- Social icons:
  - Instagram: https://www.instagram.com/faithandhomelessness/
  - LinkedIn: https://www.linkedin.com/company/national-faith-coalition-to-end-homelessness/
  - Facebook: https://www.facebook.com/profile.php?id=61576493879847
  - YouTube: https://youtube.com/channel/faithandhomelessness
- Full nav repeated in footer

### Site-wide SEO
- google-site-verification: `iwhAE3uvUFCcR_C_yo3Cd5NP0A_BjSgwMXIBDqV9Qtc`
- og:site_name: NFCEH (home page uses full org name)
- Default og:image (all pages): main logo —
  `https://static.wixstatic.com/media/7c19a7_ccd42cc13f054bff89f77256a0a99337~mv2.png` (2500×1330)
- twitter:card: summary_large_image

---

## 3. Page-by-Page Content

### 3.1 Home (`/`)
**Title:** National Faith Coalition to End Homelessness | Equipping Churches to End Homelessness
**Meta description:** same as title.

**Hero:**
- H2: "Faith Communities, Equipped to End Homelessness"
- Body: "We dream of a coalition of churches and faith-based organizations united in purpose, sharing resources and building power to END homelessness in the United States."
- CTA: "Learn About NFCEH" → /about

**Homelessness Sunday banner:**
- "On October 11, 2026"
- H5: "The Church Unites to End Homelessness."
- CTA: "Learn More" → /homelessness-sunday
- Image: homeless-sunday-home.png

**Statistic section:**
- Image: "Love thy (6).png" (heart/figure graphic)
- Caption (H4): "neighbors experiencing homelessness in 2024" — *(the number itself renders via dynamic counter; ~771,480 per HUD 2024 PIT count — verify before rebuild)*

**"We are at an inflection point" section (H1):**
> Homelessness is rising in nearly every major city and small town in America, becoming one of the defining moral questions of our generation.
>
> Yet while churches remain rich in compassion, they are often poor in coordination. Congregations feed the hungry, shelter families, and fund ministries — but most do so in isolation, unaware that thousands of others are wrestling with the same questions, facing the same barriers, and longing for the same guidance.
>
> Meanwhile, a new generation of Christians is awakening to the call of justice, eager to put their faith into practice. They don't want to just talk about homelessness — they want to do something about it. They just don't know where to start.
>
> That's where the Coalition begins.

- CTA: "Join Us" → /join

**Pathways band:**
- H2: "As we build, we will offer simple pathways for people of faith to grow compassion into action."
- CTA: "Get The Newsletter" → Mailchimp signup

**"Uniting Faith Communities" section (H2):**
> Homelessness in America is not just a housing crisis — it's a spiritual one. Every night, over half a million people sleep without a place to call home. Behind each statistic is a story of displacement, trauma, and hope deferred. And yet, in churches across the country, pews are filled with people who believe in a God who prepares rooms, builds belonging, and restores dignity. What if those two realities met? What if the Church became the most powerful force in ending homelessness — not through charity alone, but through justice, creativity, and unity?

**"The Moment" (H1):** repeats the inflection-point copy above verbatim. *(Duplicate content on live site — consolidate in rebuild.)*

**"Transforming Lives Together" section (H2):**
- Intro: "By mobilizing faith communities, we foster hope and tangible support for those experiencing homelessness."
- CTA: "Show Support" → /donate
- Four cards (H3 + body + link label):
  1. **Education** — "Educational workshops prepare congregations to effectively engage and implement changes within their communities." (Volunteer)
  2. **Community Outreach** — "Community outreach programs create awareness about homelessness, mobilizing action through events and collaboration." (Partner with Us)
  3. **Partnerships** — "Partnerships with local organizations amplify our outreach and initiatives, fostering sustainable solutions." (Share Your Story)
  4. **Support Networks** — "Support networks enable ongoing dialogue, resource sharing, and collective action across faith communities." (Get In Touch)
  *(Card link labels don't match card topics on the live site — likely template remnants; fix in rebuild.)*

### 3.2 About Us (`/about`)
**Title:** About Us | NFCEH Leadership Team

- H2: "Uniting Faith to End Homelessness" / label "Our Journey"
- Image: Light - Big Vertical.jpg (`baac51_037dbf236c3f4e948b88b0618ad53120`)
- Body: "The Coalition to End Homelessness was born from the need for dignity and belonging in our communities. Together, we strive to bring hope and resources to those in need." + "Join Us" link
- Image: Light - Big Horizontal image 4.jpg (`55d98a_aeec24ea4668401a88c440d765e6d22d`)
- H2: "Empowering Communities Together"
- Body: "Our mission is to unite faith-based organizations to tackle homelessness through collective action and advocacy. Together, we will create a world where everyone has a place to call home." + "Support Us" link

**Team (shared with /about/leadership):**
| Name | Role | Location | Photo asset |
|---|---|---|---|
| Kevin Nye | Co-Founder, Director of Narrative Transformation | Minneapolis, MN | Kevin06.jpg (`7c19a7_0616d4b2ade649729d41ef1ee976b563`) |
| Aaron Horner | Co-Founder, Director of Engagement | Castro Valley, CA | Aaron.png (`7c19a7_c4116d41b21a4a489664d7170ffb37b4`) |
| Rashida Tyler | — | NY | Rashida Tyler2.jpeg (`7c19a7_ce31a43620824304924fb78c1ef55354`) |
| Sparrow Etter Carlson | — | Seattle, WA | Sparrow.jpeg (`7c19a7_38ca28d1a0b94a388394399999a7904a`) |
| Daniel Davis | — | Phoenix, AZ — links to [Trinity Mennonite Church](https://www.trinitymennonite.com) | head shot_edited.jpg (`7c19a7_461492d583cd41ec88aade436902be25`) |

- Bottom CTA: "Join Us" → **/blank-5** (broken/orphan link — should be /join)

### 3.3 Leadership (`/about/leadership`)
**Title:** Leadership Team | NFCEH
**Meta description:** "Meet the leaders guiding the National Faith Coalition to End Homelessness and advancing faith-based solutions to homelessness"

Content is essentially identical to /about (same intro sections + same five team members; "Join Us" correctly → /join). **Rebuild decision:** differentiate the two pages or merge — planned site structure has About → Vision / Participating Churches / Leadership.

### 3.4 Participating Churches (`/about/participating-churches`)
**Title:** Churches Helping End Homelessness | NFCEH
**Meta description:** "See churches across the country working together to end homelessness through partnership, housing solutions, and coordinated action."

**Intro (H1: "Participating Faith Communities"):**
> These are the congregations that said yes — to learning, to acting, and to moving forward together.
>
> There is always something meaningful about taking a step forward in faith.
>
> These communities represent different traditions, different regions, and different points in their journey with this work. What they share is a conviction that homelessness is not someone else's problem, and that showing up — alongside other congregations, guided by what actually works — is part of what faithfulness looks like.
>
> We are grateful to be building this with them.

CTA: "Get More Info" → https://mailchi.mp/nfceh/homelessness-sunday

**Church roster (23 listed as of June 10, 2026):**
| Church | Denomination | Location |
|---|---|---|
| The Table MPLS | Nondenominational | Minneapolis, MN |
| The Shepherds House | Nazarene | Mount Vernon, OH |
| Portland Mennonite | Mennonite | Portland, OR |
| Emmaus Church | Converge Baptist | Northfield, MN |
| Trinity Mennonite Church | Mennonite | Phoenix, AZ |
| Crosswinds Church | Nondenominational | Livermore, CA |
| Resonate Atlanta | Nondenominational | Atlanta, GA |
| All Souls | Anglican | Seattle, WA |
| West Richmond | Friends Meeting | Richmond, IN |
| Edgehill UMC | United Methodist | Nashville, TN |
| Sammamish Presbyterian | — | Sammamish, WA |
| Roots Moravian Church | — | St. Paul, MN |
| OKC First | Nondenominational | Oklahoma City, OK |
| Long Beach Christian Fellowship | — | (Long Beach, CA) |
| Heart of the Rockies | Disciples of Christ | Fort Collins, CO |
| Gracepointe | Nondenominational | Nashville, TN |
| Trinity Lutheran | ELCA | Enumclaw, WA |
| Awake Church | Nondenominational | Seattle, WA |
| Caldwell Church | PCUSA | Charlotte, NC |
| Living Water Nazarene | — | San Diego, CA |
| Monroe Covenant Church | Covenant | Monroe, WA |
| Point Loma Community Presbyterian | PCUSA | San Diego, CA |
| All Saints PDX | Episcopal | Portland, OR |

**"What it means to partner." (H2):**
> Every church on this page made the same decision: that the time to start was now, not later. That learning alongside a coalition was better than figuring it out alone. That Homelessness Sunday — October 11, 2026 — was worth showing up for.
>
> If your congregation isn't listed yet, that's an easy thing to change.
>
> When you register your church, you'll receive the full Homelessness Sunday Toolkit — sermon guide, bulletin insert, small group study, social graphics, and explainer video — everything your congregation needs to center this work in a single Sunday of preaching, prayer, and commitment. And you'll join the network: a growing coalition of faith communities that share what's working, learn from each other, and move forward together.
>
> The best time to join was last year. The second best time is now.
>
> Registering your congregation is the beginning, not the finish line. Here's what participating churches are doing together:
>
> **Observing Homelessness Sunday** — On October 11, 2026, hundreds of congregations across the country will center homelessness in their worship through preaching, prayer, and voices with lived experience. Participating churches will do this together — not as isolated acts of compassion, but as a shared national witness.
>
> **Accessing the Toolkit** — (Launching soon!) Every registered church receives practical resources designed to make Homelessness Sunday accessible and meaningful, whether your congregation has been doing this work for years or is just beginning.
>
> **Joining the Coalition** — Registered churches are part of something that extends beyond a single Sunday. As the coalition grows, participating churches will connect with one another, share what they're learning, and help build the kind of coordinated, sustained engagement that actually moves the needle on homelessness.

CTA: "Get More Info" → https://mailchi.mp/nfceh/homelessness-sunday

### 3.5 Homelessness Sunday (`/homelessness-sunday`)
**Title:** Homelessness Sunday | Equip Your Church to Act
**Meta description:** "Equip your church to engage homelessness with wisdom and compassion. Participate in Homelessness Sunday and join a national movement."

**Hero image:** nfceh_facebook_cover2.png (`ae63f0_155c6a4ee4434b828c7545e02925b67e`)

**Scripture (H4):**
> "For you have been a refuge to the poor, a refuge to the needy in their distress, a shelter from the rainstorm and a shade from the heat." ~ Isaiah 25

**Three pillars (H3 cards):**
1. **Call to Action** — "Create a shared national moment that awakens awareness, builds empathy, and catalyzes tangible next steps toward housing justice."
2. **Our Strategy** — "Mobilize 500+ churches in the first year to preach, pray, and act on homelessness on the same day."
3. **Building Networks** — "Participants in National Homelessness Sunday become the foundation of an ongoing coalition — turning our shared moment into a movement"

**"National Homelessness Sunday" (H2):**
> On October 11, 2026, we are calling on congregations across the country to consider together how God invites everyone home—and what it could look like for the church to do the same.
>
> To empower congregations to hear from those closest to the work and to speak with one voice, we are developing a toolkit for churches to use on Oct 11 that will create a cohesive service:
> - Liturgy
> - Sermon Points
> - Worship Music Set
> - Children's curriculum
> - and more

CTAs: "Sign Up" → https://mailchi.mp/nfceh/homelessness-sunday • "Get the Flyer" → `/_files/ugd/ae63f0_0ddc68085bc44ee783fc8b78e2da70aa.pdf` (**download this PDF before leaving Wix**)
Decorative image: mosaic sphere.png (`7c19a7_f42043825e76433daa6429e7575e48b4`)

**"For the Faith Leader" (H2):**
> Your congregation is ready for this. More ready than you might think.
>
> Over the years, we've talked with enough pastors and faith leaders to know that the hesitation usually isn't about whether people care — it's about whether there's a clear, manageable way to engage. Homelessness Sunday is designed with that in mind. It's flexible by design, scalable to your community's size and capacity, and built around resources that do most of the heavy lifting.
>
> One Sunday. One intentional step. And then the door is open.
>
> Here's what participation looks like:
>
> - **Register your congregation.** When you register, you join a national network of faith communities committing to this moment together. You'll receive a toolkit with everything you need: a sermon guide, bulletin inserts, small group discussion materials, and connections to local homelessness response organizations in your region.
> - **Incorporate it your way.** Some congregations will dedicate their entire service to Homelessness Sunday. Others will weave in a single element — a moment of reflection, a bulletin insert, a brief pastoral message. Both matter. The goal isn't uniformity; it's movement.
> - **Connect your congregation to local partners.** One of the most valuable things a faith leader can do is make a warm introduction — between your congregation and the organizations in your community already working to end homelessness. We'll help you find those connections. The local Continuum of Care, the housing program that needs volunteers, the organization with a gap your congregation's skills or resources could fill.
> - **Take the next step together.** Homelessness Sunday is a beginning, not a finish line. After October 11, we'll help you discern what comes next — whether that's ongoing partnership, a new volunteer commitment, a giving focus, or something your congregation is uniquely positioned to offer.
>
> The hardest part is usually the decision to start. Once that's made, the rest tends to follow.

CTAs: Sign Up + Get the Flyer (same links)

**"For the Person in the Pew" (H2):**
> You have more power than you may realize.
>
> Individual church members have started conversations, brought ideas to their leadership, and opened doors that no organization could have opened alone. Sometimes the most important move a congregation makes begins with one person who said, I think we should pay attention to this.
>
> If you've been carrying a concern for your unhoused neighbors and haven't known where to take it, Homelessness Sunday is a real and concrete place to begin.
>
> Here's what you can do:
>
> - **Bring it to your pastor or leadership team.** Share this page. Ask if your congregation would be willing to observe Homelessness Sunday on October 11, 2026. You don't need a formal proposal — a genuine conversation is enough.
> - **Register your congregation yourself.** If you have the standing to do it, you can register your church directly. It takes a few minutes and signals that your community is ready to engage.
> - **Come prepared to listen.** On Homelessness Sunday, your congregation will hear about what homelessness actually looks like in your region and what local organizations are already doing to address it. Showing up with an open mind is the most important thing you can bring.
> - **Share it with someone who should know.** Know a pastor, a deacon, a small group leader, or a faith community in your network? Forward this to them. The coalition grows one connection at a time.
>
> You don't need a title or a committee assignment for this to matter. Faithfulness often begins with a single conversation.

CTAs: "Learn More" → Mailchimp homelessness-sunday + Get the Flyer

**"Partnering Churches" (H2):** first 10 churches from the roster (The Table MPLS through Edgehill UMC).
Decorative image: Love thy (6).png (heart graphic, reused from home).

### 3.6 Join Us (`/join`)
**Title:** Join the Movement to End Homelessness | NFCEH
**Meta description:** "Join churches and individuals working together to end homelessness. Learn, participate, and take action in your community."

**Hero (H3): "Forward Together"**
> We exist to bring faith communities into shared learning, shared work, and shared impact—grounded in what actually works.
>
> Here are ways to participate.

CTA: "Get the Newsletter" → Mailchimp main signup

**Section 1 — Homelessness Sunday** (icon: 3.png `ae63f0_5e254a40a7d44fe9a34f544e81bccde9`):
> H1: Bring your congregation into a shared moment of awareness, prayer, and action.
>
> Homelessness Sunday is an opportunity for churches and faith communities across the country to align around a common purpose—to better understand homelessness, reflect on our calling, and take meaningful steps forward.
>
> You don't have to design this on your own. We provide the framework. You bring your community.

CTA: "Learn more" → /homelessness-sunday

**Section 2 — Newsletter** (icon: 2.png):
> H1: Putting Compassion into Action
>
> Many people of faith question how to have a lasting impact for their unhoused neighbors but don't know how to put that compassion into action.
>
> Our newsletter is how we begin to close that gap.
>
> You'll receive:
> - Practical guidance rooted in real homelessness response systems
> - Stories from churches learning and acting together
> - Clear next steps you can take in your own context
>
> This is not just information. It's practical steps and an invitation a shared learning community. *(sic — typo on live site: "an invitation a shared")*

CTA: "Sign Up" → Mailchimp main signup

**Section 3 — HOUSE model** (icon: 1.png `ae63f0_467d7b067dee4e999a967dbaceab4c56`):
> H2: How can our church actually help end homelessness?
>
> The answer is more complex than most expect—but also more hopeful.
>
> The HOUSE model is a practical framework that helps faith communities move from intention to effective action. It connects what churches are already doing with what actually leads to people being housed.
>
> It's designed to help you:
> - Learn about homelessness– its causes, solutions, and what it's like to experience it
> - Identify where your church can contribute
> - Move from isolated efforts to coordinated impact
>
> As we launch this new movement, we will be adding resources, toolkits, and stories about how to get involved as we go!

CTA: "Explore HOUSE" → /learn
**⚠️ HOUSE was retired June 2026 — this section and /learn should be replaced/rewritten in the rebuild, not carried over.**

### 3.7 Donate (`/donate`)
**Title:** Donate to Help End Homelessness | NFCEH
**Meta description:** "Support coordinated, evidence-based solutions to homelessness. Give to help faith communities work together to end homelessness."

**Full copy (H2: "Make this movement possible!"):**
> Our goal is for all of the resources for National Homelessness Sunday to be free. To produce these resources, and simultaneously build a national coalition to carry the work forward, we are fundraising for $50k for:
>
> - **Non-Profit Infrastructure:** Incorporation, liability insurance, and so much more provide the basic structure needed to do this right
> - **Marketing and Production:** Galvanizing 500 churches and empowering them with resources will be a massive undertaking: print materials, web design, social media, video production, and tabling at key conferences.
> - **Professional, Expert Work:** Our leadership, present and future, is highly experienced and gifted for this work, and we want to honor that with fair compensation. Additionally, we want to include the voices and perspective of those with lived and living experience of homelessness, and pay generously for it.
>
> While we build ourselves up, Crosswinds Church, a community committed to ending homelessness in Livermore CA, has generously offered to be our 501(c)3 sponsor. This means that donations are collected and overseen by their trusted structure, and allocated to the National Coalition. This allows for your donation to be tax-deductible, and also ensures that our finances and oversight are trustworthy even as we build the coalition from the ground up.

**Donate CTA (critical link):**
`https://pushpay.com/g/crosswindschurch?fnd=Iugr2kP1JqqASTsf4RNPRg&fndv=Lock&lang=en&src=pcgl`

### 3.8 Learn / HOUSE (`/learn`)
**Title:** How Churches Can Help the Homeless | The HOUSE Model
**Meta description:** "Explore practical ways churches can help the homeless through learning, partnership, and action grounded in proven homelessness solutions."

- H2: "This is where we are starting"
- Image-driven page: HOUSE title graphic + five banner images with labels: **Hear, Offer, Unite, Strengthen, Expand**
- Assets (prefix `ae63f0_`): NFCEH_HOUSE_Title_v2.png `45e0f5cbcb4a459bb3879079fd42d41f`, H_Hear `81a8e2b0b96447e4b61ec5b1a0e14256`, O_Offer `3e09fc58319047318b730e5a64291583`, U_Unite `a8b4978e918645e597ba4021ff344d88`, S_Strengthen `9031d9d6b9104beeadeca18cdef5227d`, E_Expand `280dde96bf2e48c69854f0437c7346fd`
- **⚠️ HOUSE retired — do not rebuild as-is.** Either repurpose /learn as an education/resources page (matches planned "Love Thy Unhoused Neighbor → Resources/Toolkits" structure) or 301 it.

### 3.9 Blog (`/blog`)
**Title:** Faith and Homelessness | NFCEH Blog
**Meta description:** "Explore how faith communities can help end homelessness through practical guidance, system insights, and proven solutions."

**Intro copy:**
> This blog exists for people of faith curious to learn about homelessness — its causes, solutions, stories of unhoused neighbors, and lessons from communities of faith figuring out how to love their unhoused neighbor.
>
> Homelessness is rising in communities across the country. The need is real. But so is the confusion. Most congregations that want to engage don't know where to start, aren't sure what actually works, or have tried things that didn't go the way they hoped. This blog is an attempt to close that gap — with honest writing, grounded in experience, organized around what faith communities can realistically do.
>
> As we build this resource, you'll find essays, how-to guides, and stories from people doing this work on the ground — organized around the HOUSE pathway: Hear, Offer, Unite, Strengthen, and Expand. It's not a curriculum, and there's no right order. Start wherever you are.

*(⚠️ third paragraph references retired HOUSE pathway — rewrite for rebuild with the simple Type tags: Cornerstone / Educate / Action / Foundational.)*

- Categories: All Posts, "Homeless Sunday" (/blog/categories/homeless-sunday), "Love Thy Unhoused Neighbor" (/blog/categories/love-thy-unhoused-neighbor)
- **No posts published** ("Check back soon"). Header image: Blog header.png (`7c19a7_e11b0ec5987a437c8aa0f86585478272`)
- Cornerstone post "How Faith Communities Can Help End Homelessness" is written and ready — publish at launch of rebuild.

### 3.10 Pages NOT worth rebuilding
- **/news** — Wix template filler (Spotlight/News/Impact/Train/Engage/Support placeholder cards). No real content.
- **/events** — three placeholder "Event Title" events (Thu, Sep 12, Location TBD). Wix Events app, never configured.
- **/collections** — empty Wix Stores collection page (store actually lives at Printful).
- **/privacy** — **unedited Wix legal template** (literally the "how to write a privacy policy" instructional text). Write a real policy for the new site.
- **/accessibility** — **unedited Wix template with bracketed placeholders** ("[enter organization / business name]"). Write a real statement (mention WCAG level, contact).
- **/event-details/*** — placeholders.

---

## 4. Asset Inventory (download from Wix before DNS cutover)

All hosted at `https://static.wixstatic.com/media/...`. Strip Wix transform params (`/v1/...`) to get originals.

| Asset | Wix media ID | Used on |
|---|---|---|
| Main logo (og:image, header on /about) | `7c19a7_ccd42cc13f054bff89f77256a0a99337~mv2.png` | site-wide |
| Inverted header logo (NFCEH Inverted Logo2.png) | (rendered via Wix; export from Wix media manager) | site-wide |
| Love thy (6).png — heart graphic | `7c19a7_ab4cb8f88528469ca0c851084d461f79~mv2.png` | home, homelessness-sunday |
| homeless-sunday-home.png | (export from Wix) | home |
| Light - Big Vertical.jpg | `baac51_037dbf236c3f4e948b88b0618ad53120~mv2.jpg` | about, leadership |
| Light - Big Horizontal image 4.jpg | `55d98a_aeec24ea4668401a88c440d765e6d22d~mv2.jpg` | about, leadership |
| Kevin Nye photo (Kevin06.jpg) | `7c19a7_0616d4b2ade649729d41ef1ee976b563~mv2.jpg` | about, leadership |
| Aaron Horner photo (Aaron.png) | `7c19a7_c4116d41b21a4a489664d7170ffb37b4~mv2.png` | about, leadership |
| Rashida Tyler photo | `7c19a7_ce31a43620824304924fb78c1ef55354~mv2.jpeg` | about, leadership |
| Sparrow Etter Carlson photo | `7c19a7_38ca28d1a0b94a388394399999a7904a~mv2.jpeg` | about, leadership |
| Daniel Davis photo (head shot_edited.jpg) | `7c19a7_461492d583cd41ec88aade436902be25~mv2.jpg` | about, leadership |
| nfceh_facebook_cover2.png (HS hero) | `ae63f0_155c6a4ee4434b828c7545e02925b67e~mv2.png` | homelessness-sunday |
| mosaic sphere.png | `7c19a7_f42043825e76433daa6429e7575e48b4~mv2.png` | homelessness-sunday |
| Join icons 1.png / 2.png / 3.png | `ae63f0_467d7b067dee4e999a967dbaceab4c56`, (2.png export), `ae63f0_5e254a40a7d44fe9a34f544e81bccde9` | join |
| HOUSE graphics (6 files, see §3.8) | `ae63f0_*` | learn (retired) |
| Blog header.png | `7c19a7_e11b0ec5987a437c8aa0f86585478272~mv2.png` | blog |
| **Homelessness Sunday flyer PDF** | `https://www.nfceh.org/_files/ugd/ae63f0_0ddc68085bc44ee783fc8b78e2da70aa.pdf` | homelessness-sunday (2 pages link to it) |

---

## 5. External Links & Integrations

| Integration | URL | Notes |
|---|---|---|
| Newsletter signup (main) | https://mailchi.mp/nfceh/national-faith-coalition-to-end-homelessness | Mailchimp landing page — survives rebuild as-is |
| Homelessness Sunday signup | https://mailchi.mp/nfceh/homelessness-sunday | Mailchimp landing page — church registration |
| Donations | https://pushpay.com/g/crosswindschurch?fnd=Iugr2kP1JqqASTsf4RNPRg&fndv=Lock&lang=en&src=pcgl | Pushpay via Crosswinds (fiscal sponsor) |
| Store | http://nfceh.printful.me | Printful — note **http**, change to https if supported |
| Trinity Mennonite | https://www.trinitymennonite.com | Daniel's bio link |
| Socials | Instagram, LinkedIn, Facebook, YouTube (URLs in §2) | footer |

Because signup, donate, and store are all external, a **static GitHub Pages site loses no functionality** except: Wix blog engine (replace with static posts or a generator), Wix Events (unused), Wix Stores (unused), and the animated stat counter on home (replace with static number or small JS).

---

## 6. Known Issues on Live Site (fix in rebuild, don't replicate)

1. `/about` "Join Us" button → `/blank-5` (broken).
2. `/about` and `/about/leadership` are ~95% duplicates with an inconsistent (older) nav.
3. Home page repeats "The Moment" copy twice.
4. "Transforming Lives Together" card link labels (Volunteer / Partner with Us / Share Your Story / Get In Touch) don't match card content and link nowhere.
5. /privacy and /accessibility are unedited Wix templates.
6. /news, /events, /collections are template filler.
7. /join typo: "an invitation a shared learning community" → "an invitation to a shared learning community."
8. HOUSE model still live on /learn, /join, /blog intro — retired June 2026; replace with current framing.
9. Store link is plain http.
10. YouTube URL format (`youtube.com/channel/faithandhomelessness`) is likely invalid — channel URLs need an ID or @handle; verify.

---

## 7. GitHub Pages Rebuild Checklist

1. **Repo:** create repo (e.g., `nfceh/nfceh.org`), enable GitHub Pages, add `CNAME` file containing `www.nfceh.org`.
2. **DNS (at registrar / current Wix DNS):**
   - `www` CNAME → `<username>.github.io`
   - Apex `nfceh.org` A records → GitHub Pages IPs: 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153 (verify current IPs in GitHub docs)
   - Keep MX/other records if domain email is configured.
   - Enable "Enforce HTTPS" once cert issues.
3. **Before cancelling Wix:** download all §4 assets + the flyer PDF; export any Wix form submissions/contacts; keep google-site-verification meta tag (or re-verify via DNS).
4. **Preserve URLs** for SEO: `/about`, `/about/leadership`, `/about/participating-churches`, `/homelessness-sunday`, `/join`, `/donate`, `/blog`. GitHub Pages = folder-per-page (`/about/index.html`).
5. **Per-page meta:** carry over titles + meta descriptions from §3 (they're decent SEO already); add og: tags with logo image.
6. **Add:** sitemap.xml, robots.txt, 404.html, favicon.
7. **Blog:** static HTML (or Jekyll, native to GitHub Pages) — publish cornerstone post at launch; tag by Type (Cornerstone/Educate/Action/Foundational), not HOUSE.
8. **Replace** HOUSE content per current strategy; write real privacy + accessibility pages.
