# TAR-06 · Open for All: The Feature Map

**Read [TAR-00](TAR-00-vision-and-requirements.md) first.** This document describes the Open for All door: the version of the app for anyone who lives on rent, whether or not their landlord uses RentOk. It is written as requirements: what the app does for the renter, moment by moment through their renting life. How any of it gets built belongs to engineering documents, not here.

*Last updated 12 August 2026. Owner: Sanchay.*

---

## What this app is

A lifestyle app for everyone who lives on rent. Not a property app with extras: an app for the renting life itself, personalized to the person living it. A student in a PG, a professional in a flat, a couple in a gated society, a family in a rented house. Young India lives on rent, earns on rent, builds its life on rent, and no one has built the app that treats that life as worth designing for.

Renting should be fun, and renting should be rewarding. Rewarding does not mean cashback first: it means the renting life builds something. A record. Credibility. A reputation that opens the next door. Today a tenant who has paid rent on time for three years has nothing to show for it. This app witnesses the renting life, turns it into a record the tenant owns, and makes that record work for them. Think of how Cred took the most boring obligation in personal finance, paying a credit card bill, and made doing it into an identity and a community. Rent is a bigger obligation, more emotional, and completely unwitnessed. We do the same for it, with one deliberate difference: no entry gate, no exclusive club. Everyone starts at zero and builds. The record is the status, and anyone can build one.

And because it is a lifestyle app, it must be useful on ordinary days, not just on rent day. The everyday layer below is not decoration; it is what makes the app part of the renter's life rather than a filing cabinet they visit monthly.

**The standard this door is held to:** if anything makes renting in India harder than it should be, this app is where it gets easier. When someone asks how to make their renting life simpler, the honest answer should be this app. That is the ambition, and it is deliberately never finished. The features below are where we start; the list grows and the workflows sharpen for as long as renting has friction left in it.

## A new standard for renting

Renting already exists. How people rent exists too, and most of it is broken the same way everywhere: nothing is written down, nothing is standard, and nobody trusts anybody. The tenant does not trust the landlord to return the deposit. The landlord does not trust the tenant with the house. Neither trusts the broker. Flatmates move in with strangers and hope. Every one of these is a trust gap, filled today by a leap of faith or a fight.

The cost of that distrust is measurable. India counted over 1.1 crore empty urban homes in its last census, while about 1.9 crore urban households needed a place to live. Those homes stay locked not because nobody wants them, but because their owners fear what happens when the wrong tenant moves in and the law moves slowly. Renting fell from more than half of urban Indian housing in 1961 to barely more than a quarter by 2011. Renting in India has been shrinking for fifty years, and trust is why.

So the pieces in this document are not conveniences. Move-in and move-out records, condition checklists, agreements, police verification, ratings in both directions, the passport: each one closes a specific trust gap, and each one is deliberately fair to both sides. The tenant gets proof they left the room as they found it. The landlord gets proof of who is moving in. Neither side is the villain here, and neither is being protected against the other.

This is the goal behind the goal: a way of renting that is fair, standard, and helpful to everyone involved, practiced first inside this app, until it stops being our process and becomes how renting is done.

## A renter's life, moment by moment

The app is organized the way the renting life is. Five moments. Every feature lives inside one.

---

### 1. Finding the next home

**Browse Properties** is the acquisition engine of this door: real properties, listed and kept current by the people who run them. Each property has its own page: photos, rooms, units and beds, pricing, amenities, reviews. From the page a renter can reserve a room, unit, or bed, pay a token amount, or book a visit: a physical tour, a video call, or a phone call.

There are two ways to browse, and the second is the hero of this app.

**The classic way**: search, filter, compare, shortlist. The marketplace as the world knows it, done well.

**The AI Broker**: a conversation. The renter describes what they need the way they would to a broker in real life: budget, area, when they are moving, what matters to them. The Broker recommends, shows real options as cards inside the chat, answers questions honestly, and hands off into the marketplace flow: view the property, book the visit, reserve, right from the conversation.

The Broker can do everything the classic way can, conversationally, and more, because it remembers everything and compares without effort. Six shortlisted flats are six open tabs for a human; for the Broker they are one question: "which of these has the geyser, gets morning light, and is under my budget?" And what the renter tells it is never wasted: every preference, requirement, and dealbreaker spoken in conversation is captured into the app's memory of that person, so the next search, and the next home after this one, starts already knowing them.

What makes the Broker different from every chat widget ever bolted onto a listing site, and why it is the USP of this door:

- **It works only for the renter.** It is not a salesperson for any property. It recommends what fits, says what is true, and flags what does not fit, even about the properties it shows: the good, the bad, the highlights, the compromises.
- **It knows the market and the area.** What rent really is in that lane, what renters report about water, power, commute, and safety, and what the place is actually like: the landmarks nearby, the kind of community, the properties, businesses, and offices around it. It answers "is this a fair price" and "what is it like to live there" with data, not opinion.
- **It knows the properties.** For RentOk-powered properties it runs on the property's own live data: real pricing, real availability, real amenities. It also understands who a property suits, in general terms, never about any individual: a building of working professionals, a family-dominated society, a student floor. That is how it answers the question no listing site can: "will I fit here?"

No one in the Indian rental marketplace offers this. Listing sites answer interest with a flood of broker calls; our Broker answers with the truth and lets the renter decide.

**Supporting the search**: property reviews and ratings on every listing, each stamped when it comes from a verified stay the system itself witnessed, so real reviews cannot be drowned by fake ones · verified landlord and verified property badges · scam and fake-listing protection · visit notes and side-by-side comparison of shortlisted places. Token payments made through the app to verified-landlord listings are protected: if the listing was fraudulent, the money comes back. For unverified listings the app says plainly that no such protection applies, which is itself a reason for landlords to get verified.

**Searching together.** The household often exists before the home does: three friends decide to live together first, then hunt. The search itself becomes shared, one shortlist, joint visits, a combined budget, the Broker advising the whole group in one conversation. And when they apply, it is a group application: every member's passport goes together, so the landlord evaluates the actual household instead of one known person and two strangers.

**Brokers, but verified.** Renters use brokers, and will keep using them. Rather than pretend otherwise, the app offers the honest version: RentOk-verified brokers, clearly marked as verified, so a renter who wants a human helping them search gets one who has been checked. The renter's passport is what they carry into that conversation, which is the same document the broker would otherwise spend a week collecting. As RentOk's broker app arrives, this becomes the brokers' own home inside the renting ecosystem.

**The application: the Tenancy Passport.** The moment a renter reserves, pays a token, or books a visit, they become a lead for that property, and the property decides. The passport (described fully in moment 4) is what they decide with. The renter builds it once; it attaches to every request automatically. No more sending the same documents over WhatsApp to every landlord, different documents each time. One passport, reusable everywhere, and the renter chooses what each share includes. It also shares outward: with a broker who asks for "your profile" to forward to landlords, or downloaded and sent to any landlord anywhere.

---

### 2. Moving in

**The rent agreement, without the middleman fee.** Brokers and agents charge heavily for what is mostly paperwork. Here the renter creates the agreement themselves, or brings the landlord's draft and completes it: identity verification, drafting, stamping, and signing, one complete workflow inside the app, for a small service fee plus the government's own charges. Verification is not a separate errand; it is the first step of signing, the way it should be. Others offer agreement services; we offer it cheaper, and ours feeds everything else: the finished agreement lands in the vault, its dates set the reminders, and the tenancy it starts feeds the record.

**Signed by everyone it binds.** Agreements in real life are rarely two names. Several tenants sign one agreement; property is often jointly owned, so several landlords sign too; students and young professionals are routinely asked for a guarantor's signature on top. The signing flow carries all of it: any number of tenants, any number of landlords, a guarantor where one is asked for, everyone's status visible, and the agreement complete only when every party has signed. Every signer chooses their method: an OTP-based sign included in the experience, or an Aadhaar-based digital signature as the paid option.

**The agreement, before signing.** The **AI Lawyer** reviews any agreement, self-created or received, and co-living or hostel membership terms count too, since for those renters the clicked T&C is the agreement. An agent that knows the tenancy law that actually applies in that state, flags one-sided clauses in either direction, landlord-sided or tenant-sided, explains every clause in plain words, and answers rights questions any time. It always says which state's law it is applying, and says plainly when it does not know. And when the renter wants a human, they book one: verified expert lawyers, available at any point, to review a draft, advise on a clause, or take a matter further. RentOk's legal services live one tap from the document that needs them.

**The agreement, working for the renter.** An uploaded or created agreement is not just stored, it is read. Landlord details, rent amount, due date, notice period, lock-in, rent escalation steps, end date, and who is responsible for what, the landlord's duties and the tenant's: everything the agreement contains gets extracted and offered back as a ready-made setup. Rent reminders configured, the ledger updating itself on the escalation date, the notice tracker warning when leaving early would forfeit the deposit under lock-in, the vault filled, the landlord line started, without the renter typing any of it twice.

The same reading captures every person the agreement names: co-tenants, dependents, a guarantor, the landlords, with whatever the document carries about them, PAN, Aadhaar, addresses. The uploader confirms what was read, and every co-tenant gets an invite: they arrive to find their place in the tenancy already set up, waiting for their yes, because each person claims and verifies their own entry, their identity is theirs to confirm, not a flatmate's to assert. Re-sending an invite or nudging the one flatmate who never checks their phone is one tap. One document, and the whole household is arranged around its tenancy.

**Terms without paper.** Most renting in India has no agreement at all: cash rent, a register at the PG desk, notice terms that live in memory. The app serves this renter as a first-class citizen, not a fallback. They declare their own terms, rent, due date, deposit paid, notice period, and everything runs off the declarations: reminders, receipts, the ledger, the record. The app is honest that unwritten terms protect nobody when things go wrong, and one tap starts a real agreement whenever they are ready. The paperless renter is the majority, and turning their handshake into paper, gently and on their schedule, is one of the most useful things this app will ever do.

**Verification, the renter's own.** Identity verification and background check, done once, paid once, reusable in the passport across every future application.

**Police verification, on its own.** Not a line item folded into background verification: its own service, because a landlord signing an agreement with a new tenant asks for it almost as often as they ask for the agreement itself. Digital where the state offers it, physically arranged where it does not, the app knows which applies and offers what actually works there. Self-initiated, for the renter and for every family member when a family rents together, done once and carried in the passport rather than arranged fresh, in person, at a station, for every move. And because the two belong together, every agreement completed in the app ends with the same recommendation: get the police verification done now, while the details are fresh. The tool-to-workflow rule, applied to paperwork.

**The move-in record.** The renter walks their space with their camera, and the record scales to what the space is: a whole flat, one room, or a PG bed with a cupboard and a geyser that was already broken. The app extracts everything from the video: what items are there, their condition, the meter reading. The renter confirms the list, adds anything the extraction missed, and the app produces a proper condition report, keeping the video itself as part of the proof. If the landlord participates, both sides sign it: an OTP-based sign included in the experience, or an Aadhaar-based digital signature as a paid option. If the landlord never participates, the report still stands as the renter's own dated, structured proof. Either way it goes into the vault, and it is what makes the deposit conversation at move-out a matter of record instead of memory.

**Money help at move-in**: the move-in lump sum is the hardest cheque of the renting life. Zero-deposit and pay-in-parts offers from partners, matched to the renter's record and credit score. A true-cost calculator so nobody is surprised by deposit plus advance plus brokerage plus movers.

**Getting there**: movers and packers, storage between homes, courier services for what gets sent ahead, all through partners, at partner rates better than walking in alone.

**The society, handled.** In apartment cities the housing society is a gate of its own: agreement copy, police verification, an NOC before the moving truck is allowed in. The verification pack the renter already built shares to the society as easily as to the landlord, and society requirements sit in the move-in flow so nobody discovers them from a security guard on moving day.

---

### 3. Living on rent

The everyday layer. This is where the app earns its place in ordinary life, and where most of its personality lives.

**The money surface.** One connected module, not five features:

- **Rent, handled.** The renter sets up their rent once: landlord details, bank details, PAN or GST where available, amount, due date. Most of it arrives pre-filled from the agreement. The landlord's own details get verified from what the renter provides, without the landlord needing to be involved at all, so payments and receipts rest on checked information rather than typed guesses. Paying happens the renter's way: through the app by card or gateway, through their own UPI app with the app recording it, or on autopay for the renter who never wants to think about it, set up once, cancelled any time. Nobody is forced through our rails to get the benefit of the record.
- **The reminder, automatic.** Rent due dates never depend on memory: the app reminds ahead of every due date, every month, on its own, the same way it already does for bills.
- **The receipt, automatic.** Every recorded payment produces a proper HRA-compliant rent receipt, ready for the office, every month, without asking. Where the landlord has GST, serviced apartments especially, the receipt becomes a proper GST invoice, because that is what the renter's employer needs for reimbursement.
- **Real months, real payments.** Move in on the 17th and the first month pro-rates itself, in everyone's shares. Part-payments, late payments, and late fees where the agreement names them are all recorded as they happened: a ledger that only understands full on-time payments is dishonest by omission.
- **Bills.** Electricity, gas, broadband, DTH, mobile, paid in the app through BBPS, with their own reminders. The bill is usually still in the landlord's name; the app fetches and pays by consumer number regardless of whose name is on it, and records it as the renter's expense, because it is. New bills surface as they generate, and the moment one is recorded in a shared home, splitting it with the flatmates is one suggestion away.
- **Split.** Rent and bills split between flatmates: settled in the app, or paid outside and recorded, with the ledger kept honest either way.
- **Expenses and budget, the full product.** Not a rent-only ledger: a complete expense and budget manager living inside the renting life. The renter sets budgets, records expenses by hand when they want, and expenses record themselves through channels the renter consents to. Splits connect to it, settlements connect to it, rent and bills flow into it on their own. Other apps charge for this; here it comes with the life.

**The document vault.** The renting life generates paper, and the vault keeps it, structured and searchable: the agreement, receipts, the move-in report and its video, identity documents, landlord details, payment history, and anything else the renter chooses to keep there. Everything the app produces lands here on its own, and everything the vault knows about dates becomes a reminder. Nothing expires silently.

**The maintenance log, connected to money and quietly intelligent.** A private, dated record of everything that breaks and every time the landlord was told. Photos before and after, bills attached, descriptions, dates: each entry a small evidence pack of its own, shareable with the landlord as one piece, by hand or automatically. And the app does the noticing: upload a plumber's bill and the AI reads it, records the expense, recognizes it as maintenance, and drafts the log entry. Because the agreement reader already extracted who is responsible for what, the suggestion completes itself: this looks like the landlord's to bear, add it to the ledger against next month's rent? One tap, or ignore it, and ignoring is free. Records win deposit conversations, ledgers keep friendships with landlords civil, and written duties are one more quiet reason the paperless renter eventually wants a real agreement.

**The community: the Flat and Flatmate board.** Where the city's renters already are, but with real identity. People post rooms available and rooms wanted, the way the locality Facebook and WhatsApp groups work today. Members who verify themselves carry a verified tag; unverified members can browse and post, with the difference visible. Members can share their passports with each other, which turns the terrifying stranger-roommate decision into an informed one, and compatibility matching helps people find flatmates whose lives actually fit: schedules, food, guests, cleanliness. Every renter controls what each audience sees: what is public, what peers see, what landlords see. The peer-to-peer marketplace lives here too: the mattress, the fridge, the desk, sold to the next renter in the same locality instead of abandoned.

**Talking, inside the app.** The community only works if its members can actually reach each other: negotiate the price of that fridge, coordinate a flat viewing, get to know a possible flatmate before deciding. In-app messaging carries all of it, which also means nobody has to hand a stranger their phone number just to ask a question. And a community of strangers with messaging needs its plumbing: report, block, and real consequences for members who abuse it, verified or not. A woman evaluating an unknown flatmate must be able to end a conversation and know it stays ended.

**Flatmates rate flatmates.** People who actually lived together leave each other ratings, the signal every future flatmate wishes existed. Shown when someone is weighing a potential flatmate, governed by the same visibility controls as everything else.

**The flat of three bachelors.** Worth naming as a picture, because it is this door's most common real household and its best word-of-mouth story. Three friends rent a flat; the landlord has never heard of us. Inside one flat, the whole everyday layer is at work: a shared budget, rent and bills split three ways, reminders landing before due dates, the chore list rotating, the repair one of them paid for sitting in the ledger against next month's rent. When one moves out, the board finds the replacement, the deposit math settles cleanly, and the new flatmate walks in with a passport the other two have already seen. One flatmate installing the app quietly makes it three people living in it. The machinery underneath this picture, and underneath a family renting the same way, is the shared tenancy, given its own section later in this document.

**Local services.** The renter with no property manager has nobody to call. A curated directory of partnered services fills that gap: cleaning, repairs, maid, cook, tiffin, laundry, doctor visits, couriers, legal help from verified lawyers, and CA and tax help for the renter who files returns: HRA proofs, deductions, the paperwork of a renting life, handled by verified professionals. Everything in this layer is chosen, not scraped; a directory of everyone is a directory of no one.

**Offers.** A separate surface from services, on purpose: services are things you book and someone shows up; offers are deals brands bring to verified renters. Tenant insurance, medical insurance, zero-deposit and pay-in-parts products, brand deals that earn their place. Services must never feel like an ad shelf, and offers never pretend to be anything but offers.

**The to-do list.** Daily chores, errands, the small logistics of a shared flat: a simple, fast list that is always there, with shared lists for flatmates so the gas cylinder actually gets bought. Other apps charge for a good one; here it comes with the life, and it is one more reason the app is opened on an ordinary day.

**Small AI companions.** Light, independent, each one useful alone. The **trip planner**: tell it where you are going, get a plan. The **meal planner**: for the renter who cooks, or keeps a cook, it plans the week's meals and shops the list, shaped to their food, their budget, their household. The **cost-of-living guide**: what it really costs to live in Mumbai, or Gurugram, or Pune, answered for this renter in particular, because the app knows their life well enough to draft the budget for the move. The companion list is meant to grow: each new one is cheap to add, and each is one more ordinary day the app gets opened. The small pleasures that make this a lifestyle app rather than a filing cabinet.

---

### 4. Being known: the Tenancy Passport

The heart of the door. One portable credential that says: this is who I am as a tenant, and here is the proof. It is the renter's own profile, and it grows richer the longer they rent.

**Four layers, clearly labeled, so anyone reading it knows exactly what is verified and what is claimed:**

| Layer | What it holds | How it gets there |
|---|---|---|
| Self-declared | History, employment and education, dependents and family, anything the renter writes in | The renter, any time |
| Witnessed | Payment record, on-time streaks, tenancies completed, condition reports signed | Automatically, from everything the app records |
| Verified | Identity, background check, police verification, employment verification | The renter pays once, reuses everywhere |
| Showcase | LinkedIn, Instagram, X, anything the renter wants a landlord to see | The renter links what they choose, and chooses per share |

The passport shapes itself to the renter. A student's passport leads with education and guardian details; a family's carries its dependents; a professional's carries employment. No two passports look alike, and that is by design. A passport with three months of history is a young passport, not a bad one. Every month of renting adds to it on its own. Each verification shows when it was done, so a landlord reading the passport knows what is current and what has aged out; police verification, for one, expires yearly.

One scoring rule, stated here so it never gets designed wrong: the score reads how someone rented, never how often they moved. A student who changed PGs every semester and paid on time every month is a reliable tenant with normal mobility, not a flight risk. Punishing movement would punish exactly the young renters this app exists for.

Anyone who has ever rented through a RentOk-powered property arrives with theirs already written: the tenancies, the payment record, the reports, waiting for them. Their years of renting well were being witnessed all along, and this is where they collect it. It is the single best reason for someone who has left our properties to come back to us.

**Reputation carries two voices, kept separate on purpose:**

- **What landlords said.** Ratings and feedback from each stay, shown as what they are: one party's view. If a renter disputes one, that conversation is between them and that landlord; the app presents it fairly and without judgment, but the app is not the referee.
- **What was witnessed.** Impartial, factual, machine-kept: rent on time 34 of 36 months, two tenancies completed in full, deposit returned in full, condition reports signed by both sides. Facts, and the tenancy score derived from them. Never opinions, never verdicts, never labels. The facts speak in both directions: they expose a genuinely bad history, and they quietly defend a good tenant against one unfair review.

**The memory, beside the passport.** The app keeps two pictures of the renter, and they are deliberately not the same thing. The **passport proves**: payments, verifications, history, the record a landlord reads. The **memory knows**: tastes, habits, hobbies, dealbreakers, everything gathered from Broker conversations and everything the renter writes about themselves, in as much richness as they want to give, the way a good concierge knows a regular. The memory is private-first: it powers matching, recommendations, and personalization, and none of it reaches a landlord unless the renter puts it there. The showcase bio is the renter choosing what the memory shows to peers, a rich, warm, self-authored introduction for the person deciding whether to live with them, modern the way the best people-meeting apps are, never leaking to the person deciding their application.

**The passport travels.** It attaches automatically to every application inside Browse. It goes to brokers who ask for a profile to forward. And it downloads as a document the renter can send to any landlord anywhere, on RentOk or not, carrying its verification marks and the name of who stands behind them. Every passport shared with a landlord who has never heard of us is a small introduction: this is what a renter looks like when someone has been keeping score. Some of those landlords will be curious enough to ask who was keeping it.

**The score.** The witnessed record rolls up into a tenancy score the renter watches grow: the renting life's answer to a credit score, built by simply living well. Offers get better as it grows. The long-term ambition, stated so it is not lost: rent history this clean should one day count toward actual credit.

---

### 5. Moving on

**The notice, protected.** The vault already knows the notice period and the agreement's end; the app reminds before each is due and drafts the notice letter, ready for the renter to edit, and, since the landlord's details are already saved, ready to send with one tap.

**The next home, offered at the right moment.** As the agreement's end approaches, the app already knows this renter: their preferences from the passport, the kind of home they chose last time. The Broker starts suggesting what their next home could be, and one tap opens the full search. The end of one tenancy flowing into the start of the next is not churn; it is the renting life continuing inside the app, and each move is a chance at a better-run home.

**The move-out record.** The same video walkthrough as move-in, producing the closing condition report, signed by both sides when the landlord participates. Move-in report plus move-out report plus payment history plus maintenance log equals the deposit conversation settled by record.

**Getting the deposit back, the happy path.** The renter's verified bank details are already saved, so requesting the deposit is a stage, not a chase: one tap sends the landlord a proper message, the amount, the account, the settled condition reports behind it. Gentle reminders go from the app until it lands, and the renter marks it received. Most deposits come back this way, and the workflow's job is to keep it that boring.

**When the deposit conversation goes wrong.** The app assembles the evidence in one packet: dated reports, payments, the log of what was reported and when. If it comes to it, legal help through partners, with the packet ready to hand over. The strongest sentence a renter will ever say about this app is "it got my deposit back."

**And the record moves with them.** The tenancy that just ended becomes the newest entry in the passport, and the passport is already attached to the search for the next place.

---

## The landlord line

A named thread running through the whole door, because it is bigger than any one feature.

A renter living in a property that is not on RentOk saves their landlord's details once. From then on, the renter chooses which activities reach the landlord automatically: the move-in report to acknowledge, the logged repair that should be reimbursed, the running ledger of what gets deducted from next month's rent, the move-out report to sign. The landlord starts receiving structured, professional, dated documents from their own tenant, each one carrying our name.

And the renter rates the landlord, whether or not the landlord has ever touched RentOk. Every stay leaves feedback both ways, in every state we operate. A landlord's reputation starts accumulating before they arrive, so the day they do log in, they find a history already waiting, and the renters who come after get what renters have never had: a way to know what a landlord is like before signing.

**Reaching the landlord who never signed up.** The landlord line also speaks to the landlord about the things a landlord cares about. The agreement is about to expire: renew it here, properly, without a broker, and renewal is the easiest sale in the product, the same draft carried forward, the escalation already calculated, both sides reviewing the same document, the stamp purchased in a tap or two. Police verification expires every year: get it done again, from the app, in minutes. The stay has ended: rate your tenant, so your experience counts too. And at renewal time the renter gets the mirror of the landlord's reminder: what rents actually did in that lane this year, so if an increase is proposed, both sides negotiate from the same facts. Each message is useful on its own, each is about their own property and their own tenant, and each gives the landlord one more reason to be curious about what their tenant has been using. Two rules govern this channel. Each side hears what serves them: renters get what helps renters, landlords get what helps landlords, never a cold pitch. And nothing about the renter's private life in the app is ever reported: what a renter browses, plans, or considers is theirs alone. An expiring agreement is a shared fact; a search for the next home is not.

**Refer your landlord.** The one referral this app pays real money for. A renter who brings their landlord onto RentOk's management products has delivered a business customer, and the reward is cash, paid when the landlord becomes a paying customer, not on a signup, which is also what keeps the mechanic honest. (A variant worth testing alongside: rent coins, redeemed against the renter's own monthly rent.) This is not the invite-your-friends mechanic this project removed elsewhere; nobody is farming contacts. It is a fee for the most natural sale in the ecosystem, made by the one person both sides already trust.

Where this leads: when a renter adds landlord details, a landlord profile takes shape in the RentOk ecosystem. The landlord gets a message: your tenant shared this with you, see the full picture here. When they log in with nothing but their phone number, everything already linked to them is waiting: their tenants, their property, the payment history, the reports. From there, the landlord app and the manager app are one step away. RentOk's vision is the whole of renting: single-family homes, multi-tenant buildings, PGs, co-living, hostels, serviced apartments, short stays, commercial property, and the firms that manage all of it. The landlord line is how this door feeds that vision: the tenant builds the landlord's front door without either of them experiencing it as sales.

## The shared tenancy

The second named thread, because the most common door 3 household is not one person: it is three friends in a flat, or a family. One agreement, one home, several people, each with their own login, their own phone number, their own passport, linked together. The tenancy is the shared thing; the identity stays individual.

**Two roles, kept distinct.** A **co-tenant** is a party to the agreement: own login, own rent share, own deposit share, their signature on the document. A **dependent** lives in the home without being a paying party: a child, a parent, sometimes a spouse. Dependents sit on a co-tenant's passport and can have their own login for the household layer, chores, lists, shared visibility, without ever touching the money or the agreement. A family is usually one or two co-tenants plus dependents; a bachelor flat is co-tenants all the way down. Same machinery, different mix.

**What is shared and what is private.** Shared between the members: the agreement, the condition reports, the landlord ledger, the chore lists, the split ledger, the shared budget, the bill reminders. Private to each person: their own passport, their own expenses and personal budget, their own share history, and what they choose to show anyone. The app never merges people into a household blob; it links individuals.

**Shares, not assumptions.** Rent rarely splits evenly, the bigger room pays more, and every recurring expense carries its own participant list and its own shares, defaulting to everyone-equal: rent splits by room, the maid splits three ways, and the flatmate who never eats the tiffin is not in the tiffin split. Without per-expense participants, the first exception breaks the ledger and everyone goes back to WhatsApp math. Fixed recurring costs (rent, maid, wifi) post themselves, and each can carry its payee: the maid's UPI saved once, paid from the app, on autopay if the household wants. Variable ones (electricity, gas, groceries) remind, take the amount, then split.

The rent itself usually leaves as one payment: the landlord quoted one number, one flatmate pays it out, and the ledger's real job is settling the others to whoever fronted it, the same as the fridge and the electricity. Where flatmates pay the landlord separately instead, that works too, it is normal and the ledger simply records it that way. Either way, each co-tenant gets their own HRA-compliant receipt for their own share, because three people each paying ten thousand need three receipts, not one for thirty.

**When one member leaves, the tenancy continues.** The most common shared-tenancy event, handled today entirely on trust, works here as a flow. Anyone can start it, usually the one leaving. The vacancy posts to the Flat and Flatmate board from inside the tenancy, pre-filled: the room, the share, the date. Candidates apply with their passports; the remaining flatmates review together, and only mutual agreement finalizes, consent for people, records for money. The swap then fires its own paperwork: the agreement re-signs with the new party list, which is also where the landlord's own consent lives, police verification starts for the newcomer, and the newcomer records their move-in condition for the room they take over. The outgoing member's deposit share settles person to person, newcomer to leaver, recorded in the ledger, so a year later everyone can prove what happened. Shared assets settle the same way: the fridge bought together stays with whoever keeps it, the buyout on the record, or it goes to the marketplace.

**When everyone leaves,** the deposit returns split by the recorded shares, and each member's passport carries the tenancy out the door.

**Deliberately not a feature:** who talks to the landlord. Flatmates arrange their own spokesperson, and everyone is a party to the agreement anyway, so anyone can step in when someone is unreachable. People solve this with a message today at zero cost; an app feature would be ceremony.

## The mechanics that run through everything

**The tools are the way in.** Several things this app does are useful to a person who has never heard of us: a rent receipt, made properly and ready to file · an agreement checked against the law of their own state · what rent really costs in a lane they are considering · what a city really costs to live in, for someone weighing a move to it · what a move will actually cost, all of it counted · a trip planned · a week of meals planned. Each one works completely on its own, for its own sake, for someone with that problem today. They are how a stranger finds us at the moment they need us, and most renters will meet this app through one of them rather than through a property search.

**The tool ends where the workflow begins.** Every tool works standalone, fully, with no strings: generate one receipt, check one agreement, plan one trip. And at the moment the tool's value has just landed, and only then, the app offers the next step: the receipt is ready, want this automatic every month? The agreement is checked, want it kept in your vault with the notice-period reminder set? One suggestion, at the moment it is obviously useful, never a popup at the door, never twice. That is how tools become workflows and visitors become residents: by being genuinely useful first and quietly ambitious second.

**Login gates the result, never the discovery.** The tools are findable and startable by anyone searching at their moment of need. The finished result is where the account begins. Nothing useful escapes without a login, and nobody hits a wall before they have seen the value.

**Everything feeds the record.** Every payment, report, verification, and completed tenancy makes the passport heavier. Features that add to the record and features that spend it are both welcome; features that do neither must be genuinely delightful to stay.

**The record is owned, and leaving is honest.** The renter can export everything they built and delete their account, and their personal data and passport go with it. What survives deletion is only what was never theirs alone: a condition report both parties signed, a rating a landlord wrote about their own property's stay. The paper agreement does not vanish when one signer burns their copy, and neither do its digital equivalents. Everything one-sided dies with the account; everything bilateral survives for the other party.

**Every artifact carries the name.** The receipt that reaches an employer, the passport that reaches a landlord or a broker, the condition report both parties sign, the ledger entry a landlord receives: each one travels beyond the app and introduces us to someone who never installed anything.

**Personal to the renter.** The student, the professional, the couple, the family: different budgets, different tools up front, different offers, differently shaped passports. Same app, personally arranged. Per TAR-00, offers respect age: minors are never targeted.

**It must never feel like work.** The rule that governs every workflow above: **the app does the noticing, the renter does the deciding.** Pattern recognition drafts the expense, the split, the log entry, the deductibility call, the deposit request; the human taps yes, edits, or ignores, and ignoring is always free. Nothing nags twice. Nothing demands completion. No onboarding checklists, no progress guilt, and no app-generated "pending tasks", the only pending tasks in this product are the ones the renter wrote on their own to-do and chore lists. Every suggestion appears where its value is self-evident and says, elegantly, why it helps; and everything that can be suggested can also be opened at will, so the renter who wants to do a thing right now never has to wait to be offered it. This is a lifestyle app: it should feel rewarding, purposeful, and light, never like Jira wearing a friendly color.

**A note for the designers, as suggestion, not instruction:** rent is monthly, but the money surface and the community are daily and social. Our instinct is that the everyday layers lead the experience and the monthly layers sit one step in, but every renter's rhythm differs, and the home experience is the design team's call.

## How this door earns

Three layers, in the order they unlock. The full strategy gets its own document; this is the shape.

1. **Transactions**: service fees on agreements, verification, signing, bookings, and margins on bill payments and services.
2. **The offers economy**: brands paying to reach verified renters through the offers surface, the way Cred's store monetized a community built on trust.
3. **The record itself**: lending and financing partners underwriting renters through their rent history. Zero-deposit moves, pay-in-parts, micro-finance for the renter who has no credit history but has eighteen months of on-time rent. This is the biggest layer and the slowest, and it carries one rule that is also the business model: **the record works for the renter, never against them.** Data reaches a partner when the renter asks for a product and shares it, the same per-share choice the passport has everywhere. The moment renters believe their record can quietly hurt them, they stop feeding it, and the record is the asset. Consent is not the compliance cost of this model; it is what keeps the asset growing.

## Deferred, and what revives each

| Deferred | Revived by |
|---|---|
| Polls | A door 1 and door 2 feature first; this door borrows it later if its community wants it |
| Event planner | Same: proven in doors 1 and 2 before it earns a place here |
| Internships and jobs board | An open question from stakeholder review; parked until the need it serves is clearer |
| Company-leased homes (employer rents, employee lives) | A real archetype, but a business-to-business sales motion; revived when that motion exists |
| Reporting rent history to credit bureaus | The witnessed record reaching real volume |
| Rent as a payable inside every bank's bill-pay app | Bill-payment volume justifying the registration |
| Electricity overcharge detection | Area intelligence learning real tariffs from renters themselves |
| Room handover matching, outgoing renter to incoming | Community density making matches likely |

## Not building, and why

| Not building | Why |
|---|---|
| Utility connection transfers | Government workflows differ by state and utility; partners in the services directory can serve this. |
| A safety and SOS layer | A half-built safety feature is a liability. Phones and dedicated apps do this properly. |
| Broker fee blacklists | Naming individuals invites legal exposure; reviews of properties and verified-broker tags carry the honest part. |
| A parent window | Belongs to the RentOk and white-label doors, where the property relationship exists. This door is the renter's own. |
| Subletting workflows | The AI Lawyer answers the legality question; a workflow would help people breach their own agreements. |

## Why this holds together

One loop, running through all five moments: the app is useful enough to live in, living in it builds a record, the record opens the next door, and the next door was found in the app. Browse brings renters in, the everyday layer keeps them, the passport makes leaving costly in the only honest way: not by locking anything, but by having witnessed a life no other app can vouch for. And through the landlord line, every renter quietly brings their landlord to ours.

Underneath the loop sits the larger bet. Rent this way at enough scale and it stops being an app's process and becomes the standard: the trust deficit closes gap by gap, locked homes open, and renting becomes what it should have been all along, fair, trustworthy, and rewarding for everyone in it. That is what solving renting means, and it is solved the way anything real is solved: slowly, one closed gap at a time.
