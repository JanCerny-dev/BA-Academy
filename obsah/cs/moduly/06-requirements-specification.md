---
id: 06
slug: requirements-specification
title: Psaní požadavků a specifikací
phase: B
priority: P1
quick_min: 5
deep_min: 45
job_ad: "tvořit technické specifikace pro dodavatele"
---

## Why this matters
Inzerát to říká přímo: požadavky od oddělení budeš převádět na specifikace pro dodavatele. Dodavatel postaví to, co je napsané, ne to, co se myslelo. Každá vágní věta skončí jako defekt, jako change request s cenovkou, nebo jako hádka v UAT. Psaní jasných, testovatelných a dohledatelných požadavků je nejviditelnější část práce BA a na pohovoru tě často nechají vylepšit špatný požadavek přímo na místě.

## Quick version
**Requirement** (požadavek) je výrok o potřebě nebo schopnosti, kterou musí řešení splnit. **Specification** (specifikace) je dokument, který požadavky sbírá v dohodnuté struktuře, aby někdo jiný (dodavatel, vývojář, tester) mohl řešení postavit a ověřit.

**Dobré požadavky jsou** (vlastnosti pocházejí z ISO/IEC/IEEE 29148 a IREB CPRE, každý zdroj je formuluje trochu jinak):
- **Unambiguous** (jednoznačný) – připouští jediný výklad.
- **Verifiable** (ověřitelný) – tester umí prokázat, že je splněný.
- **Atomic** (atomický, v normě *singular*) – jeden požadavek na jeden výrok, žádné „a ještě“.
- **Consistent** (konzistentní) – neodporuje jiným požadavkům.
- **Feasible** (proveditelný) – dá se postavit v daných omezeních.
- **Necessary** (nezbytný) – vede zpět ke skutečné business potřebě.
- **Traceable** (dohledatelný) – má jedinečné ID a známý zdroj.

**Šablona věty:** `[ID] The system shall [action] [object] [condition / constraint].`
Příklad: *FR-012 The system shall retrieve the buyer's name and registered address from ARES within 5 seconds after a valid 8-digit registration number is entered.* „Shall“ označuje povinný požadavek, „should“ žádoucí, „will“ konstatování faktu. Vyber si konvenci a uveď ji v dokumentu.

**Funkční vs. nefunkční.** **Functional requirement** (funkční požadavek) říká, co systém dělá (počítá, zobrazuje, odesílá, validuje). **Non-functional requirement** (nefunkční požadavek, také *quality requirement*) říká, jak dobře nebo za jakých omezení: výkon, bezpečnost, dostupnost, použitelnost, auditovatelnost, soulad s předpisy. Nefunkční požadavky musí být měřitelné: „dostupnost 99,5 % v pracovní době (po–pá 8:00–18:00 SEČ)“, ne „vysoce dostupný“.

**Business rules** (business pravidla) jsou pravidla organizace, která musí systém vynucovat: „Úvěrové limity nad 1 000 000 EUR musí schválit Risk Committee.“ Veď je v samostatném seznamu s vlastními ID, protože se mění nezávisle na softwaru.

**Běžné dokumenty:**
- **BRD** (Business Requirements Document) – proč, cíle, rozsah, business a stakeholder požadavky.
- **FRS / funkční specifikace** – co přesně řešení dělá: funkce, obrazovky, data, pravidla.
- **SRS** (Software Requirements Specification) – úplné softwarové požadavky, funkční i nefunkční, často ve struktuře podle IEEE.
- **Technická specifikace** – jak se to postaví: architektura, rozhraní, databáze. Obvykle ji píše dodavatel nebo architekt.

Názvy se mezi firmami liší. Důležité je, aby dodavatel dostal dokument, který uvádí kontext, rozsah, co je mimo rozsah (out of scope), aktéry, proces, číslované funkční požadavky, UI, data, integrace, nefunkční požadavky, akceptační kritéria a otevřené otázky.

**Use cases** (případy užití) popisují interakci mezi aktérem a systémem krok za krokem: hlavní tok, alternativní toky, výjimkové toky. Jsou dobrým nástrojem, jak najít chybějící požadavky.

**Prioritizace:** **MoSCoW** – Must have, Should have, Could have, Won't have (this time).

**Traceability matrix** (matice dohledatelnosti): tabulka, která propojuje každý požadavek s jeho zdrojem, business cílem, prvky návrhu a testovacími případy. Odpovídá na otázky „proč tu tohle je?“ a „je to otestované?“.

**Po napsání:** projdi dokument se stakeholdery a dodavatelem, verzuj ho, získej **sign-off** (formální schválení) a pozdější změny řeš přes **change requests** (změnové požadavky).

**Slova, kterým se vyhnout:** fast, user-friendly, flexible, etc., and/or, if possible, appropriate, as needed, support, minimal, robust (rychlý, uživatelsky přívětivý, flexibilní, atd., a/nebo, pokud možno, vhodný, dle potřeby, podporovat, minimální, robustní).

**Věta na pohovor:** „Píšu atomické, testovatelné požadavky s ID, odděluji business pravidla a nefunkční požadavky s měřitelnými hodnotami a vedu traceability matrix od business cíle po testovací případ.“

## Deep dive

### Co dělá požadavek dobrým [P1]
ISO/IEC/IEEE 29148 (mezinárodní norma pro requirements engineering) i sylabus IREB CPRE uvádějí vlastnosti kvality jednotlivých požadavků. Formulace se trochu liší a liší se i vydání normy: aktuální 29148 (2018) uvádí pro jeden požadavek necessary, appropriate, unambiguous, complete, singular, feasible, verifiable, correct a conforming, a konzistenci posuzuje u celé množiny požadavků; starší vydání z roku 2011 jmenovalo ještě traceable a implementation-free. Tabulka používá společné jádro:

| Vlastnost | Význam | Špatně | Lépe |
|---|---|---|---|
| Unambiguous | Jen jeden výklad | „The system shall display recent requests.“ | „The system shall display credit limit requests created in the last 30 calendar days.“ |
| Verifiable | Dá se prokázat inspekcí, analýzou, demonstrací nebo testem | „The form shall be easy to use.“ | „A new user shall complete a credit limit request without help in under 5 minutes in a usability test with 5 users.“ |
| Atomic (singular) | Jedna potřeba na jeden výrok | „The system shall validate and save the request and notify the underwriter.“ | Tři požadavky: validovat, uložit, upozornit. |
| Consistent | Neodporuje jiným požadavkům | FR-10 říká limit v EUR, FR-22 limit v měně exportéra | Dohodnout jedno pravidlo a odkazovat na něj. |
| Feasible | Dosažitelný v rámci rozpočtu, času a technologie | „The lookup shall always return in 0 seconds.“ | „…within 5 seconds for 95 % of requests.“ |
| Necessary | Bez něj by zůstala potřeba nesplněná | „The screen shall show a weather widget.“ | Odstranit. |
| Complete | Obsahuje všechny potřebné informace | „The system shall send a notification.“ | Komu, kdy, jakým kanálem, s jakým obsahem. |
| Traceable | Jedinečné ID, známý zdroj a vazby | Odrážka bez ID | „FR-014, source: interview with Underwriting, 12 March, BR-02.“ |
| Implementation-free | Říká co, ne jak (pokud nejde o omezení) | „Store the limit in an Oracle table.“ | „The system shall store the approved limit…“ (volba databáze patří do návrhu). |

Praktický test pro každý požadavek: *Mohli by dva lidé podle této věty postavit dvě různé věci?* a *Jak by tester prokázal, že je splněný?* Pokud je ti některá odpověď nepříjemná, přepiš ho.

### Šablony vět [P1]
Šablony dělají požadavky jednotnými a snáz se reviduje. Běžně používaný vzor (podobný šabloně IREB):

`[ID] [When/If <condition>,] the system shall [<action verb>] [<object>] [<qualifier / constraint>].`

Příklady pro ExportShield:
- *FR-001* The system shall allow an exporter to submit a credit limit request for one buyer.
- *FR-002* When the exporter enters a buyer registration number, the system shall validate that it consists of exactly 8 digits.
- *FR-003* If the registration number is valid, the system shall retrieve the buyer's name, legal form and registered address from ARES.
- *FR-004* If ARES returns no record, the system shall display the message "Buyer not found in the registry. Please check the number or enter the details manually." and allow manual entry.
- *FR-005* The system shall assign each submitted request a unique request number in the format CLR-YYYY-NNNNN.

Konvence klíčových slov (uveď je v dokumentu):
- **shall** = povinné,
- **should** = žádoucí, dá se vyjednat,
- **may** = volitelné,
- **will** = konstatování faktu nebo záměru, není to požadavek.

V moderních dokumentech se běžně používá i „must“. Jde hlavně o jednotnost.

### Funkční požadavky [P1]
Funkční požadavky popisují chování: vstupy, zpracování, výstupy. Typická slovesa: create, display, calculate, validate, send, store, search, export, assign, notify. Seskupuj je podle funkce nebo kroku procesu, aby je čtenář našel (například „3.1 Request submission“, „3.2 Buyer lookup“, „3.3 Assessment“, „3.4 Decision and notification“).

Každý funkční požadavek má říkat *kdo* (který aktér nebo jaký spouštěč), *co* a *za jaké podmínky*. Funkční je i ošetření chyb: co se stane při neplatném vstupu, chybějících datech, vypršení časového limitu (timeout). Začátečníci na to zapomínají a dodavatel pak postaví, co je nejlevnější.

### Nefunkční požadavky [P1]
Nefunkční požadavky (NFRs) popisují kvality a omezení. Často o nich rozhoduje IT, bezpečnost nebo compliance, ne business uživatelé, takže tyto lidi přizvi brzy. Každý NFR potřebuje číslo nebo ověřitelnou podmínku.

| Kategorie | Vágně | Měřitelný příklad |
|---|---|---|
| Performance (výkon) | „The system shall be fast.“ | „The buyer lookup shall return a result within 5 seconds for 95 % of requests at a load of 50 concurrent users.“ |
| Availability (dostupnost) | „The portal shall be always available.“ | „The exporter portal shall be available 99.5 % of the time Mon–Fri 7:00–19:00 CET, measured monthly, excluding announced maintenance.“ |
| Security (bezpečnost) | „Data shall be secure.“ | „Users shall authenticate with multi-factor authentication. Exporters shall see only requests of their own company.“ |
| Usability (použitelnost) | „The form shall be intuitive.“ | „All mandatory fields shall be marked and each validation error shall be shown next to the field it concerns.“ |
| Auditability (auditovatelnost) | „Changes shall be logged.“ | „The system shall record user ID, timestamp, old value and new value for every change of a credit limit decision, and keep the record for 10 years.“ |
| Compliance (soulad s předpisy) | „The system shall be GDPR-compliant.“ | „Personal data of buyer contact persons shall be deleted or anonymized no later than X years after the policy ends, as defined by the data retention policy.“ |
| Capacity (kapacita) | „The system shall handle many requests.“ | „The system shall support at least 2,000 credit limit requests per month.“ |
| Recoverability (obnovitelnost) | „Data shall not be lost.“ | „After an outage, the service shall be restored within 4 hours, with data loss of at most 15 minutes.“ |

Na pohovoru přijdou na řadu dva z těchto pojmů: **RTO** (Recovery Time Objective, za jak dlouho musí služba znovu běžet, tady 4 hodiny) a **RPO** (Recovery Point Objective, kolik dat se smí ztratit, tady 15 minut).

Doby uchování (retention) a zákonné povinnosti musí dodat právní oddělení nebo compliance. Nehádej je; napiš „X let podle retention policy, potvrdí Compliance“ a dej to do otevřených otázek.

### Business pravidla [P1]
**Business rule** (business pravidlo) je zásada nebo předpis, který omezuje nebo vymezuje business, nezávisle na jakémkoli systému. Příklady:
- *BR-01* A credit limit request above 1,000,000 EUR requires Risk Committee approval.
- *BR-02* A credit limit cannot be approved for a buyer in a country with risk rating 7 unless the CEO approves an exception.
- *BR-03* Payment terms longer than 180 days are not insurable under the standard policy.

Proč je oddělovat: pravidla se mění, když rozhodne vedení, ne když se mění software. Funkční požadavek pak na pravidlo *odkazuje*: *FR-031 The system shall route the request to the Risk Committee queue when BR-01 applies.* Když se hranice změní na 1,5 mil. EUR, změní se jen BR-01. Složité sady pravidel jde zapsat jako rozhodovací tabulky (viz DMN v modulu 04).

### Datové požadavky [P1]
Dodavatel potřebuje přesné definice dat. Nejjasnějším formátem je tabulka **data dictionary** (datový slovník):

| Pole | Popis | Typ / formát | Povinné | Validace | Zdroj |
|---|---|---|---|---|---|
| request_no | Jedinečné číslo žádosti | Text, `CLR-YYYY-NNNNN` | Ano (systém) | Generované, jedinečné | Systém |
| buyer_reg_no | Registrační číslo odběratele (u českých odběratelů IČO) | Text, 8 číslic | Ano u CZ odběratelů | Přesně 8 číslic, kontrolní součet podle pravidel registru | Exportér |
| buyer_name | Obchodní název odběratele | Text, max. 255 znaků | Ano | Neprázdné | ARES nebo ručně |
| country_code | Země odběratele | ISO 3166-1 alpha-2 (např. `DE`) | Ano | Z číselníku zemí | Exportér |
| requested_amount | Požadovaný úvěrový limit | Desetinné číslo, 2 místa, > 0 | Ano | 1 000 – 50 000 000 | Exportér |
| currency | Měna částky | ISO 4217 (např. `EUR`) | Ano | EUR, USD, CZK | Exportér |
| payment_terms_days | Sjednaná splatnost | Celé číslo | Ano | 1 – 180 (viz BR-03) | Exportér |
| status | Stav žádosti | Výčet (enum) | Ano (systém) | Submitted, In assessment, Approved, Reduced, Rejected | Systém |

Standardy jako ISO 3166 (kódy zemí) a ISO 4217 (kódy měn) tě ušetří vymýšlení vlastních číselníků. Datovému modelování se věnuje modul 09.

### Dokumenty: BRD, FRS, SRS, technická specifikace [P1]
Firmy tyto názvy používají nejednotně, proto se vždy zeptej: „Co obsahuje vaše šablona?“ Typické rozdělení:

| Dokument | Hlavní otázka | Typický obsah | Typický autor | Čtenář |
|---|---|---|---|---|
| Business case | Máme to dělat? | Problém, varianty, náklady, přínosy | BA / sponzor | Vedení |
| BRD | Proč a co na úrovni businessu? | Cíle, rozsah, stakeholdeři, business a stakeholder požadavky, AS-IS/TO-BE proces | BA | Sponzor, business, dodavatel |
| FRS / funkční specifikace | Co přesně řešení dělá? | Funkční požadavky, use cases, UI, data, business pravidla, integrace (funkční pohled), NFRs | BA | Dodavatel, vývojáři, testeři |
| SRS | Úplné softwarové požadavky | Podobné FRS, často ve struktuře IEEE/ISO, silné v NFRs | BA / requirements engineer | Vývojáři, testeři |
| Technická specifikace / návrh | Jak se to postaví? | Architektura, komponenty, API kontrakty, databáze, nasazení | Dodavatel / architekt | Vývojáři, IT provoz |

V dodavatelských projektech obvykle klient píše funkční specifikaci a dodavatel odpoví technickým návrhem nebo popisem řešení. Tvoje specifikace je často přílohou smlouvy, takže přesnost má finanční důsledky.

### Šablona: funkční specifikace pro dodavatele [P1]
Struktura, která funguje pro změnu typu „automatická kontrola v ARES v žádosti o úvěrový limit“:

1. **Document control** (řízení dokumentu) – název, verze, datum, autor, stav (draft / in review / approved), historie změn, schvalovatelé.
2. **Kontext a cíl** – business problém, business požadavky s ID, odkaz na BRD. Dva odstavce, ne dvě stránky.
3. **Scope** (rozsah) – co je zahrnuto. **Out of scope** (mimo rozsah) – co výslovně zahrnuto není (tahle sekce předejde většině sporů).
4. **Předpoklady a omezení** – například „PolicyHub zůstává ve verzi X“, „použije se veřejné API ARES, SLA není k dispozici“.
5. **Aktéři a role** – exportér, underwriter, vedoucí underwritingu, systémoví aktéři (ARES, PolicyHub), s oprávněními.
6. **Proces** – TO-BE diagram v BPMN a krátký popis každého kroku.
7. **Funkční požadavky** – číslované (FR-001…), seskupené podle funkce, každý s prioritou a zdrojem. Kde se hodí, use cases.
8. **Business pravidla** – BR-01…, odkazovaná z FR.
9. **Uživatelské rozhraní** – wireframy, seznam polí na každé obrazovce, hlášky a chybové texty.
10. **Data** – data dictionary, validace, uchovávání dat.
11. **Integrace** – pro každé rozhraní: systémy, směr, spouštěč, datová pole, formát (JSON/XML), frekvence, ošetření chyb, kdo rozhraní vlastní.
12. **Nefunkční požadavky** – výkon, dostupnost, bezpečnost, auditovatelnost, compliance, s čísly.
13. **Reporting** – jaké reporty nebo exporty, pole, filtry.
14. **Transition requirements** (přechodové požadavky) – migrace, školení, nasazení.
15. **Akceptační kritéria a přístup k UAT** – jak klient dodávku převezme, klíčové testovací scénáře.
16. **Otevřené otázky a log rozhodnutí** – ID, otázka, vlastník, termín, odpověď.
17. **Glosář** – doménové pojmy (buyer, credit limit, IČO, indemnity).

### Specifikace use case [P1]
**Use case** (případ užití) popisuje, jak aktér používá systém k dosažení cíle, jako posloupnost kroků. Je užitečný, protože při procházení kroků se ukážou chybějící požadavky, hlavně v chybových situacích. Diagramy use case patří do UML (modul 08); tady se soustředíme na textovou specifikaci.

**Příklad: UC-03 Look up buyer in registry**

| Položka | Obsah |
|---|---|
| ID / název | UC-03 Look up buyer in registry |
| Primární aktér | Exportér (uživatel portálu) |
| Sekundární aktér | ARES (externí registr) |
| Cíl | Údaje o odběrateli se vyplní z oficiálního registru bez přepisování |
| Preconditions (vstupní podmínky) | Exportér je přihlášený; formulář žádosti o úvěrový limit je otevřený; země odběratele je vybraná |
| Trigger (spouštěč) | Exportér zadá registrační číslo odběratele a zvolí „Look up“ |
| Postconditions (výstupní podmínky, úspěch) | Název, právní forma a adresa odběratele jsou ve formuláři zobrazené jen pro čtení a uložené k žádosti spolu s časem vyhledání |
| Související | BR-G1, FR-002 – FR-006, NFR-P01 |

**Hlavní tok (main flow)**
1. Exportér zadá osmimístné registrační číslo a zvolí „Look up“.
2. Systém ověří formát čísla.
3. Systém pošle do ARES požadavek s registračním číslem.
4. ARES vrátí záznam o firmě.
5. Systém zobrazí název, právní formu a sídlo jako pole jen pro čtení.
6. Systém uloží získaná data a čas vyhledání k rozpracované žádosti.
7. Use case končí.

**Alternativní toky (alternative flows)**
- *A1 – Země odběratele není CZ (před krokem 1):* systém skryje tlačítko „Look up“ a exportér zadá údaje o odběrateli ručně. Žádost dostane příznak „Manual buyer data“.
- *A2 – Exportér po úspěšném vyhledání změní číslo (po kroku 5):* systém vymaže načtená pole a vrátí se ke kroku 2.

**Výjimkové toky (exception flows)**
- *E1 – Neplatný formát (v kroku 2):* systém u pole zobrazí „Registration number must have 8 digits“. Tok se vrací ke kroku 1.
- *E2 – Odběratel nenalezen (v kroku 4):* systém zobrazí „Buyer not found in the registry. Please check the number or enter the details manually.“ a povolí ruční zadání. Žádost dostane příznak „Manual buyer data“.
- *E3 – ARES není dostupný nebo neodpoví do 10 sekund (v kroku 4):* systém zobrazí „The registry is temporarily unavailable. You can enter the details manually or try again later.“ a povolí ruční zadání. Systém chybu zaloguje. Žádost dostane příznak „Manual buyer data“, aby ji underwriter ověřil.
- *E4 – Odběratel je v ARES veden jako zaniklý nebo v likvidaci (v kroku 4):* systém zobrazí data s varováním a označí žádost pro underwritera.

Každý tok se promítne do požadavků a do testovacích případů. Příznak „Manual buyer data“ například nezmínil žádný stakeholder; objevil se proto, že výjimkové toky vynutily otázku „a co se stane pak?“. Jestli ARES opravdu vrací stav likvidace v polích, která potřebuješ, je otázka pro analýzu integrace, takže ji zapíšeš jako otevřenou otázku.

### Prioritizace [P1]
**MoSCoW** je nejběžnější technika:
- **Must have** – bez toho řešení není přijatelné nebo není v souladu se zákonem.
- **Should have** – důležité, ale existuje náhradní řešení (workaround).
- **Could have** – hezké, pokud zbude čas a rozpočet.
- **Won't have (this time)** – dohodnuto jako mimo rozsah tohoto release, zapsáno, aby se téma nevracelo každý týden.

Varovný signál: 80 % požadavků označených „Must“. Zeptej se: „Co se stane, když půjdeme do provozu bez toho?“ Pokud zní odpověď „nějak bychom to zvládli“, není to Must.

**Kano model** [P3] třídí vlastnosti podle toho, jak ovlivňují spokojenost: *basic* (základní, očekávané; když chybí, uživatel je nespokojený, když jsou, nikdo si jich nevšimne, například že se žádost uloží), *performance* (výkonnostní, čím víc, tím líp, například rychlejší rozhodnutí) a *delighters* (nadšení, nečekané, vyvolají nadšení, například automatické předvyplnění z registru). Časem se z delighters stanou základní očekávání.

Existují i další techniky (pořadí, rozdělení 100 bodů, matice náklady–hodnota), ale nejčastěji potkáš MoSCoW.

### Traceability matrix [P1]
**Traceability** (dohledatelnost) je schopnost sledovat požadavek zpět k jeho zdroji a dopředu k návrhu, implementaci a testům. **Requirements traceability matrix (RTM)** je nejjednodušší nástroj, obvykle tabulka v Excelu:

| Req ID | Požadavek (zkráceně) | Zdroj | Business req. | Priorita | Sekce návrhu / specifikace | Testovací případ(y) | Stav |
|---|---|---|---|---|---|---|---|
| FR-002 | Validate 8-digit registration number | Interview Underwriting 12 Mar | BR-G1 | Must | 7.2 | TC-010, TC-011 | Approved |
| FR-003 | Retrieve buyer data from ARES | Workshop 19 Mar | BR-G1 | Must | 7.2, 11.1 | TC-012 | Approved |
| FR-004 | Message when buyer not found | UC-03 E2 | BR-G1 | Must | 7.2, 9 | TC-013 | Approved |
| NFR-P01 | Lookup within 5 s for 95 % | IT Operations | BR-G2 | Should | 12 | TC-040 | In review |

Odpovídá na praktické otázky: Které požadavky nemají test? Které testy se rozbijí, když se změní FR-003? Chtěl tenhle požadavek vůbec někdo? V nástrojích jako Jira dělají totéž vazby mezi issues (modul 07).

### Verzování, revize a sign-off [P1]
**Verzování:** používej čísla verzí (0.1, 0.2 pro koncepty, 1.0 pro první schválenou verzi, 1.1 pro schválené změny) a tabulku historie změn: verze, datum, autor, co se změnilo. Měj jednu hlavní kopii na sdíleném místě, například v Confluence nebo SharePointu, nikdy ne verze v přílohách e-mailů.

**Revize:** před sign-off specifikaci revidují:
- business stakeholdeři (je to, co potřebujeme?),
- dodavatel nebo vývojáři (je to jasné a proveditelné? co chybí?),
- testeři (dá se to otestovat?),
- IT bezpečnost, architektura, compliance, kde je to relevantní.

Schůzka typu walkthrough, na které dokument projdeš sekci po sekci, funguje lépe než „prosím o připomínky do pátku“. Zapisuj připomínky a jak byly vyřešené.

**Sign-off** je formální schválení verze lidmi, kteří za ni odpovídají (product owner, vlastník procesu, někdy dodavatel). Vzniká tím **baseline** (schválený základ): od této chvíle se změny řídí.

### Řízení změn a change requests [P1]
I po sign-off se požadavky budou měnit: změní se legislativa, někdo si vzpomene na výjimku, UAT odhalí mezeru. **Change control** (řízení změn) je dohodnutý postup, jak s tím naložit. **Change request (CR)** typicky obsahuje:
- ID, název, žadatele, datum,
- popis změny a důvod,
- dotčené požadavky a dokumenty (pomůže traceability matrix),
- analýzu dopadu: pracnost, náklady, harmonogram, riziko (často odhaduje dodavatel),
- prioritu, rozhodnutí (schváleno / zamítnuto / odloženo), schvalovatele, datum.

Ve smlouvě s dodavatelem za pevnou cenu znamenají CR obvykle vícenáklady, což je jeden z důvodů, proč musí být původní specifikace přesná. V agilním prostředí jdou změny do backlogu a prioritizují se jako každá jiná položka, ale smluvní rozsah může i tak vyžadovat formální CR.

### Slova, která vytvářejí nejednoznačnost [P1]
| Slovo nebo fráze | Problém | Nahraď |
|---|---|---|
| fast, quickly, real time (rychle, v reálném čase) | Chybí číslo | „do 5 sekund“ |
| user-friendly, intuitive, easy (přívětivý, intuitivní, snadný) | Nedá se otestovat | Konkrétní kritéria použitelnosti |
| etc., and so on (atd., a tak dále) | Neúplný výčet | Úplný výčet |
| and/or (a/nebo) | Nejasná kombinace | Dva požadavky nebo explicitní logika |
| if possible, ideally (pokud možno, ideálně) | Není to požadavek | Rozhodni: shall, nebo odstranit |
| appropriate, adequate, sufficient (vhodný, přiměřený, dostatečný) | Kdo o tom rozhodne? | Přesné kritérium |
| support, handle (podporovat, zvládat) | Co přesně? | Konkrétní činnost |
| all, always, never (vše, vždy, nikdy) | Často to neplatí | Ověř a uveď výjimky |
| minimize, maximize, optimize | Chybí cíl | Cílová hodnota |
| flexible, scalable, robust | Není měřitelné | Konkrétní kapacita nebo scénář změny |
| should (když myslíš povinné) | Oslabuje závazek | shall / must |
| it, they, this (nejasný odkaz) | Který objekt? | Pojmenuj objekt |

AI asistenti se hodí na první průchod: vlož vlastní požadavky (nedůvěrné nebo fiktivní) a zeptej se, které obsahují nejednoznačné výrazy. Výstup ber jako návrhy; rozhoduješ pořád ty.

## Key terms
- **Requirement** (požadavek) — výrok o potřebě nebo schopnosti, kterou musí řešení splnit.
- **Specification** (specifikace) — dokument, který sbírá požadavky v dohodnuté struktuře, aby šlo řešení postavit a ověřit.
- **Functional requirement** (funkční požadavek) — co musí systém dělat: chování, vstupy, zpracování, výstupy.
- **Non-functional requirement (NFR)** (nefunkční požadavek) — měřitelná kvalita nebo omezení, například výkon, bezpečnost nebo dostupnost.
- **Business rule** (business pravidlo) — pravidlo organizace, které omezuje business, nezávisle na jakémkoli systému.
- **Atomic requirement** (atomický požadavek) — požadavek, který vyjadřuje právě jednu potřebu.
- **Verifiable** (ověřitelný) — požadavek, jehož splnění jde prokázat inspekcí, analýzou, demonstrací nebo testem.
- **BRD** — Business Requirements Document, popisuje cíle, rozsah a požadavky na úrovni businessu.
- **Functional specification (FRS)** (funkční specifikace) — podrobný popis toho, co řešení dělá, pro vývojáře a dodavatele.
- **SRS** — Software Requirements Specification, úplná sada softwarových požadavků, funkčních i nefunkčních.
- **Technical specification** (technická specifikace) — popis toho, jak se řešení postaví, obvykle ji píše dodavatel nebo architekt.
- **Use case** (případ užití) — popis krok za krokem, jak aktér používá systém k dosažení cíle, s hlavním, alternativními a výjimkovými toky.
- **Data dictionary** (datový slovník) — tabulka, která definuje každé datové pole s formátem, validací a zdrojem.
- **MoSCoW** — prioritizace do skupin Must have, Should have, Could have a Won't have this time.
- **Traceability matrix (RTM)** (matice dohledatelnosti) — tabulka, která propojuje požadavky se zdroji, návrhem a testovacími případy.
- **Sign-off** (formální schválení) — formální schválení verze dokumentu, kterým vzniká baseline.
- **Baseline** (schválený základ) — schválená verze požadavků, vůči které se řídí změny.
- **Change request (CR)** (změnový požadavek) — formální žádost o změnu schváleného rozsahu, u které se před rozhodnutím posoudí dopad.
- **RTO / RPO** — nejdelší přijatelná doba obnovy služby a největší přijatelná ztráta dat vyjádřená časem.

## Hands-on
:::exercise id="m06-e1" title="Přepiš 10 špatných požadavků" min="40" tool="text editor"
Cíl: procvičit převod vágních výroků na testovatelné požadavky.

Přepiš každý výrok. Kde je to potřeba, rozděl ho, doplň čísla a poznamenej si každou otázku, kterou bys musela položit stakeholderovi.

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

Postup: (1) označ nejednoznačná slova, (2) napiš přepsaný požadavek (nebo požadavky) podle šablony s ID, (3) každý zařaď jako funkční, nefunkční nebo business pravidlo, (4) sepiš své otevřené otázky.

Hotovo, když: každý přepsaný požadavek projde testem „uměl by tester prokázat, že je splněný?“ a tam, kde ti chyběly informace, jsi napsala otázku, místo abys potichu vymyslela číslo.
:::

:::exercise id="m06-e2" title="Mini funkční specifikace: automatická kontrola v ARES" min="120" tool="text editor"
Cíl: napsat funkční specifikaci pro dodavatele o rozsahu 3–5 stran pro změnu v ExportShield „automatická kontrola v ARES v žádosti o úvěrový limit“.

1. Použij šablonu se 17 sekcemi z Deep dive. Sekce, které nedokážeš vyplnit, označ „N/A“ s důvodem.
2. Napiš kontext, rozsah a výslovný seznam out of scope (například zahraniční registry, automatické rozhodnutí o úvěru).
3. Vlož TO-BE diagram ze cvičení m04-e2 nebo jeho popis.
4. Napiš alespoň 12 funkčních požadavků s ID, prioritou MoSCoW a zdrojem, včetně ošetření chyb.
5. Napiš UC-03 vlastními slovy nebo druhý use case, například „Underwriter reviews registry data“.
6. Přidej data dictionary s alespoň 6 poli a alespoň 4 měřitelné NFRs.
7. Popiš integraci s ARES: spouštěč, vstup, výstupní pole, chybové případy. Podívej se na skutečnou odpověď v prohlížeči přes veřejné [API ARES](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}) s IČO libovolné veřejně známé firmy.
8. Zakonči alespoň 5 otevřenými otázkami.

Hotovo, když: kolega, který o projektu nikdy neslyšel, ti umí říct, co se postaví, co ne a jak se dodávka převezme.
:::

:::exercise id="m06-e3" title="Sestav traceability matrix" min="40" tool="Excel / Google Sheets"
Cíl: propojit požadavky s jejich zdroji a testy.

1. Vytvoř list se sloupci: Req ID, Requirement (short), Type, Source, Business requirement, Priority, Spec section, Test case IDs, Status.
2. Zadej požadavky ze cvičení m06-e2 a dva business požadavky (například BR-G1 „reduce manual data entry“, BR-G2 „decide within 3 working days“).
3. Vymysli ID testovacích případů (TC-001…) a na druhém listu ke každému napiš jednořádkový popis.
4. Přidej podmíněné formátování, které zvýrazní požadavky bez testovacího případu.
5. Přidej filtr a odpověz: které požadavky Must zatím nepokrývá žádný test?
6. Nasimuluj change request: hranice v BR-01 se mění z 1 mil. na 1,5 mil. EUR. Vypiš všechny dotčené řádky.

Hotovo, když: každý požadavek má zdroj a business požadavek, nepokryté požadavky jsou vidět na první pohled a umíš ukázat dopad change requestu.
:::

## Self-check
:::q
Co je špatně na požadavku „The system shall validate and save the request and notify the underwriter“?
---
Není atomický: obsahuje tři požadavky. Když se jedna část implementuje a jiná ne, požadavek není ani celý splněný, ani celý nesplněný, a nedá se samostatně dohledat ani prioritizovat. Má se rozdělit na tři požadavky, každý s vlastním ID.
:::

:::q
Proč držet business pravidla odděleně od funkčních požadavků?
---
Business pravidla patří organizaci a mění se, když se změní rozhodnutí vedení nebo regulace, nezávisle na softwaru. Když funkční požadavky odkazují na pravidlo přes ID, změna pravidla (například nová schvalovací hranice) se provede na jednom místě a dopad na systém se snadno najde.
:::

:::q
Převeď „The portal shall be available“ na měřitelný nefunkční požadavek.
---
Například: „The exporter portal shall be available 99.5 % of the time Mon–Fri 7:00–19:00 CET, measured monthly, excluding maintenance announced at least 3 working days in advance.“ Uvádí cílovou hodnotu, časové okno, období měření a výjimky.
:::

:::q
K čemu slouží sekce „Out of scope“ ve specifikaci pro dodavatele?
---
Výslovně říká, co se dodávat nebude, aby ani jedna strana později netvrdila, že to bylo očekávané. Většina sporů mezi klientem a dodavatelem vzniká z věcí, které se předpokládaly, ale nikdy nebyly napsané. Jasný seznam out of scope také brání nekontrolovanému rozšiřování rozsahu (scope creep) a vymezuje budoucí change requesty.
:::

:::q
Co ti dají výjimkové toky v use case, co popis šťastné cesty (happy path) nedá?
---
Vynutí otázku „co se stane, když se něco pokazí“, například neplatný vstup, chybějící data nebo nedostupný systém. Odpovědi se stanou dalšími funkčními požadavky, chybovými hláškami a testovacími případy, které stakeholdeři sami od sebe zmiňují jen zřídka.
:::

:::q
Skoro každý požadavek v konceptu je označený „Must have“. Co uděláš?
---
U každého se zeptáš „co se stane, když půjdeme do provozu bez toho?“ a navážeš ho na business cíl. Požadavky s přijatelným náhradním řešením se stanou Should nebo Could. Seznam, kde je všechno Must, nedává žádné vodítko pro kompromisy, až dojde čas nebo rozpočet.
:::

:::q
Jak traceability matrix pomáhá s change requestem?
---
Ukáže, které požadavky, sekce specifikace a testovací případy jsou se změněnou položkou propojené, takže se dopad dá posoudit rychle a úplně. Bez ní se dotčené testy nebo závislé požadavky snadno přehlédnou a změna zanese defekty.
:::

:::q
Jaký je rozdíl mezi funkční a technickou specifikací?
---
Funkční specifikace popisuje, co musí řešení dělat z pohledu businessu a uživatele: funkce, pravidla, data, obrazovky, požadavky na kvalitu. Technická specifikace popisuje, jak se postaví: architekturu, komponenty, rozhraní, databázi. BA obvykle píše tu první, dodavatel nebo architekt tu druhou.
:::

## Interview corner
:::interview
Tady je požadavek: „The system should respond quickly and be user-friendly.“ Jak bys ho vylepšila?
*EN: Here is a requirement: "The system should respond quickly and be user-friendly." How would you improve it?*
---
- Upozorni, že spojuje dvě témata a používá netestovatelná slova („quickly“, „user-friendly“, „should“).
- Rozděl ho na výkonnostní NFR a požadavek na použitelnost.
- Doplň čísla: odezva do X sekund pro Y % požadavků při zátěži Z.
- Použitelnost zkonkrétni: doba splnění úkolu, chybové hlášky u polí, test s uživateli.
- Zmiň, že čísla bys potvrdila se stakeholdery a s IT, místo abys je vymýšlela.

Typická chyba: nahradit jedno vágní slovo jiným („efficient“, „intuitive“).
:::

:::interview
Co bys dala do funkční specifikace pro externího dodavatele?
*EN: What would you put into a functional specification for an external vendor?*
---
- Řízení dokumentu, kontext a cíl, rozsah a výslovně out of scope.
- Aktéry, TO-BE proces, číslované funkční požadavky s prioritou.
- Business pravidla, UI/wireframy, data dictionary, integrace s ošetřením chyb.
- Měřitelné NFRs, akceptační kritéria a přístup k UAT, otevřené otázky, glosář.
- Zmiň revizi s dodavatelem a sign-off před začátkem vývoje.

Typická chyba: popsat jen seznam funkcí bez rozsahu, NFRs a akceptačních kritérií.
:::

:::interview
Co dělá požadavek dobrým?
*EN: What makes a good requirement?*
---
- Jednoznačný, ověřitelný, atomický, konzistentní, proveditelný, nezbytný, dohledatelný (ISO/IEC/IEEE 29148, IREB).
- Říká co, ne jak, pokud nejde o skutečné omezení.
- Má ID, zdroj a prioritu.
- Uveď jeden špatný a jeden vylepšený příklad.

Typická chyba: vyjmenovat přídavná jména a neukázat, jak je v praxi kontroluješ.
:::

:::interview
Jak řešíš změny požadavků po sign-off?
*EN: How do you handle changes to requirements after sign-off?*
---
- Řízení změn: change request s popisem, důvodem, žadatelem.
- Analýza dopadu pomocí traceability matrix: dotčené požadavky, testy, náklady, harmonogram (s dodavatelem).
- Rozhoduje odpovědná osoba nebo change board; aktualizuje se baseline, verze a log změn.
- V agilním prostředí jde změna do backlogu, ale smluvní rozsah může i tak vyžadovat formální CR.

Typická chyba: potichu upravit dokument a říct to dodavateli mezi dveřmi.
:::

:::interview
Co je traceability matrix a proč bys ji vedla?
*EN: What is a traceability matrix and why would you maintain one?*
---
- Tabulka, která propojuje každý požadavek s jeho zdrojem, business cílem, návrhem a testovacími případy.
- Ukáže neotestované požadavky a požadavky, o které nikdo nežádal.
- Podporuje analýzu dopadu změn a reporting pokrytí v UAT.
- Může to být tabulka v Excelu nebo vazby v nástrojích, jako je Jira a nástroj pro test management.

Typická chyba: říct, že je „jen pro audit“, a nepropojit ji s testováním a dopadem změn.
:::
