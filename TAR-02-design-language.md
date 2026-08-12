---
title: TAR-02 RentOk Tenant App Design Language
date: 2026-08-10
tags: [rentok, tenant-app, revamp, design-system]
owner: Sanchay
status: v1-proposal
---

# TAR-02 · The RentOk Tenant App Design Language

> The companion to [[TAR-01 Brief]]. That document says what we are betting. This one says how everything will look, move, and feel, and why those choices survive being repainted in a client's colours.

> [!NOTE] Naming is deferred
> This system will eventually carry a name, and a named language is part of the benchmark bar set in [[TAR-01 Brief]]. But naming it needs several stakeholders in the room, so it stays "the RentOk tenant app design language" until that conversation happens. Nothing below depends on the name.

## What this system believes

**A tenant should feel the app belongs to the place they live, not to the company that sold it.** Every rule below is downstream of that.

### The four laws

**1. The place is the hero, and it is made of facts, not photographs.**
We cannot art-direct the client's building, and nothing arrives in the post for us to make desirable. So the hero is the tenant's own facts, set with real weight: *Room 302. Third floor. Eighteen months. ₹25,000 held.* The property's logo, name and address frame those numbers; the numbers carry the screen.

**2. Timeless in structure, modern in behaviour.**
Restraint holds the still image: type, grid, honest photography, none of this year's trend. Motion carries the modernity. A screenshot should be hard to date; the moment a finger touches it, it should feel like next year's software.

**3. The ceiling is world-class, the floor is dignified.**
The app must delight a design-literate twenty-six-year-old in a Bangalore co-living and remain completely usable for a migrant tenant on a budget LCD screen in daylight. Sophistication reveals itself as someone engages. Nothing basic is ever gated behind novelty, and there is never a stripped-down "simple mode", which is only a polite insult.

**4. Identity lives everywhere except colour.**
A client replaces our palette and our logo. What stays is the typeface, the way type is scaled and tracked, how things move, how surfaces separate, the illustration voice, and the shape of our moments. That constraint is harder than what the apps we admire had to solve, and meeting it is what would make this worth citing.

---

## Type — the one expensive commitment

Everything else in this system is disciplined and cheap. The typeface is where we spend, because it is what carries identity when colour cannot.

### The face: Anek, by Ek Type, Mumbai

- **Ten Indian scripts** — Bangla, Devanagari, Gujarati, Gurmukhi, Kannada, Latin, Malayalam, Odia, Tamil, Telugu — **all metrically identical** (x-height 0.489 em, cap 0.639 em, matching digit advances). A Tamil or Telugu build becomes a file swap with nothing reflowing. No other family offers this.
- **Real weights on a continuous axis**, 100 to 800, plus a **width axis 75 to 125**.
- **Tabular figures**, so money aligns.
- **SIL OFL 1.1** — unlimited use inside unlimited client-branded apps, forever, free. This matters more than taste: every commercial foundry licenses per app, and one of them explicitly forbids passing the font to a third party, which is exactly what shipping a white-label build does.
- **It ships smaller than what we have.** 184 KB for one file with every weight, against 457 KB today for two fonts with one real weight each.

Two things it costs us, both planned rather than discovered later: Anek sets about 10% smaller than Inter at the same size, so the whole type scale rises about 12%; and Hindi support is an 846 KB file when we add it.

**Why an Indian foundry is the right answer and not a sentimental one:** Inter, Poppins, Geist and Plus Jakarta all read as "some app". A face drawn in Mumbai for ten Indian scripts reads as a decision, and it is a decision no competitor can copy without also copying the reasoning.

### The scale, and the middle we forbid

Every reference app shares one structural trick: **body type has a hard ceiling and display type is three to six times larger, with nothing usable in between.** That is what prevents the mushy mid-sized paragraph that makes an app look like a form.

| Role | Size | Weight | Tracking | Use |
|---|---|---|---|---|
| Display XL | 44 | 700–800, width 85 | −0.5 | the one number on a hero screen |
| Display | 32 | 700 | −0.5 | screen titles, amounts |
| Display S | 24 | 600 | −0.4 | section heroes, card amounts |
| Title | 18 | 600 | −0.2 | card headings |
| Body L | 16 | 400–500 | −0.2 | **the ceiling for reading text** |
| Body | 14 | 400 | 0 | default |
| Caption | 12 | 400–500 | 0 | metadata, helper text |
| Eyebrow | 10 | 600, all caps | **+1.5** | the label above a display line |
| Micro | 8 | 600, all caps | +1.5 | tags, chips |

**Tracking is a property of size and script, not a decision a developer makes.** For Latin: negative above 15, zero below, positive only on capitals. Every reference system does the first half and most do the second, and the sign is doing real work — **negative means this is a statement, positive means this is a label.** That is identity no client colour can overwrite, and it is the highest quality-per-hour change available to us.

**The script condition, which most systems never need and we cannot skip.** Negative tracking is a Latin rule. Tightening Devanagari damages it: the conjuncts and the marks above and below the line need their room, and the connecting line across the top makes crowding worse rather than tighter. So Indic scripts take zero tracking at every size, and more line height than Latin at the same size. Mixed lines — a rupee figure inside a Hindi sentence — follow the script of the sentence, not the number. Our whole typeface argument rests on ten Indian scripts; a rule that only works in English would undo it.

**All caps exists only at 8 and 10.** That single constraint produces the composition we will use everywhere: a tiny wide-tracked label over a large tight line. *"RENT DUE" over "₹8,500 by 5 March."*

**Money is always tabular.** Not globally, because tabular digits look gappy in prose, but on every amount, passbook row, dues column and receipt. Indian grouping is a solved problem in a library we already ship: ₹1,50,000, never ₹150,000.

**Weight has a ceiling of 700.** Emphasis comes from size and colour. This is what stops a screen from shouting.

**The display voice is the width axis, not a serif.** Condensing Anek to width 85 at weight 800 gives us a hero treatment that is genuinely uncommon, costs nothing, and adds no licence exposure. We deliberately reject the display serif that Kiwi, CRED and Stable Money use: that signal is aimed at an affluent, English-first, credit-card-holding reader, and to a tenant checking whether their rent went through it reads as a legal notice.

---

## Colour — a system that survives being replaced

The client hands us a brand colour. **We never render it.** We render a tone selected from a ramp built on its hue. Their brand is recognisable on every screen; it is never the thing text has to sit on.

This is possible because of one property of the colour space we use: **its lightness axis is the exact input to the contrast formula.** Contrast between any two colours depends only on their two tone numbers, whatever the hue or saturation. So we fix the tones, let the client own the hue, and accessibility stops being something we check and starts being something we cannot violate.

**The pipeline:** brand colour in → extract hue → build a light and a dark scheme → read every token by role. Extreme colours are handled by *discarding saturation rather than clamping it*: a neon green and a muted sage produce the same well-behaved ramp, differing only in hue. A near-grey brand colour switches to a neutral scheme instead of producing a colourless app that looks broken. It needs no new dependency; the library is already in our lockfile.

**Neutrals are ink at reduced opacity, never a separate grey ramp.** Four steps: 90% for headings, 70% for subheadings, 50% for body, 30% for disabled, and 10% for borders. Every reference app does this and none ships greys, because a hardcoded grey breaks the moment a client picks a dark background.

**Meaning colours are locked and are not white-labelled.** Paid is always the same green; overdue is always the same red. A client does not get to decide what "payment failed" looks like. This fixes a defect shipping today, where our semantic colours derive from the brand colour — hand a property a red brand and the money screen stops telling paid from overdue.

**Colour never carries meaning alone.** Every state has an icon and a word beside it. This is an accessibility requirement anyway, and it is also what makes a red-branded property merely awkward instead of dangerous.

**Light first.** Dark is a stage we walk onto for celebration moments, not a theme. Our tenants read outdoors, on cheap panels, in daylight.

---

## Surface and depth

**Hairlines, not shadows.** Cards are a white surface on a near-white background, separated by a half-pixel border at 10% ink. One shadow exists in the whole system, reserved for things that genuinely float, such as a bottom sheet. This is most of why the calmest app we studied feels expensive, and it costs less to render.

**Radii stay in the 4 to 16 range**, with pills for chips and buttons. We explicitly reject the very large radii currently fashionable: they are the most obviously time-stamped thing in this study, they eat vertical space on a five-inch screen, and they fight with client logos of unknown shape.

**Spacing is a 4-point rhythm.** Every gap is a multiple of 4.

---

## Motion

Two rules govern every number below.

**Exit is always faster than entry.** The tenant has already decided to leave; do not make them wait.

**Frequency is inversely proportional to duration.** The bottom navigation is tapped dozens of times a session and gets nothing. Payment success happens once a month and can afford a real moment. Before choosing a duration, count how often the thing is touched.

| Role | Duration | Feel |
|---|---|---|
| Tab switch, keyboard-adjacent actions | 0 ms | instant |
| Button press, toggle, chip | 100 ms | quick ease-out |
| Colour and state changes | 150 ms | standard |
| Expand | 250 ms | decelerating |
| Collapse | 200 ms | accelerating |
| Sheet in | 300 ms | decelerating |
| Sheet out | 200 ms | accelerating |
| Page transition | 300 ms | emphasized |
| Shared element | 350 ms | emphasized |
| Celebration | 800 ms | spring, slight overshoot |

**Colour and opacity never overshoot; only position and size are allowed to spring.** Anything a finger is dragging follows the finger with real velocity rather than playing a fixed animation.

**Reduced motion ships on day one.** Retrofitting it across five hundred files later is miserable, and the people most likely to need it are the people we are least likely to hear from.

---

## Voice

**Concrete, not clever.** The best-written app we studied earns its charm in English wordplay that does not survive translation and does not land for a tenant with limited English. We take its concreteness and leave its cleverness: name the actual thing — rent, deposit, room, food, complaint.

**Plain first, warm second.** "₹8,500 due in 4 days" before any personality. Warmth lives in the moments, not in every label.

**Never exclusive.** The aspirational register of Indian fintech — membership, eligibility, tiers — is exclusionary when applied to housing. Nobody should feel their home is a club they might not get into.

---

## The signature moments

Three moments carry the brand. Each one is designed to be worth a screenshot, and none of them is a gimmick.

**1. Arrival.** The property's logo resolves at boot. This is the only per-property brand element and today it is fetched, cached, and shown nowhere. The first thing a tenant sees should be their home's mark, not ours.

**2. Rent paid.** The screen settles into the success colour and a receipt becomes a paper object: amount in display type, property and room in body, transaction reference in a monospaced line, date set small along the edge. One share button. **We are luckier than the apps we admire here — a rent receipt is a document an Indian tenant genuinely needs, for tax claims on house rent, for police verification, for proving where they live.** They had to invent a reason to make a receipt beautiful. Ours is already needed, which makes it the most-shared screen in the app without a single nudge.

There is no prize wheel after rent. Rent is an obligation, often paid late, sometimes with borrowed money, sometimes by a company the tenant never sees. A slot machine there trivialises it.

**3. Showing up.** Marking attendance or a meal returns something human rather than a toast, and the history fills in like a streak. This is the daily loop, and the daily loop is what makes the app a habit.

---

## What "benchmark" means concretely

This is only a real design language if someone outside RentOk can read it and build something consistent with it. That means publishing: the principles, the type scale with its tracking rules, the colour derivation pipeline with its guardrails, the motion tokens with real numbers, the composition patterns, and honest do-and-don't examples. The system we learned the most from is the one that open-sourced itself.

## What ships first

The design language is Wave 1's first deliverable because everything else inherits it. Three fixes can land immediately, before any of it:

1. **Turn on tabular figures** for money. The font we already ship supports it and it has never been switched on; passbook and dues columns are misaligned today.
2. **Fix the thirty-three references to a font that does not exist** in the services module, which silently fall back to the system default on Android.
3. **Decide the Flutter version floor**, because below a certain version a variable font renders every weight at its default.

## Changelog

- 2026-08-10: v1. Written from the fintech teardown (source-code extraction of Scapia, Kiwi, slice, Stable Money, CRED, Jupiter, Fi), the palette and motion research, and the typeface research (font binaries measured, weights rendered in Flutter). Companion to [[TAR-01 Brief]].
- 2026-08-11: naming removed. A name needs several stakeholders, so the system stays unnamed until that conversation; nothing in the document depended on it.