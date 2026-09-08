# TAR-08 · The Structure Lock

**Read [TAR-00](TAR-00-vision-and-requirements.md) first.** This document is rung six of your ladder: the shape of the app, decided before anyone opens Figma. It says what the bottom bar is, what leads the home screen, and where every part of the app lives. [TAR-07](TAR-07-standard-app-feature-map.md) decided what exists in the standard door and [TAR-06](TAR-06-open-for-all-feature-map.md) decided what exists in the open door. This document decides where all of it sits and in what order a designer may touch it.

*First version, 9 September 2026. Owner: Sanchay. Written for the session on the 15th or 16th, to be read cold and argued with.*

**The page to read this on:** https://claude.ai/code/artifact/ef39894d-7857-4890-95ae-2ad782a113ee

---

## What this is for, and what it is asking you to do

This is a first cut, not a lock. It becomes the lock in the room on the 15th, after you have marked it up.

**What I need from you** is your red pen on the tree and a written answer to the eight questions. Not agreement. The parts I am least sure of are named as such where they sit, rather than defended.

**Where the product actually stands**, so the number is at the front rather than buried at the back. Of the thirty-nine marked sections in the tree, ten can be drawn today, five need one part settled before the rest is drawn, and twenty-four need their whole sequence settled first. All eleven of the flows that take over the screen need their sequence settled, without exception. That ratio is why the structure had to be locked before the design and not alongside it. Two designers put on this today would spend most of their time drawing screens whose steps are about to move.

**How to read it.** Budget an hour and a quarter: about an hour to read, fifteen minutes to write your answers to the eight.

1. **Three things that are true in production today.** Three findings from the shipped code that answer the first question for us.
2. **The bottom bar.** The five tabs, why those five, and what happens when a property has nothing to put in one of them.
3. **The home screen.** What leads it, stated as a rule rather than a preference.
4. **The tree**, in six parts. Every part of the app, where it sits, and up to three marks on each. The last of the six is everything deliberately left out, with a reason for each absence.
5. **The eight questions.** The only part you have to answer.
6. **What this asks the backend for.** The engineering roll-up. Skip it unless you want it.
7. **Before the 15th.** What to bring.

## How the marks work

Every part of the tree carries up to three marks. They are short on purpose and each one is a plain word rather than a code.

**Can a designer start?** This is your mark, sharpened into the decision it has to drive.

- **Draw it.** The sequence of steps is settled. A designer can start today and the drawing will survive.
- **Solve it first.** The sequence is not settled. Drawing now wastes the drawing, because the steps will move.

Every part gets one or the other. A part where the flow and the visuals are both broken still gets **Solve it first**, because that is the one that has to happen first. The mark sits on the section where a whole section is one or the other, and drops onto individual parts only where a section is mixed.

**Is there anything behind it?** The mark you did not ask for. Without it, a designer gets sent at a screen with no data under it, draws it beautifully, and waits four months.

- **today** means it ships in the current app and the service behind it exists.
- **partly** means something exists but not in the shape this needs, and the missing half is named.
- **new** means nothing like it exists and the service has to be built.

**Does the property control it?** Marked **switched** on any section whose existence a property decides from the manager app. Everything unmarked exists in every property, always. This is the mark that changes what a tenant actually sees, so it is the one to argue with hardest.

**On the doors.** There is deliberately no fourth mark. Doors one and two share this tree, because TAR-07 settles that the branded app is this same system with the brand's voice and its own limits, so it takes a difference note where it needs one and nothing where it does not. The open door's own surfaces are handled together in the last part rather than scattered through the tree as absences, which is question five.

## Three things that are true in production today

I checked these in the shipped code before writing anything else, because the first question in front of us has already been answered once by accident, and knowing that changes the answer.

**One. The bottom bar is already variable, and nobody decided that it should be.**

In the tenant app, `lib/application/bottom_navigation_provider.dart:17`: if the server sends more than two navigation items, the entire bar is built from the server's list, in the server's order, from a menu of eight possible entries (home, accounts, services, profile, tickets, attendance, offers, food). If the server sends two or fewer, the app falls back to four hardcoded tabs: Home, Account, Tickets, Profile.

So the variable bar is not a proposal. It shipped. What never shipped is any floor under it.

**Two. A property that runs a gate loses its complaints tab, and gets nothing in its place.**

In the backend, `src/controllers/others.ts:10439`: for a standard property that is not white-labelled, the server builds those same four tabs and then **overwrites the third one**. If the property has entry and exit settings, the third entry becomes a key called `gatepass`. If the property belongs to one of ten accounts on a hardcoded list (`src/helpers/constants.ts:14765`, eleven entries with one duplicated), it becomes Services.

The third tab is Tickets. And the app has never handled a `gatepass` key: searching the entire tenant package for it returns nothing, so the key falls through the switch and adds no tab at all.

So the real behaviour is worse than losing complaints. A property that runs a gate gives its tenants a **three-tab app**: Home, Accounts, Profile. Complaints is gone, the gate never arrives, and nobody decided any of it. TAR-07 names complaints as part of the trust floor that never switches off. It switches off, it switches off by accident, and it takes the slot with it.

**Three. Food and attendance can never reach the bar of a standard property.**

The same code path offers one replacement that works, Services, and one that renders as nothing, and only for the third slot. Food and Attendance are reachable in the bar only through a white-label configuration. TAR-00, the vision document, promoted both into the core set for one reason: they are the daily habits, and daily habit is what adoption is made of. The two features chosen because they bring students back every day cannot appear in the navigation of a standard RentOk property.

**What these three change.** The question is not whether the tab set should vary. It already does. The question is what is guaranteed underneath the variation, and today the answer is nothing. Everything below is an answer to that.

---

## The bottom bar

```
Home   ·   Money   ·   [ My PG ]   ·   Help   ·   Me
                          the one slot that changes
```

**Four never change. One changes.**

Home, Money, Help and Me sit in every RentOk tenant app on every phone, in that order, always. They are TAR-07's trust floor with Home in front of it: money, complaints, documents and the tenant's own profile, the four things TAR-07 says exist in every property's app because an app whose landlord can hide your receipts is not a trustworthy app.

I did not pick them from that list. I walked eight lives first and the four came out the other end.

- A nineteen-year-old in a Kota girls' hostel, whose father pays.
- A working professional in a Bengaluru PG bed, paying their own rent.
- A family of four in a Gurugram flat, inside a housing society.
- Three bachelors sharing a flat in Pune.
- A resident of a premium co-living.
- A seventy-one-year-old in a senior residence, whose daughter pays.
- A blue-collar tenant paying cash from a budget phone.
- A company-sponsored tenant on a three-month serviced stay.

All eight needed Home, Help and Me. Six of them needed Money often, and the other two, the Kota student whose father pays and the sponsored tenant whose company pays, still need it for the receipt and the record even though they never pay a bill, which is exactly why TAR-07 puts it on the floor that never switches off.

The fifth is where they part company:

- The hostel student and the PG tenant want food and the gate.
- The senior resident wants meals and the events calendar.
- The family in the flat wants its papers, its bills and its help at the gate.
- The three bachelors want their shares, their splits and their chores.
- The co-living resident wants events, amenities and the concierge.
- The serviced stay wants extensions and housekeeping.

Food comes closest and it serves three of the eight. Nothing serves five. That is the whole finding, and it is why one slot has to move.

### The third slot is the property's own

Its contents come from what the property actually runs, and its label is the home rather than the feature: **My PG**, **My Flat**, **My Hostel**, or in a white-label app the brand's own word for the place.

- In a hostel: food, presence, the gate, the notice board, outpass.
- In a co-living: events, community, and what is coming to your home.
- In a bachelor flat: shares, chores, the split ledger, the people on the agreement.
- In a family flat: house facts, the society's notices, and the household's own help arriving at the gate.
- In an institute property: all of the hostel's, plus the academic calendar.

Two things a reader might expect here and will not find. The directory of who to call sits in Help, because reaching a human is trust floor and cannot depend on a tab that might be absent. Booking a service or an amenity sits in the hub, which is Part C and has its reasons there.

Naming it for the home rather than the feature does a second job. TAR-00 says the property's logo and name lead the app, not RentOk's. Today a property logo does appear, but only in the property switcher and the account chooser, two screens a tenant visits almost never. It is stored at login and then fetched and thrown away without being drawn: `profile_my_renting_info_section_card.dart:23` calls `PrefsUtils.getPgLogo();` on a line of its own and discards what comes back. The promise is kept nowhere a tenant actually looks. Here it is carried by a permanent tab that belongs to the place they live.

**Why the middle.** It is the easiest place on the bar for a thumb, and it means only Help moves position when the tab is absent. Home and Money are always first and second. Me is always last.

### When a property has nothing to put in it, the bar is four

The tab is never created empty. There is no empty tab that exists to explain why it is empty, which was my earlier answer and was the worse one. A tenant should never meet a tab that exists to apologise.

This is the honest answer to the question you asked, which was what a tab does when the property switches off everything inside it. It does not sit there hollow. It is not in the bar.

### Three rules that make a changing slot safe

**Nothing is reachable only from the property's tab.** Everything a property runs is also in one index that is always in the same place, inside Me, complete and in the same order for everyone. TAR-00 already scoped this as Feature navigation, one of the ten core sections. It is what makes a variable bar honest rather than a hiding place, and it is the reason I am comfortable with the bar moving at all.

**The bar never changes silently.** When an owner switches food on in March, the tenant gets one card on Home saying so, once. A bar that rearranges under someone's thumb overnight reads as a bug, and a tenant who thinks the app is broken does not come back to check.

**The property's tab can never evict a fixed one.** This is the defect shipping today, written as a rule so it cannot ship again.

### The labels, and why they are not the module names

The tree below uses TAR-07's own names for everything. The tab labels are different on purpose, and this is a decision worth arguing with.

**Help**, not Tickets or Complaints. [TAR-03](TAR-03-what-each-part-must-become.md), the module-by-module review of what the current app taught us, records that tenants looked for complaints under Profile and not under Tickets: the words we use are not the words they think in. Help is the word a person uses at the moment something is wrong.

**Me**, not Profile. What sits there is not a set of profile fields. It is the tenant's home, their documents, their record, their passport, their family links and their tenancy. Profile undersells all of it.

**Money**, not Accounts. Accounts is a banking word. Money is what a tenant calls it.

---

## The home screen

You asked whether the money leads or the day leads. The answer is the day, and I want to state it as a rule rather than a preference, because a flat preference breaks for a family in a flat who has no day.

**Home is four blocks, in this order.**

1. **What is happening right now.** A thin live strip: the meal being served, the gate closing in twenty minutes, a poll ending tonight, a person waiting on you.
2. **What changed since you last looked.** The complaint that moved, the notice that went up, the deposit that landed, the parent who paid.
3. **This home's rhythm.** Tonight's dinner and today's mark in a hostel. Nothing at all in a flat.
4. **Money, sized to what is true.** A quiet line when nothing is due. A card when something is.

**The rule produces both behaviours with no exception written.** In a hostel the day fills the screen and money is a calm line saying the fees are paid through March. In a family flat there is no rhythm block at all, so money is what remains and it leads by itself. I did not have to write a family-flat special case, and that is the evidence the rule is the right shape rather than a compromise between two answers.

**Money is never hunted for and never shouts when there is nothing to shout about.** That is the second half of the answer to your question. It is always on the first screen and always in the second tab. Its size is set by whether anything is actually due, which also settles TAR-07's sponsored tenant, whose company pays and who therefore sees a home and never a nag about money that is not theirs.

**And one number explains why the day leads at all.** Across roughly four hundred thousand tenants, between six and nine in every hundred open the app in a month. That is a monthly-app number. What makes an app daily is not money and it is not food specifically. It is that something changed since you last looked, which is why that is block two and not block four.

**Deliberately absent from Home:** the marketing banner slots. TAR-07 bans them by name, and the current app has two of them.

---

# The tree

Six parts. What happens before the tabs exist, the five tabs themselves, the hub that is not a tab, the flows that take over the whole screen, the index that guarantees nothing is hidden, and what is deliberately outside the tree.

---

## Part A · Before the tabs

The app meets a person at whatever stage they are already in, which TAR-07 names as looking, booked, living here, and moved on. Everything in this part happens before the tabbed app appears.

### A0 · Before there is a tenancy

**Solve it first.** TAR-07's first commitment is one app carrying the whole journey natively, rather than a marketplace website handing off to a joining flow handing off to a web check-in. None of this exists in the app today. The web journeys keep running for anyone who has not installed it, and a person who used them simply arrives further along.

- Arriving: from the brand's own website, from RentOk's marketplace, or because an owner shared a link (new)
- Who you are, the light step early on, so the journey speaks to a student, a professional, a family or a group correctly from the first screen. This is also where a renter's record begins, before any tenancy exists. (new)
- Seeing the place: rooms, sharing options, rent and terms, photos and video, location and the commute (new)
- Booking a visit, with a type, a date and a time, plus directions, what to bring, who to ask for, and a short list of things worth checking while there, because a renter who inspects well is a renter protected well (new)
- Rescheduling or cancelling a visit, without penalty games (new)
- Reserving: a token amount holds the room, the receipt is immediate, and the terms of the token are stated in plain words before paying, including exactly what happens if plans change (new)
- Changing a booking: a different room, a later move-in date, or a cancellation, each with its consequences stated up front (new)
- Applying as a group: one home, several people, one shared application, each person with their own entry (new)
- The lead who never moves in: their profile stays in their own account, positioned honestly as their renting profile saved for their next search and deletable in one tap, with sensitive documents expiring from our side on a stated schedule (new)

**Not here:** browsing any property other than this one. The short reason is that the landlord's own app will not advertise his competitors. The last part of this document carries the full list of what sits deliberately outside the tree.

### A1 · The entrance

**Solve it first.** TAR-03 records this as the single most documented problem in all our research: first-time setup confused nearly every new user watched in the field, buttons stayed disabled without explanation, and finishing a step gave no feedback. The steps themselves are wrong, not just their drawing.

- Phone number and the one-time code (today)
- The seven destinations in the routing switch: the login screen, home, a forced update, waiting for approval, a moved-out screen, one brand's own splash, and a no-network retry. Boot itself only ever reaches five of them. (today)
- The moved-out screen is reached from the login path, and that is the defect. Any non-success answer from the status check clears the whole session and shows a tenant a screen saying they were evicted. An ordinary server error costs a tenant their login and tells them they have been thrown out of their home. (today)
- What happens after login: a new tenant, an existing one, or one who needs a self-invite, and the picker when a single phone number has more than one tenancy (today)
- Joining by the code or poster the owner hands over at move-in (partly: joining by code works, the designed handover artifact does not exist)
- Joining by the property's own app code (today)
- The join request, and the screen that waits on a human being rather than a spinner (partly: the waiting screen exists and shows nothing about who is being waited for)
- Arriving from the web journey with half of it already done (new)
- Arriving from the old app on migration day, with everything already in place, and one clear moment showing what is new (new)
- The two walls that stand in front of the app today, and come down. Identity checks can block access to the rest of the app until they are cleared, and attendance setup can be forced before a tenant sees anything at all. TAR-07 is explicit that nothing stands in front of the welcome: no walls, no forced setup, no dead ends. Both walls ship today. (today, and being removed rather than redesigned)

### A2 · Joining, before the keys

**Solve it first.** The order of these steps is a property decision in TAR-07, which means the sequence is a variable, which means it has to be designed as a sequence before any one screen is drawn.

- Who you are: the light step that lets the journey speak to a student, a professional, a family or a group correctly from the first screen (new)
- Identity check (partly: document upload and verification status exist, the check itself is not a designed flow)
- Filling in your profile (today)
- The renting terms in plain words: rent, deposit, notice period, lock-in, house rules (new)
- The property's deposit deduction rules, shown here, on day minus three (new). TAR-07 calls this the single choice that kills India's worst renting dispute at its root, because there are no surprise rules at the exit if every rule was visible at the entrance.
- The agreement, previewed and signed, with every person it names signing their own part (partly: viewing, signing and downloading exist for one signer; several signers do not)
- Setting up autopay (partly: exists but hands the tenant off to a portal outside the app)
- Starting the move-in record early, where the property prefers it (partly: the signed move-in document already shows to the tenant in profile details, right beside the move-out one, and its data reuses the move-out checklist's shape. What does not exist is the capture flow, walking the room and marking condition, which move-out has and move-in does not.)
- The manager-assisted path: the manager fills, the tenant confirms with a code, and the record produced is identical (new on the tenant side, where nothing manager-assisted exists today)

### A3 · Day one

**Solve it first.** Almost nothing here exists today, and this is the moment TAR-00 says decides adoption.

- The welcome, where the property's own name and logo lead (new. A property logo renders today only in the property switcher and the account chooser, never on the first open.)
- Whatever is already finished simply being there, and whatever is left offered warmly and skippably (new)
- The move-in record: walking the room with the camera, items confirmed, condition noted, both sides signing (partly: the finished document exists, the walk does not)
- Meeting the home: tonight's dinner, the gate hours, who to call when something breaks (new)
- The house facts card: the wifi password, water timings, the garbage schedule, quiet hours, parking, and in a housing society its own rules (new, and nothing resembling it exists in the code)

---

## Part B · The five tabs

### Tab 1 · Home

**Solve it first.** The four blocks are a new composition and the ordering rule is new. There is no version of this to draw from.

- The live strip: what is happening right now (new)
- What changed since you last looked (new)
- This home's rhythm: tonight's dinner, today's mark, the gate (new)
- Money, sized to what is due (partly: the dues snapshot exists, the sizing rule does not)
- The property's pinned notice, and the acknowledgment on a critical one (partly: an announcements banner exists, and it glows even when there is nothing new, so tenants learned to ignore it)
- Waiting on a person: a join request with the owner, a complaint with the electrician, a deposit with the accounts desk (new)
- One card, once, when the property switches something on and the bar changes (new)

**Deliberately absent:** the two marketing banner slots that exist today, the always-empty pending tasks list, and the status card that can tell an incomplete profile it is complete. All three are in the current app and all three are named in TAR-07's not-building list or TAR-03's defects.

### Tab 2 · Money

TAR-07 says the money surface answers three questions rather than one: what happened, what stands right now, and what is coming. The tab follows TAR-07's own section order, which puts what stands right now first, because that is the question a tenant opens the tab to ask.

#### B2.1 · What stands right now

**Draw it** for the parts that ship today. **Solve it first** for shares and the billing calendar, which change the shape of every screen under them.

- What you owe, itemised by name, never one grey number (today)
- Charges that repeat: rent, food, maintenance, laundry, and the packages this property bills (today)
- Charges that follow use rather than the calendar: a prepaid meter recharged when it runs low, a meter read at month end (partly: the prepaid meter balance and its recharge link exist)
- One-off charges: a service booked, a dish ordered, a guest who stayed the weekend, something broken and owned up to (partly: these arrive as dues, without the story of what each one was)
- Your own share, alongside the whole picture, in a shared home (new). **Solve it first.**
- The billing calendar that matches the property: monthly for a working PG, by semester or year in instalments for a college hostel, by the week or the day for a serviced stay, and no calendar at all for usage charges. Pro-rated honestly whenever a stay, a plan or a room changes mid-cycle. (new) **Solve it first.**
- Money you hold with the property: the deposit, advance money and caution money, each a living balance with its full story (partly: a security deposit view exists and shows a number, not a story)
- Where the property uses a deposit bond partner, the bond's journey shown in the same place as the deposit's (new)
- Money you have earned, with its expiry in plain sight: owner discounts and cashback (today). Referral credits (new), because no referral system ships.
- Every refund and its journey (partly, and worth stating precisely because two of our own documents disagree here). Refunds already reach the app as records, carrying date, reason, mode, who paid them out and photographs. What does not exist is the journey: the property's own promised timeline, a countdown against it, and the deposit's path from held to inspected to agreed to landed. Both documents were right about different halves.
- Electricity, handled with care: the balance, the warning early enough to act, a grace period, and an emergency top-up so nobody is left in a dark room at eleven at night (partly: balance and recharge exist, the warning, the grace and the top-up do not)

#### B2.2 · Paying

**Draw it.** This is the best-established flow in the current app and its sequence is settled.

- The apps a tenant already has on their phone (today)
- Card, including rent on a credit card (today)
- Netbanking (today)
- Cash, handed over against a one-time code to a named staff member (today). Paying against the property's own payment QR does not ship (new), and neither does the streak it should earn (new). The rule is the point: cash earns the identical receipt, the identical record entry and the identical streak credit. Paying in cash is a payment, not a confession.
- Autopay, its state, next date and amount changeable inside the app (partly: today it hands off to an outside portal) **Solve it first.**
- Paying for someone else, and sending a payment link (today)
- Rent day as a moment: paying on time acknowledged the day it happens, within the standing rule that it is designed and dignified and never a slot machine (new)

#### B2.3 · What happened

**Draw it.**

- Every payment in one running statement (today)
- The receipt, per person in a shared home, tax-ready, address-proof-ready, and good enough to send (partly: receipts generate and download today, per person does not exist). TAR-03 calls the receipt our quietest growth engine, because tenants already send receipts to employers and parents.
- The invoice, where billing needs one, with tax details (new)
- A whole year in one view, for the month when an employer or a tax return asks for it (new)
- The streak of months paid on time, accumulating into the record (new)

#### B2.4 · What is coming

**Solve it first.** None of it exists and it is a new way of using data the app already holds.

- What next month will probably cost, from the rent date, the packages, the usual electricity and the services booked (new)
- The warning before the picture gets uncomfortable (new)
- Cash spending entered by hand (new)
- Budgets built from the real repeating charges rather than typed in from scratch (new)
- The flat's shared expenses folded in (new)

#### B2.5 · The household's other bills

**Solve it first.** (new for wifi, cable and recharges. The prepaid electricity meter's balance and recharge already ship and are listed above under what you owe; what is new is every other household bill sitting beside the rent.) TAR-07's reason is that it gives every kind of tenant, including the family in a flat, a reason to open the app more than once a month, and it is one of the things the monthly platform fee is meant to buy.

---

### Tab 3 · The property's tab

**This is the one tab that changes.** Every section below is **switched**: the property decides whether it exists. The tab is labelled for the place the tenant lives, and if a property runs none of this, the tab is not in the bar and the tenant has four tabs.

TAR-07's rule holds over all of it: what a property switches on is itself a signal, and what it turns on tells the app what kind of home this is.

#### B3.1 · Food · switched

**Draw it** for the parts that ship. **Solve it first** for the vote and the canteen.

- Tonight, with honest timing (today, and timings shown to tenants have drifted from what the kitchen actually does, which tenants noticed)
- The week ahead (today)
- Choosing dinner, with the count of who else is eating (partly: meal confirmation ships, the communal count does not). Framed as choosing dinner, never as reporting attendance.
- Pre-selecting the week, which gives the kitchen true numbers days early (new)
- The live meal and the QR plate check-in (today, and TAR-03 calls it solidly built and worth carrying forward)
- Rating the meal, and seeing the kitchen answer (partly: rating ships, the kitchen answering does not)
- The menu vote (new) **Solve it first.** The one feature where community and food feed each other daily.
- The cafe or canteen: ordering and paying in the same place (new) **Solve it first.**

#### B3.2 · Presence · switched

**Solve it first, all of it.** TAR-03 records marking today as a maze of states with three different colour systems for the same statuses, and TAR-05, the document on how features earn their place, puts attendance in the group of features a tenant would never ask for, where the whole design job is turning a chore into a willing trade. The order of the steps, and what the tenant visibly gets back for marking their day, both have to be settled before anything is drawn.

TAR-07's design decision to preserve: residents marking their day, the gate recording comings and goings, a visitor arriving, a friend staying the night and a parcel waiting at reception are the same question, and they are one system rather than four logs that happen to sit together.

- Marking your day, and getting a human acknowledgment rather than a log entry (today for the marking, new for the acknowledgment. Nothing anywhere acknowledges the tenant who shows up day after day.)
- The calendar that feels like a streak, kept with pride, broken with mercy, mended within reason (partly: the history calendar and its monthly percentage exist)
- Setup, warm and guided and clear about why each permission is asked (partly, and today this is a wall: some tenants are forced through attendance setup before they can see anything else, on the very first open)
- The gate: comings and goings (partly: entry and exit settings exist on the property, the tenant's own view of their day does not)
- Late entry, with the option to inform family (partly: the late check-in request ships, telling the family does not)
- Leave and outpass over several days, with guardian approval where the tenant is a minor, the gate and the kitchen informed, the food component adjusted, and the room held (partly: marking leave and the pending requests tab exist; the rest does not)
- The property's curfew rules, stated plainly (new)
- What the property sees, which is exactly what you see (new). TAR-07 allows no configuration in which the property watches and the tenant cannot see.
- The smart lock, where the property installs one: the tap that opens the door is the tap that records presence (new)
- Where the property already runs a QR or fingerprint gate, presence uses that rather than asking the tenant to mark twice (new)

#### B3.3 · Guests, visitors and deliveries · switched

**Solve it first.**

- Pre-approving a visitor so a friend is expected at the gate rather than interrogated (partly: hosting a friend or guest exists as an entry point)
- A regular guest remembered rather than re-explained: the partner who visits every weekend, the cousin who comes monthly (new)
- An overnight stay, requested where the property requires it and priced in advance where the property charges for it (new)
- Parcels announcing themselves instead of being a phone call to the guard (new, nothing in the code)
- The household's own people in a flat or family home: the cook, the maid, the tutor, arriving and leaving with a notification, their month's attendance ready when it is time to settle up (new). This is the one part of presence that a family in a flat actually wants, and it is why the family flat's tab is not empty.

#### B3.4 · The notice board · switched

**Solve it first.**

- Pinned and categorised, with an archive that never lies about newness (partly: an announcements banner and a stories viewer exist, and the ring glows when there is nothing new, which the team itself flagged)
- Critical notices carrying an acknowledgment, and ordinary ones carrying none, because a notice board must never become a watching feature (new)
- The institute shape: circulars, schedules, exam-season notices, the sheets a warden tapes to the wall today, dated and findable forever (new)
- My own acknowledgment history (new)

#### B3.5 · The house facts card · switched

**Draw it.** (new) The wifi password, water timings, the garbage schedule, quiet hours, parking rules, and in a housing society its own rules and move-in permissions. Small, always current, and TAR-07's judgment is that it will be one of the most opened things in the app. Nothing resembling it exists in the code today.

#### B3.6 · Community · switched, on by default in PGs, co-livings, hostels and senior residences, off in family flats

**Solve it first, all of it.** (all new) Most of this is on the flexible list in TAR-00, the vision document, which means tenants validate it before we build it, so nothing here should be drawn before the research round reports. Two things on this list are not on it: chores and the report-and-block plumbing. Chores needs its own call on whether it waits for research. Report and block is not optional at all, because a resident space without it is unsafe from the first day.

The one thing that is settled: every member is a verified resident of this building, which is the entire safety model, and the reason no messaging app can offer this.

- The residents' own space: lost and found, borrow a ladder, selling a cycle, planning a Sunday (new)
- Report and block, with the manager as a moderator of last resort (new)
- Polls, in two kinds: the property's own, such as the menu vote or an amenity decision, and the residents' own, such as movie night or the temperature of the air conditioning (new)
- Buying and selling between verified residents, with its natural moment at move-out (new)
- Events, property-hosted and resident-created with approval, and in a senior residence a calendar the linked family can see (new)
- Chores, as shared rotation lists for groups and shared rooms (new)
- A personal to-do list, which belongs to the tenant alone. The app never generates tasks onto it, and TAR-07 bans app-generated pending tasks by name. (new)

#### B3.7 · The people on your agreement · switched, present wherever a tenancy has more than one person

**Solve it first, all of it.** (all new) TAR-07 is explicit that this is not a feature but a thread running through every moment, and that everyone on the agreement is a full user of the app rather than a viewing window into somebody else's.

- Each person with their own login and their own app (new)
- Shares that are explicit from the agreement onward: rent share, deposit share, and each person's slice of every package the property bills (new)
- The ledger that settles the others to whoever paid the property (new)
- Splitting the things the property never bills, with each expense carrying its own participants, because the flatmate who never eats the tiffin is not in the tiffin split (new)
- A member leaving: the vacancy visible to the group, the replacement found through their circles or through the owner's referral bounty, the newcomer walking the full joining journey, the agreement re-signed by all parties, and the departing member's deposit share settling person to person (new)
- Dependents, who follow a request path: a tenant fills in the details, and the other core tenants and the manager approve from their own sides (new)
- Every party the agreement names gets their own claim, not just co-tenants: a guarantor, and a guardian where someone is a minor. Each logs in with their own phone, finds their entry waiting, verifies themselves and signs their own part. Nobody signs for anybody else. (new)

**Deliberately absent:** any point-of-contact role. TAR-07 bans it by name. The property talks to the tenancy, not to one designated tenant on behalf of silent others.

#### B3.8 · The academic calendar · switched, institute and college properties only

**Solve it first.** (all new) Term billing and its instalments, closures the app already knows about, vacation holds, luggage storage, and the return date.

#### B3.9 · What is coming to your home · switched

**Draw it.** (new) Where the property schedules recurring work, housekeeping, deep cleaning or pest control, the tenant sees what is coming and when. Read-only and calm. No surprises at the door.

---

### Tab 4 · Help

One job: **reach someone.** A human is involved in all four things in this tab. Something is wrong and needs fixing, a question needs answering, an opinion needs to land somewhere, or you need to know who to call.

Booking a service is not in here, and the reason is in Part C, the hub. Asking for help and choosing to buy something are opposite feelings, and a tenant who opens this tab because their geyser is broken should not land on a shelf of tiffin vendors.

#### B4.1 · Something is wrong

**Draw it** for filing and the list. **Solve it first** for escalation, reopening and the shared complaint.

- Filing it by describing it, by tapping a chip or typing a sentence (today, and TAR-03 judges the chat assistant the best-built screen in the entire current app, sitting right next to a long form with dropdown menus). The chat is the front door and the form is the fallback, never the other way round.
- The confirmation that names a human being and sets an honest expectation (partly: a complaint can carry an assigned staff member, the named confirmation and the time promise do not exist)
- The plain list of all my complaints, open and closed, with status, who holds each one and how long it has been there, searchable and filterable (today). Chat is the fastest way in and the list is how people keep track, and neither hides behind the other.
- The escalation path: who has it now, what happens if it stalls, and the one tap that raises it (partly: a WhatsApp escalation exists) **Solve it first.**
- A reopened problem carrying its past (new: there is no reopen today) **Solve it first.** TAR-03 records that tenants whose past complaints sat unresolved stop filing new ones, which means history is the design problem here.
- The shared complaint that neighbours join, so a building-wide water or lift problem is one issue rather than fifteen duplicate tickets and fifteen separate silences (new) **Solve it first.** Filing stays private by default; joining a shared issue is the social act.
- Rating a resolved complaint (today)
- Repairs that cost money, carrying their money story: who pays already known from the declared terms, and where the tenant paid for something that was the property's duty, the reimbursement or rent-adjustment path visible and trackable (new) **Solve it first.**

#### B4.2 · The conversation

**Solve it first.** (partly: a notification feed ships and leads nowhere; the conversation itself does not exist at all) TAR-07 is explicit that the conversation itself is native: searchable, linked to the thing being discussed, surviving a lost phone, and never competing with the tenant's personal chats for attention.

- Talking directly to the property team: a question about a bill, a request, a photo of a leaking tap, an answer from a named person (new. There is no in-app messaging today; what exists is the property's WhatsApp number, used outside the app.)
- The notification feed, and the bell (today, and tapping most notifications does nothing at all, so tenants learned they lead nowhere)
- Everything the property has sent me on **any** channel in one place, the app's own notifications and the WhatsApp thread together, each item leading to the screen where I act on it (partly: the WhatsApp message store exists and is populated, and every reader of it today is on the manager side, which is already filed with engineering as the ask for a tenant-side read of the message log)
- Which channels reach me, for everything that is not transactional (new)

#### B4.3 · Feedback

**Solve it first.** (partly: the survey and review system already runs and reaches tenants over WhatsApp, and nothing of it is in the app. An endpoint exists, and its shape and campaign coverage are unverified, which is already filed with engineering as a first task of this work.)

- The property asking: quick surveys and ratings at the right moments (partly: it runs on WhatsApp, not in the app)
- The tenant starting it themselves, choosing what it is about: food, cleanliness, staff, safety, the building (new)
- The reply, the close, and reopening it if the answer did not hold (new)
- Feedback becoming a complaint, carrying its whole history, so nobody retypes anything and nothing restarts at zero (new)

#### B4.4 · The directory

**Draw it.** The sequence is trivial. The sort is the whole design.

This sits here, and it is not switched, and both of those are changes I am making rather than carrying from TAR-07. Being able to reach a human about the place you live is trust floor. A landlord does not get to switch off the phone numbers any more than he gets to hide your receipts. What varies is how rich it is, from a manager and an owner in a small property up to a warden and a safety helpline in a hostel, and every property has at least one person to call, so it is never empty.

Organised by need, not as an organisation chart.

- Something broke: who fixes it (partly: a support contact exists, the sort by need does not)
- Late at night: the warden (new)
- Money: the manager, the owner (today)
- My roommates and flatmates, by their own choice, names first and more by mutual consent (new. A roommate screen exists today and shows a "coming soon" message when tapped.)
- The property team and their roles (partly: one support contact, no roles)
- Calls and messages routed through the app, so staff personal numbers stay private, which protects the staff as much as the tenants (new)
- In hostels, the safety layer the law expects, in plain sight: the anti-ragging helpline and emergency contacts (new)
- Trusted household help, where neighbours in the same building have vouched for them (new)

---

### Tab 5 · Me

TAR-07's three clean layers, plus the record that grows and the requests a tenant makes about their own tenancy.

#### B5.1 · My home

**Draw it.** The emotional centre of the tab.

- Room, rent, agreement, tenancy facts, move-in date, how long I have been here (today)
- More than one tenancy, changed here (today)

#### B5.2 · My documents

**Draw it** for what ships. **Solve it first** for the honest statuses and for knowing whether an upload worked.

- The agreement, readable and downloadable (today)
- The clause explainer: what does this actually mean, in plain words, any time (new)
- Receipts (today). Invoices, where billing needs one, do not ship (new).
- Verification certificates (today)
- The move-in record and the move-out record, side by side (partly, and closer than it looks: both documents already sit next to each other on profile details. What is missing is the move-in capture flow behind the first one.)
- Police verification as its own feature, not a buried checkbox: the app doing the heavy lifting and explaining each step, handing the tenant legal safety they did not have to figure out alone (today for the status, new for the explaining)
- Background verification, with what is being checked, why, what the result means, and the tenant's own copy of the outcome (partly: the status and an explainer exist)
- Honest statuses everywhere. A completion meter that lies is worse than none, and the current app has one that can tell an incomplete profile it is complete, because the home screen's profile card assigns the incomplete flag straight to the complete flag without inverting it. (partly: the statuses exist and one of them is wrong) **Solve it first.**
- Uploading a document and knowing whether it worked (partly: uploading, cropping and the per-document status all ship, and the app gives no feedback at all during upload, so nobody knows if anything happened) **Solve it first.**

#### B5.3 · My personal details

**Solve it first.** (today, and it is the largest surface in the current profile: demographics, family and guardian, previous and permanent address, education, employment, banking, and social and professional links.) The sequence needs solving because TAR-03 records the current screen trying to be a viewing screen and a very long editing form at the same time, and because we do not yet know which of these fields anyone ever updates after moving in, which is a research question the round already asks.

- Viewing what the property holds about me (today)
- Changing it, where I am allowed to (today)
- Profile Lock (today, and it is a live property-controlled behaviour nobody has designed). Where the property switches it on, management is the gatekeeper of profile changes and the tenant requests rather than edits. It already drives the locked state on every document card and edit field. **switched.**
- What each field is for, and what it unlocks, said at the moment of asking (new)

#### B5.4 · My record

**Solve it first, all of it.** This is the bridge between this door and the open one, and it is what every reward is calculated from, so its rules matter more than its screens.

- Months on time, verifications, room history, presence summary (new)
- What the property contributed, recorded as things that happened with a date and a source, never as a judgment about the tenant (new)
- Seeing and contesting an entry before it can ever travel anywhere (new)
- What never enters the record: complaint counts, because asking for help must never cost a tenant their reputation, and how often somebody moved, because the score measures how you rented and never how long you stayed (new)
- One rewards system, built on the record (partly, and this is a merge rather than a build: three separate reward-like systems exist today, the membership rewards, the general offers and the scratch-card credits, and TAR-03 records that even we needed a diagram to tell them apart) **Solve it first.**
- The credit story: rent reported to the credit bureaus with consent, and a free credit-score check inside the app (new)

#### B5.5 · The passport

**Solve it first.** (new) Verified identity, rent history and tenancy facts, gathered as a side effect of simply living well. In this door it accumulates quietly. In the open door it is the product, which is why its shape is decided in [TAR-06](TAR-06-open-for-all-feature-map.md) and only carried here.

#### B5.6 · The memory

**Draw it.** (new) A year in this room. The photos of the move-in day. The goodbye artifact when the time comes. Private first, shown to others only by the tenant's own choice, and feeding the passport only by choice.

#### B5.7 · The activity log

**Draw it.** (new) Everything that happened on your tenancy in one trail: payments, requests, documents, consents, agreement events. It is the transparency rule in ledger form and it doubles as the tenant's protection in any dispute.

#### B5.8 · My family's access

**Solve it first.** (partly: the parent app itself ships, and the tenant-side flow for creating and scoping the link does not) **switched**: TAR-07 lists the Family Window among the things a property turns on, off or limits. The parent app is a separate product and its own surfaces are not in this tree. What stays here is the tenant's side of the link, and it stays here because TAR-07 makes the adult tenant the gatekeeper of their own tenancy.

- Adding my parents, both of them, each verifying their own identity before they can log in (partly: the parent app ships, this flow does not)
- Seeing exactly what they can see (new). The window is never a surveillance tool, because what it may show is always visible to the tenant themselves.
- Removing the link (new)
- Nudging upward: reminding a parent that the rent is due, that their identity check is pending, or that the agreement is waiting for their signature, and then seeing whether it was done (new). Students spend real emotional energy chasing their own parents by phone; this turns it into one tap and an honest status.
- The emergency health card, opt in: blood group, allergies, an emergency contact, travelling with the tenant's profile for the day it is needed (new)

**Where the seam is.** For a minor, the tenant is not the gatekeeper: the property or the guardian holds that role and the tenant can at most request. Everything on the parent's side of that seam leaves this tree and belongs to the parent product's own map.

#### B5.9 · My tenancy

**Solve it first, all of it.** Every one of these is a request with a property approval and a money consequence, so the sequence is the design.

These live in Me and not in the property's tab on purpose. The property's tab is about the building and it can be absent. Your tenancy is yours and it is never absent, so nothing here can be reachable only from a tab that might not exist.

- Change your room or bed (new). TAR-07 calls this the most common move a tenant ever makes and says it deserves first-class treatment. Nothing in the code does it today.
- Change your plan: opt out of food this month, add laundry next, with the month's components recalculating honestly (new)
- Go away for a while: leave, the outpass, guardian approval, the food component adjusted for the days away, the room held (partly: marking leave and the pending requests tab exist, and nothing else on that list does)
- Stay longer: extensions by days, weeks or a full term, with rates and pro-ration stated before agreeing (partly: extending exists inside the move-out flow only)
- Host for longer: a guest staying the weekend or joining meals, becoming a clean priced item agreed in advance (new)
- Transfer to a sister property or any RentOk property, with the record, documents and deposit conversation travelling and the joining journey replaying only what actually changed (new)
- Renew, which is the app's quietest best work: a yearly moment of dread turned into a two-minute task (new)
- Give notice (today)

#### B5.10 · The membership

**Solve it first.** TAR-07 sets a platform fee in the thirty to fifty rupee band per tenant per month, designed to feel obviously fair rather than extracted. One place has to say what it costs and what it buys, and today no such place exists in the shape TAR-07 describes.

- What I pay, and what it buys: no charge on any payment ever, the household's other bills in one place, the yearly housing-rent tax pack, rent building a credit story, and offers scoped to members (new)
- Where the fee does not apply: a tenant who pays in cash and only records it here is not charged for a payment service they never used, and their record grows with full equality regardless (new)
- What the fee never gates: receipts, the record, complaints and documents, free for every tenant forever. A record you must rent back is not yours. (new)
- A sponsored tenant's fee going onto the company's bill, through the family link (new)
- Changing or stopping it (partly: a purchase and upgrade flow exists for the current plans, and there is no way to stop one from inside the app on iOS)

**Why this is a demolition and not an extension.** A membership module ships today with two plan tiers, a savings calculator, a benefits list, member reviews, a purchase flow, a spin wheel and a rewards path that can be locked behind buying a plan. TAR-07 replaces all of it with one flat fee and bans the wheel by name. Almost none of the existing screens survive.

Rent Day, the membership's visible moment on the first of the month, lives in Money where the payment happens, not here.

#### B5.11 · Bringing people in

**Solve it first.**

- Filling your property's vacancy: a reward the owner configured, paid after the referred tenant's first rent, as rent credit by default. It costs RentOk nothing, fills the owner's bed, rewards genuine advocacy, and gates nothing. A bounty, not a wall. (new)
- Inviting your own property onto RentOk (partly, and broken today in a way worth naming precisely). The current app has two separate invite surfaces in the same file. One of them is hidden from white-label users, and its button works. The other is visible to everyone, promises "Earn Rs 500, invite your property", and its button is an empty function that does nothing at all. TAR-01, the product brief, records the two failures as a single compound claim and marks it verified, which is wrong in both directions; correcting it is an open item. The accurate version is filed as issue 39 on the tenant app repository. TAR-01 is right about the stakes: this is a warm sales lead that costs nothing, and it is wired to a dead end.

**Deliberately absent:** share-to-unlock, referral walls and contact harvesting. TAR-07, the door one feature map, bans all three by name; TAR-00, the vision, bans share-to-unlock. No feature in this app is ever locked behind sharing.

#### B5.12 · My account

**Draw it.**

- Settings, and which channels reach me (partly: a WhatsApp opt-in exists at login and nothing else is choosable)
- Privacy, data usage, the policies (today)
- Everything in this property: the complete index of what this property runs, always here, always in the same order. This is what makes the property's tab safe. (new)
- Deleting my account honestly: the tenant takes their one-sided data with them, and signed bilateral artifacts such as agreements and receipts survive for the other party, as the law and fairness require (partly: a delete-my-data request exists)
- Logout (today)

---

## Part C · The hub, which is not a tab

Everything a tenant can **get**: services from the property, services from the city, the help RentOk brings because renting is hard, and the offers brands bring. One place, four shelves, each labelled by who provides it.

**Why it is not a tab.** TAR-07 names the spine as welcome, rhythm, proof, heard and record, and says removing any of the five stops the door making sense. Services are not on that spine. They strengthen it. Making a strengthener into a tab would also mean shipping an empty tab in every family flat that runs no services, and the bar rule already settled that we do not ship tabs that apologise.

**Why it is one object rather than three sections.** Everything else in this app is about **this tenancy**: the money, the complaints, the documents, the food, the notices. The hub is the only surface about **this life**. The tiffin service, the tax help, the insurance and the movers are not part of the tenancy at all.

That line is the seam between the doors. TAR-06's whole everyday layer for a renter with no property is this same class of thing. So the hub is built once and appears in all three doors, with the property shelf present only where a property exists. Written as a door one section, we would build the same shelf twice and it would drift inside a month.

**How a tenant reaches it.** TAR-07 already decided this and I had it backwards in an earlier draft. The moment does the introducing: movers when someone is leaving or arriving, tax help when receipts are being downloaded in tax season, insurance at move-in. Offered once, where the need has just appeared, and free to ignore. Browsing the whole hub on purpose is the second path, not the first, reached from Home and from the index. In a premium co-living, where the amenities are half of what the resident paid for, the property's tab opens into the hub filtered to that property: one object, a second door into it, nothing duplicated.

#### C1 · From your property

**Draw it.** (today: browsing, booking, rescheduling, cancelling, history and the QR check-in all ship. The overview leads with statistics no tenant asked for.) **switched**, and TAR-07 is explicit that it is invisible where the property offers none.

What this property offers, its slots, honest cancellation terms, a QR check-in and ratings that matter, including its own shared amenities: the gym slot, the theatre room, the coworking desk. Service categories carry defaults set by RentOk and adjustable by the property within bounds.

The concierge, where a premium property runs one: a named person with a face, reachable in a tap, with a stated response promise (new).

#### C2 · From your city

**Solve it first.** (new) Vendors partnered per city and per property: the tiffin service, the laundry, the gym nearby, the broadband deal. Vetted, geo-scoped, and shrinking gracefully to nothing where no partner exists.

#### C3 · From RentOk, because you rent

**Solve it first.** (new) Tax and accounting help for housing-rent claims, insurance, movers and packers, a doctor on call, couriers, and legal help for the paperwork of renting.

Legal help here means the agreement explained and general legal services. Tooling for disputes against one's own landlord belongs to the open door, not to the app the landlord distributes.

#### C4 · Offers

**Draw it** once the scoping exists. (partly: offers, redemption, expiry and history all ship today. What does not exist is any scoping, so every tenant in India currently sees the same catalogue, because the rewards endpoint returns one flat global pool with no filter by place, property, kind of tenant or age. That is already filed with engineering as the ask for scoping the rewards catalogue.)

Offers sit beside services and not inside them, on TAR-06's distinction: a service is something you book and someone shows up, an offer is a deal a brand brings to a verified renter. Below eighteen, a curated set only and all profiling off, which is both our standard and the law.

**Where offers belong is genuinely unsettled in our own documents.** TAR-03 groups them with rewards. TAR-07 lists them under the monthly money moment. TAR-06 insists they are their own surface. I have put them here on TAR-06's logic. This is a call, not a rule.

**The guard this whole part needs**, in TAR-07's own words: each layer labelled by who provides it, never mixed together, and never an advertising space. A hub is exactly how this becomes a mall if we are careless.

---

## Part D · The flows that take over the screen

Some things are not a tab and not a section. They take the whole screen, run to an end, and put the tenant back where they were. They are listed separately because they are where the sequence matters most and where a designer needs the whole path in front of them rather than one screen.

Every one of these is **Solve it first**, without exception, because a flow whose steps are unsettled cannot be drawn at all.

| The flow | Where it starts | Behind it |
|---|---|---|
| Joining, from the code to the keys | The entrance, or a link from the property | partly: joining by code and the waiting screen ship, the web hand-in and the designed welcome do not |
| Signing the agreement, every party signing their own part | Joining, or My documents | partly: one signer works, several do not, and the signing screen asks people to sign sideways |
| The move-in record | Day one, or Joining where the property prefers it | partly: the document already shows to the tenant, the capture flow does not exist |
| Paying | Money, Home, or a message that deep-links to it | today |
| Setting up presence for the first time | The property's tab, and never on the first open | partly: it exists and today it is a wall on the very first open |
| Giving notice and moving out | My tenancy | partly: requests, approvals and the checklist ship; the deposit journey does not |
| The deposit's journey, held to landed | Move-out, and visible from Money throughout | partly: refund records reach the app, the journey with its dates and countdown does not exist |
| Renewing | My tenancy, and a calm reminder as the end date approaches | new |
| Transferring to another property | My tenancy | new |
| A member joining or leaving a shared tenancy | The people on your agreement | new |
| Migrating from the old app | The first open, once | new |

**Two rules from the design language, [TAR-02](TAR-02-design-language.md), govern all of them.** Every multi-step flow saves its progress and reopens where the tenant left off, because starting over is a design failure and not a tenant failure. And every system permission is preceded by a plain-words screen of ours saying what we need and why, and survives refusal gracefully with a way back later.

**One rule from TAR-07 governs the endings.** The app presents staying before leaving. Renewal comes first as the end date approaches, and the leaving path opens only by the tenant's own act.

**Two more rules from TAR-07 govern the whole tree and are easiest to forget here.** Login gates the result and never the discovery, so browsing, menus and public information are open and an account begins where personal value begins. And every artifact the app produces carries the name: receipts, records and reports are designed, branded by the property where the app is white-labelled, and worth showing to someone.

---

## Part E · The index, and why the changing slot is safe

The one structural guarantee in this document.

**Everything a property runs appears in one index, inside Me, in the same place and the same order for every tenant in India.** It is complete. It does not shrink when the bar shrinks. TAR-00 already scoped it as Feature navigation, one of the ten core sections.

Three rules on it:

1. **Nothing is reachable only from the property's tab.** If it is in the app, it is in the index.
2. **The index is a list, not a home screen.** It does not personalise, reorder or hide. Its whole value is that it is the same every time.
3. **It names what is switched off, and says who switched it.** A tenant who has heard that another building has the food menu should find out here that this property does not run one, rather than concluding the app is broken. This is a small thing and it is the difference between an app that was arranged for you and an app that looks broken.

---

## Part F · What is deliberately not in this tree

Nothing is silently dropped. These are the absences, each with its reason.

### The open door's own surfaces

Each of these has its own subtree in [TAR-06](TAR-06-open-for-all-feature-map.md), the open door's feature map, where they are that app's heroes. They are absent here for stated reasons rather than by oversight.

| Not in this door | Why |
|---|---|
| Browsing properties, and the AI Broker | The landlord's channel will not advertise his competitors. The sanctioned move inside this door is the transfer. |
| The AI Lawyer, checking an agreement against a state's own tenancy law | Here, legal help means the agreement explained. Tooling for a dispute against your own landlord cannot live in the app he handed you. |
| The maintenance log and the landlord line | Both serve a renter whose landlord is not on RentOk. Here, complaints and the money story do that work. |
| The flat and flatmate board | Here, a member leaving posts the vacancy to their own group and to the owner's bounty. |
| The document vault as a separate place | My documents does this job, inside the tenant's own three layers. |
| The small companions: the trip planner, the meal planner, the cost-of-living guide | Three different reasons, none of them a node yet: the trip planner is deferred, the meal planner waits on research, the cost-of-living guide has no door one entry at all. |
| Rating your landlord | A public landlord rating inside the landlord's own app is not something we can honestly ship. |
| Declaring your own renting terms | Only needed where no property is in the loop. Here the terms are the property's, shown before day one. |
| Zero-deposit and pay-in-parts money help at move-in | Here the property sets the deposit and the joining flow states it. Revisit if research says the lump sum is a barrier in our properties too. |
| Verified brokers, and flatmates rating flatmates | Both help a stranger evaluate a stranger. Here the property has already done that, and the directory carries who actually lives here. |

**This table is how the open door lives in this document: named and reasoned in one place, rather than scattered through the tree as absences.** That is why this is one document and not three, and question five asks whether it is enough. Doors one and two are the same system with the brand's voice and its own limits, so door two takes a difference note where it needs one and never a column of its own.

### The parent's own app

`com.rentok.parent` is a shipped package with its own build number in the backend's hardcoded force-update list, and the server already branches on it in two places: the complaint bot is switched off for it, and it receives its own hardcoded feature block. It is a separate product and it gets its own map. What stays in this tree is the tenant's side of the link, in My family's access, because the tenant is the gatekeeper of their own tenancy.

### Named in TAR-07's not-building list, and therefore absent here

Compliance leaderboards ranking tenants. Share-to-unlock, referral walls and contact harvesting. A section for browsing other properties. Tenant activity dashboards for landlords. App-generated pending tasks. Money custody in expense splitting. A point-of-contact role in shared tenancies. A prize wheel attached to rent. A simple mode. Read receipts on ordinary notices. Marketing banner slots on the home screen. Stored-value wallet custody.

Three of those exist in the app today and are being removed by this structure rather than redesigned: the two marketing banner slots, the always-empty pending tasks list, and the reward reveal on the payment success screen, which is the closest thing the current app has to a prize wheel attached to rent.

### Deferred in TAR-07, and therefore not given a place here

The jobs and internships board. Group search across properties. Anonymous posting in community. City-level community. The institute's own aggregate window. Deeper connected-home work beyond locks and meters. The institutional health log. The trip planner. Becoming a bill-payments biller directly. Each one has a revival condition recorded in TAR-07 and none of them needs a node until that condition is met.

---

## The eight questions

Each one is a fork, my pick and what that pick costs, and the thing I need you to answer. All eight are argued where they arise in the document. This is where you answer them.

**1. Is the floor right?** Home, Money, Help and Me in every app always, plus one slot whose contents the property decides, and four tabs where a property has nothing to put in that slot. The cost of a floor this wide is that a hostel student carries a Money tab that stays quiet all year. Do you accept four fixed and one changing, and is four the right floor?

**2. Where does the changing slot sit?** I put it third, in the middle, because it is the easiest place on the bar for a thumb and because only Help shifts position when the slot is absent. The cost is that Money is locked at position two even for the tenant who never opens it. Third, or somewhere else?

**3. Should the changing slot be labelled for the home, or for what is in it?** I label it for the home, so it reads My PG or My Flat or the brand's own word, which turns the property's identity into a permanent surface. The cost is that a hostel's food menu sits one tap further away than it would under a tab called Food. Which way?

**4. Does the day lead the home screen?** My rule: what is happening now, then what changed since you last looked, then this home's rhythm, then money sized to what is actually due. The cost is that a tenant with a large bill meets it fourth rather than first, and we are betting the live strip and the change block earn that place. Is the rule right, and is money in the right position inside it?

**5. One tree, with the open door's own surfaces listed at the end rather than marked through the tree.** Browse, the broker, the lawyer, the maintenance log and the landlord line are named and reasoned in the last part rather than carried as marked nodes. The risk I am carrying knowingly is that this flattens the open door into a footnote. Read that part and tell me: does it hold, or do we need three trees?

**6. Help and Me, rather than Tickets and Profile.** Our own research says tenants looked for complaints under Profile and not under Tickets, so the words we use are not the words they think in. The cost is that the words on the bar become the words the whole company then uses, which makes this harder to undo than it looks. Do the two new names stand?

**7. Where do offers belong?** Our own documents disagree three ways: TAR-03 groups them with rewards, TAR-07 puts them under the monthly money moment, TAR-06 insists they are their own surface. I have put them in the hub beside services, because a service is something you book and someone shows up while an offer is a deal a brand brings you. This is the one call in the document I made on judgment rather than on a rule. Hub, or beside the record in Me?

**8. Does complaints earn a permanent tab?** A tenant files a few complaints a year, which is not a frequency that earns a tab. My argument is that it has to be findable at the moment something is wrong, which is a moment of stress, and that hunting for it then is the failure. The directory and the conversation are what give the tab weight on an ordinary day. Does that hold, or does Help come off the bar?

---

## What this asks the backend for

The roll-up of every part marked **new**, so the engineering conversation has a list rather than a document to read. The asks already filed with engineering are not restated, except where one of them blocks a whole tab.

**The ones that block a whole tab or flow:**

1. **A tenant's share of everything, in a shared home.** Rent share, deposit share, and a slice of every recurring package, per person, with receipts and tax proofs per person. Without it, the money tab has one shape instead of two and the people on your agreement cannot exist at all.
2. **A billing calendar that is not monthly.** Semester and yearly billing with instalments, weekly and daily billing, and honest pro-ration whenever a stay, a plan or a room changes mid-cycle.
3. **The deposit's journey as a state machine, not a number.** Held, inspected, agreed, refunded, each with a date, against a timeline the property commits to. Refund records already reach the app; the journey does not exist.
4. **A read side for the message log.** Already filed, and repeated here because it blocks the Help tab outright. The store exists and is populated; every reader today is manager-side.
5. **Room and bed change, plan change, extension and transfer as first-class requests** with approval, pro-ration and a fresh condition record on the new room.
6. **The changing slot itself**: a property's real feature configuration flowing to the app, replacing the hardcoded ten-account list and the two-option third slot that ship today, one of whose two options the app has never been able to render.

**The ones that unlock a section:**

7. The move-in record as a tenant flow, on top of the checklist data and document that already exist.
8. The house facts card as property-authored content.
9. A notice board with categories, pinning, an honest archive and acknowledgment on critical notices only.
10. A directory with roles, and call routing that keeps staff personal numbers private.
11. Presence, the gate, guests and parcels as one system with one shared record, and the tenant's mirror of exactly what the property sees.
12. The record: facts with a date and a source rather than judgments, contestable by the tenant before they travel anywhere, with complaint counts and move frequency structurally excluded.
13. Community, polls, events, chores and splitting. Most sit on TAR-00's flexible list, so they wait on the research round. Chores does not sit on it and needs its own call.
14. The academic calendar: terms, closures, instalments.
15. Bill payments beside the rent.
16. Credit bureau reporting with consent, and a score check inside the app.

**What is deliberately not asked for yet:** anything on TAR-07's deferred list, and anything the research round could still change. Community and polls are the largest example. They have a place in the tree so the shape is visible, and they have no backend ask until tenants say they want them.

---

## Before the 15th

Bring your red pen on the tree and a written answer to the eight. Half a day: the first two hours on the eight, the rest on whatever your red pen turned up. Structure locks that day.

One item is not written down and belongs in the room rather than on paper: I want to raise a change to the tenant-type screen you sketched, once the tree is marked up.

Then the theme, and then design in pieces, in the order this document already implies. Everything marked **Draw it** starts the following Monday. Everything marked **Solve it first** goes back through a flow round before a designer touches it.

## Changelog

- 9 September 2026: first version. Written after the door one and door three feature maps, against three findings in the shipped bottom navigation code, with the archetype walk run generatively across eight lives rather than as a checking pass over finished thinking. Four forks were ruled before writing: the changing slot, the parent app as a separate product, the day leading the home screen, and one tree rather than three. Services and offers were moved out of the Help tab and into a hub during review, after the grouping was tested against TAR-07's spine and failed it.
