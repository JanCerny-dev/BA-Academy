# Kontrola modulu 04 – Process modeling with BPMN 2.0

Ověřeno proti BPMN 2.0.2 (OMG, 2013; ISO/IEC 19510:2013): okraje událostí (start tenký, intermediate dvojitý,
end tlustý), throwing = plná ikona / catching = obrysová, ikony událostí (message, timer, error, signal, escalation,
conditional, terminate), typy úloh a jejich ikony, markery (loop, parallel / sequential multi-instance), call activity
s tlustým okrajem, sémantika bran (XOR join nečeká, AND join čeká na všechny, OR join čeká jen na aktivované větve,
event-based brána), default flow s lomítkem, boundary events (interrupting plná dvojitá čára, non-interrupting
čárkovaná), sequence flow jen uvnitř poolu a message flow jen mezi pooly, DMN hit policy Unique/First.

| Místo | Bylo | Opraveno na | Proč (zdroj) |
|---|---|---|---|
| Quick version, odrážka Flows | message flow = „dashed arrow with an open envelope start“ | čárkovaná čára s malým prázdným kolečkem na začátku a prázdnou šipkou | BPMN 2.0.2, kap. 9 Collaboration – Message Flow: kolečko na začátku, nevyplněná šipka. Obálka je volitelný symbol zprávy, ne začátek spojnice. Deep dive to měl správně, Quick si odporoval. |
| Deep dive, TO-BE krok 4 + Mermaid TO-BE | Cesta z error boundary eventu („Verify buyer manually“) vedla přímo do paralelního joinu, který tak měl 3 vstupy | Ruční ověření a běžná cesta ARES se nejdřív spojí exkluzivní bránou (merge), teprve pak jdou do paralelního joinu | Paralelní join čeká na token ze všech příchozích sekvenčních toků (BPMN 2.0.2, kap. 13 Execution Semantics – Parallel Gateway). Při chybě ARES dorazí token jen z „Verify buyer manually“, při úspěchu jen z ARES – join se třemi vstupy by nikdy nepokračoval (deadlock). |
| Mermaid TO-BE | Větev „Notify head of underwriting“ končila bez koncové události | Přidána koncová událost „Head notified“ | Vlastní pravidlo modulu („every path ends in an end event“) a cvičení m04-e2, krok 6. |
| Hands-on m04-e2, krok 5 | „…which rejoins the flow.“ | Spojit s běžnou cestou exkluzivní bránou před paralelním joinem, s vysvětlením proč | Stejný důvod jako výše; původní zadání vedlo k chybnému modelu. |
| Deep dive, tabulka událostí, Escalation | „without stopping the work“ | „unlike an error, the work can continue“ | Eskalační boundary event může být interrupting i non-interrupting (BPMN 2.0.2, kap. 10 Process – Events, boundary events); „vždy bez přerušení“ neplatí. Odstavec níže už správně říká „may continue“. |
| Interview corner, otázka 3 (inclusive) | Příklad „request extra documents for each missing type“ (zní jako multi-instance) | Konkrétní příklad inclusive brány: faktura a/nebo doklad o dodání podle toho, co chybí; join čeká jen na spuštěné větve | Upřesnění, aby příklad nesplýval s multi-instance aktivitou. |
