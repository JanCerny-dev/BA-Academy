---
id: 01
slug: ba-role
title: Role IT business analytika
phase: A
priority: P1
quick_min: 5
deep_min: 30
job_ad: "general"
---

## Why this matters
Než se pustíš do jakékoli techniky, potřebuješ jasnou představu o samotné práci: za co je business analytik placený, co vytváří a s kým spolupracuje. Každý pohovor na pozici IT Business Analyst začíná nějakou variantou otázek „Co dělá BA?“ a „Proč jím chcete být?“. Tento modul ti dá slovník, abys uměla odpovědět na obě, a ukáže, že velká část toho, co už v práci děláš, má formální název.

## Quick version
**Business analyst (BA)** (business analytik) pomáhá organizaci měnit se tak, aby změna přinesla hodnotu. V praxi stojí IT business analytik mezi lidmi, kteří mají business potřebu (underwriteři, likvidátoři škod, finance, vedení), a lidmi, kteří IT systémy staví nebo konfigurují (vývojáři, testeři, architekti, externí dodavatelé). BA hlídá, aby obě strany myslely totéž.

**Co BA dělá, jednou větou:** zjistí, jaký problém business doopravdy má, popíše, co musí řešení dělat, ve formě, kterou IT umí postavit a otestovat, a ověří, že dodaná věc problém opravdu řeší.

**Typické činnosti:**
- Mluví se **stakeholdery** (každý, koho změna zasáhne nebo kdo ji může ovlivnit), aby pochopil problém. Tomu se říká **elicitation** (získávání požadavků).
- Modeluje současný (**AS-IS**) a budoucí (**TO-BE**) proces.
- Píše **requirements** (požadavky): co musí systém dělat (funkční) a jak dobře (nefunkční, například rychlost nebo bezpečnost).
- Převádí požadavky na **user stories** (uživatelské příběhy) s **acceptance criteria** (akceptačními kritérii), nebo do **specifikace** pro dodavatele.
- Odpovídá na otázky vývojářů a testerů, reviduje testovací případy, podporuje **UAT** (user acceptance testing, akceptační testování, při kterém business uživatelé potvrdí, že jim řešení funguje).
- Řeší **change requests** (změnové požadavky), když se mění rozsah, a reportuje stav.

**Typy analytiků.** Názvy pozic se hodně překrývají. *Business analyst* se zaměřuje na potřeby a procesy. *IT business analyst* k tomu přidává převod do systémových požadavků. *Systems analyst* (systémový analytik) jde hlouběji do technického návrhu (data, rozhraní). *Process analyst* (procesní analytik) se soustředí na to, jak práce teče. *Data analyst* pracuje s daty a reporty. *Product owner* ve Scrumu určuje pořadí backlogu a odpovídá za hodnotu produktu. *Project manager* odpovídá za čas, rozpočet a dodávku. V malých týmech jeden člověk často dělá dvě nebo tři z těchto rolí.

**BABOK v3** (*Business Analysis Body of Knowledge*, vydává IIBA) je hlavní referenční příručka oboru. Zhruba popisuje:
- **6 knowledge areas** (znalostních oblastí): plánování a řízení BA práce; elicitace a spolupráce; řízení životního cyklu požadavků; strategická analýza; analýza požadavků a definice návrhu; vyhodnocení řešení.
- **4 typy požadavků**: business, stakeholder, solution (funkční a nefunkční) a transition (přechodové) požadavky.
- **6 základních pojmů (BACCM)**: Change, Need, Solution, Stakeholder, Value, Context. Každou BA situaci jde popsat těmito šesti slovy.

**Myšlení analytika:** ptej se „proč?“ dřív než „jak?“; drž problém odděleně od navrhovaného řešení; přepínej mezi detailem (jedno pole ve formuláři) a celkovým obrazem (celý proces a jeho náklady).

**Kde BA pracují na českém trhu:** interně v bankách, pojišťovnách a automotive (zastupuješ business uvnitř firmy); na straně dodavatele v softwarových firmách (píšeš specifikace a odhaduješ práci pro klienta); a v konzultačních firmách (krátké projekty pro mnoho klientů).

**Část toho už děláš.** Pokud sis někdy všimla pomalého procesu, navrhla jeho automatizaci, probrala to s IT, získala schválení a výsledek otestovala, udělala jsi identifikaci problému, návrh řešení, práci se stakeholdery, sign-off i akceptační testování. Modul ukazuje toto přiřazení, abys na pohovoru uměla popsat svou zkušenost jazykem BA.

## Deep dive

### K čemu je business analytik [P1]
Organizace se mění neustále: nové produkty, nová regulace, nové systémy, tlak na náklady. Každá změna stojí peníze a nese riziko. Business analytik existuje proto, aby se peníze utratily za správnou změnu a aby ta změna fungovala.

Jednoduše se dá role vidět jako **most**. Na jedné straně je business: lidé, kteří znají pojištění, riziko a klienty, ale ne databáze nebo API. Na druhé straně je IT: lidé, kteří znají systémy, ale nevědí, proč rozhodnutí o úvěrovém limitu potřebuje rating země. Každá strana mluví svým slovníkem. Bez mostu IT postaví to, co *slyšelo*, ne to, co business *potřeboval*.

Příklad z ExportShield Insurance: oddělení škod říká „potřebujeme, aby byl ClaimDesk rychlejší“. Vývojář by mohl optimalizovat databázové dotazy. BA se zeptá, co „rychlejší“ znamená. Ukáže se, že likvidátoři tráví dvě hodiny na každé škodě přepisováním údajů z faktur v PDF přílohách do ClaimDesku. Skutečná potřeba je přestat data přepisovat, ne zrychlit databázi. Právě v tomhle rozdílu je hodnota BA.

### Typy analytiků a příbuzné role [P1]
Názvy pozic nejsou standardizované. Čti popis práce, ne jen titulek. Tabulka ukazuje typické zaměření.

| Role | Hlavní otázka | Typické výstupy | Technická hloubka |
|---|---|---|---|
| Business analyst | Co business potřebuje a proč? | Business case, popis problému, business požadavky, procesní mapy | Nízká až střední |
| IT business analyst | Co musí systém dělat, aby tu potřebu splnil? | Funkční a nefunkční požadavky, user stories, specifikace pro dodavatele | Střední |
| Systems analyst | Jak přesně se bude systém chovat a jak se napojí? | Datové modely, specifikace rozhraní, mapování API | Střední až vysoká |
| Process analyst | Jak práce teče a kde se ztrácí? | BPMN modely, procesní metriky, návrhy zlepšení | Nízká až střední |
| Data analyst | Co říkají data? | Reporty, dashboardy, SQL dotazy, zjištění o kvalitě dat | Střední až vysoká |
| Product owner (Scrum) | Co postavit jako další, aby hodnota byla co největší? | Seřazený product backlog, product goal, rozhodnutí o přijetí | Nízká až střední |
| Project manager | Dodáme včas a v rozpočtu? | Plán, rozpočet, registr rizik, status reporty | Nízká |

**Překryvy, které uvidíš v praxi:**
- V agilních týmech BA často píše stories a **product owner** je pak prioritizuje. V menších týmech BA *je* product owner.
- IT BA v bance často dělá i systémovou analýzu: mapuje pole mezi dvěma systémy, píše specifikaci API.
- Na malých projektech BA píše i status report a vede schůzky, což je práce projektového manažera.

Cílový inzerát tohoto kurzu míchá IT BA, systémovou analýzu (API, JSON/XML, SQL), procesní analýzu (BPMN) a trochu low-code automatizace. Taková kombinace je ve středně velkých organizacích běžná.

### Typické výstupy [P1]
**Deliverable** (výstup) je něco konkrétního, co předáš. Ne každý projekt potřebuje všechny.

| Výstup | Co to je | Kdo ho používá |
|---|---|---|
| Problem statement (popis problému) | Pár vět: co je špatně, pro koho, dopad, jak vypadá úspěch | Sponzor, tým |
| Business case | Náklady, přínosy, rizika, doporučení | Vedení, schvalovatelé |
| Mapa stakeholderů | Kdo je zapojený, vliv, zájem | BA, projektový manažer |
| AS-IS / TO-BE model procesu | Diagramy, často v BPMN 2.0 | Business, IT, testeři |
| Business requirements document (BRD) nebo seznam požadavků | Číslované požadavky s prioritou | Všichni |
| User stories s akceptačními kritérii | Malé kusy práce v backlogu | Vývojáři, testeři |
| Funkční specifikace | Detailní chování: obrazovky, pravidla, validace, rozhraní | Dodavatel, vývojáři |
| Datové mapování / specifikace rozhraní | Které pole kam jde, formáty (JSON, XML) | Vývojáři, integrátoři |
| Traceability matrix (matice sledovatelnosti) | Propojuje každý požadavek s návrhem, testy a defekty | BA, test lead, auditoři |
| Change request | Zdokumentovaná změna dohodnutého rozsahu i s dopadem | Dodavatel, projektový manažer |
| Podklady pro UAT | Testovací scénáře, testovací data, záznam o sign-offu | Business testeři |
| Školicí materiály, release notes | Jak novou funkci používat | Koncoví uživatelé |

V regulovaných oborech (bankovnictví, pojišťovnictví) záleží na papírové stopě. Auditoři se mohou ptát, kdo požadavek schválil a jak byl otestován. Záznamy o **traceability** (sledovatelnosti) a **sign-offu** (formálním schválení) jsou součást práce, ne byrokracie pro byrokracii.

### Jeden týden v práci [P2]
Ilustrativní týden IT BA v ExportShield, který pracuje na automatizaci příjmu škod s externím dodavatelem NovaSoft s.r.o.:

- **Pondělí.** Daily stand-up s dodávkovým týmem (15 minut). Projdeš dvě otázky vývojářů z NovaSoftu, jak počítat částku plnění, když část faktury už byla zaplacena. Ověříš business pravidlo s vedoucím likvidace, aktualizuješ specifikaci a odpovíš v Jiře.
- **Úterý.** 90minutový workshop se třemi likvidátory, na kterém projdete TO-BE proces. Zjistíš, že dokumenty ke škodám nad určitou částkou potřebují druhého schvalovatele. Přidáš požadavek a označíš ho, že potřebuje sign-off.
- **Středa.** Napíšeš pět user stories na další sprint, každou s akceptačními kritérii. Spustíš krátký SQL dotaz nad testovací databází, abys zjistila, jaké stavy škod existují, protože na nich story závisí.
- **Čtvrtek.** Backlog refinement s product ownerem a vývojáři. Jedna story je moc velká, tak ji rozdělíš. Dodavatel vyhodnotí, že nové pole v PolicyHubu je mimo dohodnutý rozsah; zakládáš change request.
- **Pátek.** Kontroluješ testovací případy, které tester napsal podle akceptačních kritérií. Pomáháš business uživateli projít UAT scénáře pro předchozí release. Odešleš týdenní status report: zelená pro rozsah, oranžová pro harmonogram kvůli change requestu.

Všimni si poměru: velká část času jsou rozhovory a vyjasňování, menší část psaní dokumentů. Junioři často čekají opak.

### BABOK v3 v hrubých rysech [P2]
BABOK v3 (IIBA, 2015) je soubor znalostí, ne metoda. Popisuje, *co* business analýza zahrnuje, ne pevné pořadí kroků. Na juniorskou pozici ho nemusíš umět nazpaměť, ale jeho slovník se objevuje na pohovorech a v certifikacích jako ECBA nebo CCBA.

**Šest knowledge areas** (skupin úloh), jednoduše řečeno:

1. **Business Analysis Planning and Monitoring** — rozhodnutí, jak budeš na tomto projektu analýzu dělat: kteří stakeholdeři, jaké techniky, jak se budou požadavky schvalovat a měnit.
2. **Elicitation and Collaboration** — získávání informací od lidí a z dokumentů (rozhovory, workshopy, pozorování) a potvrzení, že jsi je pochopila správně.
3. **Requirements Life Cycle Management** — péče o požadavky od vzniku po vyřazení: sledování vazeb, prioritizace, schvalování, řízení změn.
4. **Strategy Analysis** — pochopení současného stavu, definice požadovaného budoucího stavu a mezery a rizik mezi nimi. Tady žije business case.
5. **Requirements Analysis and Design Definition** — strukturování a modelování požadavků, kontrola jejich kvality a popis možných návrhů řešení.
6. **Solution Evaluation** — ověření, zda dodané řešení opravdu přináší očekávanou hodnotu, a pokud ne, proč.

**Čtyři typy požadavků:**

| Typ | Význam | Příklad z ExportShield |
|---|---|---|
| Business requirement | Cíl organizace | Zkrátit průměrnou dobu vyřízení škody z 15 na 7 pracovních dnů |
| Stakeholder requirement | Potřeba konkrétní skupiny | Likvidátoři potřebují mít údaje z faktur k dispozici bez přepisování |
| Solution requirement — funkční | Co systém dělá | ClaimDesk vytáhne číslo faktury, datum a částku z nahraného PDF |
| Solution requirement — nefunkční | Jak dobře to systém dělá | Vytěžení skončí do 30 sekund u desetistránkového PDF |
| Transition requirement | Potřebný jen pro přechod ze starého stavu do nového | Před spuštěním převést otevřené škody z excelového přehledu do ClaimDesku |

(Čísla v příkladech jsou ilustrativní.)

**Šest základních pojmů (BACCM — Business Analysis Core Concept Model)**, jednoduše řečeno:

- **Change** (změna) — akt přeměny. Potom bude něco jinak.
- **Need** (potřeba) — problém nebo příležitost, která ke změně motivuje.
- **Solution** (řešení) — konkrétní způsob, jak potřebu uspokojit.
- **Stakeholder** — osoba nebo skupina, která má vztah ke změně, potřebě nebo řešení.
- **Value** (hodnota) — užitečnost nebo význam něčeho pro stakeholdera. Mohou to být peníze, čas, nižší riziko, soulad s regulací.
- **Context** (kontext) — okolnosti, které změnu ovlivňují a jsou jí ovlivňovány: regulace, kultura, existující systémy, trh.

Pojmy se hodí jako kontrolní seznam. Když nedokážeš říct, co je *potřeba*, nebo pro kterého *stakeholdera* vzniká *hodnota*, iniciativa není připravená.

### Myšlení analytika [P1]
Techniky se dají naučit z knihy. Tyto návyky chtějí praxi.

**Ptej se „proč?“ dřív než „jak?“.** Požadavky většinou přicházejí jako řešení: „přidejte tlačítko“, „pošlete e-mail“, „kupte nástroj“. Zeptej se, co se děje dnes, co se kazí a co by se změnilo, kdyby se požadavek splnil. Uvedené řešení často není to nejlepší.

**Odděl problém, symptom a řešení.** „Škody se vyřizují pozdě“ je symptom. „Údaje z faktur se ručně přepisují z PDF a každá třetí škoda čeká na chybějící dokumenty“ je blíž problému. „Kupme nástroj na OCR“ je jedno z možných řešení. Podrobně to probírá modul o analýze problému a procesů.

**Drž detail a celkový obraz současně.** V jednu chvíli kontroluješ, jestli datum faktury může být v budoucnosti; vzápětí vysvětluješ vedoucí likvidace, jak změna ovlivní celý proces. Dobrý BA přibližuje a oddaluje záměrně.

**Buď neutrální.** Zastupuješ potřebu, ne jedno oddělení nebo dodavatele. Když underwriting a likvidace chtějí různé věci, zviditelníš kompromis a necháš rozhodnout toho, kdo rozhoduje.

**Zapisuj a nech si potvrdit.** Požadavek, který existuje jen na schůzce, není požadavek. Shrň, pošli, získej potvrzení.

**Řekni „ještě nevím, zjistím to“.** Tazatelé to mají rádi. Hádání u business pravidel plodí defekty.

### Kde BA pracují na českém trhu [P2]
Stejný název pozice může znamenat různou práci podle toho, na které straně stolu sedíš.

| Prostředí | Kdo tě platí | Typická práce | Výhody | Nevýhody |
|---|---|---|---|---|
| Interně (banka, pojišťovna, automotive, investiční skupina) | Organizace, která systém používá | Sbírat potřeby od oddělení, psát specifikace pro dodavatele, přebírat dodávky, vést UAT | Hluboká znalost oboru, dlouhodobý pohled, vidíš výsledek v provozu | Pomalejší tempo, víc vnitřní politiky, mnoho dodavatelů ke koordinaci |
| Strana dodavatele (softwarová firma, systémový integrátor) | Klient, přes smlouvu | Převádět požadavky klienta na návrhy, odhadovat, vyjasňovat s klientem, podporovat dodávku | Silný kontakt s technikou, mnoho projektů | Spory o rozsah, change requesty, tlak klienta |
| Konzultační firma | Klienti, obvykle krátké zakázky | Posouzení, přepracování procesů, výběr softwaru, regulatorní projekty | Rozmanitost, rychlé učení | Cestování, krátký kontakt s výsledky, vysoká očekávání |

Banky a pojišťovny v Česku často kupují klíčové systémy od externích dodavatelů a roli BA si drží interně, aby měly kontrolu nad tím, co objednávají. To odpovídá cílovému inzerátu: „požadavky od oddělení → technické specifikace pro dodavatele“. Automotive firmy mají mnoho BA rolí v IT pro výrobu, logistiku a prodej, často v anglicky mluvících týmech. Regulovaní klienti (bankovnictví, pojišťovnictví) přidávají požadavky na bezpečnost, auditní stopu a ochranu dat, které musí BA zachytit jako nefunkční požadavky.

### Co už děláš a jak se tomu říká [P1]
Pokud jsi v práci zlepšovala procesy bez toho titulu, máš relevantní zkušenost. Klíčové je popsat ji jazykem BA a být poctivá, pokud jde o rozsah.

| Co už děláš | Jak se tomu říká | Oblast BABOK |
|---|---|---|
| Všimneš si, že úkol trvá moc dlouho nebo způsobuje chyby | Identifikace problému, analýza pain pointů | Strategy Analysis |
| Spočítáš, jak často se to děje a jak dlouho to trvá | Měření procesu, výchozí stav (baseline) | Strategy Analysis |
| Ptáš se kolegů, jak to dělají | Elicitace (rozhovory, pozorování) | Elicitation and Collaboration |
| Načrtneš kroky na papír | Modelování AS-IS procesu (popis současného stavu) | Strategy Analysis |
| Navrhneš „tohle by šlo automatizovat“ | Návrh řešení, TO-BE proces, business case | Strategy Analysis |
| Vysvětlíš IT, co potřebuješ | Specifikace požadavků | Requirements Analysis and Design Definition |
| Domluvíš se s vedoucím, že to stojí za to | Zapojení stakeholderů, schválení, sign-off | Requirements Life Cycle Management (schválení); zapojení stakeholderů se plánuje v Planning and Monitoring |
| Odpovídáš na otázky IT, zatímco to staví | Vyjasňování a správa požadavků | Requirements Life Cycle Management |
| Vyzkoušíš to, než to jde do provozu | User acceptance testing (UAT) | Solution Evaluation |
| Ukážeš kolegům, jak to používat | Školení, podpora přechodu | Transition requirements (Requirements Analysis and Design Definition) |
| Později ověříš, že to opravdu šetří čas | Realizace přínosů, vyhodnocení řešení | Solution Evaluation |

Na pohovoru se vyhni větě „jen jsem trochu pomáhala s IT“. Řekni místo toho: „Identifikovala jsem ruční krok v našem procesu škod, zhruba změřila, kolik času zabírá, navrhla automatizaci, dohodla požadavky s IT a před spuštěním to otestovala.“ Pak přidej jeden konkrétní detail. Nepřeháněj: pokud specifikaci psalo IT, řekni, že jsi do ní dodávala podklady.

### Co BA není [P3]
Vyjasnit omyly pomáhá na pohovorech:
- **Není zapisovatel požadavků.** Zapsat, co lidé říkají, není analýza. Analýza znamená zpochybňovat, strukturovat a hledat mezery.
- **Není ten, kdo rozhoduje.** Rozhoduje sponzor nebo product owner. BA rozhodnutí připravuje.
- **Není vývojář.** API, datům a SQL musíš rozumět natolik, abys uměla specifikovat a kontrolovat, ne psát produkční kód. Low-code automatizace je šedá zóna a cílový inzerát ji do jisté míry očekává.
- **Není tester.** Ale s testery úzce spolupracuješ a v menších týmech můžeš testovat sama.

## Key terms
- **Business analyst (BA)** (business analytik) — člověk, který identifikuje potřeby a definuje změny, jež přinášejí stakeholderům hodnotu.
- **Stakeholder** (zainteresovaná strana) — jakákoli osoba nebo skupina, kterou změna zasáhne nebo která ji může ovlivnit.
- **Elicitation** (elicitace, získávání požadavků) — získávání informací od stakeholderů a z dalších zdrojů, například rozhovory nebo workshopy.
- **Requirement** (požadavek) — zdokumentované vyjádření potřeby nebo schopnosti, kterou řešení musí mít.
- **Business requirement** (business požadavek) — cíl organizace na vysoké úrovni, který změnu ospravedlňuje.
- **Stakeholder requirement** (požadavek stakeholdera) — potřeba konkrétní skupiny stakeholderů, most mezi business a solution požadavky.
- **Solution requirement** (požadavek na řešení) — schopnost (funkční) nebo kvalita (nefunkční), kterou řešení musí mít.
- **Transition requirement** (přechodový požadavek) — dočasný požadavek potřebný jen pro přechod ze současného do budoucího stavu, například migrace dat.
- **BABOK v3** — Business Analysis Body of Knowledge od IIBA, hlavní referenční příručka oboru.
- **BACCM** — Business Analysis Core Concept Model: Change, Need, Solution, Stakeholder, Value, Context.
- **AS-IS / TO-BE** (současný / budoucí stav) — současný stav procesu a zamýšlený budoucí stav.
- **Deliverable** (výstup) — konkrétní výstup předaný někomu dalšímu, například specifikace nebo model procesu.
- **Sign-off** (formální schválení) — formální schválení výstupu oprávněným stakeholderem.
- **Traceability** (sledovatelnost) — schopnost dohledat u požadavku jeho zdroj, návrh, testy a defekty.
- **Product owner** — odpovědnost (accountability) ve Scrumu za maximalizaci hodnoty produktu a řazení product backlogu.
- **UAT (user acceptance testing)** (uživatelské akceptační testování) — testování business uživateli, které před spuštěním potvrdí, že řešení splňuje jejich potřeby.
- **Pain point** (bolavé místo) — konkrétní problém nebo frustrace v současném procesu.

## Hands-on
:::exercise id="m01-e1" title="Přiřaď své vlastní zlepšení k životnímu cyklu BA" min="45" tool="draw.io"
**Cíl:** popsat jedno zlepšení, které jsi v práci iniciovala, jazykem BA, připravené na pohovor.

1. Vyber jedno zlepšení, které jsi vedla nebo ke kterému jsi přispěla (automatizace, nový formulář, změněný schvalovací tok). Vynech jména klientů, částky a jakákoli interní data. Používej obecná slova jako „měsíční report“ nebo „žádost o schválení“.
2. Otevři [draw.io](https://app.diagrams.net/) a nakresli sedm obdélníků v řadě: Problem identified → Measured → Proposed solution → Agreed requirements → Approval → Testing → Rollout and evaluation.
3. Pod každý obdélník napiš jednu nebo dvě věty o tom, co jsi v té fázi opravdu dělala. Pokud jsi fázi přeskočila, napiš „přeskočeno“ a proč.
4. Pod každý obdélník doplň formální termín z tabulky „Co už děláš a jak se tomu říká“.
5. Napiš pětivětné shrnutí ve formátu STAR (Situation, Task, Action, Result a jedno poučení).

**Hotovo, když:** máš diagram a pětivětný příběh, který dokážeš nahlas říct za méně než 90 sekund, bez důvěrných informací.
:::

:::exercise id="m01-e2" title="Ohodnoť se podle cílového inzerátu" min="40" tool="Excel or Google Sheets"
**Cíl:** znát své mezery a naplánovat, které moduly studovat jako první.

1. Vytvoř tabulku se sloupci: Požadavek, Můj doklad, Hodnocení 0–3, Modul, který to pokrývá (doplň z přehledu kurzu).
2. Každou položku z cílového inzerátu zadej jako řádek: požadavky od oddělení → technické specifikace pro dodavatele; návrh funkcí v souladu s architekturou; spolupráce s dodavateli a stakeholdery; podpora testerů a testování dodávek; reporting stavu; low-code automatizace; prezentace a školení; AI v procesech; logické myšlení; základní SQL; API, JSON/XML; algoritmizace (programování / low-code / technická zadání); UML nebo BPMN; prezentování.
3. Ohodnoť se: 0 = nikdy jsem o tom neslyšela, 1 = znám pojem, 2 = dělala jsem to s pomocí, 3 = dělala jsem to sama.
4. U každého hodnocení 0 nebo 1 najdi modul tohoto kurzu, který to pokrývá.
5. Vyber tři položky s nejnižším hodnocením. To jsou tvoje první studijní priority.

**Hotovo, když:** každý řádek má hodnocení a doklad (nebo „zatím nic“) a máš seznam tří priorit.
:::

:::exercise id="m01-e3" title="Připrav si informační rozhovor s praktikujícím BA" min="60" tool="LinkedIn"
**Cíl:** slyšet od praktikujícího BA, jak práce vypadá ve skutečnosti.

1. Na LinkedInu najdi 3–5 lidí, kteří mají v pozici „Business Analyst“ a pracují v bance, pojišťovně nebo u softwarového dodavatele. Přednost dej lidem o jeden dva kroky před tebou, ne seniorním manažerům.
2. Pošli krátkou, zdvořilou zprávu: kdo jsi (měníš kariéru a zajímá tě BA), o co žádáš (20 minut online) a že nežádáš o práci. Drž ji pod 400 znaků.
3. Připrav 8 otázek. Návrh: Co jste dělal/a minulý týden? Které výstupy píšete nejčastěji? Jaké nástroje? Kolik práce se SQL nebo API? Jak jste získal/a první BA pozici? V čem junioři chybují? Co byste se učil/a jako první? Je něco, co byste už znovu nedělal/a?
4. Po rozhovoru napiš půlstránkové shrnutí a porovnej ho se sekcí „Jeden týden v práci“ výše.
5. Ještě týž den pošli poděkování.

**Hotovo, když:** máš připravenou zprávu, seznam otázek a (jakmile někdo souhlasí) písemné shrnutí. Během rozhovoru nesdílej nic důvěrného od svého zaměstnavatele.
:::

## Self-check
:::q
Kolega říká: „BA jen zapíše, co business chce, a pošle to do IT.“ Co v tom popisu chybí?
---
Chybí v něm analýza. BA požadavek zpochybní, aby našel skutečnou potřebu, porovná ji s potřebami ostatních stakeholderů, strukturuje požadavky, hledá mezery a rozpory a později ověří, že dodané řešení funguje. Zápis je jen výstup; hodnota je v dotazování a strukturování, které mu předchází.
:::

:::q
Jaký je praktický rozdíl mezi IT business analytikem a product ownerem?
---
IT BA se soustředí na pochopení potřeb a na detailní popis toho, co musí řešení dělat (požadavky, stories, specifikace). Product owner odpovídá za hodnotu produktu a rozhoduje o pořadí backlogu. V mnoha týmech BA připravuje a zpřesňuje položky backlogu a PO je prioritizuje; v malých týmech může obojí dělat jeden člověk.
:::

:::q
Zařaď tento požadavek: „Před spuštěním musí být všechny otevřené škody z excelového přehledu nahrané do ClaimDesku.“
---
Je to transition requirement (přechodový požadavek). Je potřeba jen pro přechod ze současného do budoucího stavu a po dokončení migrace nemá smysl. Přesto potřebuje vlastníka, akceptační kritéria a testování.
:::

:::q
Vyjmenuj šest základních pojmů BACCM a použij je na automatizaci příjmu žádostí o úvěrový limit v ExportShield.
---
Change: žádosti se už nepřepisují ručně. Need: underwriteři ztrácejí čas přepisováním a dělají chyby. Solution: webový formulář, který plní PolicyHub přímo. Stakeholders: exportéři, underwriteři, IT, NovaSoft. Value: kratší doba odezvy, méně chyb. Context: regulovaná pojišťovna, systém externího dodavatele, zavedené e-mailové zvyky klientů.
:::

:::q
Proč si banky a pojišťovny v Česku často drží roli BA interně, i když systém staví dodavatel?
---
Protože potřebují někoho, kdo zastupuje zájmy organizace a zná její procesy a regulaci. Interní BA definuje, co se objednává, kontroluje, jak dodavatel věci pochopil, řeší change requesty a přebírá dodávku. Nechat to všechno na dodavateli vytváří střet zájmů a slabou kontrolu nad rozsahem.
:::

:::q
Manažer tě požádá, abys „přidala do ClaimDesku tlačítko pro export“. Co uděláš jako první a proč?
---
Zeptáš se, proč je export potřeba a co se s exportovanými daty dnes děje. Požadavek je řešení; skrytou potřebou může být report, datový tok pro jiný tým nebo požadavek auditu. Jakmile je potřeba jasná, tlačítko pro export může být pořád správně, nebo může potřebu lépe obsloužit plánovaný report.
:::

## Interview corner
:::interview
Co dělá business analytik?
*EN: What does a business analyst do?*
---
- Most mezi businessem a IT: pochopit potřebu, popsat řešení, ověřit, že bylo dodáno.
- Zmiň konkrétní činnosti: elicitace, modelování procesů, požadavky a user stories, podpora testování a UAT, řízení změn.
- Dej jeden krátký příklad (z vlastní zkušenosti, v termínech BA).
- Zmiň hodnotu: správná změna, správně provedená, šetří peníze a snižuje riziko.

Typická chyba: popsat BA jako zapisovatele nebo malého projektového manažera bez zmínky o analýze.
:::

:::interview
Nemáte formálně pozici BA. Proč bychom vás měli přijmout?
*EN: You have no formal BA job title. Why should we hire you?*
---
- Přiřaď svou současnou práci k činnostem BA: identifikace problému, návrh, dohoda s IT, schválení, testování.
- Dej jeden STAR příběh s měřitelným nebo aspoň konkrétním výsledkem.
- Ukaž, co jsi udělala pro zaplnění mezer: tento kurz, vyzkoušené nástroje (BPMN, SQL, Jira), případová studie v portfoliu.
- Znalost oboru: rozumíš pojištění, schvalovacím procesům a regulovanému prostředí.

Typická chyba: omlouvat se za nedostatek zkušeností místo toho, abys přeložila zkušenosti, které máš.
:::

:::interview
Jaký je rozdíl mezi business požadavkem a funkčním požadavkem?
*EN: What is the difference between a business requirement and a functional requirement?*
---
- Business požadavek: cíl organizace, například kratší doba vyřízení škody.
- Funkční požadavek: konkrétní chování řešení, například vytěžení údajů z nahraného PDF faktury.
- Vysvětli řetězec: business → stakeholder → solution (funkční a nefunkční), plus přechodové požadavky.
- Jeden příklad od každého typu ze stejného projektu.

Typická chyba: uvést dva funkční požadavky a jeden z nich nazvat „business“, protože zní důležitě.
:::

:::interview
Jak jednáte se stakeholderem, který už má řešení v hlavě?
*EN: How do you handle a stakeholder who already has a solution in mind?*
---
- Ber nápad vážně a zapiš si ho.
- Zeptej se na problém za ním: co se děje dnes, co se kazí, jak často, kolik to stojí.
- Porovnej navržené řešení s alternativami vůči potřebě.
- Pokud je navržené řešení dobré, řekni to; pokud ne, ukaž kompromis na faktech a nech rozhodnout toho, kdo rozhoduje.

Typická chyba: buď postavit požadované řešení bez otázek, nebo ho odmítnout, abys dokázala, že víš víc.
:::
