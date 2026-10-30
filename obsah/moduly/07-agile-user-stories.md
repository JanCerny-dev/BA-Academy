---
id: 07
slug: agile-user-stories
title: "Agile requirements: user stories, acceptance criteria and Jira"
phase: B
priority: P1
quick_min: 5
deep_min: 40
job_ad: "general"
---

## Why this matters
Most IT teams, including vendors, plan their work in a backlog of user stories, usually in Jira. As a BA you write those stories, define acceptance criteria that testers and developers rely on, and keep the backlog in shape together with the product owner. Interviewers frequently ask you to write a user story with acceptance criteria on the spot, or to explain INVEST and Given/When/Then.

## Quick version
In agile development (an approach where software is delivered in small increments, typically every 1–4 weeks, with frequent feedback), requirements are kept in a **product backlog**: an ordered list of everything that might be built.

**Hierarchy of backlog items** (names vary by tool):
- **Epic** – a large body of work, too big for one sprint. "Online claim notification for exporters."
- **Feature** – a capability within an epic (used in some setups, for example SAFe).
- **User story** – a small piece of value for a user, deliverable within one sprint.
- **Task / sub-task** – technical work needed to deliver a story ("Create API endpoint", "Write test cases").

**User story format:**
> As a **[role]**, I want **[capability]**, so that **[benefit]**.

Example: *As an exporter, I want to upload the unpaid invoice and the reminder letters with my claim notification, so that ExportShield can start checking my claim without asking for documents by e-mail.*

A story is a placeholder for a conversation, not a full specification. The three Cs: **Card** (the short text), **Conversation** (discussion that clarifies details), **Confirmation** (acceptance criteria).

**INVEST** – checklist for good stories: Independent, Negotiable, Valuable, Estimable, Small, Testable.

**Splitting stories.** Big stories are split vertically (each piece still delivers something usable): by workflow steps, by business rules, by data variations, happy path first and unhappy paths later, or by operations (create, read, update, delete).

**Acceptance criteria (AC)** are conditions a story must meet to be accepted. Two styles:
- **Rule-based** – a checklist: "Only PDF, JPG and PNG files are accepted. Maximum 10 MB per file."
- **Scenario-based** – Gherkin **Given / When / Then**:

```gherkin
Scenario: Exporter uploads a file that is too large
  Given the exporter is on the claim notification form
  When the exporter uploads a PDF file of 12 MB
  Then the system rejects the file
  And shows the message "The file is larger than 10 MB."
```

**Definition of Ready (DoR)** – what a story needs before the team takes it into a sprint (clear AC, dependencies known, estimated). **Definition of Done (DoD)** – what must be true for any item to count as finished (code reviewed, tested, documented, deployed to test).

**Backlog refinement** – a regular session where the product owner, BA and team clarify, split and estimate upcoming stories. **Story points** are relative estimates of effort and complexity, made by the developers; the BA explains the story, but does not estimate it alone.

**Product owner vs BA.** The **product owner** (a Scrum role) is accountable for maximizing the value of the product and for ordering the backlog. The BA supports with analysis: elicitation, writing stories and AC, modeling, clarifying details. In small teams one person may do both.

**Jira basics.** Issue types (epic, story, task, bug, sub-task), a workflow (To Do → In Progress → In Review → Done), a backlog, sprints and a board. Filters use **JQL** (Jira Query Language): `project = CLM AND status = "In Progress"`. Confluence is the companion wiki for specifications, meeting notes and decisions.

**Hybrid and vendor projects.** A functional specification often defines the contractual scope, and stories in Jira break it into deliverable pieces. Each story links back to the specification section or requirement ID, which keeps traceability.

**Interview one-liner:** "I write stories in role-capability-benefit form, check them against INVEST, split them vertically, and define acceptance criteria as rules or Given/When/Then scenarios that testers can use directly."

## Deep dive

### Agile in one page [P1]
Agile is a family of approaches based on the Agile Manifesto (2001): deliver working software in short cycles, collaborate closely with customers, and respond to change. **Scrum** is the most common framework. The official [Scrum Guide](https://scrumguides.org/scrum-guide.html) (2020 version) defines:
- three accountabilities: **Product Owner**, **Scrum Master**, **Developers**,
- events: the **Sprint** (a fixed timebox of one month or less, often two weeks), Sprint Planning, Daily Scrum, Sprint Review, Sprint Retrospective,
- artifacts: **Product Backlog**, **Sprint Backlog**, **Increment**, with commitments Product Goal, Sprint Goal and Definition of Done.

The Scrum Guide does not mention a "business analyst", "user stories" or "story points". These are common practices that teams add. **Kanban** is an alternative without sprints: work flows continuously through columns, with limits on work in progress. Module 02 covers delivery approaches in more detail.

### Epics, features, stories, tasks [P1]
| Level | Size | Who reads it | ExportShield example |
|---|---|---|---|
| Epic | Weeks to months | Management, PO, team | Online claim notification for exporters |
| Feature | Several sprints | PO, team | Document upload in claim notification |
| User story | Fits in one sprint, ideally a few days | Team, testers | Upload invoice as PDF to a claim notification |
| Task / sub-task | Hours | Developers | Add file size validation on the server |

Jira's default hierarchy is Epic → Story/Task/Bug → Sub-task. Larger organizations add levels above epics (initiatives, themes). Use whatever your team uses; the key point is that stories are small and deliver value, while tasks are technical steps that alone deliver nothing to a user.

A **bug** (defect) is also a backlog item: something does not work as specified.

### Writing user stories [P1]
Format: *As a [role], I want [capability], so that [benefit].*

- **Role**: a specific user type, not "user". Exporter, claims handler, underwriter, head of claims. If the role is "the system", it is probably a technical task or should be written from the perspective of the person who benefits.
- **Capability**: what they can do, in their language, without UI details ("submit", "see", "be notified").
- **Benefit**: why it matters. This part is often skipped and is the most useful, because it lets the team find a cheaper way to the same benefit.

**Examples for the ExportShield claim notification portal:**
1. As an exporter, I want to notify a non-payment online by selecting the insured buyer and the unpaid invoice, so that I do not have to fill in a paper form.
2. As an exporter, I want to see the status of my claim notifications, so that I do not have to call ExportShield to ask.
3. As a claims handler, I want new notifications to appear in my ClaimDesk queue automatically, so that I do not have to retype them from e-mails.
4. As a claims handler, I want to see which mandatory documents are missing, so that I can request them in one message.

**Weak stories and why:**
- "As a user, I want a better claims portal." – role too generic, not testable, not small.
- "As a developer, I want to create a REST endpoint." – no user value; this is a task.
- "As an exporter, I want a green button at the top right." – describes UI design, not a need.

The **3 Cs** (Card, Conversation, Confirmation, described by Ron Jeffries) remind you that the card is deliberately short. Details come from the conversation and are captured in acceptance criteria, attached wireframes, or links to the specification.

### INVEST [P1]
INVEST (coined by Bill Wake) is a checklist:

| Letter | Meaning | Question to ask | Problem example |
|---|---|---|---|
| I – Independent | Can be built and delivered without waiting for another story | Can we change the order? | "Story B only works after story A" for every story |
| N – Negotiable | Details can still be discussed | Is it written as a need, or as a fixed design? | Full screen design dictated in the story |
| V – Valuable | Delivers value to a user or the business | Who benefits? | "Create database table" |
| E – Estimable | Team understands it well enough to estimate | Can developers size it? | Unknown integration with no documentation |
| S – Small | Fits in a sprint, ideally a few days | Can it be done in under half a sprint? | "Build the claims portal" |
| T – Testable | Has clear criteria for done | How would a tester check it? | "The portal should be pleasant to use" |

Complete independence is rarely possible. Aim to reduce dependencies, not to eliminate them.

### Splitting stories [P1]
Large stories are split **vertically**: each slice goes through all layers (screen, logic, data) and delivers something testable. Splitting **horizontally** ("build the database", "build the UI") produces pieces with no value on their own.

Common patterns, applied to the epic "Online claim notification":

| Pattern | How it splits | Example slices |
|---|---|---|
| Workflow steps | One story per step of the process | Select buyer and invoice → upload documents → submit → see confirmation |
| Business rules | Simple rule first, complex rules later | Accept any notification → reject invoices older than the policy reporting deadline → warn if the invoice is not insured |
| Data variations | One data type or case at a time | Notification in EUR → other currencies; one invoice → several invoices |
| Happy / unhappy path | Main success first, errors separately | Successful upload → file too large → wrong file type → virus detected |
| Operations (CRUD) | Create, read, update, delete separately | Create draft notification → view draft → edit draft → delete draft |
| Interface / channel | One channel first | Portal first, API for large exporters later |
| Defer performance | Make it work, then make it fast | Basic list of claims → paging and filtering for exporters with hundreds of claims |

A good split lets the product owner drop the less valuable slices. If every slice is equally essential, the split did not help prioritization.

### Acceptance criteria [P1]
Acceptance criteria are the conditions a story must satisfy to be accepted by the product owner. They define the scope of the story, guide development and become the basis for test cases.

**Rule-based (checklist):**
Story: *As an exporter, I want to upload documents to my claim notification, so that ExportShield can check my claim without e-mail exchange.*
- Accepted file types: PDF, JPG, PNG.
- Maximum file size: 10 MB per file, maximum 20 files per notification.
- Each file must be assigned a document type: invoice, reminder, delivery proof, other.
- Uploaded files are stored in DocVault and linked to the claim number.
- The exporter can remove a file until the notification is submitted.

**Scenario-based (Gherkin):** described in the next section.

Good AC are testable, describe behavior and not implementation, include the important negative cases, and fit the story size (3–8 criteria is typical; 20 suggests the story should be split). AC are not the Definition of Done: AC are specific to one story, DoD applies to all stories.

### Gherkin: Given / When / Then [P1]
**Gherkin** is a structured language for describing behavior as scenarios. It is used in BDD (Behavior-Driven Development), where scenarios are written before development, and tools such as Cucumber can run them as automated tests. Even without automation, Gherkin is a clear format for AC.

Structure:
- **Feature** – the capability being described.
- **Background** – Given steps that run before every scenario of the feature.
- **Scenario** – one concrete example.
- **Given** – the starting state (context).
- **When** – the action or event.
- **Then** – the expected outcome.
- **And / But** – continue the previous step type.

```gherkin
Feature: Claim notification document upload

  Background:
    Given the exporter "Demo Exporter Ltd" is logged in to the portal
    And has a draft claim notification for buyer "Demo Buyer GmbH"

  Scenario: Upload a valid invoice
    When the exporter uploads the file "invoice_2026_118.pdf" of 2 MB
    And selects the document type "Invoice"
    Then the file appears in the list of uploaded documents
    And the document type is shown as "Invoice"

  Scenario: Reject an unsupported file type
    When the exporter uploads the file "invoice.docx"
    Then the file is not uploaded
    And the message "Only PDF, JPG and PNG files are accepted." is shown

  Scenario: Submit is blocked while mandatory documents are missing
    Given no document of type "Invoice" has been uploaded
    When the exporter selects "Submit notification"
    Then the notification is not submitted
    And the message "Please upload the unpaid invoice." is shown
```

**Scenario Outline** runs the same scenario with several data rows from an **Examples** table. It is ideal for business rules with thresholds:

```gherkin
Scenario Outline: Route claim for approval by amount
  Given a calculated indemnity of <amount> EUR
  When the claims handler completes the assessment
  Then the claim is routed to "<approver>"

  Examples:
    | amount  | approver            |
    | 49999   | Claims handler      |
    | 50000   | Head of claims      |
    | 499999  | Head of claims      |
    | 500000  | Management board    |
```

The thresholds above are fictional. Notice how the examples deliberately test values on both sides of each boundary; this is the same idea as boundary value analysis in testing (module 13).

Writing tips:
- One behavior per scenario. If you need many "When" steps, it is probably several scenarios.
- Describe business behavior, not clicks: "When the exporter submits the notification", not "When the user clicks the button with id btnSubmit".
- Use concrete example data; it uncovers questions ("Is 50,000 exactly still the handler's limit?").
- Keep the language of the domain (glossary terms) consistent across scenarios.

### Definition of Ready and Definition of Done [P1]
**Definition of Ready (DoR)** is a team agreement on what a story needs before it enters a sprint. It is not in the Scrum Guide, but many teams use it. Example:
- Story written in role-capability-benefit form, linked to an epic.
- Acceptance criteria agreed with the product owner.
- Dependencies (other teams, vendor, data) identified and resolved or planned.
- Wireframe or spec reference attached where there is UI.
- Estimated by the team; small enough for the sprint.

**Definition of Done (DoD)** is defined in the Scrum Guide as a formal description of the state of the Increment when it meets the quality measures required for the product. Example:
- Code reviewed and merged.
- All acceptance criteria tested and passed in the test environment.
- No open critical or major defects.
- User documentation or release notes updated.
- Product owner has accepted the story.

The BA usually owns most of the DoR checklist in practice: if a story is not ready, it is often because analysis is missing.

### Backlog refinement and estimation [P1]
**Backlog refinement** (formerly "grooming") is an ongoing activity: adding detail, splitting, ordering and estimating backlog items. Many teams hold a weekly 1–2 hour session. A good rhythm for a BA is to have stories for the next two sprints ready and the ones after that roughly understood.

Your role in refinement:
- Present stories with their context and AC; answer questions.
- Note open questions and take them back to stakeholders.
- Split stories that are too big.
- Make sure dependencies and non-functional aspects are visible.

**Story points** are a relative unit of effort, complexity and uncertainty. A team picks a reference story ("upload one invoice = 3 points") and compares others to it. Many teams use a modified Fibonacci scale (1, 2, 3, 5, 8, 13, 20…). The growing gaps reflect growing uncertainty. **Planning poker** is a common technique: each developer shows a card at the same time, and large differences are discussed.

Important for a BA: **developers estimate**, because they do the work. The BA clarifies scope. If you are asked "how many points is this?", the right answer is "let's ask the team". **Velocity** (points completed per sprint) helps the team plan, but it is not a performance metric and cannot be compared between teams.

### User story mapping [P2]
A **user story map** (popularized by Jeff Patton) arranges stories in two dimensions:
- Horizontally: the user's journey, as activities in order (the "backbone").
- Vertically: stories under each activity, ordered by priority.

A horizontal line across the map marks the first release (often the MVP, minimum viable product: the smallest version that delivers value and allows learning). Everything above the line is in the release.

Example backbone for the claims portal: *Log in → Start notification → Select buyer and invoice → Upload documents → Submit → Track status → Respond to questions*. Under "Upload documents": upload PDF (release 1), assign document type (release 1), drag and drop (release 2), upload from mobile camera (later).

Story mapping is done in a workshop with stakeholders and the team, on a wall or a [Miro](https://miro.com/) board. It prevents a common backlog problem: a flat list of 200 stories where nobody sees the whole journey or what the first usable release is.

### Product owner and business analyst [P1]
| Aspect | Product owner | Business analyst |
|---|---|---|
| Accountability | Maximizing product value, ordering the backlog, accepting work | Analysis quality: understanding needs, defining requirements |
| Defined in | Scrum Guide | BABOK, not part of Scrum |
| Typical tasks | Product goal, priorities, stakeholder decisions, accepting stories | Elicitation, modeling, writing stories and AC, clarifying details, supporting testing |
| Decides | What is built and in which order | Proposes, documents, recommends |

The PO is one person who decides; the BA often works for or with the PO. In a client-vendor setup, the client may have the PO and the BA, while the vendor has the developers. In small companies, one person may hold both roles. In an interview, show that you know the difference and that you are comfortable either way.

### Jira basics [P1]
Jira (by Atlassian) is the most common tool for managing backlogs. [Jira Free](https://www.atlassian.com/software/free) is available for up to 10 users, so you can practice.

**Core concepts:**
- **Project** – container for issues, with a key such as `CLM`. Issues get IDs like `CLM-42`.
- **Issue types** – Epic, Story, Task, Bug, Sub-task (configurable).
- **Fields** – summary, description, assignee, priority, labels, components, fix version, story points, custom fields.
- **Workflow** – the statuses an issue moves through and the allowed transitions, for example *To Do → In Progress → In Review → Testing → Done*.
- **Board** – columns mapped to statuses. **Scrum board** with sprints, or **Kanban board** with continuous flow.
- **Backlog** – the ordered list of issues not yet in a sprint.
- **Sprint** – a timeboxed set of issues taken from the backlog.
- **Links** – for example "blocks", "relates to", "duplicates"; used for dependencies and traceability. Test management apps for Jira (such as Xray or Zephyr) add links like "is tested by".

**JQL (Jira Query Language)** lets you filter issues. It looks similar to SQL's WHERE clause (module 10):

```sql
project = CLM AND status = "In Progress"
project = CLM AND issuetype = Story AND "Epic Link" = CLM-1
project = CLM AND status != Done AND assignee = currentUser()
project = CLM AND labels = portal AND created >= -14d ORDER BY priority DESC
project = CLM AND issuetype = Bug AND priority in (Highest, High) AND resolution = Unresolved
```

Field names can differ between Jira versions and configurations (for example newer cloud projects use `parent` instead of `"Epic Link"`). Jira's search box suggests fields as you type. Saved filters can be shared and shown on dashboards, which is how BAs and project managers report status.

**Confluence** is Atlassian's wiki. It is where teams keep specifications, meeting notes, decision logs, glossaries and process diagrams. Typical practice: a Confluence page per epic or feature with context, process, rules and wireframes, and Jira stories linked to it. Confluence also offers templates for product requirements, meeting notes and retrospectives.

### Stories and specifications in hybrid and vendor projects [P1]
Many real projects are not pure Scrum. For example, ExportShield contracts NovaSoft to extend PolicyHub. The contract needs a defined scope and price, so there is a signed functional specification (module 06). Delivery still happens in sprints with a Jira backlog.

How the two fit together:
1. The specification defines scope, requirements with IDs, business rules, NFRs and integrations.
2. Epics in Jira correspond to major spec sections or features.
3. Stories break each section into deliverable pieces. Each story references the requirement IDs it implements ("Implements FR-003, FR-004").
4. AC in stories are consistent with the spec; if detail is added during refinement, it is reflected in the spec or recorded as a decision.
5. Changes of scope go through a change request (contract), then into the backlog.
6. Testers trace test cases to stories and requirements; UAT reports coverage against the spec.

Risks: the spec and the backlog drift apart, or the vendor treats the backlog as the contract while the client treats the spec as the contract. Agree at the start which document wins in case of conflict.

## Key terms
- **Agile** — an approach to delivery in short iterations with frequent feedback and adaptation.
- **Scrum** — an agile framework with sprints, three accountabilities and defined events, described in the Scrum Guide.
- **Product backlog** — the ordered list of everything that might be built for a product.
- **Epic** — a large body of work that is split into smaller stories.
- **User story** — a short description of a capability from a user's perspective, in the form "As a…, I want…, so that…".
- **INVEST** — checklist for good stories: Independent, Negotiable, Valuable, Estimable, Small, Testable.
- **Vertical slice** — a story split that goes through all layers and delivers usable value on its own.
- **Acceptance criteria (AC)** — conditions a specific story must satisfy to be accepted.
- **Gherkin** — a structured language for scenarios using Given, When and Then.
- **Scenario Outline** — a Gherkin scenario template run with multiple rows of example data.
- **Definition of Ready (DoR)** — team agreement on what a story needs before it can enter a sprint.
- **Definition of Done (DoD)** — the quality criteria every increment must meet to be considered done.
- **Backlog refinement** — ongoing work of clarifying, splitting, ordering and estimating backlog items.
- **Story points** — a relative estimate of effort, complexity and uncertainty, made by the developers.
- **Velocity** — the amount of work, usually in story points, a team completes per sprint.
- **User story map** — a two-dimensional arrangement of stories by user journey and priority, used to plan releases.
- **MVP** — minimum viable product, the smallest version that delivers value and allows learning.
- **Product owner** — the Scrum accountability for maximizing product value and ordering the backlog.
- **JQL** — Jira Query Language for filtering issues.
- **Confluence** — Atlassian's wiki for specifications, meeting notes and team documentation.

## Hands-on
:::exercise id="m07-e1" title="Write 6 stories with acceptance criteria for the claims portal" min="60" tool="text editor"
Goal: write a small, coherent set of user stories for the ExportShield claim notification portal.

1. List the roles involved: exporter, claims handler, head of claims.
2. Write 6 user stories in the form "As a…, I want…, so that…". At least two must be for the claims handler.
3. Check each against INVEST and rewrite the ones that fail.
4. For each story, write 3–6 acceptance criteria. Use the rule-based style for at least three stories and Given/When/Then for at least two.
5. Include at least one negative case per story (invalid input, missing data, no permission).
6. Note open questions you would take to the product owner.

Done when: every story names a specific role and a benefit, every story can be tested from its AC alone, and none of the stories is a technical task.
:::

:::exercise id="m07-e2" title="Split an oversized epic" min="40" tool="Miro / paper"
Goal: practice vertical splitting and release planning.

Epic: *"As a head of claims, I want a claims dashboard, so that I can manage the workload of my team."*

1. Write down the user journey of the head of claims as 4–6 activities (the backbone of a story map).
2. Under each activity, write stories using at least three different splitting patterns (workflow steps, business rules, data variations, happy/unhappy path, CRUD, defer performance).
3. Produce at least 10 stories. Order them vertically by priority.
4. Draw a release line for an MVP that you could deliver in two sprints.
5. For each story above the line, write one sentence explaining why it is in the MVP.

Done when: every story above the line delivers something the head of claims can use, and nothing above the line is a purely technical task.
:::

:::exercise id="m07-e3" title="Set up a Jira (or Trello) project" min="60" tool="Jira Free / Trello"
Goal: get hands-on with the tool you will use daily.

1. Create a free account at [Jira Free](https://www.atlassian.com/software/free) (or use [Trello](https://trello.com/) if you prefer a simpler tool). Use only fictional data.
2. Create a Scrum project named "Claims Portal" with key `CLM`.
3. Create one epic "Online claim notification" and enter your 6 stories from exercise m07-e1, with AC in the description, linked to the epic.
4. Add sub-tasks to one story (for example "Design upload form", "Implement validation", "Write test cases").
5. Estimate the stories with story points (pretend to be the team) and order the backlog.
6. Create a sprint, move 3 stories into it, start it and move one story across the board.
7. Look at the workflow and add a status "Testing" between "In Progress" and "Done" if your project type allows it.
8. Write and save a JQL filter: `project = CLM AND status = "In Progress"`. Then write one more filter of your own.

Done when: you have a backlog, a running sprint, a board with at least one moved story, and two saved filters. In Trello: lists for backlog, sprint, in progress, testing, done, with labels for epics.
:::

:::exercise id="m07-e4" title="Write three Gherkin scenarios" min="30" tool="text editor"
Goal: write precise scenario-based acceptance criteria.

Story: *As an exporter, I want to notify a non-payment online, so that the claim process starts without paper forms.* Business rule (fictional): a non-payment must be notified no later than 60 days after the original due date of the invoice.

1. Write a Feature header and a Background with the logged-in exporter.
2. Scenario 1: successful notification within the deadline.
3. Scenario 2: notification rejected after the deadline, with the exact message.
4. Scenario 3: a Scenario Outline with an Examples table testing the deadline at day 59, 60 and 61, and the expected outcome for each.
5. Check: business language, no UI element IDs, one behavior per scenario.

Done when: a tester could run all three scenarios without asking you anything, and the outline covers both sides of the deadline boundary.
:::

## Self-check
:::q
What is wrong with the story "As a developer, I want to create a database table for claims"?
---
It delivers no value to a user on its own and describes implementation rather than a need. It is a technical task that belongs under a user story such as "As an exporter, I want to save a draft claim notification, so that I can finish it later."
:::

:::q
Why should stories be split vertically rather than horizontally?
---
A vertical slice goes through all layers and delivers something a user can test and use. Horizontal splits, such as "build the database" and "build the UI", produce pieces with no value on their own, cannot be accepted by the product owner separately and hide integration problems until the end.
:::

:::q
What is the difference between acceptance criteria and the Definition of Done?
---
Acceptance criteria are specific to one story and describe the behavior it must show. The Definition of Done applies to every item and describes general quality conditions, such as code reviewed, tested in the test environment and documentation updated. A story is finished only when both are met.
:::

:::q
When would you use a Scenario Outline instead of several scenarios?
---
When the same behavior must be checked with different data values, for example amount thresholds or deadline boundaries. The outline keeps one set of steps and puts the variations into an Examples table, which is shorter and makes the tested values easy to review.
:::

:::q
Who estimates story points, and what is the BA's role in estimation?
---
The developers estimate, because they will do the work. The BA explains the story, answers questions, clarifies scope and helps split stories that are too large or unclear to estimate.
:::

:::q
What problem does a user story map solve compared to a flat backlog?
---
A flat list hides the user journey and makes it hard to see which stories together form a usable release. A story map shows the journey horizontally and priorities vertically, so the team can draw a release line and deliver a complete, if minimal, end-to-end flow first.
:::

:::q
In a vendor project, how do you keep user stories and the signed functional specification consistent?
---
Link each story to the requirement IDs it implements, keep AC consistent with the spec, record decisions made in refinement and update the spec or decision log, and send scope changes through change requests. Agree at the start which document takes precedence if they conflict.
:::

## Interview corner
:::interview
Write a user story with acceptance criteria for uploading documents to a claim.
---
- Specific role, capability and benefit: "As an exporter, I want to upload…, so that…".
- 3–6 AC: allowed file types, size limit, document type, where the file is stored, behavior on error.
- At least one Given/When/Then scenario for a negative case.
- Mention open questions you would clarify (virus scanning, maximum number of files).

Typical mistake: writing only the story sentence with no acceptance criteria, or writing AC that describe UI layout instead of behavior.
:::

:::interview
What does INVEST mean, and which letter is most often violated in practice?
---
- Independent, Negotiable, Valuable, Estimable, Small, Testable, each with a short explanation.
- Most often violated: Small (stories too big) and Valuable (technical tasks written as stories); Independent is hard to achieve fully.
- Show how you would fix it: splitting patterns, rewriting from the user's perspective.

Typical mistake: reciting the acronym without any example of applying it.
:::

:::interview
What is the difference between a product owner and a business analyst?
---
- PO: Scrum accountability, maximizes product value, orders the backlog, decides and accepts.
- BA: analysis discipline (BABOK), elicitation, modeling, stories and AC, supports PO and team.
- In practice roles overlap or are combined; in vendor projects they may sit on the client side.
- You support the PO's decisions with analysis.

Typical mistake: saying the roles are the same, or that the BA decides priorities.
:::

:::interview
How would you split a story that is too large for one sprint?
---
- Split vertically, each slice delivers value.
- Name patterns: workflow steps, business rules, data variations, happy/unhappy path, CRUD, defer performance.
- Give a concrete example from a domain you know.
- Check that the PO can prioritize slices independently.

Typical mistake: splitting by technical layers (front end, back end, database).
:::

:::interview
How do you use Jira and Confluence as a BA?
---
- Jira: epics and stories with AC, links to requirements and dependencies, backlog ordering with the PO, sprints, board.
- JQL filters and dashboards for status reporting, for example open bugs by priority.
- Confluence: specifications, process diagrams, decision log, meeting notes, glossary, linked to Jira issues.
- Keep one source of truth and link instead of copying.

Typical mistake: only saying "I have used Jira" without describing what you did in it.
:::
