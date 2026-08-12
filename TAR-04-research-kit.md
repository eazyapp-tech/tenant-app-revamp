---
title: TAR-04 Research Kit: Instruments for the Tenant App Overhaul
date: 2026-08-11
tags: [rentok, tenant-app, revamp, research, instruments]
owner: Sanchay
status: v1-ready-to-pilot
---

# TAR-04 · Research Kit

> Derived from [TAR-03](TAR-03-what-each-part-must-become.md). Three instruments, one per audience, each asking only what that audience uniquely knows. Every question carries its scope frame and the hypothesis it tests. Broad quantitative survey comes AFTER interview round one sharpens these: qualitative first, always.

## The rules these instruments obey

1. **No question about anything the codebase already answers.** Zero bug-asking.
2. **Nobody is asked to design.** Stories, recalls, counts, choices. We translate.
3. **Every question declares its scope**: [TODAY] answer only about the app as it exists · [NO LIMITS] anything is possible, money and tech no object · [PICK] choose from exactly these options.
4. **Ideas are harvested as needs, never as features.** Workarounds, wishes, irrelevance. A volunteered feature always gets the follow-up "what would that let you do?": we log the need, not just the feature.
5. **Session order is fixed:** experience recall → specific moments → THEIR wishes/workarounds → OUR concept tests → ranking. Their fresh ideas always come before our proposals, so ours can't anchor theirs.
6. **Banned forms:** "Is it easy/intuitive/clear?" · "What would you improve (visually)?" · "Any issues?" · "Would you use X?" (Behavioral anchor instead: "When did you last need X?")
7. **Language:** deliver in the tenant's language. Hindi-first script variants needed before field use. Interviewer speaks plainly: if a question needs our vocabulary, the question is wrong.
8. **Pilot rule:** run each instrument on 2 people, fix what confused them, then scale.
9. **Age and consent:** log every tenant's age band. Sessions with tenants under 18 require guardian consent, and their sessions skip all offer and money concept tests. Their lived-experience answers (food, attendance, gate, complaints) are among the most valuable we will collect.
10. **Gender context:** in girls-PG and co-ed sessions, the interviewer treats entry-exit, attendance, and family-visibility questions with extra care. The same feature can read as protection or as surveillance, and which one it is belongs to the respondent. Never suggest either frame; note the words they choose themselves.

**Sampling minimums (interview round 1):** tenants: 3 student-PG, 3 working-professional/co-living, 2 family-flat, 2 cash-first/blue-collar, 1 sponsored, 1 recently-moved-out (12 total, ≥4 properties, ≥2 cities, mix of app-users and never-installed). **Plus 2–3 renters with no RentOk connection at all** (recruited outside the owner channel: personal networks, other PGs) to test the open-for-all needs with their real audience; see the variant note after Instrument A. Owners/managers: 4 (1 white-label client, 1 small PG, 1 co-living, 1 family-flat landlord). Internal: 2 support, 2 sales, 1 onboarding/ops, 1 designer.

---

# Instrument A: Tenant Interview Guide (~45 min, semi-structured)

*Interviewer keeps TAR-03 open. Tags in brackets link each question to what it tests. Probe rule: every recall gets "walk me through it" + "what happened next" + "how did that feel" before moving on.*

## A0. Context (5 min): register identification without asking "which persona are you"

1. "Tell me about where you live: how long, who else, how did you find it?"
2. "Who pays the rent: you, family, your company? How does the money actually move each month?" *(register + cash/UPI reality; tests M1 assumptions)*
3. "What phone do you use? What languages do you read comfortably?" *(floor-audience check; S6)*
4. "Show me the apps on your first home screen. Which did you open today?" *(the real competition; TAR-01 bet)*

## A1. Arrival (5 min): [TODAY] [tests M2]

5. "Think back to your first week here. What did you have to do: forms, documents, apps? Walk me through it."
6. If they have the app: "Who told you to install it? What happened the first time you opened it?" *(owner-channel hypothesis; setup-wall frequency)*
7. If they don't: "Was there ever an app you were asked to install? What happened?" *(never-installed tenants are the adoption goldmine: do not skip them in sampling)*

## A2. A normal day (7 min): [TODAY] [tests M3, M7, M8]

8. "Yesterday evening, start to end: what did you check or do about food, coming in, going out?"
9. "How do you find out what's for dinner? When did you last want to know and couldn't?" *(menu-anticipation hypothesis)*
10. If attendance applies: "Tell me about marking attendance yesterday. What happens if you forget?" Then: "Some people say marking attendance feels like school, others say it makes the place feel safe, others don't think about it. Which is closest for you?" *(surveillance-vs-safety: the M7 dignity question; the three options prevent a politeness answer)*
11. "When did the property last tell you something important? How did it reach you?" *(M11; WhatsApp-vs-app channel reality)*

## A3. Money (8 min): [TODAY] [tests M1: the trust core]

12. "Walk me through the last time rent was paid: from remembering it was due to knowing it went through." *(every step they narrate is data: reminder source, channel, confirmation trust)*
13. "After paying, how do you know it worked? Have you ever needed to prove you paid: to whom, and what did you show them?" *(receipt-need hypothesis; HRA/police/parent use cases)*
14. "Has a payment ever gone wrong or left you unsure? What did you do?" *(consequence chain, not bug bingo)*
15. "Do you have any cashback, credits, or rewards in this app right now?": let them open it: "what do you think these are?" *(tests the three-overlapping-systems confusion directly, by observation)*

## A4. When something breaks (6 min): [TODAY] [tests M4]

16. "Last time something in your room or building needed fixing: what was it, and what did you do first?" *(channel choice: app/WhatsApp/warden/paper: the real filing split)*
17. "What happened after you reported it? When did you next hear anything?"
18. "Is there anything you've stopped bothering to report? Why?" *(trust-decay hypothesis)*

## A5. Paperwork (4 min): [TODAY] [tests M5]

19. "Where is your rent agreement right now: could you show it to me if I asked?" *(awareness test: hypothesis: most can't; do NOT hint it's in the app)*
20. "When you gave your documents: ID, photos: how did that go? How do you know if they were accepted?"

## A6. Moving out (4 min: if they've done it or are planning it): [TODAY] [tests M6]

21. "Tell me about the last move-out: yours or a friend's. What happened with the deposit?" *(deposit-story frequency; the #1 trust gap)*
22. "When you moved in, did anyone record the room's condition? If a deduction were claimed tomorrow, what proof would you have?" *(checklist-as-protection hypothesis: do tenants see it as theirs or the owner's weapon?)*

## A6.5 Life around the app (6 min): need probes for the new-feature space: [TODAY]

*These test the needs underneath the candidate features (Srijan's list + open-for-all + our additions) without naming any feature. Distribute naturally; skip what the conversation already covered.*

- "How did you and your roommates split last month's electricity bill? Walk me through it." *(→ Expense/splitwise)*
- "Who on your floor would you ask for help at 11pm? How did you meet them?" *(→ Community)*
- "When the mess last changed something: menu, timings: did anyone ask you first? Did you care?" *(→ Polls)*
- "What do you and your roommates keep forgetting or fighting about?" *(→ To-do/chores; probe what "task" even means to them)*
- "When you moved in, what did you have to buy? Where from? What did the previous tenant do with theirs?" *(→ P2P buy-sell)*
- "Last time you were sick here: what happened?" *(→ doctor-on-call; strongest expected for migrant/student registers)*
- "Was there ever a month when rent was hard to time? What did you do?" *(→ credit-card rent / cashflow)*
- "How many times in your renting life have you re-submitted the same documents: ID, photos, agreements?" *(→ tenancy passport)*
- "Have you ever needed rent proof: for office tax, for anything? What did you show?" *(→ receipt generator; overlaps A13, skip if covered)*
- "What does your family ask you about this place when they call?" *(→ parent window; note register)*
- "If you changed jobs to another city tomorrow, how would you find your next place?" *(→ Browse Property / relocation / movers-packers)*
- Students only: "Beyond rent, what's the money pressure this year?" *(→ jobs/internships: big need, unproven fit; do not pitch, just listen)*

## A7. Their ideas (5 min): elicitation BEFORE our concepts

23. [NO LIMITS] "If this app could do one thing for you that it doesn't today: anything at all: what would it be?" *(magic wand; follow up: "what would that let you do?")*
24. [TODAY] "What do you do around living here: payments, splitting bills with roommates, complaints, anything: using WhatsApp, paper, calls, or another app, that you wish you didn't have to?" *(workaround inventory = behavioral feature requests)*
25. [TODAY] "Open the app's home screen. Point at anything that has nothing to do with you." *(irrelevance harvest: personalization gaps without the word "personalization")*

## A8. Our concepts on trial (8 min): concrete scenarios, plain words, forced choice

*Present verbally or on a card. Never ask "do you like it": ask which is theirs, and for the last time they needed it.*

26. **Personalization pair** [PICK]: "Two versions of the app's first screen. **A:** offers, banners, and menus: the same for every tenant in India. **B:** your building's name and logo at the top, tonight's dinner at your mess, your rent counted down, and offers from shops in your city. Which one is your app? What in B would you not want?" *(the second question is the creepy-line probe: note WHICH element they reject: city? gender-implied content? being 'known'?)* [tests TAR-01 three-axis bet + stereotype trap]
27. **The record** [PICK]: "**A:** pay rent on time, get a scratch card worth ₹5-50. **B:** pay on time, build a record: '14 months, always on time': that you could show a future landlord anywhere. **C:** neither matters, rent is rent. Which is closest to you?" *(streak/tenancy-record vs cashback vs indifference: tests M9 overhaul bet honestly, C included so indifference is a permitted answer)*
    Follow-up if B or C: "And if paying on time also improved your credit score: the thing banks check before giving loans: does that change anything?" *(rent-to-credit-score; the whitespace candidate. Note whether "credit score" needs explaining: that itself is register data.)*
28. **Property's messages in-app** [PICK]: "All messages from your property: reminders, notices: currently on WhatsApp. **A:** keep them in WhatsApp. **B:** also see the whole history inside the app, so nothing gets lost between your other chats. Would B change anything for you? When did you last lose a property message in WhatsApp?" [tests Messaging direction]
29. **Deposit tracker** [scenario]: "From the day you give notice, the app shows: deposit held ₹25,000 → room inspected → deductions listed with photos → refund sent, with dates. When you last moved out, what would this have changed?" [tests M6 overhaul bet]
30. **Meal count** [scenario]: "The menu shows '43 of 60 people are eating tonight.' Helpful, pressuring, or nothing?" *(community-vs-pressure; one word answers are fine)*

## A8.5 The deck: pick 3, kill 3 (6 min): [PICK]

*Sixteen cards, each a plain-language outcome, never a feature name. Lay them all out (paper or phone). "Pick the 3 that would actually change living here for you. Then throw out the 3 you'd never touch." The kill pile is as informative as the picks. Probe the top pick: "when did you last need this?"*

1. Split electricity and other bills with roommates, automatically
2. A record of every rent you've paid on time: usable with any future landlord
3. Paying rent on time improves your credit score
4. All your rent receipts ready for office tax proof, any time
5. A proper rent agreement made in minutes, legally valid
6. Timestamped photos of your room's condition: so your deposit can't be unfairly cut
7. A doctor on call when you're sick
8. Pay rent by credit card when the month is tight
9. Vote on mess menus and building decisions
10. Buy and sell furniture from tenants moving out nearby
11. Find your next room in another city from this same app
12. Movers and packers arranged when you relocate
13. Your family can see rent is paid and you've checked in safe *(autonomy-sensitive: a kill here is creepy-line data, log which register kills it)*
14. Jobs and internships through the property network
15. A shared to-do list for your room or flat
16. Local services near you: tiffin, laundry, gym: with tenant discounts

## A9. Close (3 min)

31. "If the owner said this app costs ₹30 a month with the rent: and it included your top pick from those cards: what's your honest reaction?" *(value-anchored to THEIR pick, not abstract; log the reason, not the yes/no)*
32. "What's the one question I should have asked you and didn't?"

---

### Variant: the non-RentOk renter (2–3 sessions, ~30 min)

Same guide, adapted: run A0, A2–A6.5 about their current renting life (no app to reference: their workarounds ARE the baseline data); skip A1 and app-dependent probes (Q15, Q25); run A7, the open-for-all cards from the deck (2, 3, 4, 5, 6, 7, 8, 11, 12), and close with: "would you install an app for [their top pick] even though your landlord has nothing to do with it? What would make you trust it with your documents/money?": the open-for-all door's two real questions: standalone value and trust-without-the-landlord.

---

# Instrument B: Owner / Manager Interview Guide (~30 min)

*They are the distribution channel and the white-label buyer. Their questions are about THEIR behavior and THEIR business, never about app design.*

## B0. Context (3 min)
1. "Tell me about your property: beds, tenant type, how long. Who handles day-to-day tenant communication?"

## B1. The handover (6 min): [TODAY] [tests M2 owner-channel hypothesis]
2. "Walk me through your last tenant move-in, from deal agreed to keys handed. Where does the app appear, if at all?"
3. "When you tell tenants about the app, what exactly do you say? What do they ask back?"
4. "What share of your current tenants use the app? What do the rest do instead?" *(their estimate vs reality is itself data)*

## B2. Their burden (6 min): [TODAY] [demand harvest]
5. "What do tenants ask you or your manager every week that feels like it shouldn't need you?" *(the app's job list, in their words)*
6. "Show me your WhatsApp with tenants: what are the last five things there?" *(channel reality; only if they offer)*
7. "What's the most painful part of a tenant leaving?" *(M6 owner-side)*

## B3. Pride and brand (5 min): [NO LIMITS] [tests owner-pride metric + white-label]
8. "When a prospective tenant's parent visits, what do you show them to prove this place is well-run?"
9. "If the app carried your property's name and look, and you could show it during that visit: what would need to be on the first screen for you to actually pull out your phone and show it?" *(their answer designs the boot ritual better than we can)*
9b. "What kind of tenants do you most want more of, and what do those tenants ask about before choosing a place?" *(connects the personalization data the manager app already captures to what owners would want the app to signal for them)*
10. For white-label clients: "What made you buy your own branded app? What did tenants say when it launched?"

## B4. Their ideas (4 min)
11. [NO LIMITS] "If the tenant app could take one thing completely off your plate, what?"
12. [TODAY] "What's the cleverest thing you've seen another property do: any property, any tool: that made tenants happier?" *(harvested innovation)*

## B5. Concepts on trial (6 min)
13. **Invite economics** [scenario]: "A tenant taps 'invite my previous landlord', the landlord gets a demo and you get ₹X if they join. Would your tenants do this? Would YOU have responded to it as a landlord?" [tests every-tenant-is-a-channel]
14. **Deposit tracker** [scenario]: the A29 scenario, owner-side: "would you commit to showing deduction photos and a refund date inside the app? What would stop you?" *(the honest blocker surfaces here)*
15. **The fee** [PICK]: "If the app clearly saved your manager 5 hours a week and tenants loved it: **A:** I'd pay for it as a business cost. **B:** I'd pass ₹30-50/tenant into rent. **C:** it should stay free. Which, and why?"
16. **The deck, owner-side** [PICK]: show the same 16 cards from A8.5. "Which 3 would make you push the app hardest to your tenants? And which would you NOT want running under your property's name?" *(the objection pile is the finding: expect owner-liability smell on buy-sell, community, and jobs; their reasons shape what white-label clients can toggle)*

---

# Instrument C: Internal Team Guide (~20 min or async form)

*Support, sales, onboarding, ops. Two things only: heard demand and witnessed moments. No bug bingo: we own the codebase.*

## C1. Heard demand
1. "What do tenants contact you for that the app should have handled? Last five, verbatim if you can."
2. "What do owners ask for in sales calls that we don't have? What deal did we last lose, and to what?"
3. "What's the most repeated question in support this month?" *(their top-of-mind IS the frequency data)*
3b. Show the 16 cards from A8.5: "Which of these have you actually HEARD a tenant or owner ask for: in what words? Which have you never once heard anyone want?" *(heard-demand mapped onto the candidate deck; the never-heard pile deflates our enthusiasm cheaply)*

## C2. Witnessed moments
4. "Describe the last time you physically watched a tenant try to install and set up the app. Where did they stop? What did they say out loud?"
5. "Describe the last onboarding of a new property's tenants: what did the owner do, what did tenants do, what did YOU have to do manually?"
6. "When a tenant gives up on the app, what's the moment it happens: as specifically as you've seen it?"

## C3. Harvested innovation
7. "What's the cleverest workaround you've seen a tenant, owner, or teammate use where the app fell short?"
8. "If you could hand the design team one recording of a real moment you've witnessed, what moment?"

## C4. One scoped concept check (their unique vantage)
9. [PICK] "Of these, which ONE would most change what tenants say to you: better receipts and payment proof · complaints that visibly progress · attendance that feels less like policing · deposit transparency at move-out · the app in Hindi and regional languages? Pick one, tell us the story behind your pick." *(forced trade-off; the story is the data)*

---

# Analysis contract (so the answers land back in the docs)

- Every session gets logged against TAR-03 tags: which [OBSERVED] items gained/lost support, which [INFERRED] items survived or died, plus new needs (from A7/B4/C3) logged as candidate hypotheses with their evidence.
- Concept-test outcomes (A8/B5/C4) update TAR-01's bets directly: each bet gets *supported / challenged / needs-more* after round one.
- The creepy-line probe (Q26) reports which personalization elements were rejected and by which register: this feeds the personalization spec's boundaries, not just its features.
- **Card-deck tallies across all three audiences:** per card: tenant picks, tenant kills, owner pushes, owner objections, internal heard/never-heard. A card strong on tenant picks + owner pushes + internal heard-demand is a build candidate; a card strong only in our own enthusiasm is not. Card 13's kill pattern (by register) feeds the personalization creepy-line boundary alongside Q26.
- Need-probe answers (A6.5) log against the candidate features they test: a feature whose need never surfaced unprompted across 14 sessions starts the prioritization conversation from behind, whatever its card ranking.
- After 12+3 tenant sessions: write the round-one synthesis, THEN derive the broad quantitative survey from whatever needs counting (never before).

## Changelog
- 2026-08-11: v1. Built from TAR-03 under the locked philosophy: no bug-asking, nobody designs, scope frames on every question, needs-not-features elicitation ordered before concept tests. Internal track retained per Sanchay's call (heard demand + witnessed moments only).
- 2026-08-11: v2. New-feature space added per Sanchay: need-probes for Srijan's candidate list + open-for-all services + four additions (rent-to-credit-score, tenancy passport, parent window, standalone deposit protection), woven as A6.5; the 16-card pick-3/kill-3 deck (A8.5) with owner and internal mirrors; credit-score follow-up on Q27; fee question value-anchored to the tenant's own top pick; 2–3 non-RentOk renter sessions added to sampling with a session variant testing the open-for-all door's two real questions (standalone value, trust without the landlord).