# TAR-03 · What Each Part of the App Must Become

**Read [TAR-00](TAR-00-vision-and-requirements.md) first.** This document walks through the app part by part. For each one it answers four questions: what should this become, why does it matter, what did the current app teach us, and what must we learn from real people before locking the design.

The current app is treated here as a first draft. It taught us real lessons and we thank it for them, but it sets no limits. Every part below is open to be imagined from scratch.

One companion to keep beside this document: for every feature a tenant would not ask for themselves (attendance, documents, entry and exit), how it earns willing participation lives in [TAR-05](TAR-05-how-features-earn-their-place.md).

How we mark what we know:
- **Verified** means we checked it ourselves and it is fact.
- **Seen in the field** means our team observed or heard it from real tenants and staff. True, but from a small sample.
- **Our read** means it is our professional judgment. Research exists to test these, and some will turn out wrong.

Technical defects of the current app live in a separate engineering register, not here. Correct money display, receipts that always arrive, text that never gets cut off: these are grammar rules the new app follows everywhere, and they get no further mention.

*Last updated 12 August 2026. Owner: Sanchay.*

---

## 1. Money

**What it becomes.** The most trusted screen in a tenant's phone. One clear answer to "what do I owe, is it paid, can I prove it." A rent receipt designed like a document worth keeping, because for an Indian tenant it genuinely is one: tax proof, address proof, police verification. Paying rent becomes the emotional peak of the month, acknowledged with a designed moment. Paying in cash gets the same dignity as paying by UPI.

**Why it matters.** Money is where trust is won or lost, and trust is the whole ladder: a tenant who trusts the app with rent will trust it with documents, services, and eventually a monthly fee. The receipt is also our quietest growth engine, because tenants already send receipts to employers and parents. A beautiful receipt travels.

**What the first draft taught us.**
- Tenants have been left without proof of payment when receipt delivery failed, and it colored their whole view of the app. *(Seen in the field)*
- The current payment flow buries "what do I owe" under three tabs and mixes three different reward systems no one can tell apart. *(Our read)*
- The moment after payment succeeds today tries to do four jobs at once and does none of them memorably. *(Verified)*

**What we must learn.** How often proof of payment is needed and where it goes. Whether tenants understand any of the current rewards. The real split between cash and online payment across property types. What a "paid" moment should feel like to someone who just parted with most of their salary.

---

## 2. Joining and first open

**What it becomes.** Arrival, not paperwork. The owner shows a code at move-in, the tenant opens the app, and the first thing they see is their own building's name and logo welcoming them. Setup asks for as little as possible, explains itself at every step, and can always be finished later. The waiting-for-approval moment shows the property's identity and a sense of progress, not a blank pending screen.

**Why it matters.** Adoption is the gate every other goal stands behind, and the field research is unambiguous: the first minutes decide everything. Existing users manage; new users struggle and leave. The owner is the channel, so the handover moment between owner and tenant is part of the product, not something that happens before it.

**What the first draft taught us.**
- The single most documented problem in all our research: first-time setup confused nearly every new user watched in the field. Buttons stayed disabled without explanation, steps did not look tappable, and finishing a step gave no feedback. *(Seen in the field)*
- Some tenants are forced through attendance setup before they can see anything else, a wall on the very first open. *(Verified)*
- An ordinary server hiccup at start-up can show a tenant a message implying they were evicted. *(Verified)* Few first impressions could damage trust more. *(Our read)*
- A flow inviting a tenant's landlord to join RentOk exists in the current app, but it is hidden from white-label users and its button does nothing. That is our warmest sales channel, wired to a dead end. *(Verified)*

**What we must learn.** Where exactly new tenants get stuck and give up, step by step. What owners actually say when they hand the app to a tenant. Whether move-in is calm enough for a guided first run, or whether tenants need a "later" path for everything.

---

## 3. Home

**What it becomes.** One glance answers "is anything wrong, what is next." A tenant's own facts lead the screen: their room, their dues countdown, tonight's dinner. A thin live strip carries what is happening right now: meal being served, gate closing soon. Below that, sections chosen and ordered for who this tenant is. A student's home leads with food and attendance. A professional's leads with rent and receipts. A sponsored tenant sees their home, never a nag about money that is not theirs to pay.

**Why it matters.** Home is where the personalization promise becomes visible, where the property's brand lives, and where daily habit is built or lost.

**What the first draft taught us.**
- Today's home is a fixed stack of a dozen sections, the same for every tenant, in an order the backend cannot change. *(Verified)* Nothing on it reads as the headline. *(Our read)*
- The announcements ring glows even when there is nothing new, so tenants learned to ignore it. The team itself flagged this. *(Seen in the field)*
- Several sections show stale or broken content on every open, including a task list that is always empty and a status card that can tell an incomplete profile it is complete. *(Verified)*

**What we must learn.** What each register actually checks daily. How far down today's home anyone scrolls. Which of our planned sections would earn a place on the first screen, and which are our own wishful thinking.

---

## 4. Complaints

**What it becomes.** Help that feels heard. A tenant describes the problem the way they would tell a friend, by tapping a chip or typing a sentence, and the app takes it from there. The confirmation names a human and sets an expectation: "We have told Rajesh, the electrician. Most fixes here happen within a day." Progress is visible without asking. The existing chat assistant becomes the front door, with a simple form as the fallback, never the other way round.

**Why it matters.** A complaint is the moment a tenant tests whether the app beats the old way: the paper register, the WhatsApp message, walking to the warden. Win this moment repeatedly and the app becomes the way things get done. Lose it once or twice and tenants stop reporting anything at all, which is exactly what long-term tenants told us they do.

**What the first draft taught us.**
- Tenants looked for complaints under Profile, not under Tickets. The words we use are not the words they think in. *(Seen in the field)*
- Filing today is a long form with dropdown menus, while the best-built screen in the entire current app is the chat assistant sitting right next to it. *(Verified)*
- Trust decays with history: tenants whose past complaints sat unresolved stop filing new ones. *(Seen in the field)*

**What we must learn.** Where complaints really get filed today, app versus WhatsApp versus in person. Whether chat-first filing feels faster or slower to real tenants, including ones uncomfortable typing. What update rhythm rebuilds trust after a bad experience.

---

## 5. Profile, documents, and the agreement

**What it becomes.** The safe place a tenant's renting life lives. Three clean layers: my home (room, rent, agreement, the emotional facts), my documents (each with an honest status: provided, pending, verified), and my account. The rental agreement becomes something the app treats as fully real: readable, downloadable, and explainable, with an assistant that answers "what does this clause actually mean" in plain words.

**Why it matters.** Paperwork is the highest-anxiety part of renting in India, and the research says it is where trust is won or lost. It is also the seed of something bigger: verified identity and documents that could one day travel with the tenant from property to property.

**What the first draft taught us.**
- Tenants reported edits that would not save and uploads that crashed, and the current app gives no feedback at all during document upload, so no one knows if anything worked. *(Seen in the field, and verified for the missing feedback)*
- Signing the agreement fails often enough that staff hear about it, and the signing screen itself asks people to sign sideways. *(Seen in the field; verified)*
- The profile screen tries to be a viewing screen and a very long editing form at once. *(Verified)*

**What we must learn.** Where document submission actually stalls, step by step. Whether tenants even know their agreement is in the app today. Which profile fields anyone ever updates after moving in, so the rest can get out of the way.

---

## 6. Moving out

**What it becomes.** A closure ritual that protects both sides. From the day notice is given, the deposit's journey is visible: held, inspected, deductions itemized with photos, refunded, with dates at every step. The move-in condition record is reframed as the tenant's own protection: timestamped photos that make an unfair deduction impossible. The goodbye includes something worth keeping: a record of their time in the home.

**Why it matters.** "Where is my deposit" is the number one exit complaint in Indian renting. A tenant who can say "this app got my deposit back" tells everyone they know. Move-out done right is not an ending; it is the strongest word-of-mouth moment we have, and it hands the tenant to the open-for-all door as they move to their next home.

**What the first draft taught us.**
- The current flow handles requests and approvals competently, and its status logic is worth keeping. *(Verified)*
- But after handover, the deposit simply vanishes from the app's story: we found no refund tracking anywhere in the flows. *(Our read)*
- The condition checklist reads as the owner's tool against the tenant, not the tenant's protection. Nothing explains whose side it is on. *(Our read)*

**What we must learn.** How often deposits are actually disputed and over what. Whether tenants see the checklist as protection or threat. What refund timeline owners will genuinely commit to showing.

---

## 7. Attendance

**What it becomes.** "Show up, get seen." Marking attendance returns a human acknowledgment, not a system log entry. History fills a calendar that feels like a streak, something maintained with quiet pride. Setup becomes warm, guided, skippable, and clear about why each permission is asked. The idea shifts from proving you are here to keeping your own record.

**Why it matters.** For students and hostel tenants this is the app's daily heartbeat, and daily use is what adoption means. It is also the most delicate feature we have: done carelessly it feels like surveillance, and for underage tenants it touches guardianship questions that deserve care, not defaults.

**What the first draft taught us.**
- Attendance setup is the wall most new users hit (see Joining, above). *(Seen in the field)*
- Marking today is a maze of states with three different color systems for the same statuses. *(Verified)*
- Nothing anywhere acknowledges the tenant who shows up day after day. *(Our read)*

**What we must learn.** How tenants actually feel about attendance: safety, surveillance, or indifference, and how that differs by register and by gender context. What parents expect to see, and what tenants are comfortable with parents seeing. The line is not ours to guess.

---

## 8. Food

**What it becomes.** The most checked screen of the day in properties with a mess. Tonight's menu presented with appetite: real photos when the kitchen shares them, warm illustration when not, and honest timing. Confirming meals feels communal: "43 of 60 are eating tonight." Rating food becomes feedback the kitchen actually sees, closing a loop tenants currently doubt exists.

**Why it matters.** Food is the second daily habit, and the most emotional everyday touchpoint in hostel life. Nobody has ever presented mess food with the care a food-delivery app gives a restaurant. The gap between how little effort this takes and how much tenants would feel it is the best ratio in the whole project.

**What the first draft taught us.**
- Menu timings shown to tenants have drifted from what the kitchen actually does, and tenants noticed. *(Seen in the field)*
- Today's menu is plain text on cards: the day's most anticipated information gets the least loving presentation in the app. *(Our read)*
- The QR-based meal check-in is solidly built and, in our judgment, worth carrying forward. *(Our read)*

**What we must learn.** Whether tenants check menus ahead or learn the rhythm by heart. Why meal confirmation gets skipped. Whether the "43 of 60 eating" idea reads as community or as pressure.

---

## 9. Rewards and offers

**What it becomes.** One honest system instead of three confusing ones. The spine is the tenant's own record: months of on-time rent building into something real, potentially including their credit score. Offers become genuinely local and genuinely relevant: scoped by city, property type, register, and age. Where nothing relevant is live, the section shrinks gracefully instead of showing everyone the same national catalog. Underage tenants see only an age-appropriate, curated set, with all behavioral targeting off, because that is both our standard and the law.

**Why it matters.** Rewards are how being a good tenant starts to feel like it counts for something. Done as a record rather than a carnival, this becomes the seed of the tenancy passport, one of the strongest long-term ideas we hold.

**What the first draft taught us.**
- Most tenants ignore the current rewards area entirely. Our own persona research says so. *(Seen in the field)*
- Three separate reward-like systems exist today and even we needed a diagram to tell them apart. *(Verified)*
- Every tenant in India currently sees the same offers, which reads as spam in any city where the offers do not apply. *(Verified)*

**What we must learn.** Whether anything here is wanted at all, register by register. Whether a rent record or credit-score angle motivates more than cashback. Which offer categories tenants would actually redeem, city by city.

---

## 10. Services

**What it becomes.** Booking help for your home without a phone call: cleaning, laundry, repairs, with clear slots, honest cancellation terms, and a rating that matters. Relevant mostly to co-living and professional tenants; invisible where a property offers none.

**What the first draft taught us.** The bones of browsing and booking exist. The overview leads with statistics no tenant asked for. Short-term tenants have no offerings sized for them. *(Verified; our read; seen in the field, respectively)*

**What we must learn.** Real booking volume where services are on. Which services tenants want by property type. Whether the barrier is discovery or doubt that the booking will actually happen.

---

## 11. Messages and updates

**What it becomes.** Everything the property says to a tenant, in one place inside the app: reminders, notices, the full history of the property's WhatsApp messages, each one leading somewhere useful when tapped. The property's existing WhatsApp channel keeps working; the app becomes the organized memory of it.

**Why it matters.** Today important messages drown in personal WhatsApp chats, and the team already knows announcements need to become real notifications. This section, done well, is also how the app earns its place next to WhatsApp instead of pretending WhatsApp does not exist.

**What the first draft taught us.** Notifications exist today, but tapping most of them does nothing at all. Announcements pose as always-new and tenants have learned the bluff. *(Verified; seen in the field)*

**What we must learn.** Which property messages tenants want pushed versus quietly available. When a tenant last lost an important property message in WhatsApp, and what it cost them.

---

## 12. Reviews and surveys

**What it becomes.** The property listening at the right moments, inside the app: quick pulse surveys, honest ratings, feedback that visibly reaches someone. The survey system already runs today over WhatsApp; this brings it home and gives owners a reason to love the app too.

**What we must learn.** Whether tenants answer more or less inside an app than on WhatsApp. What owners do with the results, and what would make acting on feedback visible to tenants, because feedback that disappears teaches people to stop giving it.

---

## 13. The white-label experience

**What it becomes.** A property brand's own app, indistinguishable from custom-built: their name and logo on the store, their colors applied safely everywhere, their tone in the welcome. Behind the scenes, one system: a brand color goes in, and a full, always-readable palette comes out, so no client choice can ever make the app illegible or make "paid" look like "overdue."

**What the first draft taught us.** Clients bought white-label for brand pride, and the sales pitch is easy. But owners struggled to supply color codes until the team began deriving palettes from logos, which is exactly the approach the new system formalizes. Meanwhile the current app applies client colors so unevenly that much of the promise silently fails. *(Seen in the field; verified)*

**What we must learn.** From owners: what would make them proudly demo their app during a property visit. What parts of the experience they most want to feel "theirs."

---

## 14. The open door

**What it becomes.** The version of the app for any tenant in India, whatever their landlord uses: agreements, receipts, deposit protection, and help around moving. This is a later phase, but the design and the service layer leave a place for it from day one, and the research kit already tests its two make-or-break questions with renters outside RentOk: is it valuable alone, and would they trust it without their landlord involved?

---

## How this document connects forward

Every "what we must learn" line above maps to specific questions in [TAR-04, the research kit](TAR-04-research-kit.md). After the first research round, each "our read" claim gets marked supported, challenged, or open, and this document gets updated rather than replaced. The design work per module then starts from "what it becomes," carrying the research verdicts with it.
