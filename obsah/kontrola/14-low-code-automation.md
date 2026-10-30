# Kontrola modulu 14 – Low-code automation and algorithmic thinking

Modul je věcně v pořádku. Ověřeno (30. 10. 2026):
- Power Apps Developer Plan (Microsoft Learn, stránka „Power Apps Developer Plan“, aktualizace 26. 10. 2026): jen pracovní/školní účet s Microsoft Entra ID; obsahuje cloud flows, ne RPA (desktop flows); od 15. 11. 2026 registrace nevytváří developer environment, unmanaged developer environments se pozastavují od 15. 12. 2026 a mažou od 15. 1. 2027. Text sedí.
- Power Automate for desktop zdarma ve Windows 10/11 pro attended použití; unattended a spouštění z cloudu vyžaduje placenou licenci. Sedí.
- Standard vs premium konektory (HTTP, SQL Server, Dataverse premium), DLP skupiny business / non-business / blocked. Sedí.
- Make free plán: 1 000 credits měsíčně, omezený počet aktivních scénářů (2), minimální interval 15 min (make.com/pricing a recenze 9/2026). Text je formulovaný obecně („around“), ponecháno.
- ARES API: `GET .../ekonomicke-subjekty/00006947` vrací 200 a `obchodniJmeno` „Ministerstvo financí“; `12345678` vrací 404 (`NENALEZENO`); neplatný formát (např. `123`) vrací 400. Cvičení m14-e2 tedy funguje, jak je popsáno.
- Výpočet úspory: 40 × 11 min × 48 týdnů = 21 120 min = 352 h. Sedí.
- Pravidla 500 000 EUR a 60 dní po splatnosti sedí s moduly 07 a 13.

| Místo | Bylo | Opraveno na | Proč (zdroj) |
|---|---|---|---|
| Deep dive, Flow design table, krok 1 | Outlook "When a new email arrives" (shared mailbox) | Outlook "When a new email arrives in a shared mailbox (V2)" | Pro sdílenou schránku má konektor Office 365 Outlook samostatný trigger s tímto názvem; běžný trigger sleduje jen vlastní schránku. |
