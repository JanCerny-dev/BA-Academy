# Kontrola modulu 10 – SQL for business analysts

Všech 49 bloků SQL (příklady v Deep dive i řešení úloh 1–15) spuštěno v Python sqlite3 (SQLite 3.49.1) proti
`data/sql/exportshield.sql`. Všechny uvedené počty řádků, součty, průměry a jména sedí (např. 31 nezaplacených
faktur, 80 řádků po joinu faktur s limity, 24 vs. 25 odběratelů, 39 rozhodnutí / průměr 12,5 dne / 18 nad 14 dní,
pásma rizik High 14 / Low 19 / Medium 5 = 38 z 39, podíly v řešení 15). Vysvětlení JOIN / NULL / GROUP BY /
HAVING / NOT IN s NULL jsou správně. Pořadí lekcí SQLBolt 1–12 odpovídá popisu.

Pozn. k ověření: blok s INSERT/UPDATE/DELETE (ukázka „read, don't run“) mění data. Kdo spustí příklady za sebou
na jednom spojení, dostane pak u řešení 14 navíc škodu 6 (smazaná platba 8). Text je v pořádku, jde jen o pořadí.

| Místo | Bylo | Opraveno na | Proč (zdroj) |
|---|---|---|---|
| Quick version, pod tvarem dotazu | „Only `SELECT` and `FROM` are required.“ | Ke čtení tabulky stačí `SELECT` a `FROM`, ostatní klauzule jsou volitelné. | `FROM` není povinné obecně (`SELECT 1` je platný dotaz); původní věta byla nepřesná. |
| Deep dive, Setup | Textové hodnoty jsou case-sensitive „in most comparisons“ | Case-sensitive v SQLite a PostgreSQL; SQL Server a MySQL obvykle porovnávají bez ohledu na velikost písmen podle collation | Výchozí collation SQL Serveru (`…_CI_AS`) a MySQL (`utf8mb4_0900_ai_ci`) jsou case-insensitive. |
| Deep dive, IN | „Look at row 6“ | „Look at the limit with id 6“ | Ve výsledku je to 4. řádek, id je 6; původní text mátl. |
| Deep dive, GROUP BY | SQLite vrací „arbitrary value; other databases raise an error“ | hodnotu z libovolného řádku skupiny; „most other databases (… MySQL in its default mode)“ | MySQL bez `ONLY_FULL_GROUP_BY` je také benevolentní; tvrzení o „ostatních“ bylo příliš absolutní. |

Stylisticky bez zásahů.
