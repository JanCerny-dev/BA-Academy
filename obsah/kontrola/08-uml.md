# Kontrola modulu 08 – UML 2.5 for business analysts

Modul je věcně v pořádku: 14 typů diagramů UML 2.5.1 (7 strukturních vč. profile, 7 behaviorálních), směr «include» (od základního k zahrnutému use case, v PlantUML `UC1 ..> UC2`) a «extend» (od rozšiřujícího k základnímu), notace zpráv v sekvenčním diagramu (synchronní plná šipka, asynchronní otevřená, reply čárkovaně), combined fragments alt/opt/loop/par, multiplicity, generalizace a kompozice, transition `trigger [guard] / effect`. Stavy v ukázce state machine (NOTIFIED, IN_REVIEW, APPROVED, REJECTED, PAID) sedí s hodnotami `claims.status` v datové sadě, asociace v doménovém modelu sedí s cizími klíči (`invoices.policy_id`, `invoices.buyer_id`, `claims.invoice_id`). Chování ARES (404 `NENALEZENO`, 400 při špatném formátu IČO) sedí s modulem 11.

| Místo | Bylo | Opraveno na | Proč (zdroj) |
|---|---|---|---|
| Deep dive, Activity diagram, popis symbolů | „a circle with a ring as end“ | „a filled circle inside a ring as the end of the whole activity (a circle with an X ends only one flow)“ | UML 2.5.1, kap. 15: activity final node (terč) vs. flow final node (kruh s X); původní popis byl nepřesný |
| Deep dive, tabulka BPMN vs. activity diagram, řádek „Executable in workflow engines“ | UML: „No“ | „Not in everyday practice“ | Spustitelná podmnožina UML existuje (OMG fUML, Alf), jen se v praxi workflow enginů nepoužívá; „No“ bylo příliš absolutní |
| Deep dive, State machine, popis symbolů | „the circled dot the final state“ | „the filled dot inside a ring the final state“ + doplněn zápis `trigger [guard] / effect` a poznámka, že Mermaid píše obojí jako `[*]` | UML 2.5.1, kap. 14: final state = terč; doplnění pro čtení ukázky v Mermaid |
| Deep dive, Sequence diagram, popis ARES | „the Czech public business register API“ | „the Czech public register of economic entities, which combines data from several official registers and offers a free API (… module 11)“ | ARES (Administrativní registr ekonomických subjektů) je informační systém, který agreguje data z více registrů (obchodní, živnostenský aj.); není to obchodní rejstřík |

Bez stylistických změn.
