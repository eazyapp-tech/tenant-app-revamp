---
title: TAR-03 Problem Hypotheses — What the Overhaul Must Solve
date: 2026-08-11
tags: [rentok, tenant-app, revamp, research, hypotheses]
owner: Sanchay
status: v1-for-validation
---

# TAR-03 · Problem Hypotheses · What the Overhaul Must Solve

> Companion to [[TAR-01 Brief]] (the bet) and [[TAR-02 Tenant App Design Language]] (the system). This document is the input to validation — UAT, tenant interviews, internal interviews, surveys — not a settled verdict. Research instruments derived from it live in [[TAR-04 Research Kit]].

**How to read it.** Every claim carries an evidence tag:
- **[PROVEN]** — verified in the code or measured directly. Needs prioritizing, not validating.
- **[OBSERVED]** — reported in field visits or team interviews. Real, but from a small sample; validation sharpens frequency and severity.
- **[INFERRED]** — my read of the flows as a designer. The most likely place I am wrong; treat as a question, not a finding.

**Ranking axis, decided:** trust first, adoption second. A problem that breaks trust inside a flow tenants already use outranks everything else, because it loses users today and poisons the platform-fee conversation tomorrow.

**The overhaul framing, decided:** this is a complete redesign, not a patch list. Broken things below justify the overhaul; they do not define its ceiling. Each module ends with the question the redesign must answer, which is always bigger than the fixes.

---

## Part 1 — The systemic layer: trust debt that lives in no single module

The biggest problems are not in any feature. They are in how the app talks, fails, and renders — everywhere at once. A module-by-module redesign that skips this layer repaints a cracked wall.

**S1. Money is rendered wrong. [PROVEN]** Amounts appear as `₹12500.0` — raw number-to-text with no Indian formatting anywhere in the app, and digits that do not align in columns. On the surfaces where trust is decided, the numbers themselves look careless.

**S2. The app breaks at ordinary text sizes. [PROVEN]** The UPI payment row fails when a user moves the system font slider to its top notch — before accessibility settings are even involved. In release builds the failure is a silent clip: content just disappears. Money screens must survive 2× text, full stop.

**S3. Failure has no design. [PROVEN]** Four different toast mechanisms; raw exception text shown to tenants; loading dialogs that never dismiss on error paths, leaving the tenant staring at a spinner after a failed payment; whole flows (payment sheet, UPI rail, profile screens) with no error state at all. And no vocabulary anywhere for offline or stale data — the states our weakest-connection users live in most.

**S4. The app is invisible to assistive tech and silent to the hand. [PROVEN]** One screen-reader annotation in 498 files; icon buttons announce as "button" with no name; zero haptic feedback anywhere, including payment success; animations never respect reduce-motion.

**S5. The white-label promise is structurally broken. [PROVEN]** A client's brand color mostly never reaches the screen; ~41% of color decisions are hardcoded hex. Worse: the meaning colors derive from the brand color, so a red-branded property cannot visually distinguish paid from overdue. The property's own logo — the one per-property brand element — is fetched, cached, and rendered nowhere.

**S6. The wrong words at the wrong moments. [PROVEN]** A payment failure screen shipping placeholder copy ("June Rent", "test description by example example…"). A network error that tells a tenant "you may have been evicted." A move-out WhatsApp message that sends internal key names instead of the tenant's actual details. English only, everywhere, for an audience that includes tenants who read Hindi first.

**The overhaul question for this layer:** these are not fixes to schedule after the redesign — they are what the design language exists to make impossible. TAR-02's token system, state matrix, and voice rules are the systemic answer; every module below inherits it.

---

## Part 2 — Module by module

Modules appear in trust×adoption order, not menu order. Depth is deliberately uneven: the core four (Money, Onboarding, Home, Complaints) carry the most; modules most personas ignore get less.

---

### M1. Accounts / Money — the trust core

**The job:** answer "what do I owe, is it paid, and can I prove it" — for every register including the cash-first tenant and the sponsored tenant who has never seen a due.

**Broken today:**
- Receipt delivery fails: "Download Receipt" hands off to a WhatsApp send that frequently never arrives, leaving tenants without proof of payment. **[OBSERVED — strong, multiple sources]** The in-app regeneration path can strand the user on a stuck loader when it errors. **[PROVEN]**
- The payment failure screen shipped with placeholder text, an invalid color constant, and a crash path for cash payments. **[PROVEN]**
- The payment sheet impersonates a full page without being one — system back closes the whole flow instead of stepping out of it. **[PROVEN]**
- The success screen is four screens in one (confirmation, receipt, rewards, rating prompt), diluting the one moment that matters. **[PROVEN]**
- Credit-card surcharge was not disclosed before payment; high-value UPI stayed enabled above ₹1 lakh. Both flagged internally; current status needs confirming. **[OBSERVED]**
- Three tabs (cashback / dues / expenses) bury the single question every tenant arrives with. Autopay hands off to an external browser mid-trust-moment. **[INFERRED]**

**The overhaul must answer:** what does a money surface look like that a tenant would *show someone*? The receipt as a designed legal artifact (tenants genuinely need it — tax, police verification, proof of address), the rent-paid moment as the month's emotional peak, a ledger so clean it reads as a bank statement, and cash flows treated with the same dignity as UPI.

**Research must validate:** how often receipts fail and what tenants do next; whether tenants understand the three overlapping credit/cashback/reward systems (hypothesis: no); the cash-vs-UPI split by property type; what "proof of payment" tenants actually need and where they send it.

---

### M2. Onboarding & Auth — the adoption gate

**The job:** get a tenant from install to "this is my home's app" in one sitting, with the owner's push converted rather than wasted.

**Broken today:**
- First-time UX is the single most documented blocker: the attendance setup sheet's final button stays disabled with no explanation of why; step links styled like plain text are not recognized as tappable; completing a step gives no feedback. Field pattern: existing users fine, nearly all new users struggled. **[OBSERVED — strongest finding in the corpus]**
- When smart attendance is on, a brand-new user is pushed into a setup screen they cannot leave — a hard wall on first open. **[PROVEN]**
- Tap targets in the login flow are shrunk below minimum; the OTP screen allows double-submit and has no SMS auto-read; the login screen bypasses the design system entirely. **[PROVEN]**
- A tenant who hits an ordinary server error at boot is shown the *evicted* screen — "you may have been evicted" as a response to a network hiccup. **[PROVEN]**
- The waiting-for-approval state is a dead end: no auto-refresh, no property identity, no sense of progress. **[PROVEN]** The intro carousel exists in code and is unreachable. **[PROVEN]**
- The invite-your-property flow — our warmest owner-acquisition channel — is hidden from all white-label tenants and its CTA does nothing. **[PROVEN]**

**The overhaul must answer:** what does *arriving* feel like? The owner shows a QR at move-in; the tenant lands in a first run that greets them with their building's name and logo; joining reads as being welcomed home, not filing paperwork. The waiting state becomes "asking {property} to let you in," with the property's identity visible.

**Research must validate:** where exactly the funnel loses people (need install→login→join→first-week numbers, even rough); what share of new tenants hit the smart-attendance wall; whether the owner-handover assumption holds — do owners actually sit with tenants at move-in, and what do they say about the app?

---

### M3. Home — where the concept proves itself

**The job:** one glance answers "is anything wrong, what's next" — and the screen visibly belongs to *this* property and *this* tenant.

**Broken today:**
- The stories ring looks active even when nothing is new — a signal that cries wolf daily. **[OBSERVED + PROVEN]**
- The "pending tasks" section is empty on every cold open because its data is never fetched from home. **[PROVEN]** Reward cards render clipped. **[PROVEN]** The profile-status card tells tenants with incomplete profiles that they're complete. **[PROVEN]**
- The same data is fetched two and three times per open; a timer leak makes the promo carousel accelerate the longer the screen is left open. **[PROVEN]**
- Properties without an electricity meter still get an electricity card saying there's no data. **[PROVEN]**
- Twelve sections of equal visual weight with no hierarchy — nothing is the headline. **[INFERRED]** Section order is compiled into the app; the backend cannot reorder or tailor it. **[PROVEN]**

**The overhaul must answer:** the composable home from TAR-01 — hero facts ("Room 302 · ₹8,500 due in 4 days"), a live strip for now-moments (meal being served, spin available), sections chosen and ordered by register, the property's name and logo leading. What earns a place on this screen, per register, and what does the *sponsored* tenant — who should never be nagged about dues — see instead?

**Research must validate:** what each register actually checks daily (hypothesis: student = food + gate; professional = dues + receipts; family = nothing daily, which is fine); scroll depth on the current home (which sections are ever seen); whether tenants notice or value the stories/announcements at all.

---

### M4. Complaints — the trust-repair loop

**The job:** make "something's broken in my home" feel heard within seconds and visibly moving within hours. This is where the app either beats the paper register or loses to it.

**Broken today:**
- Tenants look for complaints under Profile, not Tickets — the entry point is mislabeled for how tenants think. **[OBSERVED]**
- The home complaint card refreshes a different data copy than pull-to-refresh updates — the list can silently show stale state. **[PROVEN]**
- Filing is a 1,400-line form with dropdown taxonomies; the availability window is requested from four different places. **[PROVEN]**
- Long-term tenants stop filing when past complaints sat unresolved — trust decays with history. **[OBSERVED]**
- Meanwhile Tarini (the AI chat) is the best-crafted screen in the app and can already file and track tickets conversationally. **[PROVEN]**

**The overhaul must answer:** does conversational filing become the *front door* (tap "Wi-Fi down / AC / water / type it myself," Tarini handles the rest), with the form as fallback? And what does a dignifying confirmation look like — "We've told Rajesh (electrician). Most fixes here happen within a day" — versus today's ticket number?

**Research must validate:** the real filing split (app vs WhatsApp vs paper vs walking to the warden); whether chip-first/conversational filing feels faster or slower to actual tenants; what update cadence rebuilds trust after a bad experience; whether tenants trust an AI intermediary with a complaint about their home.

---

### M5. Profile, Documents & Agreement — the paperwork chapter

**The job:** hold the tenant's identity and paperwork with bank-grade care. Research says documentation is the highest-anxiety chapter of Indian tenancy — this is where trust is won or lost.

**Broken today:**
- Profile edits fail to save (father's phone, university fields reported specifically). **[OBSERVED — root cause not yet isolated in code; validation should include a repro attempt]**
- Uploading documents from the gallery crashes the app. **[OBSERVED]** Uploads give zero feedback — no progress, no success, no failure; fire and forget. **[PROVEN]**
- Agreement signing regularly fails to load or errors out. **[OBSERVED]** Signing happens rotated sideways on a portrait screen. **[PROVEN]**
- The "Profile 100% Completed" indicator lies (inverted logic). **[PROVEN]** Document verification status is only discoverable by tapping a badge that shows a toast. **[PROVEN]**
- The error-recovery path for a failed profile load is a button that wipes all local data. **[PROVEN]**
- Three parallel profile screens exist in code; the live one has the worst validation of the three. **[PROVEN]**

**The overhaul must answer:** the three-tier structure from the research (My Home / Documents & KYC with honest per-document states / Account & Support), and the agreement as a first-class object — viewable, explainable ("what does clause 4 mean?" via AI), shareable. What would make a tenant *confident* their paperwork is safe here?

**Research must validate:** where KYC actually stalls (which document, which step); whether tenants know their agreement lives in the app at all (hypothesis: most don't); which profile fields anyone ever edits after day one.

---

### M6. Move-Out — the deposit story

**The job:** end the tenancy with the deposit story resolved in daylight. "Where's my deposit" is India's #1 exit complaint; this module is the app's best future marketing or its worst review.

**Broken today:**
- The legacy move-out path sends the property manager a WhatsApp message containing internal placeholder names instead of the tenant's actual details — a shipped data bug on a high-stakes message. **[PROVEN]**
- Two entirely different move-out flows exist behind a hidden flag; tenants on the old one get a form stitched from cached values. **[PROVEN]**
- The move-out checklist screens are the least design-system-compliant in the app. **[PROVEN]**
- There is no deposit-refund state anywhere: after handover, the money simply disappears from the app's story. **[INFERRED from flows + backed by the research's trust-gap finding]**
- The eviction hub handles state well (server-driven status machine) — the logic is worth keeping. **[PROVEN]**

**The overhaul must answer:** move-out as a closure ritual: a transparent deposit tracker (held → inspected → deductions itemized → refunded, with dates), the checklist reframed as the *tenant's* protection (timestamped photos = deposit evidence), and a goodbye moment — a "your time here" recap worth keeping. The "this app got my deposit back" story is the strongest advocacy asset available to us.

**Research must validate:** deposit-dispute frequency and typical deduction fights; whether tenants understand the checklist protects them (hypothesis: they see it as the owner's tool against them); what refund-timeline transparency owners will actually commit to.

---

### M7. Attendance — the daily loop, and a dignity question

**The job:** the student register's daily touchpoint. Also the module most likely to feel like surveillance if designed carelessly — and it currently is.

**Broken today:**
- The setup wizard is the documented first-run wall (see M2). **[OBSERVED + PROVEN]**
- Marking lives in a ~28-state bottom sheet with three inconsistent color systems for the same statuses and 120 hardcoded colors. **[PROVEN]**
- The experience is framed entirely as compliance — mark, verify, prove — with no acknowledgment, no history-as-achievement, nothing given back. **[INFERRED]**

**The overhaul must answer:** "show up, get seen." Marking returns a human moment, history fills like a streak calendar, and the framing shifts from *prove you're here* to *your record, yours to keep*. Setup becomes a guided, warm, exitable flow. Where's the line between engagement and gamifying a curfew — what does the *parent* register need to see versus the tenant?

**Research must validate:** how tenants actually feel about attendance (surveillance vs. safety vs. indifferent — likely varies by register); manual vs. smart split in practice; whether parents/guardians value the visibility (they're a stakeholder here, uniquely).

---

### M8. Food — the anticipation surface

**The job:** the other daily habit. A captive menu has no ordering competition — the job is anticipation and trust in what's being served.

**Broken today:**
- Menu timings updated by the manager don't reliably reach the tenant's screen. **[OBSERVED]**
- Success and failure of meal confirmation show the *same* toast. **[PROVEN]** There is no error state — failures render as an empty menu. **[PROVEN]**
- The menu is text on cards; the day's most-anticipated information has the least sensory presentation in the app. **[INFERRED]**

**The overhaul must answer:** menu as something tenants *check the way they check a food app* — sensory descriptions, real photos when the mess uploads them and dignified illustration when not, "43 of 60 eating tonight" as both social proof and belonging signal, confirmations that feel communal rather than transactional.

**Research must validate:** whether tenants check the menu before meals or learn it by routine; meal-confirmation compliance and why it's skipped; whether the count-of-diners idea reads as community or as pressure.

---

### M9. Rewards, RentPass & Offers — three systems, one confusion

**The job (unmet):** make being a good tenant feel worth something. Today three overlapping systems (scratch-card credits, an offers catalog, RentPass rewards) share no mental model.

**Broken today:**
- Offers duplicate on every refresh; the offers page double-fetches with conflicting initial tabs; reward cards use the error color; server-sent colors crash when absent; "up to ₹X" displays the minimum. **[PROVEN — all]**
- Most personas actively ignore this entire area. **[OBSERVED — persona research]**
- Offers are one global catalog: nothing is scoped to city, property, or tenant — a Goa tenant and a Pune tenant see identical content, which reads as spam. **[PROVEN — backend audit; targeting is a logged backend ask]**

**The overhaul must answer:** TAR-01's position — the streak/reliability record as the spine (on-time rent history as something a tenant *owns*), one unified rewards model instead of three, and no prize-wheel moment attached to rent. What is the honest version of "rewarding" for each register, given most ignore what exists?

**Research must validate:** whether any register values the current rewards (hypothesis: no, except scratch cards at payment); what would make on-time payment feel recognized — cashback, streak, a portable record, or nothing; offer categories tenants would actually redeem, by city and register.

---

### M10. Add-On Services — co-living's module

**The job:** book a cleaning, a laundry slot, a gym session without a WhatsApp message. Relevant mostly to the professional/co-living register.

**Broken today:** the module is the least design-system-compliant in the app; one visible action ships a "Coming soon" toast; the overview leads with stats of unclear value to a tenant. **[PROVEN]** Short-stay tenants have no scoped offerings (persona gap). **[OBSERVED]**

**The overhaul must answer:** borrow the best booking pattern in Indian consumer apps (clear slots, plain-language cancellation, post-service rating) and decide what the overview is *for* — probably "your next booking," not statistics.

**Research must validate:** actual booking volume where enabled; which services tenants want by property type; whether discovery or trust (will it actually happen?) is the blocker.

---

### M11. Notifications & Announcements — the signal channel

**Broken today:** every notification card except move-out does nothing when tapped. **[PROVEN]** Announcements show as an always-on ring with no real push semantics — the team itself flagged Stories as stale and wants real announcements. **[OBSERVED + PROVEN]**

**The overhaul must answer:** one feed where everything the property says to the tenant lands and taps *go somewhere* — converging with the Messaging direction (the WhatsApp thread surfaced in-app) from TAR-01.

**Research must validate:** which property communications tenants actually want pushed vs. available; current notification fatigue and mute rates.

---

### M12. Entry & Exit / Gate — scoped, but real where it exists

Gated to specific properties; thin tenant-side surface today. Fold its research into the attendance conversation (same registers, same dignity question, same parent stakeholder). No standalone depth until validation says the module expands. **[INFERRED priority call]**

---

### M13. Boot, White-Label & the brand moment

**Broken today:** covered in S5 — plus the boot experience itself is a white screen and a spinner; the backend can already serve splash media that the app ignores; and owners struggled to enter brand colors as hex codes, which the team already works around by deriving palettes from logos — external validation of exactly the palette-derivation direction in TAR-02. **[PROVEN + OBSERVED]**

**The overhaul must answer:** the arrival ritual (property logo resolving at boot) and the white-label pipeline that guarantees a client's colors land safely everywhere.

**Research must validate (owner-side):** what makes an owner *proud* to show the app; which brand elements they care about beyond logo and color (the "About Us" / property-story idea from team interviews).

---

### M14. Messaging & Reviews — the two not-yet-features

Both already run over WhatsApp (the white-label business thread; the survey engine). The redesign brings them in-app — TAR-01 holds the positions; the open research questions are appetite questions:
- Would tenants read the property's WhatsApp thread inside the app, and what would make them check it here rather than in WhatsApp? **[hypothesis: only if the app is already their daily surface — depends on M3/M7/M8 landing]**
- Will owners run surveys through the app, and will tenants answer more or fewer than over WhatsApp?

---

## Part 3 — The bridge to research

What Parts 1–2 mean for the instruments (built next, in [[TAR-04 Research Kit]]):

1. **The [PROVEN] tier gets no questions at all.** We own the codebase; defects are known, and the overhaul rebuilds those flows regardless of how often each one fires. Nobody is asked "have you faced bugs."
2. **Research asks only what only humans know.** Behavior (where complaints really get filed), feeling (does attendance read as surveillance or safety), context (who actually pays the rent), and heard demand (what tenants ask staff for that the app can't do). Everything answerable from code or data is answered from code or data.
3. **Nobody is asked to design.** Respondents are experts in their own experience, not in solutions. We ask for stories, last-time recalls, and choices; we translate them into design. "Is it easy / intuitive / what would you improve visually" — banned forms.
4. **Every question carries a scope frame.** Each question tells the respondent what kind of answer is in bounds: "only about how things are today," or "assume anything is possible," or "pick from exactly these." Respondents can't be expected to guess the altitude; we set it.
5. **The [INFERRED] tier is where research must be free to demolish us.** Hierarchy, feeling, and framing hypotheses are tested with open, non-leading questions — direction appetite is tested with concrete scenarios in plain words, never abstractions, and always after experience questions so it can't contaminate them.

## Changelog
- 2026-08-11: v1. Synthesized from Phase 0 code discovery, the research corpus, the craft-layer audit, and the fintech/brand teardowns. Ranking axis locked with Sanchay (trust → adoption). For internal discussion and validation planning — not a build list.