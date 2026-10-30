# Kontrola modulu 06 – Writing requirements and specifications

Modul je věcně v pořádku v hlavních bodech: MoSCoW (DSDM: Must / Should / Could / Won't have this time), Kano (basic / performance / delighters), RTO/RPO, konvence shall/should/may/will (ISO/IEC/IEEE 29148), struktura use case (primary actor, preconditions, trigger, main / alternative / exception flows, postconditions). Opraveny dvě nepřesnosti vůči normě a dva vnitřní rozpory v ukázkovém use case UC-03.

| Místo | Bylo | Opraveno na | Proč (zdroj) |
|---|---|---|---|
| Deep dive, „What makes a requirement good“, úvodní věta | „this table uses the common core“ (bez rozlišení vydání normy) | Doplněno: 29148:2018 uvádí pro jednotlivý požadavek necessary, appropriate, unambiguous, complete, singular, feasible, verifiable, correct, conforming; consistency je vlastnost celé množiny požadavků; vydání 2011 mělo navíc traceable a implementation-free | ISO/IEC/IEEE 29148:2018, kap. 5.2.5 a 5.2.6; tabulka v modulu (consistent, traceable, implementation-free jako vlastnosti jednoho požadavku) odpovídá vydání 2011, ne aktuálnímu |
| Tabulka charakteristik, řádek Verifiable + Key terms „Verifiable“ | „test, inspection or analysis“ | „inspection, analysis, demonstration or test“ | ISO/IEC/IEEE 29148 i ISTQB uvádějí čtyři metody verifikace; chyběla demonstration |
| UC-03, Preconditions | „buyer country is CZ“ | „the buyer country is selected“ | Vnitřní rozpor: alternativní tok A1 „Buyer is not Czech“ by při této precondition nemohl nastat |
| UC-03, A1 | „Buyer is not Czech (at step 1)“ | „Buyer country is not CZ (before step 1)“ | Navazuje na opravenou precondition; tlačítko „Look up“ se skrývá ještě před krokem 1 |
| UC-03, Related | „BR-04“ | „BR-G1“ | BR-04 v modulu neexistuje (business rules jsou jen BR-01 až BR-03); UC-03 souvisí s business requirementem BR-G1 „reduce manual data entry“ z RTM a cvičení m06-e3 |

Bez stylistických změn. Poznámka: prefix BR- se v modulu používá pro business rules (BR-01) i business requirements (BR-G1). Je to rozlišené, ale pro začátečnici to může být matoucí; ponecháno, protože na BR-G1 odkazují i cvičení.
