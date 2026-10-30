---
id: 01
slug: ba-role
title: The IT Business Analyst role
phase: A
priority: P1
quick_min: 5
deep_min: 30
job_ad: "general"
---

## Why this matters
Before you learn any technique, you need a clear picture of the job itself: what a business analyst is paid for, what they produce, and who they work with. Every interview for an IT Business Analyst position starts with some version of "What does a BA do?" and "Why do you want to be one?". This module gives you the vocabulary to answer both, and shows that a good part of what you already do at work has a formal name.

## Quick version
A **business analyst (BA)** helps an organization change in a way that delivers value. In practice, an IT business analyst sits between the people who have a business need (underwriters, claims handlers, finance, management) and the people who build or configure IT systems (developers, testers, architects, external vendors). The BA makes sure both sides mean the same thing.

**What a BA does, in one sentence:** finds out what problem the business really has, describes what a solution must do in a form that IT can build and test, and checks that what was delivered actually solves the problem.

**Typical activities:**
- Talk to **stakeholders** (anyone affected by or influencing the change) to understand the problem. This is called **elicitation**.
- Model the current (**AS-IS**) and future (**TO-BE**) process.
- Write **requirements**: what the system must do (functional) and how well (non-functional, for example speed or security).
- Turn requirements into **user stories** with **acceptance criteria**, or into a **specification** for a vendor.
- Answer developers' and testers' questions, review test cases, support **UAT** (user acceptance testing, where business users confirm the solution works for them).
- Handle **change requests** when scope changes, and report status.

**Types of analysts.** The titles overlap a lot. A *business analyst* focuses on needs and processes. An *IT business analyst* adds the translation into system requirements. A *systems analyst* goes deeper into technical design (data, interfaces). A *process analyst* focuses on how work flows. A *data analyst* works with data and reports. A *product owner* in Scrum decides the order of the backlog and owns the product's value. A *project manager* owns time, budget and delivery. In small teams one person often does two or three of these.

**BABOK v3** (the *Business Analysis Body of Knowledge*, published by IIBA) is the main reference for the profession. At a rough level it describes:
- **6 knowledge areas**: planning and monitoring BA work; elicitation and collaboration; requirements life cycle management; strategy analysis; requirements analysis and design definition; solution evaluation.
- **4 requirement types**: business, stakeholder, solution (functional and non-functional), and transition requirements.
- **6 core concepts (BACCM)**: Change, Need, Solution, Stakeholder, Value, Context. Any BA situation can be described with these six words.

**The analyst mindset:** ask "why?" before "how?"; keep the problem separate from the proposed solution; switch between detail (one field on a form) and the big picture (the whole process and its cost).

**Where BAs work in the Czech market:** in-house at banks, insurers and car makers (you represent the business inside the company); on the vendor side at software companies (you write specifications and estimate work for the client); and at consultancies (short projects for many clients).

**You already do some of this.** If you have ever noticed a slow process, suggested automating it, discussed it with IT, got approval and tested the result, you have done problem identification, solution proposal, stakeholder management, sign-off and acceptance testing. This module shows the mapping, so you can describe your experience in BA language in an interview.

## Deep dive

### What a business analyst is for [P1]
Organizations change constantly: new products, new regulation, new systems, cost pressure. Each change costs money and carries risk. The business analyst exists to make sure the money is spent on the right change and that the change works.

A simple way to see the role is as a **bridge**. On one side is the business: people who know insurance, risk and clients, but not databases or APIs. On the other side is IT: people who know systems, but not why a credit limit decision needs a country rating. Both sides use their own vocabulary. Without a bridge, IT builds what it *heard*, not what the business *needed*.

Example at ExportShield Insurance: the claims department says "we need ClaimDesk to be faster". A developer could optimize database queries. A BA asks what "faster" means. It turns out claims handlers spend two hours per claim copying invoice data from PDF attachments into ClaimDesk. The real need is to stop re-typing data, not to speed up the database. That difference is the BA's value.

### Types of analysts and related roles [P1]
Job titles are not standardized. Read the job description, not just the title. The table shows typical focus areas.

| Role | Main question | Typical outputs | Technical depth |
|---|---|---|---|
| Business analyst | What does the business need and why? | Business case, problem statement, business requirements, process maps | Low to medium |
| IT business analyst | What must the system do to meet that need? | Functional and non-functional requirements, user stories, specifications for vendors | Medium |
| Systems analyst | How exactly will the system behave and integrate? | Data models, interface specifications, API mappings | Medium to high |
| Process analyst | How does work flow, and where is it lost? | BPMN models, process metrics, improvement proposals | Low to medium |
| Data analyst | What do the data say? | Reports, dashboards, SQL queries, data quality findings | Medium to high |
| Product owner (Scrum) | What should be built next to maximize value? | Ordered product backlog, product goal, acceptance decisions | Low to medium |
| Project manager | Will we deliver on time and budget? | Plan, budget, risk log, status reports | Low |

**Overlaps you will see in practice:**
- In agile teams the BA often writes stories that the **product owner** then prioritizes. In smaller teams the BA *is* the product owner.
- An IT BA at a bank often does systems analysis too: mapping fields between two systems, writing an API specification.
- On small projects the BA also writes the status report and runs meetings, which is project management work.

The target job ad for this course mixes IT BA, systems analysis (API, JSON/XML, SQL), process analysis (BPMN) and some low-code automation. That mix is common in mid-sized organizations.

### Typical deliverables [P1]
A **deliverable** is something concrete you hand over. Not every project needs all of them.

| Deliverable | What it is | Who uses it |
|---|---|---|
| Problem statement | A few sentences: what is wrong, for whom, impact, what success looks like | Sponsor, team |
| Business case | Costs, benefits, risks, recommendation | Management, approvers |
| Stakeholder map | Who is involved, influence, interest | BA, project manager |
| AS-IS / TO-BE process model | Diagrams, often in BPMN 2.0 | Business, IT, testers |
| Business requirements document (BRD) or requirements list | Numbered requirements with priority | Everyone |
| User stories with acceptance criteria | Small pieces of work in a backlog | Developers, testers |
| Functional specification | Detailed behavior: screens, rules, validations, interfaces | Vendor, developers |
| Data mapping / interface specification | Which field goes where, formats (JSON, XML) | Developers, integrators |
| Traceability matrix | Links each requirement to design, tests and defects | BA, test lead, auditors |
| Change request | A documented change to agreed scope, with impact | Vendor, project manager |
| UAT support materials | Test scenarios, test data, sign-off record | Business testers |
| Training material, release notes | How to use the new feature | End users |

In regulated industries (banking, insurance) the paper trail matters. Auditors may ask who approved a requirement and how it was tested. **Traceability** and **sign-off** records are part of the job, not bureaucracy for its own sake.

### A week in the life [P2]
An illustrative week for an IT BA at ExportShield, working on automating claim intake with the external vendor NovaSoft s.r.o.:

- **Monday.** Daily stand-up with the delivery team (15 minutes). Review two questions from NovaSoft developers about how to calculate the claim amount when part of the invoice was already paid. Check the business rule with the claims manager, update the specification, reply in Jira.
- **Tuesday.** 90-minute workshop with three claims handlers to walk through the TO-BE process. Discover that documents for claims above a certain amount need a second approver. Add a requirement, mark it as needing sign-off.
- **Wednesday.** Write five user stories for the next sprint, each with acceptance criteria. Run a short SQL query on the test database to check what claim statuses exist, because the story depends on them.
- **Thursday.** Backlog refinement with the product owner and developers. One story is too big, so you split it. The vendor estimates that a new field in PolicyHub is outside the agreed scope; you start a change request.
- **Friday.** Review test cases written by the tester against acceptance criteria. Help a business user run UAT scenarios for the previous release. Send the weekly status report: green on scope, amber on schedule because of the change request.

Notice the ratio: a large share of time is conversation and clarification, a smaller share is writing documents. Juniors often expect the opposite.

### BABOK v3 at a rough level [P2]
BABOK v3 (IIBA, 2015) is a body of knowledge, not a method. It describes *what* business analysis covers, not a fixed sequence of steps. You do not need to memorize it for a junior role, but the vocabulary appears in interviews and in certifications such as ECBA or CCBA.

**Six knowledge areas** (groups of tasks), in plain words:

1. **Business Analysis Planning and Monitoring** — deciding how you will do the analysis on this project: which stakeholders, which techniques, how requirements will be approved and changed.
2. **Elicitation and Collaboration** — getting information from people and documents (interviews, workshops, observation) and confirming you understood it.
3. **Requirements Life Cycle Management** — looking after requirements from creation to retirement: tracing, prioritizing, approving, handling changes.
4. **Strategy Analysis** — understanding the current state, defining the desired future state, and the gap and risks between them. This is where the business case lives.
5. **Requirements Analysis and Design Definition** — structuring and modeling requirements, checking their quality, and describing possible solution designs.
6. **Solution Evaluation** — checking whether a delivered solution actually delivers the expected value, and why not if it does not.

**Four requirement types:**

| Type | Meaning | ExportShield example |
|---|---|---|
| Business requirement | Goal of the organization | Reduce average claim processing time from 15 to 7 working days |
| Stakeholder requirement | Need of a specific group | Claims handlers need invoice data available without re-typing |
| Solution requirement — functional | What the system does | ClaimDesk extracts invoice number, date and amount from an uploaded PDF |
| Solution requirement — non-functional | How well the system does it | Extraction finishes within 30 seconds for a 10-page PDF |
| Transition requirement | Needed only to move from old to new state | Migrate open claims from Excel tracker into ClaimDesk before go-live |

(The numbers in the examples are illustrative.)

**The six core concepts (BACCM — Business Analysis Core Concept Model)**, in plain words:

- **Change** — the act of transformation. Something will be different afterwards.
- **Need** — a problem or opportunity that motivates the change.
- **Solution** — a specific way of satisfying the need.
- **Stakeholder** — a person or group with a relationship to the change, the need or the solution.
- **Value** — the worth or usefulness of something to a stakeholder. It can be money, time, lower risk, compliance.
- **Context** — the circumstances that influence and are influenced by the change: regulation, culture, existing systems, market.

The concepts are useful as a checklist. If you cannot say what the *need* is, or for which *stakeholder* the *value* arises, the initiative is not ready.

### The analyst mindset [P1]
Techniques can be learned from a book. These habits take practice.

**Ask "why?" before "how?".** Requests usually arrive as solutions: "add a button", "send an email", "buy a tool". Ask what happens today, what goes wrong, and what would change if the request were done. Often the stated solution is not the best one.

**Separate problem, symptom and solution.** "Claims are late" is a symptom. "Invoice data is re-typed by hand from PDFs, and every third claim waits for missing documents" is closer to a problem. "Buy an OCR tool" is one possible solution. The module on problem and process analysis covers this in detail.

**Hold detail and big picture at the same time.** One moment you are checking whether the invoice date can be in the future; the next you are explaining to the head of claims how the change affects the whole process. Good BAs zoom in and out on purpose.

**Be neutral.** You represent the need, not one department or the vendor. When underwriting and claims want different things, you make the trade-off visible and let the decision-maker decide.

**Write things down and confirm.** A requirement that exists only in a meeting is not a requirement. Summarize, send, get confirmation.

**Say "I don't know yet, I'll find out".** Interviewers like this. Guessing about business rules creates defects.

### Where BAs work in the Czech market [P2]
The same title can mean different jobs depending on which side of the table you sit on.

| Setting | Who pays you | Typical work | Pros | Cons |
|---|---|---|---|---|
| In-house (bank, insurer, car maker, investment group) | The organization that uses the system | Gather needs from departments, write specifications for vendors, accept deliveries, run UAT | Deep domain knowledge, long-term view, see the result in use | Slower pace, more internal politics, many vendors to coordinate |
| Vendor side (software company, system integrator) | The client, through a contract | Turn client requirements into designs, estimate, clarify with client, support delivery | Strong technical exposure, many projects | Scope fights, change requests, client pressure |
| Consultancy | Clients, usually short engagements | Assessments, process redesign, selection of software, regulatory projects | Variety, fast learning | Travel, short contact with results, high expectations |

Banks and insurers in Czechia often buy core systems from external vendors and keep the BA role in-house to control what is ordered. That matches the target job ad: "requirements from departments → technical specifications for the vendor". Automotive companies have many BA roles in production, logistics and sales IT, often in English-speaking teams. Regulated clients (banking, insurance) add requirements around security, audit trail and data protection, which a BA must capture as non-functional requirements.

### What you already do and what it's called [P1]
If you have improved processes at work without the title, you have relevant experience. The key is to describe it in BA language and to be honest about the scale.

| What you already do | What it's called | BABOK area |
|---|---|---|
| Notice that a task takes too long or causes errors | Problem identification, pain point analysis | Strategy Analysis |
| Count how often it happens and how long it takes | Process measurement, baseline | Strategy Analysis |
| Ask colleagues how they do it | Elicitation (interviews, observation) | Elicitation and Collaboration |
| Sketch the steps on paper | AS-IS process modeling (describing the current state) | Strategy Analysis |
| Propose "this could be automated" | Solution proposal, TO-BE process, business case | Strategy Analysis |
| Explain to IT what you need | Requirements specification | Requirements Analysis and Design Definition |
| Agree with your manager that it is worth doing | Stakeholder engagement, approval, sign-off | Requirements Life Cycle Management (approval); stakeholder engagement is planned in Planning and Monitoring |
| Answer IT's questions while they build it | Requirements clarification, managing requirements | Requirements Life Cycle Management |
| Try it out before it goes live | User acceptance testing (UAT) | Solution Evaluation |
| Show colleagues how to use it | Training, transition support | Transition requirements (Requirements Analysis and Design Definition) |
| Check later that it actually saves time | Benefits realization, solution evaluation | Solution Evaluation |

In an interview, avoid "I just helped a bit with IT". Say instead: "I identified a manual step in our claim process, measured roughly how much time it took, proposed an automation, agreed requirements with IT, and tested it before go-live." Then give one concrete detail. Do not exaggerate: if IT wrote the specification, say you provided input to it.

### What a BA is not [P3]
Clearing up misconceptions helps in interviews:
- **Not a secretary for requirements.** Writing down what people say is not analysis. Analysis means questioning, structuring and finding gaps.
- **Not the decision-maker.** The sponsor or product owner decides. The BA prepares the decision.
- **Not a developer.** You need to understand APIs, data and SQL well enough to specify and check, not to build production code. Low-code automation is a grey zone, and the target job ad expects some of it.
- **Not a tester.** But you work closely with testers, and in smaller teams you may test yourself.

## Key terms
- **Business analyst (BA)** — a person who identifies needs and defines changes that deliver value to stakeholders.
- **Stakeholder** — any person or group affected by a change or able to influence it.
- **Elicitation** — drawing out information from stakeholders and other sources, for example through interviews or workshops.
- **Requirement** — a documented statement of a need or capability that a solution must have.
- **Business requirement** — a high-level goal of the organization that justifies the change.
- **Stakeholder requirement** — a need of a particular stakeholder group, bridging business and solution requirements.
- **Solution requirement** — a capability (functional) or quality (non-functional) the solution must have.
- **Transition requirement** — a temporary requirement needed only to move from the current to the future state, such as data migration.
- **BABOK v3** — the Business Analysis Body of Knowledge from IIBA, the main reference guide of the profession.
- **BACCM** — the Business Analysis Core Concept Model: Change, Need, Solution, Stakeholder, Value, Context.
- **AS-IS / TO-BE** — the current state of a process and the intended future state.
- **Deliverable** — a concrete output handed over to someone, such as a specification or process model.
- **Sign-off** — formal approval of a deliverable by an authorized stakeholder.
- **Traceability** — the ability to follow a requirement to its source, design, tests and defects.
- **Product owner** — the Scrum accountability for maximizing product value and ordering the product backlog.
- **UAT (user acceptance testing)** — testing by business users to confirm the solution meets their needs before go-live.
- **Pain point** — a specific problem or frustration in a current process.

## Hands-on
:::exercise id="m01-e1" title="Map your own improvement to the BA lifecycle" min="45" tool="draw.io"
**Goal:** describe one improvement you initiated at work in BA language, ready for an interview.

1. Pick one improvement you drove or contributed to (automation, new form, changed approval flow). Leave out client names, amounts and any internal data. Use generic words such as "a monthly report" or "an approval request".
2. Open [draw.io](https://app.diagrams.net/) and draw seven boxes in a row: Problem identified → Measured → Proposed solution → Agreed requirements → Approval → Testing → Rollout and evaluation.
3. Under each box, write one or two sentences about what you actually did in that stage. If you skipped a stage, write "skipped" and why.
4. Under each box, add the formal term from the table "What you already do and what it's called".
5. Write a 5-sentence summary in the STAR format (Situation, Task, Action, Result, plus one learning).

**Done when:** you have the diagram and a 5-sentence story you can say aloud in under 90 seconds, with no confidential information.
:::

:::exercise id="m01-e2" title="Rate yourself against the target job ad" min="40" tool="Excel or Google Sheets"
**Goal:** know your gaps and plan which modules to study first.

1. Create a table with columns: Requirement, My evidence, Rating 0–3, Module that covers it (fill in from the course overview).
2. Enter each item from the target job ad as a row: requirements from departments → technical specifications for vendors; feature design aligned with architecture; working with vendors and stakeholders; supporting testers and testing deliveries; status reporting; low-code automation; presentations and training; AI in processes; logical thinking; basic SQL; API, JSON/XML; algorithmic thinking (programming / low-code / technical specs); UML or BPMN; presenting.
3. Rate yourself: 0 = never heard of it, 1 = know the term, 2 = done it with help, 3 = done it on my own.
4. For each rating of 0 or 1, find the module of this course that covers it.
5. Pick the three lowest-rated items. These are your first study priorities.

**Done when:** every row has a rating and evidence (or "none yet"), and you have a list of three priorities.
:::

:::exercise id="m01-e3" title="Prepare an informational interview with a working BA" min="60" tool="LinkedIn"
**Goal:** hear from a practicing BA how the job looks in reality.

1. On LinkedIn, find 3–5 people with "Business Analyst" in their title at a bank, insurer or software vendor. Prefer people one or two steps ahead of you, not senior managers.
2. Send a short, polite message: who you are (career changer interested in BA), what you ask (20 minutes, online), and that you will not ask for a job. Keep it under 400 characters.
3. Prepare 8 questions. Suggested: What did you do last week? Which deliverables do you write most? Which tools? How much SQL or API work? How did you get your first BA role? What do juniors get wrong? What would you learn first? Is there anything you would not do again?
4. After the conversation, write a half-page summary and compare it with the "week in the life" section above.
5. Send a thank-you message the same day.

**Done when:** you have the message drafted, the question list ready, and (once someone agrees) a written summary. Do not share anything confidential from your own employer during the conversation.
:::

## Self-check
:::q
A colleague says: "A BA just writes down what the business wants and sends it to IT." What is missing from that description?
---
It misses the analysis. A BA questions the request to find the real need, checks it against other stakeholders' needs, structures requirements, finds gaps and conflicts, and later checks that the delivered solution works. Writing down is only the output; the value is in the questioning and structuring before it.
:::

:::q
What is the practical difference between an IT business analyst and a product owner?
---
The IT BA focuses on understanding needs and describing what the solution must do in detail (requirements, stories, specifications). The product owner is accountable for the value of the product and decides the order of the backlog. In many teams the BA prepares and refines backlog items and the PO prioritizes them; in small teams one person can do both.
:::

:::q
Classify this requirement: "Before go-live, all open claims from the Excel tracker must be loaded into ClaimDesk."
---
It is a transition requirement. It is needed only to move from the current state to the future state and has no meaning once the migration is done. It still needs an owner, acceptance criteria and testing.
:::

:::q
Name the six BACCM core concepts and apply them to automating credit limit request intake at ExportShield.
---
Change: requests are no longer typed in by hand. Need: underwriters lose time re-typing and make errors. Solution: a web form that feeds PolicyHub directly. Stakeholders: exporters, underwriters, IT, NovaSoft. Value: shorter response time, fewer errors. Context: regulated insurer, an external vendor system, existing email habits of clients.
:::

:::q
Why do banks and insurers in Czechia often keep the BA role in-house even when a vendor builds the system?
---
Because they need someone who represents the organization's interests and knows its processes and regulation. The in-house BA defines what is ordered, checks the vendor's understanding, handles change requests and accepts the delivery. Leaving all of this to the vendor creates a conflict of interest and weak control over scope.
:::

:::q
A manager asks you to "add an export button to ClaimDesk". What do you do first, and why?
---
Ask why the export is needed and what happens with the exported data today. The request is a solution; the underlying need might be a report, a data feed to another team, or an audit request. Once the need is clear, the export button may still be right, or a scheduled report may serve the need better.
:::

## Interview corner
:::interview
What does a business analyst do?
---
- Bridge between business and IT: understand the need, describe the solution, check it was delivered.
- Mention concrete activities: elicitation, process modeling, requirements and user stories, supporting testing and UAT, change management.
- Give one short example (from your own experience, in BA terms).
- Mention value: the right change, done right, saves money and risk.

Typical mistake: describing the BA as a note-taker or as a mini project manager without mentioning analysis.
:::

:::interview
You have no formal BA job title. Why should we hire you?
---
- Map your current work to BA activities: problem identification, proposal, agreement with IT, approval, testing.
- Give one STAR story with a measurable or at least concrete result.
- Show what you did to close gaps: this course, tools you tried (BPMN, SQL, Jira), a portfolio case study.
- Domain knowledge: you understand insurance, approval processes and regulated environments.

Typical mistake: apologizing for lack of experience instead of translating the experience you have.
:::

:::interview
What is the difference between a business requirement and a functional requirement?
---
- Business requirement: a goal of the organization, for example shorter claim processing time.
- Functional requirement: a specific behavior of the solution, for example extracting invoice data from an uploaded PDF.
- Explain the chain: business → stakeholder → solution (functional and non-functional), plus transition requirements.
- One example of each from the same project.

Typical mistake: giving two functional requirements and calling one of them "business" because it sounds important.
:::

:::interview
How do you handle a stakeholder who already has a solution in mind?
---
- Take the idea seriously and write it down.
- Ask about the problem behind it: what happens today, what goes wrong, how often, what it costs.
- Compare the proposed solution with alternatives against the need.
- If the proposed solution is good, say so; if not, show the trade-off with facts and let the decision-maker decide.

Typical mistake: either building the requested solution without questions, or rejecting it to prove you know better.
:::
