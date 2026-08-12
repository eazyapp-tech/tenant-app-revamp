# TAR-06 · Open for All: The Feature Map

**Read [TAR-00](TAR-00-vision-and-requirements.md) first.** This document decides what the Open for All door actually contains. TAR-00 names the three doors: the RentOk tenant app, the white-label tenant app, and Open for All, the app for tenants whose landlord is not on RentOk at all. This document is the third door's feature list, sorted into what is essential, what supports it, what waits, and what we chose not to build, with the reasoning written down so anyone can retrace the decision.

*Last updated 12 August 2026. Owner: Sanchay. Shaped in working sessions between Sanchay and Claude; every "exists today" claim below was checked against the actual systems, not remembered.*

---

## Who this door serves

A tenant renting from a landlord who has never heard of RentOk. Nothing reaches this tenant through their property: no manager pushing the app, no dues appearing automatically, no food menu. Every feature must earn its place on naked value to the tenant alone. TAR-05 said it first: in this door the burden quadrant does not exist, it is value or nothing.

This door also has a second job. Every tenant in it is a possible bridge to a landlord we have not met. The features below are chosen so that acquisition of new tenants, and through them new landlords, happens as a byproduct of tenants helping themselves, never through nagging or contact harvesting. That rule is inherited from TAR-01 and is not revisited here.

## The sorting test

Four buckets, one sentence each. Every feature in this document sits in exactly one.

- **Spine**: remove it and the door stops making sense.
- **Supporting**: makes the spine stronger or stickier. Ships without changing the thesis.
- **Parked**: a good idea with the wrong dependencies today. Each parked item names the condition that revives it.
- **Cut**: does not feed the spine, however good it sounds in isolation. Each cut names its reason.

## The spine

The spine is a chain, not a list. Each link feeds the next:

**Attract → Transact → Accumulate → Prove**

A stranger arrives (attract), pays rent through us (transact), builds a verified history by doing so (accumulate), and turns that history into a portable credential that opens their next home (prove). Everything else in the door either feeds this chain or hangs off it.

### 1. The AI Broker (attract)

A conversational agent that finds a tenant their next home from RentOk's live inventory: thousands of real, owner-listed properties. The tenant states what they need in plain words, the Broker recommends, explains, and eventually acts.

**Why spine:** this is the front door and the hero feature. The differentiation is structural, not cosmetic. Listing sites run on scraped, stale, half-fake classifieds and answer engagement with a flood of broker calls. Our Broker runs on inventory that owners themselves keep live because their business runs on it. An AI that works only for the tenant, grounded in real rooms, is a pitch no listing site can copy by adding a chatbot.

**The autonomy ladder, shipped in order:**

1. **Discover**: quiet recommendation inside browse. No chat needed. Good ranking using budget, location, and the persona model from TAR-01.
2. **Understand**: answers questions in conversation. Is this rent fair for the lane. What should I check before I visit.
3. **Decide together**: roommate matching, described under Community below.
4. **Act, with consent**: drafts and sends applications packaged with the tenant's passport, schedules visits, chases the property for updates. Every action is previewed; nothing sends without a tap.
5. **Negotiate, within limits the tenant sets**: the tenant states a ceiling, the Broker proposes terms inside it, backed by real comparable rents from our own network. Framed as fair-market, never adversarial: a landlord receiving an informed, reasonable offer is a warm first meeting with RentOk, not a bad one. The tenant approves every offer before it goes out.

*Verified: the booking bot agent this builds on already exists in our systems. Also verified, honestly: the recommendation engine behind it is thin today, a plain room catalog plus a log that nothing reads back. Recommendation quality is real work to build, not a switch to flip.*

Legal review of agent-and-broker licensing rules happens before the Negotiate rung ships, not before the feature exists. The Broker works only for the tenant and takes no commission from the deal, which places it outside the usual definition of a broker, but that gets confirmed by counsel, not assumed.

### 2. The free public tools (attract)

A public web hub, no login, no install: rent receipt generator (HRA compliant, from details the visitor types in), state-aware tenant rights checker, rent agreement checker, locality rent pages, property review pages.

**Why spine:** this door starts with zero installed base and no property pushing the app. These tools are how strangers find us. Each one answers a search people already type in volume, at high intent, at a specific moment of need: receipts every tax season, rights the week a deposit goes missing, agreement checks the day before signing. One mechanic runs through all of them: give the useful slice away free and public; the app is where it becomes automatic, saved, and connected to everything else.

The receipt generator has a quiet second audience: receipts travel to employers for HRA claims, which puts our name on a legitimate document inside companies we have never sold to.

### 3. The rent payment rail (transact and accumulate)

The tenant pays their rent through the app to a landlord who is not on RentOk. The landlord receives a normal bank transfer, with our name on it.

**Why spine:** this is the infrastructure link, and the single most consequential build in the door. Five things resolve at once when it exists. Rent history becomes verified instead of self-claimed, which is the difference between a passport that proves and a passport that asserts. Receipts generate themselves. A future credit score becomes honest. Every transaction carries revenue. And every payout lands in a landlord's account as the warmest possible introduction to RentOk: money, on time, with a name attached.

This is also the riskiest build: payment aggregator integration, landlord-side KYC, and compliance review for person-to-person rent flows. We accept that cost knowingly, because without the rail the Accumulate link of the chain is missing and the passport below is a claims document.

### 4. The Tenancy Passport (prove)

One portable, shareable credential: the tenant's verified rental identity, shared with any landlord as a tenancy application. The tenant pays for verification once and reuses it everywhere. Four layers, clearly labeled so a landlord always knows what is verified and what is claimed:

| Layer | What it holds | Who triggers it | Trust level |
|---|---|---|---|
| Self-attested | History the tenant types in | Anyone | Lowest, labeled as unverified |
| RentOk-witnessed | Payment history, on-time streaks, ratings received at RentOk properties, move-in and move-out condition records | Automatic for anyone who has ever been a RentOk tenant, any door; grows through the rail for everyone else | High. RentOk vouches, not just displays |
| Third-party verified | Aadhaar eKYC, background and court-record check | Tenant pays once, reuses across applications | Highest, an external authority stands behind it |
| Showcase | LinkedIn, Twitter, Instagram, anything the tenant chooses to link | Tenant links, and chooses per share what to include | Not a trust signal, a presentation layer. Entirely the tenant's choice |

**Why spine:** the passport is what the whole door walks toward. It is the product the record becomes, the thing the tenant owns, upgrades, and shares. Every share puts a credible RentOk document in front of a landlord we have never met. For RentOk alumni it arrives pre-filled: their history with us becomes a credential they carry out the door, which is also the single best reason for a former tenant to come back.

*Verified: management already rates tenants at move-out today, with remarks, rating chips, and a blacklist flag. Surfacing that into the passport is aggregation of existing data, not new collection.*

The far horizon of this link, named so it does not get lost: reporting verified rent history to the actual credit bureaus, so rent builds credit the way a loan does. That is a heavy, regulated build and sits in Parked, but it is the answer to why the passport matters so much.

## The AI family

Three agents share one infrastructure and one conversational surface, but have deliberately separate jobs. Keeping them separate keeps each one honest about what it is for.

- **The Broker** (spine, above) finds and secures homes. It does not do legal analysis.
- **The AI Lawyer** (supporting) reviews rent agreements against the tenancy law that actually applies in that state, flags one-sided clauses in either direction, tenant-sided or landlord-sided, and answers rights questions. It must know which state's law applies and say plainly when it does not have that state loaded, because a wrong "this clause is illegal" does real damage. The Model Tenancy Act is a template states adopt in versions, not one national law, so the Lawyer is built on the actual statute text per state.
- **The Trip Planner** (supporting) is a light itinerary assistant: tell it where you are going and it plans the trip. In the RentOk and white-label doors this same feature grows teeth, connecting to guest management, entry and exit approval, and food billing, which exist there and depend on each other. In this door it is deliberately simple, and cheap to include because the agent infrastructure already exists for the other two.

**Why the Lawyer is supporting, not spine:** it is a trust engine and a real differentiator, and it is the strongest candidate for promotion to a second hero. But a tenant who never opens it still gets the full spine value, which is the test. It also powers the agreement checker in the public tools, so it earns attention early.

## Supporting features, grouped

| Group | Contains | Why it supports |
|---|---|---|
| Browse trust layer | Property reviews, verified landlord badge, scam and fake-listing detection, visit notes and compare | Makes the Broker's recommendations trustworthy. Reviews and badges are facets of browsing, not separate products. The verified landlord badge is also the mirror of the passport: a low-commitment first RentOk touchpoint for a landlord who wants to attract careful tenants. |
| Locality truth layer | Neighborhood intelligence merged with the rent index: what rent really is lane by lane, plus water, power cuts, commute, safety after dark, crowd-sourced from tenants | Feeds the Broker's fairness answers and the public rent pages. It is a data layer with two faces, one inside the app, one public. |
| The secure-it flow | Digital check-in (the existing webcheckin product, merged in fully), rental agreement creation, stamping partner, eKYC, background verification | Mostly exists already across our products. This door assembles it end to end. Table stakes done well. |
| The money module | Bill payments over BBPS, splitting rent and utilities between roommates, expense and budget view | One module, not three. Its edge over standalone expense apps is that tracking is a byproduct of paying, not manual entry, which is exactly where standalone trackers lose their users. Adds commission revenue on every bill and a natural paid tier later. Ships after the rail, which it depends on. |
| The deposit arc | Move-in and move-out condition documentation (one feature, two moments, living inside the passport), private maintenance log, auto-assembled evidence packet, legal help partner | The advocacy asset. Deposit disputes are the loudest exit pain in Indian renting, and disputes are won on dated evidence, not on finding a lawyer faster. The app holds the photos, payments, and complaint trail already; assembling them when a dispute starts is the product. "This app got my deposit back" is the strongest sentence a tenant can say about us. |
| Community | The Flat and Flatmate board (modeled on the locality Facebook and WhatsApp groups where this already happens: people posting rooms free and rooms wanted), roommate compatibility matching, peer-to-peer marketplace for furniture and household goods | Real network effects, real cold-start risk, so it launches city by city where the RentOk network is already dense. Roommate matching between strangers is a safety feature before it is a convenience feature, so matches require the passport's verified layer, which also gives verification a second reason to be worth paying for. |
| Local services directory | Partnered home services: cleaning, repairs, maid, chef, tiffin, movers, storage between homes | A door-1 tenant raises a complaint and a manager responds. A door-3 tenant has nobody to call. Partners fill that gap and pay referral revenue. Curated partners, not a directory of everyone. |
| Small utilities | Rent due reminders, notice period tracker with a template letter, address proof from agreement plus receipts, HRA and tax helper | Each is small, cheap, and comes almost free once the rail and receipts exist. High usefulness per unit of effort, no strategic weight on its own. |

## Parked, and what revives each

| Parked feature | Revival condition |
|---|---|
| Deposit financing (pay the move-in lump sum in installments) | A vendor relationship. We used one before and stopped; the concept stands, the partner is to be chosen. |
| Deposit protection as a financial guarantee | The deposit arc proves volume first. This is a regulated financial product and takes a partner. |
| Credit bureau reporting of rent history | The rail runs and history accumulates. Then the bureau conversations begin. The internal score inside the passport ships first and does not wait. |
| Rent as a biller inside every bank's bill-pay app | BBPS front-end volume justifies the registration effort. This flips distribution: our rent appears inside other apps. |
| Electricity overcharge detector | The locality truth layer starts crowd-sourcing actual tariffs. We do not want to maintain government tariff tables by hand. |
| Moving-out to moving-in room matching | Community density exists. Before that it is an empty room nobody sees. |
| Parent window (visibility for the parent who pays) | The research in TAR-04 answers the autonomy question. The concept card exists there; we do not build past the tenant's comfort. |

## Cut, and why

| Cut feature | Reason |
|---|---|
| Utility connection transfer | Government workflows differ by state and utility, with dependencies we cannot own. The services directory can point to partners who do this. |
| Safety and SOS layer | A half-built safety feature is a liability, not a feature. Phones and dedicated apps do this better than a rental app ever will. |
| Broker fee blacklists | Naming individuals invites defamation exposure. Structured property reviews absorb the honest part of the need. |
| Standalone furniture rental | Folds into the services directory and the peer-to-peer marketplace. Not its own surface. |
| Generic expense tracker as its own product | Commodity. It survives only as the money module's byproduct view, where paying does the tracking. |

## Build order

Three waves, matching the spine chain. Each wave must stand on its own if the next never arrives.

| Wave | Ships | The bet it tests |
|---|---|---|
| **A** | Public tools hub · Browse with the Broker's Discover and Understand rungs · Passport with self-attested and RentOk-witnessed layers · rent receipts · move-in documentation | Strangers arrive through tools and the Broker, and alumni return for the passport. |
| **B** | The rail · the money module · third-party verified layer · Broker's Decide and Act rungs · community board · services directory · AI Lawyer full | Tenants transact, and verified history starts accumulating. |
| **C** | Broker's Negotiate rung · paid tiers · partner monetization at depth · parked items as their conditions arrive | The record is valuable enough that tenants pay, and partners pay to reach them. |

## Decisions still open

Written here so they are owned, not lost:

1. **Does a tenant see, and can they contest, a management rating or blacklist entry before it enters their shareable passport?** The data exists today and is entered by someone else about them, and it can gate their next home. Needs a policy decision before the witnessed layer ships.
2. **Broker licensing review** before the Negotiate rung, as above.
3. **City sequencing**: the default is to launch where the RentOk property network is already dense, borrowing the other doors' density instead of bootstrapping thin everywhere. Standing default unless argued down.
4. **What the complaint record means in a passport.** A tenant who reported a broken geyser must never score worse than one who suffered in silence, or we teach tenants to stop reporting. Only conduct flags and eviction-for-cause style signals enter the passport, never raw complaint counts. Held as a design rule; needs restating wherever scoring is specified.

## How this door feeds the other two

Named plainly because it is the business case: every passport shared puts our name in front of an unknown landlord as a vouching authority. Every rail payout arrives in a landlord's bank account with our name attached. Every verified-landlord badge is a landlord touching RentOk voluntarily. Every alum carries their record out of doors 1 and 2 and becomes this door's warmest user. The three doors are one loop: the records built where RentOk manages the property become the product where it does not, and the tenants it serves there lead us to the landlords we have not met yet.
