# Kontrola modulu 13 – Testing, UAT and accepting vendor deliveries

Kontrolováno proti ISTQB CTFL v4.0 (sylabus a glosář). V pořádku: definice statického testování, smoke testu,
severity vs. priority, životní cyklus defektu, šablona testovacího případu, traceability, rozhodovací tabulka
(R1–R5 pokrývá všech 16 kombinací C1–C4 bez překryvu), stavový diagram (Mermaid beze změny), hraniční hodnoty
9 999,99 / 10 000 / 500 000 / 500 000,01 / 2 000 000 / 2 000 000,01 (správná 2-hodnotová BVA při kroku 0,01),
TC-CL-007 a ukázkový defekt jsou konzistentní s pravidlem „nad 500 000 → druhé schválení“. SQL ukázky spuštěny:
první vrací limit 12 (REJECTED, approved 0), druhá podle textu na cvičné sadě neběží (sloupce TO-BE), což text uvádí.

| Místo | Bylo | Opraveno na | Proč (zdroj) |
|---|---|---|---|
| Quick, úrovně | „Unit testing“ bez ISTQB názvu | „Unit testing (ISTQB: component testing)“ | CTFL v4.0, kap. 2.2.1 |
| Deep dive, úrovně (pod tabulkou) | — | doplněno: v4.0 dělí integraci na component integration a system integration testing; akceptační testování zahrnuje i provozní, smluvní a regulatorní | CTFL v4.0, kap. 2.2.1 – pět úrovní testování |
| Quick + Deep dive, regrese | Regrese bez rozlišení od retestu | doplněno: confirmation testing (retest opravy) vs. regression testing, oboje change-related testing | CTFL v4.0, kap. 2.2.3 |
| Quick, state transition | „Draft → Submitted → Approved“ | „Draft → Submitted → In review → Approved“ | Vnitřní rozpor se stavovým diagramem (Submitted nemá přechod rovnou do Approved). |
| Třídy ekvivalence | „Invalid low < 10,000“ a zároveň „Invalid format: … negative“ | Invalid low zahrnuje 0 a záporná čísla; Invalid format = prázdné / není číslo | Třídy se nesmí překrývat (CTFL v4.0, kap. 4.2.1); záporné číslo patřilo do dvou tříd. |
| Hraniční hodnoty | Bez předpokladu přesnosti a bez rozlišení metod | doplněno: krok 0,01; seznam je 2-hodnotová BVA; vysvětlena 3-hodnotová BVA s příkladem | CTFL v4.0, kap. 4.2.2 |
| Rozhodovací tabulka – komentář | „what if the claim was late and above the limit?“ jako chybějící pravidlo | Tabulka je úplná; kombinaci řeší R3 („doesn't matter“) – otázka přeformulována na „je to záměr businessu?“ | Původní text tvrdil mezeru, která v tabulce není. |
| Defect lifecycle (nový odstavec) | Pojmy error/defect/failure nerozlišeny | doplněno: error → defect → failure; v UAT se pozorují selhání, statické testování nachází defekty přímo | CTFL v4.0, kap. 1.2.3 a glosář |
| Key terms – Defect | „a deviation of the system from an agreed requirement or expected behavior“ | nedostatek v pracovním produktu; při provedení může způsobit failure (viditelnou odchylku) | Původní definice popisovala spíš failure (glosář ISTQB). |
| SQL ukázka – komentář | „Did the approval store…“ u limitu 12 | „Did the decision store…“ | Limit 12 je v datové sadě REJECTED, ne schválený. |

Stylisticky bez zásahů.
