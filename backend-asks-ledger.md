---
title: Backend Asks Ledger: Tenant App Revamp
date: 2026-08-10
tags: [rentok, tenant-app, revamp, backend]
owner: Sanchay
status: living
---

# Backend Requirements Ledger

The new app gets its own service layer, built on the property and tenant data the business already keeps ([TAR-00](TAR-00-vision-and-requirements.md)). Any capability the design needs from that service layer lands here as it is discovered, with its reason. This began life as a list of deferred requests when the backend was treated as frozen; it is now simply the running requirements list for the new services. Nothing here blocks design work.

Known so far, beyond the entries below: property attributes flowing to the app (type, who it serves, city), offer targeting by city, property, register, and age, the under-18 content gate, and the survey system surfaced in-app. The entries below carry their original investigation notes.

| # | Ask | Why the tenant needs it | Ground truth | Status |
|---|---|---|---|---|
| 1 | Read endpoint over the WhatsApp message log (e.g. `GET tenant/:uuid/whatsapp-messages`) | Messaging section: show the tenant their property's white-label WhatsApp thread inside the app | Store exists and is populated (`whatsapp_messages_dash`, written by `services/meta/v2TenantMeta.ts`); every current reader is manager-side | Noted |
| 2 | Verify and, if needed, extend `GET /tenant/:tenant_uuid/review-details` | Reviews section: bring the working review + survey system (today WhatsApp-web-form) natively into the app | Endpoint exists (`routes/tenant.ts:1102` → `getBookingReviewDetails`, `controllers/tenant.ts:27875`); response shape and campaign coverage unverified | Noted: verification is a first task of the Reviews ideation round |
| 3 | Offer targeting: scope offers/rewards by property, city, and tenant type; support a second source (property's own offers alongside RentOk's partner network) | Offers must read as curated for this tenant in this city, and show nothing gracefully where nothing is live | `POST /rewards/fetchAllRewards` returns one flat global pooled catalogue; no geo/property/tenant-type scoping found (Phase 0 report 05) | Noted |
| 4 | Owner-set "sponsored tenant" flag (company pays the rent) | Register 5: mute dues nagging for tenants who do not pay their own rent; today there is no reliable signal, so the register ships as a softened monthly-loop variant | No field on any tenant endpoint indicates an external payer (Phase 0 report 05) | Noted |

## How to add an entry

One row per ask: what it is, why the tenant needs it (user reason, not team convenience), where the current code stands (file:line), status. Statuses: Noted, Approved, Built.  Declined asks stay on the list with the reason, so they are not re-litigated from scratch.