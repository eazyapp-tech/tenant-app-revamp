# Brand Design Systems Synthesis — apple / airbnb / wise / revolut / linear / stripe

## 0. METHODOLOGICAL CORRECTION (read first)
All six DESIGN.md files are **marketing-surface analyses, not product design systems.** Consequences:
- Strong on type, layout physics, elevation, radius — all in real numbers.
- **Iconography nearly absent.** Total icon content across 3,358 lines: Apple (14px search glyph, 44px circular chip), Airbnb (32px hand-illustrated product glyphs, 32/40px circular icon buttons), Linear (24px logos, 32–40px avatars). No stroke weights, no grid, no naming, no optical sizing.
- **Motion: ONE real number in the entire corpus** — Apple's `transform: scale(0.95)` press state. No durations, no easing, anywhere. **Our motion tokens already exceed all six documents.**
- **Voice/copy: nothing.** Not one line, any brand.
- Loading/empty/error/skeleton explicitly listed as *not captured* by Airbnb, Apple, Linear. Wise has 2 auto-generated stubs.

→ **The corpus is silent on exactly 4 of our 5 identity carriers (icons, motion, voice, states). Those sections must be invented, not copied.**

---

## 1. TYPOGRAPHY

| Brand | Display | Body | Display tracking | Body LH | Weight ladder |
|---|---|---|---|---|---|
| Apple | SF Pro Display 600, 56/40/34 | SF Pro Text 400 @17px | −0.28 to −0.374px | 1.47 | 300/400/600/700, **500 BANNED** |
| Airbnb | Cereal VF 500–700, 22–28 | Cereal 400 @16 | −0.44@22, −1@64 | 1.5 | 400/500/600/700 |
| Wise | Wise Sans **900**, 40–126 | Inter 400 @16 | 0 hero, −0.96@32 | 1.5 | 400/600/900 |
| Revolut | Aeonik Pro 500, 20–136 | Inter 400 @16 | −2.72@136, −0.8@80 | 1.5 | 400/500/600/700, **body 500 BANNED** |
| Linear | Linear Display 600, 28–80 | Linear Text 400 @16 | **−3.0@80 (3.75%)** | 1.50 | 400/500/600 only |
| Stripe | Sohne **300**, 22–56 | Sohne 300 @**15px** | −1.4@56 | 1.4 | 300/400 only |

### Rules that repeat
- **Negative tracking on display, scaling with size — 6/6.** Range −0.5% (Apple, mildest) to −3.75% (Linear, most aggressive) of size.
- **Positive tracking on smallest labels — 4/6.** Linear +0.4, Airbnb +0.32 (uppercase tag), Revolut +0.24, Stripe +0.1. Revolut's stated reason: the small positive nudge makes UI labels feel mechanical and precise.
- **→ SHARPEST TRANSFERABLE IDEA: tracking SIGN encodes ROLE.** Negative = "this is a statement". Positive = "this is a label". Costs nothing, invisible to client colour, Anek's axes render it cleanly.
- **Two cuts, one voice — 4/6** run separate display + text families. Linear: "the family change is silent." Airbnb/Stripe use one variable family. **We can get the two-cut optical benefit inside one family via Anek's `wdth` axis** (narrower at display, wider at caption).
- **Narrow weight ladders with a NAMED BANNED rung — 5/6.** Apple bans 500 outright; Revolut bans body 500 ("400 or 600, never the in-between"); Stripe bans above 300; Linear resists 700+. **The pattern isn't which weights you pick — it's that a small number are legal and the illegal ones are NAMED.** This is what stops a large codebase drifting into "everything is semibold".
- **Display line-height collapses.** Revolut/Wise 1.0 on hero, Linear 1.05, Stripe 1.03, Apple 1.07; body 1.4–1.5 across all six. **3× gap. Nobody uses a single global multiplier.**

### Numerals — three distinct approaches
1. **Stripe: tabular + tightening.** `tnum` on every money/transaction/count cell, PLUS a tracking tighten (−0.42px@14, −0.39px@13). Money is a dedicated role (`body-tabular` @14px — SMALLER than the 15px body). Explicit ban: "don't render money cells without tnum." Called the brand's quiet financial signal.
2. **Airbnb: the number as hero object.** Rating display = **64px / 700 / −1px**, flanked by two small ornaments, in a system whose largest other headline is 28px = **2.3× jump over the next-loudest role.** Their own note: this is the ONLY place where type alone carries hierarchy, and it gets that because a rating is the peak trust signal. **Direct precedent for our "Room 302 / 18 months / ₹25,000" hero — from a consumer marketplace, no premium-hardware assumption.**
3. **Revolut: tracking as precision cue** (+0.24px on UI labels so numbers read mechanically precise).

---

## 2. ICONOGRAPHY — no system exists in any of the six
Everything the corpus contains is listed in §0. Two things still transferable:
- **Icon size ties to the TOUCH TARGET, not the glyph.** Apple: 14px icon inside 44px target. Airbnb: 32px heart because of 12px surrounding pad. The specified number is the *target*; the glyph floats inside.
- **Icons never carry meaning alone.** Airbnb nav icons always над a text label; Apple's circular chips are positionally unambiguous; Wise flags sit inside labelled currency rows. **Nobody ships a bare icon as the only signal.** For us this is a CORRECTNESS requirement, not a preference: a client hex tinting an icon against a client background can land at any contrast ratio.

**Our divergence: 3 icon families in one app (53 SVGs + ~310-entry string→IconData registry + Material icons in nav). Not one of the six ships more than one.**

---

## 3. LAYOUT & SPACING
- **Base unit** 4px (Airbnb, Wise, Revolut, Linear) or 8px (Apple, Stripe). All six converge on the same ladder: **4/8/12/16/24/32/48**.
- **Card interior padding** 24px (Apple, Airbnb, Linear, Wise) or 32px (Revolut, Stripe). Linear steps it by importance: 24 feature/pricing, 32 testimonial, 48 closing CTA — **padding as an emphasis channel.**
- **Section rhythm** Wise 48 · Airbnb 64 · Apple 80 · Revolut 88 (120 hero) · Linear 96 · Stripe 64–96.
- **→ DENSITY IS A PER-ZONE DECISION, NOT A GLOBAL CONSTANT.** Airbnb: 64px "tighter than typical SaaS (80–96) because marketplace pages need higher card density per scroll"; whitespace note "open hero, dense marketplace below". Apple inverts: airy everywhere except a deliberately dense footer "to make the full IA visible at a glance". **Maps exactly to us: facts hero wants air, dues ledger + complaint list want density.**
- **Grids reduce column count, never reflow rows — 5/6.**
- Container widths 1200–1440. Apple splits: ~980px text-heavy reading vs ~1440px grids — **reading measure and scanning measure are different numbers.**

---

## 4. INTERACTION STATES — weakest area, strongest single rule
| Brand | Pressed | Hover | Disabled | Focus | Error/loading/empty |
|---|---|---|---|---|---|
| Apple | `scale(0.95)` | **BANNED from docs** | text at ink-muted-48 | 2px solid outline | not surfaced |
| Airbnb | colour → primary-active | not documented | pale tint fill | border 1px→2px, flips to ink, "no glow, no ring" | error text colour only |
| Linear | primary-focus fill | primary-hover fill | ink-tertiary text | 2px outline @50% | not visible |
| Revolut | faint fill | none | faint foreground | browser default | none |
| Stripe | primary-press fill | none | none | border → primary | none |
| Wise | **per semantic role** | primary-active | none | none | stubs only |

**Four rules worth stealing:**
1. **Press feedback as a TRANSFORM, not a colour change.** Apple's `scale(0.95)` system-wide. **The only interaction feedback in the entire corpus that works when you don't know the brand colour.** Every other brand's press state is a hex shift we can't specify.
2. **State variants as NAMED TOKEN ENTRIES, not prose.** 4/6 ship `button-primary-pressed` etc. as separate entries; Linear + Revolut put it in their iteration guide as a hard instruction: "add new variants as separate entries, do not bury them in prose." **Direct structural fix for our 310-entry undocumented registry.**
3. **Wise attaches pressed to the SEMANTIC ROLE, not the component** (`positive`/`positive-deep`, `negative`/`negative-deep`). Every component rendering "destructive" gets the same press behaviour free. **Survives white-labelling because semantics should be brand-independent anyway.**
4. **Apple bans documenting hover at all** (iteration guide item 4: "Default and Active/Pressed states only"). Correct posture for touch-first; removes a class of specs that never fire.

---

## 5. COMPONENT PATTERNS
- **6/6 have exactly ONE signature component carrying the brand's argument.** Wise currency converter · Airbnb pill search + 64px rating · Stripe composited dashboard · Linear product screenshot · Revolut full-bleed mockup · Apple product tile. **3/6 state the enforcement rule: "lead every section with it."** → our equivalent: lead every screen with the tenant's own facts; a screen without an instance needs a stated reason.
- **Emphasis by POLARITY FLIP, not accent fill — 4/6.** Wise card-feature-dark (ink bg, green text), Stripe pricing-featured (navy fill, white text), Linear (surface-1 → surface-2, nothing else), Apple (light tile alternating dark, "the colour change IS the divider"). **Strictly safer than a second accent under white-label — a polarity flip works with any hex.**
- **Selected state = surface lift, not accent.** Linear tabs (canvas+subtle → surface-2+full-strength). Airbnb date picker: selected day is an **ink**-filled circle, not brand-filled. Airbnb renders star ratings in ink not gold because "yellow stars feel cheap in travel context." **3 cases of choosing neutral over brand for a state that could have used it.**
- **Card elevation by border, not shadow** (Wise 1px ink border, Revolut 1px hairline, Linear hairline + surface step).
- **List/row specs essentially ABSENT.** Entire corpus: Airbnb `amenity-row` (12px vertical pad, NO border between rows, section closed by hairline above+below) and Linear `changelog-row` (24px vertical, 1px bottom rule). Plus one Wise auto-generated stub.
- **Empty states: one stub** (Wise: soft surface, 24px radius, 48px padding, body-md caption). That is the entire coverage.

---

## 6. MOTION — complete inventory of real numbers
- Apple `transform: scale(0.95)` on button active, system-wide, in the Do list.
- Apple `backdrop-filter: blur(...)` frosted nav (~`saturate(180%) blur(20px)`, not formalised as a token).
- Airbnb one hover shadow: `rgba(0,0,0,0.02) 0 0 0 1px, rgba(0,0,0,0.04) 0 2px 6px, rgba(0,0,0,0.1) 0 4px 8px`.
- **Everyone else: nothing.**
→ The principle worth taking: Apple's press transform is the only motion stated as a **system-wide LAW rather than per-component decoration**, and it's the only colour-independent one.

## 7. VOICE — nothing, any brand
Only structural inference: Apple's product tile grammar is fixed (name → one-line tagline → exactly two CTAs); Revolut one flagship display headline per page; Stripe one filled CTA per band. **Copy constraints expressed as layout rules. Constrain the slots and the writing improves by force.**

---

# A. TRANSFERS TO US (ordered by value)
1. **Tracking sign encodes role** — negative on display scaling w/ size (target −1.5% to −2.5%), zero at body, +0.2–0.4px on labels/eyebrows/metadata. Identity no client hex can overwrite.
2. **Narrow weight ladder with NAMED banned rungs** — pick 4 legal weights from Anek 100–800, publish the banned ones. Cheapest anti-drift device for 483 files.
3. **Tabular figures + tracking tighten on the money role** — money as its own role, one step SMALLER than body, ~−3% tracking.
4. **The number as hero at Airbnb's amplitude** — their 2.3× jump over the next-loudest role. Set our facts role at a similar multiple.
5. **Elevation by surface contrast + hairline, not shadow** (5/6). Renders identically on cheap LCD; costs nothing on a low-end GPU.
6. **Derive hairline/shadow from INK, not neutral grey.** Stripe's shadows are `rgba(0,55,112,0.08)`, tinted with their navy. With HCT we express hairline as ink at fixed alpha/tone-delta → re-derives automatically per client. A hardcoded `#e0e0e0` does not.
7. **Linear's 1px white top-edge highlight on lifted panels** — reads as physical lift, one line, survives low-DPI daylight where soft shadow vanishes.
8. **Radius as a semantic channel, one radius per meaning class, never mixed** (5/6 ban mixing).
9. **Per-zone density** with the reason written down.
10. **Press feedback as transform** — the only colour-free interaction feedback available.
11. **State variants as named tokens, never prose.**
12. **Emphasis by polarity flip, not a second accent.**
13. **Accent scarcity enforced NUMERICALLY.** Revolut item 6: "if more than one accent element appears per viewport, ask whether one should drop to neutral." **A per-viewport count is safer than a per-component rule when you can't predict how loud the client's hex is.**
14. **Touch floors: 48px actions / 56px inputs — take the FINTECH numbers, not Apple's 44.** Airbnb+Revolut+Wise cluster at 48/56; Revolut calls 56 "fintech-grade accessibility". 44 is Apple's desktop-era floor; our floor audience is budget phone + daylight + possibly less dexterity.
15. **Publish an explicit display-size clamp ladder** (Revolut 136→80→64→48; Stripe 56→48→32→26→22). Numbers useless to us, the *artifact* is not: publish ours across small phone / standard / large / OS-font-scale-200%.
16. **Ship Do/Don't with NAMED BANS + a lint step.** 5/6 ship Do/Don't; 3/6 ship an iteration guide ending in a lint command.

# B. DOES NOT TRANSFER
1. **All six anchor identity in a single hex; we cannot.** All six additionally ban a second accent. Their entire emphasis system routes through a colour we don't control → **we must over-invest in exactly what they under-invest in: type, motion, icons, voice.**
2. **Runtime theming breaks every literal rule in the corpus.** All six assume a design-time palette, which is why `on-primary: #ffffff` can be a constant. **Any rule expressed as a literal hex is unenforceable in our codebase. Every colour rule must be a RELATIONSHIP: tone delta, contrast ratio, or alpha over ink.** Largest structural difference; not a small adaptation.
3. Stripe's gradient mesh (colour-dependent, ships as a large SVG/image — heavy on budget phone + metered connection).
4. Linear's dark-only canvas (`#010102` + 4 surface steps a few luminance points apart — indistinguishable on cheap LCD, invisible in daylight).
5. Revolut's true-black band slamming (needs real black levels; grey mush on budget LCD; fights any client background).
6. **Photography as protagonist** (Apple/Airbnb/Revolut). Our property images are user-uploaded, inconsistent, and the data cost falls on the tenant. Facts-as-hero is the right call and means their section-rhythm logic doesn't port.
7. Backdrop-filter blur (expensive on low-end Android GPUs in Flutter; reliable frame-drop source). Use opaque surfaces + hairline.
8. **Every responsive section in the corpus** (768/1024/1280/1440). Our real axes: 320–430px width, OS font scale ~85%–200%, pixel density. **None of the six addresses any of those three.**
9. Extreme display weights/sizes (Wise 900@126px, Revolut 136px). Cap both — heavy weights lose counters at low resolution in bright light.
10. **Stripe's weight-300 body** — thin strokes vanish on low-DPI LCD in sunlight. Their entire typographic position is unusable at our floor.
11. Affluent micro-typography (Airbnb 8px uppercase tag; Apple 10px micro-legal, 12px nav at LH 1.0). Assumes Retina + young user in an office.
12. Airbnb's bespoke hand-illustrated per-product icons (commission tied to a 3-product IA).
13. **Hover states** — Apple's posture (don't document at all) is correct for touch.
14. Two extraction artifacts that look like type rules but aren't: Apple `dense-link` 17px/LH 2.41 (a footer device, they say so); Wise `display-lg` 47px/400/70.5px LH.

# C. INTERSECTION (3+ brands = likely real principles)
| # | Principle | Count |
|---|---|---|
| 1 | One accent, scarce, second accent banned | **6/6** (universal but UNAVAILABLE to us) |
| 2 | Negative tracking on display, scaling with size | **6/6** |
| 3 | **Text colour is NEVER pure black** | **6/6** — `#1d1d1f`, `#222222`, `#0e0f0c`, `#191c1f`, `#0d253d`; on dark, Apple `#cccccc`, Revolut `rgba(255,255,255,0.72)` |
| 4 | Elevation without shadows | 5/6 (Stripe the exception, at 8% alpha) |
| 5 | Narrow weight ladder w/ named banned rung | 5/6 |
| 6 | Buttons ≥44–48px, inputs ≥48–56px | 6/6 |
| 7 | Card padding 24–32px | 6/6 |
| 8 | Grids reduce columns, never reflow rows | 5/6 |
| 9 | Exactly one signature component | 6/6 (3 state "lead every section with it") |
| 10 | Featured/selected by surface change, not accent | 4/6 |
| 11 | State variants as separate named entries | 4/6 |
| 12 | Positive tracking at smallest labels | 4/6 |
| 13 | Explicit Do/Don't with bans | 5/6 |
| 14 | Body LH 1.4–1.5, display 1.0–1.20 | 6/6 |

# D. OUR GAPS (ordered by damage)
1. **3 icon families, no system, and the corpus can't help.** Must invent from first principles: optical size tiers bound to text roles · stroke weight bound to type weight (Anek 700 display next to hairline icons reads wrong) · a naming taxonomy that isn't a 310-entry string map · **"icons never carry meaning alone" as a correctness requirement under white-label.**
2. **No state matrix — and neither does anyone else, so we invent the part that matters most.** Best corpus coverage is Linear's 4 states. **Loading/empty/error/skeleton/offline/stale documented by NOBODY.** Their silence is an artifact of marketing-pages-over-broadband. **This is where our FLOOR audience lives.** Minimum needed: default, pressed, disabled, focus, loading, empty, error, offline, stale, **partial (some data arrived, some didn't)**.
3. **Offline/stale have no vocabulary anywhere.** We need "this number is from 3 hours ago" as first-class, distinct from both loading and error. Our boot flow already has a no-network page → the problem is real in our product and unaddressed in our language.
4. **OS font scaling: not mentioned by any of the six** (web gets browser zoom free). Android @200% breaks: 48px fixed-height buttons, single-line pills, tabular column alignment, every fixed-height row. Language must state which roles scale, which are capped and at what multiple, and what layout does when a 1-line label becomes 2.
5. **Numeral spec probably covers money and nothing else.** Our hero is 3 different numeral classes: **money** (tabular, right-aligned, tightened, Indian grouping 2,50,000) · **duration** ("18 months" = number + unit; unit should NOT be the same weight) · **identifier** ("Room 302" isn't arithmetic — shouldn't be tabular-aligned against money, shouldn't carry money tracking). **Need a numeral ROLE TABLE, not one tabular token. Indian grouping has no answer in the corpus and is a correctness issue, not style.**
6. **Devanagari/Indic absent from every source.** Must state: Devanagari needs more line-height than Latin at the same size (shirorekha + ascender/descender marks; a global 1.5 crowds it) · **negative tracking on display — our strongest inherited rule — is often WRONG for Devanagari, because tightening conjuncts and matras damages legibility in a way it doesn't for Latin. Our tracking rule needs a SCRIPT CONDITION.** · mixed-script lines ("₹25,000 का किराया") put tabular Latin numerals inside a Devanagari line with different baselines and optical weights.
7. **Voice/copy from scratch.** Matters more for us than them: our floor audience reads the words, not the layout. Only usable pattern: slot constraints (Apple's fixed tile grammar; Stripe's one filled CTA per band).
8. **Semantic colours will collide with an unknown client hex.** All six hardcode semantics because they know their brand colour and can guarantee no collision. Need: semantics fixed and brand-independent · a stated collision rule · very likely a second differentiating channel (icon/position/shape) so meaning never rests on hue alone. **No benchmark faces this. It's ours alone and it's the kind of thing discovered in production.**
9. **Contrast floor under an arbitrary client hex unaddressed.** All six write `on-primary: #ffffff` as a constant. We need a hard rule + automatic ink-or-white resolution by client tone. HCT gives the machinery; the language must state threshold and fallback, because a client will eventually pick mid-tone yellow.
10. **No help at all on list rows — and lists are most of our product.** Complete corpus inventory: Airbnb `amenity-row` + Linear `changelog-row` + one Wise stub. Passbook, dues ledger, complaints list, transaction history are our core. Must write: row height per density · divider treatment (**Airbnb's "no divider between rows, hairline closing the group" is the more elegant available pattern**) · leading/trailing slot rules · numeral column alignment · tap affordance.
11. **Motion tokens ahead of corpus but probably not BOUND TO MEANING.** Need a binding from duration class → semantic class (state change vs navigation vs data-arrival are three things, not one duration). Apple's posture: a small number of motions that are LAWS, not a library of effects. Also need a reduced-motion + low-end-device path (web gets `prefers-reduced-motion` free).
12. **No stated enforcement artifact.** 5/6 ship Do/Don't with named bans; 3/6 end with a lint command. Our codebase already shows what happens without one: 310 registry entries, 3 icon families, 2 overlapping preference-key classes. **The bans are the product. A design language without named prohibitions is a mood board.**
13. **The "one signature component" rule needs an ENFORCEMENT CLAUSE.** 6/6 have one; 3/6 state "lead every section with it". We've nominated the tenant-facts object — the language must carry the second half, or the hero object becomes a home-screen widget rather than the system's argument.

## Sources
`~/.claude/design-md/{apple,airbnb,wise,revolut,linear.app,stripe}/DESIGN.md`