---
id: 10
slug: sql
title: SQL pro business analytiky
phase: C
priority: P1
quick_min: 15
deep_min: 90
job_ad: "základní znalost SQL"
---

## Why this matters
Inzerát chce základní SQL. Analytik ho používá každý týden: odpoví na business otázku, aniž by čekal na report, ověří, že dodaná změna funguje, najde špatná data a vyčíslí problém dřív, než někdo zaplatí opravu. Nemusíš navrhovat databáze ani ladit výkon. Potřebuješ jistě číst data pomocí `SELECT`, spojovat tabulky přes joiny a shrnovat pomocí `GROUP BY`. Všechny příklady tady běží nad datovou sadou ExportShield v SQL playgroundu na webu.

## Quick version
**SQL** (Structured Query Language, strukturovaný dotazovací jazyk) je standardní jazyk pro práci s relačními databázemi. Dotaz popisuje, *co* chceš; databáze sama vymyslí, *jak* to získat.

**Základní tvar dotazu:**

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

Ke čtení dat z tabulky stačí `SELECT` a `FROM`; ostatní klauzule jsou volitelné. Ty, které použiješ, musí být napsané v tomto pořadí.

**Co která část dělá:**

- `SELECT name, city` vybírá sloupce. `SELECT *` vezme všechny (dobré na prozkoumání, ne do reportu).
- `WHERE` filtruje řádky: `=`, `<>` (nerovná se), `>`, `<`, `IN ('A','B')`, `BETWEEN x AND y`, `LIKE '%text%'` (vzor), `IS NULL` (prázdné).
- `ORDER BY amount DESC` řadí; `LIMIT 5` ponechá prvních pět řádků.
- `DISTINCT` odstraní z výsledku duplicitní řádky.
- **Aggregate functions** (agregační funkce) shrnou mnoho řádků do jedné hodnoty: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`.
- `GROUP BY status` vytvoří jeden řádek výsledku za každý status; agregace se pak počítají pro každou skupinu zvlášť. `HAVING` tyto skupiny filtruje.
- **Joins** (spojení) kombinují tabulky přes klíče. `INNER JOIN` ponechá jen řádky, které mají shodu na obou stranách. `LEFT JOIN` ponechá každý řádek z levé tabulky, a když vpravo shoda není, doplní pravou stranu hodnotou `NULL`.
- `CASE WHEN ... THEN ... ELSE ... END` je podmínka if/else uvnitř dotazu, hodí se na kategorie.

**NULL** znamená „žádná hodnota“. Nikdy se ničemu nerovná, ani jinému NULL, takže musíš psát `paid_date IS NULL`, ne `paid_date = NULL`.

**K čemu analytik SQL používá:**

1. **Odpovídá na business otázky**: „Kolik škod jsme loni vyplatili a v jaké výši?“
2. **Ověřuje výsledky testů**: po vydání nové verze (release) zkontroluje, že databáze obsahuje to, co říká požadavek.
3. **Kontroluje kvalitu dat**: hledá chybějící, neplatná, duplicitní nebo protichůdná data.
4. **Vyčísluje problém**: „18 z 39 rozhodnutí o úvěrovém limitu trvalo déle než 14 dní“ je silnější business case než „rozhodování je pomalé“.

**Čtení versus zápis.** `INSERT`, `UPDATE` a `DELETE` data mění. Analytik je čte ve specifikacích a migračních skriptech, ale v produkci je spouští zřídka: změny tam jdou přes aplikace, schválené skripty a change management, s auditní stopou.

**Kde si to vyzkoušet:** SQL playground na webu (`sql.html`) má data ExportShield předem nahraná. Případně vlož `data/sql/exportshield.sql` do [SQLite Online](https://sqliteonline.com/). Pro základy s vedením má [SQLBolt](https://sqlbolt.com/) krátké interaktivní lekce.

**Na pohovor jednou větou:** „Píšu SELECT dotazy s joiny, filtry a GROUP BY, abych odpověděla na otázky, ověřila výsledky testů a zkontrolovala kvalitu dat. Znám rozdíl mezi INNER a LEFT JOIN a vím, jak se chovají NULL hodnoty.“

## Deep dive

### Příprava a datová sada [P1]
Otevři SQL playground (`sql.html`). Tabulky ExportShield jsou nahrané: `countries`, `customers`, `buyers`, `policies`, `credit_limits`, `invoices`, `claims`, `payments`. Pokud chceš raději [SQLite Online](https://sqliteonline.com/), vlož do editoru celý obsah `data/sql/exportshield.sql` a jednou ho spusť; vytvoří a naplní tabulky.

Dvě věci o datech, které pro příklady potřebuješ:

- **„Dnes“ je 2026-09-30.** Data jsou snímek (snapshot). Dotazy používají toto datum jako pevnou hodnotu místo aktuálního data, aby výsledky zůstaly stejné.
- **Částky jsou v měně daného řádku** (EUR nebo USD). Sečíst EUR a USD dohromady dává nesmyslné číslo, proto mnoho příkladů filtruje nebo seskupuje podle měny.

Datový model vysvětluje modul o datech a databázích. Zkráceně: zákazník (exportér) má pojistné smlouvy (policies); v rámci smlouvy žádá o úvěrové limity (credit limits) na odběratele (buyers); odběratelům posílá faktury; nezaplacená faktura může vést ke škodě (claim); škoda se vyrovná platbami (payments).

Klíčová slova SQL nerozlišují velká a malá písmena (`select` funguje jako `SELECT`); psát je velkými písmeny je konvence kvůli čitelnosti. Textové hodnoty v uvozovkách porovnává SQLite (playground) i PostgreSQL s rozlišením velikosti písmen: `'Approved'` neodpovídá `'APPROVED'`. SQL Server a MySQL obvykle porovnávají text bez ohledu na velikost písmen, záleží na nastavení databáze (collation), takže si to ověř, než na tom postavíš dotaz.

### SELECT, FROM a WHERE [P1]
Nejjednodušší dotaz vrátí celou tabulku:

```sql
SELECT * FROM countries;
```

Výsledek: 12 řádků, sloupce `code`, `name`, `risk_category`.

Vyber sloupce a vyfiltruj řádky:

```sql
SELECT code, name, risk_category
FROM countries
WHERE risk_category >= 5;
```

Výsledek: 5 řádků: Brazil, Turkey, Kazakhstan (5), Egypt (6), Ukraine (7).

Porovnávací operátory: `=`, `<>` (nerovná se; ve většině databází funguje i `!=`), `<`, `<=`, `>`, `>=`. Podmínky spojuješ pomocí `AND`, `OR` a `NOT`; když mícháš `AND` a `OR`, použij závorky, jinak se `AND` vyhodnotí dřív a výsledek tě překvapí.

```sql
SELECT id, name, segment
FROM customers
WHERE segment <> 'CORPORATE';
```

Výsledek: 10 zákazníků (SME a MICRO).

**IN** testuje hodnotu proti seznamu:

```sql
SELECT id, status, requested_amount, approved_amount
FROM credit_limits
WHERE status IN ('REDUCED', 'REJECTED');
```

Výsledek: 18 řádků (14 snížených, 4 zamítnuté). Podívej se na limit s id 6: REJECTED, ale `approved_amount` je 75 000. To je záměrně vložená chyba v kvalitě dat.

**BETWEEN** zahrnuje obě krajní hodnoty. Data uložená jako ISO text (`YYYY-MM-DD`) se porovnávají správně:

```sql
SELECT invoice_no, amount, issue_date
FROM invoices
WHERE issue_date BETWEEN '2026-01-01' AND '2026-03-31';
```

Výsledek: 19 faktur vystavených v 1. čtvrtletí 2026.

**LIKE** hledá podle vzoru: `%` zastupuje libovolný počet znaků, `_` právě jeden znak.

```sql
SELECT name, city
FROM customers
WHERE name LIKE '%a.s.';
```

Výsledek: 5 akciových společností (názvy končící na „a.s.“). V SQLite `LIKE` nerozlišuje velká a malá písmena u anglické abecedy; jiné databáze se liší.

**IS NULL** najde chybějící hodnoty:

```sql
SELECT invoice_no, amount, currency, due_date
FROM invoices
WHERE paid_date IS NULL;
```

Výsledek: 31 nezaplacených faktur, některé ještě nejsou splatné. `WHERE paid_date = NULL` by vrátilo 0 řádků, protože porovnání s NULL nikdy není pravdivé.

### ORDER BY, LIMIT, DISTINCT a aliasy [P1]

```sql
SELECT invoice_no, amount, currency
FROM invoices
ORDER BY amount DESC
LIMIT 5;
```

Výsledek: pět největších faktur, první je INV-2025-07002 (157 900 EUR). Všimni si, že druhá je v USD; řazení podle částky napříč měnami stačí na rychlý pohled, ne do reportu.

Výchozí je `ASC` (vzestupně). `LIMIT` je syntaxe SQLite, PostgreSQL a MySQL; SQL Server používá `SELECT TOP 5`, Oracle `FETCH FIRST 5 ROWS ONLY`.

`DISTINCT` odstraní duplicity:

```sql
SELECT DISTINCT sector
FROM buyers
ORDER BY sector;
```

Výsledek: 10 odvětví, od Agriculture po Transport.

**Aliasy** přejmenují sloupce (`AS customer_name`) nebo dají tabulce krátký název (`customers AS c`). U joinů jsou aliasy tabulek nezbytné.

```sql
SELECT c.name AS customer_name,
       c.segment AS customer_segment
FROM customers AS c
WHERE c.city = 'Praha';
```

Výsledek: 1 řádek, Praha Rail Parts a.s.

### Agregace, GROUP BY a HAVING [P1]
Agregační funkce udělají z mnoha řádků jednu hodnotu.

```sql
SELECT COUNT(*)          AS all_invoices,
       COUNT(paid_date)  AS paid_invoices,
       MIN(issue_date)   AS first_issued,
       MAX(issue_date)   AS last_issued
FROM invoices;
```

Výsledek: 78 faktur, 47 zaplacených, první vystavena 2024-04-22, poslední 2026-09-17. `COUNT(*)` počítá řádky; `COUNT(column)` počítá jen hodnoty, které nejsou NULL. Tento rozdíl je rychlý způsob, jak změřit úplnost dat.

`GROUP BY` vytvoří jeden řádek za každou skupinu:

```sql
SELECT currency,
       COUNT(*)              AS invoices,
       SUM(amount)           AS total_amount,
       ROUND(AVG(amount), 0) AS avg_amount
FROM invoices
GROUP BY currency;
```

Výsledek: EUR 69 faktur, celkem 2 960 400; USD 9 faktur, 443 300.

```sql
SELECT status, COUNT(*) AS claims, SUM(claimed_amount) AS claimed
FROM claims
GROUP BY status
ORDER BY claims DESC;
```

Výsledek: PAID 7, IN_REVIEW 3, pak NOTIFIED a APPROVED (po 2) a REJECTED 1. (Součet `claimed` míchá měny, protože jedna zamítnutá a jedna nahlášená škoda jsou v USD; další části ukazují, jak to řešit.)

Pravidlo pro `GROUP BY`: každý sloupec v `SELECT` musí být buď v `GROUP BY`, nebo uvnitř agregační funkce. SQLite je benevolentní a dovolí pravidlo porušit; vrátí hodnotu z libovolného řádku skupiny. Většina ostatních databází (PostgreSQL, SQL Server, Oracle, MySQL ve výchozím režimu) skončí chybou.

`WHERE` filtruje řádky *před* seskupením. `HAVING` filtruje skupiny *po* agregaci:

```sql
SELECT buyer_id, COUNT(*) AS unpaid_invoices
FROM invoices
WHERE paid_date IS NULL
GROUP BY buyer_id
HAVING COUNT(*) >= 3;
```

Výsledek: 4 odběratelé (ID 4, 5, 8, 19) se třemi a více nezaplacenými fakturami.

### INNER JOIN [P1]
Data o jedné business události jsou rozložená do více tabulek. Join je znovu poskládá tím, že páruje klíče.

```sql
SELECT i.invoice_no, i.amount, i.currency, b.name AS buyer
FROM invoices AS i
INNER JOIN buyers AS b ON b.id = i.buyer_id
WHERE i.paid_date IS NULL
ORDER BY i.amount DESC;
```

Výsledek: 31 nezaplacených faktur, teď i se jmény odběratelů; největší je 119 100 USD od Great Lakes Industrial Supply Inc.

Jak to číst: ke každé faktuře najdi odběratele, jehož `id` se rovná `buyer_id` faktury. `INNER JOIN` (nebo jen `JOIN`) ponechá jen dvojice, které se spárovaly. Faktura s neexistujícím odběratelem by tiše zmizela.

**Past: joiny mohou násobit řádky.** Když má pravá tabulka dva odpovídající řádky, levý řádek se objeví dvakrát:

```sql
SELECT COUNT(*) AS rows_after_join
FROM invoices AS i
JOIN credit_limits AS l
  ON l.policy_id = i.policy_id AND l.buyer_id = i.buyer_id;
```

Výsledek: 80, přestože faktur je jen 78. Smlouva 18 má pro odběratele 2 dva řádky úvěrového limitu (snížený limit a novou otevřenou žádost), takže každá ze dvou faktur tohoto odběratele se započítá dvakrát. Když sčítáš částky, vždy porovnej počet řádků před joinem a po něm.

### LEFT JOIN a proč se objevují NULL [P1]
`LEFT JOIN` ponechá **každý řádek z levé tabulky** (té za `FROM`). Kde má pravá tabulka shodu, doplní se její sloupce. Kde shoda není, jsou sloupce pravé strany `NULL`.

Porovnej tyto dva dotazy:

```sql
SELECT b.id, b.name, b.country_code, co.name AS country, co.risk_category
FROM buyers AS b
INNER JOIN countries AS co ON co.code = b.country_code;
```

Výsledek: 24 řádků.

```sql
SELECT b.id, b.name, b.country_code, co.name AS country, co.risk_category
FROM buyers AS b
LEFT JOIN countries AS co ON co.code = b.country_code
ORDER BY co.risk_category DESC;
```

Výsledek: 25 řádků. Odběratel 24, Baltic Timber Traders, nemá kód země, takže není s čím párovat. `INNER JOIN` ho bez varování vynechal; `LEFT JOIN` ho ponechá s `NULL` ve sloupcích `country` a `risk_category`. V reportu rizik je tiché vypadnutí odběratele skutečný problém.

LEFT JOIN také odpoví na otázku „které záznamy **nemají** žádný související řádek?“:

```sql
SELECT b.id, b.name
FROM buyers AS b
LEFT JOIN credit_limits AS l ON l.buyer_id = b.id
WHERE l.id IS NULL;
```

Výsledek: 1 odběratel, Deccan Engineering Pvt Ltd, bez jakéhokoli úvěrového limitu.

A ukáže škody s platbami i bez nich:

```sql
SELECT cl.id AS claim_id, cl.status, cl.indemnity_amount, p.id AS payment_id, p.amount
FROM claims AS cl
LEFT JOIN payments AS p ON p.claim_id = cl.id
ORDER BY cl.id;
```

Výsledek: 17 řádků pro 15 škod. Škody 5 a 6 jsou tam dvakrát (vyplacené ve dvou splátkách). Škoda 7 má status PAID, ale sloupce platby jsou `NULL`: nekonzistence v datech.

Praktické pravidlo: když otázka zní „všechna X, a k nim Y, pokud existuje“, použij `LEFT JOIN` s X vlevo. Existují i `RIGHT JOIN` a `FULL OUTER JOIN`; right join vždy přepíšeš na left join prohozením tabulek.

### Spojení více tabulek [P1]
Postupuj krok za krokem po cizích klíčích (foreign keys). Škoda → faktura → smlouva → zákazník a faktura → odběratel → země:

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

Výsledek: 15 řádků, jeden za každou škodu, čitelné i pro business uživatele. Škoda 1: Moravia AgroTech a.s. proti Parana Agro Comercial Ltda (Brazílie), 24 200 EUR, PAID. Poslední join je záměrně LEFT JOIN, aby odběratel bez země nevypadl.

Tip: dlouhé joiny stav po jedné tabulce a po každém kroku zkontroluj počet řádků.

### CASE WHEN [P1]
`CASE` vytvoří hodnotu podle podmínek, které se vyhodnocují shora dolů; vyhrává první pravdivá větev.

```sql
SELECT code, name, risk_category,
       CASE
         WHEN risk_category <= 2 THEN 'Low'
         WHEN risk_category <= 4 THEN 'Medium'
         ELSE 'High'
       END AS risk_band
FROM countries;
```

V kombinaci s `GROUP BY` je z CASE rychlá segmentace:

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

Výsledek: High 14 limitů (3,39 milionu požadováno, 1,43 milionu schváleno), Low 19 (3,76 / 3,40 milionu), Medium 5. Underwriteři v rizikových zemích schvalují mnohem menší podíl, jak se dá čekat. Pečlivý analytik zmíní dvě výhrady: částky míchají EUR a USD a jedno rozhodnutí o limitu chybí (rozhodnutí je 39, pásma dávají dohromady 38), protože odběratele bez země vyřadil INNER JOIN.

Častý vzor je počítání pomocí CASE: `SUM(CASE WHEN status = 'REJECTED' THEN 1 ELSE 0 END)` spočítá zamítnuté řádky uvnitř skupiny.

### Datumy v SQLite [P1]
SQLite nemá samostatný datový typ pro datum; data se ukládají jako text `YYYY-MM-DD` a pracuje se s nimi pomocí funkcí:

- `date('2026-09-30', '-90 days')` vrátí `2026-07-02`.
- `strftime('%Y-%m', issue_date)` vrátí rok a měsíc, např. `2026-03`.
- `julianday(date)` převede datum na pořadové číslo dne, takže rozdíl dvou takových čísel je počet dní mezi nimi.
- `date('now')` je dnešní datum; my místo něj používáme pevné datum snímku.

Počet dní po splatnosti u nezaplacených faktur:

```sql
SELECT invoice_no, due_date,
       CAST(julianday('2026-09-30') - julianday(due_date) AS INTEGER) AS days_overdue
FROM invoices
WHERE paid_date IS NULL
  AND due_date < '2026-09-30'
ORDER BY days_overdue DESC;
```

Výsledek: 23 faktur po splatnosti, nejstarší 798 dní po splatnosti (INV-2024-02003).

Faktury po měsících:

```sql
SELECT strftime('%Y-%m', issue_date) AS month, COUNT(*) AS invoices
FROM invoices
WHERE issue_date >= '2026-01-01'
GROUP BY month
ORDER BY month;
```

Výsledek: 9 měsíců; nejvíc faktur má leden 2026 (10).

**Jiné databáze se liší.** SQL Server používá `DATEDIFF(day, a, b)` a `GETDATE()`, Oracle data přímo odečítá a používá `SYSDATE`, PostgreSQL používá `CURRENT_DATE` a `date_part`. Principy jsou stejné; názvy funkcí si dohledej pro databázi, se kterou pracuješ.

### Poddotazy a EXISTS [P2]
**Subquery** (poddotaz) je dotaz uvnitř jiného dotazu, v závorkách.

Faktury nad průměrnou EUR fakturou:

```sql
SELECT invoice_no, amount, currency
FROM invoices
WHERE currency = 'EUR'
  AND amount > (SELECT AVG(amount) FROM invoices WHERE currency = 'EUR')
ORDER BY amount DESC;
```

Výsledek: 22 faktur (průměr EUR je zhruba 42 900).

`EXISTS` ověřuje, zda související řádek existuje. Zákazníci s alespoň jednou škodou:

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

Výsledek: 7 zákazníků. `NOT EXISTS` dá opak. `NOT IN` s poddotazem funguje také, ale nevrátí nic, pokud poddotaz obsahuje NULL, takže `NOT EXISTS` je bezpečnější zvyk:

```sql
SELECT name FROM buyers
WHERE id NOT IN (SELECT buyer_id FROM invoices);
```

Výsledek: 3 odběratelé, kteří nikdy nedostali fakturu.

### Common table expressions (WITH) [P2]
**CTE** (common table expression) dá poddotazu jméno na začátku dotazu, takže se složitý dotaz čte po krocích.

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

Výsledek: 11 řádků; Polabi Chemicals a.s. má největší částku po splatnosti v EUR (3 faktury, 139 100). Seskupení i podle měny drží EUR a USD odděleně.

### Window functions (ochutnávka) [P3]
**Window functions** (okenní funkce) počítají přes související řádky, *aniž* by je slučovaly do jednoho řádku. `ROW_NUMBER()` očísluje řádky uvnitř skupiny:

```sql
SELECT b.name AS buyer, i.invoice_no, i.amount,
       ROW_NUMBER() OVER (PARTITION BY i.buyer_id ORDER BY i.amount DESC) AS rank_in_buyer
FROM invoices i
JOIN buyers b ON b.id = i.buyer_id
WHERE i.currency = 'EUR'
ORDER BY b.name, rank_in_buyer
LIMIT 8;
```

Výsledek: faktury každého odběratele očíslované od největší; Alpenmarkt Vertrieb GmbH jich má pět. Další užitečné: `SUM(...) OVER (ORDER BY date)` pro průběžné součty, `LAG()` pro porovnání s předchozím řádkem. Podporuje je SQLite od verze 3.25 a všechny hlavní databáze.

### INSERT, UPDATE, DELETE: číst, nespouštět [P2]
Tyto příkazy mění data. Měla bys jim rozumět, když je uvidíš v migračním skriptu, v přípravě testovacích dat nebo v opravě od dodavatele:

```sql
INSERT INTO countries (code, name, risk_category)
VALUES ('MX', 'Mexico', 4);

UPDATE credit_limits
SET approved_amount = 0
WHERE id = 6;

DELETE FROM payments
WHERE id = 8;
```

Nejnebezpečnější chyba je `UPDATE` nebo `DELETE` bez `WHERE`: změní každý řádek v tabulce.

Proč analytik v produkci data skoro nezapisuje:

- **Audit a odpovědnost**: v regulované pojišťovně musí být každá změna smlouvy nebo škody dohledatelná k osobě, důvodu a schválení. Aplikace to zaznamená; ruční `UPDATE` to obejde.
- **Business logika**: aplikace zároveň zapisuje historii, posílá notifikace a aktualizuje související záznamy. Přímá změna to všechno přeskočí a data zůstanou nekonzistentní.
- **Segregation of duties** (oddělení povinností): kdo změnu specifikuje, neměl by ji sám bez kontroly provádět.
- **Change management** (řízení změn): opravy dat jdou přes schválený skript, nejdřív otestovaný, který spustí dodavatel nebo provozní tým.

V testovacím prostředí nebo ve vlastní kopii dat (jako SQL playground) je experimentování v pořádku. Když data v playgroundu rozbiješ, načti je znovu.

### Jak analytik používá SQL v práci [P1]
**1. Odpovědi na business otázky.** „Kolik rozhodnutí o úvěrových limitech jsme udělali a jak dlouho trvala?“

```sql
SELECT COUNT(*) AS decisions,
       ROUND(AVG(julianday(decided_on) - julianday(requested_on)), 1) AS avg_days,
       SUM(CASE WHEN julianday(decided_on) - julianday(requested_on) > 14 THEN 1 ELSE 0 END) AS over_14_days
FROM credit_limits
WHERE decided_on IS NOT NULL;
```

Výsledek: 39 rozhodnutí, v průměru 12,5 dne, 18 trvalo déle než 14 dní.

**2. Vyčíslení problému pro business case.** Poslední výsledek je velikost problému: skoro polovina rozhodnutí trvá déle než dva týdny. Pokud navrhovaná integrace s ARES ušetří na žádosti den, máš základ pro výpočet přínosu. Vždy uveď období, zdroj a výhrady (tady: jeden záznam má zápornou délku, chyba v datech).

**3. Ověření výsledků testů.** Převeď akceptační kritérium na dotaz, který musí vrátit nula řádků. Kritérium: „Limit APPROVED nebo REDUCED má vždy schválenou částku větší než nula a ne vyšší než požadovanou částku.“

```sql
SELECT id, status, requested_amount, approved_amount
FROM credit_limits
WHERE status IN ('APPROVED', 'REDUCED')
  AND (approved_amount <= 0 OR approved_amount > requested_amount);
```

Výsledek: 0 řádků, takže v těchto datech kritérium platí. Takový dotaz můžeš pustit znovu po každém releasu.

**4. Kontrola kvality dat.** Hledej řádky, které porušují pravidla: chybějící hodnoty, neplatné formáty, rozpory, duplicity. Cvičení níže obsahují několik takových kontrol. Zjištění hlas s počty, příklady a dopadem, ne jen „data jsou špatná“.

Zvyky, které tě ochrání před problémy: začni `SELECT * ... LIMIT 10`, abys data viděla; počítej řádky před každým joinem a po něm; nikdy nesčítej různé měny; ke každému číslu, které někomu posíláš, napiš datum snímku a použité filtry.

### Řešení
:::tip
Nejdřív zkus cvičení v sekci Hands-on. Porovnávej, až když máš vlastní dotaz; často existuje víc správných řešení. Všechny výsledky níže platí pro datovou sadu ExportShield s datem snímku 2026-09-30.
:::

**1.** 3 řádky: Rheinwerk Handels, Nordhafen Logistik, Bavaria Bau Supplies.

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

**3.** 11 faktur; dvě z nich jsou v USD, takže „nad 100 000“ znamená různé hodnoty.

```sql
SELECT invoice_no, amount, currency
FROM invoices
WHERE amount > 100000
ORDER BY amount DESC;
```

**4.** 4 otevřené žádosti, ID 40 až 43, nejstarší z 2026-09-08.

```sql
SELECT id, policy_id, buyer_id, requested_amount, currency, requested_on
FROM credit_limits
WHERE status = 'REQUESTED'
ORDER BY requested_on;
```

**5.** 2 řádky se stejným IČO: stejný exportér registrovaný dvakrát (problém jedinečnosti).

```sql
SELECT id, name, ico
FROM customers
WHERE name LIKE '%Glass%';
```

**6.** EUR 5 004 000 a USD 980 000.

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

**8.** 8 odběratelů; první Dnipro Agro Holding (Ukrajina, 7). Odběratel bez země v seznamu není, a i to je zjištění.

```sql
SELECT b.name AS buyer, co.name AS country, co.risk_category
FROM buyers AS b
JOIN countries AS co ON co.code = b.country_code
WHERE co.risk_category >= 5
ORDER BY co.risk_category DESC, b.name;
```

**9.** 25 řádků; Steppe Rail Service má 4 limity, Deccan Engineering 0. Použij `COUNT(l.id)`, ne `COUNT(*)`, jinak odběratelé bez limitu ukážou 1.

```sql
SELECT b.name AS buyer, COUNT(l.id) AS credit_limits
FROM buyers AS b
LEFT JOIN credit_limits AS l ON l.buyer_id = b.id
GROUP BY b.id, b.name
ORDER BY credit_limits DESC, b.name;
```

**10.** E. Kralova 25,0 % (3 z 12), J. Marek 10,0 %, ostatní 0 %. Zápis `100.0` místo `100` zabrání celočíselnému dělení, které by zaokrouhlilo dolů na celá čísla.

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

**11.** Průměry mezi 10,6 a 14,9 dne. T. Bily má minimum -5 dní: limit 19 byl rozhodnut dřív, než o něj někdo požádal.

```sql
SELECT underwriter,
       ROUND(AVG(julianday(decided_on) - julianday(requested_on)), 1) AS avg_days,
       MIN(julianday(decided_on) - julianday(requested_on)) AS min_days,
       MAX(julianday(decided_on) - julianday(requested_on)) AS max_days
FROM credit_limits
WHERE decided_on IS NOT NULL
GROUP BY underwriter;
```

**12.** 5 faktur, od 176 dní po splatnosti (INV-2026-01001) až po 97. Jedna z nich (INV-2026-06005) má navíc datum splatnosti před datem vystavení.

```sql
SELECT i.invoice_no, i.amount, i.currency, i.due_date,
       CAST(julianday('2026-09-30') - julianday(i.due_date) AS INTEGER) AS days_overdue
FROM invoices AS i
WHERE i.paid_date IS NULL
  AND julianday('2026-09-30') - julianday(i.due_date) > 90
  AND NOT EXISTS (SELECT 1 FROM claims AS cl WHERE cl.invoice_id = i.id)
ORDER BY days_overdue DESC;
```

**13.** INV-2026-01002 je tam dvakrát.

```sql
SELECT invoice_no, COUNT(*) AS occurrences
FROM invoices
GROUP BY invoice_no
HAVING COUNT(*) > 1;
```

**14.** Škoda 7: status PAID, plnění 15 570, platby 0. `COALESCE(x, 0)` nahradí NULL nulou, takže se zachytí i škody úplně bez plateb.

```sql
SELECT cl.id, cl.status, cl.indemnity_amount,
       COALESCE(SUM(p.amount), 0) AS paid_total
FROM claims AS cl
LEFT JOIN payments AS p ON p.claim_id = cl.id
WHERE cl.status = 'PAID'
GROUP BY cl.id, cl.status, cl.indemnity_amount
HAVING COALESCE(SUM(p.amount), 0) <> cl.indemnity_amount;
```

**15.** 11 řádků. Nejvyšší podíl má Brazílie (153 400 nárokováno z 460 400 fakturováno, 33,3 %), pak Kazachstán 26,2 % a Slovensko 24,6 %. Odběratelé bez země se zobrazí jako „(missing country)“.

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
- **SQL** (strukturovaný dotazovací jazyk) — Structured Query Language, standardní jazyk pro dotazování a změny dat v relačních databázích.
- **Query** (dotaz) — příkaz SQL, který žádá databázi o data, obvykle začíná SELECT.
- **WHERE** — klauzule, která filtruje řádky před seskupením.
- **NULL** — chybějící hodnota; testuje se pomocí IS NULL, nikdy pomocí = NULL.
- **Aggregate function** (agregační funkce) — funkce, která shrne mnoho řádků do jedné hodnoty: COUNT, SUM, AVG, MIN, MAX.
- **GROUP BY** — klauzule, která vytvoří jeden řádek výsledku za skupinu, takže se agregace počítají po skupinách.
- **HAVING** — klauzule, která filtruje skupiny po agregaci.
- **Alias** — dočasný název sloupce nebo tabulky v dotazu (AS).
- **INNER JOIN** (vnitřní spojení) — spojení, které vrátí jen řádky se shodou v obou tabulkách.
- **LEFT JOIN** (levé vnější spojení) — spojení, které vrátí všechny řádky z levé tabulky, s NULL tam, kde pravá tabulka nemá shodu.
- **CASE WHEN** — výraz if/else, který vrací hodnotu podle podmínek.
- **Subquery** (poddotaz) — dotaz vnořený do jiného dotazu.
- **EXISTS** — podmínka, která je pravdivá, když poddotaz vrátí alespoň jeden řádek.
- **CTE (WITH)** — pojmenovaný poddotaz definovaný na začátku dotazu kvůli čitelnosti.
- **Window function** (okenní funkce) — funkce, která počítá přes související řádky, aniž by je sloučila, např. ROW_NUMBER.
- **COALESCE** — funkce, která vrátí první hodnotu ze svých argumentů, která není NULL.
- **DML** (jazyk pro manipulaci s daty) — data manipulation language: INSERT, UPDATE, DELETE, tedy příkazy, které mění data.

## Hands-on
:::exercise id="m10-e1" title="SQL úlohy 1–5: základy" min="30" tool="SQL playground (sql.html)"
**Cíl:** zabydlet se v SELECT, WHERE, ORDER BY a GROUP BY nad daty ExportShield.

Otevři SQL playground (`sql.html`), nebo nahraj `data/sql/exportshield.sql` do [SQLite Online](https://sqliteonline.com/). Na každou úlohu napiš jeden dotaz a poznamenej si počet řádků.

1. Vypiš všechny odběratele sídlící v Německu (kód země `DE`) s jejich odvětvím.
2. Kolik zákazníků je v každém segmentu? Seřaď od největší skupiny.
3. Vypiš faktury s částkou nad 100 000, od největší. Zobraz měnu. Co je špatně na porovnávání těchto částek?
4. Které žádosti o úvěrový limit stále čekají na rozhodnutí? Nejstarší první.
5. Najdi zákazníky, jejichž název obsahuje „Glass“. Čeho si všimneš?

**Hotovo, když:** máš pět funkčních dotazů a k úlohám 3 a 5 poznámku o jedné větě. Řešení jsou na konci Deep dive.
:::

:::exercise id="m10-e2" title="SQL úlohy 6–10: joiny a agregace" min="45" tool="SQL playground (sql.html)"
**Cíl:** kombinovat tabulky a shrnovat data.

6. Celková schválená částka všech úvěrových limitů APPROVED a REDUCED, po měnách.
7. Počet rozhodnutí o úvěrovém limitu na underwritera (bez otevřených žádostí).
8. Odběratelé v zemích s rizikovou kategorií 5 a vyšší: jméno odběratele, název země, riziková kategorie, nejrizikovější první.
9. Každý odběratel s počtem svých úvěrových limitů, včetně odběratelů bez limitu. (Nápověda: LEFT JOIN, a přemýšlej, co počítáš.)
10. Míra zamítnutí na underwritera v procentech, zaokrouhlená na jedno desetinné místo. (Nápověda: CASE WHEN uvnitř SUM.)

**Hotovo, když:** všech pět dotazů běží, úloha 9 vrací 25 řádků a umíš jednou větou vysvětlit, proč úloha 9 potřebuje LEFT JOIN.
:::

:::exercise id="m10-e3" title="SQL úlohy 11–15: analytické otázky" min="60" tool="SQL playground (sql.html)"
**Cíl:** používat SQL jako analytik: data, chybějící údaje, kvalita dat a business poměr.

11. Průměrný, minimální a maximální počet dní mezi žádostí a rozhodnutím o úvěrovém limitu, po underwriterech. Která hodnota nemůže být správně a který záznam ji způsobuje?
12. Nezaplacené faktury víc než 90 dní po splatnosti k 2026-09-30 **bez** jakékoli škody. Proč by tento seznam mohl zajímat oddělení škod?
13. Najdi duplicitní čísla faktur.
14. Najdi škody se statusem PAID, u nichž se součet plateb liší od výše plnění, včetně škod úplně bez plateb.
15. Jen pro faktury v EUR: po zemích odběratelů celková fakturovaná částka, celková nárokovaná částka a nárokovaný podíl v procentech. Odběratelé bez země nesmí zmizet. (Nápověda: dvě CTE, pak LEFT JOIN.)

**Hotovo, když:** všech pět dotazů běží a ke každému nalezenému datovému problému máš jeden řádek: co je špatně, kolik řádků a pravděpodobný business dopad.
:::

:::exercise id="m10-e4" title="SQLBolt lekce 1–12" min="90" tool="SQLBolt"
**Cíl:** procvičit základní syntaxi s okamžitou zpětnou vazbou, nezávisle na datech ExportShield.

1. Jdi na [SQLBolt](https://sqlbolt.com/) a projdi lekce 1 až 12. Pokrývají SELECT, filtrování podmínkami, řazení, joiny včetně vnějších (outer joins), NULL, výrazy, agregace a pořadí, ve kterém se dotaz vykonává.
2. Po každé lekci napiš jeden dotaz stejného typu nad daty ExportShield v SQL playgroundu a zapiš si ho do vlastního taháku.
3. Po lekci 12 popiš vlastními slovy, v jakém pořadí databáze dotaz zpracovává (FROM a JOIN, WHERE, GROUP BY, HAVING, SELECT, ORDER BY, LIMIT) a proč z toho plyne, že alias ze SELECT nemůžeš použít ve WHERE.

**Hotovo, když:** máš dokončených všech dvanáct lekcí a tvůj tahák obsahuje aspoň dvanáct dotazů nad ExportShield, jeden na lekci.
:::

## Self-check
:::q
Jaký je rozdíl mezi WHERE a HAVING?
---
WHERE filtruje jednotlivé řádky ještě před seskupením, takže nemůže používat agregace jako COUNT. HAVING filtruje skupiny po GROUP BY a agregaci, takže je používat může, například `HAVING COUNT(*) >= 3`. V jednom dotazu můžeš použít obojí: WHERE odstraní zaplacené faktury a HAVING pak ponechá jen odběratele se třemi a více nezaplacenými.
:::

:::q
Proč `WHERE paid_date = NULL` nevrátí žádné řádky a co napsat místo toho?
---
NULL znamená „neznámé“ a porovnání čehokoli s neznámou hodnotou dá výsledek „neznámé“, ne pravda. Řádky se vrací jen tehdy, když je podmínka pravdivá, takže žádný řádek neprojde. Napiš `WHERE paid_date IS NULL` (nebo `IS NOT NULL` pro opak).
:::

:::q
Spojíš `buyers` s `countries` přes INNER JOIN a dostaneš 24 řádků, ale odběratelů je 25. Co se stalo a jak to opravíš?
---
Jeden odběratel nemá kód země, takže mu v `countries` neodpovídá žádný řádek a INNER JOIN ho vyřadí. Použij LEFT JOIN s `buyers` vlevo: zůstane všech 25 odběratelů a u odběratele bez shody budou sloupce země NULL. Pak rozhodni, jestli chybějící země je problém kvality dat, který je potřeba nahlásit.
:::

:::q
Po spojení faktur s úvěrovými limity je součet částek faktur vyšší než prostý součet přes faktury. Proč?
---
Join znásobil řádky: když jedna faktura odpovídá dvěma řádkům úvěrového limitu (například existujícímu limitu a nové otevřené žádosti pro stejnou smlouvu a odběratele), faktura se objeví dvakrát a její částka se započítá dvakrát. Kontroluj počty řádků před joiny a po nich a ujisti se, že klíče joinu identifikují nejvýš jeden řádek na straně, kterou násobit nechceš.
:::

:::q
Jaký je rozdíl mezi `COUNT(*)` a `COUNT(paid_date)`?
---
`COUNT(*)` počítá všechny řádky. `COUNT(paid_date)` počítá jen řádky, kde `paid_date` není NULL. V tabulce faktur to dává 78 a 47: zaplacených faktur je 47. Rozdíl je rychlá kontrola úplnosti nebo stavu.
:::

:::q
Kolega chce „celkovou hodnotu faktur po splatnosti“. Na co se zeptáš, než napíšeš dotaz?
---
K jakému datu, a patří tam i faktury zaplacené pozdě, ale už zaplacené? Po splatnosti o jakýkoli počet dní, nebo nad nějaký práh? V jaké měně, a pokud jich je víc, přepočítat kurzem (jakým), nebo vykázat odděleně? Zahrnout faktury, ke kterým už existuje škoda? Jen u aktivních smluv? Když tyto předpoklady napíšeš k číslu, nestane se, že dva lidé dostanou různé součty.
:::

:::q
Proč business analytici v produkčních databázích skoro nespouštějí UPDATE ani DELETE?
---
Přímé změny obcházejí business logiku aplikace, historii a notifikace, takže data mohou skončit nekonzistentní. Obcházejí také audit a schvalování, které regulované firmy jako pojišťovny a banky mít musí. Opravy dat proto jdou přes schválené, otestované skripty, které spouští odpovědný tým. Analytik specifikuje, co se má změnit, a výsledek ověří pomocí SELECT.
:::

:::q
Jak pomocí SQL ověříš akceptační kritérium?
---
Přepiš kritérium na dotaz, který hledá porušení, takže očekávaný výsledek je nula řádků. Pro „schválený limit nikdy není vyšší než požadovaná částka“ vyber limity, kde `approved_amount > requested_amount`. Spusť ho po testu a po každém releasu; každý vrácený řádek je defekt s konkrétním důkazem.
:::

## Interview corner
:::interview
Jaký je rozdíl mezi INNER JOIN a LEFT JOIN? Uveď příklad.
*EN: What is the difference between INNER JOIN and LEFT JOIN? Give an example.*
---
- INNER JOIN vrací jen řádky, které mají shodu v obou tabulkách.
- LEFT JOIN vrací všechny řádky z levé tabulky; sloupce z pravé tabulky jsou NULL tam, kde nic neodpovídá.
- Příklad: všichni odběratelé s jejich zemí; odběratel bez země s INNER JOIN zmizí, s LEFT JOIN zůstane.
- LEFT JOIN plus `WHERE right.id IS NULL` najde záznamy bez souvisejícího záznamu (odběratelé bez úvěrového limitu).

Typická chyba: vysvětlovat joiny jen Vennovými diagramy a neříct, co se stane s řádky bez shody a proč se objevují NULL.
:::

:::interview
Jak jsi používala SQL v práci nebo v projektech?
*EN: How have you used SQL in your work or projects?*
---
- Konkrétní otázka, na kterou jsi odpověděla čísly, např. jak dlouho trvají rozhodnutí o úvěrových limitech.
- Ověřování výsledků testů: akceptační kritéria přepsaná na dotazy, které musí vrátit nula řádků.
- Kontroly kvality dat: duplicity, chybějící hodnoty, protichůdná data, s počty a dopadem.
- Vyčíslení problému pro business case.
- Co bys nedělala: měnit produkční data napřímo.

Typická chyba: říct „umím SQL“ bez jediného příkladu otázky, na kterou pomohlo odpovědět.
:::

:::interview
Napiš dotaz, který ukáže počet škod a celkovou nárokovanou částku podle statusu.
*EN: Write a query that shows the number of claims and total claimed amount per status.*
---
- `SELECT status, COUNT(*) AS claims, SUM(claimed_amount) AS claimed FROM claims GROUP BY status ORDER BY claims DESC;`
- Při psaní krátce vysvětli každou klauzuli.
- Zmiň problém s měnami: před sčítáním částek seskup i podle měny, nebo filtruj.
- Zmiň kontrolu výsledku: součet počtů se rovná `SELECT COUNT(*) FROM claims`.

Typická chyba: vybrat sloupec, který není v GROUP BY ani v agregaci.
:::

:::interview
Jak kontroluješ kvalitu dat pomocí SQL?
*EN: How do you check data quality with SQL?*
---
- Úplnost (completeness): počty `IS NULL` a `COUNT(*)` versus `COUNT(column)`.
- Platnost (validity): formáty a rozsahy, např. `length(ico) <> 8`, datum splatnosti před datem vystavení.
- Konzistence (consistency): rozpory mezi poli a tabulkami, např. škody PAID bez plateb (LEFT JOIN).
- Jedinečnost (uniqueness): `GROUP BY ... HAVING COUNT(*) > 1`.
- Uveď počet, příklady, dopad a příčinu (root cause) a navrhni preventivní validaci.

Typická chyba: vyjmenovat problémy, ale nevyčíslit je a neříct, proč jsou pro business důležité.
:::
