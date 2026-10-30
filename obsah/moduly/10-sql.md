---
id: 10
slug: sql
title: SQL for business analysts
phase: C
priority: P1
quick_min: 15
deep_min: 90
job_ad: "základní znalost SQL"
---

## Why this matters
The job ad asks for basic SQL. Analysts use it every week: to answer a business question without waiting for a report, to check that a delivered change works, to find bad data, and to put a number on a problem before anyone pays for a fix. You do not need to design databases or tune performance. You need to read data confidently with `SELECT`, combine tables with joins, and summarize with `GROUP BY`. Every example here runs on the ExportShield dataset in the site's SQL playground.

## Quick version
**SQL** (Structured Query Language) is the standard language for working with relational databases. A query describes *what* you want; the database works out *how* to get it.

**The basic shape of a query:**

```text
SELECT   columns or calculations
FROM     table
JOIN     other table ON how rows match
WHERE    filter on rows
GROUP BY columns to group by
HAVING   filter on groups
ORDER BY sort order
LIMIT    number of rows;
```

To read data from a table you need only `SELECT` and `FROM`; the other clauses are optional. The clauses you use must be written in this order.

**What each part does:**

- `SELECT name, city` picks columns. `SELECT *` takes all of them (fine for exploring, not for reports).
- `WHERE` filters rows: `=`, `<>` (not equal), `>`, `<`, `IN ('A','B')`, `BETWEEN x AND y`, `LIKE '%text%'` (pattern), `IS NULL` (empty).
- `ORDER BY amount DESC` sorts; `LIMIT 5` keeps the first five rows.
- `DISTINCT` removes duplicate rows from the result.
- **Aggregate functions** summarize many rows into one value: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`.
- `GROUP BY status` makes one result row per status; aggregates are then calculated per group. `HAVING` filters those groups.
- **Joins** combine tables through keys. `INNER JOIN` keeps only rows that match on both sides. `LEFT JOIN` keeps every row from the left table and fills the right side with `NULL` when there is no match.
- `CASE WHEN ... THEN ... ELSE ... END` is if/else inside a query, useful for categories.

**NULL** means "no value". It is never equal to anything, not even another NULL, so you must write `paid_date IS NULL`, not `paid_date = NULL`.

**How analysts use SQL:**

1. **Answer business questions**: "How many claims did we pay last year, and for how much?"
2. **Verify test results**: after a release, check that the database contains what the requirement says.
3. **Check data quality**: find missing, invalid, duplicate or contradictory data.
4. **Size a problem**: "18 of 39 credit limit decisions took more than 14 days" is a stronger business case than "decisions are slow".

**Reading versus writing.** `INSERT`, `UPDATE` and `DELETE` change data. Analysts read them in specifications and migration scripts, but rarely run them in production: changes there go through applications, approved scripts and change management, with an audit trail.

**Where to practice:** the site's SQL playground (`sql.html`) has the ExportShield data preloaded. Alternatively paste `data/sql/exportshield.sql` into [SQLite Online](https://sqliteonline.com/). For guided basics, [SQLBolt](https://sqlbolt.com/) has short interactive lessons.

**Interview one-liner:** "I write SELECT queries with joins, filters and GROUP BY to answer questions, verify test results and check data quality. I know the difference between INNER and LEFT JOIN and how NULLs behave."

## Deep dive

### Setup and the dataset [P1]
Open the SQL playground (`sql.html`). The ExportShield tables are loaded: `countries`, `customers`, `buyers`, `policies`, `credit_limits`, `invoices`, `claims`, `payments`. If you prefer [SQLite Online](https://sqliteonline.com/), paste the whole content of `data/sql/exportshield.sql` into the editor and run it once; it creates and fills the tables.

Two facts about the data you need for the examples:

- **"Today" is 2026-09-30.** The data is a snapshot. Queries use this date as a fixed value instead of the current date so that results stay the same.
- **Amounts are in the row's currency** (EUR or USD). Adding EUR and USD together gives a meaningless number, so many examples filter or group by currency.

The data model is explained in the data module. Short version: a customer (exporter) holds policies; under a policy it requests credit limits on buyers; it sends invoices to buyers; an unpaid invoice can lead to a claim; a claim is settled by payments.

SQL keywords are not case-sensitive (`select` works like `SELECT`); writing them in capitals is a readability convention. Text values in quotes are compared case-sensitively in SQLite (the playground) and PostgreSQL: `'Approved'` does not match `'APPROVED'`. SQL Server and MySQL usually compare text case-insensitively, depending on the database settings (collation), so check before you rely on it.

### SELECT, FROM and WHERE [P1]
The simplest query returns a whole table:

```sql
SELECT * FROM countries;
```

Result: 12 rows, columns `code`, `name`, `risk_category`.

Pick columns and filter rows:

```sql
SELECT code, name, risk_category
FROM countries
WHERE risk_category >= 5;
```

Result: 5 rows: Brazil, Turkey, Kazakhstan (5), Egypt (6), Ukraine (7).

Comparison operators: `=`, `<>` (not equal; `!=` also works in most databases), `<`, `<=`, `>`, `>=`. Combine conditions with `AND`, `OR` and `NOT`; use parentheses when you mix `AND` and `OR`, otherwise `AND` is evaluated first and results surprise you.

```sql
SELECT id, name, segment
FROM customers
WHERE segment <> 'CORPORATE';
```

Result: 10 customers (SME and MICRO).

**IN** tests against a list:

```sql
SELECT id, status, requested_amount, approved_amount
FROM credit_limits
WHERE status IN ('REDUCED', 'REJECTED');
```

Result: 18 rows (14 reduced, 4 rejected). Look at the limit with id 6: REJECTED, but `approved_amount` is 75,000. That is a planted data quality issue.

**BETWEEN** includes both ends. Dates stored as ISO text (`YYYY-MM-DD`) compare correctly:

```sql
SELECT invoice_no, amount, issue_date
FROM invoices
WHERE issue_date BETWEEN '2026-01-01' AND '2026-03-31';
```

Result: 19 invoices issued in Q1 2026.

**LIKE** matches patterns: `%` stands for any number of characters, `_` for exactly one.

```sql
SELECT name, city
FROM customers
WHERE name LIKE '%a.s.';
```

Result: 5 joint-stock companies (names ending in "a.s."). In SQLite, `LIKE` ignores upper/lower case for English letters; other databases differ.

**IS NULL** finds missing values:

```sql
SELECT invoice_no, amount, currency, due_date
FROM invoices
WHERE paid_date IS NULL;
```

Result: 31 unpaid invoices, some not yet due. `WHERE paid_date = NULL` would return 0 rows, because a comparison with NULL is never true.

### ORDER BY, LIMIT, DISTINCT and aliases [P1]

```sql
SELECT invoice_no, amount, currency
FROM invoices
ORDER BY amount DESC
LIMIT 5;
```

Result: the five largest invoices, starting with INV-2025-07002 (157,900 EUR). Note the second one is in USD; sorting by amount across currencies is fine for a quick look but not for a report.

`ASC` (ascending) is the default. `LIMIT` is SQLite, PostgreSQL and MySQL syntax; SQL Server uses `SELECT TOP 5`, Oracle uses `FETCH FIRST 5 ROWS ONLY`.

`DISTINCT` removes duplicates:

```sql
SELECT DISTINCT sector
FROM buyers
ORDER BY sector;
```

Result: 10 sectors, from Agriculture to Transport.

**Aliases** rename columns (`AS customer_name`) or give tables a short name (`customers AS c`). Table aliases become essential with joins.

```sql
SELECT c.name AS customer_name,
       c.segment AS customer_segment
FROM customers AS c
WHERE c.city = 'Praha';
```

Result: 1 row, Praha Rail Parts a.s.

### Aggregates, GROUP BY and HAVING [P1]
Aggregate functions turn many rows into one value.

```sql
SELECT COUNT(*)          AS all_invoices,
       COUNT(paid_date)  AS paid_invoices,
       MIN(issue_date)   AS first_issued,
       MAX(issue_date)   AS last_issued
FROM invoices;
```

Result: 78 invoices, 47 paid, first issued 2024-04-22, last 2026-09-17. `COUNT(*)` counts rows; `COUNT(column)` counts only non-NULL values. That difference is a quick way to measure completeness.

`GROUP BY` produces one row per group:

```sql
SELECT currency,
       COUNT(*)              AS invoices,
       SUM(amount)           AS total_amount,
       ROUND(AVG(amount), 0) AS avg_amount
FROM invoices
GROUP BY currency;
```

Result: EUR 69 invoices, 2,960,400 in total; USD 9 invoices, 443,300.

```sql
SELECT status, COUNT(*) AS claims, SUM(claimed_amount) AS claimed
FROM claims
GROUP BY status
ORDER BY claims DESC;
```

Result: PAID 7, IN_REVIEW 3, then NOTIFIED, APPROVED (2 each) and REJECTED 1. (The `claimed` total mixes currencies because one rejected and one notified claim are in USD; the next sections show how to handle that.)

The rule for `GROUP BY`: every column in `SELECT` must either be in `GROUP BY` or inside an aggregate function. SQLite is lenient and lets you break the rule, returning a value from an arbitrary row of the group; most other databases (PostgreSQL, SQL Server, Oracle, MySQL in its default mode) raise an error.

`WHERE` filters rows *before* grouping. `HAVING` filters groups *after* aggregation:

```sql
SELECT buyer_id, COUNT(*) AS unpaid_invoices
FROM invoices
WHERE paid_date IS NULL
GROUP BY buyer_id
HAVING COUNT(*) >= 3;
```

Result: 4 buyers (IDs 4, 5, 8, 19) with three or more unpaid invoices.

### INNER JOIN [P1]
Data about one business event is spread across tables. A join puts it back together by matching keys.

```sql
SELECT i.invoice_no, i.amount, i.currency, b.name AS buyer
FROM invoices AS i
INNER JOIN buyers AS b ON b.id = i.buyer_id
WHERE i.paid_date IS NULL
ORDER BY i.amount DESC;
```

Result: the 31 unpaid invoices, now with buyer names; the largest is 119,100 USD from Great Lakes Industrial Supply Inc.

How to read it: for each invoice, find the buyer whose `id` equals the invoice's `buyer_id`. `INNER JOIN` (or just `JOIN`) keeps only pairs that match. An invoice with a non-existent buyer would silently disappear.

**Pitfall: joins can multiply rows.** If the right table has two matching rows, the left row appears twice:

```sql
SELECT COUNT(*) AS rows_after_join
FROM invoices AS i
JOIN credit_limits AS l
  ON l.policy_id = i.policy_id AND l.buyer_id = i.buyer_id;
```

Result: 80, although there are only 78 invoices. Policy 18 has two credit limit rows for buyer 2 (a reduced limit and a new open request), so each of that buyer's two invoices is counted twice. Always compare the row count before and after a join when you sum amounts.

### LEFT JOIN and why NULLs appear [P1]
`LEFT JOIN` keeps **every row from the left table** (the one after `FROM`). Where the right table has a match, its columns are filled in. Where there is no match, the right-side columns are `NULL`.

Compare these two queries:

```sql
SELECT b.id, b.name, b.country_code, co.name AS country, co.risk_category
FROM buyers AS b
INNER JOIN countries AS co ON co.code = b.country_code;
```

Result: 24 rows.

```sql
SELECT b.id, b.name, b.country_code, co.name AS country, co.risk_category
FROM buyers AS b
LEFT JOIN countries AS co ON co.code = b.country_code
ORDER BY co.risk_category DESC;
```

Result: 25 rows. Buyer 24, Baltic Timber Traders, has no country code, so there is nothing to match. `INNER JOIN` dropped it without warning; `LEFT JOIN` keeps it with `NULL` in `country` and `risk_category`. For a risk report, losing a buyer silently is a real problem.

LEFT JOIN also answers "which ones have **no** related row?":

```sql
SELECT b.id, b.name
FROM buyers AS b
LEFT JOIN credit_limits AS l ON l.buyer_id = b.id
WHERE l.id IS NULL;
```

Result: 1 buyer, Deccan Engineering Pvt Ltd, without any credit limit.

And it shows claims with and without payments:

```sql
SELECT cl.id AS claim_id, cl.status, cl.indemnity_amount, p.id AS payment_id, p.amount
FROM claims AS cl
LEFT JOIN payments AS p ON p.claim_id = cl.id
ORDER BY cl.id;
```

Result: 17 rows for 15 claims. Claims 5 and 6 appear twice (paid in two instalments). Claim 7 has status PAID but `NULL` payment columns: a consistency problem.

Rule of thumb: when the question is "all X, with Y if there is one", use `LEFT JOIN` with X on the left. `RIGHT JOIN` and `FULL OUTER JOIN` also exist; you can always rewrite a right join as a left join by swapping the tables.

### Joining many tables [P1]
Follow the foreign keys step by step. Claim → invoice → policy → customer, and invoice → buyer → country:

```sql
SELECT cl.id AS claim_id,
       cu.name AS exporter,
       b.name  AS buyer,
       co.name AS buyer_country,
       i.invoice_no,
       cl.claimed_amount,
       i.currency,
       cl.status
FROM claims AS cl
JOIN invoices  AS i  ON i.id  = cl.invoice_id
JOIN policies  AS p  ON p.id  = i.policy_id
JOIN customers AS cu ON cu.id = p.customer_id
JOIN buyers    AS b  ON b.id  = i.buyer_id
LEFT JOIN countries AS co ON co.code = b.country_code
ORDER BY cl.id;
```

Result: 15 rows, one per claim, readable for a business user. Claim 1: Moravia AgroTech a.s. against Parana Agro Comercial Ltda (Brazil), 24,200 EUR, PAID. The last join is a LEFT JOIN on purpose, so that a buyer without a country would not drop out.

Tip: build long joins one table at a time and check the row count after each step.

### CASE WHEN [P1]
`CASE` creates a value based on conditions, evaluated top to bottom; the first true branch wins.

```sql
SELECT code, name, risk_category,
       CASE
         WHEN risk_category <= 2 THEN 'Low'
         WHEN risk_category <= 4 THEN 'Medium'
         ELSE 'High'
       END AS risk_band
FROM countries;
```

Combined with `GROUP BY`, CASE turns into a quick segmentation:

```sql
SELECT CASE
         WHEN risk_category <= 2 THEN 'Low'
         WHEN risk_category <= 4 THEN 'Medium'
         ELSE 'High'
       END AS risk_band,
       COUNT(*) AS limits,
       SUM(l.requested_amount) AS requested,
       SUM(l.approved_amount)  AS approved
FROM credit_limits AS l
JOIN buyers AS b     ON b.id = l.buyer_id
JOIN countries AS co ON co.code = b.country_code
WHERE l.status <> 'REQUESTED'
GROUP BY risk_band
ORDER BY risk_band;
```

Result: High 14 limits (3.39 million requested, 1.43 million approved), Low 19 (3.76 / 3.40 million), Medium 5. Underwriters approve a much smaller share in high-risk countries, as expected. Two caveats a careful analyst would mention: the amounts mix EUR and USD, and one decided limit is missing (39 decisions exist, the bands add up to 38) because the buyer without a country was dropped by the INNER JOIN.

A common pattern is counting with CASE: `SUM(CASE WHEN status = 'REJECTED' THEN 1 ELSE 0 END)` counts rejected rows inside a group.

### Dates in SQLite [P1]
SQLite has no separate date type; dates are stored as text `YYYY-MM-DD` and handled with functions:

- `date('2026-09-30', '-90 days')` returns `2026-07-02`.
- `strftime('%Y-%m', issue_date)` returns the year and month, e.g. `2026-03`.
- `julianday(date)` converts a date to a day number, so subtracting two of them gives the number of days between them.
- `date('now')` is today's date; we use the fixed snapshot date instead.

Days overdue for unpaid invoices:

```sql
SELECT invoice_no, due_date,
       CAST(julianday('2026-09-30') - julianday(due_date) AS INTEGER) AS days_overdue
FROM invoices
WHERE paid_date IS NULL
  AND due_date < '2026-09-30'
ORDER BY days_overdue DESC;
```

Result: 23 overdue invoices, the oldest 798 days overdue (INV-2024-02003).

Invoices per month:

```sql
SELECT strftime('%Y-%m', issue_date) AS month, COUNT(*) AS invoices
FROM invoices
WHERE issue_date >= '2026-01-01'
GROUP BY month
ORDER BY month;
```

Result: 9 months; January 2026 has the most invoices (10).

**Other databases differ.** SQL Server uses `DATEDIFF(day, a, b)` and `GETDATE()`, Oracle subtracts dates directly and uses `SYSDATE`, PostgreSQL uses `CURRENT_DATE` and `date_part`. The concepts are the same; look up the function names for the database you work with.

### Subqueries and EXISTS [P2]
A **subquery** is a query inside another query, in brackets.

Invoices above the average EUR invoice:

```sql
SELECT invoice_no, amount, currency
FROM invoices
WHERE currency = 'EUR'
  AND amount > (SELECT AVG(amount) FROM invoices WHERE currency = 'EUR')
ORDER BY amount DESC;
```

Result: 22 invoices (the EUR average is about 42,900).

`EXISTS` checks whether a related row exists. Customers with at least one claim:

```sql
SELECT cu.id, cu.name
FROM customers AS cu
WHERE EXISTS (
  SELECT 1
  FROM claims cl
  JOIN invoices i ON i.id = cl.invoice_id
  JOIN policies p ON p.id = i.policy_id
  WHERE p.customer_id = cu.id
);
```

Result: 7 customers. `NOT EXISTS` gives the opposite. `NOT IN` with a subquery also works, but it returns nothing if the subquery contains a NULL, so `NOT EXISTS` is the safer habit:

```sql
SELECT name FROM buyers
WHERE id NOT IN (SELECT buyer_id FROM invoices);
```

Result: 3 buyers that never received an invoice.

### Common table expressions (WITH) [P2]
A **CTE** (common table expression) gives a subquery a name at the top of the query, so a complex query reads as steps.

```sql
WITH overdue AS (
  SELECT i.*, p.customer_id
  FROM invoices i
  JOIN policies p ON p.id = i.policy_id
  WHERE i.paid_date IS NULL
    AND i.due_date < '2026-09-30'
)
SELECT cu.name, COUNT(*) AS overdue_invoices, SUM(o.amount) AS overdue_amount, o.currency
FROM overdue o
JOIN customers cu ON cu.id = o.customer_id
GROUP BY cu.name, o.currency
ORDER BY overdue_amount DESC;
```

Result: 11 rows; Polabi Chemicals a.s. has the largest overdue EUR amount (3 invoices, 139,100). Grouping by currency as well keeps EUR and USD apart.

### Window functions (teaser) [P3]
Window functions calculate across related rows *without* collapsing them into one row. `ROW_NUMBER()` ranks rows within a group:

```sql
SELECT b.name AS buyer, i.invoice_no, i.amount,
       ROW_NUMBER() OVER (PARTITION BY i.buyer_id ORDER BY i.amount DESC) AS rank_in_buyer
FROM invoices i
JOIN buyers b ON b.id = i.buyer_id
WHERE i.currency = 'EUR'
ORDER BY b.name, rank_in_buyer
LIMIT 8;
```

Result: each buyer's invoices numbered from the largest; Alpenmarkt Vertrieb GmbH has five. Other useful ones: `SUM(...) OVER (ORDER BY date)` for running totals, `LAG()` to compare with the previous row. Supported by SQLite 3.25 and later and by all major databases.

### INSERT, UPDATE, DELETE: read, don't run [P2]
These statements change data. You should understand them when you see them in a migration script, a test data setup or a vendor's fix:

```sql
INSERT INTO countries (code, name, risk_category)
VALUES ('MX', 'Mexico', 4);

UPDATE credit_limits
SET approved_amount = 0
WHERE id = 6;

DELETE FROM payments
WHERE id = 8;
```

The most dangerous mistake is an `UPDATE` or `DELETE` without `WHERE`: it changes every row in the table.

Why analysts rarely write data in production:

- **Audit and accountability**: in a regulated insurer, every change to a policy or claim must be traceable to a person, a reason and an approval. Applications record that; a manual `UPDATE` bypasses it.
- **Business logic**: the application also writes history, sends notifications and updates related records. A direct change skips all of that and leaves the data inconsistent.
- **Segregation of duties**: the person who specifies a change should not be the one who executes it unchecked.
- **Change management**: data fixes go through an approved script, tested first, run by the vendor or operations team.

In a test environment or in your own copy of the data (like the SQL playground), experimenting is fine. If you break the playground data, reload it.

### How analysts use SQL at work [P1]
**1. Answering business questions.** "How many credit limit decisions did we make and how long did they take?"

```sql
SELECT COUNT(*) AS decisions,
       ROUND(AVG(julianday(decided_on) - julianday(requested_on)), 1) AS avg_days,
       SUM(CASE WHEN julianday(decided_on) - julianday(requested_on) > 14 THEN 1 ELSE 0 END) AS over_14_days
FROM credit_limits
WHERE decided_on IS NOT NULL;
```

Result: 39 decisions, average 12.5 days, 18 took more than 14 days.

**2. Sizing a problem for a business case.** The last result is the size of the problem: almost half of the decisions take more than two weeks. If a proposed ARES integration saves a day per request, you now have a base to calculate the benefit. Always state the period, the source and the caveats (here: one record has a negative duration, a data error).

**3. Verifying test results.** Turn an acceptance criterion into a query that must return zero rows. Criterion: "An APPROVED or REDUCED limit always has an approved amount greater than zero and not higher than the requested amount."

```sql
SELECT id, status, requested_amount, approved_amount
FROM credit_limits
WHERE status IN ('APPROVED', 'REDUCED')
  AND (approved_amount <= 0 OR approved_amount > requested_amount);
```

Result: 0 rows, so the criterion holds in this data. A query like this can be rerun after every release.

**4. Checking data quality.** Search for rows that break rules: missing values, invalid formats, contradictions, duplicates. The exercises below contain several such checks. Report findings with counts, examples and impact, not just "the data is bad".

Habits that keep you out of trouble: start with `SELECT * ... LIMIT 10` to see the data; count rows before and after each join; never add up different currencies; write down the snapshot date and filters next to every number you send to someone.

### Solutions
:::tip
Try the exercises in the Hands-on section first. Compare only after you have your own query; there are often several correct solutions. All results below are for the ExportShield dataset with snapshot date 2026-09-30.
:::

**1.** 3 rows: Rheinwerk Handels, Nordhafen Logistik, Bavaria Bau Supplies.

```sql
SELECT id, name, sector
FROM buyers
WHERE country_code = 'DE';
```

**2.** SME 8, CORPORATE 5, MICRO 2.

```sql
SELECT segment, COUNT(*) AS customers
FROM customers
GROUP BY segment
ORDER BY customers DESC;
```

**3.** 11 invoices; two of them are in USD, so "over 100,000" means different values.

```sql
SELECT invoice_no, amount, currency
FROM invoices
WHERE amount > 100000
ORDER BY amount DESC;
```

**4.** 4 open requests, IDs 40 to 43, the oldest from 2026-09-08.

```sql
SELECT id, policy_id, buyer_id, requested_amount, currency, requested_on
FROM credit_limits
WHERE status = 'REQUESTED'
ORDER BY requested_on;
```

**5.** 2 rows with the same company ID: the same exporter registered twice (a uniqueness issue).

```sql
SELECT id, name, ico
FROM customers
WHERE name LIKE '%Glass%';
```

**6.** EUR 5,004,000 and USD 980,000.

```sql
SELECT currency, SUM(approved_amount) AS total_approved
FROM credit_limits
WHERE status IN ('APPROVED', 'REDUCED')
GROUP BY currency;
```

**7.** E. Kralova 12, J. Marek 10, T. Bily 10, P. Novotna 7.

```sql
SELECT underwriter, COUNT(*) AS decisions
FROM credit_limits
WHERE decided_on IS NOT NULL
GROUP BY underwriter
ORDER BY decisions DESC;
```

**8.** 8 buyers; Dnipro Agro Holding (Ukraine, 7) first. The buyer without a country is not in the list, and that is a finding too.

```sql
SELECT b.name AS buyer, co.name AS country, co.risk_category
FROM buyers AS b
JOIN countries AS co ON co.code = b.country_code
WHERE co.risk_category >= 5
ORDER BY co.risk_category DESC, b.name;
```

**9.** 25 rows; Steppe Rail Service has 4 limits, Deccan Engineering 0. Use `COUNT(l.id)`, not `COUNT(*)`, or buyers without limits show 1.

```sql
SELECT b.name AS buyer, COUNT(l.id) AS credit_limits
FROM buyers AS b
LEFT JOIN credit_limits AS l ON l.buyer_id = b.id
GROUP BY b.id, b.name
ORDER BY credit_limits DESC, b.name;
```

**10.** E. Kralova 25.0 % (3 of 12), J. Marek 10.0 %, the others 0 %. Writing `100.0` instead of `100` avoids integer division, which would round down to whole numbers.

```sql
SELECT underwriter,
       COUNT(*) AS decisions,
       SUM(CASE WHEN status = 'REJECTED' THEN 1 ELSE 0 END) AS rejected,
       ROUND(100.0 * SUM(CASE WHEN status = 'REJECTED' THEN 1 ELSE 0 END) / COUNT(*), 1) AS rejected_pct
FROM credit_limits
WHERE decided_on IS NOT NULL
GROUP BY underwriter
ORDER BY rejected_pct DESC;
```

**11.** Averages between 10.6 and 14.9 days. T. Bily has a minimum of -5 days: limit 19 was decided before it was requested.

```sql
SELECT underwriter,
       ROUND(AVG(julianday(decided_on) - julianday(requested_on)), 1) AS avg_days,
       MIN(julianday(decided_on) - julianday(requested_on)) AS min_days,
       MAX(julianday(decided_on) - julianday(requested_on)) AS max_days
FROM credit_limits
WHERE decided_on IS NOT NULL
GROUP BY underwriter;
```

**12.** 5 invoices, from 176 days overdue (INV-2026-01001) down to 97. One of them (INV-2026-06005) also has a due date before its issue date.

```sql
SELECT i.invoice_no, i.amount, i.currency, i.due_date,
       CAST(julianday('2026-09-30') - julianday(i.due_date) AS INTEGER) AS days_overdue
FROM invoices AS i
WHERE i.paid_date IS NULL
  AND julianday('2026-09-30') - julianday(i.due_date) > 90
  AND NOT EXISTS (SELECT 1 FROM claims AS cl WHERE cl.invoice_id = i.id)
ORDER BY days_overdue DESC;
```

**13.** INV-2026-01002 appears twice.

```sql
SELECT invoice_no, COUNT(*) AS occurrences
FROM invoices
GROUP BY invoice_no
HAVING COUNT(*) > 1;
```

**14.** Claim 7: status PAID, indemnity 15,570, payments 0. `COALESCE(x, 0)` replaces NULL with 0, so claims without any payment are caught.

```sql
SELECT cl.id, cl.status, cl.indemnity_amount,
       COALESCE(SUM(p.amount), 0) AS paid_total
FROM claims AS cl
LEFT JOIN payments AS p ON p.claim_id = cl.id
WHERE cl.status = 'PAID'
GROUP BY cl.id, cl.status, cl.indemnity_amount
HAVING COALESCE(SUM(p.amount), 0) <> cl.indemnity_amount;
```

**15.** 11 rows. Brazil has the highest share (153,400 claimed of 460,400 invoiced, 33.3 %), then Kazakhstan 26.2 % and Slovakia 24.6 %. Buyers without a country appear as "(missing country)".

```sql
WITH invoiced AS (
  SELECT COALESCE(b.country_code, '??') AS country_code, SUM(i.amount) AS invoiced_eur
  FROM invoices i
  JOIN buyers b ON b.id = i.buyer_id
  WHERE i.currency = 'EUR'
  GROUP BY COALESCE(b.country_code, '??')
),
claimed AS (
  SELECT COALESCE(b.country_code, '??') AS country_code, SUM(cl.claimed_amount) AS claimed_eur
  FROM claims cl
  JOIN invoices i ON i.id = cl.invoice_id
  JOIN buyers b   ON b.id = i.buyer_id
  WHERE i.currency = 'EUR'
  GROUP BY COALESCE(b.country_code, '??')
)
SELECT COALESCE(co.name, '(missing country)') AS country,
       inv.invoiced_eur,
       COALESCE(cl.claimed_eur, 0) AS claimed_eur,
       ROUND(100.0 * COALESCE(cl.claimed_eur, 0) / inv.invoiced_eur, 1) AS claimed_pct
FROM invoiced inv
LEFT JOIN claimed cl   ON cl.country_code = inv.country_code
LEFT JOIN countries co ON co.code = inv.country_code
ORDER BY claimed_pct DESC;
```

## Key terms
- **SQL** — Structured Query Language, the standard language for querying and changing data in relational databases.
- **Query** — a SQL statement that asks the database for data, usually starting with SELECT.
- **WHERE** — the clause that filters rows before grouping.
- **NULL** — a missing value; tested with IS NULL, never with = NULL.
- **Aggregate function** — a function that summarizes many rows into one value: COUNT, SUM, AVG, MIN, MAX.
- **GROUP BY** — the clause that makes one result row per group so aggregates are calculated per group.
- **HAVING** — the clause that filters groups after aggregation.
- **Alias** — a temporary name for a column or table in a query (AS).
- **INNER JOIN** — a join that returns only rows with a match in both tables.
- **LEFT JOIN** — a join that returns all rows from the left table, with NULLs where the right table has no match.
- **CASE WHEN** — an if/else expression that returns a value based on conditions.
- **Subquery** — a query nested inside another query.
- **EXISTS** — a condition that is true when a subquery returns at least one row.
- **CTE (WITH)** — a named subquery defined at the start of a query to make it readable.
- **Window function** — a function that calculates across related rows without collapsing them, e.g. ROW_NUMBER.
- **COALESCE** — a function that returns the first non-NULL value from its arguments.
- **DML** — data manipulation language: INSERT, UPDATE, DELETE, the statements that change data.

## Hands-on
:::exercise id="m10-e1" title="SQL tasks 1–5: basics" min="30" tool="SQL playground (sql.html)"
**Goal:** get comfortable with SELECT, WHERE, ORDER BY and GROUP BY on the ExportShield data.

Open the SQL playground (`sql.html`), or load `data/sql/exportshield.sql` into [SQLite Online](https://sqliteonline.com/). Write one query per task and note the number of rows.

1. List all buyers based in Germany (country code `DE`) with their sector.
2. How many customers are there in each segment? Sort from the largest group.
3. List invoices with an amount over 100,000, largest first. Show the currency. What is wrong with comparing these amounts?
4. Which credit limit requests are still waiting for a decision? Show the oldest first.
5. Find customers whose name contains "Glass". What do you notice?

**Done when:** you have five working queries and a one-sentence note for tasks 3 and 5. Solutions are at the end of the Deep dive.
:::

:::exercise id="m10-e2" title="SQL tasks 6–10: joins and aggregates" min="45" tool="SQL playground (sql.html)"
**Goal:** combine tables and summarize data.

6. Total approved amount of all APPROVED and REDUCED credit limits, per currency.
7. Number of credit limit decisions per underwriter (exclude open requests).
8. Buyers in countries with risk category 5 or higher: buyer name, country name, risk category, highest risk first.
9. Every buyer with the number of credit limits it has, including buyers with none. (Hint: LEFT JOIN, and think about what you count.)
10. Rejection rate per underwriter in percent, rounded to one decimal place. (Hint: CASE WHEN inside SUM.)

**Done when:** all five queries run, task 9 returns 25 rows, and you can explain in one sentence why task 9 needs a LEFT JOIN.
:::

:::exercise id="m10-e3" title="SQL tasks 11–15: analyst questions" min="60" tool="SQL playground (sql.html)"
**Goal:** use SQL the way an analyst does: dates, missing data, data quality and a business ratio.

11. Average, minimum and maximum number of days between request and decision of a credit limit, per underwriter. Which value cannot be right, and which record causes it?
12. Unpaid invoices more than 90 days past due on 2026-09-30 **without** any claim. Why might this list interest the claims department?
13. Find duplicate invoice numbers.
14. Find claims with status PAID where the sum of payments differs from the indemnity amount, including claims with no payments at all.
15. For EUR invoices only: per buyer country, the total invoiced amount, the total claimed amount and the claimed share in percent. Buyers without a country must not disappear. (Hint: two CTEs, then LEFT JOIN.)

**Done when:** all five queries run and for each data problem you found you have written one line: what is wrong, how many rows, and the likely business impact.
:::

:::exercise id="m10-e4" title="SQLBolt lessons 1–12" min="90" tool="SQLBolt"
**Goal:** practice the core syntax with instant feedback, independent of the ExportShield data.

1. Go to [SQLBolt](https://sqlbolt.com/) and complete lessons 1 to 12. They cover SELECT, filtering with constraints, sorting, joins including outer joins, NULLs, expressions, aggregates and the order in which a query is executed.
2. After each lesson, write one query of the same type against the ExportShield data in the SQL playground and note it in your own cheat sheet.
3. After lesson 12, write down in your own words the order in which the database processes a query (FROM and JOIN, WHERE, GROUP BY, HAVING, SELECT, ORDER BY, LIMIT) and why that explains that you cannot use a SELECT alias in WHERE.

**Done when:** all twelve lessons are completed and your cheat sheet has at least twelve ExportShield queries, one per lesson.
:::

## Self-check
:::q
What is the difference between WHERE and HAVING?
---
WHERE filters individual rows before they are grouped, so it cannot use aggregates like COUNT. HAVING filters the groups after GROUP BY and aggregation, so it can use them, for example `HAVING COUNT(*) >= 3`. You can use both in one query: WHERE removes paid invoices, then HAVING keeps only buyers with three or more unpaid ones.
:::

:::q
Why does `WHERE paid_date = NULL` return no rows, and what should you write instead?
---
NULL means unknown, and comparing anything with an unknown value gives "unknown", not true. Rows are returned only when the condition is true, so no rows qualify. Write `WHERE paid_date IS NULL` (or `IS NOT NULL` for the opposite).
:::

:::q
You join `buyers` to `countries` with INNER JOIN and get 24 rows, but there are 25 buyers. What happened, and how do you fix it?
---
One buyer has no country code, so no row in `countries` matches and INNER JOIN drops it. Use LEFT JOIN with `buyers` on the left: all 25 buyers are kept, and the country columns are NULL for the buyer without a match. Then decide whether the missing country is a data quality issue to report.
:::

:::q
After joining invoices to credit limits, the sum of invoice amounts is higher than the plain sum over invoices. Why?
---
The join multiplied rows: when one invoice matches two credit limit rows (for example an existing limit and a new open request for the same policy and buyer), the invoice appears twice and its amount is counted twice. Check row counts before and after joins and make sure the join keys identify at most one row on the side you do not want to multiply.
:::

:::q
What is the difference between `COUNT(*)` and `COUNT(paid_date)`?
---
`COUNT(*)` counts all rows. `COUNT(paid_date)` counts only rows where `paid_date` is not NULL. In the invoices table that gives 78 and 47: 47 invoices are paid. The difference is a quick completeness or status check.
:::

:::q
A colleague asks for "the total value of overdue invoices". What questions do you ask before writing the query?
---
As of which date, and are invoices paid late but now paid included? Overdue by any number of days, or beyond a threshold? Which currency, and if several, should amounts be converted at which rate or reported separately? Include invoices that already have a claim? Under active policies only? Writing these assumptions next to the number avoids two people getting different totals.
:::

:::q
Why do business analysts rarely run UPDATE or DELETE in production databases?
---
Direct changes bypass the application's business logic, history and notifications, so data can end up inconsistent. They also bypass audit and approval, which regulated companies such as insurers and banks must have. Data fixes therefore go through approved, tested scripts run by the responsible team. The analyst specifies what should change and verifies the result with SELECT.
:::

:::q
How can you use SQL to verify an acceptance criterion?
---
Rewrite the criterion as a query that finds violations, so that the expected result is zero rows. For "an approved limit is never higher than the requested amount", select limits where `approved_amount > requested_amount`. Run it after the test and after each release; any row returned is a defect with concrete evidence.
:::

## Interview corner
:::interview
What is the difference between INNER JOIN and LEFT JOIN? Give an example.
---
- INNER JOIN returns only rows that match in both tables.
- LEFT JOIN returns all rows from the left table; columns from the right table are NULL where nothing matches.
- Example: all buyers with their country; a buyer without a country disappears with INNER JOIN but stays with LEFT JOIN.
- LEFT JOIN plus `WHERE right.id IS NULL` finds records without a related record (buyers with no credit limit).

Typical mistake: explaining joins with Venn diagrams only, without saying what happens to unmatched rows and why NULLs appear.
:::

:::interview
How have you used SQL in your work or projects?
---
- A concrete question you answered with numbers, e.g. how long credit limit decisions take.
- Verifying test results: acceptance criteria rewritten as queries that must return zero rows.
- Data quality checks: duplicates, missing values, contradictory dates, with counts and impact.
- Sizing a problem for a business case.
- What you would not do: change production data directly.

Typical mistake: saying "I know SQL" without a single example of a question it helped answer.
:::

:::interview
Write a query that shows the number of claims and total claimed amount per status.
---
- `SELECT status, COUNT(*) AS claims, SUM(claimed_amount) AS claimed FROM claims GROUP BY status ORDER BY claims DESC;`
- Explain each clause briefly while writing.
- Mention the currency issue: group by currency as well, or filter, before adding amounts.
- Mention checking the result: total of counts equals `SELECT COUNT(*) FROM claims`.

Typical mistake: selecting a column that is neither in GROUP BY nor aggregated.
:::

:::interview
How do you check data quality with SQL?
---
- Completeness: `IS NULL` counts and `COUNT(*)` versus `COUNT(column)`.
- Validity: formats and ranges, e.g. `length(ico) <> 8`, due date before issue date.
- Consistency: contradictions across fields and tables, e.g. PAID claims without payments (LEFT JOIN).
- Uniqueness: `GROUP BY ... HAVING COUNT(*) > 1`.
- Report count, examples, impact and root cause, and propose a preventive validation.

Typical mistake: listing problems without quantifying them or saying why they matter to the business.
:::
