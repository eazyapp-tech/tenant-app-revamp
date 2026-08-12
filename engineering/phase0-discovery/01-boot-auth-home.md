# Phase 0 Inventory — Boot, Splash, Auth, Base, Home Page
**Package:** `/Users/eazypg/rentok_tenant_package`
**Scope:** boot init + routing constants, splash/intro, auth flow, base shell + bottom nav, home page and every section/widget under it.

---

## 0. BOOT LAYER

### 0.1 `RentOkWidget` (root package entry)
**File:** `lib/rentok_tenant_package.dart`

1. **Name:** `RentOkWidget` / `_RentOkWidgetState` — the whole package's `MaterialApp` root.
2. **What it does:** Boots the tenant app: prefs, package info, connectivity check, white-label theme fetch, Firebase, FCM, Crashlytics, then decides the first screen.
3. **Entry points:** Constructed by the host app (`net.eazypg.eazypgtenant.*` shells). Params: `name`, `packageAndroid`, `packageIos`, `overrideSplashPage` (default `true`).
4. **Exit points:** `FutureBuilder<int>` switch on `init()` result:
   - `pageHome = 2` → `BasePageBinder()`
   - `pageAuth = 0` → `PhoneNumberValidationWidget()`
   - `pageEvicted = 1` → `EvictedPage()`
   - `pageForceUpdate = 3` → `AppUpdatePage(isForceUpdate: true)`
   - `pageWaiting = 4` → `PGJoinRequestPendingWidget()`
   - `pageOleSplash = 5` → `OleStaysSplashPage()`
   - `pageNoNetwork = 6` → `NoNetworkPage(onRetry: _restartBootstrap)`
   - **default fallback** → an unstyled "Something is not right!" `Column` with Try Again / Logout buttons.
5. **Data dependencies:**
   - `ProfileRepository().getWhiteLabelAppConfig(packageName)` → `GET /others/whitelabel-user` (`ApiConst.getAppConfig`). Cached in `PreferenceKeys.whiteLabelConfig` as JSON.
   - `PackageInfo.fromPlatform()`, `Connectivity().checkConnectivity()`
   - Registers 21 `ChangeNotifierProvider`s at the root.
6. **Feature gates / conditionals:**
   - `PrefsUtils.getBool(pGRequestWaitingApproval)` → waiting page (checked FIRST, before `isLoggedIn`)
   - `PrefsUtils.getBool(isLoggedIn)` → home
   - `Constants.appPackageName == 'net.eazypg.eazypgtenant.olestays' && widget.overrideSplashPage` → Ole splash
   - `pageForceUpdate` is a declared constant but **never returned by `init()`** — dead branch at boot; force-update only reachable via `BasePage.showDismissibleDialog`.
   - White-label cache: if cached JSON exists → apply instantly + background refresh (10s timeout); else block-fetch with 15s timeout, fall through to defaults on failure.
   - `navigationMenu` global is only replaced when `navs.length > 2` (a 1- or 2-item menu from backend is silently ignored).
7. **UI inventory:** Full-screen `PlatformProgressIndicator` on `ConnectionState.waiting` (white bg), same again as `hasData == false` fallback. No shimmer, no error sheet.
8. **Visual notes:**
   - `Container(color: Colors.white)` hardcoded for the two loading states.
   - The "Something is not right!" fallback uses bare `Text` with no `AppTextStyles`, no padding, no centering. Visually broken.
   - `ScreenUtilInit` `designSize` is set to the **device's own size** → `.w/.h/.sp` effectively 1:1 — all ScreenUtil scaling is a no-op.

**Root provider list (order as registered):** `AuthProvider`, `HomeProvider`, `AccountsProvider`, `OffersProvider`, `ProfileProvider`, `CashPaymentProvider`, `FoodProvider` (lazy), `ComplaintsProvider`, `CommonProvider`, `AnnouncementProvider`, `PendingTaskProvider`, `UpiAppsProvider`, `SpinProvider`, `RentPassProvider`, `AttendanceProvider`, `WidgetHeightProvider`, `PaymentPageProvider`, `EvictionProvider`, **`PendingTaskProvider` (registered a SECOND time)**, `AddComplaintProvider`, `OverviewProvider`.
> Bug: `PendingTaskProvider` is registered twice (lines 127 and 138). Home Pending Tasks widget and eviction flows may talk to different instances.

### 0.2 `changeTheme()` — white-label application
**File:** same file, lines 372–400.
Maps `WhiteLabelUser` → global mutable statics:
`AppColor.primaryColor`, `AppColor.secondary`, `AppColor.backgroundColor`, `AppColor.textColor`, `Assets.appIcons` (logo, may be a URL), `Constants.introText`, `Constants.propertyWebPage`, `Constants.appPackageName`, `Constants.appStoreID`, `Constants.appName`, `Constants.eazyPGOfficialWhatsAppSupport`, `Constants.privacyPolicyLink`, `Constants.tncLink`.
> **Mismatch: `changeTheme` writes `AppColor.primaryColor` / `AppColor.secondary`, but ~90% of the UI reads `AppColor.appPrimaryColor` / `AppColor.secondaryColor`. White-label primary colour largely does not reach the UI.** Biggest theming finding in this slice.

**`WhiteLabelUser` fields (backend contract, frozen):** `id, appName, pgId, brandName, packageName, primaryColor, secondaryColor, textColor, backgroundColor, logo, playStoreLink, appStoreLink, websiteLink, inviteLink, shortLinkName, navigationMenu[], splashScreenMedia, showCashback, style, introText, appSupportNumber, privacyPolicyUrl, tncUrl`.
> Unused by the app today: `brandName`, `playStoreLink`, `inviteLink`, `shortLinkName`, **`splashScreenMedia`**, `showCashback`, `style`. `splashScreenMedia` is especially notable — backend can already serve a splash asset and the app ignores it.

**`NavigationMenuItem` fields:** `name, key, icon, deeplinkUrl`. Only `name` and `key` consumed; `icon` (URL/name from backend) and `deeplinkUrl` are **read into the model and never used** — icons are hardcoded Material icons in `BottomNavigationProvider`.

---

## 1. SPLASH / INTRO SCREENS

### 1.1 `OleStaysSplashPage` — `lib/viewutils/ole_splash_page.dart`
Brand landing for the OleStays white-label — hero image, tagline, two CTAs. Only reachable when package == `net.eazypg.eazypgtenant.olestays`, logged out. Fully static, heavily hardcoded (raw asset path string, `Color(0xFFFFBB05)`, `Color(0xFF143D59)`, raw font sizes 36/22/16, `bottom: 250` magic number, hardcoded English copy not `Constants.introText`).

### 1.2 `OnBoardingCarouselWidget` — **DEAD CODE**
**File:** `lib/presentation/auth/widgets/onboarding_carousel_widget.dart`
4-page `IntroductionScreen` carousel: `#LiveSmart`, `#EazyPay`, `#CashBacks`, `#HappyLiving`. **Entry points: NONE** (only ref is commented out in `routes.dart:58`). Assets `app_intro_one..four.webp` exist in `lib/assets/auth/`. Uses legacy `AppTheme.primaryColor`.

### 1.3 Other splash assets present but unused
- `lib/assets/anim_splash_logo.json` (Lottie) — no reference in auth/boot path.
- `lib/assets/icons/ic_splash_logo.png` — native splash asset.
> **No RentOk-branded animated splash inside Flutter.** First frame after native splash is a bare white screen + spinner.

---

## 2. AUTH FLOW

### 2.1 `PhoneNumberValidationWidget` — `lib/presentation/auth/widgets/phone_number_validation_widget.dart`
Login entry — logo, tagline, country-code + 10-digit phone entry, WhatsApp opt-in, T&C consent, Continue.
- **Entry points:** boot (`pageAuth`); OleStays splash; EvictedPage re-login; BasePage/Home error-widget logout; SelfInviteWidget "edit phone"; OTP "Change"; PGJoinRequestPendingWidget cancel; forceLogout.
- **Exit:** `sendOTP` success → `OTPVerificationWidget`. External: `Constants.propertyWebPage` (Android only), WhatsApp support, tnc/privacy links.
- **Data:** local `AuthProvider` (nested provider, NOT the root one) → `POST tenant/sendLoginOtp` `{phone, country_code}`.
- **Gates:** `!Platform.isIOS` hides "Looking for a Property" (App Store policy); white-label overridable copy/links; `isWhatsAppNotificationOn` defaults true.
- **UI:** loader dialog "Sending OTP"; toasts (invalid phone, server message); dead-path SnackBar; CountryCodePicker modal `0.9.sw × 0.65.sh`. No shimmer/empty/inline errors.
- **Visual:** mixes `AppColor.appPrimaryColor` AND legacy `AppTheme.primaryColor`; raw `Colors.grey.shade300` border; **zero `AppTextStyles`**; `Transform.translate` checkbox hack; hardcoded 10-digit validation regardless of country code.

### 2.2 `OTPVerificationWidget` — `lib/presentation/auth/widgets/otp_verification_widget.dart`
6-digit OTP entry, 31-second resend countdown.
- **Data:** `verifyOTP` → `POST tenant/tenantLoginSignup` `{phone, country_code, otp}`.
- **UI:** three stacked loader dialogs ("Verifying OTP" → "Signing in.." → "Fetching profile.."); SnackBars incl. raw `e.toString()`; auto-submit on `Pinput.onCompleted` AND manual button → double-submit possible. No SMS auto-read.
- **Visual:** raw TextStyles; `Icons.dialpad` in `withOpacity(0.15)` circle as hero — placeholder-grade; `sub!.cancel()` dispose crash risk.

### 2.3 `OTPInput` — `lib/presentation/auth/helper_widgets/otp_input.dart`
`PinTheme(width: 120, height: 60)` — 6×120px overflow risk. Hardcoded RGB colors, none from AppColor. No error/submitted theme.

### 2.4 `MultiAccountsWidget` ("Choose Property" sheet) + `AccountCard` — `lib/presentation/auth/widgets/choose_account.dart`
Multi-tenancy property picker at login. Entry: `verifyOTP` when `authResponse.property != null`. Exit: `getTenantCustomToken` → BasePage/SelfInvite/Evicted. Embeds `JoinAnotherPropertyTile`.
- Status: `1 = Active`, `2 = Booking`, else `Evicted`.
- **UI:** SearchWidget (client-side filter), PaginatedListView, empty state, toast. Sheet fixed 0.7 screen height.
- **Visual:** raw pixels everywhere (no `.w/.h/.sp`); Material palette pills (`Colors.blue[50]` etc.); amber-on-amber contrast fail; `TextEditingController` created in `build()`.

### 2.5 `SelfInviteWidget` (App ID entry) — `lib/presentation/auth/joining/self_invite_widget.dart`
Tenant enters property App ID / invite code.
- **Entry:** `verifyOTP` status 202 (both branches); `openJoinPropertyFlow` with `isAddingProperty: true`.
- **Exit:** `checkPgId` → `PGJoinRequestWidget`; help; property search web/WhatsApp bot `8851791188`; invite property.
- **Data:** `POST rooms/fetchRoomNames` `{eazypg_id}`; then `GET property/rooms?pg_id&pg_number`.
- **Gates:** `isAddingProperty`; `existingPgIds` blocks re-join; **`Constants.appName == 'Smart Tenant App'` gates the "Invite Property" block — white-labels never see it**; `propertyWebPage.isEmpty` → WhatsApp bot fallback.
- **UI:** auto-opened 3-page intro bottom sheet (third page CTA is a **no-op**); App-ID help sheet; toast; loader dialog; SnackBar on bad ID.
- **Visual:** most design-system-aligned auth screen (AppTextStyles consistent) BUT hardcodes a Tailwind-slate palette (`0xFFF1F5F9`, `0xFF45556C`, `0xFF101828`); CTA uses `appYellow` vs everywhere-else `appPrimaryColor`; `'+91 ${phoneNumber}'` hardcoded ignoring countryCode; SystemChrome overlay mode never restored.

### 2.6 `PGJoinRequestWidget` — `lib/presentation/auth/joining/pg_join_request_widget.dart`
Collects name, room/unit, rent, deposit, joining date → join request.
- **Data:** `POST tenant/updateTenantInvitation` `{pg_id, pg_number, name, room_no, unit_ids[], rent_amount, date_of_joining, phone, invite_id}` → `inviteId` stored.
- **Gates:** `rooms.multipleRoomPropertyStructure` (0 = flat list; else nested room→unit); `isAddingProperty`; **`security_deposit` collected but never sent** (dead field); `requestType: 101` passed but not forwarded.
- **UI:** stock Material date picker (1800–2050); toasts; loader; validator passed but no `Form` → never runs.
- **Visual:** AppTextStyles + same Tailwind-slate hardcodes; local `CustomTextField` shadows two other classes of the same name; force-unwrap crash risks on date picker dismissal.

### 2.7 `PropertyRoom` + `RoomCard` + `BedItem` — `lib/presentation/auth/joining/select_unit.dart` etc.
Room/bed selection. Filters `rentDisable` rooms but still renders disabled tint branch (unreachable); radio flow vs expandable-card flow by structure flag; shimmer + 2 empty states.
- **Visual:** `Theme.of(context).textTheme` used (only place in slice); `BedItem` renders same icon for every type and forces greyDark; Android bottom-margin fudge factor; big commented-out blocks.

### 2.8 `PGJoinRequestPendingWidget` — `lib/presentation/auth/joining/pg_join_request_pending_widget.dart`
Approval-pending holding screen; manual poll, re-request, cancel.
- **Data:** `POST tenant/checkInvitationStreaming`; `POST tenant/deleteTenantInvitation`; `POST property/notifyOwnerForSelfInvite`; `tenantAuthenticate`; `POST tenant/getTenantAppStatus`.
- **UI:** 3 loader dialogs; 7 toasts; SnackBar; illustration; info banner. No auto-polling. Loader-dialog leak on refresh-success path.
- **Visual:** good AppTextStyles; hardcoded `0xFFE5E7EB`/`0xFFF9FAFB`; double bottom padding; abandoned go_router comment.

### 2.9 `JoinAnotherPropertyTile` + `openJoinPropertyFlow`
`openJoinPropertyFlow` **snapshots and restores 10 pref keys** (+`isLoggedIn`, `pGRequestWaitingApproval`) around the join flow because it writes session prefs as a side effect. Load-bearing workaround for global-prefs auth design.

### 2.10 `AuthProvider` — routing brain — `lib/application/auth_provider.dart` (657 lines)

Post-OTP decision tree (`verifyOTP`):
```
POST tenant/tenantLoginSignup
 ├─ status >= 400 → SnackBar(message)
 └─ status < 400
     ├─ property != null → "Choose Property" sheet
     │    └─ onItemClick → getTenantCustomToken → save jwtToken → signInWithCustomToken
     │         └─ switch status: 200/201 → tenantAuthenticate → setPrefs → getTenantAppStatus
     │              ├─ !isEvicted → isLoggedIn=true → BasePageBinder
     │              └─ else → clearAll → EvictedPage
     │            202 → write pgId/pgName/pgNumber → SelfInviteWidget
     └─ property == null → same switch
```
> 200 (`authOnBoard2`) and 201 (`authLogIn2`) are fallthrough — **backend's onboard vs login distinction is not honoured in UI.**

**Prefs written by `setPrefs`:** `phoneNumber, tenantId, tenantName, parentName, tenantRoom, pgName, pgId, eazyPGID, pgNumber, tenantUUID, propertyId` (+ `jwtToken` separately).

Dead provider state: documents, tenant demographic fields, signature/agreement fields — leftovers of a removed onboarding wizard. `OnboardingDocumentCard` has no call sites.

**Auth API surface (frozen):**
| Purpose | Endpoint |
|---|---|
| Send OTP | `POST tenant/sendLoginOtp` |
| Verify OTP / login | `POST tenant/tenantLoginSignup` |
| Multi-property token exchange | `POST getTenantCustomToken` |
| Register device/session | `POST tenantAuthenticate` |
| Resolve App ID → property | `POST rooms/fetchRoomNames` |
| Room/unit tree | `GET property/rooms` |
| File join request | `POST tenant/updateTenantInvitation` |
| Cancel join request | `POST tenant/deleteTenantInvitation` |
| Nudge owner | `POST property/notifyOwnerForSelfInvite` |
| Poll approval | `POST tenant/checkInvitationStreaming` |
| Refresh JWT | `GET tenant/refreshToken` |
| App status / eviction | `POST tenant/getTenantAppStatus` |
| White-label config | `GET /others/whitelabel-user` |

### 2.11 Auth helper widgets
| Widget | Status |
|---|---|
| `OTPInput` | Live |
| `PhoneInput` | **Dead** |
| `CustomTextField` (helper_widgets) | **Dead** |
| `OnboardingDocumentCard` | **Dead** |

### 2.12 Boot-adjacent pages
- **`EvictedPage`** — terminal; `WillPopScope` clears prefs and kills app. **Doubles as generic auth-failure page** — any non-2xx from `getTenantAppStatus` shows "you may have been evicted" for ordinary network errors.
- **`NoNetworkPage`** — decent; button color hardcoded `AppColor.black`.
- **`AppUpdatePage`** — force/soft variants; effectively dead (caller has no call sites).
- **`ParentContainer`** — shared page chrome (47 usages).
- **`EazyLogo`** — renders `Assets.appIcons`, CachedNetworkImage if URL. No loading placeholder.

---

## 3. BASE / SHELL

### 3.1 `BasePageBinder` / `BasePage` — `lib/presentation/base/basepage.dart`
Hosts bottom nav + `IndexedStack`; refreshes JWT; enforces compulsory KYC; server-driven home notification sheet.
- **Data:** `RefreshTokenProvider` (15s timeout, exception → forceLogout); `POST tenant/checkTenantCompulsoryKYC`; `POST tenant/getTenantAppStatus`.
- **Gates:** KYC status 201 + kycUrl → **non-dismissible** KYC modal (`isLateFine`, `gracePeriod` default 3); on resume only KYC recheck; `isEvicted` → EvictedPage; `uiData != null` → `HomeNotification` sheet (`isDismissible`, `bottomSheetTitle`).
- Back behavior: non-home tab → tab 0; tab 0 → exit app.
- **Visual:** zero-height AppBar to tint status bar; nav bar hardcoded `Colors.white`; **icon semantics inverted** (icon=filled, filledIcon=outlined, rendered backwards); selected-tab pill overflows at 5+ tabs; `parseUri` has no call sites in file (deep-link routing broken/elsewhere); `"checkattendance"` case missing break.

### 3.2 `BottomNavigationProvider` — `lib/application/bottom_navigation_provider.dart`
Key→page map: `home`→Home, `accounts`→AccountsPageV2, `services`→ServiceOverviewPage2, `profile`→ProfilePageV2, `tickets`→ComplaintsPage, `attendance`→TenantAttendanceHistory, `offers`→OffersPageV2, `food`→FoodMenu. Unknown keys silently dropped. Fallback menu (≤2 items): Home/Account/Tickets/Profile.
> `getNavigationMenu()` **rebuilds the entire page list on every call**, called 2×/build → new page instances each rebuild, defeating IndexedStack state preservation. `item.icon`/`deeplinkUrl` ignored.

### 3.3 `RefreshTokenProvider`
Fires in constructor. **Any thrown exception (incl. timeout) → `forceLogout()`** — a timeout silently logs the tenant out.

---

## 4. HOME PAGE

### 4.1 `Home` — `lib/presentation/homepage/home.dart` (604 lines)
Dashboard: greeting header, stories/notifications bell, ~11 sections.
- **refreshStates() fans out to 7 providers:** HomeProvider (passbook), AccountsProvider, OffersProvider, ProfileProvider (+SD), ComplaintsProvider, AnnouncementProvider, AttendanceProvider. Plus 2 page-local: MarketingProvider (`POST tenant/fetchTenantHomePage`), FoodMenuProvider (`POST property/fetchFoodData` + `GET tenant/{uuid}/fetchFoodAttendance`).
- **Gates:** `Constants.appName != "Orchid Parc"` hides HomeMenuSection (**hardcoded client name**); two **hardcoded Firebase pgIDs** get "# Feels Like Home" watermark; `isVerified` → green avatar ring; `isParentApp` → parent greeting; error page only when BOTH Profile AND Home providers error.
- **Startup interstitial chain (post-frame, once):** attendanceSetup → smart-attendance dialog/setup-block/mark-sheet → fetchFoodAttendance → `isMealLive==1` → FoodAttendanceBottom; `showFoodConfirmationBottomsheet==1` → FoodConfirmationBottom. SetupAttendancePage pushed with no back button — hard block.
- **UI:** RefreshIndicator; EazyErrorWidget; SnackBar; 4 interstitial sheets; floating WhatsApp Help button (overlaps last section, no SafeArea).
- **Visual:** 20.h dead app-bar space; hardcoded shadow; watermark style override; dead `pageController` field; bell inconsistent with stories ring; avatar without placeholder.

### 4.2 SECTION ORDERING — **no ordering engine; hardcoded Column literal (lines 379–433). Backend levers: 7 customization booleans + upper/lower marketing slots + list emptiness. Nothing server-ordered.**

| # | Widget | Renders when |
|---|---|---|
| 1 | HomeAnnouncementSection | announcements > 0 |
| 2 | HomeMyAccountSection | passbook loading/success |
| 3 | HomePendingTasksWidget | tasks non-empty (**never fetched from home — always empty on cold load**) |
| 4 | HomeElectricityCard | provider not loading/error |
| 5 | HomeMyComplaintsSection | customization.complaints && complaints exist |
| 6 | MarketingList(MAJOR) | upper.cardArray non-empty |
| 7 | HomeLifeInPgSection | any customization flag true |
| 8 | HomeMenuSection | appName != "Orchid Parc" && food success |
| 9 | HomeYourProfileSection | profile success |
| 10 | HomeRewardCardsSection | unscratched credits > 0 |
| 11 | HomeOfferSection | offers success && rewards > 0 |
| 12 | MarketingList(MINOR) | lower.cardArray non-empty |
| 13 | Footer watermark | home success (pgID allowlist decides copy) |

**Duplicate network calls per home load:** `fetchTenantHomePage` ×2–3 (MarketingProvider instantiated 3×), `tenantComplaints` ×2 (ComplaintsProvider 2× — pull-to-refresh updates the WRONG instance), `fetchFoodAttendance` ×2, passbook from both HomeProvider and AccountsProvider.

### 4.3–4.16 Section detail highlights
- **HomeAnnouncementSection:** shimmer is `height: 0` (invisible); fixed `260.w` text width; only announcement[0] reachable from card.
- **AnnouncementProvider:** no-op for loop; wrong generic (`OffersModelV2`); loading state never notifies → shimmer unreachable.
- **HomeMyAccountSection / HomeAccountFactory:** business logic in presentation layer. Credits exclude `{Used, Unusable, EXPIRED}`, "Security Deposit", status 102. Card rules by totalDues; up to 3 receipt cards; "No Current Dues ☺️" title. All cards forced `secondaryColor`; ListView horizontal padding uses `.h`; cards are `ElevatedButton`s; force-unwraps.
- **HomePendingTasksWidget:** eviction taps only work when `oldEviction` pref; CachedNetworkImage placeholder is `Icon(Icons.error)`; up-arrow asset as right-chevron.
- **HomeElectricityCard:** provider retries 3× w/ 2s delay for propertyId; **"No electricity data available" EazyCard renders for every property without a meter** (null not filtered); raw asset path; `Icons.bolt` yellow.
- **HomeMyComplaintsSection** (lives in `lib/complaints/widgets/home_complaint_card.dart`): local Complaints+Marketing provider instances; `complaintDisabled` naming inverted; bot card gated `isComplaintBotActive == 1`; caps 3 + View All; hardcoded hexes; 250.h vs 300.h mismatch; dead branch.
- **MarketingList:** `startScrolling` called in `build()` → **Timer leak, carousel accelerates**; controller re-created per build; page index overrun bug; force-unwraps (empty `params` crashes on tap); MINOR has no loading state.
- **HomeLifeInPgSection:** card gates = customization flags (complaints/attendance/foodAttendance/hostFriends/checkInLate/sendNotice); **`markLeave` flag exists in model, no UI**; card color props ignored by card widget (dead palette); `\n` in subtitles; `sendEvictionNotice()` top-level dead function.
- **HomeMenuSection/Card:** most recently redesigned, worst hardcoding — raw `fontFamily: 'Poppins'/'Inter'`, fractional Figma sizes (10.5/12.3.sp), `borderRadius.circular(16777215)`, wrong line-height ratio (17.5/9.4), icons stretched as 300×200 backgrounds, unguarded `menu[weekday-1]` index crash risk. Live badge match: case-insensitive string compare of foodClass.title vs mealName.
- **HomeYourProfileSection:** **bug — `isComplete: profileModel.profileIncomplete` used un-inverted** (incomplete profile shows "Completed"); 5 cards always render; card color props ignored; ~35-line commented duplicate.
- **HomeRewardCardsSection:** height conflict 290/200/230.h → guaranteed overflow; card color `appFailureRed` (error red for rewards); copy shows MINIMUM amount labeled "upto"; intended card component never used.
- **HomeOfferSection:** 1,100-line `RPSCustomPainter` band w/ magic ratio 0.8780889621087314 vs fixed 340.h child; server hex colors w/o contrast validation; text color chosen by **string sniffing** (`contains('Black')`); "₹10,000/Yr" hardcoded; share-via-screenshot.
- **StoryDashWidget:** 0s AnimationController when no stories; unused title param; image larger than container.
- **HomeNotification:** server-driven sheet; **only `buttonIntent == "web"` does anything**; 3+ buttons squeeze; NeverScrollableScrollPhysics overflow risk; title/body same size (no hierarchy).
- **Dead:** FailureWidget, MarkLeaveItem, HomeComplaintsRegisterCard, HomeSpinTheWheelSection (commented out).

---

## 5. CROSS-CUTTING FINDINGS

**Design-system adherence:**
- Best: SelfInviteWidget, PGJoinRequestWidget, PGJoinRequestPendingWidget, HomePendingTasksWidget, HomeLifeInPgSection.
- Mixed: base page, most home sections.
- Worst: OleStaysSplashPage, PhoneNumberValidationWidget, OTPVerificationWidget, OTPInput, MultiAccountsWidget, HomeMenuSectionCard, HomeElectricityCard.

**Two competing colour systems:** `AppColor.*` and legacy `AppTheme.*` — both in same auth files.
**Three competing `CustomTextField` classes.**
**Abandoned go_router migration** — commented calls in ~6 files; all live nav is imperative.
**Toast/feedback fragmentation:** Fluttertoast, `showToast()`, SnackBar, showLoaderDialog; raw `e.toString()` shown to tenants ≥5 places in auth_provider.
**Global mutable state:** `navigationMenu` global var, `AppColor.*`, `Constants.*`, `Assets.appIcons` — mutated at boot, no rebuild signal beyond one setState.
