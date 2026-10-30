# Kontrola modulu 12 – Systems and architecture for analysts

Ověřeno a v pořádku: cloudové modely IaaS/PaaS/SaaS a jejich rozdělení odpovědnosti; C4 model (Simon Brown; úrovně
Context, Containers, Components, Code; „container“ = samostatně spustitelná/nasaditelná část, ne Docker);
DORA – nařízení (EU) 2022/2554, použitelné od 17. 1. 2025, vztahuje se i na pojišťovny a zajišťovny; pilíře řízení
ICT rizik, klasifikace a hlášení závažných ICT incidentů, testování digitální provozní odolnosti, řízení rizik ICT
třetích stran včetně registru informací o smlouvách; GDPR zásady (právní základ, účel, minimalizace, doba uložení);
RPO/RTO; prostředí DEV/SIT/UAT/PROD; CAB. Mermaid bloky jsou syntakticky v pořádku, beze změny.

| Místo | Bylo | Opraveno na | Proč (zdroj) |
|---|---|---|---|
| Deep dive, C4 – poznámka pod diagramy | „Mermaid is not a C4 tool, so this is an approximation“ | Vlastní typ diagramu C4 je v Mermaidu zatím experimentální, proto příklady používají flowcharty jako přiblížení | Mermaid má typ `C4Context`/`C4Container` (dokumentace Mermaid jej označuje jako experimentální). Původní věta byla nepravdivá. |
| Deep dive, JSON příklad rozhodnutí | `"decision": "APPROVED_REDUCED"` | `"decision": "REDUCED"` | Vnitřní konzistence: datová sada (`credit_limits.status`) i OpenAPI v modulu 11 používají hodnoty REQUESTED / APPROVED / REDUCED / REJECTED. |

Poznámka (neopraveno, jen upozornění): modul uvádí dvě různá pravidla – „nad 500 000 EUR druhé schválení“ (Quick,
shodně s moduly 13, 14 a projektem) a „underwriter schvaluje do 250 000 EUR, nad to SENIOR_UNDERWRITER“ (Deep dive,
NFR tabulka, shodně s rozhodovací tabulkou v modulu 04). Logicky si neodporují (pravomoc underwritera vs. druhé
schválení), ale začátečníka mohou mást. Sjednocení by zasáhlo více modulů, proto ponecháno na rozhodnutí autora.

Stylisticky bez zásahů.
