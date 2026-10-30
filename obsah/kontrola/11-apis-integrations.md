# Kontrola modulu 11 – APIs, JSON/XML and system integrations

Ověřeno:
- **ARES živě (curl, 30. 10. 2026):** `00006947` vrací 200 a JSON s poli `ico`, `obchodniJmeno` (Ministerstvo financí),
  `sidlo` (Letenská 525/15, `psc` jako číslo 11800), `pravniForma` "325", `dic` CZ00006947, `datumAktualizace`
  2026-03-23, `czNace` ["84110"] (vedle něj existuje i `czNace2008`). `12345678` → 404 `{"kod":"NENALEZENO",…}`,
  `abc` i sedmimístné `1234567` → 400 `{"kod":"CHYBA_VSTUPU","subKod":"VSTUP_NEVALIDNI_FORMAT_ICO",…}`. Vše v textu sedí.
- Všechny 3 bloky JSON jsou platné (Python `json`), XML zpráva a SOAP envelope jsou well-formed. Ukázka XSD je výňatek
  bez deklarace prefixu `xs:` (samostatně neprojde parserem); v textu je označená jako „excerpt“, proto ponecháno.
- Oba bloky YAML (ukázka a OpenAPI 3.0.3 ve cvičení 4) se parsují; `nullable`, `example` u parametru a `securitySchemes`
  odpovídají OpenAPI 3.0.
- Stavové kódy, CRUD tabulka, bezpečnost GET, význam 401/403, REST bezstavovost odpovídají RFC 9110.
- Data případové studie (žádost 41 = smlouva ES-2025-1018, odběratel 2 Nordhafen, 120 000 EUR, 2026-09-14; škoda 12 =
  INV-2025-06008, ES-2025-1009, Steppe Rail KZ, 11 700 EUR, 2026-02-15, IN_REVIEW) sedí s `exportshield.sql`.

| Místo | Bylo | Opraveno na | Proč (zdroj) |
|---|---|---|---|
| Deep dive, Error handling – idempotence | „GET, PUT and DELETE are idempotent by design; POST is not.“ | Podle RFC 9110 jsou idempotentní GET, HEAD, OPTIONS, PUT a DELETE; POST ne a PATCH to není zaručeně. | RFC 9110, kap. 9.2.2: idempotentní jsou PUT, DELETE a bezpečné metody; PATCH (RFC 5789) idempotentní být nemusí. Původní výčet byl neúplný a PATCH chyběl. |
| Deep dive, Authentication – Basic | „user name and password encoded in the Authorization header“ | doplněno: jen Base64, ne šifrování; kdo hlavičku vidí, dekóduje je | RFC 7617. Začátečník by „encoded“ mohl číst jako „zašifrované“. |
| Deep dive, Authentication – OAuth 2.0 | OAuth 2.0 uveden jen pod autentizací | doplněno: OAuth 2.0 je autorizační rámec; přihlášení člověka řeší OpenID Connect nad ním | RFC 6749 (OAuth 2.0 Authorization Framework), OpenID Connect Core 1.0. Častá otázka na pohovoru. |

Stylisticky bez zásahů.
