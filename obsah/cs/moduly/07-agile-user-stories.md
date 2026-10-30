---
id: 07
slug: agile-user-stories
title: "Agilní požadavky: user stories, akceptační kritéria a Jira"
phase: B
priority: P1
quick_min: 5
deep_min: 40
job_ad: "general"
---

## Why this matters
Většina IT týmů, včetně dodavatelů, plánuje práci v backlogu user stories, obvykle v Jiře. Jako BA tyhle stories píšeš, definuješ akceptační kritéria, na která se spoléhají testeři i vývojáři, a spolu s product ownerem udržuješ backlog v pořádku. Na pohovoru tě často požádají, abys na místě napsala user story s akceptačními kritérii nebo vysvětlila INVEST a Given/When/Then.

## Quick version
V agilním vývoji (přístup, kdy se software dodává po malých přírůstcích, typicky každé 1–4 týdny, s častou zpětnou vazbou) se požadavky drží v **product backlogu**: seřazeném seznamu všeho, co by se mohlo postavit.

**Hierarchie položek backlogu** (názvy se v nástrojích liší):
- **Epic** – velký celek práce, příliš velký na jeden sprint. „Online claim notification for exporters.“
- **Feature** – schopnost v rámci epicu (používá se jen v některých nastaveních, například v SAFe).
- **User story** (uživatelský příběh) – malý kus hodnoty pro uživatele, dodatelný během jednoho sprintu.
- **Task / sub-task** (úkol / podúkol) – technická práce potřebná k dodání story („Create API endpoint“, „Write test cases“).

**Formát user story:**
> As a **[role]**, I want **[capability]**, so that **[benefit]**.

(Česky: Jako [role] chci [schopnost], abych [přínos].)

Příklad: *As an exporter, I want to upload the unpaid invoice and the reminder letters with my claim notification, so that ExportShield can start checking my claim without asking for documents by e-mail.*

Story je zástupný symbol pro rozhovor, ne úplná specifikace. Tři C: **Card** (krátký text na kartičce), **Conversation** (diskuse, která vyjasní detaily), **Confirmation** (akceptační kritéria).

**INVEST** – kontrolní seznam pro dobré stories: Independent, Negotiable, Valuable, Estimable, Small, Testable (nezávislá, vyjednatelná, hodnotná, odhadnutelná, malá, testovatelná).

**Dělení stories.** Velké stories se dělí vertikálně (každý kus pořád dodá něco použitelného): podle kroků workflow, podle business pravidel, podle variant dat, nejdřív šťastná cesta a chybové cesty později, nebo podle operací (create, read, update, delete).

**Acceptance criteria (AC)** (akceptační kritéria) jsou podmínky, které musí story splnit, aby byla přijata. Dva styly:
- **Rule-based** (založená na pravidlech) – kontrolní seznam: „Only PDF, JPG and PNG files are accepted. Maximum 10 MB per file.“
- **Scenario-based** (založená na scénářích) – Gherkin **Given / When / Then**:

```gherkin
Scenario: Exporter uploads a file that is too large
  Given the exporter is on the claim notification form
  When the exporter uploads a PDF file of 12 MB
  Then the system rejects the file
  And shows the message "The file is larger than 10 MB."
```

**Definition of Ready (DoR)** – co story potřebuje, než si ji tým vezme do sprintu (jasná AC, známé závislosti, odhad). **Definition of Done (DoD)** – co musí platit, aby se jakákoli položka počítala jako hotová (code review, otestováno, zdokumentováno, nasazeno do testovacího prostředí).

**Backlog refinement** – pravidelné setkání, na kterém product owner, BA a tým vyjasňují, dělí a odhadují nadcházející stories. **Story points** jsou relativní odhady pracnosti a složitosti, které dělají vývojáři; BA story vysvětluje, ale sám ji neodhaduje.

**Product owner vs. BA.** **Product owner** (role ve Scrumu) odpovídá za maximalizaci hodnoty produktu a za pořadí backlogu. BA pomáhá analýzou: elicitace, psaní stories a AC, modelování, vyjasňování detailů. V malých týmech může obojí dělat jeden člověk.

**Základy Jiry.** Typy issues (epic, story, task, bug, sub-task), workflow (To Do → In Progress → In Review → Done), backlog, sprinty a board (nástěnka). Filtry používají **JQL** (Jira Query Language): `project = CLM AND status = "In Progress"`. Confluence je k Jiře přidružená wiki pro specifikace, zápisy ze schůzek a rozhodnutí.

**Hybridní a dodavatelské projekty.** Funkční specifikace často určuje smluvní rozsah a stories v Jiře ho rozdělují na dodatelné kusy. Každá story odkazuje zpět na sekci specifikace nebo ID požadavku, což udržuje dohledatelnost.

**Věta na pohovor:** „Stories píšu ve formě role–schopnost–přínos, kontroluji je podle INVEST, dělím je vertikálně a akceptační kritéria definuji jako pravidla nebo scénáře Given/When/Then, které testeři můžou rovnou použít.“

## Deep dive

### Agile na jedné stránce [P1]
Agile je rodina přístupů postavených na Agile Manifestu (2001): dodávat fungující software v krátkých cyklech, úzce spolupracovat se zákazníky a reagovat na změny. **Scrum** je nejrozšířenější framework. Oficiální [Scrum Guide](https://scrumguides.org/scrum-guide.html) (verze 2020) definuje:
- tři accountabilities (odpovědnosti): **Product Owner**, **Scrum Master**, **Developers**,
- události (events): **Sprint** (pevný timebox v délce nejvýš jednoho měsíce, často dva týdny), Sprint Planning, Daily Scrum, Sprint Review, Sprint Retrospective,
- artefakty: **Product Backlog**, **Sprint Backlog**, **Increment**, se závazky (commitments) Product Goal, Sprint Goal a Definition of Done.

Scrum Guide nezmiňuje „business analytika“, „user stories“ ani „story points“. Jsou to běžné praktiky, které si týmy přidávají. **Kanban** je alternativa bez sprintů: práce plyne průběžně přes sloupce s limity rozpracované práce (WIP limits). Přístupům k dodávce se podrobněji věnuje modul 02.

### Epics, features, stories, tasks [P1]
| Úroveň | Velikost | Kdo to čte | Příklad z ExportShield |
|---|---|---|---|
| Epic | Týdny až měsíce | Vedení, PO, tým | Online claim notification for exporters |
| Feature | Několik sprintů | PO, tým | Document upload in claim notification |
| User story | Vejde se do jednoho sprintu, ideálně pár dní | Tým, testeři | Upload invoice as PDF to a claim notification |
| Task / sub-task | Hodiny | Vývojáři | Add file size validation on the server |

Výchozí hierarchie v Jiře je Epic → Story/Task/Bug → Sub-task. Větší organizace přidávají úrovně nad epicy (initiatives, themes). Používej to, co používá tvůj tým; podstatné je, že stories jsou malé a dodávají hodnotu, kdežto tasks jsou technické kroky, které samy uživateli nic nedodají.

**Bug** (defekt) je také položka backlogu: něco nefunguje podle specifikace.

### Psaní user stories [P1]
Formát: *As a [role], I want [capability], so that [benefit].*

- **Role**: konkrétní typ uživatele, ne „user“. Exportér, likvidátor škod (claims handler), underwriter, vedoucí škod (head of claims). Pokud je rolí „the system“, jde nejspíš o technický task, nebo by story měla být napsaná z pohledu člověka, který z ní má prospěch.
- **Capability** (schopnost): co může udělat, jeho jazykem, bez detailů UI („submit“, „see“, „be notified“).
- **Benefit** (přínos): proč na tom záleží. Tahle část se často vynechává, a přitom je nejužitečnější, protože týmu umožní najít levnější cestu ke stejnému přínosu.

**Příklady pro portál ExportShield na hlášení škod:**
1. As an exporter, I want to notify a non-payment online by selecting the insured buyer and the unpaid invoice, so that I do not have to fill in a paper form.
2. As an exporter, I want to see the status of my claim notifications, so that I do not have to call ExportShield to ask.
3. As a claims handler, I want new notifications to appear in my ClaimDesk queue automatically, so that I do not have to retype them from e-mails.
4. As a claims handler, I want to see which mandatory documents are missing, so that I can request them in one message.

**Slabé stories a proč:**
- „As a user, I want a better claims portal.“ – role je příliš obecná, nedá se otestovat, není malá.
- „As a developer, I want to create a REST endpoint.“ – žádná hodnota pro uživatele; je to task.
- „As an exporter, I want a green button at the top right.“ – popisuje návrh UI, ne potřebu.

**3 C** (Card, Conversation, Confirmation, popsal je Ron Jeffries) připomínají, že kartička je záměrně krátká. Detaily vzniknou v rozhovoru a zachytí se v akceptačních kritériích, přiložených wireframech nebo odkazech na specifikaci.

### INVEST [P1]
INVEST (autorem je Bill Wake) je kontrolní seznam:

| Písmeno | Význam | Otázka | Příklad problému |
|---|---|---|---|
| I – Independent (nezávislá) | Dá se postavit a dodat bez čekání na jinou story | Můžeme změnit pořadí? | „Story B funguje jen po story A“ u každé story |
| N – Negotiable (vyjednatelná) | O detailech se dá ještě diskutovat | Je napsaná jako potřeba, nebo jako pevný návrh? | V story nadiktovaný celý návrh obrazovky |
| V – Valuable (hodnotná) | Dodává hodnotu uživateli nebo businessu | Kdo z toho má prospěch? | „Create database table“ |
| E – Estimable (odhadnutelná) | Tým jí rozumí natolik, aby ji odhadl | Umí ji vývojáři ocenit? | Neznámá integrace bez dokumentace |
| S – Small (malá) | Vejde se do sprintu, ideálně pár dní | Dá se udělat za méně než půl sprintu? | „Build the claims portal“ |
| T – Testable (testovatelná) | Má jasná kritéria hotovosti | Jak by ji tester ověřil? | „The portal should be pleasant to use“ |

Úplná nezávislost je zřídka možná. Cílem je závislosti omezit, ne je odstranit.

### Dělení stories [P1]
Velké stories se dělí **vertikálně**: každý řez prochází všemi vrstvami (obrazovka, logika, data) a dodá něco testovatelného. Dělení **horizontálně** („postav databázi“, „postav UI“) vytvoří kusy, které samy o sobě nemají hodnotu.

Běžné vzory, použité na epic „Online claim notification“:

| Vzor | Jak dělí | Příklady řezů |
|---|---|---|
| Kroky workflow | Jedna story na krok procesu | Výběr odběratele a faktury → nahrání dokumentů → odeslání → potvrzení |
| Business pravidla | Nejdřív jednoduché pravidlo, složitá později | Přijmout jakékoli hlášení → odmítnout faktury po lhůtě pro hlášení dle smlouvy → upozornit, pokud faktura není pojištěná |
| Varianty dat | Jeden typ dat nebo případ najednou | Hlášení v EUR → další měny; jedna faktura → více faktur |
| Šťastná / chybová cesta | Nejdřív hlavní úspěch, chyby zvlášť | Úspěšné nahrání → příliš velký soubor → špatný typ souboru → nalezen virus |
| Operace (CRUD) | Vytvořit, číst, upravit, smazat zvlášť | Vytvořit koncept hlášení → zobrazit koncept → upravit koncept → smazat koncept |
| Rozhraní / kanál | Nejdřív jeden kanál | Nejdřív portál, API pro velké exportéry později |
| Odložit výkon | Nejdřív ať to funguje, pak ať je to rychlé | Základní seznam škod → stránkování a filtrování pro exportéry se stovkami škod |

Dobré rozdělení umožní product ownerovi méně hodnotné řezy vypustit. Pokud je každý řez stejně nezbytný, rozdělení prioritizaci nepomohlo.

### Akceptační kritéria [P1]
Akceptační kritéria jsou podmínky, které musí story splnit, aby ji product owner přijal. Vymezují rozsah story, vedou vývoj a stávají se základem testovacích případů.

**Rule-based (kontrolní seznam):**
Story: *As an exporter, I want to upload documents to my claim notification, so that ExportShield can check my claim without e-mail exchange.*
- Přijímané typy souborů: PDF, JPG, PNG.
- Maximální velikost: 10 MB na soubor, nejvýš 20 souborů na jedno hlášení.
- Každému souboru se musí přiřadit typ dokumentu: faktura, upomínka, doklad o doručení, jiné.
- Nahrané soubory se ukládají do DocVault a propojí se s číslem škody.
- Exportér může soubor odebrat, dokud hlášení neodešle.

**Scenario-based (Gherkin):** popsáno v další části.

Dobrá AC jsou testovatelná, popisují chování, ne implementaci, zahrnují důležité negativní případy a odpovídají velikosti story (typicky 3–8 kritérií; 20 naznačuje, že by se story měla rozdělit). AC nejsou Definition of Done: AC platí pro jednu konkrétní story, DoD pro všechny.

### Gherkin: Given / When / Then [P1]
**Gherkin** je strukturovaný jazyk pro popis chování formou scénářů. Používá se v BDD (Behavior-Driven Development, vývoj řízený chováním), kde se scénáře píšou před vývojem a nástroje jako Cucumber je umí spouštět jako automatické testy. I bez automatizace je Gherkin přehledný formát pro AC.

Struktura:
- **Feature** – popisovaná schopnost.
- **Background** – kroky Given, které se spustí před každým scénářem dané feature.
- **Scenario** – jeden konkrétní příklad.
- **Given** – výchozí stav (kontext).
- **When** – akce nebo událost.
- **Then** – očekávaný výsledek.
- **And / But** – pokračují typem předchozího kroku.

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

**Scenario Outline** spustí stejný scénář s několika řádky dat z tabulky **Examples**. Hodí se na business pravidla s hraničními hodnotami:

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

Hranice výše jsou fiktivní. Všimni si, že příklady záměrně testují hodnoty na obou stranách každé hranice; je to stejná myšlenka jako analýza hraničních hodnot (boundary value analysis) v testování (modul 13).

Tipy k psaní:
- Jedno chování na scénář. Pokud potřebuješ hodně kroků „When“, jde nejspíš o několik scénářů.
- Popisuj business chování, ne kliknutí: „When the exporter submits the notification“, ne „When the user clicks the button with id btnSubmit“.
- Používej konkrétní příkladová data; odhalí otázky („Je přesně 50 000 ještě v limitu likvidátora?“).
- Drž jazyk domény (pojmy z glosáře) jednotný napříč scénáři.

### Definition of Ready a Definition of Done [P1]
**Definition of Ready (DoR)** je dohoda týmu o tom, co story potřebuje, než vstoupí do sprintu. Ve Scrum Guide není, ale mnoho týmů ji používá. Příklad:
- Story napsaná ve formě role–schopnost–přínos, napojená na epic.
- Akceptační kritéria odsouhlasená s product ownerem.
- Závislosti (jiné týmy, dodavatel, data) identifikované a vyřešené nebo naplánované.
- U UI přiložený wireframe nebo odkaz na specifikaci.
- Odhadnutá týmem; dost malá na sprint.

**Definition of Done (DoD)** definuje Scrum Guide jako formální popis stavu Incrementu, když splňuje míry kvality požadované pro produkt. Příklad:
- Kód prošel review a je sloučený (merged).
- Všechna akceptační kritéria otestovaná a splněná v testovacím prostředí.
- Žádné otevřené kritické ani závažné defekty.
- Aktualizovaná uživatelská dokumentace nebo release notes.
- Product owner story přijal.

Většinu checklistu DoR v praxi obvykle drží BA: když story není ready, často je to proto, že chybí analýza.

### Backlog refinement a odhadování [P1]
**Backlog refinement** (dříve „grooming“) je průběžná činnost: doplňování detailů, dělení, řazení a odhadování položek backlogu. Mnoho týmů má jednou týdně setkání na 1–2 hodiny. Dobrý rytmus pro BA je mít připravené stories na další dva sprinty a ty po nich zhruba promyšlené.

Tvoje role v refinementu:
- Představ stories s kontextem a AC; odpovídej na otázky.
- Zapisuj otevřené otázky a vezmi je zpět ke stakeholderům.
- Rozděl příliš velké stories.
- Dohlédni, aby byly vidět závislosti a nefunkční aspekty.

**Story points** jsou relativní jednotka pracnosti, složitosti a nejistoty. Tým si vybere referenční story („nahrání jedné faktury = 3 body“) a ostatní s ní porovnává. Mnoho týmů používá upravenou Fibonacciho řadu (1, 2, 3, 5, 8, 13, 20…). Rostoucí mezery odrážejí rostoucí nejistotu. **Planning poker** je běžná technika: každý vývojář ukáže kartu ve stejnou chvíli a velké rozdíly se proberou.

Pro BA důležité: **odhadují vývojáři**, protože práci dělají oni. BA vyjasňuje rozsah. Když se tě někdo zeptá „kolik bodů to je?“, správná odpověď je „zeptejme se týmu“. **Velocity** (počet bodů dokončených za sprint) pomáhá týmu plánovat, ale není to metrika výkonu a nedá se porovnávat mezi týmy.

### User story mapping [P2]
**User story map** (mapa user stories, zpopularizoval ji Jeff Patton) uspořádá stories ve dvou rozměrech:
- Vodorovně: cesta uživatele, činnosti v pořadí („backbone“, páteř).
- Svisle: stories pod každou činností, seřazené podle priority.

Vodorovná čára přes mapu označuje první release (často MVP, minimum viable product: nejmenší verze, která dodá hodnotu a umožní se učit). Vše nad čarou je v releasu.

Příklad páteře pro portál škod: *Log in → Start notification → Select buyer and invoice → Upload documents → Submit → Track status → Respond to questions*. Pod „Upload documents“: nahrání PDF (release 1), přiřazení typu dokumentu (release 1), drag and drop (release 2), nahrání z fotoaparátu v mobilu (později).

Story mapping se dělá na workshopu se stakeholdery a týmem, na zdi nebo na tabuli v [Miro](https://miro.com/). Předchází běžnému problému backlogu: plochý seznam 200 stories, ve kterém nikdo nevidí celou cestu ani to, co je první použitelný release.

### Product owner a business analytik [P1]
| Aspekt | Product owner | Business analytik |
|---|---|---|
| Odpovědnost | Maximalizace hodnoty produktu, pořadí backlogu, přijímání práce | Kvalita analýzy: pochopení potřeb, definice požadavků |
| Kde je definován | Scrum Guide | BABOK, není součástí Scrumu |
| Typické úkoly | Product goal, priority, rozhodnutí se stakeholdery, přijímání stories | Elicitace, modelování, psaní stories a AC, vyjasňování detailů, podpora testování |
| Rozhoduje | Co se postaví a v jakém pořadí | Navrhuje, dokumentuje, doporučuje |

PO je jeden člověk, který rozhoduje; BA často pracuje pro PO nebo s ním. V nastavení klient–dodavatel může mít PO i BA klient, kdežto vývojáře má dodavatel. V malých firmách může obě role zastávat jeden člověk. Na pohovoru ukaž, že rozdíl znáš a že ti vyhovuje obojí.

### Základy Jiry [P1]
Jira (od firmy Atlassian) je nejrozšířenější nástroj pro správu backlogů. [Jira Free](https://www.atlassian.com/software/free) je zdarma až pro 10 uživatelů, takže si ji můžeš vyzkoušet.

**Základní pojmy:**
- **Project** (projekt) – kontejner pro issues s klíčem, například `CLM`. Issues dostávají ID jako `CLM-42`.
- **Issue types** (typy issues) – Epic, Story, Task, Bug, Sub-task (dají se konfigurovat).
- **Fields** (pole) – summary, description, assignee, priority, labels, components, fix version, story points, vlastní pole (custom fields).
- **Workflow** – stavy, kterými issue prochází, a povolené přechody, například *To Do → In Progress → In Review → Testing → Done*.
- **Board** (nástěnka) – sloupce namapované na stavy. **Scrum board** se sprinty, nebo **Kanban board** s průběžným tokem.
- **Backlog** – seřazený seznam issues, které ještě nejsou ve sprintu.
- **Sprint** – časově ohraničená sada issues vzatých z backlogu.
- **Links** (vazby) – například „blocks“, „relates to“, „duplicates“; používají se pro závislosti a dohledatelnost. Aplikace pro test management v Jiře (například Xray nebo Zephyr) přidávají vazby jako „is tested by“.

**JQL (Jira Query Language)** umožňuje filtrovat issues. Podobá se klauzuli WHERE v SQL (modul 10):

```sql
project = CLM AND status = "In Progress"
project = CLM AND issuetype = Story AND "Epic Link" = CLM-1
project = CLM AND status != Done AND assignee = currentUser()
project = CLM AND labels = portal AND created >= -14d ORDER BY priority DESC
project = CLM AND issuetype = Bug AND priority in (Highest, High) AND resolution = Unresolved
```

Názvy polí se můžou lišit podle verze a konfigurace Jiry (například novější cloudové projekty používají `parent` místo `"Epic Link"`). Vyhledávací pole v Jiře při psaní nabízí pole. Uložené filtry se dají sdílet a zobrazit na dashboardech, a tak BA a projektoví manažeři reportují stav.

**Confluence** je wiki od Atlassianu. Týmy v ní drží specifikace, zápisy ze schůzek, logy rozhodnutí, glosáře a procesní diagramy. Běžná praxe: jedna stránka v Confluence na epic nebo feature s kontextem, procesem, pravidly a wireframy a na ni napojené stories v Jiře. Confluence nabízí i šablony pro produktové požadavky, zápisy ze schůzek a retrospektivy.

### Stories a specifikace v hybridních a dodavatelských projektech [P1]
Mnoho skutečných projektů není čistý Scrum. Například ExportShield si najme NovaSoft na rozšíření PolicyHubu. Smlouva potřebuje definovaný rozsah a cenu, takže existuje podepsaná funkční specifikace (modul 06). Dodávka přesto probíhá ve sprintech s backlogem v Jiře.

Jak to do sebe zapadá:
1. Specifikace definuje rozsah, požadavky s ID, business pravidla, NFRs a integrace.
2. Epicy v Jiře odpovídají hlavním sekcím specifikace nebo features.
3. Stories rozdělují každou sekci na dodatelné kusy. Každá story odkazuje na ID požadavků, které implementuje („Implements FR-003, FR-004“).
4. AC ve stories jsou v souladu se specifikací; pokud se v refinementu doplní detail, promítne se do specifikace nebo se zapíše jako rozhodnutí.
5. Změny rozsahu jdou přes change request (smluvně) a pak do backlogu.
6. Testeři navazují testovací případy na stories a požadavky; UAT reportuje pokrytí vůči specifikaci.

Rizika: specifikace a backlog se rozejdou, nebo dodavatel bere jako smlouvu backlog, zatímco klient specifikaci. Hned na začátku se dohodněte, který dokument při rozporu platí.

## Key terms
- **Agile** (agilní přístup) — přístup k dodávce v krátkých iteracích s častou zpětnou vazbou a přizpůsobováním.
- **Scrum** — agilní framework se sprinty, třemi accountabilities a definovanými událostmi, popsaný ve Scrum Guide.
- **Product backlog** — seřazený seznam všeho, co by se pro produkt mohlo postavit.
- **Epic** — velký celek práce, který se dělí na menší stories.
- **User story** (uživatelský příběh) — krátký popis schopnosti z pohledu uživatele ve formě „As a…, I want…, so that…“.
- **INVEST** — kontrolní seznam pro dobré stories: Independent, Negotiable, Valuable, Estimable, Small, Testable.
- **Vertical slice** (vertikální řez) — rozdělení story, které prochází všemi vrstvami a samo o sobě dodá použitelnou hodnotu.
- **Acceptance criteria (AC)** (akceptační kritéria) — podmínky, které musí konkrétní story splnit, aby byla přijata.
- **Gherkin** — strukturovaný jazyk pro scénáře s kroky Given, When a Then.
- **Scenario Outline** — šablona scénáře v Gherkinu, která se spustí s více řádky příkladových dat.
- **Definition of Ready (DoR)** — dohoda týmu o tom, co story potřebuje, než může vstoupit do sprintu.
- **Definition of Done (DoD)** — kritéria kvality, která musí splnit každý increment, aby byl považován za hotový.
- **Backlog refinement** — průběžné vyjasňování, dělení, řazení a odhadování položek backlogu.
- **Story points** — relativní odhad pracnosti, složitosti a nejistoty, který dělají vývojáři.
- **Velocity** — množství práce, obvykle ve story points, které tým dokončí za sprint.
- **User story map** (mapa user stories) — dvourozměrné uspořádání stories podle cesty uživatele a priority, používané k plánování releasů.
- **MVP** — minimum viable product, nejmenší verze, která dodá hodnotu a umožní se učit.
- **Product owner** — accountability ve Scrumu za maximalizaci hodnoty produktu a pořadí backlogu.
- **JQL** — Jira Query Language, dotazovací jazyk pro filtrování issues.
- **Confluence** — wiki od Atlassianu pro specifikace, zápisy ze schůzek a týmovou dokumentaci.

## Hands-on
:::exercise id="m07-e1" title="Napiš 6 stories s akceptačními kritérii pro portál škod" min="60" tool="text editor"
Cíl: napsat malou, ucelenou sadu user stories pro portál ExportShield na hlášení škod.

1. Vypiš zapojené role: exportér, likvidátor škod (claims handler), vedoucí škod (head of claims).
2. Napiš 6 user stories ve formě „As a…, I want…, so that…“. Alespoň dvě musí být pro likvidátora.
3. Každou zkontroluj podle INVEST a ty, které neprojdou, přepiš.
4. Ke každé story napiš 3–6 akceptačních kritérií. Aspoň u tří stories použij styl rule-based a aspoň u dvou Given/When/Then.
5. U každé story uveď alespoň jeden negativní případ (neplatný vstup, chybějící data, chybějící oprávnění).
6. Poznamenej si otevřené otázky, které bys vzala za product ownerem.

Hotovo, když: každá story jmenuje konkrétní roli a přínos, každá se dá otestovat jen podle svých AC a žádná z nich není technický task.
:::

:::exercise id="m07-e2" title="Rozděl přerostlý epic" min="40" tool="Miro / paper"
Cíl: procvičit vertikální dělení a plánování releasu.

Epic: *„As a head of claims, I want a claims dashboard, so that I can manage the workload of my team.“*

1. Zapiš cestu vedoucího škod jako 4–6 činností (páteř story mapy).
2. Pod každou činnost napiš stories s použitím alespoň tří různých vzorů dělení (kroky workflow, business pravidla, varianty dat, šťastná/chybová cesta, CRUD, odložení výkonu).
3. Vytvoř alespoň 10 stories. Seřaď je svisle podle priority.
4. Nakresli čáru releasu pro MVP, které bys dodala za dva sprinty.
5. U každé story nad čarou napiš jednu větu, proč je v MVP.

Hotovo, když: každá story nad čarou dodá něco, co vedoucí škod může použít, a nic nad čarou není čistě technický task.
:::

:::exercise id="m07-e3" title="Založ projekt v Jiře (nebo v Trellu)" min="60" tool="Jira Free / Trello"
Cíl: vyzkoušet si v praxi nástroj, který budeš používat denně.

1. Založ si zdarma účet na [Jira Free](https://www.atlassian.com/software/free) (nebo použij [Trello](https://trello.com/), pokud chceš jednodušší nástroj). Používej jen fiktivní data.
2. Vytvoř Scrum projekt s názvem „Claims Portal“ a klíčem `CLM`.
3. Vytvoř jeden epic „Online claim notification“ a zadej svých 6 stories ze cvičení m07-e1, s AC v popisu, napojené na epic.
4. K jedné story přidej sub-tasky (například „Design upload form“, „Implement validation“, „Write test cases“).
5. Odhadni stories ve story points (hraj si na tým) a seřaď backlog.
6. Vytvoř sprint, přesuň do něj 3 stories, spusť ho a posuň jednu story přes board.
7. Podívej se na workflow a přidej stav „Testing“ mezi „In Progress“ a „Done“, pokud to typ projektu dovolí.
8. Napiš a ulož JQL filtr: `project = CLM AND status = "In Progress"`. Pak napiš ještě jeden vlastní filtr.

Hotovo, když: máš backlog, běžící sprint, board s alespoň jednou posunutou story a dva uložené filtry. V Trellu: seznamy pro backlog, sprint, in progress, testing, done, s labely pro epicy.
:::

:::exercise id="m07-e4" title="Napiš tři scénáře v Gherkinu" min="30" tool="text editor"
Cíl: napsat přesná akceptační kritéria ve formě scénářů.

Story: *As an exporter, I want to notify a non-payment online, so that the claim process starts without paper forms.* Business pravidlo (fiktivní): nezaplacení se musí nahlásit nejpozději 60 dní po původní splatnosti faktury.

1. Napiš hlavičku Feature a Background s přihlášeným exportérem.
2. Scénář 1: úspěšné nahlášení v rámci lhůty.
3. Scénář 2: nahlášení po lhůtě odmítnuto, s přesnou hláškou.
4. Scénář 3: Scenario Outline s tabulkou Examples, která testuje lhůtu v den 59, 60 a 61, a očekávaný výsledek pro každý z nich.
5. Kontrola: business jazyk, žádná ID prvků UI, jedno chování na scénář.

Hotovo, když: tester by mohl všechny tři scénáře provést, aniž by se tě na cokoli ptal, a outline pokrývá obě strany hranice lhůty.
:::

## Self-check
:::q
Co je špatně na story „As a developer, I want to create a database table for claims“?
---
Sama o sobě nedodává uživateli žádnou hodnotu a popisuje implementaci místo potřeby. Je to technický task, který patří pod user story, například „As an exporter, I want to save a draft claim notification, so that I can finish it later.“
:::

:::q
Proč dělit stories vertikálně, a ne horizontálně?
---
Vertikální řez prochází všemi vrstvami a dodá něco, co uživatel může vyzkoušet a použít. Horizontální rozdělení, například „postav databázi“ a „postav UI“, vytvoří kusy, které samy o sobě nemají hodnotu, product owner je nemůže přijmout samostatně a integrační problémy se schovají až na konec.
:::

:::q
Jaký je rozdíl mezi akceptačními kritérii a Definition of Done?
---
Akceptační kritéria platí pro jednu konkrétní story a popisují chování, které musí ukázat. Definition of Done platí pro každou položku a popisuje obecné podmínky kvality, například code review, otestováno v testovacím prostředí a aktualizovaná dokumentace. Story je hotová, až když platí obojí.
:::

:::q
Kdy bys použila Scenario Outline místo několika scénářů?
---
Když se stejné chování musí ověřit s různými hodnotami dat, například s hranicemi částek nebo lhůt. Outline drží jednu sadu kroků a varianty dává do tabulky Examples, což je kratší a testované hodnoty se snadno zkontrolují.
:::

:::q
Kdo odhaduje story points a jaká je při odhadování role BA?
---
Odhadují vývojáři, protože práci budou dělat oni. BA story vysvětluje, odpovídá na otázky, vyjasňuje rozsah a pomáhá rozdělit stories, které jsou na odhad příliš velké nebo nejasné.
:::

:::q
Jaký problém řeší user story map oproti plochému backlogu?
---
Plochý seznam schovává cestu uživatele a je z něj těžké poznat, které stories dohromady tvoří použitelný release. Story map ukazuje cestu vodorovně a priority svisle, takže tým může nakreslit čáru releasu a nejdřív dodat úplný, i když minimální tok od začátku do konce.
:::

:::q
Jak v dodavatelském projektu udržíš user stories v souladu s podepsanou funkční specifikací?
---
Každou story propoj s ID požadavků, které implementuje, drž AC v souladu se specifikací, rozhodnutí z refinementu zapisuj a aktualizuj specifikaci nebo log rozhodnutí a změny rozsahu posílej přes change requesty. Hned na začátku se dohodněte, který dokument má při rozporu přednost.
:::

## Interview corner
:::interview
Napiš user story s akceptačními kritérii pro nahrávání dokumentů ke škodě.
*EN: Write a user story with acceptance criteria for uploading documents to a claim.*
---
- Konkrétní role, schopnost a přínos: „As an exporter, I want to upload…, so that…“.
- 3–6 AC: povolené typy souborů, limit velikosti, typ dokumentu, kam se soubor uloží, chování při chybě.
- Aspoň jeden scénář Given/When/Then pro negativní případ.
- Zmiň otevřené otázky, které bys vyjasnila (antivirová kontrola, maximální počet souborů).

Typická chyba: napsat jen větu story bez akceptačních kritérií, nebo AC, která popisují rozložení UI místo chování.
:::

:::interview
Co znamená INVEST a které písmeno se v praxi porušuje nejčastěji?
*EN: What does INVEST mean, and which letter is most often violated in practice?*
---
- Independent, Negotiable, Valuable, Estimable, Small, Testable, každé s krátkým vysvětlením.
- Nejčastěji porušované: Small (příliš velké stories) a Valuable (technické tasky napsané jako stories); Independent se plně dosahuje těžko.
- Ukaž, jak bys to opravila: vzory dělení, přepsání z pohledu uživatele.

Typická chyba: odříkat zkratku bez jediného příkladu, jak ji použít.
:::

:::interview
Jaký je rozdíl mezi product ownerem a business analytikem?
*EN: What is the difference between a product owner and a business analyst?*
---
- PO: accountability ve Scrumu, maximalizuje hodnotu produktu, řadí backlog, rozhoduje a přijímá práci.
- BA: analytická disciplína (BABOK), elicitace, modelování, stories a AC, podpora PO a týmu.
- V praxi se role překrývají nebo slučují; v dodavatelských projektech můžou být obě na straně klienta.
- Ty podporuješ rozhodnutí PO analýzou.

Typická chyba: říct, že jde o stejné role, nebo že BA rozhoduje o prioritách.
:::

:::interview
Jak bys rozdělila story, která je na jeden sprint příliš velká?
*EN: How would you split a story that is too large for one sprint?*
---
- Vertikálně, každý řez dodá hodnotu.
- Jmenuj vzory: kroky workflow, business pravidla, varianty dat, šťastná/chybová cesta, CRUD, odložení výkonu.
- Uveď konkrétní příklad z domény, kterou znáš.
- Ověř, že PO může řezy prioritizovat nezávisle.

Typická chyba: dělit podle technických vrstev (front end, back end, databáze).
:::

:::interview
Jak jako BA používáš Jiru a Confluence?
*EN: How do you use Jira and Confluence as a BA?*
---
- Jira: epicy a stories s AC, vazby na požadavky a závislosti, řazení backlogu s PO, sprinty, board.
- JQL filtry a dashboardy pro reporting stavu, například otevřené bugy podle priority.
- Confluence: specifikace, procesní diagramy, log rozhodnutí, zápisy ze schůzek, glosář, propojené s issues v Jiře.
- Jeden zdroj pravdy; propojuj, nekopíruj.

Typická chyba: říct jen „používala jsem Jiru“ a nepopsat, co jsi v ní dělala.
:::
