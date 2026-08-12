---
title: Current Tenant App: Full Feature Map
date: 2026-08-11
tags: [rentok, tenant-app, revamp, feature-map]
owner: Sanchay
status: reference
---

# Current Tenant App: Full Feature Map

Every feature that exists in the app today, grounded in the code (not the old research notes). Organized by module. This is the starting inventory for the redesign: what to keep, cut, merge, or rebuild gets decided against this list.

---

## 1. Boot & White-Labeling
- Connectivity check before anything loads
- White-label config fetch: colors, logo, app name, nav menu, links, intro text, support number
- Cached white-label config (instant apply) + background refresh
- Three app variants from one codebase: RentOk standard, white-label (per-property brand), OleStays (a specific branded variant with its own splash)
- Crash reporting, FCM push token registration
- Routing after boot: logged-in → home, logged-out → login, join-pending → waiting screen, evicted → evicted screen, no-network → retry screen

## 2. Onboarding & Auth
- Phone number entry with country code
- OTP send + verify
- WhatsApp opt-in toggle at login
- New user vs. existing user vs. self-invite-needed routing
- Multi-property detection: "Choose Property" picker when one phone number has tenancies at more than one property
- Search/filter within the property picker
- Join another property from within the picker
- Self-invite via property App ID/invite code
- Room/unit/bed selection (flat list or nested room→bed, depending on property structure)
- Join request submission (name, room, rent, deposit, move-in date)
- Join-request-pending screen with manual refresh, cancel, and resend-to-owner
- Onboarding intro carousel (exists in code, not currently wired to any entry point)

## 3. Home Screen
- Personalized greeting (tenant or parent, depending on account type)
- Profile completion / verification badge
- Announcements banner + "stories" viewer
- Notification bell
- Pull-to-refresh
- **Sections shown (each independently gated by data/config):**
  - My Account snapshot: dues, credits, advance payment entry, receipt download
  - Pending tasks list (eviction reminders, checklist nudges, external links)
  - Electricity meter balance + recharge link
  - My Complaints/Issues snapshot with quick-call and WhatsApp-to-staff
  - Marketing/promo banner carousel (server-driven, two slots)
  - "Life in Property" quick-action rail: raise a complaint, mark attendance, food attendance, host a guest, check in late, request move-out
  - Today's food menu preview with live-meal indicator
  - Profile status checklist: personal details, KYC, selfie, police verification, rental agreement
  - Reward/scratch cards
  - Offers & RentPass promo rail
  - Second marketing banner slot
  - Footer branding line
- Floating WhatsApp "Help" button
- First-open interstitials: smart attendance setup prompt, mark-attendance prompt, food-confirmation prompt

## 4. Accounts / Money
- **Cashback/Credits tab:** balance, expiring-soon nudge, unscratched reward cards, earning history, owner-given discounts, redeemed/expired history
- **Dues tab:** all outstanding dues, pay one or pay all, autopay setup banner, empty state
- **Expenses tab:** paid history, refund tracking, receipt re-download/re-generate
- **Pay Now flow:**
  - Amount entry (advance or exact)
  - Credit/discount auto-application, editable amount
  - RentPass plan upsell inline in the payment sheet
  - Payment method selection: UPI apps (installed-app detection), other gateways, cash
  - Cash payment: pick staff member, OTP handover confirmation
  - "Share payment link" via WhatsApp
  - Payment success screen: receipt, refund info, reward reveal, WhatsApp share, in-app rating prompt
  - Payment failure screen: retry, raise an issue via WhatsApp, reward consolation
- Security deposit view
- Property switcher (multi-property tenants)

## 5. Profile
- Profile summary: photo, name, phone, address, verification badge
- Share profile (screenshot + WhatsApp)
- My Renting Info: property, unit, rent, deposit, move-in date, tenancy duration
- Personal details view/edit: demographics, family/guardian info, previous & permanent address, education, employment, banking, social/professional links
- Document upload: Aadhaar, ID, selfie, college ID: camera or gallery, crop
- Document verification status per document
- Rental agreement: view, digital signature, download
- Background verification status + explainer
- Roommate details (placeholder, not live)
- Autopay details (hands off to an external portal)
- Property management support contact / help screen
- Send move-out request (entry point into the move-out flow)
- My Properties: list of current + past tenancies, switch active property
- Data usage policy screen
- Privacy policy / terms links
- Logout
- Delete-my-data request

## 6. Food
- Weekly menu browse (breakfast/lunch/snacks/dinner)
- Per-meal detail view
- Meal confirmation (opt in/out per meal, with a cutoff time)
- Live "meal is being served now" indicator
- QR-based plate/attendance scan for a live meal
- Post-meal rating (categories + optional photo)
- Empty state when a property has no mess/food module

## 7. Attendance
- Mark attendance: Wi-Fi-based, manual, or "smart" (selfie + geofence + Wi-Fi combined)
- First-time smart-attendance setup wizard (selfie capture, location calibration, Wi-Fi check)
- Mark absent / mark on leave, with reason
- Late check-in request
- Attendance history calendar with monthly percentage
- Pending leave/late requests tab
- Mark attendance/host a friend or guest
- Reminder nudge to a parent/guardian for pending marks

## 8. Complaints / Tickets
- Complaint list with All/Open/Closed filters and search
- Raise a complaint: category, room/location, description, photos, preferred availability window, optional team-member assignment
- AI-assisted category suggestion
- Complaint detail: status, assigned staff, activity timeline, remarks
- Add remarks/images to an existing complaint
- Rate a resolved complaint
- Batch-rate multiple pending-rating complaints
- "Property Captain" WhatsApp escalation
- AI chat assistant (Tarini) for filing and checking complaints conversationally, with the ability to open a specific ticket from the conversation

## 9. Move-Out / Eviction
- Move-out hub: rules (notice period, lock-in, agreement terms), account summary (dues, deposit, credits)
- Raise a move-out request (reason, date, notes)
- Modify an already-raised request
- Extend stay / cancel an extension
- Cancel a move-out request
- Rate the property post-move-out
- Remind management about a pending move-out
- Key/handover OTP confirmation
- Move-out checklist: per-item room condition self-report with photos
- Final checklist submission

## 10. Add-On Services
- Services overview: stats, popular services, current bookings, favorites
- Browse all services, category tabs
- Service detail page with included items and available slots
- Book a service: date/slot selection, confirm
- Reschedule or cancel a booking
- Booking history: upcoming, completed, cancelled
- Booking detail view
- QR code for service check-in

## 11. Membership / RentPass
- Plan comparison (Pro vs. Elite)
- Savings calculator / estimated monthly savings
- Benefits list with detail pages
- Member reviews and FAQs
- Purchase/upgrade flow (in-app on Android, WhatsApp contact on iOS)
- Spin-the-wheel reward mechanic
- Reward claim flow, including a "locked, buy membership to unlock" path
- All-rewards browse page

## 12. Offers
- Browse offers (tag/category filter)
- Redeemed and expired tabs
- Offer detail: coupon code, validity, redemption steps, terms, share
- Redeem an offer

## 13. Notifications
- Notification feed (property-driven cards: reminders, eviction updates, etc.)
- Tap-through to the relevant flow (currently only fully wired for move-out-related notifications)

## 14. Cross-Cutting / Shared
- Bottom navigation, contents driven by white-label config (home, accounts, services, profile, tickets, attendance, offers, food: up to 4 shown by default)
- Deep links: web, WhatsApp, and in-app (to spin wheel, monthly savings, offers) destinations
- PDF viewer (agreements, receipts, police verification)
- Image viewer + in-app image cropper
- Compulsory KYC gate (can block access to the rest of the app until cleared)
- App-update prompt (force or soft)
- No-network screen
- Evicted-tenant screen
- Hidden developer/environment panel (tap app version 5×)

---

## What's notably *not* a real feature today, despite looking like one
- **Messaging**: no in-app messaging; what exists is the property's WhatsApp Business number, used outside the app.
- **Reviews** (as a tenant-facing module): the survey/review engine exists and runs, but only over WhatsApp; nothing in-app today.
- **Roommate details**: placeholder screen, not functional.
- **Onboarding carousel**: built, not reachable from anywhere.
- Several "reward"/"offer" surfaces exist as separate, overlapping systems (RentPass rewards, general Offers, scratch-card credits) rather than one unified rewards model.