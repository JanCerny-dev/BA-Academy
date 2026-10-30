---
id: 11
slug: apis-integrations
title: API, JSON/XML a integrace systémů
phase: C
priority: P1
quick_min: 20
deep_min: 90
job_ad: "práce s API a formáty JSON/XML"
---

## Why this matters
Inzerát uvádí API, JSON a XML mezi základními dovednostmi. V pojišťovně se skoro každá změna dotkne nějaké integrace: systém smluv posílá data do systému škod, portál se ptá obchodního rejstříku, finance dostávají soubor s platbami. Analytik integrační kód nepíše, ale píše, co má integrace dělat: jaká data jdou kam, kdy, v jakém formátu a co se stane, když něco selže. K tomu musíš umět číst dokumentaci API, sama API zavolat a vidět skutečná data a popsat mapování polí tak přesně, aby to dodavatel uměl postavit a tester otestovat.

## Quick version
**API** (application programming interface, aplikační programové rozhraní) je definovaný způsob, jak jeden program požádá jiný program o data nebo o provedení akce. Web je určený lidem; API je určené programům.

**Klient a server.** **Client** (klient) posílá **request** (požadavek); **server** ho zpracuje a vrátí **response** (odpověď). Portál (klient) se ptá PolicyHubu (server) na smlouvu. PolicyHub sám může být klientem jiného serveru, například ARES.

**HTTP požadavek obsahuje:**

- **method** (metodu, co udělat): `GET` číst, `POST` vytvořit, `PUT` nahradit, `PATCH` změnit část, `DELETE` odstranit;
- **URL** (kam): adresu serveru plus **path** (cestu, `/credit-limits/CL-2026-0041`) a volitelné **query parameters** (parametry dotazu, `?status=REQUESTED`);
- **headers** (hlavičky, metadata): typ obsahu, požadovaný formát, autorizaci;
- volitelné **body** (tělo, odesílaná data, obvykle JSON), kterému se říká také **payload**.

**HTTP odpověď obsahuje** **status code** (stavový kód), hlavičky a obvykle tělo. Stavové kódy, které je dobré znát:

| Kód | Význam |
|---|---|
| 200 OK | úspěch, data jsou v těle |
| 201 Created | byl vytvořen nový záznam |
| 204 No Content | úspěch, nic se nevrací |
| 400 Bad Request | požadavek je neplatný (špatný formát, chybějící pole) |
| 401 Unauthorized | neautentizováno (chybí nebo jsou neplatné přihlašovací údaje) |
| 403 Forbidden | autentizováno, ale nepovoleno |
| 404 Not Found | zdroj neexistuje |
| 409 Conflict | konflikt s aktuálním stavem (např. duplicita) |
| 429 Too Many Requests | klient poslal příliš mnoho požadavků |
| 500 Internal Server Error | server selhal |
| 503 Service Unavailable | server nejede nebo je přetížený |

Praktické pravidlo: 2xx úspěch, 3xx přesměrování, 4xx chybu udělal klient, 5xx má problém server.

**REST** je běžný styl webových API: všechno je **resource** (zdroj) s vlastní URL (`/credit-limits`, `/credit-limits/{id}`), pracuje se s ním standardními HTTP metodami a každý požadavek nese vše potřebné (server si mezi voláními nepamatuje žádnou relaci).

**JSON** a **XML** jsou textové formáty pro strukturovaná data:

- JSON: `{"status": "REQUESTED", "requestedAmount": 120000}`. Lehký, výchozí pro REST.
- XML: `<Status>REQUESTED</Status>`. Upovídaný, ale se silnou validací přes schémata **XSD**. Pořád běžný v bankách, pojišťovnách a veřejné správě, často s webovými službami **SOAP**.

**Authentication** (autentizace) prokazuje, kdo API volá: **API key** (API klíč), **Basic** autentizace (uživatel a heslo) nebo **OAuth 2.0** s krátkodobým **bearer tokenem**. Tajné údaje (secrets) nikdy nepatří do dokumentů, kódu, ticketů ani chatu.

**Integrační vzory:** synchronní volání API (odpověď hned), asynchronní zprávy přes frontu (odpověď později, systémy jsou oddělené), dávkový přenos souborů (např. noční CSV přes SFTP), webhooky (server zavolá tebe, když se něco stane), ETL do datového skladu. Volba závisí na tom, jak rychle data potřebuješ, na objemech a spolehlivosti.

**Co analytik píše:** **integration specification** (integrační specifikaci): systémy, spouštěč, směr, frekvenci, **data mapping** (mapování dat) pole po poli, ošetření chyb, objemy, bezpečnost a monitoring.

**Procvičování na skutečných API:** český registr ekonomických subjektů ARES (`GET https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/00006947` vrátí Ministerstvo financí jako JSON), testovací API JSONPlaceholder, API playground na webu (`api.html`) a [Postman](https://www.postman.com/downloads/).

**Na pohovor jednou větou:** „Umím číst dokumentaci API a specifikace OpenAPI, zavolat API v Postmanu, číst JSON a XML a napsat integrační specifikaci s mapováním dat, ošetřením chyb a nefunkčními požadavky.“

## Deep dive

### Klient, server a HTTP [P1]
**HTTP** (Hypertext Transfer Protocol) je protokol webu; **HTTPS** je tentýž protokol šifrovaný. Prohlížeč ho používá k načítání stránek a většina API přes něj vyměňuje data.

Skutečný požadavek na ARES, český veřejný registr ekonomických subjektů, vypadá „na drátě“ takto (zjednodušeně):

```text
GET /ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/00006947 HTTP/1.1
Host: ares.gov.cz
Accept: application/json
```

- `GET` je metoda: čti data.
- Cesta končí IČO (8 číslic). Je to **path parameter** (parametr cesty): část URL, která identifikuje zdroj.
- `Host` určuje server.
- `Accept` je hlavička, která říká, jaký formát klient chce.
- GET nemá tělo.

Odpověď (zkrácená; skutečná má víc polí a hodnoty jako datum aktualizace se v čase mění):

```json
{
  "ico": "00006947",
  "obchodniJmeno": "Ministerstvo financí",
  "sidlo": {
    "kodStatu": "CZ",
    "nazevStatu": "Česká republika",
    "nazevObce": "Praha",
    "nazevUlice": "Letenská",
    "cisloDomovni": 525,
    "cisloOrientacni": 15,
    "psc": 11800,
    "textovaAdresa": "Letenská 525/15, Malá Strana, 11800 Praha 1"
  },
  "pravniForma": "325",
  "dic": "CZ00006947",
  "datumAktualizace": "2026-03-23",
  "czNace": ["84110"]
}
```

Stavový řádek této odpovědi je `200` a hlavička `Content-Type: application/json` říká klientovi, jak tělo číst. Názvy polí jsou česky: `obchodniJmeno` je obchodní jméno, `sidlo` sídlo, `psc` PSČ, `dic` DIČ, `pravniForma` kód právní formy, `czNace` kódy činností.

Dvě chyby, také skutečné:

- neexistující IČO (např. `12345678`) vrátí **404** s tělem `{"kod": "NENALEZENO", ...}`;
- IČO ve špatném formátu (např. `abc` nebo 7 číslic) vrátí **400** s `{"kod": "CHYBA_VSTUPU", "subKod": "VSTUP_NEVALIDNI_FORMAT_ICO", ...}`.

Všimni si, že těla chyb obsahují strojově čitelné kódy plus zprávu pro člověka. Když specifikuješ integraci, chtěj přesně tohle: jaké stavové kódy a chybové kódy existují a co s každým z nich má volající systém udělat.

**Query parameters** (parametry dotazu) následují za `?` a filtrují nebo upravují požadavek: `GET /credit-limits?status=REQUESTED&currency=EUR`. Parametry cesty identifikují jednu věc; parametry dotazu filtrují, řadí nebo stránkují seznamy.

**Hlavičky**, které potkáš často: `Content-Type` (formát odesílaného těla), `Accept` (požadovaný formát odpovědi), `Authorization` (přihlašovací údaje) a někdy correlation ID (jedinečné ID požadavku, podle kterého ho dohledáš v logách).

### REST jednoduše [P1]
**REST** (Representational State Transfer) je architektonický styl, ne standard se specifikací. V praxi „REST API“ znamená:

- **Zdroje** (resources) mají URL: `/policies`, `/policies/ES-2025-1018`, `/policies/ES-2025-1018/credit-limits`.
- **HTTP metody** říkají, co s nimi udělat.
- **Stateless** (bezstavovost): každý požadavek obsahuje vše, co server potřebuje (včetně přihlašovacích údajů). Server si předchozí volání nepamatuje.
- **Standardní stavové kódy** hlásí výsledek.
- Data nesou reprezentace, obvykle JSON.

CRUD (create, read, update, delete – vytvořit, číst, změnit, smazat) se mapuje na metody:

| Operace | Metoda | Příklad | Typický kód úspěchu |
|---|---|---|---|
| Vytvořit | POST | `POST /credit-limits` s JSON tělem | 201 |
| Číst jeden | GET | `GET /credit-limits/CL-2026-0041` | 200 |
| Číst seznam | GET | `GET /credit-limits?status=REQUESTED` | 200 |
| Změnit celé | PUT | `PUT /credit-limits/CL-2026-0041` | 200 nebo 204 |
| Změnit část | PATCH | `PATCH /credit-limits/CL-2026-0041` s `{"status": "APPROVED"}` | 200 nebo 204 |
| Smazat | DELETE | `DELETE /credit-limits/CL-2026-0041` | 204 |

GET nesmí měnit data. Záleží na tom monitorovacím nástrojům, cache a opakovaným pokusům (retries), které mohou GET kdykoli zopakovat.

### JSON a XML vedle sebe [P1]
Tatáž žádost o úvěrový limit (podle žádosti 41 v datové sadě ExportShield) v obou formátech.

**JSON** (JavaScript Object Notation):

```json
{
  "creditLimitId": "CL-2026-0041",
  "policyNo": "ES-2025-1018",
  "buyer": {
    "name": "Nordhafen Logistik GmbH",
    "countryCode": "DE"
  },
  "requestedAmount": 120000.00,
  "currency": "EUR",
  "status": "REQUESTED",
  "requestedOn": "2026-09-14",
  "paymentTermsDays": 60,
  "insuredRisks": ["COMMERCIAL", "POLITICAL"],
  "urgent": false,
  "decision": null
}
```

Pravidla JSON:

- **Object** (objekt) je ve složených závorkách `{}` s dvojicemi `"key": value` oddělenými čárkami.
- **Array** (pole, seznam) je v hranatých závorkách `[]`.
- Typy hodnot: řetězec ve dvojitých uvozovkách, číslo (bez uvozovek, s desetinnou tečkou, bez oddělovače tisíců), `true`/`false`, `null`, objekt, pole.
- Objekty a pole se mohou **vnořovat**: `buyer` je objekt uvnitř hlavního objektu.
- JSON **nemá datový typ pro datum**. Datumy jsou řetězce, takže formát se musí dohodnout (normou je ISO 8601 `YYYY-MM-DD`).
- Klíče rozlišují velká a malá písmena. Žádné komentáře, žádná čárka za poslední položkou. Jediná špatná čárka udělá celý dokument neplatným; [JSONLint](https://jsonlint.com/) ji najde.

**XML** (Extensible Markup Language):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<CreditLimitRequest xmlns="urn:exportshield:credit-limit:v1" id="CL-2026-0041">
  <PolicyNo>ES-2025-1018</PolicyNo>
  <Buyer countryCode="DE">
    <Name>Nordhafen Logistik GmbH</Name>
  </Buyer>
  <RequestedAmount currency="EUR">120000.00</RequestedAmount>
  <Status>REQUESTED</Status>
  <RequestedOn>2026-09-14</RequestedOn>
  <PaymentTermsDays>60</PaymentTermsDays>
  <InsuredRisks>
    <Risk>COMMERCIAL</Risk>
    <Risk>POLITICAL</Risk>
  </InsuredRisks>
  <Urgent>false</Urgent>
  <!-- no Decision element: the request is not decided yet -->
</CreditLimitRequest>
```

Pravidla XML:

- **Elements** (elementy) mají počáteční a koncový tag: `<Status>REQUESTED</Status>`. Všechno obaluje právě jeden kořenový element.
- **Attributes** (atributy) jsou uvnitř počátečního tagu: `currency="EUR"`. Typicky nesou metadata o hodnotě.
- Tagy rozlišují velká a malá písmena a musí být správně vnořené.
- Opakované elementy (`<Risk>` dvakrát) tvoří seznam.
- **Namespace** (jmenný prostor, `xmlns="urn:exportshield:credit-limit:v1"`) je jedinečný název, který říká, do jakého slovníku tagy patří, aby se `<Status>` ze dvou různých standardů nepletly. Vypadá jako adresa, ale je to jen identifikátor.
- Komentáře jsou povolené (`<!-- ... -->`).

**XSD** (XML Schema Definition) je samostatný XML dokument, který definuje, jak vypadá platná zpráva: jaké elementy, v jakém pořadí, které jsou povinné, jejich datové typy a povolené hodnoty. Ukázka:

```xml
<xs:element name="Status">
  <xs:simpleType>
    <xs:restriction base="xs:string">
      <xs:enumeration value="REQUESTED"/>
      <xs:enumeration value="APPROVED"/>
      <xs:enumeration value="REDUCED"/>
      <xs:enumeration value="REJECTED"/>
    </xs:restriction>
  </xs:simpleType>
</xs:element>
<xs:element name="RequestedOn" type="xs:date"/>
```

S tímto schématem se `<RequestedOn>14.09.2026</RequestedOn>` odmítne, protože `xs:date` vyžaduje `2026-09-14`. Proto je XML oblíbené v regulovaném prostředí: kontrakt jde ověřit strojově. JSON má obdobu, **JSON Schema**, a OpenAPI používá jeho variantu.

| | JSON | XML |
|---|---|---|
| Typické použití | REST API, webové a mobilní aplikace | služby SOAP, regulatorní reporting, starší podnikové integrace |
| Velikost | kompaktní | upovídanější |
| Datové typy | string, number, boolean, null, object, array | všechno je text; typy dává XSD |
| Atributy | ne | ano |
| Komentáře | ne | ano |
| Schéma | JSON Schema, OpenAPI | XSD |

### SOAP a WSDL [P2]
**SOAP** je starší protokol pro webové služby, který posílá XML zprávy uvnitř **envelope** (obálky), obvykle přes HTTP POST. Potkáš ho v bankách, pojišťovnách a státní správě, protože mnoho klíčových systémů bylo propojeno v nultých letech a pořád dobře funguje.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
                  xmlns:cl="urn:exportshield:credit-limit:v1">
  <soapenv:Header/>
  <soapenv:Body>
    <cl:GetCreditLimit>
      <cl:CreditLimitId>CL-2026-0041</cl:CreditLimitId>
    </cl:GetCreditLimit>
  </soapenv:Body>
</soapenv:Envelope>
```

- **Envelope** obaluje všechno, volitelný **Header** nese metadata, například bezpečnostní tokeny, **Body** nese operaci a její data.
- Chyby se vrací jako element **SOAP Fault** v těle.
- Soubor **WSDL** (Web Services Description Language) popisuje službu: její operace, XML zprávy (přes XSD) a adresu endpointu. Nástroje z něj generují klientský kód.

Rozdíly proti RESTu z pohledu analytika: SOAP je postavený na operacích (`GetCreditLimit`), ne na zdrojích, vždy XML, s přísným kontraktem ve WSDL. Otázky v integrační specifikaci zůstávají stejné.

### Autentizace a tajné údaje [P1]
**Authentication** (autentizace) odpovídá na „kdo jsi?“; **authorization** (autorizace) na „co smíš?“.

- **API key** (API klíč): dlouhý tajný řetězec posílaný v hlavičce. Jednoduché; identifikuje volající aplikaci, ne člověka.
- **Basic authentication**: uživatelské jméno a heslo v hlavičce `Authorization`, jen zakódované do Base64, ne zašifrované (kdo hlavičku uvidí, umí je dekódovat). Přijatelné jen přes HTTPS; běžné ve starších interních integracích.
- **OAuth 2.0**: klient nejdřív získá **access token** (přístupový token) od autorizačního serveru a pak ho posílá jako `Authorization: Bearer <token>` s každým voláním. Tokeny vyprší (často po minutách nebo hodinách) a nesou **scopes** (rozsahy oprávnění), které omezují, co volající smí. V integracích systém–systém je typický tok „client credentials“; když se přihlašuje uživatel, používají se jiné toky. Takové tokeny vydává Microsoft Entra ID a podobné identity platformy. Přesně vzato je OAuth 2.0 autorizační rámec (uděluje přístup); přihlášení člověka řeší OpenID Connect, vrstva postavená nad OAuth 2.0.
- **Mutual TLS (mTLS)**: obě strany prokazují svou identitu certifikáty. Běžné mezi bankami a pojišťovnami.

Pravidla, která analytik píše do požadavků a sám dodržuje:

- Přihlašovací údaje a tokeny jsou **secrets** (tajné údaje). Patří do úložiště tajných údajů (např. key vault nebo správce přihlašovacích údajů platformy), nikdy do specifikací, stránek v Confluence, ticketů, kódu, e-mailů, screenshotů ani AI chatů.
- Každá integrace dostane vlastní technický účet s minimálními právy, která potřebuje (**least privilege**, princip nejmenších oprávnění).
- Specifikuj, jak se tajné údaje rotují a kdo technický účet vlastní.
- V Postmanu drž tajné údaje v proměnných označených jako secret a nesdílej kolekce, které je obsahují. Pro veřejná API v tomto modulu žádné tajné údaje nepotřebuješ.

### Čtení dokumentace API a OpenAPI [P1]
Dobrá dokumentace API odpovídá na: základní URL, autentizaci, seznam endpointů, parametry, těla požadavků a odpovědí s příklady, chybové kódy, limity (rate limits, velikost stránek) a verzování.

**OpenAPI** (dříve Swagger) je standardní formát pro popis REST API v YAML nebo JSON. Mnoho dodavatelů dodá místo wordového dokumentu soubor OpenAPI. Krátká ukázka:

```yaml
paths:
  /credit-limits/{id}:
    get:
      summary: Get one credit limit
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: The credit limit
        '404':
          description: No credit limit with this id
```

Jak to číst: pod `paths` jsou jednotlivé URL; pod každou URL metody; u každé metody `parameters` (tady povinný parametr cesty `id`), případně `requestBody` a `responses` podle stavových kódů. `components/schemas` definují datové struktury s typy, povinnými poli (`required`), formáty a povolenými hodnotami (`enum`). Otevři soubor ve [Swagger Editoru](https://editor.swagger.io/) a uvidíš ho vykreslený jako čitelnou dokumentaci; přesně to dělá cvičení 4.

Jako analytička kontroluj soubor OpenAPI proti svým požadavkům: jsou tam všechna pole z mapování, jsou povinná pole označená, jsou výčty (enums) úplné, jsou popsané chybové odpovědi?

### Integrační vzory [P1]
| Vzor | Jak funguje | Kdy použít | Příklad v ExportShield |
|---|---|---|---|
| Synchronní volání API | Klient zavolá a čeká na odpověď | Uživatel nebo proces potřebuje odpověď hned; malá data | PolicyHub ověřuje firmu v ARES, zatímco underwriter čeká |
| Asynchronní zprávy (fronta, topic) | Odesílatel vloží zprávu do fronty; příjemce ji zpracuje později | Systémy musí být oddělené; příjemce může být pomalý nebo nedostupný; události | ClaimDesk publikuje „škoda schválena“; finance si ji vyzvednou a zaplatí |
| Dávkový přenos souborů | Soubor (CSV, XML) se podle plánu vytvoří a přesune, často přes SFTP | Velké objemy, není potřeba reálný čas, starší systémy | Noční CSV všech vyplacených plnění do účetního systému |
| Webhook | Server zavolá URL klienta, když nastane událost | Chceš dostat upozornění místo opakovaného ptaní | Služba pro dokumenty zavolá DocVault, když dorazí podepsaná smlouva |
| ETL / replikace dat | Data se vytáhnou, transformují a nahrají do jiného úložiště | Reporting, datový sklad, migrace | Denní nahrání smluv a škod do reportingové databáze |

Otázky, které rozhodnou o vzoru: Jak čerstvá musí data být (sekundy, hodiny, další den)? Kolik záznamů? Co se stane, když příjemce nejede: má odesílatel selhat, počkat, nebo zařadit do fronty? Potřebuje business potvrzení, že data dorazila?

**Polling** (dotazování každých pár minut „je něco nového?“) je jednoduchá alternativa k webhookům a zprávám. Funguje, ale plýtvá voláními a přidává zpoždění.

### Ošetření chyb, idempotence a opakování [P2]
Integrace selhávají: síť vypadne, servery se restartují, data jsou neplatná. Specifikace musí říct, co se stane v každém případě, jinak o tom rozhodne vývojář sám.

- **Validační chyby (4xx)**: neopakovat; požadavek selže znovu. Zalogovat, upozornit člověka nebo zařadit do chybové fronty k ručnímu zpracování.
- **Dočasné chyby (timeouty, 503, 429)**: opakovat omezeně, s prodlužujícím se čekáním (**exponential backoff**, exponenciální odstup: např. po 1, 2, 4 sekundách), pak to vzdát a vyhlásit alarm.
- **Timeouty**: specifikuj, jak dlouho klient čeká. Když uživatel čeká u obrazovky, nanejvýš pár sekund, pak srozumitelná hláška.
- **Idempotency** (idempotence): operace je **idempotentní**, když její dvojí provedení má stejný účinek jako jedno. Podle definice ve standardu HTTP (RFC 9110) jsou GET, HEAD, OPTIONS, PUT a DELETE idempotentní; POST není a PATCH to není zaručeně. Když POST „vyplatit plnění“ vyprší a zopakuje se, exportér může dostat zaplaceno dvakrát. Řešení: **idempotency key** (idempotenční klíč, jedinečné ID posílané s požadavkem; server opakování se stejným klíčem ignoruje) nebo business kontrola (jedna platba na číslo splátky škody).
- **Částečné selhání v dávkách**: když je řádek 5 000 z 10 000 neplatný, selže celý soubor, nebo jen ten řádek? Zapiš to.
- **Monitoring a alerting**: kdo se dozví, že integrace selhala, a jak rychle?

Příklad požadavku: „Pokud ARES neodpoví do 5 sekund, PolicyHub jednou zopakuje volání. Pokud selže i druhý pokus, PolicyHub zobrazí ‚Registr nedostupný, zkuste později‘, zaloguje chybu s correlation ID a umožní underwriterovi pokračovat bez dat z registru; žádost označí ‚čeká na kontrolu v registru‘.“

### Psaní integrační specifikace [P1]
Šablona, která funguje pro většinu integrací:

| Část | Obsah |
|---|---|
| Účel | Business důvod v jedné nebo dvou větách |
| Systémy | Zdroj, cíl, vlastník každého z nich, kontakty na dodavatele |
| Spouštěč | Událost (akce uživatele, změna stavu), plán nebo příchod souboru |
| Směr a vzor | Jednosměrná nebo obousměrná; API, zpráva, soubor, webhook |
| Frekvence a objemy | Volání za den, špička za hodinu, velikost souboru, očekávaný růst |
| Mapování dat | Tabulka polí (viz níže) |
| Validační pravidla | Co dělá zprávu platnou; co se stane s neplatnými |
| Ošetření chyb | Pro každý typ chyby: opakování, alarm, ruční zpracování |
| Bezpečnost | Autentizace, šifrování, síť, osobní údaje, logování přístupů |
| Monitoring | Logy, dashboardy, alarmy, kdo drží pohotovost |
| Nefunkční požadavky | Doba odezvy, dostupnost, doba uchování logů a souborů |
| Testovací scénáře | Happy path, každá chybová větev, objemový test |

Jádrem je tabulka **data mapping** (mapování dat):

| # | Zdrojové pole | Cílové pole | Typ / formát | Povinné | Transformace / pravidlo |
|---|---|---|---|---|---|
| 1 | `ico` | `Party.registrationId` | text, 8 číslic | ano | ponechat jako text, zachovat úvodní nuly |
| 2 | `obchodniJmeno` | `Party.legalName` | text, max 255 | ano | oříznout mezery |
| 3 | `sidlo.kodStatu` | `Party.countryCode` | ISO 3166 alpha-2 | ano | zkopírovat beze změny |
| 4 | `sidlo.psc` | `Party.postalCode` | text | ne | ve zdroji číslo; převést na text, formát „118 00“ |

Typické pasti, které mapování odhalí: čísla versus text (identifikátory a PSČ), formáty datumů, číselníky, které se mezi systémy liší (hodnoty statusů, kódy právní formy), různé délky polí, znakové sady a diakritika a pole, která existují jen na jedné straně.

### Nástroje do praxe: Postman, JSONPlaceholder a API playground [P1]
**[Postman](https://www.postman.com/downloads/)** je desktopový nástroj pro posílání HTTP požadavků a prohlížení odpovědí. Nastavíš metodu, URL, hlavičky a tělo, stiskneš Send a uvidíš stav, čas, hlavičky a tělo. Požadavky lze ukládat do **collections** (kolekcí) a kontrolovat **testy**: krátkými úryvky JavaScriptu, které proběhnou po příchodu odpovědi, například:

```javascript
pm.test("Status is 200", function () {
  pm.response.to.have.status(200);
});
pm.test("Company ID is returned unchanged", function () {
  pm.expect(pm.response.json().ico).to.eql("00006947");
});
```

**[JSONPlaceholder](https://jsonplaceholder.typicode.com/)** je bezplatné falešné REST API na procvičování. `GET /posts/1` vrátí ukázkový příspěvek. `POST /posts` s JSON tělem vrátí **201** a tvoje data s novým `id` (101), ale nic se doopravdy neuloží; proto je bezpečné na něm zkoušet metody.

**API playground** na webu (`api.html`) umožní poslat stejné požadavky z prohlížeče bez instalace. Používej ho na rychlé kontroly a Postman na kolekce a testy.

ARES je veřejná služba českého státu. Používej ho na občasná ruční volání, ne na hromadné stahování, a dodržuj jeho podmínky užití.

## Key terms
- **API (application programming interface)** (aplikační programové rozhraní) — definovaný způsob, jak programy žádají jiný program o data nebo akce.
- **Client / server** (klient / server) — program, který posílá požadavek, a program, který na něj odpovídá.
- **Endpoint** — konkrétní URL (a metoda) API, která poskytuje jednu funkci, např. `GET /credit-limits/{id}`.
- **HTTP method** (HTTP metoda) — akce požadavku: GET, POST, PUT, PATCH, DELETE.
- **Path parameter / query parameter** (parametr cesty / parametr dotazu) — část cesty URL, která identifikuje zdroj / část `?key=value`, která filtruje nebo upravuje požadavek.
- **Header** (hlavička) — metadata posílaná s požadavkem nebo odpovědí, např. Content-Type nebo Authorization.
- **Payload (body)** (tělo) — data posílaná v požadavku nebo odpovědi.
- **Status code** (stavový kód) — trojmístné číslo v odpovědi, které hlásí výsledek (2xx, 3xx, 4xx, 5xx).
- **REST** — architektonický styl API založený na zdrojích s URL, standardních HTTP metodách a bezstavových požadavcích.
- **JSON** — textový formát z objektů, polí a jednoduchých hodnot, výchozí pro REST API.
- **XML / XSD** — textový formát založený na tazích / schéma, které definuje platné XML zprávy.
- **Namespace** (jmenný prostor) — jedinečný identifikátor, který říká, do jakého slovníku XML elementy patří.
- **SOAP / WSDL** — protokol webových služeb založený na XML / soubor, který popisuje službu SOAP.
- **OAuth 2.0 / bearer token** — rámec pro vydávání přístupových tokenů / token posílaný v hlavičce Authorization pro přístup k API.
- **OpenAPI** — standardní formát v YAML nebo JSON pro popis REST API, který zobrazují nástroje jako Swagger.
- **Idempotency** (idempotence) — vlastnost, že opakování operace má stejný účinek jako její jedno provedení.
- **Webhook** — volání, které server udělá na URL klienta, když nastane událost.
- **Data mapping** (mapování dat) — tabulka, která definuje, jak se každé zdrojové pole stane cílovým polem, včetně transformací.
- **Integration specification** (integrační specifikace) — dokument, který definuje integraci: systémy, spouštěč, data, chyby, bezpečnost, objemy, monitoring.

## Hands-on
:::exercise id="m11-e1" title="Kolekce v Postmanu: ARES a JSONPlaceholder s testy" min="60" tool="Postman"
**Cíl:** volat skutečná API, číst odpovědi a automatizovat jednoduché kontroly.

1. Nainstaluj [Postman](https://www.postman.com/downloads/) (stačí bezplatný plán). Vytvoř kolekci „BA Academy – APIs“.
2. Požadavek 1: `GET https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/00006947`. Pošli ho. Najdi v odpovědi `obchodniJmeno`, `sidlo.textovaAdresa` a `dic`.
3. Požadavek 2: stejná URL s `12345678` na konci. Poznamenej si stavový kód a `kod` v těle.
4. Požadavek 3: stejná URL s `abc` na konci. Poznamenej si stavový kód a `subKod`.
5. Požadavek 4: `GET https://jsonplaceholder.typicode.com/posts/1`.
6. Požadavek 5: `POST https://jsonplaceholder.typicode.com/posts` s hlavičkou `Content-Type: application/json` a tělem `{"title": "Credit limit request", "body": "Buyer Nordhafen Logistik GmbH, 120000 EUR", "userId": 1}`. Zkontroluj stavový kód a vrácené `id`.
7. Ke každému požadavku přidej testy (záložka Scripts / Tests): očekávaný stavový kód a u požadavku 1 to, že `ico` se rovná `"00006947"`. Použij příklad z tohoto modulu.
8. Spusť celou kolekci pomocí Collection Runneru. Zkus stejné požadavky v API playgroundu na webu (`api.html`).

**Hotovo, když:** kolekce má pět požadavků, každý má aspoň jeden test, běh je zelený a umíš vysvětlit rozdíl mezi odpověďmi 400 a 404 z ARES.
:::

:::exercise id="m11-e2" title="Převeď JSON payload do XML a zvaliduj ho" min="45" tool="JSONLint and a text editor"
**Cíl:** pochopit oba formáty tím, že jeden převedeš na druhý.

Použij tento payload hlášení škody (fiktivní data, škoda 12 v datové sadě ExportShield):

```json
{
  "claimId": 12,
  "invoiceNo": "INV-2025-06008",
  "exporter": {"name": "Ostrava Steel Components a.s.", "policyNo": "ES-2025-1009"},
  "buyer": {"name": "Steppe Rail Service LLP", "countryCode": "KZ"},
  "claimedAmount": 11700.00,
  "currency": "EUR",
  "notifiedOn": "2026-02-15",
  "status": "IN_REVIEW",
  "documents": ["invoice.pdf", "reminder-1.pdf", "delivery-note.pdf"]
}
```

1. Vlož ho do [JSONLint](https://jsonlint.com/) a zvaliduj. Pak ho schválně rozbij (odstraň čárku, přidej čárku za poslední položku, použij jednoduché uvozovky) a přečti si chybové hlášky.
2. Napiš stejná data jako XML v textovém editoru. U každého pole rozhodni: element, nebo atribut? (Nápověda: `currency` se hodí jako atribut částky.) Použij jeden kořenový element `ClaimNotification` a namespace `urn:exportshield:claim:v1`. `documents` vyjádři opakovanými elementy.
3. Ulož soubor jako `claim.xml` a otevři ho ve webovém prohlížeči. Prohlížeč ukáže chybu, pokud XML není well-formed (správně utvořené). Oprav případné chyby.
4. Napiš pět pravidel, která by XSD pro tuto zprávu mělo vynucovat (povinné elementy, formát data, povolené hodnoty statusu, typ částky, délka kódu měny). Volitelně: napiš XSD podle ukázky v tomto modulu a zvaliduj ho v editoru, který umí XML, například ve Visual Studio Code s rozšířením pro XML.
5. Napiš tři věty o tom, co šlo snáz vyjádřit v XML a co v JSON.

**Hotovo, když:** tvůj JSON je platný, XML se v prohlížeči otevře bez chyby, každé pole z JSON má protějšek v XML a máš pět pravidel pro XSD.
:::

:::exercise id="m11-e3" title="Mapování polí: z ARES do záznamu subjektu v PolicyHubu" min="45" tool="Excel or Confluence"
**Cíl:** napsat jádro integrační specifikace pro skutečné API.

Scénář: když se v PolicyHubu zadá česká firma (exportér při onboardingu nebo český odběratel), PolicyHub má vyplnit její záznam subjektu (party record) z ARES. Záznam subjektu v PolicyHubu (fiktivní) má: `registrationId` (text 8), `legalName` (text 255), `vatId` (text 14), `legalFormCode` (text 3), `street` (text 100), `houseNumber` (text 20), `city` (text 100), `postalCode` (text 6, formát „118 00“), `countryCode` (text 2), `registerCheckedOn` (datum), `activityCodes` (seznam textů).

1. Zavolej ARES pro `00006947` (Postman nebo `api.html`) a odpověď si nech po ruce.
2. Sestav tabulku mapování se sloupci: #, pole ARES (JSON cesta, např. `sidlo.nazevObce`), pole PolicyHubu, zdrojový typ, cílový typ, povinné, transformační pravidlo, příklad hodnoty.
3. Rozhodni, jak sestavit `houseNumber` z `cisloDomovni` a `cisloOrientacni` (v českých adresách se píše „525/15“) a co dělat, když jedno chybí.
4. Rozhodni, odkud se vezme `registerCheckedOn` (nápověda: v odpovědi není, je to datum volání) a čím se liší od `datumAktualizace`.
5. Vypiš pole PolicyHubu, která v ARES nemají zdroj, a pole ARES, která záměrně nemapuješ.
6. Přidej část o ošetření chyb: co PolicyHub udělá při 404, 400, timeoutu a 5xx.

**Hotovo, když:** každé pole PolicyHubu je buď namapované s pravidlem, nebo výslovně označené „bez zdroje“, transformace čísla domu a PSČ jsou specifikované a všechny čtyři chybové případy mají definované chování.
:::

:::exercise id="m11-e4" title="Přečti soubor OpenAPI ve Swagger Editoru" min="40" tool="Swagger Editor"
**Cíl:** přečíst popis API od dodavatele a zkontrolovat ho proti požadavkům.

1. Otevři [Swagger Editor](https://editor.swagger.io/), vymaž příklad vlevo a vlož YAML níže. Vpravo se zobrazí vykreslená dokumentace. Adresa serveru používá rezervovanou doménu `.example`, takže neexistuje; skutečné požadavky poslat nemůžeš, jen číst.
2. Odpověz: Jaké endpointy existují? Která pole jsou při vytváření úvěrového limitu povinná? Jaké měny jsou povolené? Co API vrátí, když id neexistuje? Jak se klient autentizuje?
3. Porovnej s business pravidly ExportShield: žádost má nést i zemi odběratele a platební podmínky nesmí přesáhnout 180 dní. Je každé pravidlo ve specifikaci?
4. Najdi aspoň dvě mezery (nápověda: dá se vypsat seznam žádostí podle statusu? Je popsaný kód 409 pro duplicitní žádost? Co vrací 401?).
5. Uprav YAML: přidej dotazovací endpoint `GET /credit-limits` s parametrem dotazu `status` (`in: query`). Drž YAML platný: editor označí problémy v textu a dokumentace vpravo musí dál ukazovat všechny endpointy, teď i ten tvůj nový.

```yaml
openapi: 3.0.3
info:
  title: PolicyHub Credit Limit API (training example)
  version: 1.0.0
  description: Fictional API of ExportShield Insurance, used for BA Academy exercises.
servers:
  - url: https://api.exportshield.example/policyhub/v1
paths:
  /credit-limits:
    post:
      summary: Submit a credit limit request
      operationId: createCreditLimit
      security:
        - bearerAuth: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreditLimitRequest'
      responses:
        '201':
          description: Request accepted and stored with status REQUESTED
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreditLimit'
        '400':
          description: Invalid input, for example a missing field or unknown currency
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Missing or invalid access token
  /credit-limits/{id}:
    get:
      summary: Get one credit limit
      operationId: getCreditLimit
      security:
        - bearerAuth: []
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
          example: CL-2026-0041
      responses:
        '200':
          description: The credit limit
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreditLimit'
        '404':
          description: No credit limit with this id
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
  schemas:
    CreditLimitRequest:
      type: object
      required:
        - policyNo
        - buyerId
        - requestedAmount
        - currency
      properties:
        policyNo:
          type: string
          example: ES-2025-1018
        buyerId:
          type: integer
          example: 2
        requestedAmount:
          type: number
          minimum: 1
          example: 120000
        currency:
          type: string
          enum:
            - EUR
            - USD
        paymentTermsDays:
          type: integer
          minimum: 1
          maximum: 180
          example: 60
    CreditLimit:
      type: object
      properties:
        creditLimitId:
          type: string
          example: CL-2026-0041
        policyNo:
          type: string
        buyerId:
          type: integer
        requestedAmount:
          type: number
        approvedAmount:
          type: number
          nullable: true
        currency:
          type: string
        status:
          type: string
          enum:
            - REQUESTED
            - APPROVED
            - REDUCED
            - REJECTED
        requestedOn:
          type: string
          format: date
        decidedOn:
          type: string
          format: date
          nullable: true
    Error:
      type: object
      properties:
        code:
          type: string
          example: INVALID_CURRENCY
        message:
          type: string
          example: Currency must be EUR or USD.
```

**Hotovo, když:** máš odpovědi na pět otázek, aspoň dvě mezery sepsané jako review komentáře a editor po tvé změně nehlásí žádné problémy.
:::

## Self-check
:::q
Jaký je rozdíl mezi parametrem cesty a parametrem dotazu? Uveď příklad každého.
---
Parametr cesty (path parameter) je součást cesty URL a identifikuje konkrétní zdroj, například IČO v `/ekonomicke-subjekty/00006947`. Parametr dotazu (query parameter) následuje za `?` a filtruje, řadí nebo stránkuje výsledek, například `/credit-limits?status=REQUESTED`. Praktické pravidlo: cesta pro „který“, dotaz pro „které z nich“ nebo „jak“.
:::

:::q
ARES vrátí na jeden požadavek 404 a na jiný 400. Co ti každý z nich říká a jak má volající systém reagovat?
---
404 znamená, že požadavek byl platný, ale firma s tímto IČO neexistuje; systém má uživateli říct, že firma v registru není, a nechat ho IČO zkontrolovat. 400 znamená, že neplatný byl samotný požadavek, například IČO nemá 8 číslic; systém tomu má ideálně předejít validací vstupu před voláním. Ani jedno se nemá automaticky opakovat, protože stejný požadavek dá stejný výsledek.
:::

:::q
Proč je problém uložit české IČO nebo PSČ z JSON jako číslo?
---
IČO může mít úvodní nuly (`00006947`), které číslo zahodí, takže hodnota pak neodpovídá registru. IČO a PSČ jsou identifikátory, ne množství; nikdo s nimi nepočítá. ARES vrací `psc` jako číslo, takže mapování ho musí převést na text a doplnit formátování. To je typické transformační pravidlo v mapování dat.
:::

:::q
Kdy zvolíš asynchronní zprávy místo synchronního volání API?
---
Když odesílatel nepotřebuje odpověď hned, když příjemce může být pomalý nebo dočasně nedostupný, nebo když na stejnou událost musí reagovat víc systémů. Například ClaimDesk publikuje „škoda schválena“ a finance zpracují platbu později. Synchronní volání se hodí, když uživatel čeká na odpověď u obrazovky, třeba při kontrole v registru.
:::

:::q
POST „vytvoř platbu“ vyprší (timeout) a klient ho zopakuje. Co se může pokazit a co má říkat požadavek?
---
První požadavek mohl na serveru projít ještě před timeoutem, takže opakování může vytvořit druhou platbu a exportér dostane zaplaceno dvakrát. POST není idempotentní. Požadavek má vyžadovat idempotenční klíč nebo business kontrolu jedinečnosti, aby se opakovaný požadavek rozpoznal a neprovedl dvakrát, a má definovat, kolik opakování je povoleno.
:::

:::q
Jmenuj tři věci, ve kterých se JSON a XML liší.
---
JSON má nativní typy pro čísla, booleovské hodnoty a null, zatímco v XML je všechno text a typy dává XSD. XML má atributy, jmenné prostory a komentáře; JSON nic z toho. JSON je kompaktnější a výchozí pro REST, kdežto XML s XSD je běžné ve službách SOAP a v regulatorním reportingu.
:::

:::q
Kolega vloží bearer token na stránku v Confluence, aby dodavatel mohl API otestovat. Co je špatně a co se má stát místo toho?
---
Token je tajný údaj, který dává přístup; kdokoli, kdo stránku čte, může volat API pod tímto účtem, dokud token nevyprší nebo nebude zneplatněn, a historie stránky si ho uchová. Token se má hned zneplatnit nebo vyměnit. Dodavatel má dostat vlastní testovací přístupové údaje schváleným kanálem, uložené v úložišti tajných údajů, jen s právy, která potřebuje.
:::

## Interview corner
:::interview
Vysvětli business stakeholderovi, co je API.
*EN: Explain what an API is to a business stakeholder.*
---
- Definovaný způsob, jak jeden systém požádá jiný o data nebo o provedení akce, bez člověka mezi nimi.
- Přirovnání: přepážka s pevným formulářem; vyplníš formulář (požadavek) a dostaneš standardní odpověď.
- Konkrétní příklad: PolicyHub se zeptá obchodního rejstříku na adresu firmy, místo aby ji underwriter opisoval.
- Přínosy: méně ručních kroků a překlepů, rychlejší rozhodování, data vždy aktuální.

Typická chyba: odpovídat technickými pojmy (REST, JSON, OAuth), na které se stakeholder neptal.
:::

:::interview
Jak bys specifikovala integraci mezi systémem smluv a systémem škod?
*EN: How would you specify an integration between the policy system and the claims system?*
---
- Účel, systémy, vlastníci, spouštěč a směr.
- Volba vzoru (API, zprávy, soubor) podle potřeb na čerstvost dat, objem a spolehlivost.
- Tabulka mapování dat s typy, povinností a transformacemi.
- Ošetření chyb: validační chyby, timeouty, opakování, idempotence, alarmy.
- Nefunkční požadavky: objemy, doby odezvy, bezpečnost, osobní údaje, monitoring.
- Testovací scénáře pro každou větev, odsouhlasené s dodavatelem a testery.

Typická chyba: specifikovat jen pole a happy path.
:::

:::interview
Jaké HTTP stavové kódy znáš a co znamenají?
*EN: What HTTP status codes do you know and what do they mean?*
---
- Skupiny: 2xx úspěch, 3xx přesměrování, 4xx chyba klienta, 5xx chyba serveru.
- 200 OK, 201 Created, 204 No Content.
- 400 neplatný požadavek, 401 neautentizováno, 403 nepovoleno, 404 nenalezeno, 409 konflikt, 429 příliš mnoho požadavků.
- 500 chyba serveru, 503 služba nedostupná.
- Proč na tom BA záleží: každý kód potřebuje v požadavcích definovanou reakci a test.

Typická chyba: plést si 401 (kdo jsi?) a 403 (vím, kdo jsi, ale nesmíš).
:::

:::interview
Pracovala jsi někdy sama s API?
*EN: Have you ever worked with an API yourself?*
---
- Konkrétní příklad: volání ARES pro IČO v Postmanu, čtení JSON, porovnání odpovědí 200, 400 a 404.
- Testy v Postmanu: stavový kód a hodnota pole.
- Čtení souboru OpenAPI a hledání mezer proti požadavkům.
- Mapování dat odvozené ze skutečné odpovědi, včetně transformací (identifikátory jako text, formátování adresy).

Typická chyba: tvrdit, že máš zkušenost s API, a nebýt schopná popsat jediný požadavek a odpověď.
:::
