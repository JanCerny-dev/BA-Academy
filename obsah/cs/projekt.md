---
title: "Capstone: automatizace žádostí o úvěrový limit v ExportShield Insurance"
---

## Zadání

ExportShield Insurance je fiktivní pojišťovna exportních úvěrů. Exportéři (pojištění) prodávají zboží do zahraničí na fakturu. Než zboží odešlou, žádají ExportShield o **credit limit** (úvěrový limit) na každého zahraničního odběratele: „pojistěte faktury pro Rheinwerk Handels GmbH až do 250 000 EUR“.

Dnes proces vypadá takto:

- Žádosti přicházejí **e-mailem**, jako volný text nebo jako excelová příloha ve třech různých šablonách.
- Asistentka přepisuje data do **PolicyHub** (systém pro správu smluv, který provozuje externí dodavatel **NovaSoft s.r.o.**).
- Underwriter ručně dohledá odběratele ve veřejných registrech (u českých firem v **ARES**), v tabulce zkontroluje riziko země a rozhodne.
- Rozhodnutí jde exportérovi zpět e-mailem. Nikdo nesleduje, jak dlouho to trvalo.

Vedení si stěžuje, že rozhodnutí trvají „asi týden“, že se data přepisují s chybami a že underwriteři tráví čas dohledáváním místo posuzováním. Jako nová IT Business Analyst máš za úkol proces zanalyzovat, navrhnout lepší, specifikovat ho pro NovaSoft a postavit low-code prototyp části příjmu žádostí.

Projekt běží souběžně s moduly. U každého kroku je uvedeno, ke kterému modulu patří. Kroky dělej popořadě; dohromady z nich vznikne tvoje **portfolio** – to, co ukážeš na pohovoru, když se tě někdo zeptá „co jste vlastně udělala?“.

:::warning
Všechno tady je fiktivní. Nepoužívej skutečná data od současného ani žádného jiného zaměstnavatele, ani „anonymizovaná“. Na pohovoru řekni, že jsi portfolio postavila na fiktivním případu, aby firemní data zůstala v bezpečí – tazatelé to berou jako známku dobrého úsudku.
:::

## Kroky a výstupy

:::exercise id="p-01" title="1. Definice problému a mini business case (modul 03)" min="90" tool="Word / Google Docs"
1. Napiš problem statement (definici problému): koho se týká, co se děje, kolik to stojí, jak vypadá „lepší“.
2. Pětkrát se zeptej „proč“ na týdenní dobu rozhodnutí a nakresli fishbone diagram (diagram rybí kosti) možných příčin.
3. Odhadni náklady dnešního procesu s **jasně označenými předpoklady** (např. 6 000 žádostí ročně, 20 minut ruční práce na každou, interní hodinová sazba).
4. Napiš odstavec o tom, co bys měřila před změnou a po ní.

**Hotovo, když:** máš jednu stránku, kterou manažer přečte za tři minuty a pochopí, proč to stojí za to.
:::

:::exercise id="p-02" title="2. Proces AS-IS a TO-BE v BPMN (modul 04)" min="180" tool="demo.bpmn.io"
1. Namodeluj proces AS-IS s pools (bazény) pro Exporter a ExportShield a lanes (dráhami) pro asistentku a underwritera. Pro e-maily použij message flow.
2. Pain points vyznač textovými anotacemi (přepisování, ruční dohledávání, žádné sledování).
3. Namodeluj TO-BE: webový formulář nebo strukturovaný e-mail → automatické vytažení dat → dotaz do ARES (service task) → automatická předběžná pravidla (business rule task) → rozhodnutí underwritera (user task) → automatické oznámení. Přidej **timer boundary event** (hraniční časovač), který eskaluje, když žádost čeká déle než 2 pracovní dny.
4. Oba diagramy exportuj jako PNG a ulož soubory `.bpmn`.

**Hotovo, když:** kolega, který proces nikdy neviděl, ti ho umí převyprávět jen z diagramů.
:::

:::exercise id="p-03" title="3. Stakeholdeři a elicitace (moduly 05 a 16)" min="120" tool="Miro / draw.io"
1. Sepiš stakeholdery (exportér, asistentka, underwriter, vedoucí upisování, IT, NovaSoft, compliance, vedení) a umísti je do mřížky vliv/zájem (power/interest grid).
2. Napiš scénář rozhovoru (10–15 otázek) s underwriterem.
3. Proveď cvičný rozhovor – s kamarádem, nebo s AI asistentem, kterého požádáš, ať hraje underwritera ve fiktivní pojišťovně. Sepiš zápis a vytáhni z něj aspoň 10 kandidátních požadavků.
4. Sestav RACI pro projekt.

**Hotovo, když:** máš mapu stakeholderů, RACI a zápis z rozhovoru s požadavky dohledatelnými k tomu, kdo je řekl.
:::

:::exercise id="p-04" title="4. Funkční specifikace pro dodavatele (modul 06)" min="300" tool="Word / Confluence"
Napiš pro NovaSoft funkční specifikaci změny „Strukturovaný příjem žádostí o úvěrový limit s předběžnou kontrolou v ARES“. Použij šablonu z modulu 06. Musí obsahovat aspoň:
1. Kontext, cíl, rozsah a **out of scope** (co do rozsahu nepatří).
2. Aktéry a proces TO-BE (odkaz na tvůj BPMN).
3. 12–20 funkčních požadavků s ID (FR-01 …), každý testovatelný.
4. Business rules (obchodní pravidla) pro automatickou předběžnou kontrolu (např. odběratel nenalezen v registru → ruční posouzení; riziko země 6–7 → vždy ručně; požadovaná částka nad prahem → senior underwriter).
5. Datové požadavky: pole žádosti, formáty, povinná/nepovinná, validace.
6. 5–8 nefunkčních požadavků s čísly (doba odezvy dotazu do ARES, dostupnost, auditní log, doba uchování dat).
7. Otevřené otázky pro business a pro NovaSoft.

**Hotovo, když:** vývojář z ní umí odhadnout pracnost a tester z ní umí napsat testovací případy, aniž by ti musel volat.
:::

:::exercise id="p-05" title="5. Backlog: epiky, user stories, Gherkin (modul 07)" min="150" tool="Jira Free / Trello"
1. Převeď specifikaci na 1–2 epiky a 8–12 user stories.
2. Ke každé story napiš akceptační kritéria; aspoň 4 z nich v Gherkinu, včetně jednoho Scenario Outline pro předběžná pravidla.
3. Dej stories na nástěnku v Jira Free (nebo Trellu), prioritizuj je metodou MoSCoW (viz moduly 03 a 06) a naplánuj první sprint.
4. Udělej snímek nástěnky do portfolia.

**Hotovo, když:** každá story projde kontrolou INVEST a nástěnka ukazuje realistický první sprint.
:::

:::exercise id="p-06" title="6. Datový model a datový slovník (moduly 08 a 09)" min="120" tool="Mermaid Live / draw.io"
1. Nakresli ER diagram zapojených entit: exportér, smlouva, odběratel, země, žádost o úvěrový limit, rozhodnutí.
2. Napiš data dictionary (datový slovník) pro žádost o úvěrový limit (pole, význam, typ, povinné, zdroj, příklad).
3. Nakresli sekvenční diagram: formulář → PolicyHub → ARES API → PolicyHub → oznámení underwriterovi.
4. Nakresli stavový diagram žádosti o úvěrový limit (Requested → In review → Approved / Reduced / Rejected, plus Withdrawn).

**Hotovo, když:** všechny tři diagramy sedí navzájem i se specifikací.
:::

:::exercise id="p-07" title="7. SQL: změř problém a zkontroluj data (modul 10)" min="150" tool="SQL lab"
V [SQL labu](sql.html) napiš dotazy, které odpovědí na:
1. Kolik úvěrových limitů bylo požadováno v každém měsíci a kolik z nich bylo rozhodnuto?
2. Průměrný a maximální počet dní od žádosti po rozhodnutí, podle underwritera.
3. Podíl schválených, snížených a zamítnutých žádostí podle rizikové kategorie země odběratele.
4. Jaké problémy s kvalitou dat existují (rozhodnuto dřív, než bylo požádáno, chybějící země odběratele, duplicitní čísla faktur, škody na zaplacené faktury)?
5. Celková schválená expozice podle země.

Ke každému dotazu ulož jednovětou business interpretaci výsledku.

**Hotovo, když:** umíš s čísly říct, jak pomalý je současný proces a kde jsou data nespolehlivá.
:::

:::exercise id="p-08" title="8. Specifikace integrace a kolekce v Postmanu (modul 11)" min="180" tool="Postman / API lab"
1. Zavolej ARES pro tři české firmy (v [API labu](api.html) nebo v Postmanu). Odpovědi si ulož.
2. Napiš tabulku mapování polí: pole ARES → pole odběratele v PolicyHub → transformace → povinné?
3. Popiš ošetření chyb: firma nenalezena (404), ARES nedostupný (timeout / 5xx), neplatný formát IČO (400).
4. Postav v Postmanu kolekci s požadavky na ARES a jednoduchými testy (stav je 200, pole `ico` existuje).
5. Volitelně: napiš malý popis v OpenAPI pro interní endpoint „pre-check“, který má NovaSoft postavit.

**Hotovo, když:** integrační část tvé specifikace je tak přesná, že dodavatel nemá k polím ani chybám žádné otázky.
:::

:::exercise id="p-09" title="9. Testovací případy a plán UAT (modul 13)" min="150" tool="Excel / Google Sheets"
1. Napiš 12–15 testovacích případů z požadavků a akceptačních kritérií, včetně hraničních hodnot (prahy částek) a rozhodovací tabulky pro předběžná pravidla.
2. Napiš jednostránkový plán UAT: rozsah, účastníci, testovací data, vstupní a výstupní kritéria, harmonogram, sign-off.
3. Napiš dva ukázkové defect reporty, jako by byly nalezené v UAT (jeden s vysokou severity, jeden kosmetický).

**Hotovo, když:** každý funkční požadavek pokrývá aspoň jeden testovací případ (ukaž to v malé tabulce traceability).
:::

:::exercise id="p-10" title="10. Low-code prototyp příjmu žádostí (modul 14)" min="300" tool="Make (free) / Power Automate"
Postav funkční prototyp části příjmu žádostí:
1. Trigger: webový formulář (webhook v Make, Microsoft Forms nebo Google Forms) s exportérem, IČO odběratele, částkou a měnou.
2. Zavolej ARES API s IČO; rozvětvi podle nalezen / nenalezen.
3. Použij jedno nebo dvě jednoduchá předběžná pravidla (např. částka nad 500 000 → označit pro seniorního underwritera).
4. Zapiš řádek do tabulky (náhrada za PolicyHub) s žádostí, názvem firmy z ARES a výsledkem předběžné kontroly.
5. Pošli žadateli potvrzovací e-mail.
6. Napiš jednostránkový run-book (provozní příručku): trigger, kroky, ošetření chyb, vlastník, jak automatizaci vypnout.

**Hotovo, když:** umíš ji za dvě minuty předvést naživo – odešleš formulář a ukážeš, jak se objeví řádek a e-mail.
:::

:::exercise id="p-11" title="11. Use case pro AI: třídění dokumentů (modul 15)" min="120" tool="ChatGPT / Claude / Copilot"
Exportéři k žádostem často přikládají účetní výkazy a smlouvy. Navrhni krok s pomocí AI, který přílohy roztřídí a vytáhne klíčová čísla.
1. Popiš změnu procesu a místo, kde člověk výstup AI kontroluje.
2. Definuj metriky úspěchu a akceptační kritéria pro pravděpodobnostní výstup (např. aspoň 95 % správně určených typů dokumentů na testovací sadě 50 fiktivních dokumentů).
3. Sestav evaluační tabulku 10 testovacích vstupů (fiktivních) s očekávanými výstupy, projeď je AI asistentem a zaznamenej výsledky.
4. Vypiš rizika (důvěrná data, chyby, zkreslení, regulace) a kontrolní opatření.

**Hotovo, když:** máš jednostránkový canvas AI use case a k němu evaluační tabulku.
:::

:::exercise id="p-12" title="12. Prezentace a status report (modul 16)" min="150" tool="PowerPoint / Google Slides"
1. Připrav pro vedení prezentaci o 7–10 slidech: problém → AS-IS → TO-BE → přínosy (čísla z kroků 1 a 7) → demo prototypu → plán → co od nich potřebuješ.
2. Nahraj se, jak ji za 10 minut prezentuješ.
3. Napiš jeden týdenní status report (RAG status, hotovo, dál, rizika, potřebná rozhodnutí), jako by projekt byl v 6. týdnu.

**Hotovo, když:** záznam je kratší než 10 minut a bez obav bys ho ukázala hiring manažerovi.
:::

:::exercise id="p-13" title="13. Portfolio (modul 17)" min="180" tool="PDF / Notion / GitHub Pages"
Vyber nejlepší části do portfolia o 8–12 stranách nebo na jednu webovou stránku: definice problému, BPMN AS-IS/TO-BE, výňatek ze specifikace, 3 user stories s Gherkinem, ER a sekvenční diagram, 3 SQL dotazy se zjištěními, snímek kolekce v Postmanu, demo automatizace (snímky nebo krátké video), plán UAT a prezentace.

Nahoru přidej odstavec „Co bych ve skutečné firmě udělala jinak“ – schvalování, bezpečnostní posouzení, smlouva s dodavatelem, řízení změny.

**Hotovo, když:** umíš tazatele portfoliem provést za 5 minut a jít do hloubky u kterékoli části, kterou si vybere.
:::

## Jak to odpovídá inzerátu

| Inzerát říká | Krok capstonu |
|---|---|
| Přebírat požadavky na změny od oddělení, psát technické specifikace pro dodavatele | 3, 4, 8 |
| Navrhovat nové funkce a optimalizovat systémy v souladu s architekturou | 2, 6, 8 |
| Spolupracovat s IT dodavateli a stakeholdery | 3, 4, 12 |
| Podporovat testery, testovat dodávky, reportovat stav | 9, 12 |
| Automatizace v low-code platformách | 10 |
| Prezentovat výstupy, školit kolegy | 12 |
| Integrace AI do interních procesů | 11 |
| Základní SQL, API, JSON/XML | 7, 8 |
| UML nebo BPMN | 2, 6 |
