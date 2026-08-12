# Phase 0 — Mobbin Taste-Reference Sweep (all links verified Mobbin iOS)

## 1. Home/dashboard
- **CRED dark vault** (screens/121f46b0, flows/d5d38886): black canvas, lowercase serif headers, letterspaced CAPS micro-labels, circular quick-actions, skeuomorphic hero object, animated jackpot ticker. Numbers loudest.
- **Airbnb content-first** (screens/41e035de, 179b0617): pill search, sentence-case section headers ("Available next month in Miami"), photos do emotional work.
- **Zomato/District editorial** (screens/cb7052bb, 2ac5a045, ed665f6d): arched card masks, poster type, magazine copy, personality section names ("Showstoppers").
- **Neobanks N26/Monzo/Wise/Cleo** (52ecfd8a, 6c2bac17, 628a69b6, 84b0e0a3): one dominant number + 2-4 verb quick-actions + list. N26 setup checklist w/ 1/5 progress → maps to tenant onboarding tasks (KYC, docs, autopay).
- **Adapt:** hero = rent state as one big number + Pay as single verb; thin ticker for live moments (meal live, spin available); sentence headers; N26 checklist for pending tasks. Don't copy Cred's dark wholesale (white-label!) — adapt the TYPE system which survives any brand color.

## 2. Payments + success
- CRED first-payment flow (flows/d5d38886, 10 scr) + paying-a-bill (flows/9e6b7280): huge ₹ field on dark, incentive strip, quiet processing pill, full green success sweep with receipt sheet (share/history/support), **success chains into reward moment (slot machine)** — payment is the emotional peak.
- CRED editing-bill (flows/7d6ca5c6): paid-already chips (Pending/Min/Custom), plain-language irreversibility warning → maps to partial rent + cash reporting.
- Range: Qonto quiet 3D check (fd1d8acd); Wise ribbon (d2bd6044); Eventbrite "See you there!" (87341507); cringe baseline: Ladder/Everyday Rewards generic confetti (6d6e7bea, 314542b5).
- **Adapt:** rent success = designed full-screen moment + warm copy ("August rent — done. See you next month.") + WhatsApp receipt share (real Indian job) + chain into spin when available. Qonto restraint for small payments.

## 3. Rewards taste vs cringe
- CRED: slot machine post-payment (008e64ce), win moment (326dbc3c) — dark stage, one glowing object, always "Tap to skip"; coins-to-play (1e181278); "kill your next bill" power play (72d74f41); partner gallery (33952f91).
- Swiggy One: "customers like you save over ₹400/month" (2c83a9b9) — rupee-quantified, not badges.
- **Adapt:** spin wheel earns place only if (a) at payment-success peak, (b) prizes real + rent-adjacent, (c) staged like Cred (dark scrim, one lit object, skippable). RentPass leads with a rupee number.

## 4. Food
- Zomato menu system (e7535557, 647dc4fc, 557ace2c, c7e68403): veg/non-veg dot + name + one-line sensory description + photo on color blob + "Highly reordered" social proof + kcal.
- **Adapt:** captive menu → job is anticipation + trust. Sensory one-liners even for dal-chawal; illustrated fallback when no photos; "43 of 60 tenants eating tonight" = social proof + community; meal-live in home ticker.

## 5. Booking + issue reporting
- Urban Company add-to-cart 23-scr (flows/fa74c21d) + slot flow (flows/4b4e697b): numbered requirement steps in sheet, trust chips, plain-language cancellation policy BEFORE pay, day chips + time chips, unavailable shown not hidden, tip chips, pinned rating prompt, 3D icon grid (5e8ff03b).
- Airbnb support chat (4f3b5086, 4c3a83c5, 75b45272, 8d91ec23): chip-first conversational triage + dignifying confirmation copy.
- **Adapt:** complaints = chip-first triage ("AC not cooling / WiFi down / type it myself"), confirmation names the fixer + expectation ("We've told Rajesh (electrician). Most fixes within 24h"). Services copy UC slot picker + plain cancellation + rating pin + "thank the staff" tip pattern.

## 6. Auth warmth
Plazo welcome + shield reassurance (6f4d8059); Wonder serif OTP calm (de5cee7f); Manus "verification only, not linked" (ebba627f); DoorDash call-instead fallback (34095dcf).
- **Adapt:** "Welcome home" frame, one field per screen, auto-read OTP, privacy microcopy ("Only your property manager can see your number"). pageWaiting = emotional moment: show PG name/photo, "Asking [PG name] to let you in."

## 7. Profile IA
Airbnb three-tier (dc125dc8 → 936fbfe8 → 45f2625c, 918db004): Profile tab (few items) → Account settings (≤9 rows) → leaf label+value+Add/Edit. "Not provided" as honest gap-state. Destructive at bottom, plain text + consequence.
- **Adapt:** My Home (room, rent, agreement, roommates — emotional, top) / Documents & KYC (Provided/Not provided states) / Account & Support. Logout red, alone.

## 8. Belonging
Karrot neighborhood identity (7ae68d33); **Abode shared-house widget board (5ff0d9c6) — best co-living belonging expression: shared widgets, dinner vote, playful group identity**; WhatsApp Communities structure (3c34870d); Shangri-La arrival countdown (ff342c1a).
- **Adapt:** Life-in-PG = belonging engine: dinner poll, who's-eating count, announcements-as-stories, building name in header (identity before transactions).

## 9. Empty states + micro
Swiggy "No scratch cards? Let's fix that!" (49e36f4c); Baemin fat cat (06183923); Ubank/Coursera "(yet)" minimal (0f38d793, 7e5f69c8); UC "Hey, it feels so empty here". Streaks: Duolingo calendar w/ flame ranges + freezes (736a41b0); Me+ "You showed up, and that's what matters most" (d1e8fdf1); Speak week dots (7acbb2fc); Finch radial glow (879b0749).
- **Adapt:** first-person voice + one CTA everywhere ("No dues. Frame this screen."). Attendance = streak product: Duolingo calendar, Me+ affirmation post-selfie instead of toast. Budget: number count-up, ticker slide, sheet spring, success sweep.

## 10. Indian premium visual language
1. **Typographic contrast is THE premium signal** — serif lowercase display vs caps micro-labels vs tabular numerals. Geometric-sans-everywhere (current Poppins) = #1 template tell.
2. **Dark = stage, not theme.** Contrast between modes by moment.
3. Money rendered honestly: big tabular numerals, ₹-quantified claims, strikethroughs.
4. Motion restraint: quiet processing, celebration reserved + skippable, ambient tickers not popups.
5. Editorial confidence: wit over exclamation marks; formality reads government-portal to Indian Gen-Z.

## 7 principles ("If Airbnb built an Indian tenant app")
1. The place, not the platform — header names their building/room with warmth.
2. One number, one verb per core screen.
3. Celebrate the rent, respect the receipt — full-screen rent moment; quiet small confirms; confetti never default.
4. Talk like a good warden, not a portal — chips over dropdowns, consequence sheets, voice-forward empties.
5. Typographic theater on a white-label skeleton — type contrast + stage moments survive any brand color.
6. Belonging is a widget, not a feature — small shared-life surfaces woven into home.
7. Show up, get seen — streak grammar for attendance/food.

## Top 10 reference flows → modules
1. CRED first payment (flows/d5d38886) → pay-now → success
2. CRED paying-a-bill (flows/9e6b7280) → dues→payment→receipt
3. CRED editing bill (flows/7d6ca5c6) → partial/cash reporting
4. UC add-to-cart (flows/fa74c21d) → services listing→booking
5. UC address+slot (flows/4b4e697b) → slot picker + reschedule
6. Airbnb support chat (4f3b5086 + 75b45272 + 8d91ec23) → complaints/Tarini triage
7. Airbnb Profile→Account→Personal (936fbfe8) → profile IA
8. Zomato dish cards (557ace2c) → food menu
9. Duolingo streak calendar (736a41b0) + Me+ (d1e8fdf1) → attendance
10. CRED slot machine (008e64ce) + win (326dbc3c) → spin staging

Gaps: Jupiter, Fi, MyGate, Amenify, Livly, GPay India not in Mobbin iOS index this session — nearest analogues substituted; deeper coverage needs Android captures/teardowns.
