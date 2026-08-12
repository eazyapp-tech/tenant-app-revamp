# TAR-00 · Vision and Requirements

**The one document to read first.** Everything we have decided about the new tenant app lives here: what we are building, why, for whom, and the promises we have made to ourselves. Every other document in this repo hangs off this one.

*Last updated 12 August 2026. Owner: Sanchay. Status: living document, updated as decisions land.*

---

## What we are building, in one line

A tenant app so good that a tenant hesitates to move into a property that does not have it.

Not a better version of today's app. A new app, imagined from scratch, that becomes the industry's reference for what living in a rented home should feel like on a phone.

---

## Why we are doing this

**Today's app has not earned a place in tenants' lives.** Field visits found properties where complaints still go in a paper register and most tenants never installed the app. The tenants who do install it open it once or twice a month. Day-to-day communication happens on WhatsApp, because WhatsApp is easier and the app gave people no reason to switch.

**We plan to charge for this app.** The goal is a platform fee in the range of Rs 30 to 50 per tenant per month. Nobody pays a monthly fee for an app they open twice a month out of duty. The app has to become something tenants rely on daily and would miss if it disappeared.

**The same app opens three doors.**

1. **RentOk Tenant App.** The standard app for every tenant whose property runs on RentOk.
2. **White-label apps.** Property brands buy their own version: their name, their logo, their colors, on the App Store and Play Store. Big clients are waiting for this before they onboard their tenants.
3. **Open for all.** A version any tenant in India can use, even if their landlord has never heard of RentOk: rent agreements, rent receipts for tax, deposit protection, paying rent by card, help when relocating. This door is where paid tenant services live, and it only works if the core app is genuinely loved.

A weak core makes all three doors weak. A strong core multiplies through all three.

**The destination is dependence, not downloads.** When tenants start asking "does this property have the app?" before moving in, the value chain reverses: tenant demand starts pulling property owners onto RentOk, instead of owners pushing the app onto tenants. That is the end state every decision should serve.

---

## How we will build it

**This is a fresh build, not a renovation.** The current app keeps running in production, untouched, serving tenants as it does today. The new app is designed and built alongside it, with its own service layer. When the new app is ready, tenants migrate over.

This changes what we are allowed to imagine. Earlier we treated the backend as frozen and designed around its limits. That limit is gone. If the new app needs the backend to know a property's type, a tenant's age, or which offers are live in Pune, we build that. The property and tenant records the business already holds remain the source of data. The new app gets whatever services it needs on top of them.

**The data is already there.** The manager app already records what kind of property it is, who it serves, and what kind of tenants the owner wants. The new app's personalization runs on records the business already keeps. Where a signal is missing, we start capturing it: collecting new data points is allowed and expected. The data stays; the machinery around it is new.

**The current app is a first draft, not a boundary.** We reuse an idea from it only when that idea wins on its own merits. Nothing is kept out of habit. A separate engineering document records the current app's known defects so this document does not have to dwell on them. Things like money always formatted correctly, receipts always arriving, and text never getting cut off are grammar: the basics any new design speaks natively. They are not features and we do not celebrate them.

---

## Who we are building for

Seven kinds of tenants came out of our research: hostel and PG students, working professionals, families in flats, migrant and blue-collar workers, tenants whose company pays their rent, short-term tenants, and long-term settled tenants. For design we group them by what they need, and we call each group a register: not a fixed box, just the mode of life that shapes what a tenant needs from the app this month. One person can move between registers as their life changes.

| Register | Daily reality | The app's job for them |
|---|---|---|
| **The daily-loop tenant** (students, hostel residents) | Food, attendance, gate timings, every day | Be the rhythm of their day |
| **The monthly-loop tenant** (working professionals) | Rent, receipts, a booking or complaint now and then | Be effortless and trustworthy once a month |
| **The document-heavy tenant** (families, settled tenants) | Agreements, verification, deposits, move-out | Be the safe place their paperwork lives |
| **The cash-first tenant** (migrant and blue-collar workers) | Cash payments, WhatsApp, budget phones | Be simple, dignified, and never assume |
| **The sponsored tenant** (company pays) | Never sees a due | Show them their home, never nag about money |

Two more audiences matter as much as tenants:

- **Parents and guardians.** For student tenants, the parent often pays the rent and always worries. They are a real user and possibly a paying one. The app should have an answer for them.
- **Property owners and managers.** They are the distribution channel: our field interviews say tenants install the app when the owner pushes it, and rarely otherwise. It is the strongest signal in the research, and the research kit still tests it directly. They are also the white-label buyer. Owner pride, "this is my property's app," is a feature.

**The ceiling and the floor.** The app must delight a design-literate professional in a Bengaluru co-living and remain fully usable for a migrant worker on a budget phone in daylight. Sophistication reveals itself as someone engages. Nothing basic ever hides behind novelty, and there is never a stripped-down "simple mode", which is only a polite insult.

---

## Personalization: one app that feels personal to every tenant

The same app should feel meaningfully different for different tenants, without building a separate app for anyone. Four things shape what a tenant sees:

1. **Who they are.** Student, professional, family, and so on, read from their own profile. This changes tone, greeting, and what comes first, never what exists.
2. **Where they live.** City and state shape offers, services, and local content. A Goa tenant and a Pune tenant should not see identical, irrelevant catalogs.
3. **What kind of property it is.** PG, co-living, hostel, family flat; boys, girls, co-ed. The property's real attributes now flow to the app, so a student PG's app and a family flat's app genuinely differ.
4. **How old they are.** Underage tenants and adult tenants see different offers and content. This is also the law: Indian data protection rules prohibit targeted advertising and behavioral tracking aimed at minors. Below 18, profiling switches off entirely and the app falls back to a safe, curated set. Age changes what content appears. It never changes what the app can do.

**The line we never cross:** personalization keys on what a tenant needs, never on clichés about who they are. No "girls PG gets pink." Which offers appear in which city for which age is a targeting system with rules, not a stereotype with a paintbrush.

And one brand rule: **the property's logo and name lead the app, not RentOk's.** The app should feel like it belongs to the place the tenant lives.

---

## What the app contains

**The ten core sections** (fixed scope, from Srijan): Theme, Sign-up and Intro, Home, Feature navigation, Profile, Accounts and money, Complaints, Messaging, Rewards, Reviews. Two notes: Messaging means showing the property's existing WhatsApp conversation inside the app, not building a new chat. Reviews means bringing the survey system that already runs over WhatsApp into the app.

**Two promotions we made:** Food and Attendance join the core set. They are the daily habits that bring students back every day, and daily habit is what adoption is made of.

**The flexible list** (validated with tenants before building, via the research kit): polls, community, event planner, expense splitting, buy-and-sell between tenants, browsing properties in the same brand, meal planner, to-do lists, jobs and internships. Our starting bets from this list: polls and expense splitting, because they are naturally multiplayer, and a tenant pulls their floormates in just by using them.

**Open-for-all services** (the third door): rent agreement creation, rent receipts for tax proof, deposit protection with timestamped evidence, credit-card rent payment, movers and packers, insurance, doctor on call, legal help for deposit disputes.

**Our own additions to test:** rent payments building a credit score, a "tenancy passport" of verified identity and rent history that travels between properties, and a parent window for the student register.

**The horizon** (designed for now, built later): smart locks and door unlock from the app, deeper meter and utility integrations, weather and daily-life helpers, AI products like an agreement explainer that answers "what does this clause mean", and the portable rental identity above.

---

## The promises we have made to ourselves

1. **Benchmark, not just good.** The bar is the apps young India loves: the ones that made boring financial products feel worth showing off. Rent is the most boring product of all. Nobody has done for renting what those apps did for money. We will.
2. **Belonging first, utility always.** WhatsApp already does utility. The one thing WhatsApp can never be is the app of the place you live: your building's name, tonight's dinner, your rent record, your streak. Belonging keeps the app installed; utility makes it trusted.
3. **Every tenant is a channel.** The app spreads three ways: to floormates through features that work better together, to friends through screenshots worth sharing, and to the tenant's own landlord through "why doesn't our building have this?" We design all three paths on purpose. And we never buy sharing with nagging: no share-to-unlock, ever.
4. **Celebrate the rent, respect the receipt.** Rent paid is the emotional peak of the month and deserves a designed moment. The receipt is a legal document a tenant genuinely needs, for tax, for verification, for proof of address, and it should be beautiful enough to send. But rent is an obligation, sometimes paid late with borrowed money: there is never a slot machine after it.
5. **The moments that must be unforgettable:** the first open, where the property's own logo appears; joining a property, which should feel like being welcomed home rather than filing paperwork; paying rent; signing the agreement with a plain-language explainer beside it; filing a complaint by simply describing the problem in chat; marking attendance and being acknowledged as a person, not logged as an entry; and moving out, with the deposit's journey visible until the refund lands.
6. **AI where a conversation beats a form, never where a glance beats a conversation.** Complaints filed by chatting. Agreements explained on demand. But nobody should ever have to ask a chatbot what their balance is.
7. **Identity lives everywhere except color.** White-label clients replace our palette with theirs. So our identity is carried by typography, motion, layout, voice, and the shape of our moments, the things no repainting can remove. One typeface, chosen for real Indian-language coverage, ships inside the app for every client.
8. **The floor is dignified.** Budget phones, bright daylight, limited English, expensive data. The app respects all four without ever announcing that it is doing so.

---

## What success looks like

In order; the first gates the rest.

1. **Adoption.** Installs and monthly active tenants at pilot properties, measured against a baseline we record in the first month. The long-range reading: tenants naming the app as a reason to choose or stay in a property.
2. **Chargeable value.** The app earns the platform-fee conversation with real owners.
3. **Owner pride.** Owners showing the app to prospective tenants unprompted. Measured through owner-driven installs: move-in QR scans and owner-sent invites.
4. **Craft recognition.** The app becomes a sales asset and a reference other teams cite.

Guardrail: first-run completion. Today's app loses people in their first minutes, and no amount of beauty later survives a broken welcome.

---

## What we will not do

- Nothing is ever naked compliance: every feature that asks something of a tenant visibly gives something back, or the ask stays plain and honest. How each feature earns its place: [TAR-05](TAR-05-how-features-earn-their-place.md).
- No feature locked behind sharing or referrals.
- No behavioral targeting of minors, anywhere, in any form.
- No stereotype personalization.
- No prize wheel attached to rent.
- No "simple mode."
- No design decision that depends on a specific brand color, because every client can change ours.
- No shipping a beautiful app on top of a broken welcome, a lying badge, or a receipt that does not arrive. Grammar first, always.

---

## Where everything else lives

| Document | What it holds |
|---|---|
| [TAR-01 Brief](TAR-01-brief.md) | The full product bet in detail, wave-by-wave build order |
| [TAR-02 Design Language](TAR-02-design-language.md) | Type, color, motion, surfaces, the laws of how it all looks and moves |
| [TAR-03 What Each Part Must Become](TAR-03-what-each-part-must-become.md) | Module by module: the ambition, what the first draft taught us, what to validate |
| [TAR-04 Research Kit](TAR-04-research-kit.md) | Interview guides and concept tests for tenants, owners, and the internal team |
| [TAR-05 How Features Earn Their Place](TAR-05-how-features-earn-their-place.md) | How every feature wins the tenant's willing participation: the exchange rule, framings, gamification ethics |
| [Current App Feature Map](current-app-feature-map.md) | Everything the existing app does today |
| [Backend Requirements Ledger](backend-asks-ledger.md) | What the new service layer must provide, gathered as design surfaces it |
| `research/` | The studies behind the decisions: reference-app teardowns, typeface and color research, craft audits |
| `engineering/` | Technical material for the engineering team, including the current app's defect register |

## Open decisions

- The design language's name. Needs the stakeholder group; parked deliberately.
- Whether the current production app receives small safety fixes in parallel. Recommended yes; needs a capacity call.
