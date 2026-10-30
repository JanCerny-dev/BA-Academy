# Kontrola – závěrečná případová studie (projekt.md)

Kroky odpovídají modulům (MoSCoW je v modulech 03 a 06, Scenario Outline v 07, timer boundary event v 04, ER v 09, sekvenční a stavový diagram v 08).
Krok 7 ověřen proti `data/sql/exportshield.sql`: decided before requested = credit_limits.id 19; chybějící země odběratele = buyers.id 24;
duplicitní číslo faktury = INV-2026-01002 (invoices 2 a 3); claim na zaplacenou fakturu = claims.id 15. Všechny čtyři problémy v datech existují.
ARES: neplatný formát IČO vrací HTTP 400, neexistující IČO 404 (ověřeno 30. 10. 2026).

| Místo | Bylo | Opraveno na | Proč (zdroj) |
|---|---|---|---|
| The brief, příklad limitu | „…invoices to Nordic Timber AB“ | „…invoices to Rheinwerk Handels GmbH“ | Odběratel z datové sady (buyers.id 1); „Nordic Timber AB“ v datech není a mohl by kolidovat se skutečnou firmou. |
| Krok 5, bod 3 | „prioritise with MoSCoW“ | „prioritize with MoSCoW (see modules 03 and 06)“ | MoSCoW se vykládá v modulech 03 a 06, ne v 07. |
| Krok 8, bod 3 | „invalid IČO format.“ | „invalid IČO format (400).“ | ARES vrací pro špatný formát IČO stavový kód 400 (`VSTUP_NEVALIDNI_FORMAT_ICO`). |

Stylistické drobnosti: britské tvary (judgement, analyse, anonymised, labelled, prioritise, optimise) sjednoceny na americké podle PRAVIDLA.
Poznámka: krok 1 uvádí jako příklad předpokladu 6 000 žádostí ročně a 20 min, modul 14 počítá se 40 týdně a 15 min. Jde o jinou, výslovně označenou sadu předpokladů, ponecháno.
