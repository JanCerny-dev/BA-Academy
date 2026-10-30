---
id: 05
slug: elicitation
title: Requirements elicitation
phase: B
priority: P1
quick_min: 5
deep_min: 40
job_ad: "požadavky od oddělení"
---

## Why this matters
The job ad starts with "requirements from departments". Nobody hands you finished requirements: people describe problems, wishes and half-solutions, and much of what they know they never say out loud. Elicitation is the skill of getting the real need out of stakeholders, checking it and writing it down. If you get it wrong, the vendor builds exactly what was specified and still nobody is happy.

## Quick version
**Elicitation** means drawing out information from stakeholders and other sources. The word is chosen on purpose: requirements are not lying around to be "gathered", you have to work to get them. A **stakeholder** is anyone who affects or is affected by the change: users, managers, IT, compliance, the vendor, even clients.

**Requirement types** (as classified in BABOK v3, the IIBA's guide to business analysis):
- **Business requirements** – why the organization does this. "Reduce credit limit decision time from 10 to 3 working days."
- **Stakeholder requirements** – what a group of people needs. "Underwriters need buyer registry data available without manual search."
- **Solution requirements** – what the solution must do (**functional**: "The system shall retrieve buyer data from ARES by registration number") and how well (**non-functional**: "The lookup shall return within 5 seconds").
- **Transition requirements** – what is needed only to move from today to the new state: data migration, training, parallel run.

**Main techniques:**
- **Interviews** – one-to-one conversation, the most common technique. Prepare questions, start open, then go specific.
- **Workshops** – a facilitated session with several stakeholders to agree on requirements fast. JAD (Joint Application Design) is the classic form with business and IT in one room.
- **Observation / job shadowing** – watch people do the work. Reveals steps they forget to mention.
- **Document analysis** – procedures, forms, reports, e-mails, existing system screens.
- **Surveys** – many people, short structured questions. Good for confirming, weak for discovering.
- **Prototyping / wireframes** – a sketch of a screen. People react to a picture much better than to text.
- **Focus groups** – a moderated discussion with representative users about opinions and experiences.
- **Interface analysis** – what data goes in and out of systems and to whom.
- **Brainstorming** – generate many ideas quickly, judge later.

**Choosing a technique:** use several. Interviews for depth, observation for tacit knowledge, documents for the formal rules, workshops to resolve conflicts, prototypes to confirm.

**Typical problems and what to do:**
- **Tacit knowledge** (what people know but do not say because it is obvious to them) – observe, ask "walk me through the last case you handled", ask about exceptions.
- **Conflicting views** – make the conflict visible, go back to the business goal, escalate to the decision maker if needed.
- **Solution-first stakeholders** ("we need a button that exports to Excel") – ask *why* until you reach the real need. Maybe the need is "the manager wants a weekly overview", and a report solves it better.

**Confirm what you heard.** Send meeting notes within a day, play back the process or the requirements ("So the rule is…, correct?"), and get explicit confirmation. Unconfirmed requirements are assumptions.

**Agile.** Elicitation does not happen once at the start. It continues through backlog refinement, demos and feedback every sprint.

**AI.** An AI assistant can help draft interview questions or summarize a transcript. Use only non-confidential or fictional data in public AI tools, and check the output: AI summaries drop exceptions and sometimes add things nobody said.

**Interview one-liner:** "I combine interviews, observation and document analysis, confirm results with written notes and playback, and always ask why behind a requested solution."

## Deep dive

### Requirement types in practice [P1]
Classifying requirements is not paperwork for its own sake. It tells you who must confirm a requirement and how it will be verified. BABOK v3 uses four types:

| Type | Question it answers | Who confirms | ExportShield example |
|---|---|---|---|
| Business | Why are we doing this? Which goal? | Sponsor, management | "Decide 80 % of credit limit requests within 3 working days by end of next year." |
| Stakeholder | What does a group need to reach the goal? | Representatives of that group | "Underwriters need all buyer data in one screen when assessing a request." |
| Solution – functional | What must the solution do? | Process owner, BA, vendor | "The system shall pre-fill buyer name and address from ARES after the registration number is entered." |
| Solution – non-functional | How well, under which constraints? | IT, security, operations | "Buyer lookup shall respond within 5 seconds for 95 % of requests." |
| Transition | What is needed for the change itself? | Project manager, operations | "Open requests from the Excel tracker shall be migrated into PolicyHub before go-live." |

Business requirements come first. Every stakeholder and solution requirement should be traceable back to one. If you find a requirement that serves no business requirement, either a business goal is missing or the requirement is not needed. Module 06 covers how to write solution requirements precisely.

Other frameworks use slightly different names (IREB CPRE, for instance, distinguishes functional requirements, quality requirements and constraints). The idea is the same: separate *why*, *what* and *how well*.

### Preparing for elicitation [P1]
Much of good elicitation happens before the first meeting. Before you meet anyone:

1. **Understand the context.** Read what exists: process descriptions, the product brochure, old project documents, the org chart. You should not spend the interview asking what a "buyer" is.
2. **Identify stakeholders.** Who does the work, who decides, who is affected, who can block? (Stakeholder analysis is covered in module 16.) Do not forget compliance, IT security and operations; they bring non-functional requirements late if you do not invite them early.
3. **Define the goal of the session.** "Understand how claims are checked today and where time is lost" is a goal. "Talk about claims" is not.
4. **Choose techniques** (see the table below) and plan the sequence: for example, document analysis, then interviews, then observation, then a workshop to agree TO-BE.
5. **Prepare materials**: question script, a draft process diagram to correct, a blank template for notes.
6. **Logistics**: invitations with agenda, enough time (60 minutes for an interview is typical), permission to record if you want to.

### Interviews [P1]
The interview is the workhorse technique. Types:
- **Structured**: fixed questions in a fixed order. Comparable answers, little discovery.
- **Unstructured**: free conversation. Much discovery, hard to compare.
- **Semi-structured**: a prepared question bank, but you follow interesting answers. This is what you will use most.

**Open vs closed questions.** An *open* question cannot be answered with yes or no: "How do you decide whether financial statements are sufficient?" It invites explanation. A *closed* question gets a precise answer: "Is the 1 M EUR threshold the same for all countries?" Start open to explore, use closed questions to confirm details. A third kind, the *leading* question ("You would like this automated, right?"), should be avoided because it plants your answer.

**The funnel.** Move from broad to specific: context → process → problems → details → wishes → confirmation.

**Active listening.** Paraphrase ("So if documents are missing, you wait up to two weeks?"), ask follow-ups ("What happens then?"), notice hesitation ("You paused — is there an exception?"), and do not fill silences too fast. Take notes of facts *and* of the exact words people use; the vocabulary goes into your glossary.

**Useful question patterns:**
- "Walk me through the last request you handled, from the moment it arrived."
- "What happens when …?" (exceptions)
- "How often does that happen? How long does it take?" (impact)
- "What do you do when the system is down?" (workarounds)
- "Who else should I talk to?" (stakeholder discovery)
- "If you could change one thing, what would it be?" (priorities)
- "Why is that important?" (from solution to need)
- "How would you know the new process works?" (acceptance)

**After the interview:** write up notes the same day, separate facts, opinions and open questions, and send them to the interviewee for confirmation.

### Example: interview script for the ExportShield claims team [P1]
Goal: understand how a notification of non-payment is processed today and where time and errors occur. Interviewee: a claims handler. Duration: 60 minutes.

**Opening (5 min)**
1. Thank you; purpose of the meeting; how notes will be used; may I record?
2. What is your role and how long have you worked in claims?

**Process overview (15 min)**
3. Walk me through the last claim you processed, from receiving the notification to payment.
4. How does the notification arrive? (e-mail, portal, phone, letter)
5. Which systems and files do you use at each step? (ClaimDesk, DocVault, Excel, e-mail)
6. Who else is involved, and when do you hand over?

**Rules and decisions (15 min)**
7. Which documents must the exporter provide? What happens if one is missing?
8. How do you check that the invoice is covered by the policy?
9. How is the indemnity calculated? Where are the rules written down?
10. Who approves the payment, and does it depend on the amount?

**Problems and exceptions (15 min)**
11. Which part takes the longest? Why?
12. Where do mistakes happen most often?
13. What do you do differently from the official procedure, and why?
14. Tell me about an unusual claim from the last months.

**Wishes and closing (10 min)**
15. If you could change one thing, what would it be? Why?
16. How would you know a new process is better?
17. Who else should I talk to? Can I watch you process a claim next week?
18. Summary of what I heard; next steps; when you will receive notes.

Notice the order: process first, problems second, wishes last. If you ask for wishes first, you get solutions without context.

### Workshops and JAD [P1]
A **requirements workshop** brings several stakeholders together for a focused, facilitated session, usually 2–4 hours. Workshops are efficient for agreeing on a TO-BE process, resolving conflicts and prioritizing, because the decisions are made with everyone in the room.

**JAD** (Joint Application Design or Development) is a structured workshop format from the 1970s–80s where business users and IT designers work together to define requirements and design. The principle is still valid: the people who know the business and the people who build the solution talk directly.

Roles: a **facilitator** (often the BA) who keeps the process neutral, a **scribe** who records decisions, a **decision maker** who can settle disputes, and participants. Keep it to about 5–10 people.

Running a workshop:
1. Send the agenda, goal and pre-reading in advance.
2. Start with the goal and ground rules (timebox, phones away, parking lot for off-topic items).
3. Use visual material: a draft BPMN model on the wall or a [Miro](https://miro.com/) board, sticky notes, a prototype.
4. Close each topic with a decision or an action with an owner and date.
5. Send results within 24–48 hours.

Risk: a dominant participant (often the most senior) steers everything. Counter it by silent writing on sticky notes before discussion, round-robin input, and asking quiet people directly.

### Observation, document analysis and interface analysis [P2]
**Observation** (job shadowing) means watching someone do the actual work. *Passive* observation: you watch and take notes, questions later. *Active*: you ask while they work ("Why did you open that Excel?"). Observation reveals tacit steps, workarounds, interruptions and real timings. Ask permission, explain that you observe the process, not the person, and be aware that people behave differently when watched.

**Document analysis** means reading existing material: procedures, policy wording, forms, templates, reports, system screens, error logs, old requirements. It is a good first step because it costs stakeholders no time and gives you vocabulary. Limitation: documents are often outdated, and they describe the official process.

**Interface analysis** identifies the connections between the solution and its environment: other systems (PolicyHub ↔ DocVault), external services (ARES), users (screens), and organizations (exporter, reinsurer). For each interface you ask: what data, in which direction, how often, in which format, what happens on failure. This becomes the input for integration requirements (module 11 covers APIs).

### Surveys and focus groups [P2]
A **survey** (questionnaire) reaches many people cheaply. It works for confirming and quantifying: "How many credit limit requests do you handle per week?" or "Rate the current tracker from 1 to 5." It works poorly for discovering unknown needs. Keep it short (under 10 minutes), use mostly closed questions, test it on one person first, and add one open question at the end.

A **focus group** is a moderated discussion with 6–10 representative users or clients about their experiences and opinions, for example exporters discussing what they expect from an online claim notification. It is useful for user-facing products. Group dynamics can push towards consensus, so the moderator must encourage disagreement.

### Prototyping and wireframes [P1]
A **prototype** is an early model of the solution used to get feedback. A **wireframe** is a low-fidelity sketch of a screen: boxes, labels, buttons, no colors or design. People who cannot comment on a written requirement can immediately say "this field is missing" or "we never need that" when they see a screen.

- **Throw-away prototypes**: paper sketches, [draw.io](https://app.diagrams.net/) mock-ups. Cheap, fast, used only to learn.
- **Evolutionary prototypes**: built in the real platform (for example [Power Apps](https://make.powerapps.com/)) and improved into the final solution.

Practical tip: keep wireframes visibly rough. A polished mock-up invites discussion about colors and fonts instead of fields and rules, and stakeholders may think the system is almost finished.

For a credit limit request form you would sketch: exporter details (pre-filled), buyer registration number with a "look up" button, buyer name and address (filled from ARES, read-only), country, requested amount and currency, payment terms in days, attachments for financial statements, a submit button, and the validation messages. Every field on the sketch is a question to stakeholders: mandatory or optional, which format, who can change it.

### Brainstorming [P3]
Brainstorming generates many ideas in a short time. Rules: quantity over quality, no criticism during generation, build on others' ideas, then group and evaluate. A variant is *brainwriting*, where everyone writes ideas silently first, which reduces the influence of dominant voices. Use it when looking for solution options or root causes, for example "Why do credit limit decisions take 10 days?"

### Choosing a technique [P1]
| Situation | Good techniques | Why |
|---|---|---|
| New domain, you know little | Document analysis, interviews | Build vocabulary and context first |
| People cannot describe their work well | Observation, "walk me through the last case" | Reveals tacit knowledge |
| Many stakeholders with different views | Workshop | Agreement in one session |
| Many users, need numbers | Survey | Cheap, quantitative |
| Screens and forms | Wireframes, prototypes | People react to pictures |
| Integrations with other systems | Interface analysis, document analysis | Data, formats, error cases |
| Need ideas or root causes | Brainstorming, workshop | Breadth before depth |

In practice you combine three or four. A typical sequence for an ExportShield improvement: read procedures and sample requests → interview two underwriters and their manager → observe one morning of request handling → draw AS-IS and validate in a short workshop → sketch the TO-BE form and test it with users.

### Difficult situations [P1]
**Tacit knowledge.** Experts skip steps because they are automatic for them. Signs: the described process is suspiciously short, or numbers do not add up ("five steps but it takes three days"). Remedies: observation, asking for the last real case instead of the general rule, asking about exceptions ("When does this not work?"), and asking newcomers, who still notice the steps.

**Conflicting views.** Sales wants decisions in one day, Underwriting wants complete financial data. Do not pick a side. Make the conflict explicit, write down both positions and their reasons, link them to the business goal, and propose options (for example a fast track for small limits). If it cannot be resolved, the sponsor or process owner decides, and you record the decision.

**Solution-first stakeholders.** "We need a button that exports the tracker to Excel." Do not refuse and do not just write it down. Ask why: "What do you do with the export?" → "I send it to my manager every Friday." → "What does the manager do with it?" → "Checks which requests are older than a week." The real need is *visibility of overdue requests*. Options: a filtered view, an automatic weekly report, a timer escalation (module 04). The Excel button may still be the cheapest option, but now the decision is informed. Asking "why" repeatedly is known as the *5 Whys* technique.

**Vague answers.** "It should be fast." Ask for numbers and examples: "Fast compared to what? How long is acceptable? What is too slow?"

**Unavailable stakeholders.** Shorten sessions, come prepared with a draft to correct (people react faster to something wrong than to a blank page), or ask for a delegate with decision rights.

**Scope creep in interviews.** Stakeholders use the opportunity to ask for everything. Note every wish, mark out-of-scope ones as such, and say so politely: "I will note it as a separate idea; it is outside this project."

### Confirming results [P1]
Elicited information is not a requirement until the source has confirmed it. Techniques:
- **Meeting notes** sent within 24 hours: decisions, facts, open questions, actions with owner and date. Short and structured, not a transcript.
- **Playback**: repeat the understanding in your own words or show the diagram. "Let me play back what I heard: …" Mistakes surface immediately.
- **Walkthrough** of the drawn process or the requirement list with the stakeholders.
- **Prototype review**: users click through or comment on wireframes.

Keep track of where each requirement came from (source, date). This is the beginning of traceability (module 06).

### Elicitation in agile projects [P2]
In agile work (module 07), there is no big requirements phase. Elicitation happens continuously:
- High-level elicitation at the start for the vision, epics and story map.
- Detailed elicitation *just in time* during backlog refinement, a few sprints before a story is built.
- Feedback in sprint reviews, where stakeholders see working software and react.

Techniques stay the same, but sessions are shorter and more frequent. The results land as user stories and acceptance criteria rather than a large document. In hybrid projects with an external vendor, you often do both: a functional specification for the contract and stories for delivery.

### Using AI in elicitation [P2]
AI assistants such as [ChatGPT](https://chatgpt.com/), [Claude](https://claude.ai/) or [Copilot](https://copilot.microsoft.com/) can help in several places:
- **Preparing questions**: "Suggest interview questions for a claims handler at an export credit insurer, about checking documents for a non-payment notification." You get a first draft to adapt.
- **Role-play**: let the AI act as a stakeholder with a fictional profile to practice interviewing.
- **Summarizing**: turn a transcript into notes, list open questions, extract candidate requirements.
- **Checking**: ask it to find ambiguous words or missing exceptions in your notes.

Rules:
1. **Never paste company or client data into public AI tools.** Use fictional data or tools approved by your IT department. Recordings and transcripts of real interviews are confidential by default.
2. **Verify everything.** AI summaries tend to smooth over exceptions and disagreements, which are exactly what matters, and may invent plausible details.
3. **Be transparent.** If AI-generated content goes into official documents, follow your organization's rules for labeling it.

A good interview answer on this topic shows both the benefit and the limits: "I use AI to prepare a question bank and to check my notes for ambiguity, but only with non-confidential data, and I always confirm results with the stakeholders."

## Key terms
- **Elicitation** — drawing out requirements and related information from stakeholders and other sources.
- **Stakeholder** — a person or group that affects or is affected by the change.
- **Business requirement** — a goal or need of the organization that explains why the change is made.
- **Stakeholder requirement** — a need of a particular stakeholder group that must be met to reach the business goal.
- **Solution requirement** — a capability (functional) or quality (non-functional) the solution must have.
- **Transition requirement** — a temporary need for moving from the current to the future state, such as data migration or training.
- **Semi-structured interview** — an interview with a prepared question bank that allows follow-up on interesting answers.
- **Open question** — a question that invites explanation and cannot be answered with yes or no.
- **Active listening** — paraphrasing, asking follow-ups and checking understanding during a conversation.
- **Requirements workshop** — a facilitated session where several stakeholders define or agree requirements together.
- **JAD (Joint Application Design)** — a structured workshop format bringing business users and IT designers together.
- **Observation / job shadowing** — watching people do their actual work to understand the real process.
- **Document analysis** — studying existing documents, forms and systems to extract information.
- **Interface analysis** — identifying the data exchanged between the solution and other systems, users or organizations.
- **Wireframe** — a low-fidelity sketch of a screen used to discuss content and layout.
- **Tacit knowledge** — knowledge people have but do not express because it is obvious to them.
- **Playback** — repeating your understanding back to stakeholders to confirm it.
- **5 Whys** — asking why repeatedly to move from a symptom or proposed solution to the underlying need.

## Hands-on
:::exercise id="m05-e1" title="Write an interview script for the claims team" min="45" tool="text editor"
Goal: prepare a semi-structured interview that you could actually use.

1. Define the goal of the interview in one sentence, for example about the document check step in ExportShield claims.
2. Write 15–20 questions grouped into: opening, process, rules and decisions, problems and exceptions, wishes and closing.
3. Mark each question as open (O) or closed (C). At least two thirds should be open in the first half.
4. Add three follow-up questions you would ask if the answer is "it depends".
5. Remove any leading questions. Read each question aloud and ask yourself if it suggests an answer.
6. Prepare a one-page template for notes: facts, rules, pain points, open questions, actions.

Done when: the script fits 60 minutes, starts broad and goes specific, and ends with "who else should I talk to?".
:::

:::exercise id="m05-e2" title="Run a mock interview and extract requirements" min="60" tool="ChatGPT / Claude / Copilot"
Goal: practice interviewing and turn raw answers into requirements.

1. Find a partner (friend or family member) or use an AI assistant. For AI, start with a prompt like: "Play a claims handler at ExportShield Insurance, a fictional export credit insurer. You process notifications of non-payment using a system called ClaimDesk, e-mail and Excel. Answer only what I ask, be realistic, mention one or two frustrations only when asked about problems, and sometimes give vague answers." Use only fictional data.
2. Run your script from exercise m05-e1 for 30–40 minutes. Ask follow-up questions; do not just read the list.
3. Write meeting notes: facts, rules, pain points, open questions.
4. Extract at least 8 candidate requirements and classify them as business, stakeholder, functional, non-functional or transition.
5. Mark which statements you would need to confirm with a second source.

Done when: you have notes, a classified list of at least 8 requirements, and at least two places where you noticed a vague answer and asked for a number or example.
:::

:::exercise id="m05-e3" title="Wireframe a credit limit request form" min="45" tool="draw.io"
Goal: use a prototype to make requirements concrete.

1. On paper or in [draw.io](https://app.diagrams.net/) (search the shape library for "mockup"), sketch the form an exporter uses to request a credit limit.
2. Include: exporter details (pre-filled), buyer registration number with a lookup button, buyer name and address (read-only, from ARES), buyer country, requested amount and currency, payment terms in days, attachment upload, submit button.
3. Add notes next to each field: mandatory or optional, format, validation, source.
4. Show one error state, for example "Buyer not found in registry".
5. Write five questions the wireframe raised that you would ask stakeholders.

Done when: someone looking at your sketch can say which fields are mandatory and what happens when the lookup fails, and you have five open questions.
:::

## Self-check
:::q
Why is it called "elicitation" rather than "gathering"?
---
Because requirements are not lying around ready to be collected. Stakeholders express problems, wishes and solutions, and much of their knowledge is tacit. The BA has to actively draw out, question, analyze and confirm the information before it becomes a requirement.
:::

:::q
Classify: "Open requests from the Excel tracker must be moved into PolicyHub before go-live."
---
It is a transition requirement. It is needed only to move from the current state to the future state and will no longer apply once the migration is done.
:::

:::q
A stakeholder says "We need a button that sends the request to the Risk Committee." What do you do?
---
Ask why, until you reach the underlying need: perhaps large requests are forgotten or the committee lacks information. Then consider options, such as automatic routing based on amount or a committee queue. The button may still be the right answer, but the decision should be based on the need, not on the first proposed solution.
:::

:::q
Why are observation and "walk me through the last case" good against tacit knowledge?
---
Experts skip steps that feel obvious when they describe their work in general terms. Watching the work, or asking about one specific recent case, brings out those steps, the workarounds and the exceptions, because the person reconstructs what actually happened.
:::

:::q
When is a survey a poor choice?
---
When you need to discover unknown needs or understand reasons. Surveys work best for confirming and quantifying things you already know about, with closed questions to many people. They give little depth and you cannot ask follow-up questions.
:::

:::q
What should you do in the 24 hours after an interview?
---
Write up structured notes with facts, rules, pain points, open questions and actions, and send them to the interviewee for confirmation. Note the source and date of each item so that requirements can be traced back later.
:::

:::q
What are two risks of using a public AI tool to summarize an interview transcript?
---
First, confidentiality: a real transcript contains company and possibly client data that must not go into unapproved tools. Second, accuracy: the summary may drop exceptions and disagreements or add details nobody said, so it must be checked against the source and confirmed with stakeholders.
:::

## Interview corner
:::interview
How do you elicit requirements from a department you have never worked with?
---
- Prepare: read documents, understand the domain vocabulary, identify stakeholders.
- Start with interviews of key people, then observe the real work.
- Draw the AS-IS and play it back.
- Use a workshop to agree priorities or resolve conflicts, prototypes for screens.
- Confirm in writing and keep track of sources.

Typical mistake: describing only "I would ask them what they need", without preparation, techniques or confirmation.
:::

:::interview
Two departments want opposite things. How do you handle it?
---
- Make the conflict explicit and document both positions with their reasons.
- Go back to the business goal and the measurable objective.
- Look for options that satisfy both (for example different paths by amount or risk).
- If unresolved, escalate to the decision maker with the options and impacts, and record the decision.

Typical mistake: deciding yourself as the BA, or choosing the side of the more senior person without analysis.
:::

:::interview
What is the difference between a business requirement and a functional requirement? Give an example.
---
- Business requirement: why, organizational goal, for example "decide 80 % of requests within 3 working days".
- Functional requirement: what the solution does, for example "the system shall retrieve buyer data from ARES by registration number".
- Functional requirements must trace back to a business requirement.
- Mention stakeholder, non-functional and transition requirements as further types.

Typical mistake: giving two functional requirements and calling one of them "business".
:::

:::interview
A stakeholder gives vague answers like "it should be user-friendly and fast". What do you do?
---
- Ask for concrete examples and numbers: how fast, compared to what, what is unacceptable.
- Ask about a situation where the current system was too slow or confusing.
- Turn the answer into a measurable non-functional requirement and confirm it.
- Use a prototype to make "user-friendly" concrete.

Typical mistake: writing "the system shall be user-friendly" into the specification.
:::

:::interview
How do you use AI tools in requirements work?
---
- Draft question banks, role-play stakeholders, summarize, check ambiguity.
- Only non-confidential or fictional data in public tools; otherwise tools approved by IT.
- Always verify output and confirm results with real stakeholders.
- Follow internal rules on labeling AI-generated content.

Typical mistake: describing pasting real meeting transcripts into a public chatbot.
:::
