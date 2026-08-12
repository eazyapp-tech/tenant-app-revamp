# TAR-06 · Open for All: The Feature Map

**Read [TAR-00](TAR-00-vision-and-requirements.md) first.** This document describes the Open for All door: the version of the app for anyone who lives on rent, whether or not their landlord uses RentOk. It is written as requirements: what the app does for the renter, moment by moment through their renting life. How any of it gets built, and what parts of it already exist inside RentOk's systems, belongs to engineering documents, not here.

*Last updated 12 August 2026. Owner: Sanchay.*

---

## What this app is

A lifestyle app for everyone who lives on rent. Not a property app with extras: an app for the renting life itself, personalized to the person living it. A student in a PG, a professional in a flat, a couple in a gated society, a family in a rented house. Renting is how a huge part of India lives, and no one has built the app that treats that life as worth designing for.

The idea underneath everything: **renting well should count for something.** Today a tenant who has paid rent on time for three years has nothing to show for it. This app witnesses the renting life, turns it into a record the tenant owns, and makes that record open doors. Think of how Cred took the most boring obligation in personal finance, paying a credit card bill, and made doing it into an identity. Rent is a bigger obligation, more emotional, and completely unwitnessed. We do the same for it, with one deliberate difference: no entry gate, no exclusive club. Everyone starts at zero and builds. The record is the status, and anyone can build one.

## A renter's life, moment by moment

The app is organized the way the renting life is. Five moments. Every feature lives inside one.

---

### 1. Finding the next home

**Browse Properties** is the acquisition engine of this door: real properties, listed and kept current by the people who run them. Each property has its own page: photos, rooms, units and beds, pricing, amenities, reviews. From the page a renter can reserve a room, unit, or bed, pay a token amount, or book a visit: a physical tour, a video call, or a phone call.

There are two ways to browse, and the second is the hero of this app.

**The classic way**: search, filter, compare, shortlist. The marketplace as the world knows it, done well.

**The AI Broker**: a conversation. The renter describes what they need the way they would to a broker in real life: budget, area, when they are moving, what matters to them. The Broker recommends, shows real options as cards inside the chat, answers questions honestly, and hands off into the marketplace flow: view the property, book the visit, reserve, right from the conversation.

What makes the Broker different from every chat widget ever bolted onto a listing site, and why it is the USP of this door:

- **It works only for the renter.** It is not a salesperson for any property. It recommends what fits, says what is true, and flags what does not fit, even about the properties it shows.
- **It knows the market.** Area intelligence, what rent really is in that lane, what tenants report about water, power, commute, and safety. It answers "is this a fair price" with data, not opinion.
- **It knows the properties.** Live pricing, real availability, real photos, kept current by the property's own management.

No one in the Indian rental marketplace offers this. Listing sites answer interest with a flood of broker calls; our Broker answers with the truth and lets the renter decide.

**Supporting the search**: property reviews and ratings on every listing · verified landlord and verified property badges · scam and fake-listing protection · visit notes and side-by-side comparison of shortlisted places, so the renter who saw six flats remembers which one had the geyser.

**The application: the Tenancy Passport.** The moment a renter reserves, pays a token, or books a visit, they become a lead for that property, and the property decides. The passport (described fully in moment 4) is what they decide with. The renter builds it once; it attaches to every request automatically. No more sending the same documents over WhatsApp to every landlord, different documents for each one. One passport, reusable everywhere, and the renter chooses what each share includes.

---

### 2. Moving in

**The rent agreement, before signing.** The renter uploads or receives the draft agreement and the **AI Lawyer** reviews it: an agent that knows the tenancy law that actually applies in that state, flags one-sided clauses in either direction, landlord-sided or tenant-sided, explains every clause in plain words, and answers rights questions any time. It always says which state's law it is applying, and says plainly when it does not know.

**Agreement creation**: for renters who need an agreement made, the app creates one, with stamping and signing handled through partners.

**Verification**: identity verification and background check, done once, paid once, reusable in the passport across every future application.

**The move-in record.** The renter walks the room with their camera. The app extracts everything from the video: what items are there, their condition, the meter reading. The renter confirms the list, and the app produces a proper condition report. If the landlord participates, both sides sign it: an OTP-based sign included in the experience, or an Aadhaar-based digital signature as a paid option. If the landlord never participates, the report still stands as the renter's own dated, structured proof. Either way it goes into the vault, and it is what makes the deposit conversation at move-out a matter of record instead of memory.

**Money help at move-in**: the move-in lump sum is the hardest cheque of the renting life. Zero-deposit and pay-in-parts offers from partners, matched to the renter's record and credit score. A true-cost calculator so nobody is surprised by deposit plus advance plus brokerage plus movers.

**Getting there**: movers and packers, storage between homes, through partners.

---

### 3. Living on rent

The everyday layer. This is where the app earns the monthly open, and where most of its personality lives.

**The money surface.** One connected module, not five features:

- **Rent, handled.** The renter sets up their rent once: landlord details, bank details, GST if any, amount, due date. The app reminds on time, every month. Paying happens the renter's way: through the app by card or gateway, or through their own UPI app, with the app recording the payment either way. Nobody is forced through our rails to get the benefit of the record.
- **The receipt, automatic.** Every recorded payment produces a proper HRA-compliant rent receipt, ready for the office, every month, without asking.
- **Bills.** Electricity, gas, broadband, DTH, mobile, paid in the app through BBPS.
- **Split.** Rent and bills split between flatmates, settled in the app or recorded from outside it, with the ledger kept honest either way.
- **Expenses and budget.** Everything above records itself, so the expense tracker fills in as a byproduct of living, not as homework. On top of it: a budget for the renting life, personalized by what kind of renter this is. Other apps charge for this; here it comes with the life.

**The document vault.** The renting life generates paper, and the vault keeps it: the agreement, receipts, the move-in report, KYC, landlord details, payment history. Upload the rent agreement and the app reads it: notice period, lock-in, agreement end date, and sets the reminders that protect the renter from each. Nothing expires silently.

**The maintenance log.** A private, dated record of everything that breaks and every time the landlord was told. Photos, dates, what happened. Not a complaint system, there is no manager on the other end here: a record. Records win deposit conversations.

**The community: the Flat and Flatmate board.** Where the city's renters already are, but verified. People post rooms available and rooms wanted, the way the locality Facebook and WhatsApp groups work today, except here identity is real. Members verify themselves and carry a verified tag; unverified members can browse and post but the tag difference is visible. Members can share their passports with each other, which turns the terrifying stranger-roommate decision into an informed one, and compatibility matching helps people find flatmates whose lives actually fit: schedules, food, guests, cleanliness. The peer-to-peer marketplace lives here too: the mattress, the fridge, the desk, sold to the next renter in the same locality instead of abandoned.

**Local services.** The renter with no property manager has nobody to call. A curated directory of partnered services fills that gap: cleaning, repairs, maid, cook, tiffin, laundry, doctor visits. Verified brokers appear here too, tagged verified when RentOk has verified them, tagged plainly when not. Partner offers live here as well: tenant insurance, medical insurance, and whatever brands earn a place. Everything in this layer is chosen, not scraped; a directory of everyone is a directory of no one.

**The trip planner.** A light AI itinerary assistant: tell it where you are going, get a plan. One of the small pleasures that make this a lifestyle app rather than a filing cabinet.

---

### 4. Being known: the Tenancy Passport

The heart of the door. One portable credential that says: this is who I am as a tenant, and here is the proof.

**Four layers, clearly labeled, so anyone reading it knows exactly what is verified and what is claimed:**

| Layer | What it holds | How it gets there |
|---|---|---|
| Self-declared | The history and details the renter writes in | The renter, any time |
| Witnessed | Payment record, on-time streaks, tenancies completed, condition reports signed | Automatically, from everything the app records |
| Verified | Identity, background check, court records | The renter pays once, reuses everywhere |
| Showcase | LinkedIn, Instagram, X, anything the renter wants a landlord to see | The renter links what they choose, and chooses per share |

No two passports look alike, and that is by design. A passport with three months of history is a young passport, not a bad one. Every month of renting adds to it on its own.

**Reputation carries two voices, kept separate on purpose:**

- **What landlords said.** Ratings and feedback from each stay, shown as what they are: one party's view. If a renter disputes one, that conversation is between them and that landlord; the app presents it fairly and without judgment, but the app is not the referee.
- **What was witnessed.** Impartial, factual, machine-kept: rent on time 34 of 36 months, two tenancies completed in full, deposit returned in full, condition reports signed by both sides. No opinions, no verdicts, no labels. The facts speak, in both directions: they expose a genuinely bad history, and they quietly defend a good tenant against one unfair review.

**The passport travels.** It attaches automatically to every application inside Browse. And it downloads as a document the renter can send to any landlord anywhere, on RentOk or not, carrying its verification marks and the name of who stands behind them. Every passport shared with a landlord who has never heard of us is a small introduction: this is what a renter looks like when someone has been keeping score. Some of those landlords will be curious enough to ask who was keeping it.

**The score.** The witnessed record rolls up into a tenancy score the renter watches grow: the renting life's answer to a credit score, built by simply living well. Partner offers get better as it grows: zero-deposit moves, better terms. The long-term ambition, stated so it is not lost: rent history this clean should one day count toward actual credit.

---

### 5. Moving on

**The notice, protected.** The vault already knows the notice period; the app reminds before it is due and drafts the notice letter.

**The move-out record.** The same video walkthrough as move-in, producing the closing condition report, signed by both sides when the landlord participates. Move-in report plus move-out report plus payment history plus maintenance log equals the deposit conversation settled by record.

**When the deposit conversation goes wrong.** The app assembles the evidence in one packet: dated reports, payments, the log of what was reported and when. If it comes to it, legal help through partners, with the packet ready to hand over. The strongest sentence a renter will ever say about this app is "it got my deposit back."

**And the record moves with them.** The tenancy that just ended becomes the newest entry in the passport, and the passport is already attached to the search for the next place. The end of one tenancy is the strongest moment of the next one.

---

## The mechanics that run through everything

**The tool ends where the workflow begins.** Every tool works standalone, fully, with no strings: generate one receipt, check one agreement, plan one trip. And at the moment the tool's value has just landed, and only then, the app offers the next step: the receipt is ready, want this automatic every month? The agreement is checked, want it kept in your vault with the notice-period reminder set? One suggestion, at the moment it is obviously useful, never a popup at the door, never twice. That is how tools become workflows and visitors become residents: by being genuinely useful first and quietly ambitious second.

**Login gates the result, never the discovery.** The tools are findable and startable by anyone searching at their moment of need. The finished result is where the account begins. Nothing useful escapes without a login, and nobody hits a wall before they have seen the value.

**Everything feeds the record.** Every payment, report, verification, and completed tenancy makes the passport heavier. Features that add to the record and features that spend it are both welcome; features that do neither must be genuinely delightful to stay.

**Every artifact carries the name.** The receipt that reaches an employer, the passport that reaches a landlord, the condition report both parties sign: each one travels beyond the app and introduces us to someone who never installed anything.

**Personal to the renter.** The student, the professional, the couple, the family: different budgets, different tools up front, different offers. Same app, personally arranged. And per TAR-00, offers respect age: minors are never targeted.

## Deferred, and what revives each

| Deferred | Revived by |
|---|---|
| Zero-deposit and pay-in-parts at scale | Partner agreements in place |
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

## Why this holds together

One loop, running through all five moments: the app is useful enough to live in, living in it builds a record, the record opens the next door, and the next door was found in the app. Browse brings renters in, the everyday layer keeps them, the passport makes leaving costly in the only honest way: not by locking anything, but by having witnessed a life no other app can vouch for.
