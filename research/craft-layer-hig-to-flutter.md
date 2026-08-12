# Craft Layer — Apple HIG mapped to Flutter (measured against our code + Flutter 3.44.1 SDK source)

Baseline measured: 498 Dart files · 1,418 `Text(` · 1,025 `.h`/`.w` · 129 `.sp` · 188 `InkWell` · 73 `GestureDetector` · 34 `IconButton` · **1 `Semantics`** · **0 `tooltip`** · **0 `HapticFeedback`** · **0 `TextScaler`** · 3 `LayoutBuilder` vs **92 `MediaQuery.of(context).size`**.

## 0. THREE ROOT DEFECTS underneath everything
**D1. `flutter_screenutil` is an identity function.** `rentok_tenant_package.dart:159` sets `designSize` to the live device size. Package source (`screen_util.dart:216-224`): `scaleWidth = screenWidth / _uiSize.width` → `1.0`. All 1,154 `.h/.w/.sp` calls return input unchanged. **The app looks like it has a responsive strategy and has none.** Fix is deletion, not a real designSize (that's the proportional-scaling anti-pattern).
**D2. No `ThemeData`, no `MaterialApp.builder`.** `:142` is `MaterialApp(navigatorKey:, debugShowCheckedModeBanner:, home:)`. No `theme:`, no `builder:`. → no `IconThemeData`, no `TextTheme`, no `materialTapTargetSize`, no text-scale policy, **nowhere for any craft decision to live**, so everything must be repeated at 1,418 call sites.
**D3. System text scale flows through unmanaged.** `Text` applies `MediaQuery.textScalerOf` by default. Nothing clamps, measures, or reacts. Text grows; containers don't.

---

## 1. DYNAMIC TYPE

### iOS point sizes — the curve is NON-LINEAR and CONVERGENT
| Style | Large (default) | AX5 | Factor |
|---|---|---|---|
| Large Title | 34 | 53 | 1.56× |
| Title 1 | 28 | 48 | 1.71× |
| Title 2 | 22 | 47 | 2.14× |
| Headline / Body | 17 | 53 | **3.12×** |
| Footnote | 13 | 44 | 3.38× |
| Caption 1 | 12 | 43 | 3.58× |
| Caption 2 | 11 | 41 | **3.73×** |

**Small styles grow MORE than large ones; at AX5 everything converges to 41–53pt. Hierarchy is preserved by ORDERING, not ratio.** → a system hardcoding "caption = 0.65× body" is WRONG at accessibility sizes. Android 14 (API 34) raised its ceiling to **2.0×** and introduced its own non-linear curve above ~1.5× for the same reason. **This is why `textScaleFactor` was deprecated — a scalar cannot express a curve.**

**Body across all categories:** xSmall 0.82× · Small 0.88× · Medium 0.94× · **Large 1.00×** · xLarge 1.12× · xxLarge 1.24× · xxxLarge 1.35× · AX1 1.65× · AX2 1.94× · AX3 2.35× · AX4 2.76× · AX5 3.12×.
**The 7 non-accessibility categories span 0.82×–1.35× — reachable via the ordinary Display slider without ever opening Accessibility. Treat 1.35× as the floor of "must be pixel-perfect", not an edge case.** Realistic worst case: Android 2.0×, iOS 3.12×.

### Flutter API (verified `painting/text_scaler.dart`, `widgets/media_query.dart`)
`TextScaler.scale(fontSize)` takes the font size as input — that's what models the curve. **Never reconstruct a ratio and multiply.**
`MediaQuery.textScalerOf` (:1709) · `withClampedTextScaling` (:1438) · `withNoTextScaling` (:1414) · `boldTextOf` (:1972) · `highContrastOf` (:1907) · `disableAnimationsOf` (:1950) · `accessibleNavigationOf` (:1863).

### What breaks, precisely
A horizontal `ListView` gives children **tight cross-axis constraints** — inside `SizedBox(height: 200)` every child gets `minHeight == maxHeight == 200`; **the child's own `height:` is ignored.** Its Column still lays out at the size the text demands → `RenderFlex overflow` in debug, **silent clip in release. Release builds do not throw.**

**Growth formula:** `S_max = 1 + (H − C) / T` where H = box height, C = content at scale 1.0, T = the text portion.
- Reward card: C=141, T=53, viewport 200 → **S_max = 2.11** (survives 1.35×, dies between Android 2.0× and iOS AX2).
- **UPI row (110 tall, PAYMENT FLOW): C≈95, T≈40 → S_max = 1.38 — fails at the very first accessibility step AND at the top notch of the ordinary Display slider.**

### The correct patterns
1. **Delete the fixed height** — `SingleChildScrollView(horizontal) > IntrinsicHeight > Row(crossAxisAlignment: stretch)`. Correct for bounded counts (<~20, every rail here). O(n) extra layout pass, free at 5-10 cards. Not inside `ListView.builder` over hundreds.
2. **Compute height from the scaler** when unbounded: `chrome + MediaQuery.textScalerOf(context).scale(textAtBase)` — `.scale()`, NOT `× textScaleFactor`.
3. **Change the layout, don't just grow it** (HIG: *consider adjusting your layout at large font sizes*). `bodyScale = textScalerOf.scale(14)/14; isLargeText = bodyScale >= 1.5` → switch rail to full-width column. **Cap the NUMBER OF CARDS at large text, never the number of lines.** Dropping lines destroys information; dropping the 4th offer doesn't.
4. **Never use `FittedBox` for text scaling** — it shrinks text back down, silently cancelling the user's accessibility setting while appearing to work. 4 uses in codebase; audit each.
5. **Widget-test it:** `MediaQuery(data: MediaQueryData(textScaler: TextScaler.linear(2.0)))` + `expect(tester.takeException(), isNull)`. Parameterise over `[1.0, 1.35, 1.6, 2.0, 3.12]`.

### LIVE BUG (at scale 1.0, today, every device)
`home_reward_cards_section.dart:34-70`: `Container(height: 290.h)` → `SizedBox(height: 200.h)` → `ListView.builder` → `Container(height: 230.h, width: 172.w)`. **The card asks 230, is given tight 200, its declared height is discarded. Design intent already lost. Outer 290 leaves 90px dead space.**

### The 21 fixed-height rails to convert
| File | Line | H |
|---|---|---|
| `homepage/sections/home_offers_section/home_offers_section.dart` | 46 | 340 |
| `myservice/overview/service_overview_page2.dart` | 610 | 310 |
| `homepage/sections/home_reward_cards_section/...` | 34 | 290 |
| `homepage/sections/home_life_in_pg_section/...` | 60 | 260 |
| `complaints/widgets/home_complaint_card.dart` | 102 | 250 |
| `homepage/sections/home_menu_section/home_menu_section.dart` | 73 | 250 |
| `home_reward_cards_section` | 37 | 200 |
| `home_your_profile_section` | 57 | 200 |
| `accounts/discount/accounts_cashback.dart` | 183, 489 | 200 |
| `common/widgets/payment_failure_widget_v2.dart` | 349 | 200 |
| `accounts/discount/accounts_cashback.dart` | 278, 401 | 180 |
| `home_offers_section` | 109 | 180 |
| `home_my_account_section` | 38, 86 | 150 |
| `membership/reward/all_reward_page.dart` | 60 | 140 |
| `offer_details/...other_offers_section.dart` | 43 | 140 |
| **`accounts/pay_now/subwidget/upi_widget.dart`** | **65** | **110 ← FIRST (money screen, S_max 1.38)** |
| `upi_widget_skeleton.dart` | 40 | 110 |
| `common/media/edit_image_page.dart` | 122 | 100 |
| `complaints/add_complaint.dart` | 720 | 80 |
| `myservice/listings/book_service_page2.dart` | 381 | 80 |
| `food/widgets/rate_food_bottom.dart` | 157 | 80 |
| `offers/sections/offers_top_offers.dart` | 58 | 80 |

**Bottom nav also fails:** `basepage.dart:147,162,177` — bar 85 (iOS)/75 (Android), item 60, icon 25. Icon 25 + 10.5sp label at 1.4 leading ≈ 40 at 1.0×. At 2.0× label alone needs ~30 → 55 vs a 60 box with no padding. **Clips at ~1.7×. Bottom nav labels are the most-read text in the app.**

**Type ramp:** `app_text_styles.dart` has `s8 = 8.sp`, `s10 = 10.5.sp`. Apple's smallest (Caption 2) is 11pt. On a budget LCD at 1.5 DPR, 8pt ≈ 12 physical px. **Delete `s8`, raise `s10` to 11.** These also scale hardest (3.7×) so they generate the most overflow per character.

**Truncation:** 1,418 `Text`, 68 `maxLines`, 58 `TextOverflow.ellipsis` → ~95% unbounded (safer for a11y per HIG *keep truncation to a minimum*), but containers must then grow. **The 20 `maxLines: 1` are dangerous — at 2.0× a one-line label ellipses away most of its content.**

**Staged ceiling** (a clamp is visible to users as "this app ignores my setting" — treat as dated debt):
`MediaQuery.withClampedTextScaling(maxScaleFactor: kTextScaleCeiling)` in `MaterialApp.builder`. Phase 0: 1.3 → Phase 1: 1.6 → Phase 2: 2.0 → delete.
**Never clamp money screens (`accounts/`, `pay_now/`) below 2.0. A tenant who cannot read the amount cannot consent to the payment.**

**Delete screenutil = provable visual no-op** (it computes 1.0): `20.h→20`, `14.sp→14`, `172.w→172`. 1,154 mechanical replacements, codemod-safe. **Do this BEFORE the rail work** so engineers see real numbers.

---

## 2. ICONOGRAPHY

### Why SF Symbols is the gold standard (4 reasons)
1. **Weight matching** — 9 weights drawn to match SF Pro's text weights.
2. **Optical sizing + 3 scales** — sized relative to surrounding **cap height**, not to a box. Why symbols look *placed*, not pasted.
3. **Design variants** — HIG: outline "works well in toolbars, lists... alongside text"; fill "gives more visual emphasis, good for tab bars and selection." **Outline unselected → fill selected, same family, is the canonical selection idiom.**
4. **Rendering modes** (monochrome/hierarchical/palette/multicolour) + semantic naming (`arrow.up.circle.fill` decomposes to shape/enclosure/variant, so a name is guessable).
**LICENCE: Apple platforms only. Off the table for a Play Store Flutter build. Not negotiable, not worth a workaround.**

### Evaluation
| Library | Icons | Real weight axis? | Fill axis? | Licence |
|---|---|---|---|---|
| **Material Symbols (variable)** | ~3,600×3 | **YES `wght` 100-700** | **YES `FILL` 0-1** | Apache 2.0 |
| Phosphor | ~9,000 | No — 6 *separate static fonts* | separate font | MIT |
| Lucide | ~1,600 | No — SVG stroke-width | No | ISC |
| Remix | ~3,000 | No — 2 sets | 2 sets | Apache 2.0 |
| Tabler | ~5,900 | No | No | MIT |

**RECOMMENDATION: Material Symbols — and it's ALREADY a dependency (`pubspec.yaml:78`, `material_symbols_icons: ^4.2960.0`).**

**The decisive evidence is in the Flutter SDK itself** (`widgets/icon.dart`, `icon_theme_data.dart`):
```dart
final double? fill;          // :128  → FILL
final double? weight;        // :143  → wght
final double? grade;         // :166  → GRAD
final double? opticalSize;   // :185  → opsz
final bool? applyTextScaling;// :250
```
**Flutter's `Icon` widget was built for Material Symbols' axes specifically. Choosing Phosphor/Lucide leaves those 5 parameters permanently dead** and forces hand-rolled weight matching with separate font files.
Phosphor's 6 "weights" are 6 static fonts — **cannot interpolate, cannot animate outline→fill.** Material Symbols' `FILL` is continuous → the selection transition is a `tween`, not a swap. That IS the SF Symbols idiom reproduced.

**File size:** full variable font ~3-4 MB/style; Flutter's icon tree-shaker (`--tree-shake-icons`, default on in release) strips to referenced glyphs, typically <50 KB. Protect it: never pass `--no-tree-shake-icons`; never build `IconData` from a runtime codepoint (only `const IconData` refs are tracked). Existing `eazy_utils.dart:1531-1533` (`case 'currency_rupee': return Icons.currency_rupee;`) is SAFE (returns a const ref).

### The rules
**Size ramp — four sizes, no more:** `iconInline 16` (with 11-13 text) · `iconDefault 20` (with 14-16 text) · `iconNav 24` (standalone/tab/appbar) · `iconFeature 32` (empty states, section headers). Above 32 it's an illustration, use an asset.
Off-ramp rule: `icon = round(fontSize × 1.25)` to nearest even, **floor 16**, cap 24 inline. **Below 16 a stroke icon on a low-DPR LCD loses its counters and becomes a smudge.**
**Weight matching:** icon `wght` = numeric weight of accompanying text (w500 label → `weight: 500`). Exact, because both fonts expose real axes.
**Fill for selection:** `TweenAnimationBuilder(begin:0, end: selected?1:0, 200ms) → Icon(fill: v)`.
**Grade:** `-25` for light icons on dark (counters optical bloom), `0` otherwise. **No SF Symbols equivalent, and genuinely useful for white-label** where a dark client colour makes icons look heavier.
**Optical size:** `opsz` = rendered size, clamped 20-48 (undefined below 20).
**Alignment:** `Row(crossAxisAlignment: center)` is optically correct while icon is 1.25-1.5× the font size. Outside that, centring on the box ≠ centring on cap height and the icon sits visibly low. **Fix by returning to range, not by `Transform.translate`.**
**Icons must scale with text** — default is **OFF** (`icon.dart:267`). HIG: *increase the size of meaningful interface icons as font size increases.* Set `applyTextScaling: true` globally in `IconThemeData`; turn OFF deliberately for decorative icons only.

### Our changes
- **Sizes ad hoc:** 20 (52 uses), 16 (46), **14 (39 — below floor)**, **18 (34 — off-ramp)**, 24 (18), plus 17/22/25/28. Snap all to 16/20/24/32.
- **Two icon systems in parallel:** 178 Material `Icons.*` + 71 `SvgPicture` + 107 `Image.asset` across 5 asset folders. **Icons drawn as PNG cannot take weight, fill, recolour for white-label, or scale with text. Every `Image.asset`-as-icon must become a `Symbols.*` glyph.** Keep `Image.asset` for illustrations/brand marks only.
- **Confirm the variable font is wired, not the static one** — `fill`/`weight`/`grade` silently do nothing against a static font. **This is the single most likely way the migration fails quietly.**
- **INVERTED SELECTION BUG:** `bottom_navigation_provider.dart:32-33` and `:103-104` assign `_rounded` (filled) to UNSELECTED and `_outlined` to SELECTED. **The `FILL` axis makes this class of error impossible** — one icon, one number.

---

## 3. TOUCH TARGETS

HIG Accessibility/Mobility: *offer sufficiently sized controls* AND *consider spacing between controls as important as size*. **Two 48dp buttons touching are worse than two 44dp with 8dp between** — the failure mode of a mistap is worse than a miss.

| Standard | Min | Level |
|---|---|---|
| Apple HIG | 44×44 pt | baseline |
| Material 3 | 48×48 dp + 8dp gap | baseline |
| WCAG 2.1 SC 2.5.5 | 44×44 | AAA |
| WCAG 2.2 SC 2.5.8 | 24×24 | AA |

Flutter constants: `kMinInteractiveDimension = 48.0` (`material/constants.dart:27`), `kMinInteractiveDimensionCupertino = 44.0` (`cupertino/constants.dart:29`). Test guidelines: `androidTapTargetGuideline` 48×48 (`accessibility.dart:785`), `iOSTapTargetGuideline` 44×44 (:800).
**OUR RULE: 48×48 everywhere + 8dp gap.** Cross-platform, majority-Android audience, stricter costs nothing.

**Thumb reach** (430×932pt class; most mid-range Indian Android 393-412 × 850-920dp), from bottom: **Natural 0-280pt** (comfortable, repeated taps) · **Stretch 280-560** (grip shift) · **Hard >560** (two hands). **On a 932pt screen the top 370pt needs two hands — where the app bar and back button live.**
Rules: primary action in bottom 280 · **destructive actions NOT in the natural zone** (easy reach + irreversibility must never combine) · back/close always also available via OS gesture + swipe-to-dismiss · sheet CTA at the bottom above the home indicator.

**Pattern — small icon, large target:** `BoxConstraints(minWidth: 48, minHeight: 48)` (not `SizedBox`, so it grows with text scaling but never shrinks) + `Icon(size: 20)`.

**`GestureDetector` does NOT hit-test transparent padding by default. Only 2 of 73 set `behavior`.** Without `HitTestBehavior.opaque`, the padding added to reach 48dp **is not tappable and the target is still 20dp. The most common silent tap-target bug in Flutter — 71 instances here.**

### Our changes
- **`utils/eazy_button.dart:143`: `minimumSize: Size(width ?? 35, height ?? 35)` — 35×35 fails both 44 and 48, and it's a SHARED primitive so the failure repeats everywhere.** Raise to 48.
- `:59,63,117` use `Size(50,50)` — passes but arbitrary; use `kMinInteractiveDimension`.
- Add `behavior: HitTestBehavior.opaque` to 71 `GestureDetector`s.
- **Remove 4 `MaterialTapTargetSize.shrinkWrap` + `VisualDensity.compact` pairs** — `select_unit.dart:446`, **`phone_number_validation_widget.dart:220`**, `food.dart:596`, `add_complaint.dart:536`. **Two are in the login flow.**
- Audit the 24 icons at 14/16 inside `InkWell`/`GestureDetector` for parent ≥48.

---

## 4. INTERACTION STATES

Eight states, each communicating exactly one thing:
| State | Communicates | Treatment |
|---|---|---|
| Default | available | base |
| Hover (iPad pointer) | pointer would act | 8% state layer |
| **Pressed** | received, now | 10% layer + `scale(0.97)`, **within 100ms of pointer-DOWN** |
| Selected | current choice | FILL 0→1 + tint + **a non-colour cue** |
| Disabled | unavailable + why | 38% content / 12% container + **adjacent helper text giving the reason** |
| Focused | keyboard lands here | 2dp outline, offset 2dp, never removed |
| Loading | working, don't re-tap | in-place spinner, **container size held**, non-interactive |
| Error | this specific thing is wrong | border + icon + text, **never colour alone** |

State layers: hover .08 · focus .10 · pressed .10 · dragged .16 · disabled .38 content / .12 container.

**Two rules that outrank the numbers here:**
- **Never signal state with colour alone** (HIG: *convey information with more than color alone*). Doubly binding: a selected state that is "container turns brand blue" is invisible when a client picks pale yellow. Selected must always carry fill-axis / check glyph / weight change / border.
- **Derive states from the brand colour, never hardcode.** `onBrand(c) => c.computeLuminance() > 0.45 ? Color(0xFF111111) : Colors.white`. **Run the contrast check at boot in `changeTheme()` and log failures to Crashlytics — otherwise the first time you learn a client's colour is unreadable is a support ticket.**

**Loading must not resize the control** — `AnimatedSwitcher` + fixed `minimumSize`. HIG *when possible use a determinate progress indicator* → payment verification has a known polling budget, so show determinate, not an infinite spinner.

### Our changes
- **All 15 `WidgetStateProperty` uses are `.all(...)` — which by definition resolves the same value for every state. `.all()` is the syntax for "I do not have states."** The only genuine `resolveWith` in 498 files is a checkbox fill at `select_unit.dart:439`.
- Define ONE `RentOkButtonStyles`; today `utils/eazy_button.dart` and `viewutils/eazy_elevated_button.dart` overlap.
- **Specify 8 states × 6 primitives** (primary button, secondary button, list row, chip, text field, icon button) = a 48-cell table. Write it, put it in the design language, generate code from it.
- Add the white-label contrast guard to `changeTheme()`.
- **Add a focus outline — there is none.** External keyboard / Switch Control / TalkBack keyboard nav users currently cannot see where they are.

---

## 5. LAYOUT & ADAPTIVITY

**Adaptive ≠ responsive.** Responsive = every dimension is a continuous function of width. Adaptive = a few named configurations with thresholds. Apple's size classes are deliberately coarse because the useful decision is "does the sidebar show", not "is it 253.7pt wide".
**Why proportional scaling is wrong on phones: a 320dp and a 430dp phone differ 34% in width, but thumbs are the same size and eyes the same distance. 44dp × 320/375 = 37.5dp — below the accessibility minimum. Proportional scaling ACTIVELY BREAKS accessibility floors.** Physical constants stay constant; only *space between* and *number of* things change.

**Safe areas (iOS portrait):** Dynamic Island 59/34 · Notch 47/34 · Home button 20/0. Android: status bar 24-48dp, gesture bar 24-48 or 0. **Never hardcode — read `MediaQuery.paddingOf` / `viewPaddingOf`.**
Margins: iOS 16pt compact / 20pt regular; readable width caps ~672pt.

**Breakpoints for this app:**
| Name | Width | Layout change |
|---|---|---|
| Small | 320-359 | margin 16, 1 col, rails 1.2 cards |
| Standard | 360-399 | margin 16, rails 1.5 cards |
| Large | 400-430 | margin 20, rails 1.8 cards |
| Tablet | 600+ | margin 24, 2 col, `maxWidth: 672` |
| Expanded | 840+ | margin 24, 2 col + nav rail |
(600/840 align with M3 window size classes so Flutter's own components agree.)

| Changes at a breakpoint | NEVER changes |
|---|---|
| margin 16/20/24 · column count · cards per rail · nav placement · content max-width · whether secondary content shows | **tap target 48 · font sizes · icon sizes · corner radii · border widths · spacing steps** |

**`LayoutBuilder` vs `MediaQuery` as a rule:** `MediaQuery.sizeOf` = the **window** (global decisions). `LayoutBuilder` = the **parent's constraints** (local decisions: how many cards fit in *this* rail). Using window size for a local decision is wrong inside a split view, sheet, or 2-col tablet layout. **We have 92 window reads : 3 LayoutBuilder — the ratio inverted.**
Also: `MediaQuery.of(context)` subscribes to **every** field — a keyboard opening rebuilds widgets that only care about width. Migrate all 92 to `sizeOf`/`paddingOf`/`viewInsetsOf`/`textScalerOf`.

### Our changes
- **Delete screenutil** (codified proportional-scaling intent; currently 1.0 so removal is free).
- **Page margin is 21, 20, 11, 10 for the same concept** — `my_bottom_sheet.dart:24`, `service_amenities_page.dart:115` (21), elsewhere 20, `info_widget.dart:157` (11), `home_complaint_card.dart:106` (10.w). Collapse to one token.
- **Two spacing systems fighting:** 20(224 uses) · 10(203) · 50(73) · 16(69) · 8(65) · 30(61) · 24(58) · 12(52) · 4(47) · 40(39) · 5(39) → a 4/8/12/16/24 system AND a 5/10/15/20/30 system. **Pick 4/8/12/16/20/24/32/40/48 and codemod.**
- Tablets/foldables unhandled — correctly deprioritised, but put them in the enum so it's explicit not accidental.

---

## 6. HAPTICS

HIG *Playing haptics*: use system patterns per documented meaning · be consistent · **prefer haptics to COMPLEMENT other feedback** · avoid overuse · prefer short haptics for discrete events · **make haptics optional** · be aware of impact on other experiences. Plus HIG Hearing: *use haptics in addition to audio cues*.
**A haptic is punctuation, not narration.** If every word gets a tap the tenant silences the phone and the channel is lost permanently. Also: battery, and startling in a shared PG room.

### CORRECTION: `HapticFeedback` has EIGHT methods, not five (`services/haptic_feedback.dart`)
| Method | iOS | Android | Floor |
|---|---|---|---|
| `vibrate()` | kSystemSoundID_Vibrate | LONG_PRESS | all |
| `lightImpact()` | Light | VIRTUAL_KEY | all |
| `mediumImpact()` | Medium | KEYBOARD_TAP | all |
| `heavyImpact()` | Heavy | CONTEXT_CLICK | **API 23+** |
| `selectionClick()` | **UISelectionFeedbackGenerator** | CLOCK_TICK | all |
| `successNotification()` | Success | CONFIRM | **API 30+** |
| `warningNotification()` | Warning | KEYBOARD_TAP | **API 30+** |
| `errorNotification()` | Error | REJECT | **API 30+** |

`selectionClick()` **does** work on iOS (the "Android-only" belief is out of date).
**The whole notification family is a SILENT NO-OP on Android below API 30 (Android 11).** For migrant workers on budget phones, a meaningful slice gets nothing → **HIG's "complement other feedback" is a HARD REQUIREMENT here: the haptic must never be the only confirmation a payment succeeded.**
Hardware: iPhone Taptic / Pixel LRA are crisp; many budget Androids use ERM motors with 20-40ms spin-up so "light" arrives late and feels like a buzz. **Use few distinct patterns; never require the tenant to distinguish light from medium.**

**Wrapper** with `enabled` flag + **400ms rate limit** (prevents rebuild-loop/stream haptic storms). **Never call from `build()`, a `ChangeNotifier` listener, or a scroll callback.**

### The policy
**Money:** tap "Pay" → **none** (the press state is the feedback) · gateway confirms success → `success()` **on the verified server response, not the SDK callback** · failure → `error()` with the sheet · amount preset / UPI app selection → `select()` · cash-OTP verified → `success()` · opening passbook/receipt → none.
**RULE: fire on the confirmed OUTCOME, never on the INTENT. A haptic on button-press when the payment then fails teaches the tenant that the tap means "done" — exactly wrong on a money screen.**
**Attendance** (highest-value case — tenant holds the phone at arm's length looking at their own face, not at a toast): shutter → `light()` · face+geofence pass, server confirms → `success()` · GPS above the 30m threshold → `warning()` · face match fails → `error()` · **countdown ticking → NONE** (a haptic per second is the exact overuse HIG warns about).
**Errors:** validation on submit → `error()` **once for the whole form, not per field** · wrong OTP → `error()` · network failure on a user-initiated action → `error()` · **network failure on background refresh → none (the tenant didn't ask)** · form valid → none (success is the expectation).
**NEVER for:** page loads, toasts, marketing cards appearing, rail/list scrolling, shimmer transitions, notification arrival, any timer.
**Settings:** "Vibration feedback" toggle in `ProfileOtherOptionsSection`, default on, in `PrefsUtils`.

### Our changes
- **0 haptics in 498 files.**
- **`vibration: ^3.1.3` declared (`pubspec.yaml:44`) and NEVER imported.** It drives the raw motor — on budget Android that reads as an incoming call, not UI feedback. **Do not use it.** `HapticFeedback` needs no extra dep and no `VIBRATE` permission for these constants.
- Implement the wrapper + wire **10 call sites, not 200**.

---

## 7. ACCESSIBILITY BEYOND CONTRAST

HIG: intuitive · **perceivable** (*doesn't rely on any single method to convey information*) · adaptable. Plus *describe your interface for VoiceOver*, *convey information with more than color alone*, *be cautious with fast-moving and blinking animations*, and for reduced motion *replace transitions in x-, y-, z-axes with fades*.
**For a money screen the bar is higher than "traversable": a TalkBack user must answer three questions without sight — how much do I owe, by when, what happens if I don't pay. If the amount is announced "rupee symbol one two five zero zero point zero", none are answerable.**

### Money — two separate live problems
**(1) Formatting.** `service_overview_page2.dart:851` interpolates raw: `"₹${double.parse(booking?.totalAmount ?? '0')}"` → renders **₹12500.0**. **There is NO `NumberFormat` anywhere in `lib/`** — and `intl: ^0.19.0` is already a dependency. Indian grouping (12,500 / 1,25,000) is a locale convention intl implements. **This is a correctness bug visible to every sighted tenant, before it is an accessibility bug.**
**(2) Announcement.** Even formatted, TalkBack reads glyphs literally → `Semantics(label: 'Rent due', value: '12,500 rupees', child: ExcludeSemantics(child: Text(_inr.format(12500))))`. Dates: display `5 Sep`, announce `5 September 2026`.

**Icon-only buttons:** 34 `IconButton`, **0 `tooltip`** → every one announces as "button" with no name. `tooltip` sets the semantic label AND gives sighted users a long-press label.
**Reduce motion:** `MediaQuery.disableAnimationsOf(context)` → `Duration.zero`; per HIG replace x/y/z transitions with a crossfade rather than removing feedback. **15 `Lottie.` uses, 14 `AnimationController`s, 12 × 1200ms shimmer loops — a looping 1200ms shimmer that never stops is exactly the "fast-moving and blinking animation" HIG cautions against.**
**Also honour:** `boldTextOf` (raise weight one step), `highContrastOf`, **`accessibleNavigationOf` — stop auto-advancing carousels/stories, because auto-advance steals screen-reader focus mid-sentence.**
**TalkBack vs VoiceOver:** TalkBack reads `hint` after a pause (so hints must be genuinely optional info); linear navigation is more common on Android making reading order more important; **TalkBack does not reliably announce dynamic changes without `liveRegion: true`.**
**Test guidelines** (`flutter_test/accessibility.dart`): `androidTapTargetGuideline` :785 · `iOSTapTargetGuideline` :800 · `textContrastGuideline` :818 · `labeledTapTargetGuideline` :825. **Add `labeledTapTargetGuideline` first — it fails any node with a tap action and no label, which is close to every interactive element today.**

### The accessible money screen — checklist
1. Amount announced in words with currency named. 2. Due date announced in full, **urgency stated in the label ("overdue by 3 days"), not conveyed by red text alone.** 3. Each passbook line = ONE merged node ("description, amount, date"), not three. 4. Pay button label states the amount: "Pay 12,500 rupees", not "Pay". 5. Result via `SemanticsService.announce` (arrives async, no focus change). 6. Loading states `liveRegion: true`. 7. **Text scale to 2.0 with no clipping and no ellipsis on any number — a truncated amount is a WRONG amount.** 8. **No timeout dismisses a payment confirmation** (HIG *minimize time-boxed elements*; a screen-reader user needs several times longer). 9. Errors carry icon + text, never colour alone. 10. Every target ≥48×48.

### Our changes
**1 `Semantics` in 498 files** (`setup_selfie_camera_page.dart`) · 0 `tooltip` · 0 `MergeSemantics` · 0 `ExcludeSemantics` · **0 uses of `disableAnimations`/`boldText`/`highContrast`/`accessibleNavigation`** · no `NumberFormat`. **The app is effectively unusable with TalkBack today.**

---

## PRIORITY SEQUENCE (harm ÷ cost)

**Phase 0 — this sprint, mechanical, provably safe:**
1. Delete `flutter_screenutil`, codemod 1,154 call sites (visual no-op, it computes 1.0).
2. Add `ThemeData` with `iconTheme`, `materialTapTargetSize: padded`, `textTheme` — **everything else needs somewhere to live.**
3. `NumberFormat.currency(locale: 'en_IN')` — fix `₹12500.0`.
4. `tooltip` on 34 `IconButton`s.
5. `behavior: HitTestBehavior.opaque` on 71 `GestureDetector`s.
6. `eazy_button.dart:143` 35 → 48.
7. `withClampedTextScaling(maxScaleFactor: 1.3)` as an explicit, dated stop-gap.

**Phase 1 — correctness:**
8. Fix the reward-card 230-in-200 clamp bug. 9. Convert 21 rails, `upi_widget.dart` first. 10. Fix bottom nav (clips ~1.7×). 11. Delete `s8`, raise `s10`→11. 12. Ceiling → 1.6.

**Phase 2 — craft:**
13. Migrate to `Symbols.*` (confirm variable font wired). 14. Fix inverted nav icons. 15. 8×6 state matrix, replace 15 `.all()` with `resolveWith`. 16. White-label contrast guard in `changeTheme()`. 17. Haptic wrapper + 10 sites. 18. `Semantics` on money → attendance → complaints. 19. Reduce-motion gate on 15 Lottie + 12 shimmers. 20. `Breakpoint` enum; collapse margins and the two spacing systems. 21. Ceiling → 2.0, then delete.