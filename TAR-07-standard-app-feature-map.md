# TAR-07 · The RentOk Tenant App: The Feature Map

**Read [TAR-00](TAR-00-vision-and-requirements.md) first.** This document is the feature map for the first door: the standard RentOk tenant app, for every tenant whose property runs on RentOk. It decides what exists in this door, where each feature lives in a tenant's life, and why. It is the sibling of [TAR-06](TAR-06-open-for-all-feature-map.md), which maps the open-for-all door. [TAR-03](TAR-03-what-each-part-must-become.md) says what each module must become in depth; this document decides the portfolio: what exists, where it lives, and how it all holds together.

*Last updated 13 August 2026. Owner: Sanchay. Register: plain language, requirements only.*

---

## What this door is

This is the app a tenant gets when their home runs on RentOk. The property is present in every workflow. The manager app is the other half of most of them. The owner is the channel: the app usually arrives in a tenant's life because the property hands it to them.

Three commitments shape everything below.

**One app, one journey.** Renting today is scattered across separate surfaces: a marketplace website, a joining flow, a web check-in, a payment page, an app. In the new world, one app carries the complete journey, from searching for a home to leaving it, with no dependency on any other product. Each web journey continues to stand alone for people who never install the app, and the app and the web are two renderings of the same journey: whatever a tenant did on the web is simply there when they open the app. Nothing is ever entered twice.

**Doors connect without a break.** A renter in the open-for-all door who books a RentOk property walks straight into this door with their profile, documents, and history intact. A tenant here who moves to a property on a branded app walks into that brand's door the same way. A tenant leaving RentOk properties altogether carries their record into the open door. Every transition in, out, and between doors is one continuous experience. The single deliberate exception is listed in open decisions.

**As rich as the open door, or richer.** The open-for-all door set a bar for feature richness and care. This door is held to the same bar. Nothing here is a lesser version because the tenant is already a customer. They are the customer we most need to delight, because we plan to charge them a monthly platform fee, and nobody pays a fee for an app they open out of duty.

## The spine

Remove any of these five and this door stops making sense. Everything else strengthens them.

**Welcome → Rhythm → Proof → Heard → Record.**

The owner hands the app to the tenant at move-in, and the welcome decides whether it gets installed and kept. The daily rhythm of the home, food, presence, the people on your floor, makes it a habit. The money surface, one clear answer to what do I owe, is it paid, can I prove it, makes it trusted. Complaints that get heard and fixed make it the way things get done. And everything a tenant does quietly accumulates into their record, the reliability story that becomes the tenancy passport and travels with them for life. The record is the bridge between this door and the open one: what a tenant builds here by living well becomes an asset they own everywhere.

---

## A tenant's life, moment by moment

### 1. Before day one

The relationship starts before move-in day, often before the app is installed, on a phone browser.

**Finding this home.** A renter reaches a property through the brand's own website, through RentOk's marketplace, through the open door's search, or because an owner shared a link. However they arrive, the journey from interest to key is one flow:

- **Who are you.** A light persona step early on, so the journey speaks to a student, a professional, a family, or a group correctly from the first screen. This is also the moment the renter's record begins, before any tenancy exists.
- **See the place.** Listing, rooms, sharing options, rent and terms, photos and video, location and commute. Honest and complete.
- **Visit.** Book a visit with a type, date, and time. Directions, what to bring, who to ask for, and a short list of things worth checking while there, because a renter who inspects well is a renter protected well. Visits can be rescheduled or cancelled without penalty games.
- **Reserve.** A token amount holds the room. The receipt is immediate and the terms of the token are stated in plain words before paying, including exactly what happens if plans change.
- **The joining profile.** Name, details, documents, uploaded once into the renter's own account. A booking can also be modified: change the room, shift the move-in date, or cancel, each with its consequences stated up front.

**Web check-in: arrive with the paperwork already done.** Between booking and move-in day, the tenant completes check-in from any browser:

1. Identity verification through eKYC.
2. Profile completion.
3. The renting terms, reviewed in plain words: rent, deposit, notice period, lock-in, house rules, and the property's deposit deduction rules. The deduction rules are shown here, on day minus-three, not discovered at move-out. This single choice kills India's worst renting dispute at its root: there are no surprise rules at the exit because every rule was visible at the entrance.
4. The agreement, previewed and signed. Every person named in it signs their own part (see The shared tenancy below).
5. Autopay setup, where the property offers it.
6. The move-in checklist, begun before arrival where the property prefers it.

The property controls the order and which steps are required. Steps that are not legally required at that moment can be finished later; the app states the consequence of skipping plainly and never bluffs. A tenant who does none of this online is caught by the same steps in the app on day one, with the manager able to assist.

**Groups.** Where a group of friends joins a property together, the group applies together: one home, several people, one shared application, each person with their own entry. Group search across many properties at once belongs to the branded and open doors; here, a group that has chosen this property joins it as a group.

**The lead who never moves in** keeps their profile in their own RentOk account, positioned honestly: your renting profile, saved for your next search, deletable in one tap. Their next search may be the open door. Sensitive documents expire from our side on a stated schedule; the person, and the relationship, are what we keep.

### 2. Day one

**The handover is part of the product.** The owner or manager hands the tenant the app through a designed artifact: a join code or poster in the property's own identity, presented at move-in. The manager sees who joined. For a tenant who checked in on the web, this is a ten-second step.

**The first open is a welcome, not a form.** The property's own name and logo lead. Everything done before day one is already there. What remains is warm, guided, skippable where the law allows, and clear about why each permission is asked. The first minutes decide adoption, so nothing stands in front of the welcome: no walls, no forced setup, no dead ends.

**The move-in record.** On day one the tenant walks their room with the camera: a short video, items confirmed against what the property says is in the room, condition noted, both sides sign. It is framed as what it is, the tenant's protection: these timestamped images are what make an unfair deduction impossible, and they are half of the deposit journey that ends on the last day.

**Meeting the home.** The app introduces the place, not itself: tonight's dinner if there is a mess, the gate hours if there are gate hours, who to call when something breaks, the people layer if the property has switched it on. The directory (below) makes the building's humans findable from the first evening.

**A manager-assisted path** exists for every step of joining: the manager fills, the tenant confirms with an OTP, and the record produced is identical. A tenant helped through joining is never second-class in the data.

### 3. Every day

**The home screen answers one glance:** is anything wrong, and what is next. A thin live strip carries what is happening right now: the meal being served, the gate closing soon, a poll ending tonight. Below it, sections chosen and ordered for this tenant: a student's evening is food and the gate, a professional's month is rent and receipts, a sponsored tenant sees their home and never a due that is not theirs to pay. The composition comes from who the tenant is, where they live, what the property is, and what the property has switched on.

**Food.** The most checked screen of the day where a mess exists. Tonight's menu presented with appetite and honest timing. Confirming meals framed as choosing dinner, never as reporting attendance, with the communal count that makes a mess feel like a shared table. A live-meal moment with a QR plate check-in. Ratings that visibly reach the kitchen, and a kitchen that visibly answers. And the vote: menu polls that let residents shape next week's menu, the single feature where community and food feed each other daily.

**Presence, told as one story.** Attendance and entry-exit are one experience for the tenant: show up, get seen. Marking returns a human acknowledgment, not a log entry. History fills a calendar that feels like a streak, kept with quiet pride, broken with mercy, mended within reason. Setup is warm, guided, and clear about why each permission is asked.

The tenant's side of the watching features is the tenant's own record: their presence history, their gate passes, their late-entry request (with the option to inform family), their guest and visitor pre-approvals, and the property's curfew rules stated plainly. The transparency rule from [TAR-05](TAR-05-how-features-earn-their-place.md) binds here hardest: the tenant sees exactly what the property sees, always. Where the property archetype changes, the meaning changes with it: in a senior residence or an institute hostel, presence read by a linked family member is not surveillance, it is the point (see The Family Window).

Every feature in this section is a burden feature by TAR-05's definition, and every one carries its visible trade on the same screen. The framing library there governs the words.

**The directory: the building's people, organized by need.** Not an organization chart. Something broke: who fixes it. Late at night: the warden. Money: the manager, the owner. A parcel: reception. My home: my roommates and flatmates (opt-in, names first, more by mutual consent), my co-tenants and dependents, the property team with their roles, the owner's details. Calls and messages route through the app, so staff personal numbers stay private, which protects the staff as much as the tenants.

### 4. Every month

**The money surface is the most trusted screen in the tenant's phone.** One clear answer: what do I owe, is it paid, can I prove it.

- **Dues, itemized by name.** Rent, food, maintenance, laundry, electricity, whatever this property charges, each a named component, never one grey number. In a shared home, each person sees their own share and the whole picture.
- **Paying.** Every rail the tenant actually uses: UPI apps, cards, netbanking, autopay, and cash. Cash is handed over against an OTP or the property's payment QR and earns the identical receipt, the identical record entry, and the identical streak credit as any digital payment. Paying in cash is a payment, not a confession.
- **Autopay, native.** Its state, next date, and amount visible in the app, changeable and pausable without hunting through an external portal.
- **The receipt is a document worth keeping.** Tax-ready, address-proof-ready, beautiful enough to send, generated for every payment including cash, and per person in a shared home so each flatmate holds their own housing-rent proof.
- **Bills, in the same place.** Electricity, wifi, DTH, recharges: the household's other payments live beside the rent, which gives every register, including the family in a flat, a reason to open the app more than once a month.
- **The streak grows.** Months paid on time accumulate visibly into the tenant's record. Reminders are written as a helpful friend who assumes you intend to pay, never as a collection agency.
- **The deposit is never invisible.** Where it sits, what rules govern it (known since before day one), and what will happen to it at the end.
- **Offers that respect where you live.** Scoped by city, property, register, and age. Where nothing relevant is live, the section shrinks gracefully instead of showing everyone the same national catalog. Below 18, only a curated, age-appropriate set, with all profiling off: that is the law and our standard.

A tenant with more than one RentOk tenancy switches between them in one place.

### 5. When something needs attention

**Complaints are chat-first.** The tenant describes the problem the way they would tell a friend, by tapping a chip or typing a sentence, and the app takes it from there. The confirmation names a human and sets an honest expectation. Progress is visible without asking. The escalation ladder is visible too: who has it now, what happens if it stalls, and the one-tap escalation when it does. A form remains as the fallback, never the front door. History is honest: a reopened problem carries its past, and a tenant burned before is answered with visible action, because trust here decays fast and is rebuilt only by outcomes.

**The shared complaint.** Building-level problems, water, wifi, the lift, become one collective issue that neighbors join instead of fifteen duplicate tickets and fifteen separate silences. Everyone who joined sees the same status, and the fix is announced once to everyone. Filing stays private by default; joining a shared issue is the social act.

**Repairs that cost money carry their money story.** In flats and independent homes: before a repair happens, who pays is already known from the declared terms. If the tenant paid for something that is the property's duty, the reimbursement or rent-adjustment path is visible and trackable. No repair bill ever disappears into a verbal promise.

**Property services** are bookable without a phone call where the property offers them: clear slots, honest cancellation terms, a QR check-in, and ratings that matter. Invisible where the property offers none. And where the property schedules recurring work, housekeeping, deep cleaning, pest control, the tenant sees what is coming to their home and when, read-only and calm: no surprises at the door.

**Messages are the organized memory of everything the property says.** Reminders, notices, announcements, and the property's message history, each item leading somewhere useful when tapped. The property's existing channels keep working; the app is the place where nothing gets lost. Announcements never pose as new when they are not: a signal that lies teaches everyone to ignore it.

**The property listens back.** Quick pulse surveys and ratings at the right moments, inside the app, with visible consequences: you said the water pressure was bad, it was fixed on Tuesday. Feedback that visibly lands is the only kind people keep giving. Where acting on it is not possible, the reason is said. Every answer reaches a person, and the tenant can tell.

### 6. Living together

The floor is the app's unfair advantage: the one thing no messaging app can promise is that everyone in the room actually lives in your building.

- **Community** is the residents' voice, not the property's megaphone. The property speaks in Messages; this space belongs to the tenants. Every member is a verified resident, which is the entire safety model: no strangers, no spam. Lost and found, borrow a ladder, selling a cycle, planning a Sunday. Report and block are built in; the manager is a moderator of last resort; the property can switch the space on or off. It defaults on in PGs, co-livings, hostels, and senior residences, and off in family flats.
- **Polls**, two kinds: property polls (the menu vote, an amenity decision) and resident polls (movie night, the AC temperature). Opt-in and light.
- **Splitting expenses.** Peer money: groceries, the cook, things the property does not bill. The app keeps the ledger and hands off to UPI for settling; it never holds anyone's money. The same ledger continuity carries into shared-tenancy events like a flatmate swap.
- **Buy and sell** between verified residents of the property or brand, with a natural moment at move-out: selling anything before you go?
- **Chores**, as shared rotation lists for groups and shared rooms. Personal to-do lists belong to the tenant alone; the app never generates tasks onto them.
- **Events.** Property-hosted and resident-created with approval: the Diwali dinner, the movie night, the society meet. In senior residences, an events calendar the linked family can see.

Everything here is multiplayer by nature, which makes it the cheapest growth the app has: a tenant pulls their floormates in because the thing does not work alone.

### 7. The record that grows

**Profile is three clean layers.** My home: room, rent, agreement, tenancy facts, the emotional center. My documents: each with an honest status, provided, pending, verified. My account: settings, privacy, data, the Family Window links.

**The document home.** The agreement, readable and explainable: an assistant answers what does this clause actually mean in plain words, any time. Receipts, invoices, verification certificates, the move-in record, all downloadable, all designed like documents worth keeping. Police verification stands here as its own feature, not a buried checkbox: the app does the heavy lifting, explains each step in plain words, and hands the tenant legal safety they did not have to figure out alone. Honest statuses everywhere: a completion meter that lies is worse than none.

**One rewards system, built on the record.** The spine of rewards is the tenant's own reliability: on-time months, kept streaks, verified documents. What the record earns: recognition, scoped offers, and in time a credit story, because rent, paid well, month after month, deserves to count somewhere. There is exactly one such system in the app. Game mechanics follow the bright line in TAR-05: personal streaks with mercy, collective wins, competition only where competition is fun, and never a ranking of people by compliance.

**The record is the tenant's own, and they can see it.** Months on time, verifications, room history, presence summary. What the property contributed to it appears as witnessed facts, never verdicts, and the tenant can see and contest an entry before it can ever travel anywhere. Complaint counts never enter the record: asking for help must never cost a tenant their reputation. How often someone moved never enters it either: the score measures how you rented, never how long you stayed.

**The memory sits beside the record.** A year in this room. The photos of the move-in day. The goodbye artifact when the time comes. Private first, shown to others only by the tenant's own choice, and feeding the passport only by choice.

**The passport accumulates here.** Verified identity, rent history, tenancy facts, gathered as a side effect of simply living well. When this tenant one day moves beyond RentOk properties, the passport is the open door's welcome gift: everything they built travels with them, because it was always theirs.

### 8. When the agreement ends

This moment is a fork, not a farewell, and the app presents staying first.

**The renewal path.** As the end date approaches, the tenant sees it calmly: your agreement ends 30 September. Renewing is one or two taps: the same terms with any agreed escalation shown plainly, both sides review, both sides sign, done. Rate changes are shown as numbers, not surprises. The app helps the tenant act on their own document and never, in any words, suggests leaving. Renewal is the app doing its quiet best work: a yearly moment of dread turned into a two-minute task.

**The leaving path opens only by the tenant's own act.** Notice is raised in the app, honestly and calmly, with the notice period and any lock-in consequences already known from day one. A raised request can be modified, extended, or cancelled.

**The deposit's journey is visible end to end.** Held, inspected, agreed, refunded, with dates at every step. The inspection itemizes against the move-in record and the room's inventory, photo by photo, against deduction rules that have been visible since before day one. Deductions are itemized with evidence or they do not stand. The refund shows a date, and the journey ends only when the money lands. A cash refund is recorded with the same dignity as a transfer. Where the property uses a deposit bond partner, the bond's journey shows in the same place.

**The move-out checklist is the mirror of the move-in record**, and it is framed as what it is: the tenant's protection, completing the story the move-in video began.

**Handover is a designed closure.** The key returns against a confirmation both sides hold. The goodbye includes something worth keeping: the memory of their time in this home, their record ready to travel, and one quiet door: if their next home is not on RentOk, everything they built works in the open app. One mention, at the moment it is true, never twice.

**Group endings** follow the shared-tenancy rules below: a member swap mid-tenancy, or everyone leaving with deposit shares settling person to person.

**Moving within the system is a transfer, not an ending.** A tenant whose job moves them to another city can request a transfer to another property of the same brand, or any RentOk property: their record, documents, and deposit conversation travel with them, and the joining journey replays only what actually changed. The system keeps the tenant; the tenant keeps the record.

---

## The Family Window

Some of the most important people in a tenancy never live in the room: the parent paying a student's rent, the company paying a sponsored tenant's, the adult children of a resident in a senior home. The Family Window is one system for all of them: a linked account with its own login, a scoped view, and payment rails.

**One concept, four relationships.**

| Relationship | Where | What the window is for |
|---|---|---|
| Parent ↔ minor tenant | Institute-partnered hostels and PGs (coaching-town properties, student housing for minors) | Legally required guardianship: consent, fees, safety. The property offers the parent app as part of its service. |
| Parent ↔ adult student | Student PGs and hostels | Peace of mind and fee help, on the tenant's terms |
| Company ↔ sponsored tenant | Corporate housing | Billing to the company, dignity for the tenant, who is never nagged about money that is not theirs to pay |
| Adult child ↔ elderly parent | Senior and assisted living | Care at a distance: wellbeing, visits, payments |

In the senior and minor cases the window is not an add-on but part of what the property sells, which also makes it a first-class selling point of the branded door.

**The link is made properly or not at all.** The tenant starts it themselves: they add their parents' details, both mother and father, with phone numbers and emails. Each parent receives a link, verifies their own identity through eKYC in the same manner as web check-in, and only then can log in to the parent app. A manager can start the same flow from the manager app, and it passes through the identical verification either way. For minors, guardian verification belongs to the agreement itself: a minor's tenancy is signed for by a guardian, so the window begins at signing.

**Who controls the link.** For an adult tenant, the tenant is the gatekeeper: they create, scope, and remove links to their own tenancy. For a minor, the tenant is not the gatekeeper: the property management or the guardian side holds that role, and the tenant can at most request. And wherever the property's Profile Lock is in force, management is the gatekeeper of profile changes generally, and the tenant requests rather than edits.

**What the window shows is a property decision with our suggested defaults.** Whether a linked parent sees dues only, or presence, or complaints, or community, is configured by the property in the manager app's switchboard. We ship suggested defaults per relationship: for a minor, guardianship-appropriate visibility; for an adult tenant, money and documents only until the tenant consents to more; for a senior residence, the wellbeing signal, is my parent okay today, visits, and payments, with the resident's autonomy governing the rest. In every configuration, two lines hold: below 18, profiling is off and content is curated, because that is the law; and the window is never a surveillance tool, because what it may show is always visible to the tenant themselves.

**The payer rails.** Whoever pays through the window, parent or company, gets the payment experience, the receipts, and the platform-fee billing routed to them, without ever taking the tenancy's ownership away from the person who lives there.

---

## The shared tenancy

Homes are shared by flatmates, couples, families, and groups of friends, and the app treats the group as what it is: several full people in one tenancy, never one name and some ghosts.

- **Everyone in the agreement is a person in the app.** Co-tenants and dependents are captured when the manager creates the agreement, each with their own claimable entry: each person logs in with their own phone, finds their entry waiting, verifies their own identity, and signs their own part. Multi-party signing covers co-tenants, guarantors, and guardians. Nobody types anybody in twice, and nobody signs for somebody else.
- **Shares are explicit.** Rent share, deposit share, and each recurring package the property bills (food, maintenance, laundry) are set per person. Each person sees their own numbers; receipts, including housing-rent tax receipts, are per person.
- **One person may pay for everyone**, and the ledger settles the rest to the payer. Separate payments work equally well.
- **A member swap is a first-class flow.** Someone leaves mid-tenancy: the departure is raised, the vacancy is visible to the group, the newcomer joins through the standard joining journey (including their own verification and their own move-in record), the agreement is re-signed by all parties, which is where the property's consent lives, and the departing member's deposit share settles person to person on the ledger. Consent for people, records for money.
- **Everyone leaving** settles deposit by shares. Shared assets bought together, the fridge, the cooler, settle on the same ledger, including a buyout by whoever stays.
- **There is no point-of-contact role.** Every member has full standing. The property talks to the tenancy, not to one designated tenant on behalf of silent others.

---

## The switchboard

Every property composes its tenant app. One system governs what exists in this property's app: each module, feature, and service is a switch the property sets from the manager app, within bounds RentOk defines.

- **The trust floor never switches off.** Money, documents and the agreement, complaints, and the tenant's own profile exist in every property's app, always. An app whose landlord can hide your receipts is not a trustworthy app, and we do not sell one.
- **Everything else is a property choice.** Community, polls, services, events, food, attendance, entry-exit, the Family Window, the renting-life shelf: on, off, or scoped, per property.
- **Watching features bring their transparency with them.** If a property switches on attendance or entry-exit, the tenant's mirror of that data comes with it, not as an option but as part of the feature. There is no configuration in which the property watches and the tenant cannot see.
- **Composition is also personalization.** What a property switches on tells the app what kind of home this is, and the app's tone and ordering follow.
- **The switchboard is the white-label composer.** The branded door is this same system with the brand's voice and bounds.

## The renting-life shelf

Beyond what the property provides, RentOk brings services any tenant needs because they rent: tax and accounting help for housing-rent claims, insurance, credit-score building on rent history, movers and packers, a doctor on call, couriers.

- **Two shelves, never mixed.** Property services (bookable, from your property) and renting-life services (from the RentOk ecosystem) are visually and verbally distinct, each labeled by who provides it. Services are never an ad shelf.
- **The moment does the introducing.** Movers appear in the leaving fork and the arriving moment. Tax help appears at receipt-download season. Insurance appears at move-in. The shelf exists for deliberate browsing; the workflow offers the tool exactly where its value just became real, once, and lets it be ignored for free.
- **The property has a say.** Shelf categories carry sensible defaults set by RentOk and adjustable by the property within bounds.
- **Browsing other properties does not live inside this door.** A tenant's discovery of their next home belongs to the open door, reached by their own deliberate act; the sanctioned in-system move is the transfer flow. Nothing about a tenant's private browsing anywhere is ever reported to their landlord.

---

## How this door earns

**The platform membership.** Every tenant in this door pays a monthly platform fee in the thirty-to-fifty-rupee band, and the fee is designed to feel obviously fair rather than extracted:

- **One flat fee, then zero charges forever.** The fee absorbs payment processing costs on everything: rent, deposits, bills. A tenant never sees a convenience fee, a surcharge, or a per-payment cut. One number a month buys the promise that no other number ever appears.
- **The bundle makes the fee self-evident.** Zero payment charges. The bills hub. The yearly housing-rent tax pack. Rent building a credit story. Member-scoped offers. Any one of these used once a month outweighs the fee.
- **The fee follows the rails.** It bills tenants who transact through the app. A cash-first tenant who only records payments is not charged for rails they never use, and their record grows with full equality regardless.
- **The fee never gates the trust floor.** Receipts, the record, complaints, and documents are free for every tenant forever. A record you must rent back is not yours, and the record's whole promise is that it is the tenant's own.
- **Sponsored tenants' fees ride the company's bill** through the Family Window's payer rails, as do a linked parent's payments where the family chooses.

**The second layer is the offers economy**: partners earning their place in a scoped, city-true, register-true offers surface that shrinks gracefully to zero rather than spamming.

**The third layer is the record itself**, in time: credit and lending partnerships built on verified rent history, governed by the standing guardrail, the record works for the renter, never against them, and moves only with consent.

And one commercial truth shapes everything: this app is part of what the property's subscription buys. Every feature that makes a tenant love the app is also defending the manager-side relationship. Tenant delight is not a cost center in this business; it is the product.

---

## The mechanics that run through everything

- **It must never feel like work.** Required asks are honest, visibly traded (the exchange rule in TAR-05), and never nag twice. Everything optional follows the open door's rule in full: the app notices, the tenant decides, ignoring is always free, and the app never generates pending tasks; a to-do list contains only what the tenant put there.
- **The two channel rules.** The app speaks to two sides of one tenancy. Each side hears what serves them, never a pitch dressed as a notification. And the facts of the tenancy are shared ground while the tenant's private activity in the app is theirs alone: never reported, never summarized, never sold to the other side.
- **The app never suggests leaving.** Renewal, browsing, transfers: every surface near the landlord relationship helps the tenant act on their own decisions and plants none. The open door is reached by the tenant's own hand only.
- **The record is portable across all doors.** A tenant's record and passport belong to the tenant. Leaving a branded property with your record intact is a platform guarantee, not a courtesy.
- **Every artifact carries the name.** Receipts, records, reports: designed, branded by the property where white-labeled, and worth showing to someone.
- **One journey, two renderings.** Web for before the app, app for life; the same steps, the same data, no repetition.
- **Login gates the result, never the discovery.** Browsing, menus, and public information are open; accounts begin where personal value begins.
- **Migration is a second first impression.** Tenants of the current app are the new app's first audience: they arrive with everything already in place, a designed welcome back, and one clear moment of what is new. Nothing is re-entered, and nothing they had is lost.
- **Deletion is honest.** A tenant who deletes their account takes their one-sided data with them. Signed bilateral artifacts, agreements, receipts, survive for the other party, as the law and fairness require.

---

## Deferred, and what revives each

| Deferred | Revives when |
|---|---|
| Jobs and internships board | Partner supply exists and the student registers ask for it in research |
| Group search and shared booking across properties | Lives in the branded and open doors first; returns here if demand appears |
| Anonymous posting in community | Only with research showing need stronger than the safety cost |
| City-level community beyond one property | An open-door decision, not this door's |
| The institute's own window (aggregate, batch-level) | A stakeholder conversation with partnered institutes, plus guardian consent design |
| Smart locks, meters-depth, IoT | The horizon in TAR-00: designed for, built later |
| Trip planner, orchestrated with guest hosting and entry-exit | After the daily-rhythm cluster ships; the open door carries the light version meanwhile |
| Becoming a bill-payments biller directly | After the payments hub earns its place through partners |

## Not building, and why

| Not building | Why |
|---|---|
| Compliance leaderboards ranking tenants | Public grading of private behavior is shame in a game costume |
| Share-to-unlock, referral walls, contact harvesting | Advocacy is a by-product of pride; a toll kills both |
| A browse-other-properties shelf inside this door | The landlord's channel will not advertise his competitors; discovery lives in the open door |
| Tenant activity dashboards for landlords | The two channel rules forbid it; a tenant's app usage is theirs |
| App-generated pending tasks | The app suggests; only the tenant assigns themselves work |
| Money custody in expense splitting | We keep the ledger; banks move the money |
| A point-of-contact role in shared tenancies | Every member is a full person to the property |
| A prize wheel attached to rent | Rent is an obligation met with dignity, not a slot machine |
| A simple mode | A dignified floor for everyone, sophistication that reveals itself, never a stripped-down insult |

## Open decisions

- **Whether the branded door links onward to the open door.** Held open deliberately for the stakeholder group; the record's portability is already guaranteed either way.
- **The institute window** (aggregate visibility for partnered institutes): parked pending institute conversations and guardian-consent design.
- **The exact fee point within the thirty-to-fifty band, and its rollout staging**: a commercial call to be made with real pilot data.
- **Suggested default visibility scopes per Family Window relationship**: drafted with the research round, since the comfort lines belong to tenants and families, not to us.

---

## Why this holds together

The welcome earns the install, because the owner hands over something that honors their property and asks nothing twice. The rhythm earns the habit, because dinner, the gate, and the floor are daily life, and the app is where daily life is easiest. The money earns the trust, because every number is named, every payment has proof, and the deposit is never invisible. Being heard earns the reliance, because problems filed here get fixed here, visibly. And the record earns the future: everything a tenant does while living well accumulates into an asset that is theirs, feeds the fairest rewards we can build, justifies the fee many times over, and one day walks out the door with them, into the open app, where it becomes the product itself.

A tenant who has lived a year inside this door should hesitate to move into any building that does not have it. That is the test every feature above was chosen against.
