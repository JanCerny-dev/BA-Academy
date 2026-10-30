---
title: "Capstone: automating credit limit requests at ExportShield Insurance"
---

## The brief

ExportShield Insurance is a fictional export credit insurer. Exporters (the policyholders) sell goods abroad on credit. Before they ship, they ask ExportShield for a **credit limit** on each foreign buyer: "insure up to EUR 250,000 of invoices to Rheinwerk Handels GmbH".

Today the process looks like this:

- Requests arrive by **e-mail**, as free text or as an Excel attachment in three different templates.
- An assistant copies the data into **PolicyHub** (the policy system, run by the external vendor **NovaSoft s.r.o.**).
- An underwriter looks up the buyer in public registers by hand (for Czech companies in **ARES**), checks the country risk in a spreadsheet, and decides.
- The decision goes back to the exporter by e-mail. Nobody tracks how long it took.

Management complains that decisions take "about a week", that data gets mistyped, and that underwriters spend time on lookups instead of judgment. You have been asked, as the new IT Business Analyst, to analyze the process, propose a better one, specify it for NovaSoft, and build a low-code prototype of the intake part.

This project runs alongside the modules. Each step lists the module it belongs to. Do the steps in order; together they become your **portfolio** – the thing you show at the interview when someone asks "what have you actually done?".

:::warning
Everything here is fictional. Do not use real data from your current or any other employer, not even "anonymized". In the interview, say that you built the portfolio on a fictional case to keep company data safe – interviewers see that as good judgment.
:::

## Steps and deliverables

:::exercise id="p-01" title="1. Problem statement and mini business case (module 03)" min="90" tool="Word / Google Docs"
1. Write a problem statement: who is affected, what happens, what it costs, what "better" looks like.
2. Ask "why" five times about the one-week decision time and draw a fishbone diagram of possible causes.
3. Estimate the cost of today's process with **clearly labeled assumptions** (e.g. 6,000 requests a year, 20 minutes of manual work each, internal hourly cost).
4. Write one paragraph on what you would measure before and after the change.

**Done when:** one page that a manager could read in three minutes and understand why this is worth doing.
:::

:::exercise id="p-02" title="2. AS-IS and TO-BE process in BPMN (module 04)" min="180" tool="demo.bpmn.io"
1. Model the AS-IS process with pools for Exporter and ExportShield, and lanes for Assistant and Underwriter. Use a message flow for the e-mails.
2. Mark the pain points with text annotations (re-typing, manual lookup, no tracking).
3. Model the TO-BE: web form or structured e-mail → automatic data extraction → ARES lookup (service task) → automatic pre-check rules (business rule task) → underwriter decision (user task) → automatic notification. Add a **timer boundary event** that escalates when a request waits more than 2 working days.
4. Export both diagrams as PNG and save the `.bpmn` files.

**Done when:** a colleague who has never seen the process can explain it back to you from the diagrams alone.
:::

:::exercise id="p-03" title="3. Stakeholders and elicitation (modules 05 and 16)" min="120" tool="Miro / draw.io"
1. List stakeholders (exporter, assistant, underwriter, head of underwriting, IT, NovaSoft, compliance, management) and place them on a power/interest grid.
2. Write an interview script (10–15 questions) for an underwriter.
3. Run a mock interview – with a friend, or with an AI assistant asked to play an underwriter at a fictional insurer. Write up the notes and extract at least 10 candidate requirements.
4. Build a RACI for the project.

**Done when:** you have a stakeholder map, a RACI and interview notes with requirements traced to who said them.
:::

:::exercise id="p-04" title="4. Functional specification for the vendor (module 06)" min="300" tool="Word / Confluence"
Write a functional specification for NovaSoft for the change "Structured credit limit intake with ARES pre-check". Use the template from module 06. It must contain at least:
1. Context, goal, scope and **out of scope**.
2. Actors and the TO-BE process (link your BPMN).
3. 12–20 functional requirements with IDs (FR-01 …), each testable.
4. Business rules for the automatic pre-check (e.g. buyer not found in register → manual review; country risk 6–7 → always manual; requested amount over a threshold → senior underwriter).
5. Data requirements: the request fields, formats, mandatory/optional, validation.
6. 5–8 non-functional requirements with numbers (response time of the ARES lookup, availability, audit log, data retention).
7. Open questions for the business and for NovaSoft.

**Done when:** a developer could estimate the work from it and a tester could write test cases from it without calling you.
:::

:::exercise id="p-05" title="5. Backlog: epics, user stories, Gherkin (module 07)" min="150" tool="Jira Free / Trello"
1. Turn the specification into 1–2 epics and 8–12 user stories.
2. Write acceptance criteria for every story; write at least 4 of them in Gherkin, including one Scenario Outline for the pre-check rules.
3. Put the stories into a Jira Free (or Trello) board, prioritize with MoSCoW (see modules 03 and 06) and plan a first sprint.
4. Take a screenshot of the board for the portfolio.

**Done when:** each story passes the INVEST check and the board shows a realistic first sprint.
:::

:::exercise id="p-06" title="6. Data model and data dictionary (modules 08 and 09)" min="120" tool="Mermaid Live / draw.io"
1. Draw an ER diagram of the entities involved: exporter, policy, buyer, country, credit limit request, decision.
2. Write a data dictionary for the credit limit request (field, meaning, type, mandatory, source, example).
3. Draw a sequence diagram: form → PolicyHub → ARES API → PolicyHub → underwriter notification.
4. Draw a state diagram for a credit limit request (Requested → In review → Approved / Reduced / Rejected, plus Withdrawn).

**Done when:** the three diagrams agree with each other and with the specification.
:::

:::exercise id="p-07" title="7. SQL: size the problem and check the data (module 10)" min="150" tool="SQL lab"
In the [SQL lab](sql.html), write queries that answer:
1. How many credit limits were requested per month, and how many were decided?
2. Average and maximum days from request to decision, per underwriter.
3. Share of requests approved, reduced and rejected, per buyer country risk category.
4. Which data-quality problems exist (decided before requested, missing buyer country, duplicate invoice numbers, claims on paid invoices)?
5. Total approved exposure per country.

Save the queries with a one-line business interpretation of each result.

**Done when:** you can say, with numbers, how slow the current process is and where the data is unreliable.
:::

:::exercise id="p-08" title="8. Integration specification and Postman collection (module 11)" min="180" tool="Postman / API lab"
1. Call ARES for three Czech companies (in the [API lab](api.html) or Postman). Save the responses.
2. Write a field-mapping table: ARES field → PolicyHub buyer field → transformation → mandatory?
3. Describe error handling: company not found (404), ARES unavailable (timeout / 5xx), invalid IČO format (400).
4. Build a Postman collection with the ARES requests and simple tests (status is 200, field `ico` exists).
5. Optional: write a tiny OpenAPI description of the internal "pre-check" endpoint NovaSoft should build.

**Done when:** the integration section of your specification is precise enough that the vendor has no questions about fields or errors.
:::

:::exercise id="p-09" title="9. Test cases and UAT plan (module 13)" min="150" tool="Excel / Google Sheets"
1. Write 12–15 test cases from your requirements and acceptance criteria, including boundary values (amount thresholds) and a decision table for the pre-check rules.
2. Write a one-page UAT plan: scope, participants, test data, entry and exit criteria, schedule, sign-off.
3. Write two example defect reports as if found in UAT (one high severity, one cosmetic).

**Done when:** every functional requirement is covered by at least one test case (show it in a small traceability table).
:::

:::exercise id="p-10" title="10. Low-code prototype of the intake (module 14)" min="300" tool="Make (free) / Power Automate"
Build a working prototype of the intake part:
1. Trigger: a web form (Make webhook, Microsoft Forms or Google Forms) with exporter, buyer IČO, amount, currency.
2. Call the ARES API with the IČO; branch on found / not found.
3. Apply one or two simple pre-check rules (e.g. amount over 500,000 → flag for senior underwriter).
4. Write a row into a spreadsheet (the stand-in for PolicyHub) with the request, the ARES company name and the pre-check result.
5. Send an e-mail confirmation to the requester.
6. Write a one-page run-book: trigger, steps, error handling, owner, how to switch it off.

**Done when:** you can demo it live in two minutes – submit a form and show the row and the e-mail appear.
:::

:::exercise id="p-11" title="11. AI use case: document triage (module 15)" min="120" tool="ChatGPT / Claude / Copilot"
Exporters often attach financial statements and contracts to their requests. Design an AI-assisted step that classifies attachments and extracts key figures.
1. Describe the process change and where a human checks the AI output.
2. Define success metrics and acceptance criteria for a probabilistic output (e.g. at least 95 % correct document type on a test set of 50 fictional documents).
3. Build an evaluation table of 10 test inputs (fictional) with expected outputs, run them through an AI assistant, and record the results.
4. List the risks (confidential data, errors, bias, regulation) and the controls.

**Done when:** a one-page AI use-case canvas plus the evaluation table.
:::

:::exercise id="p-12" title="12. Presentation and status report (module 16)" min="150" tool="PowerPoint / Google Slides"
1. Prepare a 7–10 slide presentation for management: problem → AS-IS → TO-BE → benefits (numbers from step 1 and 7) → demo of the prototype → plan → what you need from them.
2. Record yourself presenting it in 10 minutes.
3. Write one weekly status report (RAG status, done, next, risks, decisions needed) as if the project were in week 6.

**Done when:** the recording is under 10 minutes and you would be comfortable showing it to a hiring manager.
:::

:::exercise id="p-13" title="13. Portfolio (module 17)" min="180" tool="PDF / Notion / GitHub Pages"
Collect the best pieces into a portfolio of 8–12 pages or one web page: problem statement, BPMN AS-IS/TO-BE, an excerpt of the specification, 3 user stories with Gherkin, the ER and sequence diagrams, 3 SQL queries with findings, the Postman collection screenshot, the automation demo (screenshots or a short video), the UAT plan, and the presentation.

Add one paragraph at the top: "What I would do differently in a real company" – approvals, security review, vendor contract, change management.

**Done when:** you can walk an interviewer through it in 5 minutes and go deep on any piece they pick.
:::

## How this maps to the job ad

| The ad says | Capstone step |
|---|---|
| Take change requests from departments, write technical specifications for vendors | 3, 4, 8 |
| Design new features and optimize systems in line with the architecture | 2, 6, 8 |
| Work with IT vendors and stakeholders | 3, 4, 12 |
| Support testers, test deliveries, report status | 9, 12 |
| Automations in low-code platforms | 10 |
| Present outputs, train colleagues | 12 |
| AI integration into internal processes | 11 |
| Basic SQL, API, JSON/XML | 7, 8 |
| UML or BPMN | 2, 6 |
