---
title: TAR-01 Tenant App Revamp Concept Brief
date: 2026-08-10
tags: [rentok, brief, tenant-app, revamp]
owner: Sanchay
time_budget: quality-paced, no hard deadline
status: v7-teardown-applied
---

# TAR-01 · Tenant App Revamp · Concept Brief

## In one line

Rebuild the tenant app so a tenant treats it as part of the home they live in, not a portal their landlord made them install.

## Why now

1. **Adoption is near zero on the ground.** Field visits found complaints kept on a paper register and tenants who had never installed the app. Day-to-day work moved to WhatsApp because the app was weak.[^1]
2. **Tenants who do install open the app once or twice a month.**[^2] An app opened that rarely cannot carry a platform fee. We intend to charge roughly Rs 30 to 50 per tenant per month (owner-side intent, not yet validated with buyers).
3. **One core, three doors.** The same app ships three ways: the standard RentOk tenant app, the white-label app for property brands, and an open-for-all app for tenants whose property is not on RentOk. White-label clients such as Meridian are holding tenant onboarding until their branded app is ready.[^3] The open-for-all door is where paid tenant services live later: rent agreements, receipts, verification, splitting bills, relocation help. A weak core makes all three doors weak.
4. **The destination is dependence, not installs.** A tenant who has lived with this app should hesitate to move into a property that does not run it, because their rent record, agreement, verified identity, streaks, and daily conveniences live here. That is what carries a platform fee, and it reverses the value chain: tenant expectation starts pulling owners onto RentOk instead of owners pushing tenants onto the app. Installs are the first reading; dependence is the destination.

## The bet

WhatsApp already handles messages and payment links fine. Competing with WhatsApp on utility is a losing game. The one thing WhatsApp can never be is the app of the place you live: your building's name and logo, tonight's dinner, your attendance streak, your rent record, the people around you. We bet that belonging is what makes a tenant keep the app, and utility is what makes them trust it. Both, in that order.

Personalization makes the belonging real, along three axes, all fed by data the backend already sends today:

- **Person.** The profile data already tells us whether the tenant is a student, a working professional, or a family (university and course fields versus company and occupation fields, plus food preference, gender, date of birth).[^4] The app changes its tone, its greeting, and what it puts first. A student's evening is food and curfew. A professional's month is rent and receipts. A sponsored tenant whose company pays the rent should never be nagged about dues they may not even know.[^5]
- **Place.** City, state, and a property photo already arrive from one existing endpoint.[^6] The property's name and logo lead the app, not RentOk's. The property logo is fetched and stored today and shown nowhere in the app.[^7] That changes: the logo becomes a designed moment at boot, on the home header, and on receipts.
- **Composition.** Which modules a property turns on already shapes what the app is. Attendance plus food on means a student PG. Services on means co-living. The app leans into this: same code, a genuinely different app per property. No new backend data needed.

We will not guess property type from stereotypes. Personal registers key on what the tenant needs, never on clichés about who they are.

One more part of the bet, because adoption gates everything: **the owner is the channel.** Research is blunt that tenants install when the owner pushes the app and not otherwise.[^18] So the handover moment is part of the product: the owner shows a QR or sends an invite at move-in, the tenant lands in a first run that feels like arriving home, and the owner can see who installed. This lives inside the Sign up & Intro section's scope.

## Who it's for

Seven tenant personas exist from research: hostel/PG student, working professional, family flat tenant, migrant/blue-collar tenant, corporate-sponsored tenant, short-term tenant, long-term settled tenant.[^8] For design we compress them into five registers by need, each with the signal that detects it:

1. **Daily-loop tenant**: food, attendance, gate. Detected by university/course fields on the profile, or by attendance and food modules being on.
2. **Monthly-loop tenant**: rent, receipts, service bookings, complaints. Detected by company/occupation/income fields. This is also the fallback register when signals are ambiguous.
3. **Document-heavy tenant**: agreement, verification, move-out trust. Detected by family fields and flat-style properties (PG modules off).
4. **Cash-first tenant**: simplest possible paths, WhatsApp help one tap away. Detected by the property's online payment being off (the passbook already sends `upi_intent` as "none" in that case[^19]).
5. **Sponsored tenant**: show the home, mute the money. No reliable signal exists today, so this ships as a softened variant of the monthly-loop register (dues stay visible, the language stops nagging); full detection waits for an owner-set flag and is out of Phase 1.

## What we must ship

Srijan's top ten is the starting scope, not a decree: Theme, Sign up & Intro, Homescreen, Feature List (navigation), Profile, Accounts, Complaints, Messaging, Rewards/RentPass/Points, Reviews. Six are unarguable (Theme, Sign up & Intro, Home, Accounts, Complaints, Profile). On the rest, this brief takes four positions, open to being overturned in review:

- **Food and Attendance join the mandatory set.** The list leaves out the two modules that create daily opens for the highest-engagement segment we have: students and PG tenants.[^22] If adoption gates everything, the daily loop cannot sit on the flexible list while two lighter modules sit on the mandatory one.
- **Messaging means the WhatsApp thread, not in-app chat, and most of it already exists.** RentOk already runs a white-label WhatsApp product: every property can have its own WhatsApp Business number, and RentOk sends payment, KYC, and dues reminders through it. Every message sent or received on that number is already logged per tenant.[^24] "Messaging" in the app means showing that thread inside the app instead of only inside WhatsApp itself. The store already exists; only a read endpoint for the tenant app is missing.[^25] No new chat system is built, and the app is not competing with WhatsApp, it is bringing WhatsApp's own record into the app the tenant already opens for other things.
- **Reviews already exists and already runs, just over WhatsApp instead of the app.** RentOk has a working review and survey system: tenants leave property reviews, and properties run feedback campaigns with configurable questions, sent and answered today through a WhatsApp-driven web form.[^26] One tenant-app endpoint for this already exists.[^27] The work is bringing an existing, already-validated feature natively into the app, not inventing a new one.
- **Rewards is rebuilt around streaks, not scratch cards.** Most personas ignore the current carnival.[^23] The version worth building is the on-time rent streak that doubles as a reliability record for the tenant, tying rewards to the core job instead of decorating it. Which rewards a tenant actually sees is a targeting problem, not a design problem: see Offer targeting below.

With those positions, this revamp carries two small, named backend asks — a read endpoint over the existing WhatsApp message log, and a tenant-app endpoint for the existing review campaign data[^27] — both additive reads over data that already exists, not new systems. Everything else ships on today's endpoints.

### Offer targeting — thinking it through

Rewards and offers are not one catalogue shown to everyone. What a tenant sees depends on three things, and none of them are solved yet:

1. **What RentOk itself can offer where.** RentOk's partner network is geography-bound — a Goa property may have five live partner offers where a Pune property has none. The app must be able to show nothing gracefully in a city where nothing is live, without looking broken.
2. **What the property itself wants to offer.** An owner may run their own discounts or partnerships independent of RentOk's network. The offer surface needs two sources, RentOk's and the property's, shown together without either one looking like an afterthought.
3. **Who the tenant is.** A student and a working professional in the same city do not want the same offer, even if both are live there. The person axis from the personalization system applies here directly.

This needs backend-side offer targeting (by property, city, and tenant type) that does not fully exist today; today's offers are a flat catalogue.[^28] It is called out here, not solved here, because it changes what the Offers/Rewards ideation round has to design for: an empty state that is not a dead end, and a surface that reads as curated rather than copy-pasted regardless of how many offers happen to be live for that tenant.

Build order, decided, in waves:

- **Wave 1: Theme (the design system), Homescreen, Sign up & Intro, Accounts.** The system because everything inherits it; today the white-label color mostly never reaches the screen.[^9] Home because the concept proves itself there. Sign up & Intro because first-run is the documented drop-off and the owner handover lives there. Accounts because money is where trust is won.
- **Wave 2: Food, Attendance, Complaints, Profile.** The daily loop plus the rest of the trust core. Feature List (navigation) falls out of the system and home work rather than being its own build.
- **Wave 3: Rewards (streak rebuild + targeting), Messaging (WhatsApp thread), Reviews.** The last two need their small backend reads; concepts are ready earlier.
- **If the design system eats more time than expected, Rewards is the first cut.** Tenants would miss it least: dues, meals, attendance, complaints, and documents are the core; rewards decorate it.

Beyond the ten, a flexible feature list is open: Polls, Community, Event Planner, Expense, P2P buy-sell, Browse Property (same group), Refer & Earn, Meal Planner, Task To Do, Internship/Jobs (partnership). Our starting bet, to be confirmed or overturned in review: **Polls** and **Expense** — the two that are multiplayer by nature, so they pull a tenant's floormates in without a referral scheme (see Every tenant is a channel). Refer & Earn leaves this list entirely: sharing is a property of the whole app, not a feature to be scheduled. For each of the ten sections and each flexible feature we will write several distinct approaches, then lock in review against a stated position, not from a blank page. **The rubric for every approach: does it serve the bet (belonging first, trust always), does it serve at least one of the five registers, and does it give the tenant something worth showing someone. An approach that fails all three is dead on arrival.**

## Design direction

**The bar is benchmark, not just good.** Apps that became industry references share three properties: a named, documented design language; radical coherence, where every screen obeys the same physics; and two or three signature moments people screen-record and share. So the Theme workstream produces a **named design language with public-grade documentation**, and every wave names its signature moment: the boot ritual where the property's logo resolves, the rent-paid moment, the move-in welcome. "Crazy good" means radical coherence and earned surprise, never noise. Design creates love; the feature horizon creates dependence; this revamp must deliver the first and leave honest room for the second.

**The closest reference is not another property app. It is what Scapia, Kiwi, Slice, and Stable Money did to Indian finance.** Each took a boring, infrastructural, adult product (a credit card, UPI rails, a fixed deposit) and made a young person want to own it, show it, and identify with it. Stable Money is the sharpest case: fixed deposits, made calm and beautiful enough that a twenty-four-year-old opens the app for pleasure. Rent, receipts, KYC, and attendance are the fixed deposit of property software. Nobody has done to renting what those four did to finance. Four laws follow from that, and they are testable:

1. **The app has a hero object, and it is the place, rendered as data rather than as a picture.** Slice and Scapia centre a card because a card arrives in the post. Nothing arrives here, and the building belongs to the client, not to us, so we cannot art-direct a photograph of it. What we can render with real weight is the tenant's own facts: Room 302. Third floor. Eighteen months. ₹25,000 held. That is the move Stable Money makes when it extrudes a number into a physical object, and it is the only hero that works when the property changes and the palette changes with it. The property's logo, name, and address frame it; the numbers carry it. A second object grows over time and matters more: the tenant's own record, the tenancy they carry between homes.
2. **Timeless in structure, modern in behavior.** Restraint carries the structure (type, grid, real photography, no trend of the month), and motion carries the modernity. A still screenshot should be hard to date; the moment a finger touches it, it should feel like next year's software.
3. **The ceiling is Scapia-grade, the floor is dignified for everyone.** Those apps design for one narrow, affluent, urban audience. We also serve a migrant worker in a hostel and a tenant whose company pays the rent. Sophistication reveals itself as a tenant engages; nothing basic is ever gated behind novelty, and there is never a stripped-down "simple mode", which is only a polite insult.
4. **Identity lives everywhere except color.** Their design is their brand. Ours has to survive being repainted in a client's colors and logo and still be unmistakably ours, so the identity is carried by type, motion, layout physics, illustration, voice, and the shape of moments. Almost nobody solves that well, and solving it is what would make this citable.

**One expensive commitment, everything else disciplined.** Each of those brands spends deeply in exactly one place and lets the rest be plain: one bought a typeface outright and left its greys at framework defaults; another licensed four display faces and separates its cards with half-pixel lines.[^34] Ours is **the typeface** — the thing that carries identity when color cannot. That means real weights instead of the single regular cut we ship today, numerals that align in a money column, and Indian-script coverage. It also means the font ships inside the package itself, never as a per-client asset: the way this class of system dies is a client budget trimming the licensed face and falling back to the phone's default, which is exactly what happened to one of the apps studied here.[^35] If there is no per-client decision to make, there is nothing to lose.

- **Type does the branding work.** Premium feel comes from typographic contrast: a display voice for moments, quiet small labels, honest tabular numbers for money. A type system survives any brand color; a color-dependent design does not. Today only the regular font weight actually ships and every bold is faked by the renderer.[^10]
- **Celebration is earned, and rent is not a slot machine.** Rent paid is the emotional peak of the month and gets a designed full-screen moment, but that moment is the receipt and the streak, never a spinning reward. A card bill is discretionary spending with a reward loop already attached; rent is an obligation often paid late or with borrowed money, sometimes by a company the tenant never sees. A wheel there trivialises it, and no family-run property brand wants gambling optics in their app.[^34] Small actions get quiet confirmations. Confetti is never the default.
- **The receipt is the artifact, and we are luckier than the fintechs here.** A payment receipt in a card app is a nice-to-have. A rent receipt is a document an Indian tenant actually needs, for tax claims on rent paid, for police verification, for proving they live where they say. Those apps had to invent a reason to make a receipt beautiful. We already have one, which means our most shareable screen is one the tenant was going to send someone anyway.
- **The app talks like a helpful senior, not a portal.** Tap-choices over dropdowns, plain-language warnings before money edits, empty states with a voice ("No dues. Frame this screen.").
- **Show up, get seen.** Attendance and meals borrow streak grammar: a calendar that fills, a human affirmation when you mark, not a toast.
- **Dark is a stage, not a theme.** Dark treatment is reserved for reward and celebration moments; the daily app stays light and calm.
- **AI where a conversation beats a form, never where a glance beats a conversation.** Tarini already exists and is the best-built screen in the app; she grows into how tenants file and track issues, with real interface pieces (choices, dates, photos, status cards) inside the chat. The rent agreement gets a plain-language explainer the tenant can question, because paperwork is the highest-anxiety moment in an Indian tenancy.[^29] Home, dues, and menus stay glanceable: no chatbot ever gatekeeps information a tenant could see in one look.

## Every tenant is a channel

Adoption cannot rest on owners alone. The app has three ways to spread, they are structurally different, and each needs its own design answer:

- **To the people on your floor.** The mechanic is not referral, it is multiplayer: the dinner poll, who is eating tonight, splitting the electricity bill, the shared list. You pull your floormates in because the thing does not work alone. This is the cheapest, densest growth we have and it is a reason to keep small shared-life features on the list rather than treat them as decoration.
- **To friends in other properties.** This runs on artifacts and a little envy: a receipt worth screenshotting, a streak worth showing, a menu that makes someone ask which app that is. The friend in a property that does not use RentOk is not a dead end, they are the open-for-all door's first real user.
- **To their own owner.** A tenant asking their landlord "why do we not have this?" is a warm lead that costs RentOk nothing. This vector already exists in the app, and it is both broken and hidden: the invite-your-property flow is gated to the standard app so no white-label tenant can ever see it, and the CTA inside the sheet does nothing at all.[^31] The whitelabel invite link and short-link fields are parsed and never used.[^32] Fixing and opening this is one of the highest-value, lowest-effort moves in the revamp.

What makes a tenant advocate is not a referral code. It is pride (an app that shows off the place they live), status (a record and a streak that say something about them), utility that needs other people, and one story stronger than any of them: **this app got my deposit back**. Deposit disputes are the single biggest trust gap in Indian renting.[^33] A tenant who kept their deposit because move-in photos were timestamped in this app will tell everyone they know. That makes move-in and move-out documentation the app's best marketing, not its most boring compliance screen.

The line we do not cross: no share-to-unlock, no contact-list harvesting, no nagging. Advocacy has to be a by-product of pride and usefulness. The moment sharing becomes a toll gate, the taste bar is gone and so is the advocacy.

## The horizon (designed for, built later)

Dependence compounds from features beyond this revamp, and the design must leave them honest room rather than bolt them on later: smart locks and in-app door unlock (a white-label client has already asked[^30]), deeper meter and IoT integrations (the prepaid electricity card already exists in the app), bill-splitting, weather and daily-life helpers, AI products such as the agreement explainer and post creation, and above all the **portable rental identity**: verified KYC, rent history, agreements, and a tenancy streak that travels with the tenant between properties. That identity is the strongest form of the open-for-all door and the deepest reason a tenant would not want a property without this app. Phase 1 builds none of these; navigation, the home registry, and the design system reserve their place.

## Boundaries

- **Backend: protect now, open later, record always.** Cycle 1 redesigns existing workflows on existing endpoints; nothing destabilizes what runs in production. Cycle 2 opens the backend, including for new features. Any additive need discovered mid-design is neither dropped nor quietly built: it goes to the [[Backend Asks Ledger]] with its reason, and Sanchay decides its cycle. The ledger opens with four entries: the WhatsApp thread read endpoint,[^25] the review endpoint verify/extend,[^27] offer targeting,[^28] and the owner-set sponsored-tenant flag. Meanwhile the property columns describing gender policy and property type stay stripped;[^11] composition remains our property-type signal in cycle 1.
- **Standard app first.** White-label uniqueness rides on the same design system later. We do not design per-client in Phase 1, and the one per-property brand element is the property logo.
- **Open-for-all is designed for, not built.** Navigation and the design system reserve its place; its paid features come after Phase 1.
- **No open community across properties.** The team already decided against it; property managers cannot carry the moderation load.[^12] In-property community features stay on the flexible list for the ideation round.
- **Working logic is kept.** Tarini chat, the eviction status machine, and the payment rails keep their behavior. They get the new structure and skin, not a rewrite of their rules.

## Traps and risks

- **Trust debt (USER).** Receipts that fail to deliver, profile edits that do not save, and a "Profile 100% Completed" badge that lies are why tenants distrust the app today.[^13] The completion flag is genuinely used backwards in code.[^14] Every module redesign must fix the trust moments it touches, or the new look reads as paint over cracks.
- **First-run wall (USER).** The forced attendance setup screen cannot be exited and is the most documented drop-off point for new users.[^15] First-run experience gets its own dedicated design pass inside Sign up & Intro.
- **Stereotype trap (USER).** Registers key on needs and are reviewed against the real persona research; no "girls PG gets pink" class of decision, ever.
- **Combinations trap (TEAM).** Hand-crafted personalization is accepted, but the matrix stays small: five registers, a small set of theme moods, and composition handled by the home's section registry. Per-property hand-tuning is not a path we open.
- **A red-branded client cannot tell paid from overdue (USER).** Every semantic color in the app is derived from the client's brand color: "paid" green, meal colors, and tab tints all resolve to `primary` or a tint of it.[^36] Hand a property a red brand color and the money screen stops distinguishing settled from overdue. Every reference app keeps brand color and meaning color as separate systems that never share a value. Ours must too, and success, warning, and error become a fixed set the white-label cannot touch. This is a trust defect shipping today, not a cosmetic one.
- **Payment reality (TEAM).** Only Cashfree is live; all eight gateway constants in the code route into it.[^16] The Accounts redesign must not assume any other gateway exists.
- **Structure before paint (TEAM).** The home fires the same network calls two to three times per load, one provider is registered twice, and the payment sheet pretends to be a page without being one.[^17] Each module redesign budgets structural repair alongside visuals.

## Success

Ordered; all four count, the first gates the rest:

1. **Adoption.** Installs and monthly active tenants at pilot properties. We measure the baseline in the first month after wave 1 ships; the working target is three times baseline installs within a quarter (owner-side estimate, to be reset against the measured baseline). The long-horizon reading is dependence: tenants naming the app as a reason to choose or stay in a property.
2. **Chargeable value.** The app earns the platform-fee conversation with real owners.
3. **Owner pride.** Observed through owner-driven installs: move-in QR scans and owner-sent invites.
4. **Craft.** Observed through store rating movement and the sales team using the app itself as a pitch asset.

Guardrail metric: first-run completion rate, because that is where today's app loses people.

## Changelog

- 2026-08-10: v1. Drafted from Phase 0 code discovery (6 reports), the Notion research corpus (15 docs), Mobbin reference research, and Srijan's top-10 mandate.
- 2026-08-10: v2, after adversarial critique. Added: owner-as-channel to the bet; Messaging/Reviews named as the only two backend asks; wave-based build order with a stated first cut (Rewards); register detection signals with monthly-loop as the ambiguous fallback; starting bets on the flexible list (Polls, Refer & Earn, Expense); ideation rubric; measurable success reads. Fixed two footnote defects (theming mechanism, pg_logo call site); verified the Place-axis endpoint works for non-booking tenants; "good warden" became "helpful senior."
- 2026-08-10: v3. Reframed Srijan's top ten as starting scope with four stated positions: Food + Attendance promoted to mandatory (the daily adoption loop was missing); Messaging reframed as Inbox (unified read view, no in-app chat); Reviews held as a three-door strategic bet that must prove itself; Rewards rebuilt around rent streaks. Waves updated accordingly.
- 2026-08-10: v4, after Sanchay's correction and a codebase check. Two v3 calls were wrong and are reversed: Messaging is not a new Inbox concept, it is the already-logged white-label WhatsApp Business thread (`whatsapp_messages_dash`) surfaced in-app through one new read endpoint; Reviews is not an unproven strategic bet, it is an already-working review and survey system (`tenant_review`, `property_review_campaigns`) currently delivered over WhatsApp, with one tenant-app endpoint already live. Boundaries corrected from "no backend changes" to three named additive asks. Added Offer targeting as a stated open problem (property, city, and tenant-type scoping) that the Rewards/Offers ideation round must design around.
- 2026-08-10: v7, after a source-code teardown of the reference apps (phase1/07-fintech-teardown.md — their live CSS, shipped design tokens, and font binaries, since none are indexed on Mobbin). Reversed an earlier call: rent payment does not chain into a prize wheel, because rent is an obligation rather than discretionary spending; the moment is the receipt and the streak. Refined the hero object from a picture of the place to the tenant's own facts given weight, since the building belongs to the client and cannot be art-directed. Added the receipt as a document tenants genuinely need, which makes it shareable without gimmicks. Named the one expensive commitment as the typeface, shipped inside the package rather than per client. Added the red-branded-client trap: semantic colors currently derive from the client's brand color, so paid and overdue can render identically.
- 2026-08-10: v6. Added the fintech reference frame (Scapia, Kiwi, Slice, Stable Money — boring adult product made desirable) with four testable laws: the place as hero object, timeless-in-structure/modern-in-behavior, Scapia ceiling with a dignified floor, and identity carried everywhere except color. Added "Every tenant is a channel": three viral vectors (floormates via multiplayer features, friends elsewhere via artifacts, owners via the invite-your-property flow that is currently gated to the standard app and wired to a no-op), the deposit-back story as the strongest advocacy asset, and a hard line against share-to-unlock. Refer & Earn removed from the flexible list because sharing is now a property of the whole app; Polls and Expense kept for being multiplayer by nature. Ideation rubric gained a third test: is it worth showing someone.
- 2026-08-10: v5, ambition raised per Sanchay. Added: dependence as the destination (Why now point 4); the benchmark bar (named design language, radical coherence, signature moments per wave); AI-native design rule (conversation over forms where it wins, glanceability protected) with the agreement explainer named; The Horizon section (IoT, smart locks, portable rental identity — designed for, built later); backend policy restated as protect-now/open-later/record-always with the Backend Asks Ledger (4 opening entries, incl. the sponsored-tenant flag); dependence added as the long-horizon success reading.

---

[^1]: Guerrilla field visits, 2 Vardhman + 1 Hari Om properties. "Interview with Property" doc, research corpus.
[^2]: Friendzo <> RentOk meeting notes (Sanjay): tenants open the app 1 to 2 times per month.
[^3]: Karan interview, research corpus: enterprise clients wait for white-label before onboarding tenants.
[^4]: Backend audit: `POST tenant/fetchTenantDetailsByKey` spreads the entire tenant row (`rentok-backend/src/controllers/tenant.ts:6618`), including university, course, occupation, company, income, food preference.
[^5]: Persona doc, research corpus: corporate-sponsored tenants "may never open Dues, may not know own rent amount."
[^6]: `GET /tenant/unified/:property_id/bookings` returns structured city, state, pincode and a property image (`rentok-backend/src/services/tenant/tenant.ts:12043-12049`). Verified it needs only an active tenant row, not a booking record: `Tenant.findOne({id, property_id})` at `:11982`; booking status simply resolves to -1 for regular tenants.
[^7]: `pg_logo` is cached at `lib/application/profile_provider.dart:156`; `PrefsUtils.getPgLogo()` is called once (`profile_my_renting_info_section_card.dart:23`) with the result discarded. Rendered nowhere.
[^8]: Persona doc + field visits + team interviews (Anil, Karan, Anurag, Harsh, Siddhant), research corpus. Personas are from real research, not invented.
[^9]: Phase 0 design-system audit: roughly 41% of color decisions are raw hex literals that ignore the theme entirely, a legacy second color class (`AppTheme`, `lib/utils/colors.dart`) still has 52 references, and `MaterialApp` carries no `theme:` at all (`lib/rentok_tenant_package.dart:142`), so the white-label colors have no reliable path to most widgets.
[^10]: Only `Poppins-Regular.ttf` and `Inter-Regular.ttf` ship in `lib/fonts/`; all other weights are synthesized.
[^11]: `delete tenant.property` at `rentok-backend/src/controllers/tenant.ts:6499` strips the property object; `pg_available_for`, `tenants_preferred`, `property_type` never reach any tenant endpoint.
[^12]: Harsh interview, Recording 7: decided against open inter-property community due to manager overhead.
[^13]: UX Finding Interview Summary: receipt delivery failures, profile fields not persisting, wrong completion status (Karan, Harsh Rec. 6).
[^14]: `home_your_profile_section.dart`: `isComplete` is set from `profileModel.profileIncomplete` without inversion.
[^15]: Field research ("Interview with Property"): attendance setup CTA stays disabled with no explanation; `SetupAttendancePage` is pushed with `PopScope(canPop: false)` (`lib/presentation/attendance/setup/setup_attendance_page.dart`).
[^16]: `MakePaymentFactory2` (`lib/presentation/accounts/pay_now/provider/make_payment_factory2.dart`): all non-cash gateway constants route to `CashfreeCheckout`.
[^17]: Phase 0 report 01: `fetchTenantHomePage` fires 2-3 times per home load; `PendingTaskProvider` registered twice (`lib/rentok_tenant_package.dart:127,138`); pay sheet expand mode draws a fake app bar without pushing a route.
[^18]: Karan interview: "the primary reason tenants do not adopt the app is that property owners fail to promote it"; field research: properties with physical QR posters show meaningfully higher adoption.
[^19]: `upi_intent` is set to the string "none" when the property or tenant has online collection off (`rentok-backend/src/controllers/tenant.ts:4618`).
[^21]: Refer & Earn raised independently by Harsh (Rec. 7), Siddhant, and Anurag in the interview corpus.
[^22]: Karan interview: "PGs and student accommodations see higher app engagement, whereas owners managing families or working professionals rely on direct UPI/cash payments and bypass app installation entirely." The Persona doc puts food and attendance at the center of the student's usage and both already have full backends.
[^23]: Persona doc: the long-term settled tenant "actively ignores: Offers, Spin the Wheel, RentPass"; the student and short-term personas list them as low or no touch. The streak/reliability-record direction is Anil's, from the interview corpus.
[^24]: RentOk's white-label WhatsApp Business product, described directly by Sanchay: every property can run its own WhatsApp Business number and logo, used for payment, KYC, and dues reminders. Confirmed in code: `whatsapp_messages_dash` (`rentok-backend/src/entities/whatsappMessagesDash.ts`) stores every sent and received message with `tenant_uuid`, `pg_id`, `sender_phone`, `receiver_phone`, and `template_name`, written by `services/meta/v2TenantMeta.ts` and read by `repositories/whatsappMessageDash.ts`.
[^25]: No route in `rentok-backend/src/routes/tenant.ts` or `src/controllers/tenant.ts` currently exposes `whatsapp_messages_dash` to the tenant app; every existing reader is on the manager/dashboard side (`controllers/others.ts`, `services/meta/*`). One new endpoint, `GET tenant/:uuid/whatsapp-messages` or similar, filtering the existing table by `tenant_uuid`, is the full backend ask.
[^26]: Two systems already exist: `tenant_review` (`rentok-backend/src/entities/tenant_reviews.ts`) holds tenant-authored property reviews with rating, category, and media; `property_review_campaigns` + `TenantReviewService` (`rentok-backend/src/services/reviews/tenantReviewService.ts`, methods `tenantCampaignData`, `tenantReviewCampaignFormData`, `sendReviewMessage`) run configurable survey campaigns sent and answered through a WhatsApp-driven web form today.
[^27]: `GET /tenant/:tenant_uuid/review-details` (`rentok-backend/src/routes/tenant.ts:1102`, handler `getBookingReviewDetails`, `controllers/tenant.ts:27875`) already exists. Confirming its exact response shape and whether it covers both review types above is a first task of the Reviews ideation round, not a new build.
[^28]: No property-, city-, or tenant-type-scoped offer targeting was found in the reward/offer endpoint map (Phase 0 report 05); `POST /rewards/fetchAllRewards` returns a single global pooled catalogue, not scoped by geography or property.
[^29]: Secondary research, tenant journey chapters: documentation is "the highest-anxiety, highest-drop-off chapter in India... This is where trust is won or lost."
[^30]: Friendzo <> RentOk meeting notes: "Key Unlock Mechanism: central, single-tap mechanism for smart gate access utilizing biometric integrations already installed across properties."
[^31]: `lib/presentation/auth/joining/self_invite_widget.dart:324` gates the entire "invite your property" block behind `Constants.appName == 'Smart Tenant App'`, so white-label tenants never see it; the intro sheet's own invite CTA at `:700` is `onTap: () {}`, a no-op.
[^32]: `inviteLink` and `shortLinkName` are parsed from the whitelabel config (`lib/models/whitelabel_res.dart`) and read nowhere in the app.
[^34]: Fintech teardown (phase1/07-fintech-teardown.md), built from source-code extraction of each company's shipped CSS, design tokens, and font binaries. slice owns a commissioned typeface (its binary's name table credits slice, 2019, OFL) while its neutrals are framework defaults; Stable Money licenses four display faces and tokenises border widths at 0.3, 0.5 and 1px with essentially one shadow in the bundle. On rewards after a compulsory payment, see the same report's anti-pattern list.
[^35]: Same teardown: Uni Cards self-hosted a licensed typeface in 2023 and now serves only the system font. The brand face was the first thing cut under cost pressure.
[^36]: `lib/utils/app_colors.dart`: semantic and category colors are getters off the mutable brand fields (for example `breakfastColor` returns `primary`, `tabColor` returns `primary.withOpacity(0.1)`), so they change with the client's brand color instead of holding meaning.
[^33]: Secondary research, tenant journey: the deposit-refund tracker addresses "India's biggest trust gap — 'where's my deposit' is the #1 exit complaint."