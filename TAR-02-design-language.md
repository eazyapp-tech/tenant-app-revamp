# TAR-02 · The Design Language

**Read [TAR-00](TAR-00-vision-and-requirements.md) first.** This document describes how the new app looks, moves, and speaks, and why those choices survive being repainted in any client's colors. Detailed measurements, specifications, and the studies behind each choice live in the `research/` folder for those who want the depth.

> **Naming is deferred.** This system will eventually carry a name, and naming it needs several stakeholders in the room. Until then it is simply the RentOk tenant app design language. Nothing below depends on the name.

*Last updated 12 August 2026. Owner: Sanchay.*

---

## What this system believes

A tenant should feel the app belongs to the place they live, not to the company that sold it. Every rule below serves that.

### The four laws

**1. The hero is the tenant's own facts.** We cannot art-direct a client's building, and nothing physical arrives in the post for us to glorify. What we can render with real weight is the tenant's own truth: Room 302. Third floor. Eighteen months. Rs 25,000 held. The property's logo, name, and address frame those facts; the facts carry the screen.

**2. Timeless in structure, modern in behavior.** The still image shows restraint: type, grid, honest photography, none of this year's visual fashion. Motion carries the modernity. A screenshot should be hard to date; the moment a finger touches the screen, it should feel like next year's software.

**3. The ceiling is world-class, the floor is dignified.** The app must delight a design-literate professional in a Bengaluru co-living and remain fully usable for a migrant worker on a budget phone in daylight. Sophistication reveals itself as someone engages. Nothing basic hides behind novelty, and there is never a stripped-down "simple mode", which is only a polite insult.

**4. Identity lives everywhere except color.** White-label clients replace our palette and logo with theirs. What stays ours is the typeface, the way type is scaled, how things move, how surfaces separate, the voice, and the shape of our moments. Meeting this constraint well is what would make this system worth citing by other teams.

### The reference bar

Our closest relatives are not other property apps. They are the Indian fintech apps that made boring, adult financial products feel worth owning and showing off. Rent, receipts, and paperwork are the most boring products of all. Nobody has done for renting what those apps did for money. From studying them at source-code level, one lesson stood out: each makes exactly one expensive, unmistakable investment and keeps everything else disciplined. Ours is the typeface.

---

## Type: the one expensive commitment

**The face is Anek, drawn by Ek Type in Mumbai.** Why this one, out of everything money could buy:

- **It speaks nine Indian scripts plus English** (Devanagari, Tamil, Telugu, Kannada, Bangla, Gujarati, Gurmukhi, Malayalam, Odia), all built to identical proportions. A Hindi or Tamil version of the app becomes a file swap where nothing shifts or breaks. No other family in the world offers this.
- **It has real weights.** The current app ships only one weight and fakes every bold, which is part of why the type never looks fully confident. Anek gives us the full range genuinely, plus a width range that gives us a distinctive voice for big numbers without buying a second font.
- **Its numbers can align in columns**, which money screens require.
- **Its license is free forever, for unlimited client apps.** Every commercial font we evaluated charges per app, which is poison for a white-label product. Here, money would buy a worse outcome. That is rare and worth savoring.
- **It is an Indian face from an Indian foundry.** The common alternatives make every app look like every other app. This reads as a decision, and it is one no competitor can copy without copying the reasoning.

**How type behaves:**

- **Reading text has a ceiling and display has a floor, with nothing mushy in between.** Screens read as one big statement plus quiet support, never as a wall of medium-sized text. This single rule is most of what separates the apps we admire from forms.
- **Spacing between letters follows the size and the script.** Big statements tighten slightly; tiny labels spread slightly and go uppercase. That contrast is a signature no client color can erase. And for Indian scripts the tightening switches off, because Devanagari and its cousins need their room; the rule bends to the script, never the reverse.
- **Money is always aligned, always grouped the Indian way.** Rs 1,50,000, never 150,000. Amounts, durations, and room numbers are three different things and are styled as three different things: a room number is a name, not a quantity.
- **Emphasis comes from size and placement, not from ever-bolder text.** There is a named ceiling on boldness. This is what keeps screens from shouting.

---

## Color: a system that survives being replaced

The client hands us one brand color. **We never place text on that raw color and we never display it as-is.** Instead we derive a complete palette from it: a family of related tones, each with a guaranteed-readable partner for text. The client sees their brand everywhere; the system guarantees no combination is ever illegible. The mathematics behind this ships in a library the app already carries, and the derivation handles hostile inputs gracefully: a neon color calms down, a near-gray color gets a dignified neutral scheme, a too-light color never receives white text.

- **Grays do not exist.** Every "gray" is the ink color at reduced strength, so the whole hierarchy re-derives itself correctly whatever background the client chose.
- **Meaning colors are locked and are not for sale.** Paid is always the same green. Overdue is always the same red. A client's brand can be red; their "payment failed" cannot become green. In the current app the meaning colors follow the brand color, which means a red-branded property cannot tell paid from overdue at a glance. The new system makes that impossible.
- **Color never carries meaning alone.** Every state also has an icon and a word. This is required for accessibility, and it means a color collision is only ever cosmetic, never dangerous.
- **Light first.** Our tenants read outdoors, in daylight, often on inexpensive screens where dark themes turn to mud. Dark is a stage we step onto for celebration moments, not a theme.

---

## Surfaces, space, and depth

- **Hairlines, not shadows.** Cards are calm surfaces separated by fine lines, the way the most expensive-feeling financial apps do it. One soft shadow exists in the whole system, reserved for things that genuinely float, like a sheet sliding up.
- **Corners are consistent and modest.** One radius per kind of thing. We reject the giant balloon corners currently in fashion: they will date fast, they waste vertical space on small phones, and they fight client logos of unknown shape.
- **Spacing follows one rhythm.** Every gap comes from a single scale, and density is a deliberate per-screen choice: air around the hero facts, compactness in ledgers and lists, and a written reason for each.

## Motion

Two rules govern every animation:

1. **Exits are faster than entrances.** The tenant already decided to leave; never make them wait.
2. **The more often something is touched, the less it animates.** Switching tabs happens dozens of times a session and takes zero time. Payment success happens once a month and earns a real moment.

Color and transparency changes never bounce; only position and size may spring. Anything a finger drags follows the finger exactly. And from day one the app honors the system's reduce-motion setting, because the people who need it are the people we hear from least.

## Iconography

- **One icon family, everywhere.** The current app runs three unrelated icon systems side by side; the new app runs exactly one, whose thickness can match the text it sits beside, so an icon and its label always feel drawn by the same hand.
- **Four sizes, no improvisation.** Icons come in four fixed sizes tied to the text sizes they accompany. Anything larger is an illustration and is treated as one.
- **Selection is a fill, not a swap.** A chosen icon fills in smoothly; an unchosen one is an outline. One icon, one state, no mismatched pairs.
- **An icon never carries meaning alone.** Every meaningful icon has a label or an unmistakable position. Under white-labeling, an icon tinted by an unknown brand color on an unknown background cannot be trusted to be visible, so words back it up.

## States: designing for the unhappy path

Every interactive element answers for eight situations: resting, pressed, selected, disabled, focused, loading, empty, and failed. Two get special weight because our audience lives there:

- **Waiting and offline are first-class designs, not afterthoughts.** A tenant on a weak connection sees loading, retry, and stale data more often than a well-connected one sees anything. "This was updated 3 hours ago" is an honest state of its own, distinct from loading and from error.
- **Pressed feedback is a slight shrink, not a color change**, because it is the one response that works identically under every client's palette.
- **Failure explains itself.** A disabled button says why nearby. An error names the problem and the way out. Raw technical messages never reach a tenant's eyes.

## The quiet screens

When the new app launches, every migrated tenant starts with empty everything. The cold start is not an edge case for us; on day one it is the whole experience. So the screens that show nothing get as much design love as the screens that show everything, and because they are seen rarely, our own motion rule says they are exactly where rich animation and illustration are allowed to spend.

**A zero has three different feelings, and we design all three:**

- **The zero that is good news.** No dues. No open complaints. These are small victories and they look like it: a moment of warmth, a line with a smile in it ("No dues. Enjoy the month."), never a gray shrug.
- **The zero that is an invitation.** No documents yet, no first payment, nothing booked. These teach in one sentence, show one clear action, and make starting feel easy. The first-ever screen of every part of the app is designed as a welcome, not a blank.
- **The zero that is our fault.** Nothing loaded, connection lost. These own the failure plainly, keep whatever was last known on screen with its age shown honestly, and offer one obvious retry.

**Waiting on a person is its own state.** A join request waiting for the owner. A complaint waiting for the electrician. A deposit waiting for a refund. These are not loading spinners: a human is the dependency. So the screen shows who, shows honest progress, and offers a polite nudge when waiting has gone on too long. A tenant should never stare at a blank "pending."

**Permissions are asked like a good guest asks.** Camera, location, notifications: each system permission is a trust cliff. The rule: never ask before the value is obvious, always precede the system dialog with a warm plain-words screen of ours that says what we need and why in one breath, and always survive refusal gracefully with a way back later. The reasons behind each ask, and what the tenant gets in return, live in [TAR-05](TAR-05-how-features-earn-their-place.md).

**Interrupted flows resume.** A payment cut off by a phone call, a document upload abandoned at step three, the app closed mid-signature: every multi-step flow saves its progress and reopens where the tenant left off. Starting over is a design failure, not a tenant failure.

## Illustration

Type, color, motion, and icons are defined above; illustration is the fifth voice, and today's app has none: its images are a style jumble collected over years. The new app has one illustration language, and it lives in specific places:

- **Where illustration belongs:** the quiet screens, welcomes and first-runs, permission explainers, celebrations, and the moments described in TAR-05 where a warm image does what words cannot. These are also where animated illustration (the living, looping kind the best modern Indian apps use) earns its place.
- **Where it is banned:** transactional screens. A dues list, a passbook, a document status never carries decoration. Money screens stay quiet.
- **What it looks like:** warm, specific, and Indian without costume: real everyday textures of rented life (a corridor, a tiffin, a ceiling fan, a lock and key), never generic corporate figures with no faces and no place. It must sit comfortably beside any client's colors, so it leans on our ink and paper tones with restrained accents rather than a fixed palette.
- **One open decision:** whether the set is commissioned as custom artwork or built as a rigorously curated style. That is a budget and stakeholder call, tracked in TAR-00's open decisions.

## Voice

- **Concrete, not clever.** Name the actual thing: rent, deposit, room, food, complaint. Wordplay does not survive translation and does not land for a tenant reading in their second language.
- **Plain first, warm second.** "Rs 8,500 due in 4 days" before any personality. Warmth lives in the moments: the welcome, rent paid, the goodbye.
- **Never exclusive.** The membership-and-tiers style of Indian fintech is exclusionary when applied to housing. Nobody should feel their home is a club they might not get into.
- **Built for translation from day one.** Hindi first among them. Copy is written so it translates without dying, and every screen survives longer words.

## Touch, comfort, and access

- **Targets fit thumbs, with breathing room.** Every tappable thing meets the stricter of the international standards, with space between neighbors, because a mistap on a money screen costs trust.
- **The screen respects the hand.** Primary actions live where a thumb rests. Destructive actions never sit in the easiest spot.
- **Text can grow without breaking.** When a tenant raises their system font size, containers grow and layouts adapt; nothing clips, and an amount is never truncated, because a cut-off amount is a wrong amount. The current app fails this at even modest settings; the new one treats it as law.
- **The app speaks to screen readers.** Every amount, date, and button announces itself meaningfully. A tenant who cannot see the screen can still answer: how much do I owe, by when, and did my payment go through.
- **Touch has a pulse.** Gentle physical feedback marks confirmed outcomes: rent confirmed, attendance accepted, an error stopping you. Never decoration, never repetition, always the outcome rather than the tap, and always accompanied by something visible.

## The dignity laws

- **Age limits content, never ability.** Under-18 tenants get curated, age-appropriate content with all profiling off. That is Indian law and our floor.
- **No stereotype ever ships.** Personalization keys on needs and rules, not on assumptions about gender, age, or class.
- **The floor is served silently.** Budget phones, daylight, limited English, expensive data: accommodated everywhere, announced nowhere.

## The bans

A design language is enforced by what it forbids. The named prohibitions:

1. No text on the client's raw brand color.
2. No meaning carried by color alone.
3. No boldness above the named ceiling; no reading text below the named floor.
4. No letter-tightening on Indian scripts.
5. No giant fashion corners; no decorative blur.
6. No animation on high-frequency actions; no bounce on color or fade.
7. No icon without a label or unmistakable position.
8. No fixed-height container around text that can grow.
9. No raw technical error shown to a tenant.
10. No dark-only design; daylight is the default condition.
11. No prize mechanics attached to rent.
12. No "simple mode."
13. No system permission asked before its value is shown.
14. No fake exchange: if a feature asks something of a tenant and offers nothing real back, the ask stays plain and honest instead of gamified.

## The signature moments

Three moments carry the brand, designed to be worth showing someone:

1. **Arrival.** The property's own logo resolves on first open. The tenant's first impression is their home's mark, not ours.
2. **Rent, done.** The screen settles into success and the receipt appears as a document: designed like paper, worth keeping, ready to send. Tenants genuinely need this document, for tax, for verification, for proof of address, which is why it will be the most shared screen in the app without a single gimmick.
3. **Showing up.** Marking attendance or a meal returns a human acknowledgment, and history fills in like a streak: quiet pride, daily.

## What "benchmark" means here

This system counts as a benchmark only if someone outside RentOk could read its published form and build something consistent with it: the principles, the type rules, the color derivation, the motion values, the bans, and honest examples of right and wrong. The systems we learned the most from are the ones that published themselves. Ours will be publishable.

## Changelog

- 10 August 2026: first version, assembled from the fintech teardown, brand-system synthesis, typeface, color, and craft research (all in `research/`).
- 12 August 2026: rewritten in plain language for the full audience. Added: iconography, states, voice, touch and access, the dignity laws including the under-18 rule, and the named bans. Measurement detail moved entirely to `research/`.
- 12 August 2026, later: added the quiet screens chapter (the three kinds of zero, waiting on a person, permission manners, resumed flows), the illustration language, and two bans (13, 14) that came out of the positioning work in TAR-05.
