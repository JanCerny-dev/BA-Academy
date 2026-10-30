# Kontrola modulu 07 – Agile requirements: user stories, acceptance criteria and Jira

Modul je věcně v pořádku: Scrum Guide 2020 (3 accountabilities, Sprint ≤ 1 měsíc, artefakty a jejich commitments, definice DoD; Scrum Guide nezná BA, user stories ani story points), INVEST (Bill Wake), 3 C (Ron Jeffries), story mapping (Jeff Patton), syntaxe Gherkin včetně `Scenario Outline` / `Examples` a `<placeholder>`, JQL (`currentUser()`, `-14d`, `resolution = Unresolved`, `"Epic Link"` vs. `parent`). Opraveny dvě drobné věcné chyby a jedna nejednotnost.

| Místo | Bylo | Opraveno na | Proč (zdroj) |
|---|---|---|---|
| Quick version, Jira basics, ukázka JQL | `project = CLAIMS` | `project = CLM` | Vnitřní rozpor: Deep dive i cvičení m07-e3 používají klíč projektu `CLM` |
| Deep dive, Jira basics, Links | „blocks“, „relates to“, „is tested by“ jako běžné typy vazeb | „blocks“, „relates to“, „duplicates“; „is tested by“ přidávají aplikace pro test management (Xray, Zephyr) | Výchozí typy vazeb v Jira jsou Blocks, Clones, Duplicates, Relates; „is tested by“ ve standardní Jira není (dokumentace Atlassian k issue linking) |
| Deep dive, Gherkin, Background | „steps common to all scenarios in the file“ | „Given steps that run before every scenario of the feature“ | Background se spouští před každým scénářem dané Feature (nebo Rule) a nese kontext (Given); přesnější popis podle Gherkin reference (Cucumber) |

Bez stylistických změn.
