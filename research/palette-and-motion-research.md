# Palette Derivation + Motion System — Research

## HEADLINE
`material_color_utilities` **0.13.0 is ALREADY in `pubspec.lock`** (transitive, from Flutter SDK, sha256 `9c337007…`). Promote to direct dependency at zero download cost. **Pin as `material_color_utilities: 0.13.0` with NO caret** — Flutter pins it exactly; a `^` range breaks resolution on SDK upgrade.

---

# PART A — PALETTE DERIVATION

## A1. Why HCT solves this exactly

HCT = Hue + Chroma (from CAM16) + **Tone, which is literally CIELAB L\***. From `contrast.dart`: *"Methods refer to tone, T in the HCT color space. Tone is equivalent to L\* in the L\*a\*b\* color space."*

**That equivalence is the whole trick.** WCAG relative luminance Y is a pure function of L\*, so **contrast between two HCT colours depends ONLY on their two tone numbers, regardless of hue or chroma.** Fix the tones → let the client own the hue → accessibility guaranteed by construction.

```dart
static double ratioOfTones(double toneA, double toneB) {
  toneA = MathUtils.clampDouble(0.0, 100.0, toneA);
  toneB = MathUtils.clampDouble(0.0, 100.0, toneB);
  return _ratioOfYs(ColorUtils.yFromLstar(toneA), ColorUtils.yFromLstar(toneB));
}
static double _ratioOfYs(double y1, double y2) {
  final lighter = y1 > y2 ? y1 : y2;
  final darker  = (lighter == y2) ? y1 : y2;
  return (lighter + 5.0) / (darker + 5.0);   // standard WCAG 2.x
}
```

**Gamut guardrail is built into the type.** `Hct.from(hue, chroma, tone)`: *"The color returned may be lower than the requested chroma... If the HCT color is outside of the sRGB gamut, chroma will decrease until it is inside the gamut."* Hue and tone always honoured exactly; **chroma is the axis that yields.** Cannot request an unrepresentable colour and get garbage.

## A2. Confirmed Dart API (v0.13.0, material.io, Apache-2.0)
| Symbol | Signature | Use |
|---|---|---|
| `Hct.from` | `(double hue, double chroma, double tone)` | build from HCT |
| `Hct.fromInt` | `(int argb)` | parse client hex |
| `TonalPalette.of` | `(double hue, double chroma)` | fixed-chroma ramp |
| `TonalPalette.get` | `int get(int tone)` / `Hct getHct(double)` | pull a tone |
| `TonalPalette.commonTones` | `[0,10,20,30,40,50,60,70,80,90,95,99,100]` | |
| `Contrast` | `ratioOfTones`, `lighter`, `darker`, `lighterUnsafe`, `darkerUnsafe` | validation |
| `DynamicColor` | `foregroundTone`, `enableLightForeground`, `tonePrefersLightForeground`, `toneAllowsLightForeground` | on-colour picking |
| `Blend.harmonize` | `(int designColor, int sourceColor)` | pull semantics toward brand |
| Schemes | `SchemeTonalSpot`, `SchemeContent`, `SchemeFidelity`, `SchemeVibrant`, `SchemeExpressive`, `SchemeNeutral`, `SchemeMonochrome` | |
| `MaterialDynamicColors` | role accessors, takes `DynamicScheme` | full token set |

## A3. Tone table (verified from `material_dynamic_colors.dart`)
| Role | Light tone | Dark tone | ContrastCurve (low, normal, medium, high) |
|---|---|---|---|
| primary | 40 | 80 | 3.0, 4.5, 7.0, 7.0 |
| onPrimary | 100 | 20 | 4.5, 7.0, 11.0, 21.0 |
| primaryContainer | 90 | 30 | 1.0, 1.0, 3.0, 4.5 |
| onPrimaryContainer | 30 | 90 | 3.0, 4.5, 7.0, 11.0 |
| secondary | 40 | 80 | 3.0, 4.5, 7.0, 7.0 |
| surface | 98 | 6 | — |
| onSurface | 10 | 90 | 4.5, 7.0, 11.0, 21.0 |
| outline | 50 | 60 | 1.5, 3.0, 4.5, 7.0 |
| error | 40 | 80 | 3.0, 4.5, 7.0, 7.0 |

ContrastCurve numbers = **target WCAG ratios**, not tones. `contrastLevel` (−1.0→1.0) interpolates between the four columns; 0.0 = normal (4.5 body text). **`contrastLevel: 1.0` is a free high-contrast accessibility mode.** `ToneDeltaPair` additionally forces e.g. primary/primaryContainer ≥10 tones apart so they can never collapse.

## A4. Scheme variants — where guardrail strength is chosen
```dart
// SchemeTonalSpot (Material You default)
primaryPalette:        TonalPalette.of(hue, 36.0),   // ← CLIENT CHROMA DISCARDED
secondaryPalette:      TonalPalette.of(hue, 16.0),
tertiaryPalette:       TonalPalette.of(hue + 60.0, 24.0),
neutralPalette:        TonalPalette.of(hue,  6.0),
neutralVariantPalette: TonalPalette.of(hue,  8.0),

// SchemeVibrant:  primary chroma 200 (gamut-clamped), neutral 10, neutralVariant 12
// SchemeExpressive: primary hue+240, neutral hue+15 chroma 8
// SchemeContent/Fidelity: TonalPalette.of(hue, sourceHct.chroma)  ← brand chroma PRESERVED
```
**`SchemeTonalSpot` throws away the client's chroma entirely (fixed 36).** Neon `#00FF00` and muted `#4A7C4A` produce the same ramp. **That is Material You's answer to an extreme source colour: don't clamp it, discard the chroma channel and keep only hue.** Only Content/Fidelity preserve brand chroma — those are where a bad client hex can hurt.

Error is fixed and brand-independent: `errorPalette ?? TonalPalette.of(25.0, 84.0)`.

## A5. Radix 12-step role table (the clearest published "what each step is FOR")
| Step | Role |
|---|---|
| 1 | App background |
| 2 | Subtle background |
| 3 | UI element background |
| 4 | Hovered UI element bg |
| 5 | Active/selected UI element bg |
| 6 | Subtle borders & separators |
| 7 | UI element border, focus rings |
| 8 | Hovered UI element border |
| 9 | Solid backgrounds (**highest chroma — this is the brand colour slot**) |
| 10 | Hovered solid bg |
| 11 | Low-contrast text |
| 12 | High-contrast text |

Grouped: 1–2 backgrounds · 3–5 component bg · 6–8 borders · 9–10 solid fills · 11–12 text. Steps 11/12 guaranteed Lc 60 / Lc 90 APCA on step-2 bg.
**Key exception:** *"Sky, Mint, Lime, Yellow, and Amber are designed for dark foreground text at steps 9 and 10."* Radix hardcodes this per-hue. **We must compute it (see A8a).**
Radix note: use **grey** for text steps in application UI (functional); accent-tinted text only for marketing. → tenant app text should be near-neutral, not brand-tinted.

## A6. OKLCH vs HCT
HSL's three failures: (1) unequal perceived lightness per hue — same `L:50%` looks far darker on blue than yellow; (2) hue shift on lightness change (SASS `darken()` surprises); (3) resulting contrast/accessibility drift. OKLCH: L 0–1 perceptually uniform, C 0–~0.37 (hue-dependent max), H 0–360. Correct gamut mapping = reduce chroma in OKLCH holding hue (CSS Color 4 mandates this), not naive RGB clipping which shifts hue visibly.

**Verdict: use HCT.** Same strategy as OKLCH, but **HCT's lightness axis is the exact input to the WCAG formula** — decisive for a contrast-guaranteeing system. Consider OKLCH only if sharing identical tokens with a web surface via CSS `oklch()`. Dart OKLCH packages exist (`oklch`, `oklab_flutter`, `okcolor`) but none is as mature and none is already in the lockfile.

## A7. Contrast standard: WCAG 2.x gate, APCA tune
**Status 2026:** WCAG 3.0 still a Working Draft (Mar 2026); CR expected ~Q4 2027, REC no earlier than 2028. **APCA remains exploratory, not in the normative WCAG 3.0 draft.** WCAG 2.2 (Oct 2023) is current normative and is what EN 301 549 / EU Accessibility Act reference.
→ **Gate builds on WCAG 2.x AA** (also what `Contrast.ratioOfTones` computes free). Use APCA Lc as a secondary design-review signal only.

**WCAG 2.2 AA thresholds:** body 4.5:1 · large text (≥24px, or ≥18.66px bold) 3:1 · non-text UI (icons, input borders, focus rings) 3:1 · AAA 7:1 / 4.5:1. These map exactly onto MCU's ContrastCurve columns.
**APCA Lc:** 90 preferred body · 75 min body ≥18px · 60 min non-body (24px normal/16px bold) · 45 headlines · 30 placeholder/disabled floor · 15 absolute non-text floor ("below this, treat as invisible"). Dark mode uses negative Lc. No production-grade APCA package on pub.dev — port the ~30-line formula if wanted.

## A8. GUARDRAILS

**GOVERNING PRINCIPLE: never render the client's raw hex as a surface. Render a *tone selected from a ramp whose hue came from their hex*.** The raw hex appears nowhere except possibly a "your brand colour" settings swatch. This alone eliminates problems (a) and (b), because text is never placed on the client's colour — it's placed on tone 40 (light) / tone 80 (dark) of the client's hue.

### (a) Brand too light for white text — shift the ON-colour, clamp the fill
```dart
static bool tonePrefersLightForeground(double tone) => tone.round() < 60;
static bool toneAllowsLightForeground(double tone)  => tone <= 49;
static double enableLightForeground(double tone) {
  if (tonePrefersLightForeground(tone) && !toneAllowsLightForeground(tone)) return 49.0;
  return tone;
}
```
| Fill tone | Behaviour |
|---|---|
| ≤49 | white text passes 4.5:1 → use white |
| **50–59** | **dead zone: people expect white but it fails → snap fill down to tone 49.0** |
| ≥60 | white is wrong → use dark text |
Source comment: *"People prefer white foregrounds on ~T60-70... T60 used to create the smallest discontinuity possible when skipping down to T49."*
**This is Radix's hardcoded Sky/Mint/Lime/Yellow/Amber rule, computed instead of hardcoded.**

### (b) Brand too dark for a dark background
Same mechanism inverted: dark scheme puts primary at **tone 80**, not 40. Brand contributes hue; scheme supplies tone. `ToneDeltaPair(primary, primaryContainer, delta:10, nearer)` prevents convergence; ContrastCurve(3,4.5,7,7) forces separation from surface.

### (c) So saturated it vibrates — DON'T detect, DISCARD
`SchemeTonalSpot` = `TonalPalette.of(hue, 36.0)`. Client chroma never enters.
Chroma budget: primary 36 · secondary 16 · tertiary 24 (hue+60) · **neutral 6 · neutralVariant 8**.
If more fidelity wanted, soft-clamp `chroma = min(sourceChroma, 48)` for primary but **hold neutrals at 6/8 regardless** — a chroma-40 background makes every screen feel like a tinted overlay. Vibration is a *pairing* problem anyway, and tone-delta constraints already keep adjacent roles ≥10 tones apart.

### (d) Brand collides with semantic success/error
**Part 1 — keep semantics fixed and independent.** MCU already does: `errorPalette = TonalPalette.of(25.0, 84.0)`, not derived from source. Do the same for success (~hue 145) and warning (~hue 85). **Semantic colours are not white-labelled. A client does not get to make "payment failed" green.**
**Part 2 — detect the collision:** `MathUtils.differenceDegrees(brandHue, 25) < 20` → red-branded operator, alerts stop reading as alerts. Mitigations in order:
1. **Never carry state on colour alone** — every error gets icon + text label (WCAG SC 1.4.1 requires this anyway) → collision becomes cosmetic, not functional.
2. Separate on **tone and chroma**, not hue: error at chroma 84 vs brand primary ≤48 is clearly distinguishable.
3. Tertiary already rotates to hue+60 (brand 25 → tertiary 85, well clear).
4. Never use primary as a status colour when collision detected.

**Opposite move when far apart:** `Blend.harmonize()` pulls a semantic toward brand hue with a hard cap: `rotationDegrees = min(differenceDegrees * 0.5, 15.0)` — never >15°, never >halfway. **Use on success/warning/info so they feel designed; leave ERROR alone** (error should be maximally recognisable, not harmonised).

## A9. RECOMMENDED PIPELINE
**One input: `primaryColor`. Everything else derived.** Other three API fields become *validated hints*, not authorities.
```
client hex → sanitize/parse (fallback 0xFF1672EC on garbage, NEVER transparent)
  → Hct.fromInt(argb)
  → degenerate check: chroma <5 → SchemeMonochrome/SchemeNeutral (grey source makes
                                   TonalSpot produce a colourless app that looks broken)
                      chroma >48 → soft clamp
  → SchemeTonalSpot(light) + SchemeTonalSpot(dark), contrastLevel from OS high-contrast setting
  → MaterialDynamicColors.<role>.getArgb(scheme) for EVERY token
     (do NOT pull TonalPalette.get(40) directly — that skips ContrastCurve + ToneDeltaPair enforcement)
  → semantics OUTSIDE the scheme: error fixed; success/warning via Blend.harmonize
  → assert Contrast.ratioOfTones(...) >= 4.5 on every fg/bg pair (debug + CI)
  → immutable RentOkPalette → ThemeExtension
```
Runtime on-colour when unavoidable:
```dart
final onTone = DynamicColor.foregroundTone(bgHct.tone, 4.5);
final onColor = Hct.from(bgHct.hue, 4.0, onTone).toInt();  // low chroma = near-neutral text
```
Use `Contrast.lighter`/`darker` (return **−1 when unachievable**) not `lighterUnsafe`/`darkerUnsafe` (clamp to 100/0) in validation, so impossible requests surface as failures rather than silently becoming white.

**Ship as immutable state.** Current mutable `AppColor` statics: any path can overwrite them, hot reload doesn't reset, tests leak theme between cases, nothing rebuilds. Replace with `ThemeExtension<RentOkPalette>` built once at boot; the ~150 alias getters become fields computed once.

**API migration (backend stays frozen):** derive everything from `primaryColor`; accept `backgroundColor` only if `ratioOfTones(bgTone, onSurfaceTone) >= 4.5` else log+drop for derived surface; same for `textColor`; `secondaryColor` as tertiary hue/chroma hint or ignore.

---

# PART B — MOTION

## B1. Material 3 (verified from Flutter source)
**`Easing` class** (`packages/flutter/lib/src/material/motion.dart`):
| Token | Value |
|---|---|
| `emphasizedAccelerate` | `Cubic(0.3, 0.0, 0.8, 0.15)` |
| `emphasizedDecelerate` | `Cubic(0.05, 0.7, 0.1, 1.0)` |
| `standard` | `Cubic(0.2, 0.0, 0.0, 1.0)` |
| `standardAccelerate` | `Cubic(0.3, 0.0, 1.0, 1.0)` |
| `standardDecelerate` | `Cubic(0.0, 0.0, 0.0, 1.0)` |
| `legacy` | `Cubic(0.4, 0.0, 0.2, 1.0)` |

**GAP: there is no `Easing.emphasized`.** M3's "emphasized" is a two-segment path, not one cubic. Flutter's stand-in:
```dart
static const ThreePointCubic easeInOutCubicEmphasized = ThreePointCubic(
  Offset(0.05, 0), Offset(0.133333, 0.06), Offset(0.166666, 0.4),
  Offset(0.208333, 0.82), Offset(0.25, 1));
```
**`Durations`:** short1 50 · short2 100 · short3 150 · short4 200 · medium1 250 · medium2 300 · medium3 350 · medium4 400 · long1 450 · long2 500 · long3 550 · long4 600 · extralong1 700 · extralong2 800 · extralong3 900 · extralong4 1000.

**M3 Expressive springs** (androidx tokens; LLM-summarised fetch — spot-check before hardcoding):
| Token | Std damping/stiffness | Expressive damping/stiffness |
|---|---|---|
| Spatial default | 0.9 / 700 | 0.8 / 380 |
| Spatial fast | 0.9 / 1400 | 0.6 / 800 |
| Spatial slow | 0.9 / 300 | 0.8 / 200 |
| Effects default | 1.0 / 1600 | 1.0 / 1600 |
| Effects fast | 1.0 / 3800 | 1.0 / 3800 |
| Effects slow | 1.0 / 800 | 1.0 / 800 |

**Structure matters more than digits: effects (colour, opacity) are ALWAYS critically damped at 1.0 and never overshoot; spatial (position, size, shape) is where bounce lives.**

## B2. Apple / iOS springs
| API | Defaults |
|---|---|
| `.spring(response:dampingFraction:blendDuration:)` | 0.5 / 0.825 / 0 |
| `.spring(duration:bounce:)` | 0.5s / 0.0 |
| `.smooth` / `.snappy` / `.bouncy` | 0.5s; bouncy base bounce ≈0.3 |
| `.interactiveSpring` | response 0.15, damping 0.86, blend 0.25 |

Conversion (WWDC23 s10158): `stiffness = (2π/response)² × mass` · `damping = 4π × dampingFraction × mass / response`.
Interactive → low response + high damping (springs carry incoming velocity, retarget continuously). One-shot → start bounce 0; add 0.15–0.3 only for hero moments; WWDC cautions above ~0.4. Typical iOS: 0.35s nav push/pop, 0.25–0.3s modal sheets.

## B3. Emil Kowalski (emilkowal.ski/ui/great-animations)
- **Duration typically <300ms.**
- `ease-out` for snappy interactions (fast start = quick response impression); plain `ease` for slower/elegant; springs for natural.
- **Animate:** state changes, modal enter/exit, things that genuinely happen gradually, anything with communicative purpose.
- **Do NOT animate:** keyboard-triggered actions — *"never animate these, as they repeat hundreds of times daily and feel slow."* Not every element.
- **Interruptibility is mandatory** — an animation that must finish before reversing feels broken.
- Animate `transform`/`opacity` only (hardware accelerated); never padding/margin (forces layout).
- Respect reduced motion.

## B4. Flutter specifics
Curve mapping: M3 standard → `Easing.standard` · emphasized → `Curves.easeInOutCubicEmphasized` · entering → `emphasizedDecelerate` · leaving → `emphasizedAccelerate` · Emil's snappy → `Curves.easeOutCubic` · legacy → `Curves.fastOutSlowIn`.
Springs: `SpringDescription.withDurationAndBounce({duration = 500ms, bounce = 0.0})` is the direct analogue of Apple's `.spring(duration:bounce:)`. Drive via `controller.animateWith(SpringSimulation(spring, from, to, velocity))` — passing real gesture velocity is what makes drag-release feel continuous.
**Performance:** Impeller default on Android API 29+ since Flutter 3.27 (precompiled shaders kill first-run stutter). Real jank sources now = `saveLayer` (via `Opacity` over complex subtrees, `ShaderMask`, AA clipping) and `BackdropFilter` blur. Prefer `FadeTransition`/`AnimatedOpacity` over `Opacity`; prefer `color.withOpacity()` on one paint over an opacity layer; avoid blur on scroll. `RepaintBoundary` on still subtrees surrounded by repainting ones (overuse on small changing widgets adds layer overhead).
**Hero:** one Hero per tag per route. **Heroes ARE interruptible** — mid-flight navigation redirects the flight (the common "can't interrupt" claim is wrong). Nested navigators: only Heroes in the top-most `PageRoute` of each nested Navigator participate — **the real limitation for our bottom-nav app with per-tab navigators.** `flightShuttleBuilder` is the escape hatch for shape morphing / cross-fading different content.

## B5. RECOMMENDED MOTION TOKENS (`RentOkMotion`, all const, no deps)
| Role | Duration | Curve | Where |
|---|---|---|---|
| instant | 0ms | — | bottom nav tab switch, keyboard-adjacent, scroll position |
| microFeedback | 100ms (short2) | `easeOutCubic` | button press, checkbox, switch, chip |
| stateChange | 150ms (short3) | `Easing.standard` | colour changes, selected fills, badge, icon swap |
| expand | 250ms (medium1) | `emphasizedDecelerate` | accordion, card expand, show-more |
| collapse | 200ms (short4) | `emphasizedAccelerate` | the reverse |
| sheetIn | 300ms (medium2) | `emphasizedDecelerate` | bottom sheets, dialogs, pay-now |
| sheetOut | 200ms (short4) | `emphasizedAccelerate` | dismissing |
| pageTransition | 300ms (medium2) | `easeInOutCubicEmphasized` | push/pop |
| heroFlight | 350ms (medium3) | `easeInOutCubicEmphasized` | complaint card → detail |
| shimmer | 1200ms repeating | `linear` | skeletons |
| celebration | 800ms (extralong2) | spring bounce 0.3 | payment success, spin result, reward |
| springInteractive | — | `withDurationAndBounce(150ms, 0.0)` | drag-dismiss, swipe, finger-tracked |
| springSpatial | — | `withDampingRatio(mass:1, stiffness:380, ratio:0.8)` | position/size soft settle |
| springEffects | — | `withDampingRatio(mass:1, stiffness:1600, ratio:1.0)` | colour/opacity, never overshoots |

**Three governing rules:**
1. **Exit is always faster than entry** (every out-token 50–100ms shorter). Users already decided to leave.
2. **Frequency is inversely proportional to duration.** Bottom nav (dozens of taps/session) = 0ms. Payment success (monthly) = 800ms. Check the tap count before picking a number.
3. **Honour reduced motion from day one.** `MediaQuery.of(context).disableAnimations` → collapse durations to zero except opacity cross-fades. Retrofitting across 483 files later is miserable.

**Scope with the palette:** one `RentOkTheme` ThemeExtension holding `palette` + `motion`, built once at boot, read via one extension getter. Replaces both the mutable `AppColor` statics and scattered `Duration(milliseconds: 300)` literals.

---
## Sources
Radix scale docs · pub.dev/packages/material_color_utilities · material-color-utilities GitHub (material_dynamic_colors.dart, dynamic_color.dart, contrast.dart, dynamic_scheme.dart, blend.dart) · evilmartians.com/chronicles/oklch-in-css-why-quit-rgb-hsl · git.apcacontrast.com/documentation/APCAeasyIntro.html · w3.org/TR/wcag-3.0 · adrianroselli.com/2026/04/wcag3-contrast-as-of-april-2026.html · api.flutter.dev (Durations, Easing, SpringDescription, AnimationController, Hero, RepaintBoundary) · flutter GitHub curves.dart · docs.flutter.dev/perf/impeller · developer.apple.com/videos/play/wwdc2023/10158 · SwiftUI spring/interactiveSpring docs · androidx StandardMotionTokens.kt + ExpressiveMotionTokens.kt · emilkowal.ski/ui/great-animations