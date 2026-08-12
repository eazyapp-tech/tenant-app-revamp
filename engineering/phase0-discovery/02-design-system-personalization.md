# Phase 0 — Design System Layer & Personalization Pipeline Audit
Package: `/Users/eazypg/rentok_tenant_package` (498 Dart files, 96,833 LoC in lib/)

# PART A — CURRENT DESIGN LANGUAGE

## A1. Color model — `lib/utils/app_colors.dart` (360 lines)
Static class `AppColor`. No ThemeData, no ThemeExtension, no dark mode. Global mutable statics.

**4 mutable core fields:** `primary 0xFF1672EC`, `secondary 0xFF3A89F3`, `background ARGB(255,254,254,254)`, `text 0xFF000000` — each with a null-safe setter.
**6 hardcoded semantic consts (whitelabel can't touch):** success `0xFF4CD964`, warning `0xFFFFC107`, error `0xFFFF1744`, black, white, grey.
**Derived machinery:** `_getContrastingTextColor` (luminance), `_lighten/_darken` (HSL), primaryLight/Dark, secondaryLight/Dark.

**152 `static Color get` getters — aliases, not tokens:**
- ~25 pure `primary` aliases (appPrimaryColor, appBlueColor, appPurple, breakfastColor, colorAccent, appStrongCyan…)
- ~20 `primary.withOpacity(x)` (tabColor .1, appBottomNavBarBg .1, appVeryVeryVeryVeryPaleBlue .03…)
- ~16 `warning` aliases (appYellow, lunchColor, buttonOrange…) + pale variants
- ~13 `success` aliases (rentokGreen, whatsappGreen, green_amount…)
- ~6 `error` aliases (appRed, appFailureRed, accountsDues…)
- ~16 `text.withOpacity(x)` greys (textGrey .6, greyDark .5, widgetBorderColor .15, skeleton .1…)
- ~30 escapees still hardcoded hex: RentPass block (memberShipBack 0xFF0F333E, elite 0xFFF7B124, spin 0xFF214E5B, +16 more), offer yellows, card colors, hintColor, greenCheck, skinTone
- 6 gradients (2 primary-derived, 4 hardcoded); 1 shadow token (`primaryBoxShadow` black .05 blur 10)
- 7 no-op setters that silently swallow assignment

**Verdict:** ~4 real tokens + 6 frozen semantics + 152 alias names. No scale (primary-50..900), no surface/on-surface pairs, no elevation ramp, no state colors, no border family.

**Dead parallel file:** `lib/utils/colors.dart` — legacy `AppTheme` class (primaryColor 0xFF3A89F3 etc.), **still referenced 52 times** — un-whitelabelable second palette.

## A2. Type — `lib/viewutils/app_text_styles.dart`
- Fonts: Poppins + Inter, **only the Regular TTF ships for each** — all other weights faked by the rasterizer. No GoogleFonts.
- `FontType {BOLD w700, SEMI_BOLD w600, MEDIUM w500, REGULAR w400, LIGHT w300}`
- Family selection: `isBody! ? 'Inter' : 'Poppins'` — Poppins default everywhere.
- Scale: s8, s10 (=10.5.sp!), s12, s14, s16, s18, s20, s24, s28. All `.sp`.
- Missing: line-height, letter-spacing, semantic names, TextTheme. Default color `AppColor.black`, NOT whitelabel `AppColor.text`.

## A3. Spacing — `lib/utils/app_dimensions.dart`
14 tokens, all EdgeInsets, all screen-specific, no scale. Referenced only **27 times** — effectively unused. No radius/icon/gap tokens.
**ScreenUtil is a no-op:** `designSize = device size` at `rentok_tenant_package.dart:159` → `.w/.h/.sp` scale ≈ 1.0 always (1,025 `.h/.w` + 111 `.sp` sites ceremonial).

## A4. eazy_* components + adoption counts
- `eazy_card.dart` — EazyCard + SlidableListItem; inline shadow ignores primaryBoxShadow.
- `eazy_button.dart` — EazyButton (20 params); label style hardcoded w400/16 bypassing AppTextStyles.
- `eazy_icons.dart` — ~310-entry String→IconData registry for server icon names. Used 5×.
- `eazy_ui_components.dart` (~20KB) — EazyText/EazyTextField/EazyPrimaryButton…EazyWarningButton + EazyUI snackbars: **the semantic button family and EazyUI API have 0 usages — dead**.
- `shimmer.dart` — randomized skeleton, Colors.grey[300] hardcoded.

Adoption: `showToast` **232** (most-used component, entirely untokenized) · ParentContainer 47 · PlatformProgressIndicator 46 · EazyButton 44 · AppCachedImage 44 · EazyElevatedButton 38 · showSnackBar 30 · EazyCard 23 · EazyErrorWidget 19 · EazyLogo 12 · ShimmerWidget 9 · MyBottomSheet 0.

## A5. viewutils inventory (21 files, 3,261 lines)
Load-bearing three: `toast.dart` (hardcoded Colors.green/red/orange.shade600, fontSize 13), `parent_container.dart` (18-param page shell), `my_bottom_sheet.dart` (openBottomSheet, header fontSize 15.8 hardcoded, Colors.* defaults). Also: eazy_error_widget, eazy_logo (whitelabel logo widget — errorWidget re-loads the same https URL as asset → guaranteed double-fail), rps_custom_painter.dart (1,100-line vector painter), swipeable_button_view (385-line vendored package), info_tooltip_helper (245).

## A6. info_widget — the only server-driven-UI primitive
`TopWidgetModel {title, value, leading_icon, back_color (hex), filter_code, back_color_opacity}`; `_parseColor` defaults **Colors.yellow**. Rendered by `TopWidgetList` (8 sites). Backend already sends per-chip colors + icons.

## A7. Inconsistency quantification (excluding token files)
| Pattern | Count |
|---|---|
| `Color(0x…` | **738** |
| `Colors.…` | **699** (white 270, grey 162, black 130 → 400 sites ignore whitelabel bg/text) |
| `TextStyle(` | **708** |
| `fontSize:` | 633 |
| `AppColor.` | 2,046 |
| `AppTextStyles.` | 666 |
| `AppDimensions.` | **27** |
| `AppTheme.` legacy | 52 |
| EdgeInsets 1,186 · BorderRadius 586 · GoogleFonts 0 |

**Roll-up: ~41% of color decisions, ~52% of typography, ~98.5% of spacing bypass tokens.**

Worst dirs: presentation/attendance (255 raw hex/9,193 lines), myservice (224 hex, ZERO AppTextStyles), eviction (131 hex). Best: membership (0 raw hex — its palette was moved INTO app_colors as hardcoded getters), offers, notification.

**176 unique hex literals; top repeats are a hand-pasted Tailwind gray/neutral ramp:** 0xFF101828 ×65 (gray-900), 0xFF171717 ×46, 0xFF4A5565 ×43, 0xFFE5E7EB ×39, 0xFF737373 ×38, 0xFF6A7282 ×29, 0xFFF3F4F6 ×24, 0xFF404040 ×22 … + brand primary 0xFF1672EC re-hardcoded 16×. **De-facto second neutral scale = what the redesign's neutral ramp should formalize.**

## A8. Assets
456 files / 413 generated constants (~43 orphans). png 222 · webp 152 · svg 53 · lottie json 26 · mp3 2. Icons mostly raster → can't recolor with whitelabel primary. Triple-tracked icon strategy (SVGs, EazyIcons map, Material icons). 26 Lotties incl. payment success/failure, confetti, attendance anims, splash logo (unused). Generated-file path bug: `accountsWhatsappIcon = '...lib/Assets.whatsAppIcon'` (literal template failure). No single illustration language.

# PART B — PERSONALIZATION PIPELINE

## B1. `/others/whitelabel-user` contract (`lib/models/whitelabel_res.dart`)
Envelope `whitelabel_user` → `WhiteLabelUser`. Consumed: appName, packageName, 4 colors, logo, appStoreLink, websiteLink, navigationMenu, introText, appSupportNumber, privacyPolicyUrl, tncUrl.
**Parsed then dropped: playStoreLink, inviteLink, shortLinkName, `splashScreenMedia`, `showCashback`, `style`** ← `style` looks purpose-built for design variants, nothing consumes it. Never parsed: id, pgId, brandName. NavigationMenuItem: `icon` and `deeplinkUrl` never used.

## B2. `changeTheme()` — 14 global static mutations, no rebuild signal
`rentok_tenant_package.dart:373`. Writes AppColor.primaryColor/secondary/backgroundColor/textColor + Assets.appIcons + 9 Constants. Defects:
1. Fallbacks are accidental self-assignments via getter/setter aliasing.
2. `Assets.appIcons` is a mutable static in the GENERATED assets file — regeneration wipes the whitelabel hook.
3. `EazyUtils.hexToColor` (eazy_utils.dart:1086): returns Colors.transparent on bad input; `alpha` param BLENDS TOWARD WHITE (not opacity); strips incoming alpha.

Bootstrap: cache-hit → apply + 10s background refresh; cache-miss → blocking 15s fetch. `MaterialApp` has **no `theme:` at all**. navigationMenu only applied when length > 2.

## B3. Attributes reaching the client
**`profile_details_v2.dart` TenantData (~150 fields)** — richest source: propertyId/Address/MapLink, pgName, **pgLogo**, room/roomType, support contacts; gender, dob, nationality, motherTongue, bloodGroup, parents, guardians, emergencyContacts; prev+perm 9-field addresses; **life-stage: workingType, employmentType, occupation, monthlyIncome, company fields, university, graduationYear, courseName/Year**; **foodPreference**; `facilities` (dynamic, unparsed); tenancy commercials (rent, deposit, DOJ, lockin, notice, grace…); KYC/docs incl. PAN data; vehicle; Eqaro block; checklists (EvictionChecklist.color = server hex). Wrapper adds showKycSection, tenantAppInfo versions, isComplaintBotActive, complaintBotNumber.

**`pg_details_model.dart` (property profile, 42 fields):** **city, state, pincode, landmark, lat/long, `pgAvailableFor` (gender policy), `tenantsPreferred` (segment), isMess, wifiIsChecked, maxOccupancy, noOfRooms, noOfFloors**, electricityUnitCost, lastEntryTime, ownername, billCycle… **No propertyType, no businessType, no structured amenities.**
⚠ Model exists client-side — but check which endpoint populates it (see backend report: these columns never reach tenant endpoints).

**Auth-time:** `auth_response.dart` property records carry **propertyLogoUrl** (second logo channel), propertyAddress, status(0/1/2). `my_properties_res.dart` same.

**Prefs (PreferenceKeys ~48 keys):** identity + pgId/pgNumber/pgName/**pgLogo**/eazyPGID/propertyId + support + doj/loi/np/ap + autopayStatus/Url + whiteLabelConfig. **No city/state/gender/property-type cached.** `PrefsConst` is the MANAGER app's key set vendored in (has `currentLang` — the only i18n hook, wrong class; no l10n exists).

## B4. Feature gating
1. **navigationMenu** — only real server-driven gate. Global untyped `var navigationMenu = []`. 8 hardcoded key cases; unknown keys dropped; ≤2 items ignored → fallback Home/Account/Tickets/Profile. Backend icon + deeplinkUrl ignored (EazyIcons registry exists but unwired). icon/filledIcon naming inverted.
2. **76 flag-shaped fields scattered across response models** (showKycSection, isSmartAttendanceEnabled, isMealLive, isPartialPayment, autopayStatus, payment page flags, isProfileLocked…). No feature-flag service.
3. **Hardcoded client-side gating:** home = fixed Column; `Constants.appName != "Orchid Parc"` gate; two hardcoded Firebase pgIDs for "# Feels Like Home" (home.dart:397 + profile_my_renting_info_section_card.dart:53,86).

## B5. pgLogo — three uncoordinated channels
1. Whitelabel app logo → Assets.appIcons → EazyLogo (12 render sites). RENDERED.
2. **Property logo `pg_logo`** → fetched via profile, cached to prefs at profile_provider.dart:156 — **`PrefsUtils.getPgLogo()` has ZERO call sites. Never rendered anywhere.**
3. Login-time `propertyLogoUrl` — never persisted, never rendered.
Also `PreferenceKeys.isLogoChanged` has no writer or reader.

## B6. Server-driven visual data already flowing (live hooks)
- info_widget chips: back_color + leading_icon + opacity (live)
- RewardModel: textColor, ctaColor, ctaTextColor, backgroundColor, logoSrc, brandName, tags (live, full per-reward theming)
- HomeAccountCardModel.color/imagePath (live)
- EvictionChecklist.color, eviction status colors, attendance typeTextColor (live via hexToColor)
- announcement_res: tag, filterCode, **templateId** (template system exists server-side)
- **Unused hooks: whitelabel.style, splashScreenMedia, NavigationMenuItem.icon+deeplinkUrl (EazyIcons.getIcon ready to consume)**
