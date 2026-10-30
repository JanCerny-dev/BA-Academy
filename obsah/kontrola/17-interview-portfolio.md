# Kontrola modulu 17 – Interview preparation and portfolio

Modul je věcně v pořádku; žádná vymyšlená čísla o platech (jen postup, jak rozsah zjistit). Rady k pohovoru (STAR, case method, formáty) odpovídají běžné praxi.

| Místo | Bylo | Opraveno na | Proč (zdroj) |
|---|---|---|---|
| Interview corner, SQL otázka | „a WHERE filter on unpaid status“ | „a WHERE filter for unpaid invoices (for example `paid_date IS NULL`)“ | Tabulka `invoices` v datové sadě nemá sloupec status; nezaplacená faktura = `paid_date IS NULL` (schéma `exportshield.sql`). |
| Tamtéž | jen zmínka o LEFT JOIN | doplněna odrážka: částky v různých měnách nelze prostě sečíst (GROUP BY i podle měny, nebo převést) | Faktury v datové sadě jsou v EUR a USD; modul 10 na to sám upozorňuje. |
| CV, tabulka Weak/Strong | ≈300 hours/year | ≈350 hours/year | Soulad s výpočtem v modulu 14 (40 × 11 min × 48 týdnů ≈ 352 h, úspora ~73 %). |
