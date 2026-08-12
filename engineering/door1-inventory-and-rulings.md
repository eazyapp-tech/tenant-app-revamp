# Door 1 Feature Map — Running Inventory
Completeness check for the final doc. Every item below must end up placed (spine/supporting/parked/cut) or deliberately absent with a reason.

## A. Sources
1. current-app-feature-map.md (14 modules, verified 2026-08-13 spot-check: gating x4, dead self-invite CTA, pgLogo unrendered, eviction rating entity — all hold)
2. Srijan top-10: Theme, Sign-up & Intro, Home, Feature List, Profile, Accounts, Complaints, Messaging, Rewards, Reviews
3. Promotions: Food, Attendance (mandatory)
4. Flexible list (post v6-edit): Polls, Community, Event Planner, Expense split, P2P buy-sell, Browse same-group properties, Meal Planner, To-do, Internships/Jobs (Refer&Earn removed globally — sharing is app property)
5. TAR-03 module ambitions (14 sections incl. white-label + open door)
6. TAR-05: four quadrants, exchange rule, framing library (attendance, entry/exit, KYC, food confirmation, profile completion, police verification, reviews, paying on time), gamification bright line
7. TAR-06 door-3 doc = quality bar + backport candidate source
8. TAR-00 horizon: smart locks, IoT/meters, weather, AI (agreement explainer, post creation), portable rental identity
9. TAR-00 own additions: rent→credit score, tenancy passport, parent window, deposit protection

## B. Sanchay rulings this session (2026-08-13)
- R1: Door-3 services CAN sell into door 1 where they don't offend/undercut landlords. Reframe = THE SWITCHBOARD: property composes the app; per-property feature visibility; landlord can switch off; dynamic. Frame it that way. Experimentation welcome.
- R2: Shared tenancy IS a door-1 requirement (property mediates what door 3 settled P2P).
- R3: Every tenant feature carries its manager-app counterpart line.
- R4: Re-litigate the corpus wherever required; existing material may be stale/wrong; be smart, use him for hard calls w/ recommendation+justification+options.
- R5: Phased process approved: A skeleton → B sweep in 2-3 chunks → C complete picture → go → write once.
- R6: Quality over everything; I am the judge/product owner.

## C. Standing rules in force (from memory/docs)
- Register: plain language, no em dashes, requirements only, no build-state/verified-against commentary in design docs, no code refs in design docs.
- Doc contract: gather-first, framing approval ≠ go, complete-picture-back, verify checkable claims, push back once, user's taxonomy wins, reframe > trim.
- Sweep mode: proactive full sweep, calls marked as calls, batch policy questions once.
- No share-to-unlock/contact harvesting/nagging. No compliance leaderboards. Minors: profiling off (DPDP). No stereotype personalization. No simple mode. No prize wheel on rent. Sponsored tenants never nagged.
- Exchange rule: every burden feature visibly trades give↔get, same screen. Sincerity + transparency tests.
- Channel rules (door 3, likely echo here): each side hears what serves them; renter's private activity never reported to landlord.
- Complaint counts never in passport (anti-chilling); conduct flags only.
- Personalization keys: register × geography × property-type × age. Persona detection signals per TAR-01.

## D. My seven threads (from opening statement) + status
1. Fee has no daily story for non-PG registers → Phase B chunk 1 (rhythm for monthly-loop/family)
2. Door-3 services into door 1 → RULED (R1, switchboard). Design in B3.
3. Shared tenancy in door 1 → RULED (R2). Design in B3.
4. Manager-app counterpart per feature → RULED (R3). Doc convention.
5. Two-voice reputation in door 1: tenant sees/contests own record (eviction rating/blacklist exists in backend) → policy Q for Phase C batch
6. Community/moderation inside a property (owner has opinion) → B3
7. Migration as second first-impression → B1 or mechanics section

## E. Current-app feature checklist (must all be placed)
Boot/WL: connectivity check · WL config fetch+cache · 3 variants · crash/FCM · boot routing (incl. evicted screen)
Auth/Join: phone+OTP · WhatsApp opt-in · new/existing/self-invite routing · multi-property picker+search · join-another-property · self-invite via App ID · room/unit/bed select · join request (name/room/rent/deposit/date) · pending screen (refresh/cancel/resend) · orphan intro carousel
Home: greeting (tenant/parent) · completion badge · announcements/stories · notif bell · account snapshot · pending tasks · electricity meter · complaints snapshot · marketing banners ×2 · quick-action rail · food preview · profile checklist · reward cards · offers/RentPass rail · footer brand · WhatsApp help FAB · first-open interstitials
Money: credits tab (balance/expiry/scratch/history/discounts) · dues tab (pay one/all, autopay banner) · expenses tab (history/refunds/receipt re-download) · pay-now (amount/credit-apply/RentPass upsell/UPI detect/cash OTP handover/share link) · success screen (receipt/reward/share/rating) · failure screen · security deposit view · property switcher
Profile: summary+badge · share profile · renting info · personal details edit (demographics/family/addresses/education/employment/banking/socials) · doc upload+status · rental agreement (view/sign/download) · BV status · roommates (placeholder) · autopay (external) · support contact · move-out entry · my properties · data policy · privacy/logout/delete-data
Food: weekly menu · meal detail · confirmation w/ cutoff · live indicator · QR plate scan · post-meal rating+photo · empty state
Attendance: 3 modes (wifi/manual/smart) · setup wizard · absent/leave+reason · late check-in · history calendar+% · pending requests · guest hosting · parent reminder nudge
Complaints: list/filters/search · raise (category/location/desc/photos/availability/assignee) · AI category · detail+timeline · remarks/images · rate resolved · batch-rate · Property Captain WhatsApp escalation · Tarini chat assistant
Move-out: hub (rules/summary) · raise/modify/extend/cancel · post-move-out rating · remind mgmt · handover OTP · condition checklist+photos · final submission
Services: overview/stats · browse/categories · detail+slots · book · reschedule/cancel · history · QR check-in
RentPass: plan compare · savings calc · benefits · reviews/FAQ · purchase (Android IAP / iOS WhatsApp) · spin wheel · locked-reward upsell · all-rewards browse
Offers: browse/filter · redeemed/expired tabs · detail (code/validity/steps/terms/share) · redeem
Notifications: feed · tap-through (only move-out wired)
Cross-cutting: bottom nav (WL-driven, 4 shown) · deeplinks (web/WA/in-app) · PDF viewer · image viewer/cropper · KYC gate · update prompt · no-network · evicted screen · dev panel
Not-real-today: Messaging (WA only) · Reviews (WA only) · Roommates placeholder · unified rewards (3 overlapping systems)

## F. Door-3 backport candidates (test each through the switchboard + landlord-conflict lens)
- Rent receipts for tax/HRA (per-person HRA receipts) — likely safe, tenant-wanted
- Document vault + agreement extraction/explainer (AI Lawyer) — mostly safe; explainer touches landlord relationship (clause disputes?)
- Police verification standalone — already in door 1 partially
- Credit-score/rent-history reporting, tenancy passport accumulation — safe, strategic
- Deposit protection/move-in record — exists as checklist; door-3 framing (tenant's protection) backports
- Movers/packers, insurance, doctor-on-call, CA services, couriers — safe services
- Splitwise/expense (already on flexible list)
- Budget/expense product — safe
- Cost-of-living companion, trip planner (orchestrated version w/ guest mgmt + entry/exit per TAR-06)
- Meal planner (flexible list; door-3 had it as AI companion)
- Browse properties: SENSITIVE (helping tenant leave). Door-3 lease-end Broker recs = strategic for RentOk, offensive to current landlord? Same-group browse is the safe subset (Srijan's list).
- Community messaging (door-3 had P2P negotiate/coordinate) — in-property version = floormates
- Notice letter / renewal flows — door-1 versions exist as move-out/agreement
- To-do/chores (flexible list + door-3 personal pending tasks rule: NO app-generated pending tasks)
- "It must never feel like work" mechanic — backport as door-1 mechanic?
- Landlord line: N/A (landlord already on platform) but echoes as owner-visibility rules

## B2. Ruling (2026-08-13, checkpoint 1 feedback)
- R7: WEB CHECK-IN MERGES IN. Verified live at Eazypg-marketplace/pages/checkin/[checkinId].js: step-locked journey = KYC (Aadhaar eKYC/OCR/doc upload/parentKyc) → autopay setup (conditional is_autopay, Eqaro bond) → move-in checklist w/ photos (order configurable vs agreement via move_in_property_settings) → agreement e-sign → app download prompt. Journey stands alone on web AND merges into tenant app. One system, two renderings — not two builds.
- Marketplace also already hosts door-3-ish free tools: rent-receipt-generator, receipt-generator, tenant-verification, insurance, CirclePe, Eqaro, esign, rentpass pages. Flag for door-3 alignment + door-1 "before day one" moment.
- R8: Moments frame approved in principle; pushed to "do better" → bookends + loops + threads structure (Before day one · Day one · Every day · Every month · When something needs attention · Living together · The record that grows · The last month).

## B3. Rulings + findings (2026-08-13, round 3)
- R9 DOOR TRANSITIONS (Sanchay verbatim rules): door 3 → door 1 seamless. door 3 → door 2 seamless. door 1 → door 3 seamless. door 2 → door 3 NEVER (white-label sanctity — brand's app never funnels its tenants to RentOk consumer surfaces).
- R10 UNIFIED JOINING FLOW verified: repo eazyapp-tech/unified-joining-flow (React/Vite/TS, active Apr–Jun 2026) = standalone pre-tenancy product. Features: property-listing (listing/detail/room/rental-options/wishlist/location-commute) · property-filter · persona-selection · book-visit (type/date/time, my-bookings, review, cancel) · reservation · onboarding · joining-form (JoiningProfilePage/AddDocumentsPage/JoiningStatusPage = LEAD PROFILE) · confirmed-booking (+AllPaymentsPage) · modify-booking (change room/update move-in/cancel) · user-profile · webcheckin · SubdomainPropertyLoader (per-property subdomains = white-label web). Older Next.js version also live in marketplace (onboarding/[eazypgid]/unified.js: Welcome→Auth OTP→PersonaOptions→ExpandedBookingForm→BookingReview→payment→joining-request→AppDownloadScreen) + backend unified APIs (tenant/unified/otp|details|bookings, unified payment-page).
- FINDING: persona captured at LEAD stage (persona-selection pre-booking) — personalization key exists before day one; lead profile is the record's true t=0.
- FRAME IMPLICATION: unified flow = the shared vestibule between doors. Door 3's finding-a-home and door 1's before-day-one are the same corridor; lead profile → tenant profile → passport is one continuous record. Door 1 map covers from "this property/brand's funnel onward"; open-market browse stays door 3's.

## B4. Door-3 carryover preview calls (full treatment in chunks; presented to Sanchay round 3)
1. Never-feels-like-work → CARRY w/ door-1 amendment: required asks = honest + traded (TAR-05 exchange rule) + never nag twice; optional = door-3 rule verbatim (no app-generated pending tasks; suggestions ignorable free).
2. Magical agreement flow (capture all parties, co-tenant auto-invite, claim-own-entry) → CARRY into before-day-one/documents.
3. Two channel rules → CARRY verbatim, needed MORE in door 1 (landlord present in-app): each side hears what serves them; tenant's private in-app activity never reported to landlord.
4. Deletion policy (one-sided dies w/ account, bilateral signed artifacts survive) → CARRY.
5. Passport rules (mobility-neutral score, verification freshness, complaint-counts-never, contest-before-shareable) → CARRY at record level.
6. Memory-beside-passport → PARTIAL: door 1 builds the memory (life in property), door 3's broker consumes it. Seam, not a door-1 feature.
7. Terms-without-paper → MOSTLY N/A door 1 (terms exist via property records); echo = declared-terms drive everything even where no formal agreement.
8. Structure patterns (moments, named mechanics, deferred/cut tables w/ reasons, spine test) → adopted already.

## B5. Rulings (2026-08-13, round 4)
- R11: Door 1 → door 2 ALSO seamless. Confirmed working transitions: 3→1, 3→2, 1→2, 1→3. Door 2→3 = OPEN QUESTION by explicit request (write down, discuss with team later; his own instinct in this round leaned "works," earlier ruling said never — needs the stakeholder conversation). → Q9.
- R12: 3-4 separate products exist today (marketplace site, unified-joining-flow, webcheckin, payment page product, current tenant app). They all STAY RUNNING as-is. The NEW 3-door tenant app combines ALL their features into ONE seamless journey — complete renting experience and lifecycle — composed per persona/door/property. Current features = current reality, never the limit; everything is being made anew.
- R13: Door 2 browse = limited to the brand's own properties (white-label workflow precedent already exists in unified-joining-flow subdomains). Door 3 browse = the whole RentOk ecosystem. (Door 1 browse default → Q2, refined.)
- R14: PARITY RULE — door 1's feature richness must be comparable to door 3 or better.
- R15: Memory-beside-passport partial carry approved; also works in door 2 (brand-scoped).
- R16: Passport rules carry approved. Terms-without-paper N/A verdict approved.
- PENDING his understanding before ruling: two channel rules (explained round 4), magical agreement flow in door 1 (explained round 4 incl. migration-onboarding use).

## B6. Rulings (2026-08-13, round 5)
- R17 VOICE/CHURN GUARDRAIL: renewal messaging to the tenant must NEVER imply moving out ("plan your move" = banned). Owner reads it as RentOk churning his client. Renewal exists to CONTINUE the stay; tenant-side words help them act on their own agreement, never suggest leaving. Applies to every landlord-adjacent surface. (Renewal mechanism verified live: tenantAgreementRenewal entity, AgreementRenewalService, cron /agreement-renewal, property/renew-agreement, tenant/:uuid/agreement-details, reports — manager-side + pending task; tenant app has NO renewal surface today.)
- R18 COMMERCIAL FACT: tenant app is not sold separately. Manager app subscription bundles manager app + tenant app + unified joining flow + web check-in. Rewrites the fee framing (Q7): the Rs 30-50/tenant/month is a bundle economics question, not a standalone tenant-app SKU. Channel rule 2 approved as stated.
- R19 MAGICAL AGREEMENT, DOOR-1 CORRECTION: the MANAGER uploads/creates the agreement and fills all details. The TENANT NEVER UPLOADS in door 1 (tenant-upload belongs to door 3 only). Door-1 magic = what the manager enters flows to every named person + every workflow. Carry: co-tenants + dependents, multi-party signature, share splits (rent share, deposit share), and RECURRING PACKAGES beyond rent set by property management (food, maintenance, laundry, etc. as named recurring components). None of this fully exists today.
- R20 BOOKING BOT / AI BROKER: merges into door 2 as the brand's own AI broker, scoped to that brand's properties/trees. Door 3 = ecosystem-wide broker. Door 1 = property-scoped assistant (Tarini lineage) — confirm scope in B3.

## B1 SWEEP FINDINGS (2026-08-13) — Before day one · Day one · Every day · Every month

### Verified ground truth added this pass
- ENTRY/EXIT: 8 backend entities (entryExitGates, GatePass, GateSchedules, Requests, PresenceStatus, ActivityLog, Settings, Logs) + visitor entity. Settings are PER-PROPERTY: curfew times (4 time columns, defaults 23:00/21:00/23:30/21:30), approval modes ALWAYS/WARDEN, several on/off smallints, json config. PresenceStatus records tenant lat/long, device_info, approver_name, entry_exit_type, incoming_time. TENANT APP HAS ZERO REFERENCES to any of it.
- DUES ARE TYPED: dueType (per property: name, description, amount, unit_cost, enabled, type) + dueTypeHierarchy + dueTypeBankMapping. Recurring packages beyond rent already have a home. Tenant app uses dueType ONLY for add-on service bookings, never for the money surface.
- PAYMENT PAGE PRODUCT: generatePaymentPageLink + getTenantDetailsForPaymentPage + getPropertyDetailsForPaymentPage + unified payment-page meta = no-login pay-by-link, separate record from app ledger.
- Property archetype fields confirmed on property entity: pg_available_for (225), tenants_preferred (243), property_type (723).
- Tenant entity: notice_period (default 30), under_notice, notice_raised_on, security_deposit, food_preference, food_opted, electricity_bill_reading/date, monthly_income.
- Web check-in is STEP-LOCKED (blocking messages per step); order partially property-configurable (move_in_property_settings, is_autopay).
- Switchboard already exists as FOUR embryos: entryExitSettings · is_autopay/move_in_property_settings · dueType.enabled · navigationMenu (whitelabel). Plus KYC compulsory gate + home section data-gating.

### Calls made (writing in)
W1 Vestibule inheritance: app opens already signed in with vestibule state intact; zero re-entry; download prompt moves to peak-warmth moment, framed as the home in your pocket.
W2 Record starts at lead stage (persona captured pre-booking) — lead profile → tenant profile → passport is one continuous record.
W3 Visit moment designed: directions, what to bring, who to ask for, what-to-check list (renter's protection). VisitTips precedent exists in unified repo.
W4 No walls anywhere: vestibule and first run become skippable-with-consequence-stated, except legally-required-at-that-moment (signature before move-in).
W5 Manager-assisted mode for cash-first/low-literacy: manager fills, tenant confirms by OTP; produces an identical record, never second-class.
W6 Move-in condition record = day one welcome ritual doubling as deposit protection; tenant-led photo walkthrough, countersigned.
W7 Tenant's side of entry/exit: own presence record, own gate pass, own late-entry request, own visitor pre-approval. Transparency rule applied to the most watched feature.
W8 One presence story: attendance + entry/exit unified for the tenant even though two systems feed it.
W9 Money surface itemized by due type: rent + food + maintenance + laundry + electricity shown as named components, per person where shared.
W10 Autopay native and visible: state, next date, amount, pause/change in-app.
W11 Cash payments earn identical receipt + streak + record credit as online.
W12 Pre-tenancy payments (token, first rent, deposit) appear in the same ledger from day one.
W13 Don't fake a daily habit for flat archetypes: excellence at weekly/event-driven + multiplayer features carry them; app never punishes infrequent openers with stale content.
W14 Group application at the vestibule (bachelor-group archetype) + parent as named party from lead stage.

### Deliberately NOT adding (this chunk)
N1 No streak/gamification on entry-exit compliance (gamification bright line: compete on joy never on compliance).
N2 No parent-visible location or live presence by default (autonomy-sensitive; research-gated card 13).
N3 No re-marketing to lead-stage renters who did not move in, absent explicit consent.
N4 No countdown-shaming on dues; no collection-agency tone; no interest/penalty theatre.

## B7. GAP-MINING PASS (2026-08-13, after Sanchay's expand-the-scope correction) — THE INVISIBLE INVENTORY
What exists in backend/manager/web but tenant app never shows. All verified this pass.

### Parent mode (HALF-EXISTS IN THE TENANT APP ITSELF — Sanchay flagged, confirmed bigger than a tab)
- tenant app: PreferenceKeys.isParentApp flag; home + profile greet parent by name (getParentName); complaint card behaves differently for parent; late_checkin has is_parent_informed; guardian name/phone/address fields in profile
- backend: POST /:tenant_uuid/remind-parent (remindParents); parent refs across attendance/entry-exit entities
- web: parentKyc.js component in marketplace KYC
- MISSING: parent login/link flow, parent's own view, consent model. → Named thread: THE PAYER WINDOW (generalization: parent pays for student, company pays for sponsored = same structural role "the payer who is not the tenant"; money surface adapts per payer; autonomy line research-gated per card 13)
- DPDP note: minors = profiling off; parent window ≠ surveillance window.

### My People directory (Sanchay's list; data backing verified)
- roommates/flatmates: NO backend endpoint today; derivable from room/unit allocation (stay_history, room, bed). Tenant app has dead "Roommate details" placeholder.
- co-tenants/dependents: from magical agreement parties (R19).
- property team: teamMember + teamMemberDesignationMap + team_property_designation_map (per-property designations exist). Manager people/team module. Nothing tenant-facing.
- owner details: on property entity. Not shown.
- DESIGN CALL W15: directory organized by NEED not org-chart (something broke → who fixes; late night → warden; money → manager/owner; parcel → reception) + consent-gated peer visibility (roommates opt-in, TAR-06 community precedent: no phone-number sharing, in-app messaging).

### Other invisible machinery (backend exists, tenant never sees)
- stay_history: allocation→eviction timestamps per unit = room-change history → feeds passport + "your time here" memory + goodbye artifact.
- roomInventoryMap: per-room asset inventory (qty, working flag, timestamps) → move-in record pre-fill ("what's in my room"), condition checklist grounding.
- invoices + invoiceNumberConfig + getTenantSDInvoices: GST/SD invoices exist → tenant-facing documents.
- stampAgreements: stamped agreements entity.
- tenant_eqaro_bonds + eqaro_payments: deposit bond/guarantee integration LIVE (door-3 deposit-protection parallel already in door 1's backend).
- tenant_payment_savings: savings ledger (RentPass savings claims).
- taskSchedule/taskInstance/taskTemplate (+taskScheduleTeamMember): property task system → could answer "when is cleaning coming" (tenant-visible schedule, NOT tenant task creation).
- meter + roomMeterMap + managerMeterRecharge + frontierRechargeHistory: per-room meters.
- message_sender (manager module): property→tenant broadcast exists manager-side → the Messages moment's sending half.
- payment_qr (manager): property payment QR → cash-first tenants scan at office; receipt auto.
- joining_poster (manager): printable QR join poster EXISTS = the owner-handover moment's physical artifact, already built manager-side.
- review_module + review_module2 (manager): review collection manager-side.
- media (manager): property photos/media library → food photos, property gallery sources.
- short_link, social_proof, wishlistUsers: growth plumbing.
- CORRECTED FALSE LEAD: manager "eventsmanager" = analytics SDK wiring, NOT event planner. Do not cite as event feature.

### Standalone principle (Sanchay, this round)
- The new app = ONE app absorbing all 3-4 products' features; works standalone with zero dependency on the current products; they keep running for their own users; every transition (3→1, 3→2, 1→2, 1→3, direct entry into any door) seamless inside the one app.

### New calls from this pass
W15 directory-by-need (above). W16 Parent/Payer window as named thread. W17 room inventory pre-fills move-in record. W18 stay_history feeds record/goodbye. W19 property task schedule surfaces as "upcoming in your home" (read-only). W20 joining_poster becomes the designed handover artifact. W21 Eqaro bond surfaces in deposit journey where property uses it. W22 payment QR path earns same receipt/record (cash-first dignity).

## B2 SWEEP (2026-08-13) — When something needs attention · The record that grows · When the agreement ends
Register: ambition-first per Sanchay's correction; existing machinery = feasibility hints only (noted in parens for engineering, never in design doc).

### STRUCTURAL REFRAME (presented for ruling)
W23 Moment 8 renamed: "The last month" → "WHEN THE AGREEMENT ENDS" — a fork, not a farewell. Renewal fork FIRST (stay: terms reviewed, escalation shown plainly, renewed in a tap or two) then notice fork (go: deposit journey, goodbye). Structurally embodies R17: the app never assumes or suggests leaving. Sponsored variant: company offboarding. 

### When something needs attention — calls
W24 Complaints chat-first, named human + honest expectation ("told Rajesh the electrician; most fixes here happen in a day"), visible progress, escalation ladder visible. (hints: escalate_v2, email digest services exist)
W25 SHARED COMPLAINT (new idea): floor/building-level issues (water, wifi, lift) become one collective issue neighbors join instead of N duplicates; everyone gets status; kitchen-table social proof. Consent: joining is visible, filing stays individual-private by default.
W26 Repair-with-cost flow for family-flat/1RK archetypes: repair → who-pays known upfront (property duty vs tenant) → if tenant paid, reimbursement or rent-adjust path visible. (door-3 maintenance-log echo, property-mediated; hints: propertyEvictionCharges rule shapes, dues rails)
W27 Services: honest slots, real cancellation terms, ratings with consequences; exists only where switchboard enables.
W28 Messages = organized memory of everything the property says (announcements, reminders, the WhatsApp history) with every item tappable to its action; announcements never fake-new. (hints: manager message_sender = sending half; whatsapp_messages_dash + read-endpoint ask stands)
W29 Pulse/reviews in-app with visible consequences ("you said water pressure; fixed Tuesday"); answers reach a person; acting-on-feedback made visible to tenants. (hint: tenant_reviews supports threading via parent_review — two-voice precedent)

### The record that grows — calls
W30 Profile = three layers (my home / my documents / my account), honest statuses everywhere; edit rarely needed, never a wall.
W31 Document home: agreement readable + plain-language explainer; receipts, GST/SD invoices, verification certificates all downloadable, beautiful, shareable. (hints: invoices, stampAgreements, getTenantSDInvoices exist)
W32 Streaks personal + merciful (rent on-time, attendance), milestones celebrated small, breaks mended kindly; feed the record; never compliance-competitive (bright line).
W33 ONE rewards system on the record; kill the three-system split; offers scoped city/property-type/register/age; graceful shrink to zero (empty-state-safe); minors curated only. RentPass fate = Q3.
W34 The record itself visible to the tenant: months on time, streaks, verifications, room history, "your time here" memory (photos, milestones). See-your-own-record always; contest path per Q1. Complaint counts never in it.
W35 Memory artifacts: year-in-this-room moments, the goodbye keepsake; memory private-first, feeds passport only by choice. (hint: stay_history)

### When the agreement ends — calls
W36 DEPOSIT TERMS VISIBLE FROM DAY ONE (new idea, kills the #1 dispute at the root): deduction rules the property defines are shown at move-in, sit quietly in documents, and the deposit journey at exit itemizes against the move-in record + room inventory. No surprise rules at exit. (hint: propertyEvictionCharges = per-property named rules already data)
W37 Deposit journey end-to-end: held → inspected (photos, itemized vs move-in record) → agreed → refunded with date → done. Cash refunds recorded with same dignity. (hints: settlements, adjustDeposit, eqaro bonds)
W38 Move-out checklist = mirror of move-in record, tenant's protection framing.
W39 Handover = designed closure ritual (OTP exists; make it a moment); goodbye carries the memory artifact + passport-ready record + open-door handoff (only by tenant's own act, R17).
W40 Group endings: member-swap property-mediated (consent for people, records for money, re-sign carries landlord consent), everyone-leaves = shares settle per ledger. (R2)
W41 Both-way rating at exit: tenant rates property/management; management's rating of tenant enters the record ONLY as witnessed facts + see-and-contest (Q1); RentOk never referee of subjective verdicts (two-voice rule).

### Not adding (B2)
N5 No public complaint feeds/leaderboards of properties inside door 1 (door-3 reputation is its own surface).
N6 No move-out upsell of door-3 services beyond the single open-door handoff moment.
N7 No streak-loss penalties touching money, ever.
- Q16: Payer window consent model — who links whom (tenant invites payer? payer initiates? manager sets at move-in?) and what payer sees by default (recommendation: dues/receipts/agreement yes; presence/complaints/community never without tenant consent; minors separate rules).
- Q17: Roommate directory visibility default — opt-in vs on-by-default-within-room (recommendation: opt-in, names only until mutual).
- Q18: Team directory depth — personal numbers masked behind in-app call/chat? (recommendation: yes, protects staff too).
- Q10: Entry/exit tenant surface depth — full presence history and curfew rules visible to tenant, or summary only? (Recommendation: full, per transparency rule.)
- Q11: Cash-first record parity — confirm cash earns streaks/record identically. (Recommendation: yes, else the record economy structurally excludes the poorest register.)
- Q12: Sponsored tenant's empty monthly loop — what fills it?
- Q13: Pre-tenancy payment ledger continuity (data ask across products).
- Q14: Group application at vestibule — build in door 1 or door 3 only?
- Q15: Lead-stage record retention and consent for renters who never moved in.
- Q9: Door 2 → door 3 transition: open by request. Earlier ruling = never (white-label sanctity). Round-4 instinct = might work. Needs team discussion; someone may have another opinion. Do not let this get lost.
- Q1: Tenant sees/contests own eviction rating/blacklist entry? (door-3 ruled "sees before shareable" for passport; door-1 version?)
- Q2: Browse-properties default: same-brand only by default, all-RentOk opt-in per landlord? Lease-end recommendations on/off default?
- Q3: RentPass fate: fold into unified rewards? Plan-based membership vs record-based rewards tension.
- Q4: Spin wheel: TAR-00 bans prize wheel attached to rent; RentPass spin exists generally. Keep anywhere?
- Q5: Parent window scope for door 1 (research-gated per card 13, but skeleton needs a slot).
- Q6: Switchboard governance: who sets defaults, what's never-off (money? complaints?), what's landlord-only vs RentOk-only toggle.
- Q7: Fee: what is actually behind the Rs 30-50 — whole app? services? Who pays (tenant vs owner passes through)?
- Q8: Doc identity: TAR-07 as the door-1 map? Relation to TAR-03 (ambitions) stated how?

## H. Structure skeleton (proposed, Checkpoint 1)
Moments: Arriving · The rhythm of the day · The month and the money · Being heard · Living together · Being known · Moving on
Cross-cutting: the switchboard · exchange rule (TAR-05 pointer) · record accumulates everywhere · manager counterpart lines · migration
Phase B chunks: B1 = Arriving + rhythm + money (+ fee story) · B2 = heard (complaints/services/messages/reviews) + known (profile/docs/rewards/passport) + moving on · B3 = living together (community/shared tenancy) + switchboard + door-3 backports + white-label seam

## B8. Ruling (2026-08-13, mid-B2): SENIOR / ASSISTED LIVING
- R21: Senior assisted living = a door-1/2 archetype (old-age homes, assisted living, managed senior properties). The linked-family concept FLIPS: resident = elderly parent; linked account = adult child living elsewhere ("parent app for children").
- CONSEQUENCE: "Payer Window" generalizes to THE FAMILY WINDOW — one linked-account system, role-configured per archetype: parent<->student (PG), company<->sponsored, adult child<->elderly parent (assisted living). Same machinery: link + consent + role-scoped view + payer rails. Resident autonomy rules still govern (elderly resident is an adult; their consent controls visibility; care-relevant defaults may differ per property type + family agreement).
- Archetype sweep additions: attendance/presence reads as WELLBEING signal ("mom is okay today") — the burden feature becomes the product for the family; food = nutrition visibility; complaints raisable BY family on behalf; payments by the child; book-a-visit machinery = family visit planning; directory = care staff prominent.
- Archetype list now SEVEN: PG bed · co-living room · 1RK · serviced apartment · bachelor-group flat · family flat · senior assisted living.
- NOTE: G section heading was consumed by an edit; Q9-Q18 items above remain valid, heading restored here:

## G (continued). Open policy questions
- Q19: Family Window care defaults for assisted living — what does the adult child see by default (wellbeing signal? presence? health-adjacent info?) vs resident-consented extras. Sensitive: elderly autonomy vs family peace of mind. Research + property-policy gated.

## B3 SWEEP (2026-08-13) — Living together · The switchboard · The service shelf · The white-label seam
Verified this pass: NO split/poll/community/event/transfer machinery exists anywhere (pure greenfield); whitelabel parses style/splashScreenMedia/inviteLink/shortLinkName, all unused; micrositeUsers exists.

### Living together — calls
W42 Community = property-scoped, every member a verified resident (the moat vs WhatsApp groups: no strangers, no spam). Residents' voice, NOT the property's megaphone (property speaks in Messages; community belongs to tenants). Moderation: report/block (door-3 precedent) + manager as last resort; property can switch community off (switchboard). Default on for PG/co-living/hostel/senior, default off family flats.
W43 Polls: two kinds — property polls (menu vote feeds the kitchen = food integration, the killer multiplayer) and resident polls (movie night, AC temperature). Opt-in, light.
W44 Expense split: room/flat-scoped peer expenses (groceries, cook, shared wifi) distinct from property dues (which split via agreement shares). Records + UPI handoff, never a wallet. Ledger continuity with shared-tenancy flows (member swap, deposit shares).
W45 P2P buy-sell within property/brand: verified-resident marketplace; natural hook at the leaving fork ("selling anything before you go?").
W46 Chores: shared rotation lists for bachelor-group/co-living (door-3 vignette); personal to-dos remain tenant's own only (no app-generated tasks rule holds).
W47 Events: property-hosted + resident-created-with-approval (Diwali dinner, movie night); senior-living variant = family-visible events calendar. (door-3 v5 explicitly deferred polls+events TO doors 1/2 — this is their home.)
W48 Meal planner: where mess exists → menu voting inside Food; self-cooking archetypes → door-3 companion via service shelf. Not a standalone module.
W49 Jobs/internships (Srijan flexible item): PARKED — not living-together core; revive condition = partner supply + student-register demand in research round.
W50 Intra-brand transfer (NEW, replaces "browse same-group" as a workflow not a browse): job moves you to Pune → request transfer to the brand's Pune property in-app → passport/record/deposit conversation travel → vestibule replays only what changed. No machinery exists today; genuinely new. The brand keeps the tenant; the tenant keeps the record.

### The switchboard — design calls
W51 One per-property composition system replacing today's four fragments. Every module/feature/service = a switch (on/off/default + audience rules) set by the property in the manager app, within RentOk-set bounds.
W52 NEVER-OFF FLOOR (my call, needs Sanchay ratification → Q20): money, documents/agreement, complaints, profile = the trust floor no landlord can hide. Community/polls/services/door-3 shelf/entry-exit/attendance = property choice; if a watching feature is ON, transparency rules bind automatically.
W53 Composition is also personalization: enabled modules per property = property-type proxy (locked earlier in project); switchboard state feeds register detection.
W54 Switchboard IS the white-label composer: door 2 = same system + brand voice + brand bounds.

### The service shelf (door-3 services in door 1) — calls
W55 Two shelves, never mixed (door-3 rule carried): property services (from your property, bookable slots) vs renting-life services (RentOk ecosystem: CA/tax help, insurance, receipts/HRA, credit-score building, doctor-on-call, couriers). Each shelf labeled by who provides.
W56 Context-first surfacing: movers appear in the leaving fork and arriving moment, not as shelf ads; CA services surface at tax season + receipt downloads; insurance at move-in. Shelf exists for deliberate browsing; moments do the introducing ("the tool ends where the workflow begins" carried from door 3).
W57 Landlord-conflict categories default per RentOk policy, property can adjust within bounds (Q2 refined: browse-other-properties default-off inside door 1 standard app? my rec: off; discovery lives in door 3 and the tenant can always walk through the open door themselves).

### The white-label seam — calls
W58 Every moment carries a one-line "in the brand's voice" note in the doc; framings that lean on sibling features name their fallback (TAR-05 rule operationalized).
W59 Door 2 = brand-scoped everything: brand AI broker (R20), brand community, brand transfer network (W50 is door 2's killer feature), brand microsites/subdomains as the web front door, joining posters in brand identity.
W60 RECORD PORTABILITY ACROSS DOORS (structural): the tenant's record/passport belongs to the tenant, never hostage to a brand app; leaving a door-2 property with your record intact is a tenant right and a RentOk platform guarantee. (Q9 about door-2→3 in-app transition stays open; record portability is NOT open — it is the floor.)
W61 AI assistant scopes: door 1 = property-scoped assistant (Tarini lineage: complaints, agreement explainer, how-do-I, when-is-dinner). Door 2 = brand broker + assistant. Door 3 = ecosystem broker. One architecture, three scopes, never cross-scoped.

### Migration + mechanics
W62 Migration = second first impression: existing tenants land in the new app with everything already there (zero re-entry, records intact), a designed welcome-back, and one "what's new" moment. Old app users are the FIRST audience, not an afterthought.

### Not adding (B3)
N8 No cross-property public community (door 1 community = your building only; city-level community is a door-3 question).
N9 No anonymous posting in community v1 (verified-resident identity is the safety model; anonymity revisited only with research).
N10 No jobs/internships board (parked, W49).
N11 No money custody in expense split (records + UPI handoff only).

### New questions
Q20: Ratify the never-off floor list (money, documents, complaints, profile).
Q21: Community default-on set (my rec: PG/co-living/hostel/senior on; family flats off) and manager moderation powers (delete posts? or only escalate?).
Q22: Intra-brand transfer — door 1 standard app too (RentOk-wide transfer between any two RentOk properties?) or door 2 only? (My rec: both; RentOk-wide transfer is the standard app's version of the brand network effect.)

## B9. Rulings (2026-08-13, round on shared renting + flags)
- R22: Shared renting structures (co-tenants, dependents, family renting, shared tenancy) DO NOT EXIST in any current system and ARE WANTED — all shared-tenancy calls (R2, R19 multi-party, W14, W40) are new builds, confirmed.
- R23: Live app already hides features per property (offers, RentPass) based on features/integrations — switchboard formalizes an existing operational practice, not a new concept. Validation, not invention.
- R24: Group/shared booking, visits, search, conversation absent from unified joining flow. Sanchay wants them in DOOR 2. Door 1: delegated to me ("okay not to have it, I guess — what do you think? up to you").
- MY DECISION (D1, per delegation, overridable at Phase C): SPLIT the concept. Group DISCOVERY (searching together, shared shortlists/wishlists, group conversation about options, group visits across properties) = doors 2 and 3 only — door 1 has no browse, so nothing to search together. Group APPLICATION (several people booking one flat/room at a known property: joint application, shared visit to THE property, group joining forms, one agreement with all parties) = ALL doors including door 1. Reasons: (a) bachelor-group + family archetypes arrive at door 1's vestibule AS a group; (b) the multi-party magical agreement needs a group booking upstream or the group gets manually recreated behind one lead booking, which is today's broken reality; (c) same machinery door 2 needs anyway — build once, scope discovery per door. Q14 CLOSED by this decision.

## B10. Rulings (2026-08-13, Phase C review round 1)
- R25: INSTITUTE HOSTELS = major Family Window archetype: coaching/institute-partnered hostels (FIITJEE, Allen, PhysicsWallah etc.) house UNDERAGE tenants; properties SELL the parent app as part of their service (like senior living). Consequences: (a) minor variant of Family Window = guardian-controlled (DPDP: profiling off, guardian consent legally required, curated content); (b) Family Window becomes a SALES FEATURE for doors 1+2 (property offers "parents get an app"); (c) archetype list gains: institute hostel (minors). NOTE flagged Q23: partnered institute may be a 4th party wanting aggregate visibility (batch-level, never individual without guardian+institute agreement) — parked as question.
- R26: PLATFORM FEE RULING (corrects my Q7 rec — TAR-00 already said this, I contradicted the brief and was called out): door 1 AND door 2 tenants WILL pay platform fee Rs 30-50/mo. Driver: govt MDR charges coming on UPI (subsidy ending); fee covers MDR on rent/bill payments via app; without it payments business unsustainable. Zomato/Swiggy platform-fee strategy as reference or better. FEE MUST BE JUSTIFIED BY VALUE: supporting/lifestyle layer must be rich enough that Rs 30-50 is obviously fair.
- R27: Supporting layer needs LIFESTYLE-GRADE richness in doors 1+2 (not just PG utilities) to justify the fee. Design task: the fee-worthy bundle.
- LEAD DATA (Q15): Sanchay inclined to RETAIN; asked for drawbacks. My position: convert-don't-retain — the lead who never moved in becomes a door-3 user; their profile lives in THEIR account (user-owned retention, DPDP-clean purpose, commercially better than CRM retention). Drawbacks of raw indefinite retention: DPDP purpose-limitation exposure esp. KYC docs of non-customers (pure breach liability, zero revenue), creepy-factor, stale-data weight. Sensitive docs auto-expire sooner than profile basics.
- Q16 and Q2 explained this round (see chat); rulings pending his read.
- Platform section: agreed as recommended (Q20 floor ratified, Q21, Q22, Q8 accepted; Q9 stays open).
- Record section: agreed as recommended (Q1, Q10, Q11, Q13 accepted).
- Commerce: agreed except fee (R26); Q2 pending explanation; Q3/Q4/Q12 accepted.

## B11. Rulings (2026-08-13, Phase C review round 2 — ALL QUESTIONS NOW RULED)
- R28 FAMILY WINDOW MECHANICS (Q16 CLOSED, his spec):
  (a) Parent app = switchboard-gated feature, property-controlled from manager app.
  (b) Linking workflow: tenant self-initiated — tenant adds parent details (BOTH mother and father: names, phones, emails) → link shared to parents → each parent verifies THEMSELVES via eKYC (web check-in pattern) → parent logs into parent app. Manager can also add from manager app; same verification process either way.
  (c) Gatekeeper rules: MINOR-parent → tenant NOT gatekeeper; property management or the parent side is; tenant can at most request. Adult-parent → tenant can be gatekeeper. PROFILE LOCK (existing concept, verified: updateTenantProfileLockStatus endpoint) → when locked, management is gatekeeper for changes; tenant only requests.
  (d) Visibility scopes (payer sees dues/presence/complaints/community): ENTIRELY configurable from manager-app switchboard; we ship suggested defaults per relationship (minor-parent / adult-parent / senior-assisted).
  (e) Minor+parent: agreement signing + parent KYC already required in a way today — the workflow formalizes it.
- R29 Q2 CLOSED: browse-other-properties off in door 1 as recommended.
- R30 Q15 CLOSED: lead data RETAINED — no problem, but framed and positioned purposefully (the convert-to-account framing serves this).
- R31 FEE CLOSED: fold into subscription (platform membership, RentPass reborn as the fee tier; flat monthly, absorbs MDR, zero per-payment charges, never gates trust floor, follows the rails, sponsored rides company bill).
- STATUS: every Phase C question ruled or deliberately parked (Q9 team, Q23 institute window parked). AWAITING EXPLICIT CONTENT-GO to write TAR-07 once.

## B12. v2 ROUND (2026-08-13): approvals + archetype walk + market research
- R32: Q24-Q28 ALL APPROVED as recommended (legal general-in/dispute-door-3, refer-a-tenant owner-bounty paid-after-first-rent rent-credit default, ack on critical notices only, balances-not-wallet, WhatsApp transactional fixed + channel choice for rest).
- R33: Sanchay's 16-item additions round = 6 systems (connected home, money completed, property's voice 3-channel, local layer, owner-funded growth, activity log) + agreement flow correction (manager adds core tenants/parties; tenant fills dependents, core tenant + manager approve).
- R34: Archetype GENERATIVE walk (12 new): term billing periodicity · plan changes mid-tenancy · room/bed change within property · leave/outpass + mess rebate + room hold · term closures/academic calendar · house facts card · parking · guest charges · anti-ragging/safety statutory display · society layer for flats · amenity booking · stay extension (serviced).
- RESEARCH FINDINGS (verified via web, 2026-08):
  * Stanza: weekly meal PRE-selection + per-item feedback, cafe orders, VAS opt-in/out (validates plan changes), late-night check-in informing loved ones (validates), digital KYC.
  * MyGate: DOMESTIC HELP attendance + arrival notifications + verified-help discovery + monthly payments (flats archetype gold), delivery/parcel management, SOS broadcast, amenity booking.
  * Hostel software (SpaceBasic et al): outpass w/ instant parent alerts (validates), absence→parent notification, QR/biometric attendance, HEALTH RECORDS (institutional), automated invoicing.
  * LifeLoop (senior): WEEKLY FAMILY DIGEST pattern (digest > live surveillance — fits our autonomy stance), event-attendance visible to family, photo/message exchange staff-resident-family.
  * Zolo: referral up to 25k (validates refer-a-tenant scale), weekly events, zero-deduction refund as marketable promise, biometric access.
  * Bilt: free rent reporting to all 3 bureaus (validates credit), RENT DAY = 1st-of-month branded benefits moment (transfer bonuses, experiences, win-free-rent) → our "celebrate the rent" promise gets its mechanism.
- NEW FROM RESEARCH (W63-W70): W63 domestic help layer for flats (arrival notifs, attendance, payment records, verified discovery via local layer) · W64 parcel/delivery notifications at reception · W65 weekly family digest as Family Window default rhythm (digest-first, live-view by consent) · W66 Rent Day monthly member moment · W67 meal pre-selection for the week + cafe ordering where property has canteen · W68 emergency health card opt-in (blood group, allergies, emergency contact) + institutional health-log DEFERRED (privacy design) · W69 enforcement-without-shame positioning: management gets accurate counts/alerts/who's-inside (fire-safety list) on manager side; tenant side stays dignified — the institutional sales pitch · W70 attendance may ride property's QR/biometric infra where installed (device-agnostic).
- MGMT/INSTITUTE ANGLE synthesized into W69 + switchboard institutional composition (academic calendar, outpass rules, term billing).
