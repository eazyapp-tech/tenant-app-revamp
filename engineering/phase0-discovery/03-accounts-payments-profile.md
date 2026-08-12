# Phase 0 — Accounts/Payments + Profile Inventory

## 0. Global constraints
- All slice providers are ROOT singletons (`rentok_tenant_package.dart:114-136`): AccountsProvider, ProfileProvider, CashPaymentProvider, UpiAppsProvider, **PaymentPageProvider (not sheet-scoped — reset via setBasicInfo() per open; two sheets in one session mutate shared state)**. UpiAppsProvider fetches UPI apps at app boot; ProfileProvider fetches profile + SD in constructor.
- Sheet helpers (eazy_utils.dart): showFlatBottomModal (square, pay-now), showRoundBottomModal (20px radius), openBottomSheet (titled).
- **Shared loader dialog** (`accounts/widgets/loading_dialog.dart`): Lottie splash logo, barrierDismissible false, no route name, no auto-dismiss — every caller must pop manually → the "stuck dialog" bug class.

### Endpoint map (slice)
passbook `tenant/getTenantPassbookForTenantApp` · checkout `tenant/getPaymentCheckoutPage` · pay-link `payment/generatePaymentPageLink` · credits fetch/validate/scratch/unscratched `credits/*` · CF token `payment/getCashfreeToken` · verify `payment/verifyPayment` · confirm by order `payment/confirmPaymentByOrderId` · record `payment/addPayment` / `payment/addPaymentAgainstInvoice` · RentPass `tenantMembership/addMembershipForTenantWithPayment` · cash staff `teamMember/fetchTeamMembersForCashCollection` · cash OTP `payment/sendCashOtp`/`verifyCashOtp` · receipt `invoices/generateReceipt` · unpaid `invoices/unpaid-receipt` · SD `tenant/fetchTenantDeposit` · profile r/w `tenant/fetchTenantDetailsByKey` / `editTenantDetailsByTenant` · notice `tenant/sendNotice` · switcher `GET tenant/properties` · erasure `tenant/deleteUserDataRequest` · handover OTP `tenant/{uuid}/send-otp-for-eviction-handover`.

# PART A — ACCOUNTS

## A1 `AccountsPageV2` — tabbed shell (Cashback/Dues/Expense; default tab 1 = Dues)
Entries: bottom nav, basepage:287, transaction_records_widget:100, GiveNoticeSheet:477 "View Breakup". `hideCashback` param declared, never used. TabController(3) hardcoded; `showCashback` whitelabel flag not consulted. Custom 110.h pill TabBar with per-tab amounts (3 hardcoded semantic colors). Raw Colors.black.withOpacity(.04) shadow, radii 24/32 magic.

## A2 `AccountsCashback` (tab 0)
Balance (Countup), expiry nudge, scratch cards (ScratchViewWidget dialog, barrier .8 non-dismissible), FlipCard owner discounts, redeemed/expired. Data: passbookV2 + unscratched credits. **Filter chain (`otherDescription != Used/Unusable/EXPIRED`, `!= "Security Deposit"`) duplicated 4× inline; owner-discount itemCount vs itemBuilder use DIFFERENT chains → index desync possible.** Shimmer ×3, EazyErrorWidget, RefreshIndicator. **No empty state.** 3 different date formats on one screen.

## A3 `AccountsDues` (tab 1)
Dues list + sticky "pay all" bar (paymentKey = every firebaseId→amount, dateDue = LAST due's date). Gates: `isPartialPayment` (also mirrored into SessionManager), `upiIntent` string = gateway selector for whole chain, AutopaySetupBanner (autopayStatus == 2). Shimmer ×5, empty state with broken copy ("Pay your dues in advance and hefty cashback and rewards"), sticky CTA bypasses AppTextStyles entirely. Banner duplicated in both branches.

## A4 `AutopaySetupBanner`
Renders only when autopayStatus == 2. "Setup Now" → launchUrl(autopayUrl) external. `onSetupNow` callback ignored — debug SnackBar 'Setup Now button pressed!' can never fire. 100% raw Material palette (Colors.orange.shade50-700).

## A5 `AccountsDuesCard`
Tap → DuesDetails; Pay Now → PayNowSheetWidget (singular, invoiceId). Gates: isAutopayScheduled chip; isPartialPayment inline button. Title: dueType=='Rent' → "Mon YYYY Rent".

## A6 `DuesDetails`
Hero amount card (gradient), status banner (Overdue/Due today/Due in N), payment info, Download Invoice (`invoices/unpaid-receipt`), description, attachments (MediaViewerWidget), floating Pay CTA. **Bug: loader dialog never popped on error branch — user stuck.** Dead `getPdf()` with `pdfUrl!` force-unwrap.

## A7 `AccountsExpense` (tab 2) + card
Paid history. Card tap → PaymentSuccessfulWidgetV2 (success screen doubles as receipt-detail). Receipt: receiptUrl → PDF direct; else generateReceipt via loader; empty keys → toast. Analytics typo `Accounts_DownloadReciept` shipped. Amount color appPrimaryColor here vs appFailureRed on dues (inconsistent semantics).

## A8 PAY-NOW FLOW END TO END

### Gateway decision
`upiIntent` (from passbook: "cashfree"|"paytm_upi_intent"|"none") → PaymentPageProvider.upiIntent → set as livePaymentGateway when a UPI tile is tapped. `paymentArray[]` from getPaymentCheckoutPage; "PaymentLink" items stripped client-side; mode=="Cash" flips isCashMode.

**`MakePaymentFactory2` routing: ALL eight non-cash constants (cashfree, cashfree_collect, cashfree_other, paytm, paytm_upi_intent, paytm_collect, payu, payu_collect) funnel into `CashfreeCheckout`. There is NO Razorpay and NO live PayU/Paytm SDK.** Credit-only (201) and Cash (202, after OTP) go straight to PaymentSuccess. Dead Paytm remnants in PaymentRepository (Env.paytmMerchantId, WEBSTAGING).

### Sheet chain
Launch surfaces: home account card ×3 paths (incl. GetPaymentSheetWidget amount entry for advance), offer sheet, dues tab pay-all, dues card singular, DuesDetails CTA.
`PayNowSheetWidget` (flat modal) → ALL UI in `PayNowHeading`: header row → RentPassSelector (isRentPassOnly) → RentPass cashback row + EDIT → "I am paying" + Edit Amount (EditAmountSheet) → credit-state-dependent body: compact = UpiWidget + PayWithOther; expanded = PayWithCashWidget (isCashMode) + OtherPaymentModesWidget + "Share link on WhatsApp" (AlertDialog warning if RentPass plan selected).
`PayNowSizeProvider` = 1 bool isFullWindow. Expanded mode = **bottom sheet cosplaying as a page** (fake app bar in a Stack; no route pushed; system back closes everything).

### Nodes
- **GetPaymentSheetWidget:** advance amount entry; validates non-empty/≠"0"; mixes AppTheme + AppColor in 134 lines.
- **EditAmountSheet:** `>original` guard unless advance; **crashes on empty input (double.parse(''))**; imports pinput unused; triggers full checkout re-fetch.
- **UpiWidget:** CFUPIUtils().getUPIApps(); PhonePe/Paytm/GPay hardcoded by lowercase displayName match ×3 blocks; O(2n) nested ListViews returning Container() for non-matches; base64 icons decoded every rebuild; Android-only "Show all apps"; **onDone passed only for the 3 hardcoded apps**; no empty/error state.
- **OtherPaymentModesWidget:** rows w/ saving line; only success state handled.
- **RentPassSelector:** plan PageView, benefits screen = server-rendered images list; `.data!.data`, `.pro!.benefits!` no guard.
- **UpiCollectInputSheet: DEAD** → `*_collect` paths unreachable from UI.

### Cash-with-OTP
CashPaymentPage → staff dropdown (**value = name+designation string concat — breaks on duplicates**; empty list = empty dropdown no message; failed call = permanent spinner) → Send OTP **navigates without awaiting** → CashPaymentOTPWidget (61s countdown but **startTimer() never called in initState — resend live immediately**; provider owns navigation = double-pop risk; wrong-length toast "Wrong OTP entered"). CashPaymentProvider also carries unrelated eviction-handover OTP pair.

### Execution
**CashfreeCheckout = factory singleton** with mutable state — overlapping payments corrupt each other; pollingDone never reset. orderId = epoch millis. `CFEnvironment.PRODUCTION` hardcoded. Web checkout theme hex-hardcoded #1672EC. verifyOrderId retries once with no delay (payment path).
**PaymentSuccess:** endpoint choice (RentPass / addPayment / addPaymentAgainstInvoice); **always returns success state regardless of HTTP status.**
**PayNowResponseHandler:** switch on paymentState — pending/fail → PaymentFailureWidgetV2; cancelled → toast; error → toast `response.error!`; success+status≥400 → toast; success → refresh Home+Accounts+RentPass, popUntil(isFirst), PaymentSuccessfulWidgetV2 or RenPassSuccessBridge; **null → silent dead end, loader stays up**.
**Bugs:** showFailure does `int.parse(orderId ?? '')` — throws for cash/credit-only (orderId ""); success path `paymentKeys?.add(paymentRes!.paymentKeys![0])` outside its init guard.
**RenPassSuccessBridge:** full-screen Pro/Elite celebration, ConfirmationSlider, → SpinTheWheelPage if spinStatus==4. All colors inline.

### PaymentPageProvider (553 lines)
20+ loose public mutable fields; setBasicInfo force-unwraps 8 params; ~35-line block duplicated verbatim in Cash/non-Cash branches; `_creditResponse.responseState` doubles as page loading state; 8 credit-validation status codes → toast copy IN the provider; **arithmetic on `iAmPayingText` strings via parse/toString — drift-prone.**

## A9 `PaymentSuccessfulWidgetV2` (698 lines, 31 imports)
Success screen + receipt viewer + rewards rail + rating prompt in one file. Gates: showTopNudge, isRentPassInDue, offerButton, refunds, unscratched credits, hasShownRatingPopup (in_app_review once). Exits: PDF receipt, OffersPageV2, ScratchViewWidget, AppRatingBottom, WhatsApp share. **First thing a redesign should split.**

## A10 `PaymentFailureWidgetV2` (518 lines)
**Placeholder copy shipped: 'June Rent' (line 214) + 'test description by example example…' (line 222). Invalid color literal `Color(0x446464339)` (9 hex digits) ×2.** Stringly-typed args ('isUPI':'true'). "Payment received via to EazyApp Tech Pvt. Ltd." grammar error. Raise Issue → prefilled WhatsApp.

## A11 `ScratchViewWidget`
Scratcher dialog → nested second dialog with confetti Lottie whose onLoaded does the API work, pops after hardcoded 3000ms.

## A12 Dead code
CreditCardWidget, CreditScratchCardWidget, PaymentMethodListTile, CardShimmerWidget, PaymentFailureWidget v1 (still references Paytm/EazyPg), UpiCollectInputSheet, UpiWidgetSkeleton, ExpenseCatModel.

# PART B — PROFILE

## B1 `ProfilePageV2`
Gates: isVerified → gold ring + "Verified Member"; isParentApp → parent name; version label ×5 taps → DevEnvBottom. **Error recovery = "Re-Login" button that calls PrefsUtils.clearAll()** (full wipe as only recovery). No RefreshIndicator. Name-row tap copies address AND opens share simultaneously. ProfileMyAddressSection commented out.

## B2 `ProfileMyRentingInfoSection`
Screenshot share; PG logo/name, "Feels Like Home", unit, rent, SD (fallback "0/0"), joined/stayed, evicted-on. **Two hardcoded Firebase IDs at :53-54 and :86-87 branching UI.**

## B4 `ProfileOptionsSection` rows
Personal Details → ProfileDetailsPage · Rental Agreement → PDF or RentalAgreementWidget · Background Verification → PDF or info Dialog (**never opens PoliceVerificationWidget**) · Roommate details → toast **"Coming soon"** · Autopay (gated autopayStatus≠0) → external URL · Property Management Support → ManagementDetail · Move-out → oldEviction ? GiveNoticeSheet : EvictionConfirmedComponent · My Properties. 4 commented go_router blocks.

## B5 `ProfileOtherOptionsSection`
Privacy/TnC links, DataUsingPage, Logout dialog (**Yes/No styled identically, no destructive affordance**) → clearAll. Dead `sendEvictionNotice`; `resetAppThemeToDefault()` (global AppColor/AppTheme mutation) commented out of logout.

## B6 `ProfileDetailsPage` (2,101 lines, LIVE)
View+edit in one. Gates: isProfileLocked (toast + lock label), areFieldsEditable (~40 ProfileTextFields). 10 sections. Placeholder "Not Filled". Toast-only validation on save; no Form/inline errors. 6 DocumentCardWidgets. Enum-normalisation helpers to repair server values. ~14 raw TextStyles.

## B7/B8 `ProfileDetailsPage2` (906 L) + `ProfileEditPage` (1,809 L) — **BOTH UNREACHABLE**
The dead pair has better validation (real regex validators, saving state, success/failure toasts) and better IA; live B6 has the full field set. **Redesign must reconcile deliberately.**

## B9 `DocumentCardWidget`
Status badge only discoverable by tapping (toast) — no visible label. Verified/Rejected/Not Verified/Not uploaded. Upload via openMediaPicker.

## B10 Upload chain
picker → EditImagePage (crop 2x3) → uploadDocumentOrImage (docTypes: Selfie, Aadhar Front/Back, CollegeID Front/Back). **No upload progress/success/failure feedback anywhere — fire and forget.**

## B11 `RentalAgreementWidget` + `SignatureWidget`
Server HTML agreement (HtmlWidget — unstyleable). Sign = rotated canvas ("landscape-signing-in-portrait"), saves rotated base64 PNG → 3 consecutive pops → PDF.

## B12 `PoliceVerificationWidget` — unreachable skeleton (disabled buttons).

## B13 `GiveNoticeSheet` (713 lines, legacy eviction)
Rules from PREFS (getAP/getLOI/getNP), not provider. **SHIPPED DATA BUG: WhatsApp message template interpolates `PreferenceKeys.tenantName` etc. — the KEY CONSTANTS, not values — manager receives literal key strings.** sendNotice → `tenant/sendNotice`.

## B14 `MyProperties` switcher
BaseProvider pattern. switchAccount: loader → Firebase re-auth → profile fetch → EvictedPage or BasePage + refresh 4 providers. **Raw exception shown to tenant ("Error during property switch: $e").**

## B15 `ManagementDetail` / `HelpSupport` — ~90% duplicate screens; "Erase Your Data?" dialog exists in 3 places (also DataUsingPage).

## B17 Viewers
**PDFViewerWidget:** 4-branch WillPopScope encoding onboarding/agreement/newRoute logic incl. setting isLoggedIn and possible clearAll→EvictedPage — business logic in a back handler in a PDF viewer.
**ImageViewerWidget:** hardcoded horizontal 100 padding — overflows small screens.

# PART C — Cross-cutting
- Two color systems mixed within single files; screenutil applied inconsistently; fixed-height rails clip under text scaling.
- Shipped copy defects: June Rent, test description, key-constant WhatsApp message, "via to EazyApp", broken dues copy, analytics typo, debug SnackBar.
- Error/empty/loading uneven: tabs have shimmer+error; pay sheet, UPI rail, method list, cash dropdown, profile screens have NO error state.
- Structural cleanups before visual work: (1) scope PaymentPageProvider + de-singleton CashfreeCheckout; (2) make expanded pay sheet a real route; (3) delete dead gateway constants; (4) reconcile 3 profile screens; (5) split PaymentSuccessfulWidgetV2; (6) merge ManagementDetail/HelpSupport + extract erase-data dialog; (7) fix Color(0x446464339), int.parse(''), paymentKeys![0], missing startTimer().
