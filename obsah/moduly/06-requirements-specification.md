---
id: 06
slug: requirements-specification
title: Writing requirements and specifications
phase: B
priority: P1
quick_min: 5
deep_min: 45
job_ad: "tvořit technické specifikace pro dodavatele"
---

## Why this matters
The job ad says it plainly: you will turn requirements from departments into specifications for vendors. A vendor builds what is written, not what was meant. Every vague sentence becomes either a defect, a change request with a price tag, or an argument in UAT. Writing requirements that are clear, testable and traceable is the most visible part of a BA's output, and interviewers often ask you to improve a bad requirement on the spot.

## Quick version
A **requirement** is a statement of a need or capability that a solution must meet. A **specification** is a document that collects requirements in an agreed structure, so that someone else (a vendor, a developer, a tester) can build and verify the solution.

**Good requirements are** (the characteristics come from ISO/IEC/IEEE 29148 and IREB CPRE, in slightly different wording):
- **Unambiguous** – only one possible interpretation.
- **Verifiable** – a tester can prove it is met.
- **Atomic** (singular) – one requirement per statement, no "and also".
- **Consistent** – does not contradict other requirements.
- **Feasible** – can be built within the constraints.
- **Necessary** – traces back to a real business need.
- **Traceable** – has a unique ID and a known source.

**Sentence template:** `[ID] The system shall [action] [object] [condition / constraint].`
Example: *FR-012 The system shall retrieve the buyer's name and registered address from ARES within 5 seconds after a valid 8-digit registration number is entered.* "Shall" marks a mandatory requirement; "should" a desirable one; "will" a statement of fact. Pick a convention and state it in the document.

**Functional vs non-functional.** A **functional requirement** says what the system does (calculate, display, send, validate). A **non-functional requirement** (quality requirement) says how well or under which constraints: performance, security, availability, usability, auditability, compliance. Non-functional requirements must be measurable: "99.5 % availability during business hours (Mon–Fri 8:00–18:00 CET)", not "highly available".

**Business rules** are policies of the organization that the system must enforce: "Credit limits above 1,000,000 EUR require Risk Committee approval." Keep them in a separate list with their own IDs, because they change independently of the software.

**Common documents:**
- **BRD** (Business Requirements Document) – why, goals, scope, business and stakeholder requirements.
- **FRS / functional specification** – what the solution does in detail: functions, screens, data, rules.
- **SRS** (Software Requirements Specification) – complete software requirements, functional and non-functional, often in IEEE style.
- **Technical specification** – how it will be built: architecture, interfaces, database. Usually written by the vendor or architect.

Names vary between companies. What matters is that the vendor gets a document that states context, scope, out of scope, actors, process, numbered functional requirements, UI, data, integrations, non-functional requirements, acceptance criteria and open questions.

**Use cases** describe the interaction between an actor and the system step by step: main flow, alternative flows, exception flows. They are a good way to find missing requirements.

**Prioritization:** **MoSCoW** – Must have, Should have, Could have, Won't have (this time).

**Traceability matrix:** a table linking each requirement to its source, the business goal, design elements and test cases. It answers "why is this here?" and "is this tested?".

**After writing:** review with stakeholders and the vendor, version the document, get **sign-off** (formal approval), and handle later changes through **change requests**.

**Words to avoid:** fast, user-friendly, flexible, etc., and/or, if possible, appropriate, as needed, support, minimal, robust.

**Interview one-liner:** "I write atomic, testable requirements with IDs, separate business rules and NFRs with measurable values, and keep a traceability matrix from business goal to test case."

## Deep dive

### What makes a requirement good [P1]
ISO/IEC/IEEE 29148 (the international standard for requirements engineering) and the IREB CPRE syllabus both list quality characteristics for individual requirements. The wording differs a little, and so do the editions: the current 29148 (2018) lists necessary, appropriate, unambiguous, complete, singular, feasible, verifiable, correct and conforming for a single requirement, and treats consistency as a property of the whole set of requirements; the older 2011 edition also named traceable and implementation-free. This table uses the common core:

| Characteristic | Meaning | Bad | Better |
|---|---|---|---|
| Unambiguous | One interpretation only | "The system shall display recent requests." | "The system shall display credit limit requests created in the last 30 calendar days." |
| Verifiable | Can be proven by inspection, analysis, demonstration or test | "The form shall be easy to use." | "A new user shall complete a credit limit request without help in under 5 minutes in a usability test with 5 users." |
| Atomic (singular) | One need per statement | "The system shall validate and save the request and notify the underwriter." | Three requirements: validate, save, notify. |
| Consistent | No contradiction with other requirements | FR-10 says limit in EUR, FR-22 says limit in exporter's currency | Agree one rule and reference it. |
| Feasible | Achievable within budget, time, technology | "The lookup shall always return in 0 seconds." | "…within 5 seconds for 95 % of requests." |
| Necessary | Removing it would leave a need unmet | "The screen shall show a weather widget." | Remove it. |
| Complete | Contains all information needed | "The system shall send a notification." | Who, when, which channel, which content. |
| Traceable | Unique ID, known source and links | Bullet point without ID | "FR-014, source: interview with Underwriting, 12 March, BR-02." |
| Implementation-free | States what, not how (unless a constraint) | "Store the limit in an Oracle table." | "The system shall store the approved limit…" (database choice is design). |

A practical test for every requirement: *Could two people build different things from this sentence?* and *How would a tester prove it?* If either answer is uncomfortable, rewrite.

### Sentence templates [P1]
Templates make requirements consistent and easier to review. A widely used pattern (similar to the IREB requirement template):

`[ID] [When/If <condition>,] the system shall [<action verb>] [<object>] [<qualifier / constraint>].`

Examples for ExportShield:
- *FR-001* The system shall allow an exporter to submit a credit limit request for one buyer.
- *FR-002* When the exporter enters a buyer registration number, the system shall validate that it consists of exactly 8 digits.
- *FR-003* If the registration number is valid, the system shall retrieve the buyer's name, legal form and registered address from ARES.
- *FR-004* If ARES returns no record, the system shall display the message "Buyer not found in the registry. Please check the number or enter the details manually." and allow manual entry.
- *FR-005* The system shall assign each submitted request a unique request number in the format CLR-YYYY-NNNNN.

Keyword conventions (state them in the document):
- **shall** = mandatory,
- **should** = desirable, negotiable,
- **may** = optional,
- **will** = statement of fact or intention, not a requirement.

"Must" is also common in modern documents. The point is consistency.

### Functional requirements [P1]
Functional requirements describe behavior: inputs, processing, outputs. Typical verbs: create, display, calculate, validate, send, store, search, export, assign, notify. Group them by function or by process step so readers can find them (for example "3.1 Request submission", "3.2 Buyer lookup", "3.3 Assessment", "3.4 Decision and notification").

Every functional requirement should state *who* (which actor or which trigger), *what*, and *under which condition*. Error handling is also functional: what happens on invalid input, missing data, timeout. Beginners forget these, and vendors then implement whatever is cheapest.

### Non-functional requirements [P1]
Non-functional requirements (NFRs) describe qualities and constraints. They are often decided by IT, security or compliance, not by the business users, so invite those people early. Each NFR needs a number or a verifiable condition.

| Category | Vague | Measurable example |
|---|---|---|
| Performance | "The system shall be fast." | "The buyer lookup shall return a result within 5 seconds for 95 % of requests at a load of 50 concurrent users." |
| Availability | "The portal shall be always available." | "The exporter portal shall be available 99.5 % of the time Mon–Fri 7:00–19:00 CET, measured monthly, excluding announced maintenance." |
| Security | "Data shall be secure." | "Users shall authenticate with multi-factor authentication. Exporters shall see only requests of their own company." |
| Usability | "The form shall be intuitive." | "All mandatory fields shall be marked and each validation error shall be shown next to the field it concerns." |
| Auditability | "Changes shall be logged." | "The system shall record user ID, timestamp, old value and new value for every change of a credit limit decision, and keep the record for 10 years." |
| Compliance | "The system shall be GDPR-compliant." | "Personal data of buyer contact persons shall be deleted or anonymized no later than X years after the policy ends, as defined by the data retention policy." |
| Capacity | "The system shall handle many requests." | "The system shall support at least 2,000 credit limit requests per month." |
| Recoverability | "Data shall not be lost." | "After an outage, the service shall be restored within 4 hours, with data loss of at most 15 minutes." |

Two of these terms come up in interviews: **RTO** (Recovery Time Objective, how long until the service is back, here 4 hours) and **RPO** (Recovery Point Objective, how much data may be lost, here 15 minutes).

Retention periods and legal obligations must come from the legal or compliance team. Do not guess them; write "X years per retention policy, to be confirmed by Compliance" and put it in open questions.

### Business rules [P1]
A **business rule** is a policy or regulation that constrains or defines the business, independent of any system. Examples:
- *BR-01* A credit limit request above 1,000,000 EUR requires Risk Committee approval.
- *BR-02* A credit limit cannot be approved for a buyer in a country with risk rating 7 unless the CEO approves an exception.
- *BR-03* Payment terms longer than 180 days are not insurable under the standard policy.

Why separate them: rules change when management decides, not when the software changes. A functional requirement then *references* the rule: *FR-031 The system shall route the request to the Risk Committee queue when BR-01 applies.* If the threshold changes to 1.5 M EUR, only BR-01 changes. Complex rule sets can be represented as decision tables (see DMN in module 04).

### Data requirements [P1]
Vendors need exact data definitions. A **data dictionary** table is the clearest format:

| Field | Description | Type / format | Mandatory | Validation | Source |
|---|---|---|---|---|---|
| request_no | Unique request number | Text, `CLR-YYYY-NNNNN` | Yes (system) | Generated, unique | System |
| buyer_reg_no | Buyer registration number (IČO for Czech buyers) | Text, 8 digits | Yes for CZ buyers | Exactly 8 digits, checksum per registry rules | Exporter |
| buyer_name | Legal name of the buyer | Text, max 255 chars | Yes | Not empty | ARES or manual |
| country_code | Buyer country | ISO 3166-1 alpha-2 (e.g. `DE`) | Yes | From country list | Exporter |
| requested_amount | Requested credit limit | Decimal, 2 places, > 0 | Yes | 1,000 – 50,000,000 | Exporter |
| currency | Currency of the amount | ISO 4217 (e.g. `EUR`) | Yes | EUR, USD, CZK | Exporter |
| payment_terms_days | Agreed payment terms | Integer | Yes | 1 – 180 (see BR-03) | Exporter |
| status | Request status | Enum | Yes (system) | Submitted, In assessment, Approved, Reduced, Rejected | System |

Standards such as ISO 3166 (country codes) and ISO 4217 (currency codes) save you from defining your own lists. Data modeling is covered in module 09.

### Documents: BRD, FRS, SRS, technical specification [P1]
Companies use these names inconsistently, so always ask "what does your template contain?" A typical division:

| Document | Main question | Typical content | Typical author | Reader |
|---|---|---|---|---|
| Business case | Should we do this? | Problem, options, costs, benefits | BA / sponsor | Management |
| BRD | Why and what at business level? | Goals, scope, stakeholders, business and stakeholder requirements, AS-IS/TO-BE process | BA | Sponsor, business, vendor |
| FRS / functional specification | What exactly does the solution do? | Functional requirements, use cases, UI, data, business rules, integrations (functional view), NFRs | BA | Vendor, developers, testers |
| SRS | Complete software requirements | Similar to FRS, often IEEE/ISO structure, strong on NFRs | BA / requirements engineer | Developers, testers |
| Technical specification / design | How will it be built? | Architecture, components, API contracts, database, deployment | Vendor / architect | Developers, IT operations |

In vendor projects the client usually writes the functional specification, and the vendor answers with a technical design or a solution description. Your specification is often an attachment to the contract, so precision has financial consequences.

### Template: vendor-facing functional specification [P1]
A structure that works for a change such as "automated ARES check in the credit limit request":

1. **Document control** – title, version, date, author, status (draft / in review / approved), change history, approvers.
2. **Context and goal** – business problem, business requirements with IDs, link to BRD. Two paragraphs, not two pages.
3. **Scope** – what is included. **Out of scope** – what is explicitly not included (this section prevents most disputes).
4. **Assumptions and constraints** – for example "PolicyHub version X remains", "ARES public API is used, no SLA available".
5. **Actors and roles** – exporter, underwriter, head of underwriting, system actors (ARES, PolicyHub), with permissions.
6. **Process** – TO-BE BPMN diagram and a short description of each step.
7. **Functional requirements** – numbered (FR-001…), grouped by function, each with priority and source. Use cases where useful.
8. **Business rules** – BR-01…, referenced from FRs.
9. **User interface** – wireframes, field list per screen, messages and error texts.
10. **Data** – data dictionary, validation, data retention.
11. **Integrations** – for each interface: systems, direction, trigger, data fields, format (JSON/XML), frequency, error handling, who owns the interface.
12. **Non-functional requirements** – performance, availability, security, auditability, compliance, with numbers.
13. **Reporting** – which reports or exports, fields, filters.
14. **Transition requirements** – migration, training, rollout.
15. **Acceptance criteria and UAT approach** – how the client will accept the delivery, key test scenarios.
16. **Open questions and decisions log** – ID, question, owner, due date, answer.
17. **Glossary** – domain terms (buyer, credit limit, IČO, indemnity).

### Use case specification [P1]
A **use case** describes how an actor uses the system to achieve a goal, as a sequence of steps. It is useful because walking through the steps reveals missing requirements, especially in error cases. Use case diagrams belong to UML (module 08); here we focus on the textual specification.

**Example: UC-03 Look up buyer in registry**

| Item | Content |
|---|---|
| ID / name | UC-03 Look up buyer in registry |
| Primary actor | Exporter (portal user) |
| Secondary actor | ARES (external registry) |
| Goal | Buyer details are filled in from the official registry without retyping |
| Preconditions | Exporter is logged in; the credit limit request form is open; the buyer country is selected |
| Trigger | Exporter enters the buyer registration number and selects "Look up" |
| Postconditions (success) | Buyer name, legal form and address are shown read-only on the form and stored with the request together with the lookup timestamp |
| Related | BR-G1, FR-002 – FR-006, NFR-P01 |

**Main flow**
1. The exporter enters the 8-digit registration number and selects "Look up".
2. The system validates the format of the number.
3. The system sends a request to ARES with the registration number.
4. ARES returns the company record.
5. The system displays name, legal form and registered address as read-only fields.
6. The system stores the retrieved data and the timestamp of the lookup with the draft request.
7. The use case ends.

**Alternative flows**
- *A1 – Buyer country is not CZ (before step 1):* the system hides the "Look up" button and the exporter enters buyer details manually. The request is flagged "Manual buyer data".
- *A2 – Exporter changes the number after a successful lookup (after step 5):* the system clears the retrieved fields and returns to step 2.

**Exception flows**
- *E1 – Invalid format (at step 2):* the system shows "Registration number must have 8 digits" next to the field. The flow returns to step 1.
- *E2 – Buyer not found (at step 4):* the system shows "Buyer not found in the registry. Please check the number or enter the details manually." and enables manual entry. The request is flagged "Manual buyer data".
- *E3 – ARES not available or no response within 10 seconds (at step 4):* the system shows "The registry is temporarily unavailable. You can enter the details manually or try again later." and enables manual entry. The system logs the error. The request is flagged "Manual buyer data" so the underwriter verifies it.
- *E4 – Buyer is marked as dissolved or in liquidation in ARES (at step 4):* the system shows the data with a warning and flags the request for the underwriter.

Each flow translates into requirements and into test cases. The "Manual buyer data" flag, for instance, was not mentioned by any stakeholder; it appeared because the exception flows forced the question "what happens next?". Whether ARES actually returns liquidation status in the fields you need is a question for the integration analysis, so you would log it as an open question.

### Prioritization [P1]
**MoSCoW** is the most common technique:
- **Must have** – without it the solution is not acceptable or not legal.
- **Should have** – important, but there is a workaround.
- **Could have** – nice to have if time and budget allow.
- **Won't have (this time)** – agreed out of scope for this release, recorded so the topic does not come back every week.

A warning sign: 80 % of requirements marked "Must". Ask "What happens if we go live without this?" If the answer is "we would manage", it is not a Must.

**Kano model** [P3] classifies features by how they affect satisfaction: *basic* (expected; missing means dissatisfaction, present goes unnoticed, for example the request is saved), *performance* (more is better, for example faster decisions), and *delighters* (unexpected, create enthusiasm, for example automatic pre-fill from the registry). Over time, delighters become basic expectations.

Other techniques exist (ranking, 100-point voting, cost-value matrix), but MoSCoW is what you will meet most.

### Traceability matrix [P1]
**Traceability** is the ability to follow a requirement backward to its source and forward to design, implementation and tests. A **requirements traceability matrix (RTM)** is the simplest tool, usually a spreadsheet:

| Req ID | Requirement (short) | Source | Business req. | Priority | Design / spec section | Test case(s) | Status |
|---|---|---|---|---|---|---|---|
| FR-002 | Validate 8-digit registration number | Interview Underwriting 12 Mar | BR-G1 | Must | 7.2 | TC-010, TC-011 | Approved |
| FR-003 | Retrieve buyer data from ARES | Workshop 19 Mar | BR-G1 | Must | 7.2, 11.1 | TC-012 | Approved |
| FR-004 | Message when buyer not found | UC-03 E2 | BR-G1 | Must | 7.2, 9 | TC-013 | Approved |
| NFR-P01 | Lookup within 5 s for 95 % | IT Operations | BR-G2 | Should | 12 | TC-040 | In review |

It answers practical questions: Which requirements have no test? Which tests break if FR-003 changes? Was this requirement requested by anyone? In tools like Jira, links between issues do the same (module 07).

### Versioning, review and sign-off [P1]
**Versioning:** use version numbers (0.1, 0.2 for drafts, 1.0 for the first approved version, 1.1 for approved changes) and a change history table: version, date, author, what changed. Keep one master copy in a shared location such as Confluence or SharePoint, never versions in e-mail attachments.

**Review:** before sign-off, the specification is reviewed by:
- business stakeholders (is it what we need?),
- the vendor or developers (is it clear and feasible? what is missing?),
- testers (is it testable?),
- IT security, architecture, compliance where relevant.

A walkthrough meeting where you go through the document section by section is more effective than "please comment by Friday". Record comments and their resolution.

**Sign-off** is the formal approval of a version by the people responsible (product owner, process owner, sometimes the vendor). It creates a baseline: from this point, changes are managed.

### Change control and change requests [P1]
After sign-off, requirements will still change: legislation changes, someone remembers an exception, UAT reveals a gap. **Change control** is the agreed process for handling this. A **change request (CR)** typically contains:
- ID, title, requester, date,
- description of the change and reason,
- affected requirements and documents (the traceability matrix helps here),
- impact analysis: effort, cost, schedule, risk (often estimated by the vendor),
- priority, decision (approved / rejected / deferred), approver, date.

In a fixed-price vendor contract, CRs usually mean extra cost, which is one reason the original specification must be precise. In agile setups, changes go into the backlog and are prioritized like any other item, but contractual scope may still require a formal CR.

### Ambiguity words to avoid [P1]
| Word or phrase | Problem | Replace with |
|---|---|---|
| fast, quickly, real time | No number | "within 5 seconds" |
| user-friendly, intuitive, easy | Not testable | Specific usability criteria |
| etc., and so on | Incomplete list | The full list |
| and/or | Unclear combination | Two requirements or explicit logic |
| if possible, ideally | Not a requirement | Decide: shall or remove |
| appropriate, adequate, sufficient | Who decides? | The exact criterion |
| support, handle | What exactly? | The concrete action |
| all, always, never | Often untrue | Check and state exceptions |
| minimize, maximize, optimize | No target | A target value |
| flexible, scalable, robust | Not measurable | Concrete capacity or change scenario |
| should (when you mean mandatory) | Weakens the obligation | shall / must |
| it, they, this (unclear reference) | Which object? | Name the object |

AI assistants are useful for a first pass: paste your own requirements (non-confidential or fictional) and ask which ones contain ambiguous terms. Treat the output as suggestions; you still decide.

## Key terms
- **Requirement** — a statement of a need or capability that a solution must meet.
- **Specification** — a document that collects requirements in an agreed structure for building and verifying a solution.
- **Functional requirement** — what the system must do: behavior, inputs, processing, outputs.
- **Non-functional requirement (NFR)** — a measurable quality or constraint such as performance, security or availability.
- **Business rule** — an organizational policy that constrains the business, independent of any system.
- **Atomic requirement** — a requirement that expresses exactly one need.
- **Verifiable** — a requirement whose fulfillment can be proven by inspection, analysis, demonstration or test.
- **BRD** — Business Requirements Document, describing goals, scope and business-level requirements.
- **Functional specification (FRS)** — a detailed description of what the solution does, for developers and vendors.
- **SRS** — Software Requirements Specification, a complete set of software requirements, functional and non-functional.
- **Technical specification** — a description of how the solution will be built, usually written by the vendor or architect.
- **Use case** — a step-by-step description of how an actor uses the system to reach a goal, with main, alternative and exception flows.
- **Data dictionary** — a table defining each data field with format, validation and source.
- **MoSCoW** — prioritization into Must have, Should have, Could have and Won't have this time.
- **Traceability matrix (RTM)** — a table linking requirements to sources, design and test cases.
- **Sign-off** — formal approval of a document version, which creates a baseline.
- **Baseline** — an approved version of requirements against which changes are controlled.
- **Change request (CR)** — a formal request to change approved scope, assessed for impact before a decision.
- **RTO / RPO** — maximum acceptable time to restore a service, and maximum acceptable data loss measured in time.

## Hands-on
:::exercise id="m06-e1" title="Rewrite 10 bad requirements" min="40" tool="text editor"
Goal: practice turning vague statements into testable requirements.

Rewrite each statement. Split it where needed, add numbers, and note any question you would have to ask a stakeholder.

1. The system should be fast.
2. The underwriter can see and edit and approve requests.
3. The portal must be user-friendly for exporters.
4. The system shall handle errors from the registry appropriately.
5. Reports shall be available in real time.
6. The system shall support various currencies, e.g. EUR, USD etc.
7. Requests will be sent to the committee if necessary.
8. The system must be secure.
9. Data shall be kept as long as needed.
10. It should be possible to export it to Excel.

Steps: (1) mark the ambiguous words, (2) write the rewritten requirement(s) using the template with IDs, (3) classify each as functional, non-functional or business rule, (4) list your open questions.

Done when: every rewritten requirement passes the test "could a tester prove this?", and where you lacked information you wrote a question instead of inventing a number silently.
:::

:::exercise id="m06-e2" title="Mini functional specification: automated ARES check" min="120" tool="text editor"
Goal: write a vendor-facing functional specification of 3–5 pages for the ExportShield change "automated ARES check in the credit limit request".

1. Use the 17-section template from the Deep dive. Sections you cannot fill, mark "N/A" with a reason.
2. Write context, scope and an explicit out-of-scope list (for example foreign registries, automatic credit decision).
3. Include the TO-BE diagram from exercise m04-e2 or a description of it.
4. Write at least 12 functional requirements with IDs, MoSCoW priority and source, including error handling.
5. Write UC-03 in your own words or a second use case, for example "Underwriter reviews registry data".
6. Add a data dictionary with at least 6 fields and at least 4 measurable NFRs.
7. Describe the ARES integration: trigger, input, output fields, error cases. Look at a real response in a browser using the public [ARES API](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}) with the registration number of any public company you know.
8. End with at least 5 open questions.

Done when: a colleague who has never heard of the project can tell you what will be built, what will not, and how it will be accepted.
:::

:::exercise id="m06-e3" title="Build a traceability matrix" min="40" tool="Excel / Google Sheets"
Goal: link requirements to their sources and tests.

1. Create a sheet with columns: Req ID, Requirement (short), Type, Source, Business requirement, Priority, Spec section, Test case IDs, Status.
2. Enter the requirements from exercise m06-e2 and two business requirements (for example BR-G1 "reduce manual data entry", BR-G2 "decide within 3 working days").
3. Invent test case IDs (TC-001…) and write a one-line description of each on a second sheet.
4. Add conditional formatting that highlights requirements with no test case.
5. Add a filter and answer: which Must requirements are not yet covered by a test?
6. Simulate a change request: BR-01 threshold changes from 1 M to 1.5 M EUR. List all affected rows.

Done when: every requirement has a source and a business requirement, uncovered requirements are visible at a glance, and you can show the impact of the change request.
:::

## Self-check
:::q
What is wrong with "The system shall validate and save the request and notify the underwriter"?
---
It is not atomic: it contains three requirements. If one part is implemented and another is not, the requirement is neither fully passed nor failed, and it cannot be traced or prioritized separately. It should be split into three requirements, each with its own ID.
:::

:::q
Why keep business rules separate from functional requirements?
---
Business rules belong to the organization and change when management or regulation changes, independently of the software. If functional requirements reference a rule by ID, a change of the rule (for example a new approval threshold) is made in one place, and the impact on the system is easy to find.
:::

:::q
Turn "The portal shall be available" into a measurable non-functional requirement.
---
For example: "The exporter portal shall be available 99.5 % of the time Mon–Fri 7:00–19:00 CET, measured monthly, excluding maintenance announced at least 3 working days in advance." It states the target, the time window, the measurement period and the exclusions.
:::

:::q
What is the purpose of the "Out of scope" section in a vendor specification?
---
It states explicitly what will not be delivered, so neither side can later claim it was expected. Most disputes between client and vendor come from items that were assumed but never written down. A clear out-of-scope list also prevents scope creep and frames future change requests.
:::

:::q
What do exception flows in a use case give you that a happy-path description does not?
---
They force the question "what happens when something goes wrong", such as invalid input, missing data or an unavailable system. The answers become additional functional requirements, error messages and test cases that stakeholders rarely mention on their own.
:::

:::q
Almost every requirement in a draft is marked "Must have". What do you do?
---
Challenge each one with "what happens if we go live without it?" and link it to the business goal. Requirements with an acceptable workaround become Should or Could. A list where everything is Must gives no guidance for trade-offs when time or budget runs short.
:::

:::q
How does a traceability matrix help with a change request?
---
It shows which requirements, spec sections and test cases are linked to the changed item, so the impact can be assessed quickly and completely. Without it, affected tests or dependent requirements are easily missed, and the change introduces defects.
:::

:::q
What is the difference between a functional specification and a technical specification?
---
The functional specification describes what the solution must do from the business and user perspective: functions, rules, data, screens, quality requirements. The technical specification describes how it will be built: architecture, components, interfaces, database. The BA usually writes the first; the vendor or architect writes the second.
:::

## Interview corner
:::interview
Here is a requirement: "The system should respond quickly and be user-friendly." How would you improve it?
---
- Point out it combines two topics and uses untestable words ("quickly", "user-friendly", "should").
- Split into a performance NFR and a usability requirement.
- Add numbers: response within X seconds for Y % of requests under Z load.
- Make usability concrete: task completion time, error messages next to fields, test with users.
- Mention you would confirm the numbers with stakeholders and IT rather than invent them.

Typical mistake: replacing one vague word with another ("efficient", "intuitive").
:::

:::interview
What would you put into a functional specification for an external vendor?
---
- Document control, context and goal, scope and explicit out of scope.
- Actors, TO-BE process, numbered functional requirements with priority.
- Business rules, UI/wireframes, data dictionary, integrations with error handling.
- Measurable NFRs, acceptance criteria and UAT approach, open questions, glossary.
- Mention review with the vendor and sign-off before development.

Typical mistake: describing only a list of features without scope, NFRs or acceptance criteria.
:::

:::interview
What makes a good requirement?
---
- Unambiguous, verifiable, atomic, consistent, feasible, necessary, traceable (ISO/IEC/IEEE 29148, IREB).
- States what, not how, unless it is a real constraint.
- Has an ID, source and priority.
- Give one bad and one improved example.

Typical mistake: listing adjectives without showing how you check them in practice.
:::

:::interview
How do you handle changes to requirements after sign-off?
---
- Use change control: a change request with description, reason, requester.
- Impact analysis using the traceability matrix: affected requirements, tests, cost, schedule (with the vendor).
- Decision by the responsible person or change board; update the baseline, version and change log.
- In agile, the change goes into the backlog, but contractual scope may still need a formal CR.

Typical mistake: quietly updating the document and telling the vendor in a hallway conversation.
:::

:::interview
What is a traceability matrix and why would you maintain one?
---
- A table linking each requirement to its source, business goal, design and test cases.
- Shows untested requirements and requirements nobody asked for.
- Supports impact analysis of changes and UAT coverage reporting.
- Can be a spreadsheet or links in tools such as Jira and a test management tool.

Typical mistake: saying it is "for audit only" and not connecting it to testing and change impact.
:::
