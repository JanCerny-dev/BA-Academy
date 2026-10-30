---
id: 05
slug: elicitation
title: Získávání požadavků (elicitace)
phase: B
priority: P1
quick_min: 5
deep_min: 40
job_ad: "požadavky od oddělení"
---

## Why this matters
Inzerát začíná „požadavky od oddělení“. Hotové požadavky ti nikdo nepředá: lidé popisují problémy, přání a polovičatá řešení a spoustu toho, co vědí, nikdy nahlas neřeknou. Elicitace je dovednost dostat ze stakeholderů skutečnou potřebu, ověřit ji a zapsat. Když ji pokazíš, dodavatel postaví přesně to, co bylo specifikováno, a stejně nebude nikdo spokojený.

## Quick version
**Elicitation** (elicitace) znamená získávání informací od stakeholderů a z dalších zdrojů. Slovo je zvolené záměrně: požadavky se neválejí kolem, aby se daly „posbírat“, musíš se k nim dopracovat. **Stakeholder** je každý, kdo změnu ovlivňuje nebo koho změna zasáhne: uživatelé, manažeři, IT, compliance, dodavatel, dokonce i klienti.

**Typy požadavků** (podle BABOK v3, příručky business analýzy od IIBA):
- **Business requirements** (business požadavky) – proč to organizace dělá. „Zkrátit dobu rozhodnutí o úvěrovém limitu z 10 na 3 pracovní dny.“
- **Stakeholder requirements** (požadavky stakeholderů) – co potřebuje skupina lidí. „Underwriteři potřebují mít data z registru o odběrateli k dispozici bez ručního hledání.“
- **Solution requirements** (požadavky na řešení) – co musí řešení dělat (**funkční**: „Systém načte údaje o odběrateli z ARES podle IČO“) a jak dobře (**nefunkční**: „Vyhledání vrátí výsledek do 5 sekund“).
- **Transition requirements** (přechodové požadavky) – co je potřeba jen pro přechod z dneška do nového stavu: migrace dat, školení, souběžný provoz.

**Hlavní techniky:**
- **Interviews** (rozhovory) – rozhovor jeden na jednoho, nejběžnější technika. Připrav si otázky, začni otevřeně, pak jdi do konkrétností.
- **Workshops** (workshopy) – moderované setkání více stakeholderů, kde se rychle dohodnou požadavky. JAD (Joint Application Design) je klasická forma, kdy jsou business a IT v jedné místnosti.
- **Observation / job shadowing** (pozorování) – sleduješ lidi při práci. Odhalí kroky, které zapomenou zmínit.
- **Document analysis** (analýza dokumentů) – postupy, formuláře, reporty, e-maily, obrazovky stávajících systémů.
- **Surveys** (dotazníky) – hodně lidí, krátké strukturované otázky. Dobré na potvrzení, slabé na objevování.
- **Prototyping / wireframes** (prototypy / drátěné modely) – náčrt obrazovky. Lidé reagují na obrázek mnohem lépe než na text.
- **Focus groups** (fokusní skupiny) – moderovaná diskuse s reprezentativními uživateli o názorech a zkušenostech.
- **Interface analysis** (analýza rozhraní) – jaká data jdou do systémů a ze systémů a ke komu.
- **Brainstorming** – rychle vymyslet hodně nápadů, hodnotit až potom.

**Volba techniky:** kombinuj několik. Rozhovory pro hloubku, pozorování pro skryté znalosti, dokumenty pro formální pravidla, workshopy pro řešení konfliktů, prototypy pro potvrzení.

**Typické problémy a co s nimi:**
- **Tacit knowledge** (skryté, implicitní znalosti: co lidé vědí, ale neřeknou, protože je to pro ně samozřejmé) – pozoruj, říkej „proveďte mě posledním případem, který jste řešil/a“, ptej se na výjimky.
- **Protichůdné názory** – zviditelni konflikt, vrať se k business cíli, v případě potřeby eskaluj k tomu, kdo rozhoduje.
- **Stakeholdeři s hotovým řešením** („potřebujeme tlačítko na export do Excelu“) – ptej se *proč*, dokud nedojdeš ke skutečné potřebě. Možná je potřebou „manažer chce týdenní přehled“ a lépe ji vyřeší report.

**Potvrď, co jsi slyšela.** Do druhého dne pošli zápis ze schůzky, přehraj zpátky proces nebo požadavky („Takže pravidlo je…, správně?“) a získej výslovné potvrzení. Nepotvrzené požadavky jsou jen předpoklady.

**Agile.** Elicitace neproběhne jednou na začátku. Pokračuje každý sprint při backlog refinementu, demech a zpětné vazbě.

**AI.** AI asistent může pomoct navrhnout otázky do rozhovoru nebo shrnout přepis. Do veřejných AI nástrojů dávej jen nedůvěrná nebo fiktivní data a výstup kontroluj: AI shrnutí vynechávají výjimky a někdy přidají věci, které nikdo neřekl.

**Odpověď na pohovor jednou větou:** „Kombinuji rozhovory, pozorování a analýzu dokumentů, výsledky potvrzuji písemným zápisem a přehráním zpátky a u požadovaného řešení se vždycky ptám, proč.“

## Deep dive

### Typy požadavků v praxi [P1]
Třídění požadavků není papírování pro papírování. Říká ti, kdo musí požadavek potvrdit a jak se bude ověřovat. BABOK v3 používá čtyři typy:

| Typ | Na jakou otázku odpovídá | Kdo potvrzuje | Příklad z ExportShield |
|---|---|---|---|
| Business | Proč to děláme? Jaký cíl? | Sponzor, vedení | „Do konce příštího roku rozhodovat 80 % žádostí o úvěrový limit do 3 pracovních dnů.“ |
| Stakeholder | Co skupina potřebuje, aby cíle dosáhla? | Zástupci té skupiny | „Underwriteři potřebují při posuzování žádosti všechna data o odběrateli na jedné obrazovce.“ |
| Solution – funkční | Co musí řešení dělat? | Vlastník procesu, BA, dodavatel | „Po zadání IČO systém předvyplní název a adresu odběratele z ARES.“ |
| Solution – nefunkční | Jak dobře, za jakých omezení? | IT, bezpečnost, provoz | „Vyhledání odběratele odpoví do 5 sekund u 95 % požadavků.“ |
| Transition | Co je potřeba pro samotnou změnu? | Projektový manažer, provoz | „Otevřené žádosti z excelového přehledu se před spuštěním převedou do PolicyHubu.“ |

Business požadavky jsou první. Každý požadavek stakeholdera i požadavek na řešení by měl jít zpětně dohledat k některému z nich. Když najdeš požadavek, který neslouží žádnému business požadavku, buď chybí business cíl, nebo požadavek není potřeba. Jak přesně psát požadavky na řešení, probírá modul 06.

Jiné rámce používají trochu jiné názvy (například IREB CPRE rozlišuje functional requirements, quality requirements a constraints, tedy funkční požadavky, požadavky na kvalitu a omezení). Myšlenka je stejná: oddělit *proč*, *co* a *jak dobře*.

### Příprava na elicitaci [P1]
Velká část dobré elicitace se odehraje ještě před první schůzkou. Než se s kýmkoli setkáš:

1. **Pochop kontext.** Přečti si, co existuje: popisy procesů, produktovou brožuru, staré projektové dokumenty, organizační schéma. Neměla bys na rozhovoru ztrácet čas otázkou, co je „buyer“ (odběratel).
2. **Identifikuj stakeholdery.** Kdo práci dělá, kdo rozhoduje, koho se to týká, kdo může věc zablokovat? (Analýzu stakeholderů probírá modul 16.) Nezapomeň na compliance, IT bezpečnost a provoz; když je nepozveš brzy, přinesou nefunkční požadavky pozdě.
3. **Definuj cíl setkání.** „Pochopit, jak se dnes kontrolují škody a kde se ztrácí čas“ je cíl. „Pobavit se o škodách“ není.
4. **Vyber techniky** (viz tabulka níže) a naplánuj pořadí: například analýza dokumentů, pak rozhovory, pak pozorování, pak workshop k dohodě o TO-BE.
5. **Připrav materiály**: scénář otázek, návrh procesního diagramu k opravě, prázdnou šablonu na poznámky.
6. **Logistika**: pozvánky s agendou, dost času (na rozhovor je typických 60 minut), souhlas s nahráváním, pokud chceš nahrávat.

### Rozhovory [P1]
Rozhovor je tažný kůň mezi technikami. Typy:
- **Structured** (strukturovaný): pevné otázky v pevném pořadí. Srovnatelné odpovědi, málo objevů.
- **Unstructured** (nestrukturovaný): volný rozhovor. Hodně objevů, těžko se porovnává.
- **Semi-structured** (polostrukturovaný): připravená banka otázek, ale jdeš za zajímavými odpověďmi. Tento typ budeš používat nejčastěji.

**Otevřené vs. uzavřené otázky.** Na *otevřenou* otázku nejde odpovědět ano nebo ne: „Jak rozhodujete, jestli jsou účetní výkazy dostatečné?“ Zve k vysvětlení. *Uzavřená* otázka dá přesnou odpověď: „Je hranice 1 M EUR stejná pro všechny země?“ Začni otevřeně, abys prozkoumala terén, uzavřené otázky použij k potvrzení detailů. Třetímu druhu, *sugestivní* otázce („Chtěl byste to mít automatizované, že?“), se vyhni, protože do odpovědi vkládá tvůj názor.

**Trychtýř (funnel).** Postupuj od obecného ke konkrétnímu: kontext → proces → problémy → detaily → přání → potvrzení.

**Active listening** (aktivní naslouchání). Parafrázuj („Takže když chybějí dokumenty, čekáte až dva týdny?“), ptej se dál („Co se stane potom?“), všímej si zaváhání („Zarazila jste se — je tam nějaká výjimka?“) a nevyplňuj ticho příliš rychle. Zapisuj si fakta *i* přesná slova, která lidé používají; slovník půjde do tvého glosáře.

**Užitečné vzory otázek:**
- „Proveďte mě poslední žádostí, kterou jste řešil/a, od chvíle, kdy dorazila.“
- „Co se stane, když …?“ (výjimky)
- „Jak často se to stává? Jak dlouho to trvá?“ (dopad)
- „Co děláte, když systém nejede?“ (obezličky)
- „S kým dalším bych měla mluvit?“ (hledání stakeholderů)
- „Kdybyste mohl/a změnit jednu věc, co by to bylo?“ (priority)
- „Proč je to důležité?“ (od řešení k potřebě)
- „Jak byste poznal/a, že nový proces funguje?“ (akceptace)

**Po rozhovoru:** ještě týž den sepiš poznámky, odděl fakta, názory a otevřené otázky a pošli je dotazovanému k potvrzení.

### Příklad: scénář rozhovoru pro tým škod v ExportShield [P1]
Cíl: pochopit, jak se dnes zpracovává oznámení o nezaplacení a kde vznikají ztráty času a chyby. Dotazovaný: likvidátor. Délka: 60 minut.

**Úvod (5 min)**
1. Poděkování; účel schůzky; jak se poznámky použijí; mohu nahrávat?
2. Jaká je vaše role a jak dlouho pracujete ve škodách?

**Přehled procesu (15 min)**
3. Proveďte mě poslední škodou, kterou jste zpracoval/a, od přijetí oznámení po výplatu.
4. Jak oznámení přichází? (e-mail, portál, telefon, dopis)
5. Jaké systémy a soubory v každém kroku používáte? (ClaimDesk, DocVault, Excel, e-mail)
6. Kdo další je zapojený a kdy předáváte práci?

**Pravidla a rozhodnutí (15 min)**
7. Jaké dokumenty musí exportér dodat? Co se stane, když některý chybí?
8. Jak kontrolujete, že faktura je krytá pojistnou smlouvou?
9. Jak se počítá plnění? Kde jsou pravidla zapsaná?
10. Kdo výplatu schvaluje a záleží to na částce?

**Problémy a výjimky (15 min)**
11. Která část trvá nejdéle? Proč?
12. Kde nejčastěji vznikají chyby?
13. Co děláte jinak, než říká oficiální postup, a proč?
14. Řekněte mi o nějaké neobvyklé škodě z posledních měsíců.

**Přání a závěr (10 min)**
15. Kdybyste mohl/a změnit jednu věc, co by to bylo? Proč?
16. Jak byste poznal/a, že nový proces je lepší?
17. S kým dalším bych měla mluvit? Mohu se příští týden podívat, jak zpracováváte škodu?
18. Shrnutí toho, co jsem slyšela; další kroky; kdy dostanete poznámky.

Všimni si pořadí: nejdřív proces, pak problémy, přání nakonec. Když se na přání zeptáš hned, dostaneš řešení bez kontextu.

### Workshopy a JAD [P1]
**Requirements workshop** (workshop k požadavkům) svede dohromady několik stakeholderů na soustředěné, moderované setkání, obvykle na 2–4 hodiny. Workshopy jsou efektivní pro dohodu o TO-BE procesu, řešení konfliktů a prioritizaci, protože rozhodnutí padají, když jsou všichni v místnosti.

**JAD** (Joint Application Design nebo Development) je strukturovaný formát workshopu ze 70. a 80. let, kde business uživatelé a IT návrháři společně definují požadavky a návrh. Princip platí dodnes: lidé, kteří znají business, a lidé, kteří řešení staví, spolu mluví přímo.

Role: **facilitator** (moderátor, často BA), který drží proces neutrální, **scribe** (zapisovatel), který zaznamenává rozhodnutí, **decision maker** (ten, kdo rozhoduje), který umí rozsoudit spory, a účastníci. Drž to zhruba na 5–10 lidech.

Jak workshop vést:
1. Předem pošli agendu, cíl a materiály k přečtení.
2. Začni cílem a pravidly (timebox, telefony stranou, „parkoviště“ pro témata mimo program).
3. Používej vizuální materiál: návrh BPMN modelu na zdi nebo tabuli v [Miro](https://miro.com/), lepicí papírky, prototyp.
4. Každé téma uzavři rozhodnutím nebo úkolem s vlastníkem a termínem.
5. Výsledky pošli do 24–48 hodin.

Riziko: dominantní účastník (často ten nejvýš postavený) řídí všechno. Brání se tomu tichým psaním na papírky před diskusí, slovem postupně po kruhu a přímým oslovením tichých lidí.

### Pozorování, analýza dokumentů a analýza rozhraní [P2]
**Observation** (pozorování, job shadowing) znamená sledovat někoho při skutečné práci. *Pasivní* pozorování: díváš se a píšeš si poznámky, otázky až potom. *Aktivní*: ptáš se během práce („Proč jste otevřel/a ten Excel?“). Pozorování odhalí skryté kroky, obezličky, přerušení a skutečné časy. Požádej o svolení, vysvětli, že pozoruješ proces, ne člověka, a počítej s tím, že se lidé chovají jinak, když je někdo sleduje.

**Document analysis** (analýza dokumentů) znamená číst existující materiály: postupy, pojistné podmínky, formuláře, šablony, reporty, obrazovky systémů, logy chyb, staré požadavky. Je to dobrý první krok, protože stakeholderům nebere čas a dá ti slovník. Omezení: dokumenty jsou často zastaralé a popisují oficiální proces.

**Interface analysis** (analýza rozhraní) určí propojení řešení s okolím: jiné systémy (PolicyHub ↔ DocVault), externí služby (ARES), uživatelé (obrazovky) a organizace (exportér, zajistitel). U každého rozhraní se ptáš: jaká data, kterým směrem, jak často, v jakém formátu, co se stane při selhání. To je vstup pro integrační požadavky (API probírá modul 11).

### Dotazníky a fokusní skupiny [P2]
**Survey** (dotazník) osloví mnoho lidí levně. Funguje na potvrzení a kvantifikaci: „Kolik žádostí o úvěrový limit týdně vyřídíte?“ nebo „Ohodnoťte současný přehled od 1 do 5.“ Na objevování neznámých potřeb funguje špatně. Drž ho krátký (pod 10 minut), používej hlavně uzavřené otázky, nejdřív ho vyzkoušej na jednom člověku a na konec přidej jednu otevřenou otázku.

**Focus group** (fokusní skupina) je moderovaná diskuse 6–10 reprezentativních uživatelů nebo klientů o jejich zkušenostech a názorech, například exportérů, kteří diskutují, co čekají od online hlášení škody. Hodí se pro produkty pro koncové uživatele. Skupinová dynamika může tlačit ke shodě, takže moderátor musí nesouhlas podporovat.

### Prototypy a wireframy [P1]
**Prototype** (prototyp) je raný model řešení, na který sbíráš zpětnou vazbu. **Wireframe** (drátěný model) je hrubý náčrt obrazovky: obdélníky, popisky, tlačítka, bez barev a designu. Lidé, kteří nedokážou okomentovat psaný požadavek, hned řeknou „tohle pole chybí“ nebo „tohle nikdy nepotřebujeme“, když vidí obrazovku.

- **Throw-away prototypes** (prototypy na zahození): náčrty na papíře, maketa v [draw.io](https://app.diagrams.net/). Levné, rychlé, slouží jen k učení.
- **Evolutionary prototypes** (evoluční prototypy): postavené ve skutečné platformě (například [Power Apps](https://make.powerapps.com/)) a vylepšované až do finálního řešení.

Praktický tip: nech wireframy viditelně hrubé. Vyleštěná maketa svádí k diskusi o barvách a písmech místo o polích a pravidlech a stakeholdeři si mohou myslet, že systém je skoro hotový.

U formuláře žádosti o úvěrový limit bys načrtla: údaje exportéra (předvyplněné), IČO odběratele s tlačítkem „vyhledat“, název a adresu odběratele (vyplněné z ARES, jen pro čtení), zemi, požadovanou částku a měnu, splatnost ve dnech, přílohy pro účetní výkazy, tlačítko pro odeslání a validační hlášky. Každé pole v náčrtu je otázka pro stakeholdery: povinné nebo volitelné, jaký formát, kdo ho může měnit.

### Brainstorming [P3]
Brainstorming vytvoří hodně nápadů za krátkou dobu. Pravidla: kvantita před kvalitou, žádná kritika během vymýšlení, stavět na nápadech ostatních, pak seskupit a vyhodnotit. Varianta je *brainwriting*, kdy každý nejdřív potichu píše nápady, což omezí vliv dominantních hlasů. Použij ho, když hledáš varianty řešení nebo kořenové příčiny, například „Proč rozhodnutí o úvěrovém limitu trvají 10 dnů?“

### Volba techniky [P1]
| Situace | Vhodné techniky | Proč |
|---|---|---|
| Nový obor, víš málo | Analýza dokumentů, rozhovory | Nejdřív vybudovat slovník a kontext |
| Lidé neumějí svou práci dobře popsat | Pozorování, „proveďte mě posledním případem“ | Odhalí skryté znalosti |
| Mnoho stakeholderů s různými názory | Workshop | Dohoda na jednom setkání |
| Mnoho uživatelů, potřebuješ čísla | Dotazník | Levné, kvantitativní |
| Obrazovky a formuláře | Wireframy, prototypy | Lidé reagují na obrázky |
| Integrace s jinými systémy | Analýza rozhraní, analýza dokumentů | Data, formáty, chybové stavy |
| Potřebuješ nápady nebo kořenové příčiny | Brainstorming, workshop | Šíře před hloubkou |

V praxi kombinuješ tři čtyři techniky. Typické pořadí u zlepšení v ExportShield: přečíst postupy a vzorové žádosti → rozhovor se dvěma underwritery a jejich vedoucím → jedno dopoledne pozorovat vyřizování žádostí → nakreslit AS-IS a ověřit ho na krátkém workshopu → načrtnout TO-BE formulář a vyzkoušet ho s uživateli.

### Obtížné situace [P1]
**Skryté znalosti.** Experti přeskakují kroky, protože je dělají automaticky. Znaky: popsaný proces je podezřele krátký nebo čísla nesedí („pět kroků, ale trvá to tři dny“). Co pomáhá: pozorování, ptát se na poslední skutečný případ místo obecného pravidla, ptát se na výjimky („Kdy to nefunguje?“) a ptát se nováčků, kteří kroky ještě vnímají.

**Protichůdné názory.** Sales chce rozhodnutí do jednoho dne, Underwriting chce úplná finanční data. Nestav se na žádnou stranu. Konflikt pojmenuj, zapiš obě pozice i jejich důvody, propoj je s business cílem a navrhni varianty (například zrychlenou cestu pro malé limity). Když se to vyřešit nedá, rozhodne sponzor nebo vlastník procesu a ty rozhodnutí zaznamenáš.

**Stakeholdeři s hotovým řešením.** „Potřebujeme tlačítko, které vyexportuje přehled do Excelu.“ Neodmítej a jen to nezapiš. Ptej se proč: „Co s exportem děláte?“ → „Každý pátek ho posílám vedoucímu.“ → „Co s ním vedoucí dělá?“ → „Kontroluje, které žádosti jsou starší než týden.“ Skutečná potřeba je *přehled o žádostech po termínu*. Varianty: filtrované zobrazení, automatický týdenní report, eskalace časovačem (modul 04). Tlačítko pro Excel může být pořád nejlevnější varianta, ale teď je rozhodnutí informované. Opakovanému ptaní „proč“ se říká technika *5 Whys*.

**Vágní odpovědi.** „Mělo by to být rychlé.“ Ptej se na čísla a příklady: „Rychlé ve srovnání s čím? Kolik je ještě přijatelné? Co je už moc pomalé?“

**Nedostupní stakeholdeři.** Zkrať setkání, přijď s návrhem k opravě (lidé reagují rychleji na něco špatně než na prázdnou stránku) nebo požádej o zástupce s rozhodovací pravomocí.

**Scope creep (rozlézání rozsahu) na rozhovorech.** Stakeholdeři využijí příležitost a chtějí všechno. Zapiš každé přání, ta mimo rozsah tak označ a řekni to zdvořile: „Zapíšu si to jako samostatný nápad; je to mimo tento projekt.“

### Potvrzení výsledků [P1]
Získaná informace není požadavek, dokud ji zdroj nepotvrdí. Techniky:
- **Meeting notes** (zápis ze schůzky) poslaný do 24 hodin: rozhodnutí, fakta, otevřené otázky, úkoly s vlastníkem a termínem. Krátký a strukturovaný, ne přepis.
- **Playback** (přehrání zpátky): zopakuj své pochopení vlastními slovy nebo ukaž diagram. „Dovolte, abych zopakovala, co jsem slyšela: …“ Chyby vyplavou okamžitě.
- **Walkthrough** (společné projití) nakresleného procesu nebo seznamu požadavků se stakeholdery.
- **Prototype review** (revize prototypu): uživatelé proklikají wireframy nebo je okomentují.

Sleduj, odkud každý požadavek pochází (zdroj, datum). To je začátek traceability (sledovatelnosti, modul 06).

### Elicitace v agilních projektech [P2]
V agilní práci (modul 07) není žádná velká fáze požadavků. Elicitace probíhá průběžně:
- Elicitace na vysoké úrovni na začátku pro vizi, epiky a story map.
- Detailní elicitace *just in time* (právě včas) při backlog refinementu, pár sprintů před tím, než se story staví.
- Zpětná vazba na sprint review, kde stakeholdeři vidí fungující software a reagují.

Techniky zůstávají stejné, ale setkání jsou kratší a častější. Výsledky končí jako user stories a akceptační kritéria místo velkého dokumentu. V hybridních projektech s externím dodavatelem často děláš obojí: funkční specifikaci pro smlouvu a stories pro dodávku.

### Použití AI při elicitaci [P2]
AI asistenti jako [ChatGPT](https://chatgpt.com/), [Claude](https://claude.ai/) nebo [Copilot](https://copilot.microsoft.com/) mohou pomoct na několika místech:
- **Příprava otázek**: „Navrhni otázky do rozhovoru s likvidátorem v pojišťovně exportních úvěrů o kontrole dokumentů u oznámení o nezaplacení.“ Dostaneš první návrh k úpravě.
- **Hraní rolí**: nech AI hrát stakeholdera s fiktivním profilem a procvič si rozhovor.
- **Shrnutí**: převést přepis na poznámky, vypsat otevřené otázky, vytáhnout kandidátní požadavky.
- **Kontrola**: požádej ji, ať v tvých poznámkách najde nejednoznačná slova nebo chybějící výjimky.

Pravidla:
1. **Nikdy nevkládej firemní ani klientská data do veřejných AI nástrojů.** Používej fiktivní data nebo nástroje schválené tvým IT. Nahrávky a přepisy skutečných rozhovorů jsou automaticky důvěrné.
2. **Všechno ověř.** AI shrnutí mají sklon uhlazovat výjimky a neshody, tedy přesně to, na čem záleží, a mohou si vymyslet věrohodně znějící detaily.
3. **Buď transparentní.** Pokud obsah vytvořený AI jde do oficiálních dokumentů, řiď se pravidly organizace pro jeho označování.

Dobrá odpověď na pohovoru k tomuto tématu ukazuje přínos i limity: „AI používám k přípravě banky otázek a ke kontrole nejednoznačností v poznámkách, ale jen s nedůvěrnými daty, a výsledky vždycky potvrzuji se stakeholdery.“

## Key terms
- **Elicitation** (elicitace, získávání požadavků) — získávání požadavků a souvisejících informací od stakeholderů a z dalších zdrojů.
- **Stakeholder** (zainteresovaná strana) — osoba nebo skupina, která změnu ovlivňuje nebo kterou změna zasáhne.
- **Business requirement** (business požadavek) — cíl nebo potřeba organizace, která vysvětluje, proč se změna dělá.
- **Stakeholder requirement** (požadavek stakeholdera) — potřeba konkrétní skupiny stakeholderů, kterou je nutné splnit pro dosažení business cíle.
- **Solution requirement** (požadavek na řešení) — schopnost (funkční) nebo kvalita (nefunkční), kterou řešení musí mít.
- **Transition requirement** (přechodový požadavek) — dočasná potřeba pro přechod ze současného do budoucího stavu, například migrace dat nebo školení.
- **Semi-structured interview** (polostrukturovaný rozhovor) — rozhovor s připravenou bankou otázek, který dovoluje jít za zajímavými odpověďmi.
- **Open question** (otevřená otázka) — otázka, která zve k vysvětlení a nedá se zodpovědět ano nebo ne.
- **Active listening** (aktivní naslouchání) — parafrázování, doplňující otázky a ověřování porozumění během rozhovoru.
- **Requirements workshop** (workshop k požadavkům) — moderované setkání, na kterém několik stakeholderů společně definuje nebo odsouhlasí požadavky.
- **JAD (Joint Application Design)** — strukturovaný formát workshopu, který spojuje business uživatele a IT návrháře.
- **Observation / job shadowing** (pozorování) — sledování lidí při skutečné práci, aby se pochopil reálný proces.
- **Document analysis** (analýza dokumentů) — studium existujících dokumentů, formulářů a systémů za účelem získání informací.
- **Interface analysis** (analýza rozhraní) — určení dat vyměňovaných mezi řešením a jinými systémy, uživateli nebo organizacemi.
- **Wireframe** (drátěný model) — hrubý náčrt obrazovky, nad kterým se diskutuje obsah a rozložení.
- **Tacit knowledge** (skrytá, implicitní znalost) — znalost, kterou lidé mají, ale nevyjádří ji, protože je pro ně samozřejmá.
- **Playback** (přehrání zpátky) — zopakování vlastního pochopení stakeholderům, aby ho potvrdili.
- **5 Whys** (5× proč) — opakované ptaní „proč“, jak se od symptomu nebo navrženého řešení dostat ke skryté potřebě.

## Hands-on
:::exercise id="m05-e1" title="Napiš scénář rozhovoru pro tým škod" min="45" tool="text editor"
Cíl: připravit polostrukturovaný rozhovor, který bys mohla opravdu použít.

1. Definuj cíl rozhovoru jednou větou, například ke kroku kontroly dokumentů u škod v ExportShield.
2. Napiš 15–20 otázek seskupených do částí: úvod, proces, pravidla a rozhodnutí, problémy a výjimky, přání a závěr.
3. Označ každou otázku jako otevřenou (O) nebo uzavřenou (C). V první polovině mají být aspoň dvě třetiny otevřené.
4. Přidej tři doplňující otázky, které bys položila, když odpověď zní „záleží na tom“.
5. Odstraň sugestivní otázky. Přečti každou otázku nahlas a zeptej se sama sebe, jestli nenaznačuje odpověď.
6. Připrav jednostránkovou šablonu na poznámky: fakta, pravidla, pain pointy, otevřené otázky, úkoly.

Hotovo, když: scénář se vejde do 60 minut, začíná obecně a jde ke konkrétnímu a končí otázkou „s kým dalším bych měla mluvit?“.
:::

:::exercise id="m05-e2" title="Proveď cvičný rozhovor a vytáhni z něj požadavky" min="60" tool="ChatGPT / Claude / Copilot"
Cíl: procvičit vedení rozhovoru a převést syrové odpovědi na požadavky.

1. Najdi si partnera (kamaráda nebo člena rodiny), nebo použij AI asistenta. U AI začni promptem jako: „Play a claims handler at ExportShield Insurance, a fictional export credit insurer. You process notifications of non-payment using a system called ClaimDesk, e-mail and Excel. Answer only what I ask, be realistic, mention one or two frustrations only when asked about problems, and sometimes give vague answers.“ Používej jen fiktivní data.
2. Projdi svůj scénář ze cvičení m05-e1 za 30–40 minut. Ptej se doplňujícími otázkami; seznam jen nečti.
3. Napiš zápis ze schůzky: fakta, pravidla, pain pointy, otevřené otázky.
4. Vytáhni aspoň 8 kandidátních požadavků a zařaď je jako business, stakeholder, funkční, nefunkční nebo přechodové.
5. Označ, která tvrzení bys potřebovala potvrdit z druhého zdroje.

Hotovo, když: máš poznámky, roztříděný seznam aspoň 8 požadavků a aspoň dvě místa, kde sis všimla vágní odpovědi a zeptala se na číslo nebo příklad.
:::

:::exercise id="m05-e3" title="Nakresli wireframe formuláře žádosti o úvěrový limit" min="45" tool="draw.io"
Cíl: pomocí prototypu zkonkrétnit požadavky.

1. Na papíře nebo v [draw.io](https://app.diagrams.net/) (v knihovně tvarů vyhledej „mockup“) načrtni formulář, kterým exportér žádá o úvěrový limit.
2. Zahrň: údaje exportéra (předvyplněné), IČO odběratele s tlačítkem pro vyhledání, název a adresu odběratele (jen pro čtení, z ARES), zemi odběratele, požadovanou částku a měnu, splatnost ve dnech, nahrání příloh, tlačítko pro odeslání.
3. Ke každému poli připiš poznámku: povinné nebo volitelné, formát, validace, zdroj.
4. Ukaž jeden chybový stav, například „Buyer not found in registry“.
5. Napiš pět otázek, které wireframe vyvolal a které bys položila stakeholderům.

Hotovo, když: kdo se na náčrt podívá, umí říct, která pole jsou povinná a co se stane, když vyhledání selže, a ty máš pět otevřených otázek.
:::

## Self-check
:::q
Proč se tomu říká „elicitace“ (vyvolávání) a ne „sběr“ požadavků?
---
Protože požadavky neleží připravené k posbírání. Stakeholdeři vyjadřují problémy, přání a řešení a velká část jejich znalostí je skrytá. BA musí informace aktivně vytáhnout, zpochybnit, analyzovat a nechat potvrdit, než se z nich stane požadavek.
:::

:::q
Zařaď: „Otevřené žádosti z excelového přehledu se musí před spuštěním přesunout do PolicyHubu.“
---
Je to přechodový požadavek (transition requirement). Je potřeba jen pro přechod ze současného do budoucího stavu a po dokončení migrace už neplatí.
:::

:::q
Stakeholder říká: „Potřebujeme tlačítko, které pošle žádost na Risk Committee.“ Co uděláš?
---
Ptej se proč, dokud nedojdeš ke skryté potřebě: možná se na velké žádosti zapomíná nebo výboru chybějí informace. Pak zvaž varianty, například automatické směrování podle částky nebo frontu výboru. Tlačítko může být pořád správná odpověď, ale rozhodnutí má vycházet z potřeby, ne z prvního navrženého řešení.
:::

:::q
Proč pozorování a „proveďte mě posledním případem“ dobře fungují proti skrytým znalostem?
---
Experti při obecném popisu své práce přeskakují kroky, které jim připadají samozřejmé. Sledování práce nebo otázka na jeden konkrétní nedávný případ tyto kroky, obezličky a výjimky vynese na povrch, protože člověk rekonstruuje, co se skutečně stalo.
:::

:::q
Kdy je dotazník špatná volba?
---
Když potřebuješ objevit neznámé potřeby nebo pochopit důvody. Dotazníky fungují nejlépe na potvrzení a kvantifikaci věcí, o kterých už víš, s uzavřenými otázkami pro mnoho lidí. Dávají málo hloubky a nemůžeš klást doplňující otázky.
:::

:::q
Co bys měla udělat během 24 hodin po rozhovoru?
---
Sepsat strukturované poznámky s fakty, pravidly, pain pointy, otevřenými otázkami a úkoly a poslat je dotazovanému k potvrzení. U každé položky si poznamenat zdroj a datum, aby šly požadavky později dohledat.
:::

:::q
Jaká jsou dvě rizika použití veřejného AI nástroje ke shrnutí přepisu rozhovoru?
---
Zaprvé důvěrnost: skutečný přepis obsahuje firemní a možná i klientská data, která nesmějí do neschválených nástrojů. Zadruhé přesnost: shrnutí může vynechat výjimky a neshody nebo přidat detaily, které nikdo neřekl, takže se musí zkontrolovat proti zdroji a potvrdit se stakeholdery.
:::

## Interview corner
:::interview
Jak získáváte požadavky od oddělení, se kterým jste nikdy nepracovala?
*EN: How do you elicit requirements from a department you have never worked with?*
---
- Příprava: přečíst dokumenty, pochopit slovník oboru, identifikovat stakeholdery.
- Začít rozhovory s klíčovými lidmi, pak pozorovat skutečnou práci.
- Nakreslit AS-IS a přehrát ho zpátky.
- Workshop k dohodě o prioritách nebo řešení konfliktů, prototypy pro obrazovky.
- Potvrdit písemně a sledovat zdroje.

Typická chyba: popsat jen „zeptala bych se jich, co potřebují“, bez přípravy, technik a potvrzení.
:::

:::interview
Dvě oddělení chtějí opačné věci. Jak to řešíte?
*EN: Two departments want opposite things. How do you handle it?*
---
- Konflikt pojmenovat a zdokumentovat obě pozice s jejich důvody.
- Vrátit se k business cíli a měřitelnému záměru.
- Hledat varianty, které uspokojí obě strany (například různé cesty podle částky nebo rizika).
- Když se to nevyřeší, eskalovat k tomu, kdo rozhoduje, s variantami a dopady, a rozhodnutí zaznamenat.

Typická chyba: rozhodnout sama jako BA, nebo se bez analýzy přidat na stranu výš postaveného člověka.
:::

:::interview
Jaký je rozdíl mezi business požadavkem a funkčním požadavkem? Uveďte příklad.
*EN: What is the difference between a business requirement and a functional requirement? Give an example.*
---
- Business požadavek: proč, cíl organizace, například „rozhodovat 80 % žádostí do 3 pracovních dnů“.
- Funkční požadavek: co řešení dělá, například „systém načte údaje o odběrateli z ARES podle IČO“.
- Funkční požadavky musí jít zpětně dohledat k business požadavku.
- Zmínit další typy: požadavky stakeholderů, nefunkční a přechodové požadavky.

Typická chyba: uvést dva funkční požadavky a jeden z nich nazvat „business“.
:::

:::interview
Stakeholder dává vágní odpovědi typu „má to být uživatelsky přívětivé a rychlé“. Co uděláte?
*EN: A stakeholder gives vague answers like "it should be user-friendly and fast". What do you do?*
---
- Zeptat se na konkrétní příklady a čísla: jak rychlé, ve srovnání s čím, co je nepřijatelné.
- Zeptat se na situaci, kdy byl současný systém příliš pomalý nebo matoucí.
- Odpověď převést na měřitelný nefunkční požadavek a nechat ho potvrdit.
- Prototypem zkonkrétnit, co znamená „uživatelsky přívětivé“.

Typická chyba: napsat do specifikace „systém bude uživatelsky přívětivý“.
:::

:::interview
Jak používáte AI nástroje při práci s požadavky?
*EN: How do you use AI tools in requirements work?*
---
- Návrhy banky otázek, hraní role stakeholdera, shrnutí, kontrola nejednoznačností.
- Do veřejných nástrojů jen nedůvěrná nebo fiktivní data; jinak nástroje schválené IT.
- Výstup vždy ověřit a výsledky potvrdit se skutečnými stakeholdery.
- Dodržovat interní pravidla pro označování obsahu vytvořeného AI.

Typická chyba: popisovat vkládání skutečných přepisů schůzek do veřejného chatbota.
:::
