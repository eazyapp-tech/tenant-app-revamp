# Phase 0 — Backend Truth (rentok-backend, FROZEN)
Source: `/Users/eazypg/rentok-backend`. Client endpoint list: `rentok_tenant_package/lib/network/api_const.dart`.

## 1. Endpoint map (tenant-app-facing)
Router mounts `src/server.ts:163-237`.

### Auth/session
- `POST /tenant/sendLoginOtp` (controllers/tenant.ts:27963)
- `POST /tenant/tenantLoginSignup` (:25081-25417). 3 shapes: (a) multi-property → `properties[] {tenant_uuid, phone, pg_name, eazypg_id, doj, doe, pg_id, pg_number, tenant_name, property_address (concat), property_logo_url, status, room_name, parent_phone}` + multi_property_token; (b) no tenant → {url, customToken, tenantAuthenticatableTestData}; (c) single → customToken + jwtToken (jwt = {tenant_uuid, property_id, pg_id, pg_number, status, role, parent_phone}) + tenantAuthenticatableTestData + tenantConfigData.
- `GET /tenant/refreshToken` (:25419) → {jwtToken}
- `POST /tenant/login` (tenantAuthenticate, :30927) — FCM registration only
- `GET /tenant/properties` (:25707) — same property objects; **returns [] for any non-RentOk package name (:25720)**
- `POST /tenant/getTenantCustomToken`

### Profile
- **`POST /tenant/fetchTenantDetailsByKey` (:6347-6644) — richest payload. Spreads the ENTIRE Tenant entity row (:6618)** + adds: police_verification_google_form, is_evicted, property_address (concat string), property_map_link (**always "" — bug: reads property.lng but column is `long`, :6467-6469**), profile_incomplete, pg_name, pg_logo (property.logo_url || CDN fallback), communication_contact, support_email, support_whatsapp, agreement_period, is_verified, rental_frequency_text, room (STRING_AGG), checklist PDFs. Plus show_kyc_section, tenant_app_info (version floors), is_complaint_bot_active, complaint_bot_number.
  **`delete tenant.property` at :6499 — the whole Property object is stripped; only 8 hand-picked property fields survive.**
- `GET /tenant/unified/details` (services/tenant/tenant.ts:11929) — tenant + tenant_meta overlay (board, medium, stream, class, medical, parent_pan_card, secondary phones, parent emails).
- **`GET /tenant/unified/:property_id/bookings` (svc :11965-12058) — THE ONLY endpoint with structured `property_address {address_line_1, address_line_2, city, state, pincode}` (:12043-12049) and the only one returning property_image (property.images[0].url).**
- `GET /others/get-tenant-details` (controllers/others.ts:9687) — NO AUTH; 14 fields incl. name/phone/selfie/gender.
- Writes: editTenantDetailsByTenant, uploadTenantImage, checkTenantCompulsoryKYC, deleteUserDataRequest.

### Home
- `POST /tenant/fetchTenantHomePage` (:15239-15388): upper/lower marketing (lower always []), customization = 7 booleans from property.tenant_app_* + food_attendance_enabled. **Select at :15283-15296 loads ONLY those 7 columns.** Parent app package gets hardcoded override (:15311-15325).
- `POST /tenant/getTenantAppStatus` (:15395-16112): version floors (hardcoded package_build_number_json), is_evicted (**hardcoded false :15467**), ui_data (server-driven bottom sheet), old_eviction (= !is_new_eviction_flow), autopay_status (0/1/2), autopay_url.
- `GET /tenant/:uuid/tenant_app/eviction-details-card` (svc :8936-9226): task-card feed; conditioned on complete_handover_enabled, autopay_status, movein_moveout_checklist_enabled, eviction state.
- `GET /tenant/:uuid/tenant_app/notification-details` (svc :9234): from tenant_app_cards where card_type='notification'.
- **`POST /tenant/fetchTenantNotifications` — permanent stub, always [] (:28135-28141).**

### Passbook
`POST /tenant/getTenantPassbookForTenantApp` (:4368-4634): dues, collection, totals, isPartialPayment (property.is_partial_payment), **upi_intent = "none" unless property.collect_online_payment && tenant.collect_online_payment (:4618)**, credits blocks, SD totals.

### Attendance
`GET /tenant/attendance` (svc :1716-2134): slot state, is_smart_attendance_enabled, is_setup_complete, wifi_list (property.list_of_wifi), property_lat/long (correct here), spatial distance, bottom_sheet flags (**key is `bottomsheet` on early-return branch :2057 — inconsistent**), is_wifi_enabled. Plus attendanceSetup, mark_attendance, monthly_list (+attendance_widget {present, leave, absent, late} + warden_phone), markTenantLeave, late-checkin-request.

### Food
- `POST /property/fetchFoodData` (controllers/property.ts:10819): menu + timings; **400 with same body when food_menu.is_active !== true (:10966)**.
- `GET /tenant/:uuid/fetchTenantMenu` (svc :9281-9465): food_array, timings, timing text, meals_confirmed (today+tomorrow ×4), confirmation times. 400 "Food Menu is not enabled" (:9307-9315).
- fetchFoodAttendance (:9475), markFoodConfirmation (:9800), takeFoodPlate (:9981), foodRating (:10092), food history ×2.

### Complaints
fetchTenantComplaints (controllers/complaints.ts:2178) — raw entity rows, no relations. addComplaint, addTenantComplaintWithImage, addComplaintFeedback.

### Eviction
eviction_details, eviction-details (svc :4093), raise (svc :6056), extend (svc :5745), remind, add-rating (svc :5920), sendNotice, agreement-details + renew.

### Services / rewards / misc
addon-services CRUD + QR; **`POST /rewards/fetchAllRewards` (controllers/rewards.ts:110): global pooled catalogue Pool1..6 pro/elite — NOT property-scoped, no personalization surface**; fetchOuterRewards/RedeemedRewards/claim; tenantSpin; tenantMembership; benefits; announcements; hostTenant; requestLateCheckin; getTenantStepperv2; entry-exit module (routes/entryExit.ts:7-27: monthly widgets, create request, send-otp, parent-approved, instant, late-return-extend, logs, config).

## 2. ATTRIBUTES

### 2.1 Property attributes that DO reach the app
pg_name, logo_url (pg_logo), address concat (structured ONLY via unified/bookings), property image (unified/bookings only), communication contact/email, agreement_period, PV form, pg_id/pg_number/eazypg_id, tenant_app_link, lat/long + wifi (attendance only), smart-attendance flag, food flags + menu, isPartialPayment, collect_online_payment (as upi_intent), is_new_eviction_flow, autopay_status, complete_handover_enabled, checklist settings, 6 tenant_app_* module toggles, entry_exit_setting (whitelabel ride-along).

### 2.2 Tenant attributes — FULL ROW ships via fetchTenantDetailsByKey
Personalization-relevant: gender, dob, blood_group, nationality, mother_tongue, marital_status, food_preference, medical_condition, allergies, medications, vehicle_number; **life-stage: university, graduation_year, course_name/year, institude_id, working_type, employment_type, occupation, work_designation, tenant_company_name, company_position, monthly_income, work_address**; family/parents/guardians; tenancy (status, doj/doe, checkout, notice/grace/lockin, room, rent, rent_range, SD, is_short_term, rental_frequency, renting_type, facilities, food_opted, checkin/checkout_time); addresses incl. full perm_*/prev_* splits; KYC statuses; derived profile_incomplete/is_verified/is_evicted.

### 2.3 In DB but NEVER on any tenant endpoint (verified via grep of all read paths)
| Attribute | Column | Non-tenant surface |
|---|---|---|
| **Gender policy** | `pg_available_for` (property.ts:225) | write-only |
| **Tenant-type policy** | `tenants_preferred` (:243) | write-only |
| **Property type (PG/co-living/hostel)** | `property_type` (:723) | manager select; roomRecommender prompt |
| Mess available | `is_mess` (:160) | write-only |
| Capacity | max_occupancy, no_of_rooms, no_of_floors, no_of_staffs, total_available_area | manager only |
| Locality/landmark/police station | :981/:167/:234 | manager only |
| Founding year | :680 | nowhere |
| Amenities | is_parking_available (:671), is_power_backup_available (:674), wifi_is_checked (:246), is_utility_bill | microsite includedServices; roomRecommender |
| Inventory shape | sharing_types_enabled (:413), unit_types_available (:416) | microsite/search |
| **Property brand color** | `brand_color` (:391) | payment page only |
| Price band | rent_starts_from/ends_to | microsite |
| Gate timing | gate_closing_time, last_entry_time, checkin/checkout_time | not on tenant read path |
| Geo boundary | boundary_coords, coords | geofence math only |
| Birthday flag | is_birthday_whatsapp_enabled (:773) | **birthday personalization already in DB** |
| `property_nearby` relation | :449-473 | unused personalization asset |
| collect_cash_payment (:592) | — | **not sent — app can't know cash is disallowed** |
| is_verified property trust badge (:616) | — | unused |

### 2.4 Bug
`controllers/tenant.ts:6467-6469` reads `tenant.property.lng` but column is `long` → **property_map_link permanently ""** — tenant app never had a working map link.

## 3. Property entity: full column list captured in agent report (1,030 lines, ~150 columns; legend T/– above covers redesign-relevant ones). Related config entities: entryExitSettings, property_attendance_config, propertyAttendanceSlotSettings, propertyFoodConfig, property_kyc_setting, propertyChecklistSettings, property_images, property_nearby, propertyLocations, property_contact.

EntryExitSettings columns: is_active, male/female return + late-entry times, scheduled_exit_approval_enabled, late_entry_approval_enabled, approval_authority, auto_approve_warden, inform_parents_on_exit/late_entry, list_of_wifi, access_methods. Only a derived 0/1/2 int reaches the app.

## 4. Feature gating — 4 channels, no single source
(a) customization booleans (fetchTenantHomePage; select loads only those 7 columns).
(b) navigation_menu jsonb (whitelabel row served verbatim; default RentOk menu **hardcoded in handler** controllers/others.ts:10473-10499 with slot-2 swap: entry_exit_settings → `gatepass`; else SERVICES_PG_IDS (hardcoded array, helpers/constants.ts:14788) → `services`. Siblings: GATE_PASS_PGS :14802, ENTRY_EXIT_PG_IDS :15521).
(c) 400-on-disabled (food; upi_intent "none").
(d) behaviour switches on other endpoints (old_eviction, autopay_status, eviction card self-gating). Plus package-name gating (properties [], whitelabel login pg_id restriction, hardcoded version floors).

## 5. `GET /others/whitelabel-user` (controllers/others.ts:10435-10578)
Inputs: header x-package-name (required), query pg_id/property_id, JWT pg_id.
Logic: property-level whitelabel row wins → pg-level fallback (repositories/whitelabelUsers.ts:10-27, 60s cache) → else package_name lookup. entry_exit_setting derived: 0 none / 2 both approvals NEVER / 1 otherwise.
No row: build default 4-item nav (slot-2 swap) — synthetic response ONLY for net.eazypg.eazypgtenant[ios] with resolvable pg_id (hardcoded id, app_name "RentOk Tenant", support number from 8-entry hardcoded pg_id map :10519-10528); else "Whitelabel user not found".
Row exists: returns ENTIRE WhitelabelUsers entity (all of entities/whitelabelUsers.ts:12-87) + injected entry_exit_setting.
Adjacent: getWhiteLabelColorScheme is a **hardcoded stub** (#000000/#FFFFFF).

## Headline takeaways
1. **Tenant-attribute personalization is free** — full tenant row already ships.
2. **Property-side personalization signals are deliberately destroyed** (`delete tenant.property` :6499). property_type / pg_available_for / tenants_preferred / is_mess / locality / amenities / capacity are in DB, one hop away, but never reach the app. FROZEN backend = these are unavailable.
3. **unified/bookings is the existing no-change path for structured geography (city/state/pincode) + property image.**
4. Feature gating fragmented across 4 mechanisms + hardcoded pg_id arrays.
5. fetchTenantNotifications is a stub; real feed = tenant_app_cards.
6. property_map_link dead (lng/long bug).
