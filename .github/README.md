# BA Academy

Self-study path from zero to **IT Business Analyst** – in English and Czech (EN | CZ switch).

**Website:** https://jancerny-dev.github.io/BA-Academy/

- 17 modules (quick version + deep dive, priorities P1–P3), hands-on exercises, self-check and interview questions
- Capstone project on a fictional export credit insurer (ExportShield Insurance) that becomes an interview portfolio
- SQL lab (SQLite in the browser) and API lab (live calls to the Czech ARES register)
- Curated Udemy courses, free videos, tools, certificates and example job ads
- Progress tracking in the browser, optional Google sign-in to sync it across devices

All explanations are original. Courses and videos are only linked; no third-party content is copied.
All company names, people and data in the exercises are fictional.

## Build

```bash
python tools/build.py
```

Standard library only. Sources: `obsah/` (English modules), `obsah/cs/` (Czech), `data/` (resources, dataset).
Output: `web/` (English) and `web/cs/` (Czech). GitHub Actions publishes `web/` to GitHub Pages.
