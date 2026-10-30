---
id: 16
slug: communication-stakeholders
title: Stakeholders, communication, presenting and training
phase: E
priority: P2
quick_min: 5
deep_min: 35
job_ad: "spolupráce s dodavateli a stakeholdery, reporting stavu, prezentace a školení kolegů"
---

## Why this matters
A business analyst spends more time talking, writing and presenting than modeling. Requirements come from people, decisions are made by people, and a solution is only useful if people adopt it. The target job ad asks for collaboration with vendors and stakeholders, status reporting, and presentations and training of colleagues. This module gives you practical tools for each: who to involve, how to run a meeting, how to report, how to present a recommendation, and how to teach colleagues a new process.

## Quick version
**Stakeholders.** A *stakeholder* is anyone affected by a change or able to influence it. Missing one early (for example compliance or the vendor's support team) usually means a late surprise.

**Analyzing stakeholders:**
- **Power/interest grid** — place each stakeholder by power (ability to influence decisions) and interest (how much the change affects or concerns them). High power and high interest: manage closely. High power, low interest: keep satisfied. Low power, high interest: keep informed. Low power, low interest: monitor.
- **RACI matrix** — for each task or decision: who is **R**esponsible (does the work), **A**ccountable (owns the result, one person), **C**onsulted (gives input before), **I**nformed (told after).
- **Onion diagram** — concentric rings: the solution in the middle, then people who use it directly, then the wider organization, then external parties (clients, regulators, vendors).

**Communication plan.** A simple table: who, what information, how often, which channel, who sends it. It prevents both silence and spam.

**Meetings and workshops.** Every meeting needs a purpose, an agenda with times, the right people, and agreed outputs. Assign roles: facilitator, note-taker, timekeeper, decision-maker. Close with decisions and action items (what, who, by when).

**Conflicting requirements and saying no.** Make the conflict visible with facts, link each option to business goals, and escalate to the person with authority to decide. "No" is easier to accept as "not now, because…" with a trade-off: "We can add this, but then X moves to the next release."

**Managing vendors in meetings.** Agree the agenda in advance, keep one channel for requirement questions, never agree new scope verbally (route it to a change request), confirm everything in writing.

**Status reporting.** Use **RAG status** (Red, Amber, Green) for scope, schedule, budget and quality. A good weekly report fits on one page: overall status, what was done, what is next, risks and issues, decisions needed.

**Presenting a solution.** Structure: **problem → options → recommendation → ask**. For non-technical audiences, focus on impact, cost and risk. For technical audiences, add how it works, interfaces, data and constraints. Always end with a clear ask: what decision or action you need.

**Training colleagues.** Start with learning objectives ("after this session you can…"), show a short demo, let people try it themselves on test data, and hand out a one-page cheat sheet.

**Writing.** Clear emails have the ask in the first two lines. Meeting minutes record decisions and action items, not a transcript. Send minutes within 24 hours and ask for corrections by a stated date, so that agreements do not get lost or reopened later.

## Deep dive

### Identifying stakeholders [P1]
Start broad, then narrow down. Questions that help:
- Who uses the current process or system every day?
- Who receives its outputs? Who supplies its inputs?
- Who pays for the change? Who approves it?
- Who must check it for compliance, security, data protection or risk?
- Who builds, tests, runs and supports it (internal IT, vendor)?
- Who outside the company is affected (clients, partners, regulators)?

For the ExportShield project "automate claim intake" the list might include:

| Stakeholder | Relationship to the change |
|---|---|
| Head of Claims (sponsor) | Funds the project, owns the business result |
| Claims handlers | Daily users of ClaimDesk, main source of requirements |
| Claims manager | Approves claims, defines approval rules |
| Exporters (clients) | Submit notifications; experience the new form |
| Finance | Pays indemnities; needs correct amounts and accounting data |
| Recovery team | Takes over after payment to pursue the buyer |
| Compliance / data protection officer | Checks handling of personal and client data |
| IT operations | Runs ClaimDesk and DocVault, manages access |
| NovaSoft s.r.o. (vendor) | Builds and supports the integration |
| Internal audit | May review controls later |

Do this list early and revisit it. Stakeholders change during the project.

### Power/interest grid [P1]
Place each stakeholder in one of four boxes. The position tells you how much effort to spend on them.

| | Low interest | High interest |
|---|---|---|
| **High power** | Keep satisfied: short, targeted updates; involve for key decisions (e.g. CFO, IT director) | Manage closely: regular involvement, early consultation (e.g. Head of Claims, claims manager) |
| **Low power** | Monitor: minimal, general communication (e.g. internal audit until later) | Keep informed: regular updates, involve in testing (e.g. claims handlers, recovery team) |

Notes:
- Power is not only hierarchy. A compliance officer with the right to block go-live has high power on this project.
- Positions move. Finance may have low interest until the indemnity calculation is touched, then high.
- Low-power, high-interest people (often the end users) are your best source of detail and your future adopters. Do not treat "keep informed" as "ignore".

### RACI [P1]
RACI clarifies who does what for each activity or deliverable. The key rule: **exactly one A per row.** Several R are possible.

| Activity | Head of Claims | Claims manager | BA | Claims handlers | NovaSoft | Compliance | IT operations |
|---|---|---|---|---|---|---|---|
| Approve business case | A | C | R | I | I | C | I |
| Define claim approval rules | A | R | C | C | I | C | I |
| Write requirements and user stories | I | C | A/R | C | C | C | C |
| Build integration | I | I | C | I | A/R | I | C |
| Data protection assessment | I | I | C | I | C | A/R | C |
| UAT execution | I | A | R | R | C | I | I |
| Go-live decision | A | C | C | I | C | C | R |

Common problems RACI reveals: two people think they are accountable; nobody is accountable; too many people are consulted, which slows decisions.

### Onion diagram [P3]
The onion diagram shows how close each group is to the solution. Rings from inside out:
1. **The solution** (new claim intake form and integration).
2. **People who operate it** (claims handlers, IT operations).
3. **The wider business** affected by it (finance, recovery, management).
4. **External parties** (exporters, vendor, regulator).

It is a quick visual for a kick-off slide: everyone sees that the change is not only about the claims team.

### Communication plan [P2]
A communication plan is a short table. It turns good intentions into a routine.

| Audience | Information | Frequency | Channel | Owner |
|---|---|---|---|---|
| Sponsor (Head of Claims) | Status, decisions needed, risks | Weekly | 1-page report + 15 min call | BA / project manager |
| Steering committee | Progress vs plan, budget, major risks | Monthly | Meeting with slides | Project manager |
| Claims handlers | What changes, when, what we need from you | Every 2 weeks | Team meeting slot, short email | BA |
| NovaSoft | Requirement clarifications, priorities | Continuous / weekly | Jira, weekly call | BA |
| Compliance | Data flows, access, retention | At design and before go-live | Meeting, written assessment | BA + compliance |
| Exporters | New notification form | Before go-live | Email, website notice | Business / marketing |

Tip: agree with each high-power stakeholder *how* they want to be informed. Some read reports, some want a five-minute call.

### Facilitating meetings and workshops [P1]
**Before:**
- Define the purpose in one sentence and the expected output (for example "agreed list of required documents per product").
- Invite only people who are needed for that output. Send the agenda and any pre-reading 2–3 working days ahead.
- Prepare materials: a draft process, a list of open questions, a whiteboard in Miro.

**Agenda example (60-minute workshop):**

| Time | Item | Output |
|---|---|---|
| 0–5 | Purpose, agenda, roles | Shared understanding |
| 5–20 | Walk through current claim notification (AS-IS) | Corrections to the draft |
| 20–40 | Required documents per product: brainstorm and agree | Draft checklist |
| 40–50 | Open questions and edge cases | List with owners |
| 50–60 | Summary of decisions and actions | Agreed action items |

**Roles:**
- **Facilitator** — runs the process, keeps focus, makes sure everyone speaks. Ideally neutral on content.
- **Note-taker** — records decisions, actions and open questions, not every sentence.
- **Timekeeper** — signals when an item runs over.
- **Decision-maker** — the person who can confirm a decision in the room. If they are absent, label results as proposals.

**Techniques:**
- **Round robin** — everyone gives one point in turn; prevents the loudest voice from dominating.
- **Silent brainstorming** — everyone writes ideas on sticky notes for five minutes before discussing.
- **Dot voting** — each participant gets three votes to mark priorities.
- **Parking lot** — a visible list for off-topic items, so they are not lost and do not derail the meeting.
- **Walkthrough** — step through a process or screen one step at a time and ask "what happens if…?".

**After:** send minutes within 24 hours (see the writing section below).

### Handling conflicting requirements and saying no [P1]
Conflicts are normal. Claims handlers want fewer mandatory fields; compliance wants more data; finance wants a payment date that the vendor says is hard to deliver.

A practical approach:
1. **Make it visible.** Write both requirements side by side with their source and reason.
2. **Go back to the goal.** Which option better supports the business requirement and the problem statement?
3. **Look for a third option.** Mandatory field only above a certain claim amount? Data taken from another system instead of typed?
4. **Show the trade-off in numbers or risk.** Time per claim, regulatory exposure, cost.
5. **Escalate to the decision-maker** defined in the RACI. The BA prepares the decision; the accountable person makes it.
6. **Record the decision** and its reason, so it does not reopen next month.

Saying no without damaging the relationship:
- Replace "no" with a choice: "We can add it in this release if we move the reporting story to the next one. Which matters more to you?"
- Refer to agreed rules: scope, change request process, regulation.
- Acknowledge the need even if the solution is rejected: "I understand you need to see the status. The export button isn't in scope, but the dashboard planned for June covers it."

### Managing vendors in meetings [P2]
With an external vendor such as NovaSoft, words in a meeting can have contractual consequences.

- **Agree the agenda in advance** and send open questions before the call so the vendor brings the right people.
- **Separate clarification from new scope.** Clarifying an existing requirement is normal. Anything new goes through a change request.
- **Do not promise on behalf of others.** "I'll check with the claims manager and confirm by Thursday" is better than an improvised answer.
- **Confirm in writing.** Send a short summary after each call: decisions, open points, owners.
- **Keep one source of truth** (Jira, Confluence or the specification). Decisions agreed in chat or by phone must be copied there.
- **Respect and firmness together.** Vendors work better with a client who is clear and consistent than with one who is friendly but changes direction every week.

### Status reporting and RAG [P1]
**RAG status** marks each dimension:
- **Green** — on track; no action needed from management.
- **Amber** — at risk; the team has a plan to recover but management should be aware.
- **Red** — off track; a decision or help from management is needed.

Rules for honest RAG: define thresholds in advance (for example Amber = up to two weeks' delay on a milestone); never show green when you know it is amber; and for each amber or red say what you need.

**Weekly status report template (one page):**

```text
Project: ClaimDesk claim intake automation        Week: 2026-W44
Overall status: AMBER                             Prepared by: BA

Scope: GREEN     Schedule: AMBER     Budget: GREEN     Quality: GREEN

Summary (2-3 sentences)
UAT preparation is on track. The integration with DocVault is one week late
because the vendor is waiting for test environment access.

Done this week
- Requirements for document checklist signed off by claims manager
- 6 of 8 user stories for Sprint 4 refined and estimated
- UAT scenarios drafted (12 scenarios)

Planned next week
- Sprint 4 review with claims handlers
- Finalize UAT test data (fictional, anonymized)

Risks and issues
| ID | Description | Impact | Owner | Action | Due |
| R3 | No TEST access for vendor to DocVault | 1 week delay | IT ops | Access request escalated | 05/11 |

Decisions needed
- Sponsor: approve CR-07 (buyer turnover field), cost estimate attached, by 06/11

Milestones
- UAT start: 18/11 (was 11/11)   - Go-live: 09/12 (unchanged)
```

What makes a report good: short, the same structure every week, facts and dates, and decisions needed clearly at the top or highlighted. What makes it bad: long narrative, everything green until it suddenly turns red, no owners.

### Presenting a solution [P1]
Use the same backbone for any audience:

1. **Problem** — what is wrong, for whom, how much it costs (one slide).
2. **Options** — usually two to four, including "do nothing", with pros, cons, cost and risk.
3. **Recommendation** — which option and why, in one sentence plus evidence.
4. **Ask** — what you need from this audience today: a decision, budget, people, feedback.

**Adapting to the audience:**

| | Non-technical (management, business) | Technical (IT, architects, vendor) |
|---|---|---|
| Focus | Impact, cost, risk, timeline | How it works, interfaces, data, constraints |
| Detail | One number per point, rounded | Precise fields, formats, volumes, error handling |
| Visuals | Before/after process, simple chart | Sequence diagram, data model, API sample |
| Typical question | "What does it cost and when do we get it?" | "How does it integrate and what happens on failure?" |
| Avoid | Acronyms, system jargon | Vague statements like "it will be fast" |

Tips:
- Put the recommendation early for senior audiences. They may stop you after three minutes.
- Prepare a backup slide for the questions you expect.
- Rehearse aloud and time yourself. A five-minute slot means about 600–700 spoken words.
- Never show real client data in slides. Use fictional or anonymized examples.

### Preparing a short internal training [P2]
When a new feature goes live, the BA often trains the first users or the trainers.

**Structure of a 30-minute session:**
1. **Learning objectives** (2 min) — two or three statements starting with "After this session you can…", for example "…submit a claim notification with the new document checklist" and "…see why a claim is waiting".
2. **Why it changed** (3 min) — the problem in the users' words, not the project's.
3. **Demo** (8 min) — one realistic scenario, start to finish, on the UAT or training environment with fictional data.
4. **Hands-on** (12 min) — each participant does two prepared tasks themselves. Walk around (or watch shared screens) and help.
5. **Questions and where to get help** (5 min) — who to contact, where the cheat sheet and documentation live.

**Cheat sheet:** one page, screenshots with numbered steps for the three most common tasks, list of what changed, contact for help. People keep it on their desk; they will not reread a 40-page manual.

**Check learning:** ask participants to do one task without help at the end. If most can, the session worked.

### Clear emails and meeting minutes [P1]
**Emails:**
- Subject line states the topic and the ask: "Decision needed by 6/11: CR-07 buyer turnover field".
- First two lines: what you need, from whom, by when.
- Then context in short paragraphs or bullets.
- One email, one topic. Separate topics get separate emails so they can be tracked.
- Re-read before sending: would someone who missed the meeting understand it?

**Meeting minutes template:**

```text
Meeting: Claim document checklist workshop    Date: 2026-10-29
Participants: claims manager, 3 claims handlers, compliance, BA (notes)
Purpose: agree required documents per product

Decisions
D1. Proof of delivery is mandatory for all products.
D2. Correspondence with buyer is mandatory only for claims above the internal threshold.

Action items
| # | Action | Owner | Due |
| A1 | Confirm threshold amount with Head of Claims | Claims manager | 02/11 |
| A2 | Update requirement REQ-14 and send for sign-off | BA | 04/11 |
| A3 | Check retention rules for uploaded documents | Compliance | 09/11 |

Open questions
Q1. Do short-term policies need the same checklist? (owner: claims manager)

Parking lot
- Idea: automatic reminder to exporters after 5 days (to backlog)
```

Minutes record decisions and actions, not who said what. Send them within 24 hours and ask for corrections by a stated date; silence then counts as agreement.

A note on AI tools: an AI assistant can help draft minutes or a training outline, but never paste real client, colleague or company data into a public AI tool. Use approved internal tools only, and if your organization requires AI-generated text to be labeled, label it.

## Key terms
- **Stakeholder** — any person or group affected by a change or able to influence it.
- **Stakeholder analysis** — identifying stakeholders and assessing their influence, interest and needs.
- **Power/interest grid** — a 2×2 grid that sorts stakeholders by influence and interest to plan engagement.
- **RACI matrix** — a table assigning Responsible, Accountable, Consulted and Informed roles for each activity.
- **Accountable** — the single person who owns the outcome of an activity and approves it.
- **Onion diagram** — concentric rings showing how directly stakeholder groups are involved with a solution.
- **Communication plan** — a schedule of who receives which information, how often and through which channel.
- **Facilitator** — the person who guides a meeting's process so the group reaches its goal.
- **Parking lot** — a visible list of off-topic items captured for later handling.
- **Dot voting** — a quick prioritization technique where participants place a limited number of votes.
- **RAG status** — Red/Amber/Green rating of a project dimension's health.
- **Status report** — a regular, structured summary of progress, risks, issues and decisions needed.
- **Escalation** — passing a decision or issue to someone with more authority when it cannot be resolved at the current level.
- **Action item** — a task agreed in a meeting with an owner and a due date.
- **Learning objective** — a statement of what participants can do after a training session.
- **Cheat sheet** — a one-page quick reference for the most common tasks.

## Hands-on
:::exercise id="m16-e1" title="Power/interest grid and RACI for claim automation" min="45" tool="Miro"
**Goal:** practice identifying and structuring stakeholders for a realistic project.

1. In [Miro](https://miro.com/), list at least 10 stakeholders for "automating claim intake at ExportShield". Use the identification questions in the Deep dive. Add at least two that are not in the module's example.
2. Draw a 2×2 power/interest grid and place each stakeholder. Next to each, write one sentence on how you will engage them.
3. Build a RACI table with at least 7 activities (business case, approval rules, requirements, build, data protection assessment, UAT, go-live, training).
4. Check: exactly one A per row; no column that is only I's for someone you placed in "manage closely".
5. Write two sentences on the conflict you expect most and how you would handle it.

**Done when:** grid and RACI are complete, each row has one A, and you can explain every placement in one sentence.
:::

:::exercise id="m16-e2" title="Write a one-page weekly status report" min="30" tool="Word or Confluence"
**Goal:** produce a report a busy sponsor can read in two minutes.

1. Use the template from the Deep dive.
2. Invent a fictional week for the claim automation project with: one completed milestone, one risk that turns schedule to amber, one decision needed from the sponsor.
3. Write the summary in no more than three sentences.
4. Give each risk an owner, an action and a due date.
5. Ask someone outside IT to read it and tell you, in their own words, what the sponsor must do. If they cannot, rewrite.

**Done when:** the report fits on one page, RAG is justified, and an outsider can name the decision needed.
:::

:::exercise id="m16-e3" title="Present a proposed change in 5 minutes" min="90" tool="PowerPoint or Google Slides"
**Goal:** practice the problem → options → recommendation → ask structure under time pressure.

1. Choose a change: for example, the online credit limit request form, or removing the second approval for small claims (use your business case from module 03 if you have it).
2. Prepare at most 5 slides: Problem; Options (including "do nothing"); Recommendation with evidence; Plan and cost; Ask.
3. Write speaker notes of about 600–700 words.
4. Record yourself (any screen recorder or phone camera). Stop at exactly 5 minutes.
5. Watch the recording. Note three things: Did you state the ask clearly? Did you use jargon a manager would not know? Where did you lose time?
6. Re-record once with improvements.

**Done when:** you have a recording under 5 minutes with a clear ask on the final slide, and a short list of what you improved between takes. Use only fictional data.
:::

:::exercise id="m16-e4" title="Draft a 30-minute training plan" min="40" tool="Word or Confluence"
**Goal:** plan training that changes what people can do, not just what they have heard.

1. Topic: the new claim notification form with document checklist in ClaimDesk (fictional).
2. Write 2–3 learning objectives starting with "After this session you can…".
3. Plan the session minute by minute (objectives, why it changed, demo, hands-on, questions).
4. Write two hands-on tasks with fictional test data, each doable in 5 minutes.
5. Draft a one-page cheat sheet outline: three tasks with numbered steps, what changed, who to contact.
6. Define how you will check at the end whether people learned it.

**Done when:** the plan adds up to 30 minutes, every objective is practiced in a hands-on task, and the cheat sheet outline fits on one page.
:::

## Self-check
:::q
The compliance officer rarely attends project meetings but can block go-live. Where do they belong on the power/interest grid, and what does that mean for you?
---
High power, and at least at the start probably lower interest: "keep satisfied". You should involve them early at specific points (data flows, retention, access) with short, targeted information, rather than surprising them just before go-live, when their concerns would be most expensive to fix.
:::

:::q
A RACI row shows A for both the Head of Claims and the claims manager. Why is that a problem?
---
Accountability must sit with one person; with two, each may assume the other decides, or they may decide differently. Decisions then stall or conflict. Clarify who owns the outcome and make the other person R or C.
:::

:::q
In a workshop, one senior underwriter dominates and others stay silent. Name two facilitation techniques that help.
---
Round robin, where each participant contributes in turn, and silent brainstorming on sticky notes before discussion, which collects everyone's ideas independently. Dot voting afterward also gives each person equal weight in prioritization.
:::

:::q
Your project is one week behind on a milestone but you expect to recover next sprint. What RAG status should you report for schedule, and why?
---
Amber, if that matches the thresholds you agreed. It is at risk but there is a recovery plan. Reporting green hides information the sponsor may need; reporting amber early with a plan builds trust and avoids a sudden jump to red.
:::

:::q
During a call, a NovaSoft developer says: "Adding the turnover field is easy, we'll just do it." What do you do?
---
Thank them, but do not agree informally. Explain that it changes agreed scope, so it goes through the change request process with an impact estimate and sponsor approval. Record the discussion in writing. Otherwise cost and scope change without approval, and the contract no longer reflects what is being built.
:::

:::q
What is the difference between how you present the same recommendation to the steering committee and to NovaSoft's architects?
---
For the steering committee, focus on the problem, cost, benefit, risk and timeline, with the recommendation early and a clear decision ask. For the architects, keep the same structure but add interfaces, data, volumes, error handling and constraints, and ask for technical feedback or an estimate.
:::

:::q
What should meeting minutes contain, and what should they leave out?
---
They should contain participants, purpose, decisions, action items with owners and due dates, open questions and parked items. They should leave out a word-for-word record of the discussion and who said what, unless it matters for a decision.
:::

## Interview corner
:::interview
How do you handle two stakeholders with conflicting requirements?
---
- Document both requirements, their sources and reasons.
- Link each to business goals and the problem statement; quantify impact where possible.
- Look for a third option that meets both needs partly.
- Escalate to the accountable decision-maker with a clear recommendation; record the decision.
- Give a short example.

Typical mistake: deciding yourself which side is right, or simply picking the more senior person's view.
:::

:::interview
How do you keep stakeholders informed during a project?
---
- Identify and analyze stakeholders (power/interest grid).
- Agree a communication plan: who, what, how often, channel.
- Weekly status report with RAG, risks and decisions needed; honest amber/red.
- Demos at sprint reviews; involving users in testing.
- Adjust format to the person (report vs short call).

Typical mistake: describing only "I send emails" without structure or tailoring.
:::

:::interview
Tell me about a time you had to present something to people with a different background.
---
- Situation and audience: who, what they knew, what they needed.
- Structure: problem → options → recommendation → ask.
- What you adapted: language, level of detail, visuals.
- Result: decision taken, feedback received.
- What you would do differently.

Typical mistake: talking about the content of the presentation instead of how you adapted it to the audience.
:::

:::interview
How would you say no to a senior manager's request that is out of scope?
---
- Acknowledge the need behind the request.
- Explain the constraint factually: scope, budget, timeline, contract.
- Offer options: change request with impact, swap with a lower-priority item, later release.
- Let the right person decide; confirm in writing.

Typical mistake: either agreeing to avoid conflict, or refusing without offering any path forward.
:::
