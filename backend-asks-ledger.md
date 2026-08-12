---
title: Backend Asks Ledger — Tenant App Revamp
date: 2026-08-10
tags: [rentok, tenant-app, revamp, backend]
owner: Sanchay
status: living
---

# Backend Asks Ledger

The rule from [[TAR-01 Brief]]: cycle 1 redesigns existing workflows on existing endpoints and never destabilizes production. Any additive backend need found mid-design lands here with its reason. Sanchay decides its cycle. Nothing on this list blocks design work; concepts are drawn as if the ask will land, and degrade gracefully if it has not yet.

| # | Ask | Why the tenant needs it | Ground truth | Status |
|---|---|---|---|---|
| 1 | Read endpoint over the WhatsApp message log (e.g. `GET tenant/:uuid/whatsapp-messages`) | Messaging section: show the tenant their property's white-label WhatsApp thread inside the app | Store exists and is populated (`whatsapp_messages_dash`, written by `services/meta/v2TenantMeta.ts`); every current reader is manager-side | Noted |
| 2 | Verify and, if needed, extend `GET /tenant/:tenant_uuid/review-details` | Reviews section: bring the working review + survey system (today WhatsApp-web-form) natively into the app | Endpoint exists (`routes/tenant.ts:1102` → `getBookingReviewDetails`, `controllers/tenant.ts:27875`); response shape and campaign coverage unverified | Noted — verification is a first task of the Reviews ideation round |
| 3 | Offer targeting: scope offers/rewards by property, city, and tenant type; support a second source (property's own offers alongside RentOk's partner network) | Offers must read as curated for this tenant in this city, and show nothing gracefully where nothing is live | `POST /rewards/fetchAllRewards` returns one flat global pooled catalogue; no geo/property/tenant-type scoping found (Phase 0 report 05) | Noted |
| 4 | Owner-set "sponsored tenant" flag (company pays the rent) | Register 5: mute dues nagging for tenants who do not pay their own rent; today there is no reliable signal, so the register ships as a softened monthly-loop variant | No field on any tenant endpoint indicates an external payer (Phase 0 report 05) | Noted |

## How to add an entry

One row per ask: what it is, why the tenant needs it (user reason, not team convenience), where the current code stands (file:line), status. Statuses: Noted → Approved for cycle N → Built. Declined asks stay on the list with the reason, so they are not re-litigated from scratch.