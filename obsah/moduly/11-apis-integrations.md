---
id: 11
slug: apis-integrations
title: APIs, JSON/XML and system integrations
phase: C
priority: P1
quick_min: 20
deep_min: 90
job_ad: "práce s API a formáty JSON/XML"
---

## Why this matters
The job ad lists API, JSON and XML among the basic skills. In an insurer, almost every change touches an integration: the policy system sends data to the claims system, the portal calls a company register, finance receives a payment file. The analyst does not write the integration code, but writes what it must do: which data goes where, when, in which format, and what happens when something fails. To do that you must be able to read API documentation, call an API yourself to see real data, and describe field mappings precisely enough for a vendor to build and a tester to test.

## Quick version
**API** (application programming interface) is a defined way for one program to ask another program for data or to trigger an action. A website is made for people; an API is made for programs.

**Client and server.** The **client** sends a **request**; the **server** processes it and returns a **response**. The portal (client) asks PolicyHub (server) for a policy. PolicyHub can itself be the client of another server, for example ARES.

**An HTTP request has:**

- a **method** (what to do): `GET` read, `POST` create, `PUT` replace, `PATCH` change part, `DELETE` remove;
- a **URL** (where): server address plus **path** (`/credit-limits/CL-2026-0041`) and optional **query parameters** (`?status=REQUESTED`);
- **headers** (metadata): content type, accepted format, authorization;
- an optional **body** (the data sent, usually JSON), also called the **payload**.

**An HTTP response has** a **status code**, headers and usually a body. The status codes to know:

| Code | Meaning |
|---|---|
| 200 OK | success, data in the body |
| 201 Created | a new record was created |
| 204 No Content | success, nothing to return |
| 400 Bad Request | the request is invalid (wrong format, missing field) |
| 401 Unauthorized | not authenticated (no or invalid credentials) |
| 403 Forbidden | authenticated, but not allowed |
| 404 Not Found | the resource does not exist |
| 409 Conflict | conflicts with the current state (e.g. a duplicate) |
| 429 Too Many Requests | the client sent too many requests |
| 500 Internal Server Error | the server failed |
| 503 Service Unavailable | the server is down or overloaded |

Rule of thumb: 2xx success, 3xx redirect, 4xx the client did something wrong, 5xx the server has a problem.

**REST** is a common style for web APIs: everything is a **resource** with its own URL (`/credit-limits`, `/credit-limits/{id}`), standard HTTP methods act on it, and each request carries everything needed (the server keeps no session memory between calls).

**JSON** and **XML** are text formats for structured data:

- JSON: `{"status": "REQUESTED", "requestedAmount": 120000}`. Light, the default for REST.
- XML: `<Status>REQUESTED</Status>`. Verbose, but with strong validation through **XSD** schemas. Still common in banks, insurers and public administration, often with **SOAP** web services.

**Authentication** proves who calls the API: an **API key**, **Basic** authentication (user and password), or **OAuth 2.0** with a short-lived **bearer token**. Secrets never belong in documents, code, tickets or chat.

**Integration patterns:** synchronous API call (answer now), asynchronous messaging through a queue (answer later, decoupled), batch file transfer (e.g. a nightly CSV over SFTP), webhooks (the server calls you when something happens), ETL into a data warehouse. The choice depends on how fast the data is needed, volumes and reliability.

**What the analyst writes:** an **integration specification**: systems, trigger, direction, frequency, a field-by-field **data mapping**, error handling, volumes, security and monitoring.

**Practice with real APIs:** the Czech company register ARES (`GET https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/00006947` returns the Ministry of Finance as JSON), the test API JSONPlaceholder, the site's API playground (`api.html`) and [Postman](https://www.postman.com/downloads/).

**Interview one-liner:** "I can read API documentation and OpenAPI specs, call an API in Postman, read JSON and XML, and write an integration spec with a data mapping, error handling and non-functional requirements."

## Deep dive

### Client, server and HTTP [P1]
**HTTP** (Hypertext Transfer Protocol) is the protocol of the web; **HTTPS** is the same protocol encrypted. Your browser uses it to load pages, and most APIs use it to exchange data.

A real request to ARES, the Czech public register of economic entities, looks like this on the wire (simplified):

```text
GET /ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/00006947 HTTP/1.1
Host: ares.gov.cz
Accept: application/json
```

- `GET` is the method: read data.
- The path ends with the company ID (IČO, 8 digits). It is a **path parameter**: part of the URL that identifies the resource.
- `Host` names the server.
- `Accept` is a header saying which format the client wants.
- A GET has no body.

The response (abbreviated; the real one has more fields, and values such as the update date change over time):

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

The status line of this response is `200` and the header `Content-Type: application/json` tells the client how to read the body. Field names are Czech: `obchodniJmeno` is the business name, `sidlo` the registered address, `psc` the postal code, `dic` the VAT number, `pravniForma` a code of the legal form, `czNace` the activity codes.

Two errors, also real:

- an ID that does not exist (e.g. `12345678`) returns **404** with a body `{"kod": "NENALEZENO", ...}` ("not found");
- an ID in the wrong format (e.g. `abc` or 7 digits) returns **400** with `{"kod": "CHYBA_VSTUPU", "subKod": "VSTUP_NEVALIDNI_FORMAT_ICO", ...}` ("input error, invalid ID format").

Notice that the error bodies are machine-readable codes plus a human message. When you specify an integration, ask for exactly this: which status codes and error codes exist, and what the calling system must do with each.

**Query parameters** follow a `?` and filter or modify a request: `GET /credit-limits?status=REQUESTED&currency=EUR`. Path parameters identify one thing; query parameters filter, sort or page through lists.

**Headers** you will meet often: `Content-Type` (format of the body sent), `Accept` (format wanted back), `Authorization` (credentials), and sometimes a correlation ID (a unique ID per request for tracing it through logs).

### REST in plain terms [P1]
**REST** (Representational State Transfer) is an architectural style, not a standard with a specification. In practice "REST API" means:

- **Resources** have URLs: `/policies`, `/policies/ES-2025-1018`, `/policies/ES-2025-1018/credit-limits`.
- **HTTP methods** say what to do with them.
- **Stateless**: each request contains everything the server needs (including credentials). The server does not remember previous calls.
- **Standard status codes** report the outcome.
- Representations, usually JSON, carry the data.

CRUD (create, read, update, delete) maps onto methods:

| Operation | Method | Example | Typical success code |
|---|---|---|---|
| Create | POST | `POST /credit-limits` with a JSON body | 201 |
| Read one | GET | `GET /credit-limits/CL-2026-0041` | 200 |
| Read list | GET | `GET /credit-limits?status=REQUESTED` | 200 |
| Update whole | PUT | `PUT /credit-limits/CL-2026-0041` | 200 or 204 |
| Update part | PATCH | `PATCH /credit-limits/CL-2026-0041` with `{"status": "APPROVED"}` | 200 or 204 |
| Delete | DELETE | `DELETE /credit-limits/CL-2026-0041` | 204 |

GET must not change data. That matters for monitoring tools, caches and retries that may repeat a GET at any time.

### JSON and XML side by side [P1]
The same credit limit request (based on request 41 in the ExportShield dataset) in both formats.

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

JSON rules:

- An **object** is in curly braces `{}` with `"key": value` pairs separated by commas.
- An **array** (list) is in square brackets `[]`.
- Value types: string in double quotes, number (no quotes, decimal point, no thousands separator), `true`/`false`, `null`, object, array.
- Objects and arrays can be **nested**: `buyer` is an object inside the main object.
- JSON has **no date type**. Dates are strings, so the format must be agreed (ISO 8601 `YYYY-MM-DD` is the norm).
- Keys are case-sensitive. No comments, no trailing comma after the last item. A single wrong comma makes the whole document invalid; [JSONLint](https://jsonlint.com/) finds it.

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

XML rules:

- **Elements** have a start and end tag: `<Status>REQUESTED</Status>`. Exactly one root element wraps everything.
- **Attributes** sit inside the start tag: `currency="EUR"`. Typically used for metadata about a value.
- Tags are case-sensitive and must be properly nested.
- Repeated elements (`<Risk>` twice) form a list.
- A **namespace** (`xmlns="urn:exportshield:credit-limit:v1"`) is a unique name that tells which vocabulary the tags belong to, so that `<Status>` from two different standards does not clash. It looks like an address but is only an identifier.
- Comments are allowed (`<!-- ... -->`).

**XSD** (XML Schema Definition) is a separate XML document that defines what a valid message looks like: which elements, in which order, which are mandatory, their data types and allowed values. An excerpt:

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

With this schema, `<RequestedOn>14.09.2026</RequestedOn>` is rejected because `xs:date` requires `2026-09-14`. That is why XML is popular in regulated environments: the contract is machine-checkable. JSON has an equivalent, **JSON Schema**, and OpenAPI uses a variant of it.

| | JSON | XML |
|---|---|---|
| Typical use | REST APIs, web and mobile apps | SOAP services, regulatory reporting, older enterprise integrations |
| Size | compact | more verbose |
| Data types | string, number, boolean, null, object, array | everything is text; types come from the XSD |
| Attributes | no | yes |
| Comments | no | yes |
| Schema | JSON Schema, OpenAPI | XSD |

### SOAP and WSDL [P2]
**SOAP** is an older protocol for web services that sends XML messages inside an **envelope**, usually over HTTP POST. You will meet it in banks, insurers and state administration because many core systems were integrated in the 2000s and still work well.

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

- The **Envelope** wraps everything, the optional **Header** carries metadata such as security tokens, the **Body** carries the operation and its data.
- Errors come back as a **SOAP Fault** element in the body.
- A **WSDL** (Web Services Description Language) file describes the service: its operations, the XML messages (via XSD) and the endpoint address. Tools generate client code from it.

Differences from REST for an analyst: SOAP is operation-centered (`GetCreditLimit`) rather than resource-centered, always XML, with a strict contract in the WSDL. The questions in an integration spec stay the same.

### Authentication and secrets [P1]
**Authentication** answers "who are you?"; **authorization** answers "what may you do?".

- **API key**: a long secret string sent in a header. Simple; identifies the calling application, not a person.
- **Basic authentication**: user name and password in the `Authorization` header, only Base64-encoded, not encrypted (anyone who sees the header can decode them). Only acceptable over HTTPS; common in older internal integrations.
- **OAuth 2.0**: the client first obtains an **access token** from an authorization server, then sends it as `Authorization: Bearer <token>` with each call. Tokens expire (often after minutes or hours) and carry **scopes**, which limit what the caller may do. In system-to-system integrations the "client credentials" flow is typical; when a user logs in, other flows are used. Microsoft Entra ID and similar identity platforms issue such tokens. Strictly speaking, OAuth 2.0 is an authorization framework (it grants access); signing in a person is done by OpenID Connect, a layer built on top of OAuth 2.0.
- **Mutual TLS (mTLS)**: both sides prove their identity with certificates. Common between banks and insurers.

Rules an analyst writes into requirements, and follows personally:

- Credentials and tokens are **secrets**. They belong in a secrets store (e.g. a key vault or the platform's credential manager), never in specifications, Confluence pages, tickets, code, e-mails, screenshots or AI chats.
- Each integration gets its own technical account with the minimum rights it needs (**least privilege**).
- Specify how secrets are rotated and who owns the technical account.
- In Postman, keep secrets in variables marked as secret and do not share collections that contain them. For the public APIs in this module no secrets are needed at all.

### Reading API documentation and OpenAPI [P1]
Good API documentation answers: base URL, authentication, list of endpoints, parameters, request and response bodies with examples, error codes, limits (rate limits, page sizes) and versioning.

**OpenAPI** (formerly Swagger) is the standard format for describing REST APIs in YAML or JSON. Many vendors deliver an OpenAPI file instead of a Word document. A short excerpt:

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

How to read it: under `paths` each URL; under each URL the methods; for each method the `parameters` (here a mandatory path parameter `id`), the `requestBody` if any, and the `responses` by status code. `components/schemas` define the data structures with types, mandatory fields (`required`), formats and allowed values (`enum`). Open a file in [Swagger Editor](https://editor.swagger.io/) to see it rendered as readable documentation; exercise 4 does exactly that.

As an analyst, check an OpenAPI file against your requirements: are all fields from the mapping there, are mandatory fields marked, are enums complete, are error responses described?

### Integration patterns [P1]
| Pattern | How it works | Use when | ExportShield example |
|---|---|---|---|
| Synchronous API call | Client calls, waits for the answer | A user or process needs the answer now; small data | PolicyHub checks a company in ARES while the underwriter waits |
| Asynchronous messaging (queue, topic) | Sender puts a message on a queue; receiver processes it later | Systems must be decoupled; receiver may be slow or down; events | ClaimDesk publishes "claim approved"; finance picks it up and pays |
| Batch file transfer | A file (CSV, XML) is created and moved, often via SFTP, on a schedule | Large volumes, no need for real time, legacy systems | Nightly CSV of all paid indemnities to the accounting system |
| Webhook | The server calls the client's URL when an event happens | You want to be notified instead of asking repeatedly | A document service calls DocVault when a signed contract arrives |
| ETL / data replication | Data is extracted, transformed and loaded into another store | Reporting, data warehouse, migrations | Daily load of policies and claims into the reporting database |

Questions that decide the pattern: How fresh must the data be (seconds, hours, next day)? How many records? What happens if the receiver is down: should the sender fail, wait, or queue? Does the business need confirmation that the data arrived?

**Polling** (asking every few minutes "anything new?") is the simple alternative to webhooks and messaging. It works, but wastes calls and adds delay.

### Error handling, idempotency and retries [P2]
Integrations fail: networks drop, servers restart, data is invalid. A specification must say what happens in each case, otherwise the developer decides alone.

- **Validation errors (4xx)**: do not retry; the request will fail again. Log, notify a person or put it into an error queue for manual handling.
- **Temporary errors (timeouts, 503, 429)**: retry a limited number of times with increasing waits (**exponential backoff**: e.g. after 1, 2, 4 seconds), then give up and alert.
- **Timeouts**: specify how long the client waits. For a user waiting on screen, a few seconds at most, then a clear message.
- **Idempotency**: an operation is **idempotent** if doing it twice has the same effect as doing it once. By definition in the HTTP standard (RFC 9110), GET, HEAD, OPTIONS, PUT and DELETE are idempotent; POST is not, and PATCH is not guaranteed to be. If a "pay indemnity" POST times out and is retried, the exporter might be paid twice. Solutions: an **idempotency key** (a unique ID sent with the request; the server ignores repeats with the same key) or a business check (one payment per claim instalment number).
- **Partial failure in batches**: if row 5,000 of 10,000 is invalid, does the whole file fail or only that row? Write it down.
- **Monitoring and alerting**: who gets told when the integration fails, and how quickly?

An example requirement: "If ARES does not respond within 5 seconds, PolicyHub retries once. If the second attempt fails, PolicyHub shows 'Register unavailable, try later', logs the error with the correlation ID, and allows the underwriter to continue without register data; the request is flagged 'register check pending'."

### Writing an integration specification [P1]
A template that works for most integrations:

| Section | Content |
|---|---|
| Purpose | The business reason in one or two sentences |
| Systems | Source, target, owner of each, vendor contacts |
| Trigger | Event (user action, status change), schedule or file arrival |
| Direction and pattern | One-way or two-way; API, message, file, webhook |
| Frequency and volumes | Calls per day, peak per hour, file size, expected growth |
| Data mapping | Table of fields (see below) |
| Validation rules | What makes a message valid; what happens to invalid ones |
| Error handling | Per error type: retry, alert, manual handling |
| Security | Authentication, encryption, network, personal data, logging of access |
| Monitoring | Logs, dashboards, alerts, who is on call |
| Non-functional | Response time, availability, retention of logs and files |
| Test scenarios | Happy path, every error branch, volume test |

The **data mapping** table is the core:

| # | Source field | Target field | Type / format | Mandatory | Transformation / rule |
|---|---|---|---|---|---|
| 1 | `ico` | `Party.registrationId` | text, 8 digits | yes | keep as text, keep leading zeros |
| 2 | `obchodniJmeno` | `Party.legalName` | text, max 255 | yes | trim spaces |
| 3 | `sidlo.kodStatu` | `Party.countryCode` | ISO 3166 alpha-2 | yes | copy as is |
| 4 | `sidlo.psc` | `Party.postalCode` | text | no | number in source; convert to text, format "118 00" |

Typical traps the mapping reveals: numbers versus text (IDs and postal codes), date formats, code lists that differ between systems (status values, legal form codes), different field lengths, character sets and diacritics, and fields that exist on one side only.

### Hands-on tools: Postman, JSONPlaceholder and the API playground [P1]
**[Postman](https://www.postman.com/downloads/)** is a desktop tool for sending HTTP requests and inspecting responses. You set the method, URL, headers and body, press Send and see the status, time, headers and body. Requests can be saved in **collections** and checked by **tests**: short JavaScript snippets that run after the response arrives, for example:

```javascript
pm.test("Status is 200", function () {
  pm.response.to.have.status(200);
});
pm.test("Company ID is returned unchanged", function () {
  pm.expect(pm.response.json().ico).to.eql("00006947");
});
```

**[JSONPlaceholder](https://jsonplaceholder.typicode.com/)** is a free fake REST API for practice. `GET /posts/1` returns a sample post. `POST /posts` with a JSON body returns **201** and your data with a new `id` (101), but nothing is really saved; that makes it safe to experiment with methods.

The site's **API playground** (`api.html`) lets you send the same requests from the browser without installing anything. Use it for quick checks and Postman for collections and tests.

ARES is a public service of the Czech state. Use it for occasional manual calls, not for bulk loads, and respect its terms of use.

## Key terms
- **API (application programming interface)** — a defined way for programs to request data or actions from another program.
- **Client / server** — the program that sends a request and the program that answers it.
- **Endpoint** — a specific URL (and method) of an API that provides one function, e.g. `GET /credit-limits/{id}`.
- **HTTP method** — the action of a request: GET, POST, PUT, PATCH, DELETE.
- **Path parameter / query parameter** — a part of the URL path that identifies a resource / a `?key=value` part that filters or modifies the request.
- **Header** — metadata sent with a request or response, e.g. Content-Type or Authorization.
- **Payload (body)** — the data sent in a request or response.
- **Status code** — a three-digit number in the response that reports the outcome (2xx, 3xx, 4xx, 5xx).
- **REST** — an architectural style for APIs based on resources with URLs, standard HTTP methods and stateless requests.
- **JSON** — a text format of objects, arrays and simple values, the default for REST APIs.
- **XML / XSD** — a tag-based text format / the schema that defines valid XML messages.
- **Namespace** — a unique identifier that tells which vocabulary XML elements belong to.
- **SOAP / WSDL** — an XML-based web service protocol / the file that describes a SOAP service.
- **OAuth 2.0 / bearer token** — a framework for issuing access tokens / a token sent in the Authorization header to access an API.
- **OpenAPI** — a standard YAML or JSON format for describing REST APIs, displayed by tools such as Swagger.
- **Idempotency** — the property that repeating an operation has the same effect as doing it once.
- **Webhook** — a call the server makes to a client's URL when an event happens.
- **Data mapping** — a table that defines how each source field becomes a target field, with transformations.
- **Integration specification** — the document that defines an integration: systems, trigger, data, errors, security, volumes, monitoring.

## Hands-on
:::exercise id="m11-e1" title="Postman collection: ARES and JSONPlaceholder with tests" min="60" tool="Postman"
**Goal:** call real APIs, read the responses and automate simple checks.

1. Install [Postman](https://www.postman.com/downloads/) (the free plan is enough). Create a collection "BA Academy – APIs".
2. Request 1: `GET https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/00006947`. Send it. Find `obchodniJmeno`, `sidlo.textovaAdresa` and `dic` in the response.
3. Request 2: the same URL with `12345678` at the end. Note the status code and the `kod` in the body.
4. Request 3: the same URL with `abc` at the end. Note the status code and the `subKod`.
5. Request 4: `GET https://jsonplaceholder.typicode.com/posts/1`.
6. Request 5: `POST https://jsonplaceholder.typicode.com/posts` with header `Content-Type: application/json` and body `{"title": "Credit limit request", "body": "Buyer Nordhafen Logistik GmbH, 120000 EUR", "userId": 1}`. Check the status code and the returned `id`.
7. Add tests (Scripts / Tests tab) to each request: the expected status code, and for request 1 that `ico` equals `"00006947"`. Use the example from this module.
8. Run the whole collection with the Collection Runner. Try the same requests in the site's API playground (`api.html`).

**Done when:** the collection has five requests, every request has at least one test, the run is green, and you can explain the difference between the 400 and 404 responses from ARES.
:::

:::exercise id="m11-e2" title="Convert a JSON payload to XML and validate it" min="45" tool="JSONLint and a text editor"
**Goal:** understand both formats by translating one into the other.

Use this claim notification payload (fictional data, claim 12 in the ExportShield dataset):

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

1. Paste it into [JSONLint](https://jsonlint.com/) and validate. Then break it on purpose (remove a comma, add a trailing comma, use single quotes) and read the error messages.
2. Write the same data as XML in a text editor. Decide for each field: element or attribute? (Hint: `currency` works well as an attribute of the amount.) Use one root element `ClaimNotification` and a namespace `urn:exportshield:claim:v1`. Represent `documents` as repeated elements.
3. Save it as `claim.xml` and open it in your web browser. A browser shows an error if the XML is not well-formed. Fix any errors.
4. Write five rules an XSD for this message should enforce (mandatory elements, date format, allowed status values, amount type, currency code length). Optional: write the XSD, starting from the excerpt in this module, and validate with an XML-aware editor such as Visual Studio Code with an XML extension.
5. Write three sentences on what was easier to express in XML and what in JSON.

**Done when:** your JSON is valid, your XML opens in the browser without error, every JSON field has an XML counterpart, and you have the five XSD rules.
:::

:::exercise id="m11-e3" title="Field mapping: ARES to a PolicyHub party record" min="45" tool="Excel or Confluence"
**Goal:** write the core of an integration specification for a real API.

Scenario: when a Czech company is entered in PolicyHub (an exporter during onboarding, or a Czech buyer), PolicyHub should fill its party record from ARES. The PolicyHub party record (fictional) has: `registrationId` (text 8), `legalName` (text 255), `vatId` (text 14), `legalFormCode` (text 3), `street` (text 100), `houseNumber` (text 20), `city` (text 100), `postalCode` (text 6, format "118 00"), `countryCode` (text 2), `registerCheckedOn` (date), `activityCodes` (list of text).

1. Call ARES for `00006947` (Postman or `api.html`) and keep the response next to you.
2. Build a mapping table with columns: #, ARES field (JSON path, e.g. `sidlo.nazevObce`), PolicyHub field, source type, target type, mandatory, transformation rule, example value.
3. Decide how to build `houseNumber` from `cisloDomovni` and `cisloOrientacni` (in Czech addresses written as "525/15"), and what to do when one is missing.
4. Decide where `registerCheckedOn` comes from (hint: it is not in the response, it is the date of the call) and how it differs from `datumAktualizace`.
5. List the PolicyHub fields with no ARES source and the ARES fields you deliberately do not map.
6. Add an error-handling section: what PolicyHub does for 404, 400, timeout and 5xx.

**Done when:** every PolicyHub field is either mapped with a rule or explicitly marked "no source", the house number and postal code transformations are specified, and all four error cases have a defined behavior.
:::

:::exercise id="m11-e4" title="Read an OpenAPI file in Swagger Editor" min="40" tool="Swagger Editor"
**Goal:** read a vendor's API description and check it against requirements.

1. Open [Swagger Editor](https://editor.swagger.io/), clear the example on the left and paste the YAML below. The right side shows the rendered documentation. The server address uses the reserved `.example` domain, so it does not exist; you cannot send real requests, only read.
2. Answer: Which endpoints exist? Which fields are mandatory when creating a credit limit? Which currencies are allowed? What does the API return when the id does not exist? How does a client authenticate?
3. Compare with the ExportShield business rules: the request should also carry the buyer's country and the payment terms must not exceed 180 days. Is each rule in the spec?
4. Find at least two gaps (hint: is there a way to list requests by status? Is a 409 for a duplicate request described? What does 401 return?).
5. Edit the YAML: add the query endpoint `GET /credit-limits` with a `status` query parameter (`in: query`). Keep the YAML valid: the editor marks problems in the text, and the documentation on the right must still show all endpoints, now including your new one.

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

**Done when:** you have answered the five questions, listed at least two gaps as review comments, and the editor shows no problems after your change.
:::

## Self-check
:::q
What is the difference between a path parameter and a query parameter? Give an example of each.
---
A path parameter is part of the URL path and identifies a specific resource, such as the company ID in `/ekonomicke-subjekty/00006947`. A query parameter comes after `?` and filters, sorts or pages a result, such as `/credit-limits?status=REQUESTED`. Rule of thumb: path for "which one", query for "which of them" or "how".
:::

:::q
ARES returns 404 for one request and 400 for another. What does each tell you, and how should the calling system react?
---
404 means the request was valid but no company with that ID exists; the system should tell the user that the company is not in the register and let them check the ID. 400 means the request itself was invalid, for example the ID is not 8 digits; the system should ideally prevent this by validating the input before calling. Neither should be retried automatically, because repeating the same request gives the same result.
:::

:::q
Why is it a problem to store a Czech company ID or a postal code from JSON as a number?
---
IDs can have leading zeros (`00006947`), which a number drops, so the value no longer matches the register. IDs and postal codes are identifiers, not quantities; nobody calculates with them. ARES returns `psc` as a number, so the mapping must convert it to text and add formatting. This is a typical transformation rule in a data mapping.
:::

:::q
When would you choose asynchronous messaging instead of a synchronous API call?
---
When the sender does not need the answer immediately, when the receiver may be slow or temporarily unavailable, or when several systems need to react to the same event. For example, ClaimDesk publishes "claim approved" and finance processes the payment later. A synchronous call fits when a user is waiting on screen for the answer, such as a register check.
:::

:::q
A "create payment" POST times out and the client retries it. What can go wrong, and what should the requirement say?
---
The first request may have succeeded on the server before the timeout, so the retry can create a second payment and the exporter is paid twice. POST is not idempotent. The requirement should demand an idempotency key or a business uniqueness check so that a repeated request is recognized and not executed twice, and it should define how many retries are allowed.
:::

:::q
Name three things that differ between JSON and XML.
---
JSON has native types for numbers, booleans and null, while in XML everything is text and types come from an XSD. XML has attributes, namespaces and comments; JSON has none of them. JSON is more compact and the default for REST, while XML with XSD is common in SOAP services and regulated reporting.
:::

:::q
A colleague pastes a bearer token into a Confluence page so the vendor can test the API. What is wrong and what should happen instead?
---
A token is a secret that grants access; anyone who can read the page can call the API as that account until the token expires or is revoked, and the page history keeps it. It should be revoked or rotated now. The vendor should get its own test credentials through the approved channel, stored in a secrets store, with only the rights it needs.
:::

## Interview corner
:::interview
Explain what an API is to a business stakeholder.
---
- A defined way for one system to ask another for data or to trigger an action, without a person in between.
- Analogy: a service counter with a fixed form; you fill in the form (request) and get a standard answer (response).
- A concrete example: PolicyHub asks the company register for a company's address instead of the underwriter copying it.
- Benefits: fewer manual steps and typing errors, faster decisions, data always current.

Typical mistake: answering with technical terms (REST, JSON, OAuth) that the stakeholder did not ask about.
:::

:::interview
How would you specify an integration between the policy system and the claims system?
---
- Purpose, systems, owners, trigger and direction.
- Choice of pattern (API, messaging, file) based on freshness, volume and reliability needs.
- Data mapping table with types, mandatory flags and transformations.
- Error handling: validation errors, timeouts, retries, idempotency, alerting.
- Non-functional: volumes, response times, security, personal data, monitoring.
- Test scenarios for every branch, agreed with the vendor and testers.

Typical mistake: specifying only the fields and the happy path.
:::

:::interview
What HTTP status codes do you know and what do they mean?
---
- Groups: 2xx success, 3xx redirection, 4xx client error, 5xx server error.
- 200 OK, 201 Created, 204 No Content.
- 400 invalid request, 401 not authenticated, 403 not allowed, 404 not found, 409 conflict, 429 too many requests.
- 500 server error, 503 service unavailable.
- Why it matters for a BA: each code needs a defined reaction in the requirements and a test.

Typical mistake: mixing up 401 (who are you?) and 403 (I know you, but you may not).
:::

:::interview
Have you ever worked with an API yourself?
---
- A concrete example: calling ARES for a company ID in Postman, reading the JSON, comparing 200, 400 and 404 responses.
- Tests in Postman: status code and a field value.
- Reading an OpenAPI file and finding gaps against requirements.
- A data mapping derived from a real response, including transformations (IDs as text, address formatting).

Typical mistake: claiming API experience without being able to describe a single request and response.
:::
