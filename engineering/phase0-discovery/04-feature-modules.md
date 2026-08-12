# Phase 0 — Food, Attendance, Complaints, Eviction, Services, Membership, Offers, Notifications

## 0. Cross-cutting

### Routing
`lib/router/routes.dart` + `route_constants.dart` 100% commented out. All navigation imperative. Deeplink surfaces: `intent_handler.dart` (web / whatsapp / inapp → spin_wheel, monthly_saving, view_offers) + Firebase Dynamic Link switch in `basepage.dart:270-335` (account, myservice, tenant-profile, markattendance, checkattendance, latecheck-in).

### THE FEATURE GATES
- **Gate A — navigationMenu** (whitelabel): applied only if length > 2; keys home/accounts/services/profile/tickets/attendance/offers/food; unknown dropped; fallback = Home/Account/Tickets/Profile (**Services, Attendance, Offers, Food have NO tab in fallback**).
- **Gate B — customization** (fetchTenantHomePage): complaints, hostFriends, attendance, foodAttendance, markLeave (dead — parsed, never consumed), checkInLate, sendNotice. All-false → section null. toJson/fromJson key asymmetry (`food_attendance` vs `foodAttendance`).
- **Gate C — Smart Attendance** (`tenant/attendance` → TenantAttendanceSetup): isSmartAttendanceEnabled==1 → home popup chain; isSetupComplete==0 → forced non-poppable SetupAttendancePage; showBottomSheet==1 → non-dismissible MarkAttendanceBottom2; isWifiEnabled; isAttendanceWindow gates deeplink; also flips retry label + attendanceType payload.
- **Gate D — Food attendance**: isFoodAttendanceEnabled==1 → chain; isMealLive==1 → FoodAttendanceBottom (QR); else showFoodConfirmationBottomsheet==1 → FoodConfirmationBottom. Home live badge = case-insensitive title match.
- **Gate E** — HomeMenuSection hidden when `Constants.appName == "Orchid Parc"` (hardcoded).
- **Gate F — Complaint bot**: `PrefsUtils.getInt(isComplaintBotActive) == 1` — from profile response. **BUG: key string is literally '0'.** Gates WhatsApp captain button + Tarini FAB.
- **Gate G — Eviction old/new**: `oldEviction` pref (from getTenantAppStatus.old_eviction): true → GiveNoticeSheet; false → EvictionConfirmedComponent. Checked in 3 places.
- **Gate H — RentPass**: RentPassProvider.isMember/isElite from getTenantMembership (200 → member; type 1 Pro / 2 Elite). **Platform.isIOS gates purchase everywhere** (iOS: "Contact now" WhatsApp; Android: Buy Now → PayNowSheetWidget(isRentPassOnly)).
- **Gate I — Services**: no client flag; server `enabled_only=true`.

**Two FoodProvider classes exist:** `lib/application/foods_provider.dart` (legacy, registered globally, unused) vs `lib/presentation/food/food_provider.dart` (real, page-scoped).

## 1. FOOD (2,832 LOC)
- **FoodMenu (food.dart 723 L):** weekly menu + meal confirmation. Client-side clock logic for toggles (showMealToggles: tomorrow always, today until confirmation cutoff). Shimmer; empty state; **no error state** (error falls to empty). Success & failure toasts use same message. 12 inline TextStyle, ZERO AppTextStyles; Colors.grey[…]; hand-rolled month parser; Theme(useMaterial3:false) wrapper.
- **SingleFoodBottom:** meal detail; `Image.asset` on possibly-remote URL (crash risk).
- **FoodProvider (336 L):** weekday string comparison copy-pasted in 3 ladders; manual hour/min parsing; no timezone.
- **FoodConfirmationBottom:** "Will you have food tomorrow?" + live countdown ⏳; entry home only.
- **FoodAttendanceBottom (629 L):** QR plate scan (mobile_scanner). 7 internal view states incl. ML-Kit module download error, permission dialog, processing. Colors 0xFFFFF2F2/0xFFFFF8E6/0xFFFFE0A3/0xFFB8860B not in AppColor. Mixed button primitives.
- **FoodPlateError:** backend returns 400 for all business failures; message string is the discriminator → fragile mapping table.
- **FoodSuccessBottom:** "{Meal} availed" + identity card; auto-opens RatingBottomSheet if isRatingMandatory==1 (non-dismissible).
- **RatingBottomSheet + success:** per-category stars + photos → uploadImageToS3 + foodRating. Zero AppTextStyles.
- **FoodCardWidget: DEAD.**

## 2. ATTENDANCE (9,181 LOC — largest)
- **MarkAttendanceBottom2 (3,271 L — largest file): a ~28-state state machine in one bottom sheet.** Mark present (swipe)/absent/leave/late/view day. 6 entry points (home auto non-dismissible, 2 deeplinks, life-in-pg card, history ×3, post-setup). States: markingOptions, selfie upload/fail, camera init/denied/permanent/no-cameras/capture-fail, face-not-matched, location perm ×4, wifi ×3, marking, 4 success variants, leaveSummary, absentStatus, error. Swipe-to-confirm, Lottie, 3 emoji reason grids, timeline. **~120 hardcoded hexes, zero AppColor; Divider(thickness: 0.693)** — Figma exports leaked into code. Status codes: 111 present, 112 leave, 113 absent, 114 late.
- **MarkAttendanceProvider (779 L):** camera+GPS+wifi+MAC+compression+countdown stream; hardcoded emoji reasons; salutation.
- **SetupAttendancePage (497 L):** forced (PopScope canPop:false, no leading) when isSetupComplete==0. WhatsApp "Ask admin" escape only.
- **SetupAttendanceBottom (1,446 L):** selfie → location calibration → wifi wizard. **7 raw Material AlertDialogs** (visually alien to sheet language). attendanceSetup called from 3 places.
- **SetupSelfieCameraPage (665 L):** custom camera, face guide, white-on-black chrome, no tokens.
- **TenantAttendanceHistory (1,256 L):** Requests + Calendar tabs. Consumer2 — either provider's error blanks whole screen. ~55 hexes. **Calendar status palette defined 3× inconsistently** (_getStatusColor, _buildLegend, MonthlyAttendanceProvider.getStatusColor).
- **MonthlyAttendanceProvider:** UI copy + colors in provider layer.
- **HostAFriendWidget (820 L):** guest registration sheet; ~50 hexes, zero tokens; form rows repeated 4×.
- **AttendanceProvider (global):** legacy grid path dead; print() statements.

## 3. COMPLAINTS (7,623 LOC)
- **ComplaintsPage (629 L):** filters all/open/closed (closed = status 5), search (3 predicates), 2 derived banners (pendingRating, pendingAvailability), 2 FABs (Tarini + add) with shifting padding. Empty "No complaints found!".
- **AddComplaint (1,387 L):** create + edit in one State class. ConcernBottom, IssueLocationBottom, MediaViewer, AddAvailabilityWidget (opened from 4 places). AI category via `complaint-bot/get-category`. ~10 toast paths, 6 FocusNodes, debouncer. 22 inline TextStyle vs 2 AppTextStyles.
- **ComplaintDetails (1,110 L):** status/media/audit trail; audit 400 "No history found" treated as empty; close/reopen raw dialogs; video thumbnails.
- **TariniChatPage (742 L):** AI chat, page-scoped provider, **separate host rentok-complaint-bot.onrender.com**, fresh Firebase ID token per call, 90s/30s timeouts. Friendly error bubbles instead of toasts; 429 rendered as normal bot message. **Best-behaved screen in slice (44 AppColor, 11 AppTextStyles, 1 hex).** Deep-links tickets to ComplaintDetails.
- Widgets: AcivityLogsWidget (sic, 559 L), AddAvailability (sic filename), ComplaintCard (inline updateComplaint), ComplaintRatingBottom, ConcernBottom, HomeComplaintCard (commented-out block ~116-190), IssueLocationBottom, RateComplaint (batch rate), TransactionRecordsWidget.
- **MasterDesignationProvider: unused by any screen.**

## 4. EVICTION (6,003 LOC)
- **EvictionConfirmedComponent (1,385 L):** move-out hub. **Server state machine on evictionState.status:** 0 → only Raise CTA; !=1 → Modify + Cancel; ==1 → Extend Stay; always Rating + Complete Handover. checklist.cta {enabled, text, ctaColor} + evictionState.{text,textColor} server-driven hex (no fallback validation). Extra server flags: isEvictionChargesEnabled, isCompleteHandoverEnabled, isHandoverDone, isRaisedByTenant, isBlacklisted, isEvictionApproved, isEvictionComing. Error state = centered text, NO retry. EvictionProvider double-registered (global + page-scoped).
- Sheets: RaiseRequestLayout (450 L, doubles as Modify via isEdit), MoveOutReasonLayout (also owns cancelEviction — reused as Cancel sheet), AddReasonBottom, ExtendRequestBottom, EvictionRatingBottom, **SelectTeamBottom (DEAD)**, EvictionRulesBottom, EvictionHandoverOtpBottom (2 nested sheets).
- Checklist: MoveoutChecklistPage (449 L, 24 hex/0 tokens, TopWidget filters −1/−2/0…), **MarkConditionBottomSheet (845 L, 48 hex/0 tokens — 2nd worst)**, SubmitChecklist (483 L).

## 5. SERVICES (5,996 LOC) — worst token adherence as a module
- **ServiceOverviewPage2 (1,077 L):** "Life in {pgName}" overview; 43 hex, 0 AppTextStyles; borderRadius 12.75 Figma float. No section empty states.
- **ServiceAmenitiesPage (518 L):** catalogue; 25 hex/0 tokens.
- **ServiceDetailsPage2 (840 L):** detail + slots; `'Coming soon'` toast at :94; 42 hex/0 tokens.
- **BookServicePage2 (659 L):** slots + book/reschedule; 28 hex/0 tokens.
- **BookingStatusPage (357 L):** add_2_calendar; ~40-line commented AppBar.
- **BookingDetailsPage (1,024 L): 51 hex, 0 AppColor, 0 AppTextStyles — single worst file.**
- **CheckInQrCodePage (339 L):** base64 QR + PIN fallback; string-split on 'base64,'.
- **BookingHistory (211 L):** status query param commented out.

## 6. MEMBERSHIP / RENTPASS
- **MemberShipPage (568 L):** 7+ entry points (profile entry commented out). Gates all client-side on RentPassProvider (isMember/isElite/selectedTab); background rentpassBlack vs benefitColorBody; RewardWidget commented out. **Only success state handled — loading/error render nothing.** Clean tokens (0 hex).
- **RentPassProvider (99 L):** getResponse() NOT called in constructor — IntentHandler + PayNowSheetWidget read .isMember without guaranteeing load.
- **Spin wheel:** SpinTheWheelPage (345 L, flutter_fortune_wheel + SpinStream singleton w/ sound — **singleton disposed by page = re-entry hazard**; spinStatus==4 → UnlockRewardWidget; home section entry commented out). ChooseOfferPage (473 L; claim → isMember? ActivateOfferPage : locked? platform-split AlertDialog : MemberShipPage). ActivateOfferPage (client-built FAQs; **FaqsItem class defined twice**). UnlockRewardWidget.
- **Monthly savings:** MonthlySavingPage (341 L → getTenantStepperV2), stepper widget, EstimatedSavingSlider + NonElite near-duplicates.
- **Benefits/reviews/FAQs: ReviewProvider and FaqsProvider have NO API — hardcoded client content.**

## 7. OFFERS
- **OffersPageV2 (85 L):** 3 tabs (Offers/Redeemed/Expired). **Bugs: initState double-fetch (getTenantOffers + refreshOffers); TabController(3) at 0 vs inner DefaultTabController initialIndex 1 conflict.**
- Sections: TopOffers/Redeemed/Expired — Shimmer.fromColors ×5, tag rail, empty states, EazyErrorWidget.
- **OffersProvider (87 L): force-unwraps response.data!/rewards! with no status check; currentOffers never cleared → duplicates accumulate on refresh; "All" magic string.**
- **OfferDetailsPage (510 L):** redeem via claimOtherReward; 403 → Buy Now dialog (**no iOS branch here — inconsistent with ChooseOfferPage App Store handling**); `HexColor.fromHex(backgroundColor!)` force-unwrap; screenshot share.

## 8. NOTIFICATIONS (213 LOC)
- **NotificationWidget (88 L):** entry = home bell only. Data typed as **EvictionCardRes** (reuses eviction-card model). Duplicate empty states (one raw fontSize 23); **no error state**; dead postFrame callback.
- **NotificationCardWidget:** always fires callEventApi read-receipt; `activity=="eviction"` → eviction flow; **any other activity = silent no-op** (tappable, goes nowhere). Date format with backtick.

## 9. Highest-signal findings
1. **Gating split across 4 unrelated mechanisms** (navigationMenu, customization, per-API flags, prefs booleans) — a module can have a nav tab while its home card is hidden, and vice versa.
2. **Token adherence bimodal:** newer screens (Tarini, membership, offer details, eviction hub, notifications) nearly clean; Figma-handoff screens (attendance, host-a-friend, myservice, checklist) 100% raw hex. Worst: booking_details_page (51/0), mark_condition (48/0), service_overview_page2 (43/0), mark_attendance_bottom2 (~120).
3. Attendance status colors defined 3× inconsistently.
4. Dead/orphaned: food_card_widget, select_team_bottom, legacy FoodProvider, legacy attendance grid, customization.markLeave, HomeSpinTheWheelSection, RewardWidget, lib/router/, MasterDesignationProvider.
5. Latent bugs: isComplaintBotActive key '0'; OffersProvider duplicates; OffersPageV2 double-fetch/tab conflict; Customization toJson asymmetry; SingleFoodBottom Image.asset on URL; HexColor force-unwrap; SpinStream dispose; EvictionProvider double registration.
