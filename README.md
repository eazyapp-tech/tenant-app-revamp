# RentOk Tenant App — Revamp Documentation

Design and product thinking for the full RentOk tenant app overhaul. Backend frozen for this phase; this repo covers concept, design language, and research — no app code lives here.

## Read in this order

1. **[TAR-01 Brief](TAR-01-brief.md)** — the bet, why now, personalization system, build waves, boundaries, success metrics.
2. **[TAR-02 Design Language](TAR-02-design-language.md)** — the visual/motion/type system: laws, typeface choice, color derivation, signature moments. Naming deferred to a stakeholder conversation.
3. **[TAR-03 Problem Hypotheses](TAR-03-problem-hypotheses.md)** — module-by-module diagnosis of the current app, every claim tagged `[PROVEN]` / `[OBSERVED]` / `[INFERRED]`. Trust-first, adoption-second ranking. This is a hypothesis set for validation, not a verdict.
4. **[TAR-04 Research Kit](TAR-04-research-kit.md)** — the interview guides and concept-test deck (tenants, owners, internal team) that validate TAR-03 and test new-feature demand before anything gets built.
5. **[Backend Asks Ledger](backend-asks-ledger.md)** — every additive backend request surfaced along the way, logged, none built, none blocking.
6. **[Current App Feature Map](current-app-feature-map.md)** — full inventory of what the existing app does today, module by module.

## `research/`

Supporting material the docs above cite and build on:
- **[Fintech Reference Teardown](research/fintech-reference-teardown.md)** — source-code teardown of Scapia, Kiwi, slice, Stable Money, CRED, Jupiter, Fi.
- **[Brand Systems Synthesis](research/brand-systems-synthesis.md)** — Apple/Airbnb/Wise/Revolut/Linear/Stripe design systems, what transfers to a white-labelled Indian rental app and what doesn't.
- **[Typeface Research](research/typeface-research.md)** — typeface selection, measured against the app's own font binaries.
- **[Palette and Motion Research](research/palette-and-motion-research.md)** — deriving an accessible palette from one arbitrary client color; motion token specs.
- **[Craft Layer: HIG to Flutter](research/craft-layer-hig-to-flutter.md)** — Apple HIG craft principles (Dynamic Type, iconography, touch targets, states, haptics, accessibility) mapped to the actual Flutter codebase, with file:line citations.

## Status

Concept and design-language phase complete, adversarially critiqued, corrected against the codebase multiple times. No pixels yet, no research sessions run yet. Full status: see the changelog at the bottom of each doc.
