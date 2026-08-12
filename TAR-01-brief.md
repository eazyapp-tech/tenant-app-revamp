# TAR-01 · The Product Brief

**Read [TAR-00](TAR-00-vision-and-requirements.md) first.** TAR-00 says what we are building and why. This document says how the bet works: how the app spreads, how personalization behaves in practice, what gets built in what order, and what could go wrong.

*Last updated 12 August 2026. Owner: Sanchay. Evidence marks (Verified, Seen in the field, Our read) are defined once, in [TAR-03](TAR-03-what-each-part-must-become.md).*

---

## The bet, in short

WhatsApp already handles messages and payment links well. Competing with WhatsApp on utility is a losing game. The one thing WhatsApp can never be is the app of the place you live: your building's name and logo, tonight's dinner, your attendance streak, your rent record, the people around you. We bet that belonging is what makes a tenant keep the app, and utility is what makes them trust it. Both, in that order.

And because adoption gates everything: the owner is the channel. Our field interviews say tenants install the app when the owner pushes it, and rarely otherwise: the strongest signal in the research, and one the research kit still tests directly. So the handover moment is part of the product. The owner shows a code at move-in, the tenant lands in a welcome that feels like arriving home, and the owner can see who joined.

## How the app spreads

Three paths, each designed on purpose:

**To the people on your floor.** Some features simply work better when your floormates are on them too: the dinner poll, splitting the electricity bill, the shared list. A tenant pulls their neighbors in because the thing does not work alone. This is the cheapest growth we have, and it is why naturally shared features rank high on the flexible list.

**To friends in other properties.** This runs on things worth showing: a receipt that looks like a document worth keeping, a streak worth a screenshot, a menu that makes a friend ask which app that is. The friend whose landlord is not on RentOk is not a dead end. They are the open-for-all door's first real user.

**To the tenant's own landlord.** A tenant asking their landlord "why don't we have this?" is a warm sales lead that costs nothing. The current app actually contains an invite-your-property flow, but it is hidden from white-label users and its button does nothing (Verified). The new app makes this path first-class for everyone.

What makes a tenant recommend the app is not a referral code. It is pride in how the app presents their home, a record that says something about them, features that need their friends, and one story stronger than all of them: "this app got my deposit back." Deposit disputes are the most painful ending in Indian renting. A tenant protected by timestamped move-in photos will tell everyone they know.

The line we never cross: no feature is ever locked behind sharing. No contact-list harvesting. No nagging. The moment sharing becomes a toll, both the taste and the advocacy are gone.

## Personalization in practice

Four things shape what a tenant sees. The manager app already captures the property side of this data, and anything missing can start being captured.

| What we know | What actually changes |
|---|---|
| **Who the tenant is** (student, professional, family, cash-first, sponsored) | Greeting, tone, and what comes first on Home. A student's evening is food and the gate. A professional's month is rent and receipts. A sponsored tenant, whose company pays, is never nagged about dues. |
| **Where they live** (city, state) | Offers, services, and local content. Nothing irrelevant to their city. |
| **What the property is** (PG, co-living, hostel, flat; boys, girls, co-ed) | Which sections exist at all, and how sensitive features like entry and exit present themselves. |
| **How old they are** | Which offers and content appear. Under 18: profiling off entirely, curated age-appropriate content only. This is the law, not just our taste. |

Three rules keep this honest:

1. **Needs, never clichés.** No "girls PG gets pink." Content targeting runs on rules and eligibility, not stereotypes.
2. **Personalization changes what appears, never what the app can do.** Every tenant has the same abilities.
3. **The comfort line belongs to tenants, not to us.** Where being known stops feeling helpful and starts feeling watched is exactly what the research kit tests (the concept tests probe which personalized elements people reject, and why). We will follow their answers, not our assumptions.

And the standing brand rule: the property's logo and name lead the app. Today the current app fetches the property logo and never shows it anywhere (Verified). In the new app, the tenant's first moment is their own home's mark.

## What gets built, in what order

The new app is built alongside the untouched production app, then tenants migrate. Build order follows dependency and trust, not module lists:

**Phase 1: the foundation.** The design system, because every screen inherits it. Then the core loop: joining and first open, Home, and Money. These three carry the first impression, the daily glance, and the trust moment. If these three are not exceptional, nothing that comes later matters.

**Phase 2: the daily habits.** Food and Attendance. These bring the student register back every day, and daily return is what adoption means. Complaints and Profile complete the trust core alongside them.

**Phase 3: the relationship layer.** Move-out with the deposit journey. Messages (the property's WhatsApp history, inside the app). Reviews and surveys. Rewards rebuilt around the tenant's record. Services.

**Phase 4: the doors.** White-label polish on top of the finished system, and the first open-for-all services.

If time pressure forces a cut, Rewards gives way first: tenants would miss it least, because dues, meals, attendance, complaints, and documents are the core, and rewards decorate it.

Migration itself is designed, not assumed: moving a tenant from the old app to the new one is a first impression happening a second time, and it gets the same care as onboarding.

## What could go wrong

**Trust debt transfers.** Tenants burned by the old app (receipts that never arrived, edits that did not save) will meet the new app with folded arms. The new app's first weeks must be flawless on exactly the moments that burned them. This is why grammar rules (money always right, receipts always delivered) are non-negotiable before any launch.

**The welcome fails again.** First-time setup confusion is the most documented problem in all our research (Seen in the field). If the new welcome is beautiful but still confusing, adoption dies in the same place twice. The welcome gets tested with real first-time users before anything else does.

**Personalization crosses the comfort line.** Somewhere between "it knows my city" and "it knows too much" is a line that differs by register, gender context, and age. Guessing wrong reads as creepy and, for minors, may break the law. The research kit tests the line before we build near it.

**Scope gravity.** Everything in TAR-00 is worth building, which is precisely the danger. The phases above are the defense: nothing in a later phase may delay the core loop.

**The overhaul becomes a repaint.** The strongest gravitational pull in any redesign is toward keeping existing structures because they exist. Standing rule: the current app is a first draft. Reuse is a decision made on merit, screen by screen, never a default.

## What success looks like

The success criteria and their order live in [TAR-00](TAR-00-vision-and-requirements.md), the single home for that list. Two operational notes belong here: the adoption baseline gets measured in the first month at pilot properties so targets rest on real numbers, and first-run completion is watched from day one, because the first minutes are where the old app lost people.

## Changelog

- 10 August 2026: first version, written under the frozen-backend constraint, critiqued and corrected against the codebase and stakeholder input across six revisions.
- 12 August 2026: rewritten. Plain language for the full audience. New-build strategy replaces the frozen-backend framing, so earlier backend workarounds are gone. Age joined the personalization signals. Build order reframed as phases of the new app with migration as a designed moment. Technical citations moved to the engineering folder.
