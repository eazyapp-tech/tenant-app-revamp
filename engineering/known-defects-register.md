# Known Defects Register — Current Production Tenant App

Engineering-facing. This is where the current app's verified technical defects live, kept out of the design documents on purpose: the redesign treats correct behavior here as grammar, not as features. Audience: engineers and whoever schedules fixes for the production app while the new app is built.

Sources with full detail and file:line citations: [legacy-app-detailed-diagnosis.md](legacy-app-detailed-diagnosis.md) (the original module-by-module technical diagnosis) and [research/craft-layer-hig-to-flutter.md](../research/craft-layer-hig-to-flutter.md) (measured layout/accessibility audit with a phased fix sequence).

## Highest-harm defects (tenant-visible, live today)

| # | Defect | Where |
|---|---|---|
| 1 | Amounts render unformatted (e.g. ₹12500.0); no Indian digit grouping anywhere; money columns don't align (tabular figures never enabled) | All money surfaces |
| 2 | Receipt delivery via WhatsApp frequently fails, leaving tenants without proof of payment; error path can strand a stuck loading dialog | Accounts |
| 3 | Payment failure screen ships placeholder copy ("June Rent", test description), an invalid color constant, and a crash path for cash payments | Pay flow |
| 4 | Profile-completion status displayed inverted (incomplete shows as complete) | Home / profile status card |
| 5 | UPI selection row breaks at the top of the ordinary system font-size slider (before accessibility sizes); silent clip in release builds | Pay flow |
| 6 | Ordinary boot/server errors route tenants to the "you may have been evicted" screen | Boot |
| 7 | Move-out WhatsApp message interpolates internal key names instead of tenant values | Legacy move-out |
| 8 | Reward cards clipped at normal text size (230px card in a 200px viewport, plus 90px dead space) | Home |
| 9 | Notification taps do nothing except for move-out types | Notifications |
| 10 | Bottom navigation selected/unselected icons are swapped; nav clips at ~1.7× text scale | Shell |
| 11 | Tap targets below minimum in the login flow (shrunk checkboxes/radios); a shared button primitive allows 35×35 | Auth + shared |
| 12 | 71 of 73 gesture handlers don't register taps on their padding (hit-test behavior unset) | App-wide |
| 13 | Offers duplicate on refresh; offers page double-fetches with conflicting initial tabs | Offers |
| 14 | Duplicate network calls per home open (home page data ×2–3, complaints ×2, food ×2); promo carousel timer leak accelerates over time | Home |
| 15 | Screen-reader support effectively absent (1 semantic annotation in 498 files, no icon labels); no reduce-motion handling against 15 looping animations | App-wide |
| 16 | White-label client colors mostly never reach the UI; semantic colors derive from the client's brand color (a red-branded client can't distinguish paid from overdue) | Theming |
| 17 | Property logo fetched and cached but never displayed anywhere | Branding |
| 18 | Invite-your-property flow gated off for all white-label users; its sheet CTA is a no-op | Growth |
| 19 | 33 text styles reference a font that is not bundled (silently falls back to system font) | Services module |
| 20 | The responsive-scaling library is configured as a no-op (design size = device size), so all 1,154 scaling calls do nothing | App-wide |

## Recommended handling

A phased, provably-safe fix sequence for the production app exists in [research/craft-layer-hig-to-flutter.md](../research/craft-layer-hig-to-flutter.md) (Phase 0 items are mechanical and need no design decisions). Whether prod receives these fixes in parallel with the new build is an open capacity decision tracked in TAR-00.

None of these defects constrain the new app's design. They exist here so they are not forgotten, not so they are dwelt on.
