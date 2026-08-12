# Typeface Selection — Research (measured, not asserted)

## What ships today, measured from the binaries
| Fact | Measurement |
|---|---|
| `Poppins-Regular.ttf` | v4.004, static, 154 KB, 1,059 glyphs, has Devanagari |
| `Inter-Regular.ttf` | v3.019, static, 302 KB, 2,547 glyphs, NO Devanagari |
| Total font payload | **457 KB for two real weights** |
| `FontWeight` refs in `lib/` | 564 |
| Non-400 refs (all synthesized) | **398 = 70.6%** (188×w500, 143×w600, 53×bold, 10×w700, 3×w800, 1×w300) |
| `FontFeature`/`fontVariations` uses | **0** |
| `fontFamily: 'SF Pro Text'` refs | **33** in `lib/myservice/listings/service_amenities_page.dart` + `lib/myservice/bookingstatus/booking_details_page.dart` — **not declared in pubspec, silently falls back to Roboto on Android** |

**Proof of fake bold** (Flutter 3.44.1, real `TextPainter`, "Rent due" @100px):
```
Poppins  w400→443.50  w500→443.50  w600→443.50  w700→443.50
Inter    w400→423.01  w500→423.01  w600→423.01  w700→423.01
```
Identical advance widths at every weight = rasterizer smearing strokes without changing metrics.

**Two further binary defects:**
- **Poppins has NO `kern` feature.** Its entire GPOS feature list is Devanagari shaping. All Latin text in the app is unkerned today.
- **Poppins has no `tnum`.** Money columns cannot align even if requested.
- **Inter v3.019 DOES have `tnum` and it has never been switched on.** One-line quick win available now.

## Shortlist (weights = real cuts on a variable axis, verified from `fvar`)
Stem width = vertical stem of `I` in device px @12sp/1x (below ~1.0px, grayscale AA smears on budget LCDs).

### 1. Anek (Ek Type, Mumbai) — RECOMMENDED
- **Licence: SIL OFL 1.1** (verified `github.com/EkType/Anek/OFL.txt`) — unlimited embedding in unlimited redistributed binaries, no per-app accounting, no fee, no term
- Axes: `wght 100–800`, `wdth 75–125` (on all scripts AND Latin)
- 8 named instances; features `tnum, zero, frac, subs, sups, ordn`; has ₹
- **184 KB** Latin subset with both axes + tnum · **82 KB** with wdth pinned to 100
- x-height/em **0.489** (lowest — see caveat) · x-height/cap 0.765 (highest) · stem 1.00px
- **10 Indic scripts**
- **CAVEAT: Anek sets small.** 0.489 x-height vs Inter's 0.546 → swapping at same `fontSize` loses ~10% apparent size. **Budget a +12% type-scale bump across `AppTextStyles` as part of migration, not as a bug found later.**

### 2. Inter — RUNNER-UP
OFL 1.1 · `wght 100–900`, `opsz 14–32` · `tnum, zero, cv01–cv14, ss01–ss08` · **108 KB** · x-height **0.546** (best) · stem **1.11px** (sturdiest) · **NO Indic at all**. Best raw legibility; already in codebase; but it's the most common typeface in software right now — wrong property for a face that must carry identity when colour is replaced.

### 3–6 (brief)
- **Plus Jakarta Sans** — OFL, 200–800, tnum, 75 KB, x-h 0.536, stem 0.96px. Widest digits (0.732em for `0`) costs money-column width.
- **Figtree** — OFL, 300–900, tnum, **39 KB** (smallest), x-h 0.500, stem 1.01px. Only 459 glyphs; 300 floor.
- **Geist** — OFL, 100–900, tnum + ss01–ss11, 71 KB. Reads as developer-tooling (it's Vercel's brand font).
- **Manrope** — OFL, 200–800, tnum, 59 KB. **DISQUALIFYING: stem 0.88px @12sp/1x**, thinnest measured — will smear on budget LCDs. (Jupiter uses it, but their audience skews newer phones.)

### Explicitly rejected
- **Lexend Deca** (Scapia's workhorse) — **NO `tnum` feature at all.** Full list: `aalt, case, ccmp, dlig, dnom, frac, kern, liga, locl, mark, mkmk, numr, ordn, sinf, ss01, subs, sups, zero`. For an app whose primary screen is a money column, disqualified regardless of merits.
- **Poppins** (incumbent) — no tnum, no kern, single-storey `a` hurts at small sizes.

## Indic coverage — where the decision is actually made

**Anek ships 10 scripts as separate files:** Bangla, Devanagari, Gujarati, Gurmukhi, Kannada, Latin, Malayalam, Odia, Tamil, Telugu. Per-script designers at Ek Type (Kailash Malviya Devanagari, Aadarsh Rajan Tamil, Omkar Bhoir Telugu, Mrunmayee Ghaisas Gujarati, Sulekha Rajkumar Bangla, Maithili Shingre + Vaishnavi Murthy Kannada, Sarang Kulkarni Gurmukhi), engineered by Girish Dalvi.

**Metric compatibility verified directly from binaries.** Every Anek script file reports:
```
x-height 0.489 em   cap-height 0.639 em
digit advances 685/934/950/991/1053/1065/1096/1122/1151
```
**Identical across Latin, Devanagari, Tamil, Telugu, Kannada, Bangla, Gujarati.** Same axes on all ten. → **swap the script font for a localised build and NOTHING reflows.** No other family on Google Fonts offers this. (Latin+digit outlines byte-identical to Anek Latin in 4 of 6 hashed; Devanagari/Kannada have minor Latin outline differences with identical metrics.)

Sizes (wdth pinned, tnum kept): Latin **82 KB** · **Devanagari 846 KB (contains Devanagari AND Latin in one file)** · Tamil 153 KB · Telugu 559 KB · Kannada 415 KB.

**Alternatives and why they lose:**
| Family | Verdict |
|---|---|
| Noto Sans Devanagari | Digits tabular by default (551 units) but no `tnum` feature; **doesn't pair with Inter** (below); Devanagari only — other scripts need separate Noto files with different metrics |
| Mukta (Ek Type) | Has tnum; **static only, 7 files**; siblings for Gujarati/Tamil/Gurmukhi but **no Telugu, Kannada, Bengali** |
| Hind (ITF) | **No numeral features AND no `kern` feature at all** — same defect as Poppins. Reject. |
| Baloo 2 | Rounded/display, 400 floor — wrong register for body |
| Kohinoor (ITF, commercial) | All 11 official Indian writing systems + Latin + Arabic. ₹2,500/style, ₹18,500/family — but see licence section |

**If you pick Inter, the pairing problem measured:**
| | x-height | cap-height | ascent | descent |
|---|---|---|---|---|
| Inter | 0.546 | 0.728 | 0.969 | −0.241 |
| Noto Sans Devanagari | 0.536 | 0.622 | 0.896 | **−0.408** |

x-heights match within 2% (what most pairing advice checks) but **cap heights are 17% apart and descenders 69% apart.** Mixed Hindi+English in one line box either clips Devanagari or forces line height that makes pure-English screens look airy. Hand-tuning `height` per locale forever. *Anek exists precisely to avoid this work.*

## Display face — DO NOT ADD A SERIF

**Use Anek's own width axis as the display voice.** Measured in Flutter, "RENT DUE 15000" @ wght 700:
```
wdth=75 → 506.9px   wdth=90 → 642.2px   wdth=100 → 732.5px   wdth=112 → 842.2px   wdth=125 → 961.0px
```
**90% range, free, in a file we already need.** Condensed 800-weight for the hero number + normal-width 400 for the eyebrow = the two-line eyebrow+display pattern with zero extra bytes and zero extra licence exposure. Genuinely distinctive because almost nobody uses the width axis.

**On the serif question directly:** the serif signal at Kiwi/CRED/Stable Money targets an affluent, English-first, credit-card-holding audience — it says "private bank." Our user is a migrant tenant checking whether rent went through; a high-contrast display serif reads formal and institutional, closer to a legal notice. It also fails practically: **Instrument Serif has no ₹ glyph at all** (verified, U+20B9 absent). Fraunces has ₹ but no `tnum` and a thin feature set (`case, kern, liga, rvrn, ss01`).
If a second voice is ever wanted for celebration screens only: **Fraunces** (variable, opsz 9–144, wght 100–900, +SOFT/WONK, 360 KB) or **Newsreader** (opsz 6–72, wght 200–800, tabular by default, 452 KB). Both OFL, both cost more than the entire Anek Latin file, neither has Indic. Later, optional, not part of this decision.

## Numerals
| Face | `tnum` | Tabular by default |
|---|---|---|
| **Anek (all scripts)** | Yes (+`zero`) | No |
| Inter | Yes (+`zero`) | No |
| Plus Jakarta / Figtree / Geist / Manrope | Yes | No |
| **Lexend Deca** | **No** | No |
| **Poppins** | **No** | No |
| Mulish / Hanken Grotesk / Noto Sans Devanagari | No | Yes |
| Newsreader | Yes | Yes |

**Proof it matters (rendered in Flutter):**
```
Anek default:  ₹1,11,111 = 283.0px   ₹9,99,999 = 408.3px   (125px misaligned)
Anek tnum:     ₹1,11,111 = 414.8px   ₹9,99,999 = 414.8px   (aligned)
Inter default: ₹1,11,111 = 362.8px   ₹9,99,999 = 477.6px   (115px misaligned)
Inter tnum:    ₹1,11,111 = 497.7px   ₹9,99,999 = 497.7px   (aligned)
```
**QUICK WIN TODAY:** Inter already ships and already has tnum. Add `fontFeatures: [FontFeature.tabularFigures()]` to money styles → fixes passbook/dues alignment before any migration.
**Do NOT apply globally** (tabular digits look gappy in prose). Add an `isMoney` flag to `AppTextStyles.textStyle()` alongside `isBody`.

**Lakh grouping — `intl: ^0.19.0` is already a dependency and handles it natively:**
```
NumberFormat.decimalPattern('en_IN'):  150000 → 1,50,000 · 12345678 → 1,23,45,678
NumberFormat.currency(locale:'en_IN', symbol:'₹', decimalDigits:0): 150000 → ₹1,50,000
NumberFormat.compactCurrency(locale:'en_IN', symbol:'₹'): 150000 → ₹1.5L · 12345678 → ₹1.23Cr
```
**GOTCHA:** `compactCurrency` + `en_IN` renders 12,500 as **`₹12.5T`** (T = thousand) which reads as trillion. Use `hi_IN` (`₹12.5 हज़ार`, `₹1.5 लाख`) or special-case values under one lakh. Explicit ICU pattern for Indian grouping without switching locale: `'#,##,##0'`.

## Flutter specifics
**Version cliff:** `fontWeight` driving the `wght` axis landed in 3.39.0-0.0.pre, **stable in Flutter 3.41**. Local machine runs **3.44.1** — past the cliff. Verified real weights from one variable file:
```
Anek variable, "Rent due" @100px:
w300→372.59  w400→376.93  w500→380.60  w600→389.03  w700→395.93  w800→402.60
```
**RELEASE FLAG:** package declares `sdk: ">=3.3.3 <4.0.0"` → a consumer on pre-3.41 gets file-selection without axis movement, so every weight renders at the font default. **Anek's default is `wght 500` (Medium), not 400** → the entire app would render in Medium. Either raise the SDK floor or set `fontVariations` explicitly:
```dart
TextStyle(fontFamily: 'Anek', fontVariations: [FontVariation('wght', 600)])
```
(`FontVariation('wdth', 75..125)` confirmed working — produced the 506.9→961.0px range above.)

**pubspec — one asset per family, OMIT `weight:` entirely** (Flutter doesn't infer weight from filenames; `weight:` entries pointing at the same variable file cause wrong matching):
```yaml
flutter:
  fonts:
    - family: Anek
      fonts:
        - asset: lib/fonts/AnekLatin-VF.ttf
    - family: AnekDevanagari      # localised builds only
      fonts:
        - asset: lib/fonts/AnekDevanagari-VF.ttf
```
Then replace the `isBody ? 'Inter' : 'Poppins'` ternary in `lib/viewutils/app_text_styles.dart` with `'Anek'` — one edit propagating to all 125 files using `AppTextStyles`. The 33 `'SF Pro Text'` refs need separate fixing.

**Tree-shaking does NOT help.** `--tree-shake-icons` (on by default) runs `constFinder` for const `IconData` and subsets only matching families (`packages/flutter_tools/lib/src/build_system/targets/icon_tree_shaker.dart`). **Text fonts ship whole, every glyph.** Must pre-subset.

**Subsetting recipe + two traps:**
```bash
pyftsubset AnekLatin[wdth,wght].ttf \
  --unicodes='U+0000-00FF,U+0131,U+0152-0153,U+2000-206F,U+20B9,U+20AC,U+2122,U+2212,U+FEFF,U+FFFD' \
  --layout-features+=tnum,zero,case \
  --output-file=lib/fonts/AnekLatin-VF.ttf
```
1. **`pyftsubset` silently drops `tnum` by default.** Measured 174 KB without vs 179 KB with. The `+=` matters — plain `--layout-features=tnum` REPLACES the set and destroys everything else.
2. **Do NOT pass `--no-hinting`.** Zero size saving (184 KB either way) while losing `prep`-table grayscale hints that matter on low-DPI Android. None of the candidates are TrueType-hinted (no `fpgm`), so all rely on the rasterizer, and `prep`/`gasp` tune it.

Drop an unused axis: `fonttools varLib.instancer AnekLatin[wdth,wght].ttf wdth=100 -o AnekLatin-wght.ttf` → 184 KB to 82 KB. Only if abandoning the width-axis display treatment.

## Licensing — the white-label model eliminates the commercial market
**Every retail foundry prices App licences per application.** Shipping one binary into N client-branded apps with N bundle IDs = N licence units.

| Foundry | Model | Verdict |
|---|---|---|
| **Pangram Pangram** (PP Fragment, PP Cirka) | Per app AND per MAU; EULA §3.7 forbids "sublicensing the Fonts... to any third-party" | **FATAL** — each white-label client is a third party receiving the binary |
| **Fontfabric** (Gilroy, CRED's face) | Per app AND per download ceiling ("1 App (100,000 downloads)") | **Fatal at retail**; app prices unpublished |
| **Ek Type commercial fonts** | One app, **expires after 2 years** | **Worst clause found** — re-licensing treadmill on shipped binaries. *Does NOT apply to Anek or Mukta (both OFL).* |
| **Lineto** (Circular, Stable Money's) | App licence exists, price never published; corporate "tailor-made or unlimited", quote only | Unknown cost, negotiation required |
| **ITF** (Kohinoor) | Standard App licence per app count, **BUT a genuine Corporate Licence: "unlimited usage of fonts in Print, Web and Mobile applications"** | **Best commercial structure** if ever needed. Ask about their Service Licence (closest analogue to an SDK-vendor position). |
| **Displaay** (Reckless Neue) | Per app priced by company headcount, unlimited toggle, iOS+Android of one brand = one Application, perpetual one-time | Friendliest paid structure; still doesn't address multi-client white-label |

**Anek and Inter are both SIL OFL 1.1** (licence files read directly). OFL permits bundling inside redistributed software with no per-app accounting, no fee, no term limit. Obligations: include copyright + licence notice (Flutter's `showLicensePage` satisfies this) and don't use the Reserved Font Name on a modified version. **Subsetting is technically modification** → either rename the family (e.g. `RentOkSans` built from Anek) or keep the family name and leave the original name strings inside the binary untouched, which `pyftsubset` does by default.

**CORRECTION:** the claim that **slice commissioned its own typeface could NOT be verified** by this agent — eight searches across foundry sites, Fonts In Use, Behance and design press found no named custom typeface and no designer credit. (Note: the earlier teardown agent read `Copyright 2019 slice` / designer `slice` directly from the binary's name table, which is stronger evidence than absence-of-web-coverage. Treat as *probable but unconfirmed*; the binary evidence stands, the commissioning story doesn't.)

## RECOMMENDATION: **Anek (Ek Type), SIL OFL 1.1**
1. **Carries brand identity when colour cannot** — an Indian typeface by an Indian foundry with a voice that is neither Silicon Valley default nor generic geometric. Inter/Poppins/Geist/Plus Jakarta all read as "some app"; Anek reads as a decision.
2. **Only candidate that solves Indic properly** — 10 scripts, metric-identical, same axes; a Tamil or Telugu build is a file swap with no reflow.
3. **Ships SMALLER than today** — 184 KB for one file with continuous 100–800 weight + 75–125 width, vs **457 KB today for two fonts with one real weight each. Gain every weight, lose 273 KB.**
4. **Real tabular figures**, proven working in Flutter.
5. **No licence trap** — OFL 1.1, unlimited white-label apps, forever, free.

**Costs:** +12% type-scale bump (0.489 x-height), and 846 KB whenever Hindi is added.

**Ship plan:** now → `AnekLatin-VF.ttf` both axes, Latin + ₹, tnum kept = **184 KB**. Add Hindi → `AnekDevanagari-VF.ttf` (Devanagari AND Latin in one file) = 846 KB. Tamil/Telugu/Kannada = 153/559/415 KB each.
**Do not ship four static weights** — measured 161 KB vs 82 KB for the equivalent variable file, and static gives four weights instead of six.

**Runner-up: Inter** (OFL, 108 KB) if the Indic roadmap dies or migration risk must be near-zero. Best raw legibility, already in codebase, equally clean licence. Accept that it looks like every other app and Hindi is always a compromise.

**There is no budget scenario** — recommendation and runner-up are both OFL and free. **Money buys a WORSE outcome here** because every commercial foundry charges per app and this SDK ships into many apps. If spending ever makes sense: negotiated **ITF Corporate Licence for Kohinoor** (only paid family with all-India coverage + a real unlimited tier) or a **commissioned face from Ek Type** (they commission; no published rates; info@ektype.in).

## DO THIS WEEK regardless of the font decision
1. Add `FontFeature.tabularFigures()` to money text styles — Inter already supports it, fixes passbook/dues alignment immediately.
2. Fix the 33 `fontFamily: 'SF Pro Text'` refs in `lib/myservice/` — undeclared, silently falling back to Roboto on Android.
3. Decide the Flutter SDK floor — below 3.41 every variable weight renders at the font default (Medium for Anek).