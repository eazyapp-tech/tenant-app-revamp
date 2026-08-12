# TAR-05 · How Features Earn Their Place

**Read [TAR-00](TAR-00-vision-and-requirements.md) first.** This document covers the layer between what each feature is ([TAR-03](TAR-03-what-each-part-must-become.md)) and how it looks ([TAR-02](TAR-02-design-language.md)): how every feature earns the tenant's willing participation. It exists because some of our most important features are ones tenants would never ask for, and the difference between an app that polices and an app that persuades is designed, not hoped for.

*Last updated 12 August 2026. Owner: Sanchay.*

---

## Every feature has two masters

Every feature serves the tenant, the property, or RentOk, and they differ in who carries the cost. Sorting the whole app this way makes the design problem visible:

| Quadrant | Examples | The design job |
|---|---|---|
| **Tenant-wanted** | Menu, receipts, complaints | Just deliver it beautifully. No persuasion needed. |
| **Mutual** | Payments, move-out checklist, the agreement | Show each side, on screen, how it protects them. |
| **Property-needed, tenant-carried** | Attendance, entry and exit, KYC and documents, food confirmation, profile completion, police verification | **The whole game.** The tenant experiences a chore or a watchful eye. The app must turn that into a willing trade. |
| **RentOk-wanted** | Rewards, offers, invitations | Earn genuinely or shrink gracefully. Never push. |

The third quadrant is where the current app quietly became a policeman. The new app is a diplomat, and this document is its instructions.

## How the three doors change the game

The same feature lives differently in each version of the app:

**Standard RentOk app.** The app speaks as a fair third party: it helps the tenant and the property stay in sync, and it is visibly on both sides.

**White-label app.** The voice changes hands: in a branded app, "we" is the property itself. A request to mark attendance carries the landlord's own voice, which is heavier but also more legitimate, because it is their house. Two things follow. First, this whole layer becomes a selling point: a white-label buyer is buying an app that lifts compliance by persuading, not nagging, and that protects their brand from ever shaming a tenant. Second, framings must survive customization: a persuasion that leans on a sibling feature (see tonight's mess count when you mark attendance) needs a fallback wherever that sibling is switched off.

**Open for all.** The property-needed quadrant does not exist here, because no property is in the loop. Nothing can be required of anyone; every feature is tenant-wanted or it dies. And the inversion is the strategy: the records that the burden features build in the other two doors (verified identity, rent history, the reliability streak) are the product itself in this door. A tenant who marked attendance and paid on time for two years in a PG walks into the open app already holding an asset.

Tenant types and property types tilt everything further: the same attendance feature needs different words in a strict girls' hostel (safety and family peace), a premium co-living (part of a keyless, tech-forward home), and it does not exist at all for a family flat. The personalization system already knows these attributes; positioning rides on it.

## The exchange rule

**Nothing in this app is ever naked compliance. Every give has a visible get, on the same screen.** Not an explanation of why the property needs something: a genuine trade the tenant can see and feel.

Two tests keep the rule honest:

- **The sincerity test.** The get must be something the tenant would miss if it were removed. A badge in exchange for your Aadhaar is not a trade, it is an insult with confetti. If we cannot name a real get, the feature stays a plain, brief, respectful ask, and we say why honestly.
- **The transparency rule.** Nothing watches quietly. Wherever the app records something about a tenant (attendance, entry, location during setup), the tenant can see exactly what the property sees. Whether this comforts or alarms is one of the things research tests before we lean on it.

## The framing library

For each feature in the burden quadrant: what the tenant gives, what they visibly get, and how the words shift by audience. These are starting positions for design, written to be tested, not decreed.

**Attendance.** *Gives:* a daily mark, sometimes a selfie and location. *Gets:* someone knows you are home safe (strongest for hostels and for parents); an unbroken record that becomes evidence of reliability, feeding the same record that our rewards and credit ideas build on; something back at the moment of marking (tonight's meal count, gate timing, a human acknowledgment); and fewer calls from home, because worried parents can see what they need without calling the warden. *Words to reach for:* checked in, home, your record. *Words to avoid:* monitor, track, report, mandatory.

**Entry and exit.** The strongest watchful-eye feeling in the app, and the sharpest split by property type. Where smart locks exist, the same tap that logs you opens the door: convenience leads, and the logging is disclosed plainly as its companion. Where the property is a strict hostel, safety and family peace lead. Gender context matters most here, and the research kit's rule applies: whether this reads as protection or surveillance belongs to the tenant, and we follow their words.

**KYC and documents.** *Gives:* papers, effort, and a little fear. *Gets:* "your file, in order": verified once, usable again and again; a faster agreement; a protected deposit; and in time, an identity that travels with you to your next home. Positioned as something the tenant owns, never something they submit. Every request explains itself in one plain sentence, and refusal or delay is always survivable.

**Food confirmation.** *Gives:* a daily yes or no. *Gets:* fresher food and less waste, said plainly; the communal count that makes a mess feel like a shared table; and a kitchen that visibly plans around real numbers. Positioned as choosing dinner, never as reporting attendance.

**Profile completion.** *Gives:* time and personal details. *Gets:* real unlocks, stated at the moment of asking: receipts that fill themselves, verification that goes faster, support that already knows your room. Progress is always honest. A completion meter that lies is worse than none, and the current app taught us that lesson the hard way.

**Police verification.** *Gives:* documents and anxiety. *Gets:* the app does the heavy lifting and explains each step in plain words; the tenant gets legal safety they did not have to figure out alone. Positioned as protection done for you, never as a demand.

**Reviews and surveys.** *Gives:* opinions and attention. *Gets:* visible consequences. "You told us the water pressure was bad. It was fixed on Tuesday." Feedback that disappears teaches tenants to stop giving it; every survey answer must be traceable to something the property did or a reason it could not.

**Paying on time.** *Gives:* discipline, sometimes at real cost. *Gets:* the streak, the record, and everything the record becomes: recognition, offers, and one day a credit story. Reminders are written as a helpful friend, never as a collection agency; the design assumes the tenant intends to pay.

## Gamification, with a bright line

Game mechanics are welcome here, and one line is never crossed: **compete on joy, never on compliance.**

- **Personal streaks, with mercy.** Attendance, on-time rent, and meal confirmations build personal streaks with small milestone celebrations. A broken streak is met kindly, never scolded, and can be mended within reason. The tone teacher here is the best habit apps: the app is on your side.
- **Collective wins, not individual rankings.** "The whole third floor checked in before ten" celebrates a group. A leaderboard ranking individual tenants by compliance would publicly grade people's private behavior, which is shame wearing a game costume, and in some property contexts it would be genuinely harmful. It never ships.
- **Competition lives where competition is fun.** Polls, food ratings, community games: opt-in, light, and never tied to anything the property requires.
- **The streaks feed the record.** Play and asset are the same thing: what the games build is the tenant's own reliability story, which is why they are worth playing.
- **Intensity is a dial that research sets.** How game-like any of this feels is tested with real tenants per register before it hardens. Some audiences will want the streak; some will want quiet acknowledgment; the kit already asks.

## Delight is the mechanism, not the garnish

The burden moments and the quiet screens are seen rarely, so by our own motion rule they are exactly where rich animation, illustration, and celebratory moments are allowed to spend generously. The permission explainer gets a warm animated illustration. Day thirty of a streak earns a small show. The empty state breathes. This is the language of the best modern Indian consumer apps, and it is precisely how a compliance moment stops feeling like compliance: the app that asks something of you is unmistakably the same app that delights you.

Frequency still governs: daily taps stay instant, and everything honors reduced-motion settings.

## What research must confirm

This document is a set of designed positions, not proven ones. The research kit already tests the load-bearing assumptions: how attendance actually feels by register and gender context, whether the record motivates more than cashback, where the personalization comfort line sits, whether family visibility is wanted or resented, and which of these trades tenants accept as fair. Where a framing fails research, the framing changes, not the verdict.

## Changelog

- 12 August 2026: first version. Written after the states-and-positioning discussion; incorporates the three-door analysis, the exchange rule with its sincerity and transparency tests, the framing library, the gamification bright line, and motion as the sweetener.
