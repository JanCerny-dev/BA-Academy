---
id: 16
slug: communication-stakeholders
title: Stakeholdeři, komunikace, prezentace a školení
phase: E
priority: P2
quick_min: 5
deep_min: 35
job_ad: "spolupráce s dodavateli a stakeholdery, reporting stavu, prezentace a školení kolegů"
---

## Why this matters
Business analytik stráví víc času mluvením, psaním a prezentováním než modelováním. Požadavky přicházejí od lidí, rozhodují lidé a řešení má smysl, jen když ho lidé začnou používat. Cílový inzerát chce spolupráci s dodavateli a stakeholdery, reporting stavu a prezentace a školení kolegů. Tento modul ti ke každému z toho dá praktické nástroje: koho zapojit, jak vést poradu, jak reportovat, jak prezentovat doporučení a jak naučit kolegy nový proces.

## Quick version
**Stakeholdeři.** *Stakeholder* je každý, koho změna zasáhne nebo kdo ji může ovlivnit. Když na někoho zapomeneš na začátku (třeba na compliance nebo na tým podpory dodavatele), obvykle to znamená pozdní překvapení.

**Analýza stakeholderů:**
- **Power/interest grid** (mřížka vliv/zájem) — každého stakeholdera umístíš podle vlivu (power, schopnost ovlivnit rozhodnutí) a zájmu (interest, nakolik se ho změna týká nebo zajímá). Vysoký vliv a vysoký zájem: manage closely (úzce řídit). Vysoký vliv, nízký zájem: keep satisfied (udržovat spokojené). Nízký vliv, vysoký zájem: keep informed (průběžně informovat). Nízký vliv, nízký zájem: monitor (sledovat).
- **RACI matrix** (matice RACI) — pro každý úkol nebo rozhodnutí: kdo je **R**esponsible (odpovědný za provedení, dělá práci), **A**ccountable (vlastní výsledek, vždy jedna osoba), **C**onsulted (konzultovaný, dává vstup předem), **I**nformed (informovaný, dozví se potom).
- **Onion diagram** (cibulový diagram) — soustředné kruhy: uprostřed řešení, pak lidé, kteří ho přímo používají, pak širší organizace, pak externí strany (klienti, regulátoři, dodavatelé).

**Communication plan** (komunikační plán). Jednoduchá tabulka: kdo, jaké informace, jak často, jakým kanálem, kdo je posílá. Brání tichu i zahlcení.

**Porady a workshopy.** Každá porada potřebuje účel, agendu s časy, správné lidi a dohodnuté výstupy. Rozděl role: facilitátor, zapisovatel, hlídač času, rozhodovatel. Na konci shrň rozhodnutí a action items (úkoly: co, kdo, do kdy).

**Protichůdné požadavky a říkání ne.** Zviditelni konflikt fakty, každou možnost propoj s cíli businessu a eskaluj na toho, kdo má pravomoc rozhodnout. „Ne“ se přijímá snáz jako „teď ne, protože…“ s nabídnutým kompromisem: „Můžeme to přidat, ale pak se X posune do dalšího release.“

**Řízení dodavatelů na poradách.** Agendu domluv předem, pro otázky k požadavkům drž jeden kanál, nový rozsah nikdy neodsouhlas ústně (pošli ho do change requestu), vše potvrď písemně.

**Status reporting** (reportování stavu). Používej **RAG status** (Red, Amber, Green; červená, oranžová, zelená) pro rozsah, harmonogram, rozpočet a kvalitu. Dobrý týdenní report se vejde na jednu stránku: celkový stav, co se udělalo, co bude dál, rizika a problémy, potřebná rozhodnutí.

**Prezentace řešení.** Struktura: **problém → možnosti → doporučení → žádost**. Pro netechnické publikum se zaměř na dopad, cenu a riziko. Pro technické publikum přidej, jak to funguje, rozhraní, data a omezení. Vždy skonči jasnou žádostí: jaké rozhodnutí nebo akci potřebuješ.

**Školení kolegů.** Začni výukovými cíli („po tomto školení umíte…“), ukaž krátké demo, nech lidi si to vyzkoušet na testovacích datech a rozdej jednostránkový tahák.

**Psaní.** Jasný e-mail má žádost v prvních dvou řádcích. Zápis z porady zachycuje rozhodnutí a action items, ne přepis rozhovoru. Zápis pošli do 24 hodin a požádej o připomínky do stanoveného data, aby se dohody neztratily nebo se později znovu neotevíraly.

## Deep dive

### Identifikace stakeholderů [P1]
Začni široce, pak zužuj. Pomáhají tyto otázky:
- Kdo každý den používá současný proces nebo systém?
- Kdo dostává jeho výstupy? Kdo dodává jeho vstupy?
- Kdo změnu platí? Kdo ji schvaluje?
- Kdo ji musí zkontrolovat z hlediska compliance, bezpečnosti, ochrany dat nebo rizik?
- Kdo ji staví, testuje, provozuje a podporuje (interní IT, dodavatel)?
- Koho mimo firmu se týká (klienti, partneři, regulátoři)?

Pro projekt ExportShield „automatizace příjmu škod“ může seznam vypadat takto:

| Stakeholder | Vztah ke změně |
|---|---|
| Head of Claims (sponzor) | Financuje projekt, vlastní výsledek pro business |
| Likvidátoři (claims handlers) | Denní uživatelé ClaimDesk, hlavní zdroj požadavků |
| Manažer likvidace (claims manager) | Schvaluje škody, určuje schvalovací pravidla |
| Exportéři (klienti) | Podávají hlášení; zažijí nový formulář |
| Finance | Vyplácí plnění; potřebuje správné částky a účetní údaje |
| Tým vymáhání (recovery) | Po výplatě přebírá vymáhání po odběrateli |
| Compliance / pověřenec pro ochranu osobních údajů | Kontroluje nakládání s osobními a klientskými daty |
| IT provoz | Provozuje ClaimDesk a DocVault, spravuje přístupy |
| NovaSoft s.r.o. (dodavatel) | Staví a podporuje integraci |
| Interní audit | Později může kontroly prověřit |

Seznam udělej brzy a vracej se k němu. Stakeholdeři se během projektu mění.

### Power/interest grid [P1]
Každého stakeholdera umísti do jednoho ze čtyř polí. Pozice říká, kolik úsilí mu věnovat.

| | Nízký zájem | Vysoký zájem |
|---|---|---|
| **Vysoký vliv** | Keep satisfied: krátké cílené informace; zapojit u klíčových rozhodnutí (např. finanční ředitel, ředitel IT) | Manage closely: pravidelné zapojení, včasné konzultace (např. Head of Claims, manažer likvidace) |
| **Nízký vliv** | Monitor: minimální, obecná komunikace (např. interní audit, než přijde na řadu) | Keep informed: pravidelné informace, zapojit do testování (např. likvidátoři, tým vymáhání) |

Poznámky:
- Vliv není jen hierarchie. Compliance officer, který může zastavit go-live, má na tomto projektu vysoký vliv.
- Pozice se posouvají. Finance může mít nízký zájem, dokud se nezačne sahat na výpočet plnění; pak vysoký.
- Lidé s nízkým vlivem a vysokým zájmem (často koncoví uživatelé) jsou nejlepší zdroj detailů a tvoji budoucí uživatelé. „Keep informed“ neber jako „ignorovat“.

### RACI [P1]
RACI ujasňuje, kdo co dělá u každé činnosti nebo výstupu. Klíčové pravidlo: **na každém řádku právě jedno A.** R může být víc.

| Činnost | Head of Claims | Manažer likvidace | BA | Likvidátoři | NovaSoft | Compliance | IT provoz |
|---|---|---|---|---|---|---|---|
| Schválit business case | A | C | R | I | I | C | I |
| Definovat pravidla schvalování škod | A | R | C | C | I | C | I |
| Napsat požadavky a user stories | I | C | A/R | C | C | C | C |
| Postavit integraci | I | I | C | I | A/R | I | C |
| Posouzení ochrany osobních údajů | I | I | C | I | C | A/R | C |
| Provedení UAT | I | A | R | R | C | I | I |
| Rozhodnutí o go-live | A | C | C | I | C | C | R |

Typické problémy, které RACI odhalí: dva lidé si myslí, že jsou accountable; nikdo není accountable; konzultuje se příliš mnoho lidí, což zpomaluje rozhodování.

### Onion diagram [P3]
Cibulový diagram ukazuje, jak blízko má každá skupina k řešení. Kruhy zevnitř ven:
1. **Řešení** (nový formulář pro příjem škod a integrace).
2. **Lidé, kteří ho obsluhují** (likvidátoři, IT provoz).
3. **Širší business**, kterého se dotýká (finance, vymáhání, vedení).
4. **Externí strany** (exportéři, dodavatel, regulátor).

Je to rychlý obrázek na kick-off slide: každý vidí, že změna se netýká jen týmu likvidace.

### Komunikační plán [P2]
Komunikační plán je krátká tabulka. Z dobrých úmyslů udělá rutinu.

| Publikum | Informace | Frekvence | Kanál | Kdo posílá |
|---|---|---|---|---|
| Sponzor (Head of Claims) | Stav, potřebná rozhodnutí, rizika | Týdně | Jednostránkový report + 15min hovor | BA / projektový manažer |
| Řídicí výbor (steering committee) | Postup proti plánu, rozpočet, hlavní rizika | Měsíčně | Porada se slidy | Projektový manažer |
| Likvidátoři | Co se mění, kdy, co od vás potřebujeme | Každé 2 týdny | Slot na poradě týmu, krátký e-mail | BA |
| NovaSoft | Upřesnění požadavků, priority | Průběžně / týdně | Jira, týdenní hovor | BA |
| Compliance | Toky dat, přístupy, doba uchování | Při návrhu a před go-live | Schůzka, písemné posouzení | BA + compliance |
| Exportéři | Nový formulář hlášení | Před go-live | E-mail, oznámení na webu | Business / marketing |

Tip: s každým stakeholderem s vysokým vlivem se domluv, *jak* chce být informován. Někdo čte reporty, někdo chce pětiminutový hovor.

### Facilitace porad a workshopů [P1]
**Před:**
- Definuj účel jednou větou a očekávaný výstup (například „odsouhlasený seznam povinných dokumentů podle produktu“).
- Pozvi jen lidi, kteří jsou pro ten výstup potřeba. Agendu a podklady k přečtení pošli 2–3 pracovní dny předem.
- Připrav materiály: návrh procesu, seznam otevřených otázek, tabuli v Miru.

**Příklad agendy (60minutový workshop):**

| Čas | Bod | Výstup |
|---|---|---|
| 0–5 | Účel, agenda, role | Společné pochopení |
| 5–20 | Projít současné hlášení škody (AS-IS) | Opravy návrhu |
| 20–40 | Povinné dokumenty podle produktu: brainstorming a dohoda | Návrh kontrolního seznamu |
| 40–50 | Otevřené otázky a hraniční případy | Seznam s vlastníky |
| 50–60 | Shrnutí rozhodnutí a úkolů | Odsouhlasené action items |

**Role:**
- **Facilitator** (facilitátor) — řídí průběh, drží fokus, dbá, aby se dostal ke slovu každý. Ideálně je k obsahu neutrální.
- **Note-taker** (zapisovatel) — zapisuje rozhodnutí, úkoly a otevřené otázky, ne každou větu.
- **Timekeeper** (hlídač času) — upozorní, když bod přetahuje.
- **Decision-maker** (rozhodovatel) — osoba, která může rozhodnutí na místě potvrdit. Když chybí, označ výsledky jako návrhy.

**Techniky:**
- **Round robin** (kolečko) — každý postupně řekne jeden bod; nejhlasitější hlas tak nepřehluší ostatní.
- **Silent brainstorming** (tichý brainstorming) — každý pět minut píše nápady na lepicí papírky, teprve pak se diskutuje.
- **Dot voting** (hlasování tečkami) — každý účastník dostane tři hlasy na označení priorit.
- **Parking lot** (odkladiště) — viditelný seznam bodů mimo téma, aby se neztratily a nerozhodily poradu.
- **Walkthrough** (průchod) — projdeš proces nebo obrazovku krok za krokem a ptáš se „co se stane, když…?“.

**Po:** pošli zápis do 24 hodin (viz část o psaní níže).

### Protichůdné požadavky a říkání ne [P1]
Konflikty jsou normální. Likvidátoři chtějí méně povinných polí; compliance chce víc dat; finance chce datum platby, které dodavatel označuje za těžko proveditelné.

Praktický postup:
1. **Zviditelni ho.** Napiš oba požadavky vedle sebe s jejich zdrojem a důvodem.
2. **Vrať se k cíli.** Která možnost lépe podporuje business požadavek a definici problému?
3. **Hledej třetí možnost.** Povinné pole jen nad určitou výší škody? Data převzatá z jiného systému místo ručního zadání?
4. **Ukaž kompromis v číslech nebo riziku.** Čas na škodu, regulatorní expozice, cena.
5. **Eskaluj na rozhodovatele** určeného v RACI. BA rozhodnutí připraví; accountable osoba rozhodne.
6. **Zapiš rozhodnutí** i jeho důvod, aby se příští měsíc znovu neotevíralo.

Jak říct ne a nepoškodit vztah:
- Nahraď „ne“ volbou: „Můžeme to přidat do tohoto release, když posuneme story s reportingem do dalšího. Co je pro vás důležitější?“
- Odkaž na dohodnutá pravidla: rozsah, proces change requestů, regulace.
- Uznej potřebu, i když řešení odmítáš: „Rozumím, že potřebujete vidět stav. Tlačítko pro export v rozsahu není, ale dashboard plánovaný na červen to pokryje.“

### Řízení dodavatelů na poradách [P2]
U externího dodavatele, jako je NovaSoft, mohou mít slova na poradě smluvní důsledky.

- **Agendu domluv předem** a otevřené otázky pošli před hovorem, aby dodavatel přivedl správné lidi.
- **Odděl upřesnění od nového rozsahu.** Upřesnit existující požadavek je normální. Cokoli nového jde přes change request.
- **Neslibuj za jiné.** „Ověřím to s manažerem likvidace a potvrdím do čtvrtka“ je lepší než improvizovaná odpověď.
- **Potvrzuj písemně.** Po každém hovoru pošli krátké shrnutí: rozhodnutí, otevřené body, vlastníci.
- **Drž jeden zdroj pravdy** (Jira, Confluence nebo specifikace). Rozhodnutí dohodnutá v chatu nebo po telefonu se tam musí přepsat.
- **Respekt a pevnost zároveň.** Dodavatelé pracují lépe s klientem, který je jasný a konzistentní, než s takovým, který je přátelský, ale každý týden mění směr.

### Status reporting a RAG [P1]
**RAG status** označuje každou oblast:
- **Green** (zelená) — podle plánu; od vedení není potřeba žádná akce.
- **Amber** (oranžová) — ohroženo; tým má plán, jak se vrátit do plánu, ale vedení by o tom mělo vědět.
- **Red** (červená) — mimo plán; je potřeba rozhodnutí nebo pomoc vedení.

Pravidla poctivého RAG: prahy definuj předem (například Amber = zpoždění milníku až o dva týdny); nikdy neukazuj zelenou, když víš, že je to oranžová; a u každé oranžové nebo červené řekni, co potřebuješ.

**Šablona týdenního status reportu (jedna stránka):**

```text
Project: ClaimDesk claim intake automation        Week: 2026-W44
Overall status: AMBER                             Prepared by: BA

Scope: GREEN     Schedule: AMBER     Budget: GREEN     Quality: GREEN

Summary (2-3 sentences)
UAT preparation is on track. The integration with DocVault is one week late
because the vendor is waiting for test environment access.

Done this week
- Requirements for document checklist signed off by claims manager
- 6 of 8 user stories for Sprint 4 refined and estimated
- UAT scenarios drafted (12 scenarios)

Planned next week
- Sprint 4 review with claims handlers
- Finalize UAT test data (fictional, anonymized)

Risks and issues
| ID | Description | Impact | Owner | Action | Due |
| R3 | No TEST access for vendor to DocVault | 1 week delay | IT ops | Access request escalated | 05/11 |

Decisions needed
- Sponsor: approve CR-07 (buyer turnover field), cost estimate attached, by 06/11

Milestones
- UAT start: 18/11 (was 11/11)   - Go-live: 09/12 (unchanged)
```

Co dělá report dobrým: je krátký, má každý týden stejnou strukturu, obsahuje fakta a data a potřebná rozhodnutí jsou nahoře nebo zvýrazněná. Co ho kazí: dlouhé vyprávění, všechno zelené, dokud to najednou nezčervená, chybějící vlastníci.

### Prezentace řešení [P1]
Pro jakékoli publikum použij stejnou kostru:

1. **Problém** — co je špatně, pro koho, kolik to stojí (jeden slide).
2. **Možnosti** — obvykle dvě až čtyři včetně „nedělat nic“, s výhodami, nevýhodami, cenou a rizikem.
3. **Doporučení** — která možnost a proč, jednou větou plus důkazy.
4. **Žádost** — co od tohoto publika dnes potřebuješ: rozhodnutí, rozpočet, lidi, zpětnou vazbu.

**Přizpůsobení publiku:**

| | Netechnické (vedení, business) | Technické (IT, architekti, dodavatel) |
|---|---|---|
| Zaměření | Dopad, cena, riziko, harmonogram | Jak to funguje, rozhraní, data, omezení |
| Detail | Jedno zaokrouhlené číslo na bod | Přesná pole, formáty, objemy, ošetření chyb |
| Vizuály | Proces před/po, jednoduchý graf | Sekvenční diagram, datový model, ukázka API |
| Typická otázka | „Kolik to stojí a kdy to budeme mít?“ | „Jak se to napojí a co se stane při selhání?“ |
| Vyhnout se | Zkratkám, systémovému žargonu | Vágním tvrzením typu „bude to rychlé“ |

Tipy:
- U seniorního publika dej doporučení dopředu. Po třech minutách tě můžou přerušit.
- Připrav si záložní slide na otázky, které čekáš.
- Nacvič to nahlas a měř si čas. Pětiminutový slot znamená asi 600–700 vyslovených slov.
- Nikdy neukazuj ve slidech skutečná klientská data. Používej fiktivní nebo anonymizované příklady.

### Příprava krátkého interního školení [P2]
Když jde nová funkce do provozu, BA často školí první uživatele nebo školitele.

**Struktura 30minutového školení:**
1. **Výukové cíle** (2 min) — dvě nebo tři věty začínající „Po tomto školení umíte…“, například „…podat hlášení škody s novým kontrolním seznamem dokumentů“ a „…zjistit, proč škoda čeká“.
2. **Proč se to změnilo** (3 min) — problém slovy uživatelů, ne projektu.
3. **Demo** (8 min) — jeden realistický scénář od začátku do konce, v UAT nebo školicím prostředí s fiktivními daty.
4. **Vyzkoušení** (12 min) — každý účastník sám udělá dva připravené úkoly. Procházej mezi nimi (nebo sleduj sdílené obrazovky) a pomáhej.
5. **Otázky a kde hledat pomoc** (5 min) — koho kontaktovat, kde je tahák a dokumentace.

**Cheat sheet** (tahák): jedna stránka, snímky obrazovky s očíslovanými kroky pro tři nejčastější úkoly, seznam změn, kontakt na pomoc. Lidé si ho nechají na stole; 40stránkový manuál znovu číst nebudou.

**Ověření, že se naučili:** na konci požádej účastníky, ať jeden úkol udělají bez pomoci. Když to většina zvládne, školení fungovalo.

### Jasné e-maily a zápisy z porad [P1]
**E-maily:**
- Předmět uvádí téma i žádost: „Decision needed by 6/11: CR-07 buyer turnover field“.
- První dva řádky: co potřebuješ, od koho, do kdy.
- Pak kontext v krátkých odstavcích nebo odrážkách.
- Jeden e-mail, jedno téma. Různá témata patří do různých e-mailů, aby se dala sledovat.
- Před odesláním si to přečti znovu: pochopil by to někdo, kdo na poradě nebyl?

**Šablona zápisu z porady:**

```text
Meeting: Claim document checklist workshop    Date: 2026-10-29
Participants: claims manager, 3 claims handlers, compliance, BA (notes)
Purpose: agree required documents per product

Decisions
D1. Proof of delivery is mandatory for all products.
D2. Correspondence with buyer is mandatory only for claims above the internal threshold.

Action items
| # | Action | Owner | Due |
| A1 | Confirm threshold amount with Head of Claims | Claims manager | 02/11 |
| A2 | Update requirement REQ-14 and send for sign-off | BA | 04/11 |
| A3 | Check retention rules for uploaded documents | Compliance | 09/11 |

Open questions
Q1. Do short-term policies need the same checklist? (owner: claims manager)

Parking lot
- Idea: automatic reminder to exporters after 5 days (to backlog)
```

Zápis zachycuje rozhodnutí a úkoly, ne kdo co řekl. Pošli ho do 24 hodin a požádej o připomínky do stanoveného data; mlčení pak znamená souhlas.

Poznámka k AI nástrojům: AI asistent může pomoct s návrhem zápisu nebo osnovy školení, ale nikdy do veřejného AI nástroje nevkládej skutečná data klientů, kolegů ani firmy. Používej jen schválené interní nástroje, a pokud organizace vyžaduje, aby byl text vytvořený AI označený, označ ho.

## Key terms
- **Stakeholder** — každá osoba nebo skupina, které se změna týká nebo která ji může ovlivnit.
- **Stakeholder analysis** (analýza stakeholderů) — identifikace stakeholderů a posouzení jejich vlivu, zájmu a potřeb.
- **Power/interest grid** (mřížka vliv/zájem) — mřížka 2×2, která třídí stakeholdery podle vlivu a zájmu, aby šlo naplánovat jejich zapojení.
- **RACI matrix** (matice RACI) — tabulka, která ke každé činnosti přiřazuje role Responsible, Accountable, Consulted a Informed.
- **Accountable** — jediná osoba, která vlastní výsledek činnosti a schvaluje ho.
- **Onion diagram** (cibulový diagram) — soustředné kruhy, které ukazují, jak přímo jsou skupiny stakeholderů s řešením spojené.
- **Communication plan** (komunikační plán) — přehled, kdo dostává jaké informace, jak často a jakým kanálem.
- **Facilitator** (facilitátor) — osoba, která vede průběh porady tak, aby skupina dosáhla cíle.
- **Parking lot** (odkladiště) — viditelný seznam bodů mimo téma, zachycených pro pozdější řešení.
- **Dot voting** (hlasování tečkami) — rychlá technika prioritizace, při které účastníci rozdělují omezený počet hlasů.
- **RAG status** — hodnocení stavu oblasti projektu barvou Red/Amber/Green.
- **Status report** — pravidelné strukturované shrnutí postupu, rizik, problémů a potřebných rozhodnutí.
- **Escalation** (eskalace) — předání rozhodnutí nebo problému někomu s vyšší pravomocí, když ho nejde vyřešit na současné úrovni.
- **Action item** (úkol z porady) — úkol dohodnutý na poradě s vlastníkem a termínem.
- **Learning objective** (výukový cíl) — věta, co účastníci po školení umějí.
- **Cheat sheet** (tahák) — jednostránkový rychlý přehled nejčastějších úkolů.

## Hands-on
:::exercise id="m16-e1" title="Mřížka vliv/zájem a RACI pro automatizaci škod" min="45" tool="Miro"
**Cíl:** procvičit identifikaci a uspořádání stakeholderů na realistickém projektu.

1. V [Miru](https://miro.com/) sepiš aspoň 10 stakeholderů pro „automatizaci příjmu škod v ExportShield“. Použij otázky na identifikaci z části Deep dive. Přidej aspoň dva, kteří v příkladu v modulu nejsou.
2. Nakresli mřížku vliv/zájem 2×2 a každého stakeholdera do ní umísti. Ke každému napiš jednu větu, jak ho zapojíš.
3. Sestav tabulku RACI s aspoň 7 činnostmi (business case, pravidla schvalování, požadavky, stavba, posouzení ochrany osobních údajů, UAT, go-live, školení).
4. Kontrola: na každém řádku právě jedno A; žádný sloupec se samými I u někoho, koho jsi umístila do „manage closely“.
5. Napiš dvě věty o konfliktu, který čekáš nejvíc, a jak ho budeš řešit.

**Hotovo, když:** mřížka i RACI jsou kompletní, každý řádek má jedno A a každé umístění umíš vysvětlit jednou větou.
:::

:::exercise id="m16-e2" title="Napiš jednostránkový týdenní status report" min="30" tool="Word or Confluence"
**Cíl:** připravit report, který vytížený sponzor přečte za dvě minuty.

1. Použij šablonu z části Deep dive.
2. Vymysli fiktivní týden projektu automatizace škod s: jedním dokončeným milníkem, jedním rizikem, které přepne harmonogram na amber, a jedním rozhodnutím, které potřebuješ od sponzora.
3. Shrnutí napiš nejvýš na tři věty.
4. Každému riziku dej vlastníka, akci a termín.
5. Požádej někoho mimo IT, ať report přečte a vlastními slovy ti řekne, co musí sponzor udělat. Když to nedokáže, přepiš ho.

**Hotovo, když:** report se vejde na jednu stránku, RAG je zdůvodněný a člověk zvenku umí pojmenovat potřebné rozhodnutí.
:::

:::exercise id="m16-e3" title="Odprezentuj navrhovanou změnu za 5 minut" min="90" tool="PowerPoint or Google Slides"
**Cíl:** procvičit strukturu problém → možnosti → doporučení → žádost pod časovým tlakem.

1. Vyber změnu: například online formulář žádosti o úvěrový limit, nebo zrušení druhého schválení u malých škod (pokud ho máš, použij svůj business case z modulu 03).
2. Připrav nejvýš 5 slidů: Problém; Možnosti (včetně „nedělat nic“); Doporučení s důkazy; Plán a cena; Žádost.
3. Napiš poznámky pro řečníka v rozsahu asi 600–700 slov.
4. Nahraj se (jakýmkoli nahráváním obrazovky nebo kamerou telefonu). Zastav přesně v 5 minutách.
5. Pusť si záznam. Poznamenej tři věci: Řekla jsi jasně, co žádáš? Použila jsi žargon, který by manažer neznal? Kde jsi ztratila čas?
6. Nahraj to ještě jednou s vylepšeními.

**Hotovo, když:** máš záznam kratší než 5 minut s jasnou žádostí na posledním slidu a krátký seznam toho, co jsi mezi pokusy zlepšila. Používej jen fiktivní data.
:::

:::exercise id="m16-e4" title="Navrhni 30minutové školení" min="40" tool="Word or Confluence"
**Cíl:** naplánovat školení, které změní, co lidé umějí, ne jen co slyšeli.

1. Téma: nový formulář hlášení škody s kontrolním seznamem dokumentů v ClaimDesk (fiktivní).
2. Napiš 2–3 výukové cíle začínající „Po tomto školení umíte…“.
3. Naplánuj školení po minutách (cíle, proč se to změnilo, demo, vyzkoušení, otázky).
4. Napiš dva praktické úkoly s fiktivními testovacími daty, každý zvládnutelný za 5 minut.
5. Navrhni osnovu jednostránkového taháku: tři úkoly s očíslovanými kroky, co se změnilo, koho kontaktovat.
6. Urči, jak na konci ověříš, že se to lidé naučili.

**Hotovo, když:** plán dá dohromady 30 minut, každý výukový cíl se procvičí v praktickém úkolu a osnova taháku se vejde na jednu stránku.
:::

## Self-check
:::q
Compliance officer chodí na projektové porady zřídka, ale může zastavit go-live. Kam patří na mřížce vliv/zájem a co to pro tebe znamená?
---
Vysoký vliv a přinejmenším na začátku spíš nižší zájem: „keep satisfied“. Měla bys ho zapojit brzy v konkrétních bodech (toky dat, doba uchování, přístupy) krátkými cílenými informacemi, místo abys ho překvapila těsně před go-live, kdy by bylo řešení jeho výhrad nejdražší.
:::

:::q
Na řádku RACI je A u Head of Claims i u manažera likvidace. Proč je to problém?
---
Odpovědnost za výsledek musí ležet na jedné osobě; při dvou každý může předpokládat, že rozhodne ten druhý, nebo rozhodnou každý jinak. Rozhodování se pak zasekne nebo si odporuje. Ujasni, kdo výsledek vlastní, a druhého udělej R nebo C.
:::

:::q
Na workshopu dominuje jeden seniorní underwriter a ostatní mlčí. Jmenuj dvě facilitační techniky, které pomohou.
---
Round robin, kdy každý účastník přispěje postupně, a tichý brainstorming na lepicí papírky před diskusí, který sesbírá nápady všech nezávisle. Dot voting potom dává každému stejnou váhu i při prioritizaci.
:::

:::q
Projekt má týdenní zpoždění na milníku, ale čekáš, že ho dorovnáš v příštím sprintu. Jaký RAG status pro harmonogram nahlásíš a proč?
---
Amber, pokud to odpovídá dohodnutým prahům. Je to ohrožené, ale existuje plán nápravy. Zelená by zakryla informaci, kterou sponzor může potřebovat; včasná oranžová s plánem buduje důvěru a brání náhlému skoku do červené.
:::

:::q
Během hovoru vývojář z NovaSoftu řekne: „Přidat pole s obratem je snadné, prostě to uděláme.“ Co uděláš?
---
Poděkuješ, ale neformálně nesouhlasíš. Vysvětlíš, že to mění dohodnutý rozsah, takže to jde přes proces change requestu s odhadem dopadu a schválením sponzora. Diskusi zaznamenáš písemně. Jinak se cena a rozsah mění bez schválení a smlouva přestane odpovídat tomu, co se staví.
:::

:::q
Jaký je rozdíl mezi tím, jak stejné doporučení prezentuješ řídicímu výboru a architektům NovaSoftu?
---
U řídicího výboru se zaměř na problém, cenu, přínos, riziko a harmonogram, s doporučením na začátku a jasnou žádostí o rozhodnutí. U architektů drž stejnou strukturu, ale přidej rozhraní, data, objemy, ošetření chyb a omezení a požádej o technickou zpětnou vazbu nebo odhad.
:::

:::q
Co má zápis z porady obsahovat a co v něm být nemá?
---
Má obsahovat účastníky, účel, rozhodnutí, úkoly s vlastníky a termíny, otevřené otázky a odložené body. Nemá v něm být doslovný záznam diskuse a kdo co řekl, pokud to není důležité pro rozhodnutí.
:::

## Interview corner
:::interview
Jak řešíte dva stakeholdery s protichůdnými požadavky?
*EN: How do you handle two stakeholders with conflicting requirements?*
---
- Zdokumentovat oba požadavky, jejich zdroje a důvody.
- Propojit každý s cíli businessu a definicí problému; kde to jde, vyčíslit dopad.
- Hledat třetí možnost, která obě potřeby částečně splní.
- Eskalovat na accountable rozhodovatele s jasným doporučením; rozhodnutí zapsat.
- Dát krátký příklad.

Typická chyba: rozhodnout sama, kdo má pravdu, nebo prostě převzít názor služebně staršího.
:::

:::interview
Jak během projektu udržujete stakeholdery informované?
*EN: How do you keep stakeholders informed during a project?*
---
- Identifikovat a analyzovat stakeholdery (mřížka vliv/zájem).
- Dohodnout komunikační plán: kdo, co, jak často, kanál.
- Týdenní status report s RAG, riziky a potřebnými rozhodnutími; poctivá oranžová/červená.
- Dema na sprint review; zapojení uživatelů do testování.
- Přizpůsobit formu člověku (report vs krátký hovor).

Typická chyba: popsat jen „posílám e-maily“ bez struktury a přizpůsobení.
:::

:::interview
Řekněte mi o situaci, kdy jste prezentovala něco lidem s jiným zázemím.
*EN: Tell me about a time you had to present something to people with a different background.*
---
- Situace a publikum: kdo, co věděli, co potřebovali.
- Struktura: problém → možnosti → doporučení → žádost.
- Co jsi přizpůsobila: jazyk, úroveň detailu, vizuály.
- Výsledek: přijaté rozhodnutí, zpětná vazba.
- Co bys udělala jinak.

Typická chyba: mluvit o obsahu prezentace místo o tom, jak jsi ji přizpůsobila publiku.
:::

:::interview
Jak byste řekla ne požadavku seniorního manažera, který je mimo rozsah?
*EN: How would you say no to a senior manager's request that is out of scope?*
---
- Uznat potřebu, která za požadavkem stojí.
- Věcně vysvětlit omezení: rozsah, rozpočet, harmonogram, smlouva.
- Nabídnout možnosti: change request s dopadem, výměna za položku s nižší prioritou, pozdější release.
- Nechat rozhodnout správnou osobu; potvrdit písemně.

Typická chyba: buď souhlasit, aby nebyl konflikt, nebo odmítnout bez nabídky jakékoli cesty dál.
:::
