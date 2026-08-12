# Fintech Reference Teardown — Scapia / Kiwi / slice / Stable Money (+ CRED, Jupiter, Fi, OneCard, Uni, Kite)

**Method note (matters for trust):** Mobbin does NOT index Scapia, Stable Money, Kiwi, slice, Jupiter, Fi, Groww, INDmoney, OneCard, Uni, or Kite. Its Indian library is effectively CRED/Swiggy/Zomato/Blinkit. So this is built from: (1) **source-code extraction** — live CSS bundles, `@font-face` blocks, shipped design tokens, font-binary internal name tables (strongest evidence, not estimates); (2) Mobbin screens (CRED only); (3) published case studies/agency pages.

---

## Per-app extracts

### CRED (open source — NeoPOP, github.com/CRED-CLUB/neopop-web)
**Type:** Gilroy (Thin 300 → ExtraBold 800) for HEADING/BODY/CAPS; PP Cirka (Pangram Pangram) for SERIF_HEADING.
Scale:
```
Heading ExtraBold:  44 34 28 22 20 18 16 15 14 13
Heading Bold:          34 28 22 20 18 16 14 13 11
Heading SemiBold:         22 20 18 16 14 13 12 10
Serif Heading Bold:    36 34 32 24 22 20 18
Body Regular/Medium:            16 15 14 13 12 11
CAPS:                                    12 10 8
```
Three rules fall out: **body structurally forbidden above 16px** (display reaches 44); **all-caps only exists at 8/10/12** (the tiny wide eyebrow is not a choice, it's the only size caps can be); interface chrome is tiny (buttons 14/13/11, card headings 14, tags 8/10).

**Color:** core six — black `#0d0d0d` (never `#000000`), white, red `#EE4D37`, yellow `#F08D32`, blue `#144CC7`, green `#06C270`. Plus 7 "pop" ramps × 8 steps (poliPurple `#6A35FF`, orangeSunshine `#FF8744`, parkGreen `#3BFFAD`, pinkPong `#FF426F`, mannna `#FFCB45`, neoPaccha `#E5FE40`, yoyo `#AA3FFF`) and 4 semantic ramps × 5 steps. **Brand and semantic never share a value.**

**Neutrals = ink at alpha, no greys:** `FontOpacity: HEADING 0.9 / SUB_HEADING 0.7 / BODY_TEXT 0.5 / BODY_TEXT_LIGHTER 0.3`. Card strokes `rgba(255,255,255,0.1)`.

**Elevation:** not blur. `PlunkProps WIDTH=3, ANGLE=45` — 3px solid right edge skewed on Y + 3px bottom edge skewed on X. Hard extrusion, zero radius, zero blur. Button heights 50/40/30.

**Shareable moment:** post-payment screen floods brand green → white *paper receipt card* (amount in serif, txn ID in mono, date rotated vertically along edge like a till slip) → 3D reward box / slot machine on black → sheet "PAYMENT SUCCESSFUL / ₹10 / share receipt".

**Voice:** tiny uppercase eyebrow + lowercase serif sentence. "MEMBERSHIP ACTIVATED / welcome to the club. your perks await you."

**Note:** CRED already ships **RentPay** ("pay rent and win cashback up to ₹1,000"). Rent is an already-monetised, already-gamified category in Indian fintech.
**Onboarding:** asks phone on screen 2. Doesn't sell a feeling — sells a **gate** ("eligibility score 750+"). Exclusivity replaces persuasion.

### Stable Money (the key reference)
**Type (from `@font-face` at stablemoney.in):** Circular Std (Lineto) **Book 400 + Medium 500 ONLY, no bold**; Reckless Neue (Displaay); Denton (Peregrin); **Copperplate** — the engraved all-caps face of share certificates and bank documents, deliberately borrowing the visual language of the financial instrument itself.

**Shipped tokens (`--sd-` = "Stable Design"):**
| Token | Web | Mobile | Line height | Tracking |
|---|---|---|---|---|
| heading1 | 25 | 22 | 1.45 | **−0.5px** |
| heading2 | 23 | 20 | 1.40 | **−0.5px** |
| heading3 | 21 | 18 | 1.44 | **−0.4px** |
| heading4 | 18 | 15 | 1.46 | **−0.2px** |
| body1 | 15 | 13 | 1.53 | **−0.2px** |
| body2 | 13 | 11 | 1.36 | 0 |
| caption | 10 | 9 | 1.22 | 0 |
| title-all-caps | — | — | — | **+1.5px** |

**Tracking negative ≥15px, zero below, positive only on caps. Line height tightens as size grows.** Tokenised optical correction — rare, and the most transferable single rule found.

**Color:** `--sd-purple #916cff` brand, `--sd-green #12be57` money gained, `--sd-red #ee4950` error, `--sd-yellow #ffb003`, `--sd-orange #f47126`, `--sd-bg #fcfcfc`. Neutrals = `#000` at 3/5/10/20/30/40/50/60/80%; `--sd-border-color` IS `--sd-black-10`.

**Layout:** radii 4/8/10/12 + pills; spacing unit 4px; **border widths tokenised at 0.3px / 0.5px / 1px**. Only one real shadow in the bundle (`0 4px 10px #0000001a`). Cards separate by white-on-`#fcfcfc` + half-pixel hairline. That's why it feels calm.

**Hero object = the number given physical mass.** "1K" rendered as extruded 3D purple type with bevelled face and cast shadow; "0%" in 3D gold with a sunburst.
**Second hero = the bank kept physical.** Partner banks get full-colour app-icon tiles headed by **blurred photographs of the actual branch storefront, Devanagari signage included**. Most aggregators flatten partners to grey; they did the opposite because the bank IS the credibility.
**Trust gets a whole screen:** DICGC insurance on full purple gradient + 3D shield + "Insured up to ₹5,00,000" in display serif — and the acronym is glossed EVERY time ("a wholly owned subsidiary of RBI").
**Motion budget:** one thing — a `LiveTicker` scrolling 30+ bank rates. Static table → live market.
**Voice:** flat, declarative, numbers first. Loosens once: "Your new home is just an RD away."

### Scapia
**Type: Lexend Deca** (Google). Weight usage counted from inline CSS: **600 semibold ×80**, 500 ×18, 700 ×9, 300 ×8, 400 ×5 — semibold is the workhorse, not regular. Sizes: 12px dominates (×116), then 14 (×34), 18 (×16), 10 (×15); display 32/24/22/48, hero 80px. Negative tracking on display only (−0.56/−0.24/−0.2px). Lexend Deca is a reading-proficiency face — wide apertures, soft terminals — reads warmer than the Inter/Poppins default of Indian fintech.

**Color by frequency:** `#FFFDAF` pale butter (22), `#F1F6FA` ice blue (16), `#121212` (14), `#CE3E00` (12), `#9B4505` (12), `#F87B21` signature orange. Gradient orange→red.
**Accent discipline (copy exactly):** orange = the EARN color (coins, reward %) — never a button. Navy `#0B2645` = the ACTION color (all primary buttons). Green = the WIN color, reserved for when something becomes free. **Brand never means success; success never means brand.**
**Radii** 8/12/16/24 + pills. **Shadows near-invisible** (`0 0 14px 9px #f87b2008` = 3% alpha).
**Hero object:** the card, flat-illustrated, staged in 3D. Face = lone traveller from behind, straw hat, green backpack, orange sunset gradient. **Cardholder name set in handwriting script**, not embossed mono — a real departure. Flat artwork, dimensional staging.
**Voice:** second person, contractions, conspiratorial. "The card that takes you places." "No coupon hunting, no website jumping." Footer: **"Pronounced as 'skay-pea-uh'"**.
**Indian-premium signals:** lakh grouping (₹1,50,000 never 150,000); demo data that only means something here ("Volvo, AC Sleeper 2+1", "MAS UBL SF Exp", "Bengaluru → Coorg"); a real Indian airport lounge in photography, copper ceiling and all; RuPay/UPI first-class.

### slice
**Headline finding: slice commissioned and OWNS its typeface.** Internal name table of `slice-regular-webfont.woff2`: nameID 0 `Copyright 2019 slice`, nameID 1 `slice` (family, lowercase), nameID 2 `regular` (lowercase), nameID 8/9 `slice` (manufacturer/designer), nameID 13 SIL OFL 1.1. **Even the binary's metadata is lowercase.** Four weights 300/400/500/600 — **no 700+**, which caps how loud the brand can get and forces emphasis onto size.
**Tracking is the signature:** display at **−4px**, −3px, −1.52px (≈ −0.07em at 56px — optically merged). Body normal/slightly positive. Fully fluid scale using viewport AND container queries: `clamp(2.5rem, 19.44cqw, 3.5rem)`.
**Color:** electric indigo `#3410FF` + proper alpha-tint ladder (`#3410ff0a/0d/0f/12`), magenta rewards family (`#D30AD7`, `#F506AA`, `#FF37C6`). **Neutrals are undesigned Tailwind slate defaults — only brand colors got curated.**
**Radii enormous and fluid:** cards `clamp(2.5rem…3.5rem)` = 40–56px; hero shapes `clamp(8.5rem��11.6rem)` = **136–186px**. Blobs, not cards. Dark-surface shadow worth stealing: `0 0 0 1px hsla(0,0%,100%,.1), 0 25px 50px -12px rgba(0,0,0,.5), 0 0 100px rgba(139,92,246,.1)` (100px violet ambient glow).
**Correction to received wisdom:** slice's CURRENT copy is NOT meme-y Gen-Z. It reads as a regulated bank: "A new bank, for a new India." "Do right by the money." Lowercase wordmark survived; slang did not.

### Kiwi
**Type: display is a SERIF, italic, 800.** UI = Sora (via next/font). Display = "Flowers Of Nineties", self-hosted: `font-size: clamp(38px, 2.55vw, 48.896px); font-style: italic; font-weight: 800; line-height: 1; letter-spacing: 0`. Tall italic serif at 800 = fashion-editorial register, not fintech. Tracking exactly opposite of slice's.
**Color muddied** by Bootstrap 5 defaults; brand-reading `#81D829` lime, `#58A60A`, `#FFC720`, `#212121`. Canonical green unresolved.
**Motion:** scroll-driven image sequence with serif overlay title.
**Attribution:** Liquidink Design (Bangalore), Oct 2022–Feb 2023.
**Best copy in the set.** "Daily chai, coffee, cab rides, and grocery shopping, everything you're already paying for on UPI. Kiwi added a credit card behind it." And the one that names the enemy: **"This card for hotel points. That card for airline miles. Another one for the golf course. Every card rewarding a life most of us don't actually live everyday."** Stated value: "Finance makes money from fine print. We don't."

### Jupiter
**Type:** Manrope at exactly 3 weights (400/500/600-mapped-to-Bold) + PP Fragment Sans (Pangram Pangram) display. **Tops out at 600**, like slice.
**Color — strongest anti-CRED position:** `#2B2D33` warm charcoal ink (NOT black), `#FAF3E9` cream, `#357065` deep forest, coral ramp `#FC7A69`/`#E36E64`/`#CE4E42`/`#FA9E95`, `#FFCA7B` amber. A food/lifestyle palette, not a bank one.
**Published principle #1 (life.jupiter.money/design-principles-at-jupiter-f783457c976d):** *"Put Numbers in the Spotlight. Money is numbers... we made numbers the real heroes. Using typography, colour, and position, numbers are now always in the spotlight."*
Motion budget stated: "full-screen animations to haptics, from sound to micro-interactions." Liquidink brand direction: "Neo-Brutalist style combined with the personality of a sage."
**Voice:** "Money app for the life you're building." Rewards = "Jewels", buckets = "Pots", "Magic Spends". Social proof in Indian units: "Trusted by 30 Lakh+ Indians." Notably names **rent**: "from your morning tea to your monthly rent."
Design system named **Europa** (case study now 404s).

### Fi Money — cautionary tale
**Business status:** being unwound. "New savings accounts cannot be opened through the Fi app." Fi-Points accrual ends 20 Mar 2026.
**Type: Figtree only** (free Google font), 400/500/600/700. **No `letter-spacing` declarations anywhere in compiled CSS; exactly one `border-radius: 16px`.** Least differentiated typography in the set.
**Color: most disciplined in the set** — one accent hue, full stop. `#00B899` teal (×29), `#B2EADD`, `#14CCAD`, `#082320` deep forest, `#46AD95`, 5-step dark ladder `#1A1A1A→#38393B`. No secondary accent at all. Agency (Opposite) states permanent identity = "the Fi wordmark and the Fi Forest Green."
**Lesson: design quality is not a business model.**

### Secondary
**OneCard:** brand font "Lucid" is **Vercel's Geist, renamed** (name table: `Copyright 2024 The Geist Project Authors`, manufacturer `Basement.studio, Vercel`). Legal under OFL. Runs unmodified Bootstrap 4.5.3. Copy is all hero-object: "India's best metal credit card", "16-gram pure metal". **Strongest object claim, weakest craft — the claim/craft gap is instructive.**
**Uni Cards:** self-hosted Matter (Displaay) in 2023; current site serves only `system-ui, -apple-system`. **The brand face was the first thing cut.** This is what design-system decay under cost pressure looks like — the single most relevant failure mode for a white-label product.
**Zerodha Kite:** deliberate opposite. **Inter 400/500 only**, no display face, sizes cluster 8/9/10/12/`.675rem`, **largest common radius 4px** (vs slice's 186px — widest gap in the study). Stated philosophy: **"user disengagement"** — no gamification, no streaks, no confetti. Premium signal = refusal to decorate.

---

## The common formula — 9 mechanical rules (4+ apps each)

1. **A forbidden middle in the type scale.** Display 3–6× body; the middle is structurally unavailable. CRED body caps 16 / display 44. slice body 16 / display 88.
2. **Tracking is a function of size, and tokenised.** Negative on display, zero on body, positive only on all-caps. Verified in 3 independent codebases (Stable Money −0.2→−0.5 / 0 / **+1.5**; slice **−4px** display; Scapia −0.2→−0.56 display).
3. **All-caps is small or nonexistent.** CRED's CAPS role compiles ONLY at 8/10/12. The tiny wide-tracked eyebrow over a big headline is the most repeated composition in the study — and it's cheap.
4. **Neutrals are the ink at alpha, never separate greys.** CRED 0.9/0.7/0.5/0.3. Stable Money `#000` at 3–80% with border = the same token. slice `#3410ff` at 0a/0d/0f/12. **Nobody ships a grey ramp.**
5. **Brand color and semantic color are separate systems that never share a value.** Scapia: orange=earn, navy=act, green=won. CRED: 7 pop ramps + 4 semantic ramps, zero overlap.
6. **Weight ceilings, not ranges.** slice stops at 600. Jupiter stops at 600. Stable Money UI face is Book+Medium only. Emphasis via size and color, not bold. This is what stops a screen looking shouty.
7. **Elevation is a hairline or a hard edge, not a soft shadow.** Stable Money tokenises borders at 0.3/0.5/1px + one shadow. Scapia shadows at 2–3% alpha. CRED replaces shadow with a 3px 45° extrusion. **The blurry Material drop shadow is absent everywhere.**
8. **The number is the hero object, given physical mass.** Jupiter states it as principle. Stable Money extrudes "1K"/"0%" into 3D. Where there's no shippable object, they manufacture one out of the quantity.
9. **Trust gets a whole screen, not fine print.** Stable Money's DICGC screen + gloss-every-time. CRED's encryption strip on every onboarding screen.

**META-RULE: each brand makes exactly ONE expensive, unmistakable commitment and lets everything else be default.** slice bought a typeface, left neutrals as Tailwind. Stable Money licensed 4 display serifs, shipped hairline borders. Jupiter picked cream-and-coral nobody else would risk. **Premium comes from one deep commitment, not many shallow flourishes.**

---

## Transfers cleanly to us

- **Typography, entirely** — forbidden middle, tracking rules, caps size cap, weight ceiling. None of it touches the client palette. **This is the answer to "identity through type."** Own ONE typeface across every white-label instance, non-negotiable, the way slice treats theirs and Fi treats Forest Green. Client gets colors; we keep letterforms.
- **The alpha-based neutral system — close to mandatory.** Hardcoded grey hexes break on a client's dark background. `AppColor.text` at 0.9/0.7/0.5/0.3 + borders at 0.1 survives ANY re-skin automatically. Our getters-off-4-mutable-fields is the right instinct; the opacity ladder finishes it.
- **Brand/semantic separation — this is a BUG FIX for us.** Today `AppColor.breakfastColor === AppColor.primary`, `tabColor === primary.withOpacity(0.1)`. **If a client picks red as primary, "paid" and "overdue" become the same color.** Success/warning/error must be a fixed ramp white-label cannot touch.
- **The number as hero.** Rent due, deposit held, days to move-out, meals taken. Better numbers than an FD app has — personal and recurring.
- **The receipt as designed object — and we're structurally luckier than CRED.** A CRED receipt is nice-to-have. **A rent receipt is a legal document an Indian tenant needs** (HRA claims, police verification, proving tenancy). CRED had to invent a reason to make receipts beautiful. We have one.
- **Trust as a whole screen.** Deposit held, agreement signed, KYC complete. DICGC treatment maps to "your ₹25,000 deposit is recorded against this agreement."
- **Hairline elevation.** Client-agnostic, cheap, and it's most of why Stable Money feels expensive.

## Does NOT transfer

- **A signature hue.** Fi IS `#00B899`. slice IS `#3410FF`. We cannot have one. Any concept depending on a specific color is dead on arrival.
- **Dark-only.** CRED's logic (9 in 10 members prefer it) doesn't hold for us: migrant/blue-collar tenants on budget LCDs, often outdoors in daylight. 30% white on near-black is unreadable there. Light-first, client background respected.
- **The shipped physical object.** Nothing arrives in the post. **Our hero is the room — but it's the CLIENT's property, not ours.** So the hero must be built from tenant-specific DATA (room number, floor, bed, move-in date, months completed), not art we control. Closer to Stable Money's approach: make the QUANTITY the object.
- **A bespoke typeface per client.** Unaffordable and self-defeating. One face, all instances.
- **Exclusivity mechanics.** CRED gates on a 750 score. Applied to housing, exclusivity language isn't aspirational — it's exclusionary.

## Anti-patterns

1. **Variable reward after a compulsory payment.** CRED's slot machine works because a card bill is discretionary with a reward loop attached. **Rent is not discretionary.** A wheel after rent — possibly late, possibly borrowed — trivialises a stressful obligation, carries gambling optics no family-run PG operator wants on their branded app, and breaks entirely for corporate-sponsored tenants who never pay. Post-payment moment should be **the receipt and the streak, not a wheel.**
2. **Extreme corner radii.** slice's 40–186px blobs are the most obviously time-stamped thing in the study; will read "2024" within two years, eat vertical space on 5-inch screens, multiply badly against unknown client logo shapes. Stable Money's 4/8/10/12 will still look right in 2030.
3. **Dark-only** (see above).
4. **English-only editorial voice.** Kiwi's copy is the best written here and "Your everyday deserves a little more" is untranslatable. CRED's lowercase-serif register is worse — it signals "this app is for people like us," exactly the wrong signal. **The transferable part is CONCRETENESS ("daily chai, coffee, cab rides"), not wordplay.** Name the actual thing: rent, deposit, room, food, complaint.
5. **Aspirational western imagery.** Stable Money's Eiffel Tower / Scapia's global-airline montage alienate a PG tenant sending money home. Stable Money's OTHER imagery is the model: real Indian bank branches, Devanagari signage, unglamorous.
6. **Uni Cards = the failure mode to fear.** Licensed typeface 2023 → `system-ui` today. **In a white-label product with per-client margins, the design system degrades exactly there. Defence: typeface ships in the package binary, not as a per-client asset — so there is no per-client decision to lose.**
7. **OneCard = claim/craft mismatch.** "India's best metal credit card" on unmodified Bootstrap + renamed OSS font.
8. **Fi = design quality is not a business model.**
9. **Don't gate on KYC that doesn't need gating.** Current `BasePage` KYC check can route to `kyc_compulsory_page` — for a migrant tenant without immediate document access that's the highest-drop-off screen we could build. KOHO's alternative: `7/8` step counter + "Where to find it" helper + skippable path.

## 10 stealable mechanics

1. **Two-line header: tiny tracked eyebrow + large display line.** 8–10px all-caps at +1.5px tracking / 50% ink, then 28–34px display at −0.4px / 90%. "RENT DUE / ₹8,500 by 5 March." One widget; instantly stops the app looking like a form.
2. **Tracking tokens tied to size, enforced in code.** ≥18px → −0.4; 15–17 → −0.2; ≤14 → 0; all-caps → +1.5. Not a parameter a dev passes — a property of the size. ~2 hours work, highest quality-per-effort ratio in the list.
3. **Opacity ladder replaces every grey.** 4 text tokens off `AppColor.text` (0.9/0.7/0.5/0.3) + one border at 0.1. Delete every hardcoded grey. **Do this first** — it's what makes the design survive an arbitrary client palette.
4. **Lock the semantic ramp away from white-label.** Paid always the same green, overdue always the same red, regardless of client color.
5. **The rent receipt as paper artifact.** Flood in semantic success color → white card behaving like printed paper: amount in display, property+room in body, txn ID in mono, date small and rotated along the edge. One share button. Becomes the most-screenshotted screen with zero gamification, because HRA claims and police verification make it a document the tenant genuinely needs.
6. **Extrude the number into an object.** "0" late payments, "18" months completed, "₹25,000" deposit safe. One reusable 3D numeral treatment — works on any background because it's an asset, not a color.
7. **Trust as a full screen, acronym always glossed.** Deposit screen: full-bleed, shield mark, amount in display, agreement reference. "recorded against your registered rental agreement dated 4 Jan 2026."
8. **Hairline separation instead of shadows.** White surface on `#FCFCFC`-equivalent + 0.5px border at 10% ink. Keep exactly ONE shadow (`0 4px 10px rgba(0,0,0,0.1)`) for genuinely floating elements.
9. **Live ticker for comparison data.** Stable Money's insight: a static table is a chore, a moving market is a game. Tenant equivalent = the property pulse: meals served today, complaints resolved this week, rooms occupied. Slow horizontal marquee at 10px caps. Cheap, color-agnostic, makes home feel live not cached.
10. **Sell the feeling before asking for the phone number.** CRED gets away with asking on screen 2 because it gates on a credit score. We have no gate, so we need the other thing. Three display-type screens in the client's colors saying what the tenant gets — rent receipts that count for HRA, a complaint that gets a name and a timestamp, a deposit you can see — then ask.

## Could not verify
Mobbin has no in-app coverage of any target app (CRED only). No in-app motion specs for any target. No numeral-treatment specs (`font-variant-numeric` / `font-feature-settings`) found in any stylesheet — tabular-figure usage unknown. No published design system for slice/Fi/Kiwi/OneCard; Jupiter's "Europa" 404s. In-app typefaces inferred from web properties (CRED excepted). No Fi or Jupiter mascot confirmed. No verbatim historical slice Gen-Z copy. Kiwi's canonical green unresolved. No public Scapia design case study. Stable Money's serif era undated.