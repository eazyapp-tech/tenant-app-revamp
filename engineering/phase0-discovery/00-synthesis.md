# Phase 0 Synthesis — Tenant App Revamp
Date: 2026-08-10. Full detail in 01–06 in this folder.

## Scale of what exists
~140 screens/sheets/dialogs across 12 modules. 498 Dart files, ~97k LoC. All endpoints mapped client+server side (frozen backend verified at source).

## Verdict 1 — The design system must be rebuilt, not patched
- 4 real color tokens + 152 alias getters; ~41% of color decisions, ~52% of typography, ~98.5% of spacing bypass tokens entirely.
- Two competing color systems (AppColor + legacy AppTheme, 52 refs). Three CustomTextField classes. Four toast/feedback mechanisms (showToast = 232 call sites, fully untokenized).
- Only Regular font weights ship — all bold/semibold/medium are faked.
- flutter_screenutil is a no-op (designSize = device size).
- No ThemeData at all on MaterialApp; whitelabel = global static mutation with no rebuild signal; changeTheme writes fields ~90% of the UI doesn't read → whitelabel primary color mostly never lands.
- Newer screens hand-pasted a Tailwind gray ramp (0xFF101828 ×65 etc.) — the de-facto neutral scale to formalize.
- Token adherence is bimodal: Tarini/membership/offers/eviction-hub nearly clean; attendance/myservice/checklist/Figma-handoff screens 100% raw hex (worst: booking_details 51 hex/0 tokens, mark_attendance_bottom2 ~120 hex).

## Verdict 2 — Personalization fuel, reality-checked against the frozen backend
**FREE (already on the wire):**
- Entire tenant row ships via fetchTenantDetailsByKey: gender, dob, life-stage (university/course vs company/occupation/income), food_preference, marital_status, is_short_term, renting_type, family contacts → tenant-persona personalization needs zero backend change.
- Structured city/state/pincode + property image: GET /tenant/unified/:property_id/bookings (only endpoint that has them).
- Whitelabel fields parsed-but-unused: `style` (purpose-built variant hook), `splashScreenMedia`, navigationMenu `icon` + `deeplink_url` (EazyIcons registry already exists to consume icons), showCashback, brandName.
- **pgLogo: fetched, cached, and NEVER rendered anywhere.** propertyLogoUrl (login) never persisted. The one per-property brand element the user wants literally doesn't show today.
- Feature composition: nav menu + 7 customization booleans + per-module flags already make each property's app different — the composable-home concept rides on this.
- Server-driven card/color hooks already live: reward theming, info-widget chips, eviction status colors, announcement templateId.

**UNAVAILABLE with frozen backend (deliberately stripped at controllers/tenant.ts:6499 `delete tenant.property`):**
- pg_available_for (gender policy), tenants_preferred (segment), property_type (PG/co-living/hostel), is_mess, locality, amenities, capacity, brand_color, property_nearby. All in DB one hop away, none on any tenant endpoint.
→ Property-ARCHETYPE personalization can't use property columns. Pivot: persona (tenant row) + geography (unified/bookings) + feature composition (which modules are on ≈ property type proxy: attendance+food on → student PG; services on → co-living). OR: one additive backend change unlocks the full axis — decision for Sanchay.

## Verdict 3 — Structure blocks design
- Home = hardcoded Column; no ordering engine; server levers are 7 booleans + 2 marketing slots.
- Gating fragmented across 4 mechanisms (nav menu, customization, per-API flags, prefs bools) + hardcoded pg_id arrays server-side (SERVICES_PG_IDS etc.) + hardcoded client special cases ("Orchid Parc", two Firebase pgIDs).
- Duplicate network calls per home load (fetchTenantHomePage ×2-3, complaints ×2, food ×2, passbook ×2).
- PaymentPageProvider global singleton + CashfreeCheckout factory singleton; pay sheet cosplays as a page; loader-dialog stuck-state class of bugs.
- Only Cashfree is live — CLAUDE.md's Razorpay claim is false; all 8 gateway constants funnel to Cashfree.
- Three parallel profile screens (1 live worse, 2 dead better). Dead code everywhere (onboarding carousel, spin home section, po-verification, ~15 orphan widgets).
- No i18n. No dark mode. No real splash (white screen + spinner).

## Notable shipped defects (sample)
'June Rent' + test-description placeholder copy in payment failure; WhatsApp move-out message interpolates preference KEY CONSTANTS not values; profile-complete flag used un-inverted; Color(0x446464339) invalid literal; int.parse('') crash in failure handler; OffersProvider duplicates on refresh; property_map_link permanently "" (backend lng/long bug); isComplaintBotActive pref key is literally '0'.

## Mobbin north star (see 06)
7 principles: the place not the platform · one number one verb · celebrate the rent · talk like a good warden · typographic theater on a white-label skeleton · belonging is a widget · show up get seen. 10 mapped reference flows (CRED payments, UC booking, Airbnb support+profile, Zomato food, Duolingo streaks).

## Phase 1 inputs (next)
1. Concept brief: emotional thesis + personalization system (persona × geography × composition × property-logo moment) + design-language direction.
2. Decision needed: accept persona/geo/composition personalization within frozen backend, or scope one additive endpoint change for property archetype.
3. Pending: Notion share (⋯ → Connections → easyccmcp).
