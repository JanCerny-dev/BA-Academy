# -*- coding: utf-8 -*-
"""Generátor webu BA Academy (NAT-Academy). Jen standardní knihovna Pythonu.

    python tools/build.py

Čte obsah/moduly/*.md (anglicky), obsah/cs/moduly/*.md (česky), obsah/projekt.md, obsah/cs/projekt.md
a data/*.json (česká pole s příponou _cs). Zapisuje anglický web do web/ a český do web/cs/.
Oba jazyky sdílí assets/ a klíče postupu v localStorage (nat-*), takže odškrtnuté věci platí v obou.
Po přihlášení Google účtem se postup ukládá i do Firestore (assets/ucet.js, kolekce uzivatele-nat).
"""

from __future__ import annotations

import html
import json
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import markdown_ba  # noqa: E402
from markdown_ba import Prevod, frontmatter, inline, sekce, slova  # noqa: E402

KOREN = Path(__file__).resolve().parent.parent
OBSAH = KOREN / "obsah"
DATA = KOREN / "data"
WEB = KOREN / "web"
ASSETS = Path(__file__).parent / "assets"

NAZEV = "BA Academy"
MERMAID = "https://cdnjs.cloudflare.com/ajax/libs/mermaid/10.9.1/mermaid.min.js"

JAZYK = "en"   # nastavuje main() pro každý průchod


def L(en: str, cs: str) -> str:
    """Text podle jazyka právě generované verze."""
    return cs if JAZYK == "cs" else en


def D(obj: dict, pole: str) -> str:
    """Pole z dat; v české verzi pole_cs, pokud existuje."""
    if JAZYK == "cs" and obj.get(pole + "_cs"):
        return obj[pole + "_cs"]
    return obj.get(pole, "")


FAZE = {
    "A": (("Orientation", "Orientace"), ("What the job is and how IT delivery works.", "Co ta práce obnáší a jak běží IT projekty.")),
    "B": (("Core BA craft", "Jádro řemesla BA"), ("Problems, processes, requirements and models – the heart of the job.",
                                               "Problémy, procesy, požadavky a modely – jádro práce.")),
    "C": (("Technical literacy", "Technická gramotnost"), ("Data, SQL, APIs and architecture – enough to talk to developers and vendors.",
                                                        "Data, SQL, API a architektura – tolik, abys mluvila s vývojáři a dodavateli.")),
    "D": (("Delivery & automation", "Dodávka a automatizace"), ("Testing, low-code automation and AI in real processes.",
                                                              "Testování, low-code automatizace a AI ve skutečných procesech.")),
    "E": (("People & career", "Lidé a kariéra"), ("Stakeholders, presenting, and getting the job.",
                                                 "Stakeholdeři, prezentace a jak získat práci.")),
}


def faze(f: str) -> tuple[str, str]:
    (n_en, n_cs), (p_en, p_cs) = FAZE[f]
    return L(n_en, n_cs), L(p_en, p_cs)


PRIORITY = {
    "P1": (("Must know", "Nutné znát"), ("The ad asks for it directly, or interviewers almost always test it.",
                                         "Inzerát to chce přímo, nebo se na to na pohovoru skoro jistě zeptají.")),
    "P2": (("Should know", "Dobré znát"), ("Everyday part of the job; a plus at the interview.",
                                           "Běžná součást práce, na pohovoru plus.")),
    "P3": (("Nice to have", "Navíc"), ("Depth that sets you apart from other juniors.",
                                       "Hloubka, která tě odliší od ostatních juniorů.")),
}

# Doslovné citace z cílového inzerátu (EMNT, IT Business Analyst, 9/2026). V obou jazycích česky (originál).
INZERAT = {
    "01": "Nehledáme pouze pasivního zapisovatele požadavků. Hledáme proaktivního partnera…",
    "02": "Úzce spolupracovat s IT dodavateli a stakeholdery napříč společností",
    "03": "Proaktivní přístup k řešení problémů a hledání cest k optimalizaci",
    "04": "Orientujete se v UML nebo BPMN pro modelování a vizualizaci procesů",
    "05": "Přijímat požadavky na úpravy systémů od interních oddělení",
    "06": "…a tvořit technické specifikace pro dodavatele",
    "07": "Máte zkušenost s algoritmizací byznys požadavků (např. programování, low-code nebo tvorba technických zadání)",
    "08": "Orientujete se v UML nebo BPMN pro modelování a vizualizaci procesů",
    "09": "Disponujete základní znalostí SQL, prací s API a formáty JSON/XML",
    "10": "Disponujete základní znalostí SQL, prací s API a formáty JSON/XML",
    "11": "Disponujete základní znalostí SQL, prací s API a formáty JSON/XML",
    "12": "Navrhovat nové funkce a optimalizovat stávající části systémů v souladu s architekturou",
    "13": "Podporovat testery, účastnit se testování dodávek a reportovat stav vývoje",
    "14": "Realizovat automatizace v low-code platformách a zkoumat potenciál nových technologií pro byznys",
    "15": "Podílet se na projektech integrace umělé inteligence do vnitrofiremních procesů",
    "16": "Prezentovat výstupy kolegům a připravovat pro ně odborná školení",
}


def minuty(slov: int, rychlost: int) -> int:
    """Čas studia z počtu slov, zaokrouhleno na 5 min."""
    return max(5, int(round(slov / rychlost / 5.0)) * 5)


def esc(t) -> str:
    return html.escape(str(t), quote=True)


def nacti_json(nazev: str, klic: str) -> list:
    p = DATA / nazev
    if not p.exists():
        return []
    return json.loads(p.read_text(encoding="utf-8")).get(klic, [])


# ---------------------------------------------------------------- moduly

def nacti_modul(p: Path) -> dict:
    meta, telo = frontmatter(p.read_text(encoding="utf-8"))
    cast = sekce(telo)
    nid = str(meta.get("id", p.stem[:2])).zfill(2)
    prevod = Prevod(predpona_kotvy=f"m{nid}-")
    html_sekci = {k: prevod.html(v) for k, v in cast.items() if k != "_uvod"}
    pojmy = []
    for r in cast.get("Key terms", "").split("\n"):
        r = r.strip()
        if r.startswith(("- ", "* ")) and "**" in r:
            t = r[2:]
            try:
                term = t.split("**")[1]
                definice = t.split("**", 2)[2].lstrip(" —–-:").strip()
            except IndexError:
                continue
            pojmy.append({"term": term, "def": definice, "modul": nid})
    return {
        "id": nid, "slug": meta.get("slug", p.stem[3:]), "title": meta.get("title", p.stem),
        "phase": meta.get("phase", "B"), "priority": meta.get("priority", "P2"),
        "job_ad": INZERAT.get(nid, ""), "sekce": html_sekci, "pojmy": pojmy,
        "cviceni": prevod.cviceni, "otazky": prevod.otazky, "pohovor": prevod.pohovor,
        "mermaid": prevod.mermaid, "nadpisy": prevod.nadpisy,
        "slova_quick": slova(cast.get("Quick version", "")), "slova_deep": slova(cast.get("Deep dive", "")),
        "soubor": p.name, "prelozeno": True,
    }


def nacti_moduly(jazyk: str) -> list[dict]:
    """Moduly v daném jazyce; chybějící český překlad nahradí anglický originál (s poznámkou)."""
    moduly = []
    for p in sorted((OBSAH / "moduly").glob("*.md")):
        cs = OBSAH / "cs" / "moduly" / p.name
        if jazyk == "cs" and cs.exists():
            m = nacti_modul(cs)
        else:
            m = nacti_modul(p)
            m["prelozeno"] = jazyk == "en"
        # časy z počtu slov anglické verze, aby byly v obou jazycích stejné
        en = nacti_modul(p) if jazyk == "cs" and cs.exists() else m
        m["quick_min"] = minuty(en["slova_quick"], 120)
        m["deep_min"] = minuty(en["slova_deep"], 60)
        moduly.append(m)
    return moduly


def nacti_projekt(jazyk: str) -> dict | None:
    pp = OBSAH / "projekt.md"
    if jazyk == "cs" and (OBSAH / "cs" / "projekt.md").exists():
        pp = OBSAH / "cs" / "projekt.md"
    if not pp.exists():
        return None
    meta, telo = frontmatter(pp.read_text(encoding="utf-8"))
    pr = Prevod(predpona_kotvy="p-")
    cast = sekce(telo)
    return {"title": meta.get("title", "Capstone project"),
            "sekce": {k: pr.html(v) for k, v in cast.items() if v.strip()},
            "cviceni": pr.cviceni, "mermaid": pr.mermaid}


# ---------------------------------------------------------------- šablona

def nav() -> list[tuple[str, str]]:
    return [
        ("index.html", L("Home", "Úvod")), ("path.html", L("Learning path", "Studijní cesta")),
        ("modules.html", L("Modules", "Moduly")), ("project.html", "Capstone"),
        ("courses.html", "Udemy"), ("videos.html", L("Videos", "Videa")), ("tools.html", L("Tools", "Nástroje")),
        ("sql.html", "SQL lab"), ("api.html", "API lab"), ("glossary.html", L("Glossary", "Slovník")),
        ("interview.html", L("Interview", "Pohovor")), ("certifications.html", L("Certificates", "Certifikace")),
        ("jobs.html", L("Jobs", "Pozice")),
    ]


def stranka(nazev: str, telo: str, aktivni: str, soubor: str, mermaid: bool = False,
            skripty: list[str] | None = None, popis: str = "") -> str:
    """soubor = cesta stránky relativně ke kořeni jazykové verze (např. m/04.html)."""
    hloubka = soubor.count("/")
    k = "../" * hloubka                                  # ke kořeni jazykové verze
    koren = "../" * (hloubka + (1 if JAZYK == "cs" else 0))   # ke kořeni webu (assets)
    jinde = koren + soubor if JAZYK == "cs" else koren + "cs/" + soubor
    prepinac = (f'<nav class="jazyk" aria-label="Language / Jazyk">'
                f'<a href="{jinde if JAZYK == "cs" else "#"}" lang="en"{" aria-current=\"true\"" if JAZYK == "en" else ""} data-jazyk="en">EN</a>'
                f'<a href="{jinde if JAZYK == "en" else "#"}" lang="cs"{" aria-current=\"true\"" if JAZYK == "cs" else ""} data-jazyk="cs">CZ</a></nav>')
    menu = "".join(
        f'<a href="{k}{h}"{" aria-current=\"page\"" if h == aktivni else ""}>{esc(t)}</a>' for h, t in nav())
    extra = ""
    if mermaid:
        extra += (f'<script src="{MERMAID}"></script>'
                  '<script>mermaid.initialize({startOnLoad:false,theme:'
                  '(matchMedia("(prefers-color-scheme: dark)").matches?"dark":"neutral"),securityLevel:"strict"});'
                  # diagramy ve skrytých záložkách vykreslí až app.js při přepnutí (jinak mají nulovou šířku)
                  'mermaid.run({nodes:[].filter.call(document.querySelectorAll(".mermaid"),function(e){return e.offsetParent!==null;})});'
                  '</script>')
    for s in skripty or []:
        extra += f'<script src="{s if s.startswith("http") else koren + s}"></script>'
    return f"""<!doctype html>
<html lang="{JAZYK}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(nazev)} · {NAZEV}</title>
<meta name="description" content="{esc(popis or L('Self-study path from zero to IT Business Analyst.', 'Samostudium od nuly k pozici IT Business Analyst.'))}">
<link rel="stylesheet" href="{koren}assets/styl.css">
<link rel="alternate" hreflang="{'en' if JAZYK == 'cs' else 'cs'}" href="{jinde}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%230f766e'/%3E%3Ctext x='16' y='22' font-family='Arial' font-size='15' font-weight='700' fill='white' text-anchor='middle'%3EBA%3C/text%3E%3C/svg%3E">
</head>
<body>
<a class="preskocit" href="#obsah">{L('Skip to content', 'Přeskočit na obsah')}</a>
<header class="hlavicka">
  <div class="hlavicka-radek">
    <a class="logo" href="{k}index.html"><span class="logo-znak">BA</span> {NAZEV}</a>
    <div class="hlavicka-akce">
      <span class="celkem" data-celkovy-postup title="{L('Overall progress', 'Celkový postup')}"></span>
      {prepinac}
      <button type="button" class="tlacitko ucet-tlacitko" data-ucet hidden>{L('Sign in', 'Přihlásit')}</button>
      <button type="button" class="tlacitko menu-tlacitko" aria-expanded="false" aria-controls="hlavni-menu">Menu</button>
    </div>
  </div>
  <nav class="menu" id="hlavni-menu" aria-label="{L('Main', 'Hlavní')}">{menu}</nav>
</header>
<main id="obsah">
{telo}
</main>
<footer class="paticka">
  <p>{NAZEV} · {L('self-study path to IT Business Analyst · progress is saved in this browser',
                  'samostudium k pozici IT Business Analyst · postup se ukládá v tomto prohlížeči')}
  <span data-ucet-info hidden>{L('and, after signing in with Google, in your account', 'a po přihlášení Googlem i v účtu')}</span>.</p>
  <p class="pozn">{L('Udemy and YouTube links lead to external sites. Course content is not copied here; all explanations are original.',
                     'Odkazy na Udemy a YouTube vedou na cizí weby. Obsah kurzů se sem nekopíruje, všechny výklady jsou vlastní.')}</p>
</footer>
<script src="{koren}assets/ucet-konfig.js"></script>
<script src="{koren}assets/ucet.js"></script>
<script src="{koren}assets/app.js"></script>
{extra}
</body>
</html>
"""


def fajfka(klic: str, text: str = "", trida: str = "") -> str:
    t = f" <span>{text}</span>" if text else ""
    return f'<label class="fajfka {trida}"><input type="checkbox" data-key="{esc(klic)}">{t}</label>'


def postup(klice: list[str], text: str = "", velky: bool = False) -> str:
    return (f'<div class="postup{" postup-velky" if velky else ""}" data-keys="{esc(" ".join(klice))}">'
            f'<div class="postup-pruh"><span></span></div><span class="postup-text">{esc(text)}</span></div>')


def prio(p: str) -> str:
    if p not in PRIORITY:
        return ""
    (n_en, n_cs), (t_en, t_cs) = PRIORITY[p]
    return f'<span class="prio prio-{p.lower()}" title="{esc(L(t_en, t_cs))}">{p} · {L(n_en, n_cs)}</span>'


def klice_modulu(m: dict, kurzy: list, videa: list) -> list[str]:
    k = [f"nat-read-{m['id']}-quick", f"nat-read-{m['id']}-deep"]
    k += [f"nat-ex-{c['id']}" for c in m["cviceni"]]
    k += [f"nat-u-{c['slug']}" for c in kurzy if c["tier"] == "core" and c["modules"][0] == m["id"]]
    k += [f"nat-v-{v['id']}" for v in videa if v.get("modules") and v["modules"][0] == m["id"]]
    return k


def pozn_preklad(m: dict) -> str:
    if m.get("prelozeno", True):
        return ""
    return ('<aside class="box box-note"><strong class="box-nadpis">Překlad se připravuje</strong>'
            '<p>Tento modul je zatím jen v angličtině.</p></aside>')


# ---------------------------------------------------------------- karty zdrojů

def karta_kurzu(c: dict, base: str) -> str:
    stitek = (f'<span class="stitek stitek-core">{L("Core", "Hlavní")}</span>' if c["tier"] == "core"
              else f'<span class="stitek">{L("Optional", "Volitelný")}</span>')
    hodnoceni = L(f"({c['reviews']:,} ratings)", f"({c['reviews']:,} hodnocení)".replace(",", " "))
    aktual = L("updated", "aktualizace")
    return (f'<li class="zdroj">{fajfka("nat-u-" + c["slug"])}<div><a href="{esc(base + c["slug"] + "/")}" target="_blank" rel="noopener">'
            f'{esc(c["title"])}</a> {stitek}<div class="meta">{esc(c["author"])} · {str(c["hours"]).replace(".", L(".", ","))} h · ★ '
            f'{L(f"{c["rating"]:.1f}", f"{c["rating"]:.1f}".replace(".", ","))} {hodnoceni} · {aktual} {esc(c["updated"])}</div>'
            f'<p>{esc(D(c, "why"))}</p></div></li>')


def karta_videa(v: dict) -> str:
    delka = f' · {esc(v["min"])} min' if v.get("min") else ""
    uroven = f' · {esc(D(v, "level"))}' if v.get("level") else ""
    return (f'<li class="zdroj">{fajfka("nat-v-" + v["id"])}<div><a href="{esc(v["url"])}" target="_blank" rel="noopener">'
            f'{esc(v["title"])}</a><div class="meta">{esc(v.get("channel", ""))}{delka}{uroven}</div>'
            f'<p>{esc(D(v, "why"))}</p></div></li>')


def karta_nastroje(t: dict, koren_jazyka: str = "") -> str:
    url = t["url"] if t["url"].startswith("http") else koren_jazyka + t["url"]
    return (f'<li class="zdroj">{fajfka("nat-t-" + t["id"])}<div><a href="{esc(url)}"'
            f'{" target=\"_blank\" rel=\"noopener\"" if url.startswith("http") else ""}>'
            f'{esc(t["name"])}</a> <span class="stitek">{esc(D(t, "free"))}</span>'
            f'<p>{esc(D(t, "what"))}</p></div></li>')


def karta_cteni(r: dict, s_fajfkou: bool) -> str:
    f = fajfka("nat-r-" + r["id"]) if s_fajfkou else ""
    return (f'<li class="zdroj{"" if s_fajfkou else " zdroj-bez"}">{f}<div><a href="{esc(r["url"])}" target="_blank" rel="noopener">'
            f'{esc(D(r, "title"))}</a><p>{esc(D(r, "what"))}</p></div></li>')


# ---------------------------------------------------------------- stránky

def str_modul(m: dict, kurzy: list, base: str, videa: list, nastroje: list, cteni: list, vsechny: list) -> str:
    nid = m["id"]
    s = m["sekce"]
    nazev_faze = faze(m["phase"])[0] if m["phase"] in FAZE else ""
    idx = [x["id"] for x in vsechny].index(nid)
    pred = vsechny[idx - 1] if idx > 0 else None
    dalsi = vsechny[idx + 1] if idx + 1 < len(vsechny) else None

    kz = [c for c in kurzy if nid in c["modules"]]
    kz.sort(key=lambda c: (c["tier"] != "core", c["modules"].index(nid)))
    vz = [v for v in videa if nid in v.get("modules", [])]
    nz = [t for t in nastroje if nid in t.get("modules", [])]
    cz = [r for r in cteni if nid in r.get("modules", [])]

    zdroje = ""
    if kz:
        zdroje += "<h3>Udemy</h3><ul class='zdroje'>" + "".join(karta_kurzu(c, base) for c in kz) + "</ul>"
    if vz:
        zdroje += f"<h3>{L('Videos (free)', 'Videa (zdarma)')}</h3><ul class='zdroje'>" + "".join(karta_videa(v) for v in vz) + "</ul>"
    if nz:
        zdroje += f"<h3>{L('Tools to try', 'Nástroje k vyzkoušení')}</h3><ul class='zdroje'>" + "".join(karta_nastroje(t, "../") for t in nz) + "</ul>"
    if cz:
        zdroje += f"<h3>{L('Reading (free)', 'Ke čtení (zdarma)')}</h3><ul class='zdroje'>" + "".join(karta_cteni(r, False) for r in cz) + "</ul>"
    if not zdroje:
        zdroje = f"<p>{L('No extra resources for this module.', 'K tomuto modulu nejsou další zdroje.')}</p>"

    pojmy = ""
    if m["pojmy"]:
        pojmy = f"<h2 id='m{nid}-key-terms'>{L('Key terms', 'Klíčové pojmy')}</h2><dl class='pojmy'>" + "".join(
            f"<dt>{esc(p['term'])}</dt><dd>{inline(p['def'])}</dd>" for p in m["pojmy"]) + "</dl>"

    obsah_deep = "".join(
        f'<li class="u{u}"><a href="#{k}">{esc(t)}</a>{" <span class=prio-mini>" + p + "</span>" if p else ""}</li>'
        for u, t, k, p in m["nadpisy"] if k.startswith(f"m{nid}-") and u == 3)

    zalozky = [
        ("quick", f"{L('Quick version', 'Krátká verze')} · {m['quick_min']} min",
         s.get("Quick version", "") + pojmy +
         f'<div class="hotovo">{fajfka(f"nat-read-{nid}-quick", L("I have read the quick version", "Krátkou verzi mám přečtenou"))}</div>'),
        ("deep", f"{L('Deep dive', 'Do hloubky')} · {m['deep_min']} min",
         (f'<nav class="obsah-deep" aria-label="{L("Deep dive contents", "Obsah")}"><strong>{L("In this deep dive", "V této části")}</strong><ul>{obsah_deep}</ul></nav>' if obsah_deep else "")
         + s.get("Deep dive", "") +
         f'<div class="hotovo">{fajfka(f"nat-read-{nid}-deep", L("I have worked through the deep dive", "Část do hloubky mám prostudovanou"))}</div>'),
        ("practice", f"{L('Hands-on', 'Prakticky')} · {len(m['cviceni'])}", s.get("Hands-on", "")),
        ("check", f"{L('Self-check', 'Ověř se')} · {len(m['otazky'])}", s.get("Self-check", "")),
        ("interview", f"{L('Interview', 'Pohovor')} · {len(m['pohovor'])}", s.get("Interview corner", "")),
        ("resources", f"{L('Resources', 'Zdroje')} · {len(kz) + len(vz) + len(nz)}", zdroje),
    ]
    tlacitka = "".join(
        f'<button type="button" role="tab" id="tab-{k}" aria-controls="panel-{k}" aria-selected="{"true" if i == 0 else "false"}">{esc(t)}</button>'
        for i, (k, t, _) in enumerate(zalozky))
    panely = "".join(
        f'<section role="tabpanel" id="panel-{k}" aria-labelledby="tab-{k}" class="panel"{"" if i == 0 else " hidden"}>{obs}</section>'
        for i, (k, _, obs) in enumerate(zalozky))

    inzerat = (f'<p class="inzerat"><span>{L("In the target job ad (original Czech wording)", "V cílovém inzerátu")}</span> “{esc(m["job_ad"])}”</p>'
               if m["job_ad"] else "")
    navigace = f'<nav class="dalsi" aria-label="{L("Module navigation", "Navigace mezi moduly")}">'
    navigace += f'<a href="{pred["id"]}.html">← {pred["id"]} {esc(pred["title"])}</a>' if pred else "<span></span>"
    navigace += f'<a href="{dalsi["id"]}.html">{dalsi["id"]} {esc(dalsi["title"])} →</a>' if dalsi else "<span></span>"
    navigace += "</nav>"

    telo = f"""
<div class="modul-hlava">
  <p class="drobky"><a href="../modules.html">{L('Modules', 'Moduly')}</a> · {L('Phase', 'Fáze')} {esc(m['phase'])}: {esc(nazev_faze)}</p>
  <h1><span class="cislo">{nid}</span> {esc(m['title'])}</h1>
  <p class="odznaky">{prio(m['priority'])}<span class="stitek">{L('Quick', 'Krátká')} {m['quick_min']} min</span><span class="stitek">{L('Deep', 'Hloubka')} {m['deep_min']} min</span></p>
  {pozn_preklad(m)}
  {inzerat}
  <div class="proc">{s.get('Why this matters', '')}</div>
  {postup(klice_modulu(m, kurzy, videa), L('module progress', 'postup v modulu'))}
</div>
<div class="zalozky" data-zalozky="m{nid}">
  <div class="zalozky-lista" role="tablist">{tlacitka}</div>
  {panely}
</div>
{navigace}
"""
    # relativní odkazy z obsahu (sql.html, api.html) míří do kořene jazykové verze, modul je o úroveň níž
    telo = re.sub(r'href="(?!https?:|#|\.\./|mailto:|\d\d\.html)([\w-]+\.html[^"]*)"', r'href="../\1"', telo)
    return stranka(f"{nid} {m['title']}", telo, "modules.html", f"m/{nid}.html", mermaid=m["mermaid"],
                   popis=f"{L('Module', 'Modul')} {nid}: {m['title']}")


def str_index(moduly: list, kurzy: list, videa: list, projekt: dict | None) -> str:
    vse = []
    karty = ""
    for f in FAZE:
        mm = [m for m in moduly if m["phase"] == f]
        if not mm:
            continue
        nazev, popis = faze(f)
        polozky = ""
        for m in mm:
            k = klice_modulu(m, kurzy, videa)
            vse += k
            polozky += (f'<li><a href="m/{m["id"]}.html"><span class="cislo">{m["id"]}</span> {esc(m["title"])}</a>'
                        f'{prio(m["priority"])}{postup(k)}</li>')
        karty += f'<section class="faze"><h3><span class="faze-pismeno">{f}</span> {esc(nazev)}</h3><p>{esc(popis)}</p><ul class="moduly-seznam">{polozky}</ul></section>'
    if projekt:
        vse += [f"nat-ex-{c['id']}" for c in projekt["cviceni"]]
    min_quick = sum(m["quick_min"] for m in moduly)
    min_deep = sum(m["deep_min"] for m in moduly)
    hod_core = sum(c["hours"] for c in kurzy if c["tier"] == "core")
    pocet_cv = sum(len(m["cviceni"]) for m in moduly)
    telo = f"""
<section class="uvod">
  <p class="nadtitul">{L('Self-study path', 'Samostudium')}</p>
  <h1>{L('From process improver to IT Business Analyst', 'Od zlepšování procesů k IT Business Analystovi')}</h1>
  <p class="perex">{L('''You already spot processes that could run better, push automation through IT, get it approved and test it.
  That is a large part of business analysis, done by instinct. This path adds the names, methods and tools behind it,
  so you can walk into an interview, talk about the work with confidence and show things you have actually built.''',
  '''Už teď vidíš procesy, které by mohly běžet lépe, protlačíš automatizaci přes IT, necháš ji schválit a otestuješ ji.
  To je velká část business analýzy, jen dělaná intuitivně. Tahle cesta k tomu přidá pojmy, metody a nástroje,
  abys mohla přijít na pohovor, s jistotou o práci mluvit a ukázat věci, které jsi skutečně postavila.''')}</p>
  {postup(vse, L('overall progress', 'celkový postup'), velky=True)}
  <div class="volby">
    <a class="karta-volba" href="path.html#essentials"><strong>{L('Essentials route', 'Zkrácená cesta (Essentials)')}</strong><span>{L(
      '~10–12 weeks · quick versions of everything, deep dives where the ad is explicit, core courses, a lighter capstone.',
      '~10–12 týdnů · krátké verze všeho, do hloubky jen tam, kde to inzerát přímo chce, hlavní kurzy, lehčí capstone.')}</span></a>
    <a class="karta-volba" href="path.html#full"><strong>{L('Full route', 'Plná cesta')}</strong><span>{L(
      '~24 weeks at 8–10 h/week · every module in depth, all core courses, the full capstone portfolio.',
      '~24 týdnů po 8–10 h · všechny moduly do hloubky, všechny hlavní kurzy, celé portfolio z capstonu.')}</span></a>
  </div>
</section>
<section>
  <h2>{L('How it works', 'Jak to funguje')}</h2>
  <ol class="jak">
    <li>{L('<strong>Read</strong> each module in the <em>Quick version</em> (what it is, how to explain it) or the <em>Deep dive</em> (the full theory). Priorities P1–P3 tell you what matters most.',
           '<strong>Čti</strong> každý modul v <em>krátké verzi</em> (co to je a jak to vysvětlit) nebo <em>do hloubky</em> (celá teorie). Priority P1–P3 říkají, na čem záleží nejvíc.')}</li>
    <li>{L('<strong>Watch</strong> the matching Udemy course or free videos. Tick them off as you go.',
           '<strong>Sleduj</strong> odpovídající kurz na Udemy nebo videa zdarma. Průběžně je odškrtávej.')}</li>
    <li>{L('<strong>Do</strong> the hands-on exercises in free tools – BPMN, SQL, APIs, Jira, automation.',
           '<strong>Dělej</strong> praktická cvičení v nástrojích zdarma – BPMN, SQL, API, Jira, automatizace.')}</li>
    <li>{L('<strong>Build</strong> the capstone: one fictional company, ExportShield Insurance, carried from problem to automation. It becomes your interview portfolio.',
           '<strong>Postav</strong> capstone: jedna fiktivní firma, ExportShield Insurance, od problému až po automatizaci. Z toho vznikne portfolio na pohovor.')}</li>
    <li>{L('<strong>Practise</strong> the interview questions until you can answer them out loud.',
           '<strong>Trénuj</strong> pohovorové otázky, dokud je neumíš odpovědět nahlas.')}</li>
  </ol>
  <p class="cisla">{len(moduly)} {L('modules', 'modulů')} · ~{round(min_quick / 60)} h {L('quick reading', 'krátkých verzí')} · ~{round(min_deep / 60)} h {L('deep dives', 'výkladu do hloubky')} · {pocet_cv} {L('exercises', 'cvičení')} · {hod_core:.0f} h {L('of core Udemy courses', 'hlavních kurzů Udemy')}</p>
  <p class="pozn-ucet" data-ucet-info hidden>{L('Sign in with Google (top right) to keep your progress across devices.', 'Přihlas se Googlem (vpravo nahoře) a postup budeš mít na všech zařízeních.')}</p>
</section>
<section>
  <h2>{L('Modules by phase', 'Moduly podle fází')}</h2>
  <div class="faze-mrizka">{karty}</div>
</section>
<section>
  <h2>{L('Priorities', 'Priority')}</h2>
  <ul class="priority">{''.join(f'<li>{prio(p)} {esc(L(*v[1]))}</li>' for p, v in PRIORITY.items())}</ul>
</section>
"""
    return stranka(L("Home", "Úvod"), telo, "index.html", "index.html")


def str_moduly(moduly: list, kurzy: list, videa: list) -> str:
    radky = ""
    for m in moduly:
        radky += (f'<tr><td><a href="m/{m["id"]}.html"><span class="cislo">{m["id"]}</span> {esc(m["title"])}</a></td>'
                  f'<td>{esc(m["phase"])}</td><td>{prio(m["priority"])}</td><td>{m["quick_min"]}</td><td>{m["deep_min"]}</td>'
                  f'<td>{len(m["cviceni"])}</td><td>{postup(klice_modulu(m, kurzy, videa))}</td></tr>')
    telo = f"""
<h1>{L('Modules', 'Moduly')}</h1>
<p>{L('Every module has a <strong>Quick version</strong> (enough to understand and explain it) and a <strong>Deep dive</strong> (the full theory, with sub-topics marked P1–P3). Then hands-on exercises, self-check questions, interview questions and resources.',
      'Každý modul má <strong>krátkou verzi</strong> (dost na pochopení a vysvětlení) a <strong>výklad do hloubky</strong> (celá teorie, podtémata označená P1–P3). K tomu praktická cvičení, otázky na ověření, pohovorové otázky a zdroje.')}</p>
<div class="tabulka"><table class="moduly-tab"><thead><tr><th>{L('Module', 'Modul')}</th><th>{L('Phase', 'Fáze')}</th><th>{L('Priority', 'Priorita')}</th><th>{L('Quick (min)', 'Krátká (min)')}</th><th>{L('Deep (min)', 'Hloubka (min)')}</th><th>{L('Exercises', 'Cvičení')}</th><th>{L('Progress', 'Postup')}</th></tr></thead>
<tbody>{radky}</tbody></table></div>
"""
    return stranka(L("Modules", "Moduly"), telo, "modules.html", "modules.html")


def str_cesta(moduly: list, kurzy: list, base: str, cesta: list) -> str:
    podle_id = {m["id"]: m for m in moduly}
    podle_slug = {c["slug"]: c for c in kurzy}
    radky = ""
    for krok in cesta:
        mm = " ".join(f'<a href="m/{i}.html">{i} {esc(podle_id[i]["title"]) if i in podle_id else ""}</a>' for i in krok["modules"])
        cc = "".join(f'<li><a href="{esc(base + s + "/")}" target="_blank" rel="noopener">{esc(podle_slug[s]["title"])}</a> ({podle_slug[s]["hours"]} h)</li>'
                     for s in krok["courses"] if s in podle_slug)
        ess = f'<span class="stitek stitek-core">Essentials</span>' if krok["essentials"] else ""
        klic = "nat-path-" + krok["weeks"].replace("–", "-")
        radky += f"""<li class="krok{' krok-essentials' if krok['essentials'] else ''}">
<div class="krok-tyden">{L('Week', 'Týden')} {esc(krok['weeks'])}</div>
<div class="krok-telo"><h3>{esc(D(krok, 'title'))} {ess}</h3>
<p class="krok-moduly">{mm}</p><p>{esc(D(krok, 'do'))}</p>
{f'<ul class="krok-kurzy">{cc}</ul>' if cc else ''}
<p class="milnik"><strong>{L('Milestone', 'Milník')}:</strong> {esc(D(krok, 'milestone'))}</p>
{fajfka(klic, L('Done', 'Hotovo'))}</div></li>"""
    telo = f"""
<h1>{L('Learning path', 'Studijní cesta')}</h1>
<p>{L('Plan for about <strong>8–10 hours a week</strong>. It mixes theory and practice every week: read, watch, then do something in a real tool. The capstone project grows alongside the modules, so by the end you have a portfolio, not just notes.',
      'Počítej zhruba s <strong>8–10 hodinami týdně</strong>. Každý týden se střídá teorie a praxe: přečíst, podívat se, pak něco udělat ve skutečném nástroji. Capstone roste spolu s moduly, takže na konci máš portfolio, ne jen poznámky.')}</p>
<div class="filtr" role="group" aria-label="{L('Route', 'Cesta')}">
  <button type="button" class="tlacitko" data-cesta="full" aria-pressed="true" id="full">{L('Full route (~24 weeks)', 'Plná cesta (~24 týdnů)')}</button>
  <button type="button" class="tlacitko" data-cesta="essentials" aria-pressed="false" id="essentials">{L('Essentials route (~10–12 weeks)', 'Zkrácená cesta (~10–12 týdnů)')}</button>
</div>
<div class="box box-note" data-jen-essentials hidden><strong class="box-nadpis">{L('Essentials route', 'Zkrácená cesta')}</strong>
<p>{L('Do the steps marked <em>Essentials</em>, read the <em>Quick version</em> of every other module, and in the capstone do steps 2, 4, 5, 7, 8, 9 and 10. Deep dives only for BPMN (04), specifications (06), user stories (07), SQL (10) and APIs (11) – those are explicit in the job ad. Roughly 100–120 hours.',
      'Udělej kroky označené <em>Essentials</em>, u ostatních modulů si přečti <em>krátkou verzi</em> a v capstonu udělej kroky 2, 4, 5, 7, 8, 9 a 10. Do hloubky jen BPMN (04), specifikace (06), user stories (07), SQL (10) a API (11) – ty inzerát chce výslovně. Zhruba 100–120 hodin.')}</p></div>
<ol class="cesta" data-cesta-seznam>{radky}</ol>
<h2>{L('Why this order', 'Proč v tomhle pořadí')}</h2>
<ul>
<li>{L('<strong>Role and delivery first</strong> – everything else makes sense once you know who does what in an IT project.', '<strong>Nejdřív role a dodávka</strong> – všechno ostatní dává smysl, až když víš, kdo co v IT projektu dělá.')}</li>
<li>{L('<strong>Process modeling early</strong> – it builds on what you already do and gives quick wins in a real tool.', '<strong>Modelování procesů brzy</strong> – navazuje na to, co už děláš, a rychle přinese výsledek ve skutečném nástroji.')}</li>
<li>{L('<strong>Requirements before technology</strong> – SQL and APIs are tools for checking and specifying requirements, not goals in themselves.', '<strong>Požadavky před technologií</strong> – SQL a API jsou nástroje na ověření a popis požadavků, ne cíl sám o sobě.')}</li>
<li>{L('<strong>Testing, low-code and AI late</strong> – they need the earlier pieces (requirements, data, APIs) to make sense.', '<strong>Testování, low-code a AI později</strong> – potřebují předchozí části (požadavky, data, API).')}</li>
<li>{L('<strong>Interview prep at the end, applications earlier</strong> – once the Essentials steps are done you can start applying; keep going with the rest while you interview.', '<strong>Příprava na pohovor na konci, hlásit se dřív</strong> – po krocích Essentials se můžeš začít hlásit a zbytek dodělávat během pohovorů.')}</li>
</ul>
"""
    return stranka(L("Learning path", "Studijní cesta"), telo, "path.html", "path.html")


def str_kurzy(kurzy: list, base: str, moduly: list) -> str:
    nazvy = {m["id"]: m["title"] for m in moduly}
    core = [c for c in kurzy if c["tier"] == "core"]
    opt = [c for c in kurzy if c["tier"] != "core"]

    def skupina(seznam):
        out = ""
        for mid in sorted({c["modules"][0] for c in seznam}):
            cc = [c for c in seznam if c["modules"][0] == mid]
            out += f'<h3><a href="m/{mid}.html">{mid} {esc(nazvy.get(mid, ""))}</a></h3><ul class="zdroje">' + "".join(karta_kurzu(c, base) for c in cc) + "</ul>"
        return out
    hod = f"{sum(c['hours'] for c in core):.0f}"
    telo = f"""
<h1>{L('Udemy courses', 'Kurzy na Udemy')}</h1>
<p>{L(f'Selected (October 2026) by fit with the job ad, rating (mostly ≥ 4.5), freshness and length. <strong>Core</strong> courses ({len(core)}, about {hod} hours of video) carry the path; <strong>optional</strong> ones go deeper or offer an alternative. You do not need to finish every course: skip sections you already know, and do the exercises on this site instead of passive watching.',
      f'Vybráno (říjen 2026) podle shody s inzerátem, hodnocení (většinou ≥ 4,5), aktuálnosti a délky. <strong>Hlavní</strong> kurzy ({len(core)}, asi {hod} hodin videa) nesou celou cestu, <strong>volitelné</strong> jdou do hloubky nebo nabízí alternativu. Nemusíš dokončit každý kurz: přeskoč, co už znáš, a místo pasivního sledování dělej cvičení na tomto webu.')}</p>
<aside class="box box-note"><strong class="box-nadpis">{L('Paid courses', 'Placené kurzy')}</strong>
<p>{L('Courses on udemy.com are paid individually. Udemy runs discounts very often, so a course rarely costs the list price – wait for a sale. If your employer has <strong>Udemy Business</strong>, the same courses are usually included there for free; ask HR or your learning team. Ratings and hours come from the course pages in October 2026.',
      'Kurzy na udemy.com se platí jednotlivě. Udemy má slevy velmi často, takže kurz málokdy stojí plnou cenu – počkej na akci. Pokud má tvůj zaměstnavatel <strong>Udemy Business</strong>, bývají tam stejné kurzy zdarma; zeptej se HR nebo týmu pro vzdělávání. Hodnocení a délky jsou z kurzů v říjnu 2026.')}</p></aside>
{postup(['nat-u-' + c['slug'] for c in core], L('core courses completed', 'hlavních kurzů hotovo'))}
<h2>{L('Core courses', 'Hlavní kurzy')}</h2>{skupina(core)}
<h2>{L('Optional courses', 'Volitelné kurzy')}</h2>{skupina(opt)}
<p class="pozn">{L('Tip: watch at 1.25× speed, pause at every exercise, and take notes in your own words. Enrolling is done by you in Udemy.',
                   'Tip: pusť si video na 1,25×, u každého cvičení zastav a poznámky si piš vlastními slovy. Do kurzů se na Udemy zapisuješ sama.')}</p>
"""
    return stranka(L("Udemy courses", "Kurzy Udemy"), telo, "courses.html", "courses.html")


def str_videa(videa: list) -> str:
    temata: dict[str, list] = {}
    for v in videa:
        temata.setdefault(D(v, "topic") or "Other", []).append(v)
    out = ""
    for t, vv in temata.items():
        out += f"<h2>{esc(t)}</h2><ul class='zdroje'>" + "".join(karta_videa(v) for v in vv) + "</ul>"
    telo = f"""
<h1>{L('Free videos', 'Videa zdarma')}</h1>
<p>{L('Short, free videos (YouTube) that complement the modules. Tick each one when watched. Links were checked in October 2026.',
      'Krátká videa zdarma (YouTube), která doplňují moduly. Po zhlédnutí je odškrtni. Odkazy ověřeny v říjnu 2026. Videa jsou anglicky.')}</p>
{postup(['nat-v-' + v['id'] for v in videa], L('videos watched', 'videí zhlédnuto'))}
{out}
"""
    return stranka(L("Videos", "Videa"), telo, "videos.html", "videos.html")


def str_nastroje(nastroje: list, cteni: list) -> str:
    out = "<ul class='zdroje'>" + "".join(karta_nastroje(t) for t in nastroje) + "</ul>"
    ct = ""
    if cteni:
        ct = f"<h2>{L('Free reading and references', 'Ke čtení a k nahlédnutí (zdarma)')}</h2><ul class='zdroje'>" + "".join(karta_cteni(r, True) for r in cteni) + "</ul>"
    telo = f"""
<h1>{L('Tools to try', 'Nástroje k vyzkoušení')}</h1>
<p>{L('Everything a junior BA is expected to have touched. Most are free and run in the browser. Tick a tool once you have used it for a real exercise, not just opened it.',
      'Všechno, co by junior BA měl mít v ruce. Většina je zdarma a běží v prohlížeči. Nástroj odškrtni, až ho použiješ na skutečné cvičení, ne jen když ho otevřeš.')}</p>
<aside class="box box-warning"><strong class="box-nadpis">{L('Company data stays at the company', 'Firemní data zůstávají ve firmě')}</strong>
<p>{L('Practise only with the fictional ExportShield data from this site. Never paste work or client data into public AI tools or personal accounts. At work, use the tools your IT has approved.',
      'Procvičuj jen s fiktivními daty ExportShield z tohoto webu. Pracovní ani klientská data nikdy nevkládej do veřejných AI nástrojů ani do osobních účtů. V práci používej nástroje schválené IT.')}</p></aside>
{postup(['nat-t-' + t['id'] for t in nastroje], L('tools tried', 'nástrojů vyzkoušeno'))}
{out}
{ct}
"""
    return stranka(L("Tools", "Nástroje"), telo, "tools.html", "tools.html")


def str_slovnik(moduly: list) -> str:
    pojmy = sorted((p for m in moduly for p in m["pojmy"]), key=lambda p: p["term"].lower())
    data = json.dumps([{"t": p["term"], "d": p["def"], "m": p["modul"]} for p in pojmy], ensure_ascii=False)
    radky = "".join(
        f'<div class="pojem" data-hledat="{esc((p["term"] + " " + p["def"]).lower())}"><dt>{esc(p["term"])} '
        f'<a class="modul-odkaz" href="m/{p["modul"]}.html">{p["modul"]}</a></dt><dd>{inline(p["def"])}</dd></div>' for p in pojmy)
    telo = f"""
<h1>{L('Glossary', 'Slovník')}</h1>
<p>{L(f'{len(pojmy)} terms from all modules. Use the matching game to test yourself.',
      f'{len(pojmy)} pojmů ze všech modulů. Termín anglicky, výklad česky. Přiřazovací hrou se můžeš otestovat.')}</p>
<div class="zalozky" data-zalozky="slovnik">
<div class="zalozky-lista" role="tablist">
<button type="button" role="tab" id="tab-list" aria-controls="panel-list" aria-selected="true">{L('Term list', 'Seznam pojmů')}</button>
<button type="button" role="tab" id="tab-match" aria-controls="panel-match" aria-selected="false">{L('Matching game', 'Přiřazovací hra')}</button>
</div>
<section role="tabpanel" id="panel-list" aria-labelledby="tab-list" class="panel">
<label class="hledani">{L('Search', 'Hledat')} <input type="search" data-hledani placeholder="{L('e.g. gateway, JOIN, UAT', 'např. gateway, JOIN, UAT')}"></label>
<dl class="pojmy pojmy-slovnik">{radky}</dl>
</section>
<section role="tabpanel" id="panel-match" aria-labelledby="tab-match" class="panel" hidden>
<p>{L('Pick a term, then its definition. Six pairs per round.', 'Vyber pojem, pak jeho definici. Šest dvojic na kolo.')}</p>
<div class="prirazovani" data-prirazovani></div>
<p><button type="button" class="tlacitko" data-nove-kolo>{L('New round', 'Nové kolo')}</button> <span data-skore></span></p>
</section>
</div>
<script>window.BA_POJMY = {data};</script>
"""
    return stranka(L("Glossary", "Slovník"), telo, "glossary.html", "glossary.html")


def str_pohovor(moduly: list) -> str:
    out = ""
    klice = []
    for m in moduly:
        if not m["pohovor"]:
            continue
        out += f'<h2><a href="m/{m["id"]}.html">{m["id"]} {esc(m["title"])}</a></h2>'
        for i, q in enumerate(m["pohovor"], 1):
            k = f"nat-iq-{m['id']}-{i}"
            klice.append(k)
            pr = Prevod()
            out += (f'<div class="pohovor-radek">{fajfka(k)}<details class="pohovor"><summary><span class="q">{inline(q["q"])}</span>'
                    f'<span class="ukaz">{L("Strong answer", "Silná odpověď")}</span></summary><div class="odpoved">{pr.html(q["a"])}</div></details></div>')
    telo = f"""
<h1>{L('Interview practice', 'Příprava na pohovor')}</h1>
<p>{L('All interview questions from the modules in one place. Answer each one <strong>out loud</strong> (or record yourself) before opening the outline. Tick a question when you can answer it confidently in under two minutes. Module 17 covers the interview process, STAR stories and case exercises.',
      'Všechny pohovorové otázky z modulů na jednom místě. Na každou odpověz <strong>nahlas</strong> (nebo se nahraj), než si otevřeš osnovu. Otázku odškrtni, až ji zvládneš s jistotou do dvou minut. Pohovor může být anglicky, proto je u otázek i anglické znění. Průběh pohovoru, STAR příběhy a případové úlohy jsou v modulu 17.')}</p>
{postup(klice, L('questions I can answer', 'otázek zvládám'))}
{out}
"""
    return stranka(L("Interview practice", "Příprava na pohovor"), telo, "interview.html", "interview.html")


def str_certifikace(certs: list) -> str:
    karty = ""
    for c in certs:
        pole = [(L("Issued by", "Vydává"), "body"), (L("Level", "Úroveň"), "level"), (L("Cost", "Cena"), "cost"),
                (L("Format", "Formát"), "format"), (L("Weight in CZ hiring", "Váha při náboru v ČR"), "weight"),
                (L("When it makes sense", "Kdy to dává smysl"), "when")]
        radky = "".join(f"<tr><th>{esc(k)}</th><td>{inline(str(D(c, v)))}</td></tr>" for k, v in pole if c.get(v))
        karty += (f'<section class="cert" id="{esc(c["id"])}"><h2>{esc(D(c, "name"))} {prio(c["priority"]) if c.get("priority") else ""}</h2>'
                  f'<p>{inline(D(c, "verdict"))}</p><div class="tabulka"><table>{radky}</table></div>'
                  f'<p><a href="{esc(c["url"])}" target="_blank" rel="noopener">{L("Official page", "Oficiální stránka")}</a></p></section>')
    telo = f"""
<h1>{L('Certificates', 'Certifikace')}</h1>
<p>{L('Honest summary: for a junior IT Business Analyst in the Czech Republic <strong>no certificate is a hard requirement</strong>. Employers look for evidence that you can analyse, model and specify – which is what the capstone portfolio shows. A certificate helps as a tie-breaker, as structure for your learning, and in some banks and consultancies that value a common vocabulary. Prices and formats were checked in October 2026; verify before you pay.',
      'Upřímně: pro juniorního IT Business Analysta v ČR <strong>není žádná certifikace podmínkou</strong>. Zaměstnavatelé chtějí vidět, že umíš analyzovat, modelovat a specifikovat – a to ukazuje portfolio z capstonu. Certifikát pomůže při rozhodování mezi podobnými kandidáty, dá učení strukturu a v některých bankách a konzultačních firmách se cení společný slovník. Ceny a formáty ověřeny v říjnu 2026, před platbou je zkontroluj.')}</p>
{karty}
"""
    return stranka(L("Certificates", "Certifikace"), telo, "certifications.html", "certifications.html")


def str_pozice(jobs: list) -> str:
    karty = ""
    for j in jobs:
        poz = (f'<p class="meta">{esc(j.get("company", ""))} · {esc(j.get("location", ""))}'
               f'{" · " + esc(j["salary"]) if j.get("salary") else ""}{" · " + L("seen", "viděno") + " " + esc(j["seen"]) if j.get("seen") else ""}</p>')
        karty += (f'<section class="pozice"><h2><a href="{esc(j["url"])}" target="_blank" rel="noopener">{esc(j["title"])}</a></h2>{poz}'
                  f'<p><strong>{L("They ask for:", "Požadují:")}</strong> {inline(D(j, "requirements"))}</p>'
                  f'<p><strong>{L("How this path prepares you:", "Jak tě na to cesta připraví:")}</strong> {inline(D(j, "fit"))}</p></section>')
    role = [
        ("IT Business Analyst / IT analytik", "requirements to specifications, works with vendors and testers. The main target.",
         "od požadavků ke specifikacím, spolupráce s dodavateli a testery. Hlavní cíl."),
        ("Business Analyst (junior)", "same core, sometimes closer to business than IT.", "stejné jádro, někdy blíž byznysu než IT."),
        ("Process analyst / procesní analytik", "BPMN, process improvement, automation candidates.", "BPMN, zlepšování procesů, kandidáti na automatizaci."),
        ("Low-code / Power Platform analyst", "automation with Power Automate/Power Apps.", "automatizace v Power Automate / Power Apps."),
        ("Product Owner (junior)", "backlog and stories; usually after 1–2 years as a BA.", "backlog a user stories; obvykle po 1–2 letech jako BA."),
        ("IT project coordinator / junior PM", "delivery, vendors, status reporting; close cousin of the BA role.",
         "dodávka, dodavatelé, reporting stavu; blízký příbuzný role BA."),
    ]
    seznam_roli = "".join(f"<li><strong>{esc(r)}</strong> – {esc(L(en, cs))}</li>" for r, en, cs in role)
    telo = f"""
<h1>{L('Positions this path prepares you for', 'Pozice, na které tě cesta připraví')}</h1>
<p>{L('Real job ads (autumn 2026) showing the kind of roles the path targets. Ads expire quickly – use them to see what employers ask for, then search for current ones on jobs.cz, startupjobs.cz, LinkedIn and company career pages with keywords like <em>business analyst</em>, <em>IT analytik</em>, <em>procesní analytik</em>, <em>Power Platform</em>, <em>junior</em>.',
      'Skutečné inzeráty (podzim 2026), které ukazují, na jaké role cesta míří. Inzeráty rychle mizí – ber je jako ukázku požadavků a aktuální hledej na jobs.cz, startupjobs.cz, LinkedInu a kariérních stránkách firem podle slov <em>business analyst</em>, <em>IT analytik</em>, <em>procesní analytik</em>, <em>Power Platform</em>, <em>junior</em>.')}</p>
<h2>{L('Typical role titles', 'Typické názvy rolí')}</h2>
<ul>{seznam_roli}</ul>
{karty}
"""
    return stranka(L("Jobs", "Pozice"), telo, "jobs.html", "jobs.html")


def str_projekt(projekt: dict) -> str:
    s = projekt["sekce"]
    obsah = "".join(s.get(k, "") if k.startswith("_") else f"<h2>{esc(k)}</h2>" + s[k] for k in s)
    klice = [f"nat-ex-{c['id']}" for c in projekt["cviceni"]]
    telo = f"""
<h1>{esc(projekt['title'])}</h1>
{postup(klice, L('capstone deliverables done', 'výstupů capstonu hotovo'), velky=True)}
{obsah}
"""
    return stranka(L("Capstone project", "Závěrečný projekt"), telo, "project.html", "project.html", mermaid=projekt["mermaid"])


def str_sql() -> str:
    telo = f"""
<h1>SQL lab</h1>
<p>{L('A real SQLite database running in your browser, loaded with the fictional <strong>ExportShield Insurance</strong> data (exporters, buyers, policies, credit limits, invoices, claims, payments). Nothing is sent anywhere. Reload the page to reset the data.',
      'Skutečná databáze SQLite přímo v prohlížeči s fiktivními daty pojišťovny <strong>ExportShield Insurance</strong> (exportéři, odběratelé, smlouvy, limity, faktury, škody, platby). Nic se nikam neposílá. Obnovením stránky se data vrátí do původního stavu.')}</p>
<div class="sql-lab">
  <div class="sql-schema" data-sql-schema><p>{L('Loading database…', 'Načítám databázi…')}</p></div>
  <div class="sql-prace">
    <label for="sql-dotaz" class="nadpis-pole">{L('Query', 'Dotaz')}</label>
    <textarea id="sql-dotaz" spellcheck="false" rows="8">SELECT c.name AS exporter, COUNT(p.id) AS policies
FROM customers c
LEFT JOIN policies p ON p.customer_id = c.id
GROUP BY c.name
ORDER BY policies DESC;</textarea>
    <p class="sql-akce"><button type="button" class="tlacitko tlacitko-hlavni" data-sql-spust>{L('Run (Ctrl+Enter)', 'Spustit (Ctrl+Enter)')}</button>
    <select data-sql-priklady aria-label="{L('Example queries', 'Ukázkové dotazy')}"><option value="">{L('Example queries…', 'Ukázkové dotazy…')}</option></select></p>
    <div data-sql-vysledek class="sql-vysledek" aria-live="polite"></div>
  </div>
</div>
<p class="pozn">{L('Module 10 has 15 graded tasks for this lab. SQLite dialect: dates are text (YYYY-MM-DD); use <code>date()</code> and <code>julianday()</code>. The dataset is a snapshot as of 2026-09-30.',
                   'Modul 10 má pro tento lab 15 úloh od lehkých po těžké. Dialekt SQLite: data jsou text (RRRR-MM-DD), použij <code>date()</code> a <code>julianday()</code>. Data jsou stav k 30. 9. 2026.')}</p>
"""
    return stranka("SQL lab", telo, "sql.html", "sql.html", skripty=[
        "https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.10.3/sql-wasm.js", "assets/data/exportshield.js", "assets/sql-lab.js"])


def str_api() -> str:
    telo = f"""
<h1>API lab</h1>
<p>{L('Send real HTTP requests from your browser and read the response, like in Postman. Two public APIs that need no key:',
      'Posílej skutečné HTTP požadavky z prohlížeče a čti odpověď, podobně jako v Postmanu. Dvě veřejná API bez klíče:')}</p>
<ul>
<li>{L('<strong>ARES</strong> – the official Czech business register (GET a company by its IČO). This is the kind of lookup an underwriter does manually today.',
       '<strong>ARES</strong> – oficiální registr ekonomických subjektů (GET firmy podle IČO). Přesně takové dohledání dnes underwriter dělá ručně.')}</li>
<li>{L('<strong>JSONPlaceholder</strong> – a fake REST API for practice; you can also try POST, PUT and DELETE (nothing is really saved).',
       '<strong>JSONPlaceholder</strong> – cvičné REST API; zkusit můžeš i POST, PUT a DELETE (nic se doopravdy neuloží).')}</li>
</ul>
<div class="api-lab">
  <div class="api-radek">
    <label class="sr" for="api-metoda">{L('Method', 'Metoda')}</label>
    <select id="api-metoda" data-api-metoda><option>GET</option><option>POST</option><option>PUT</option><option>DELETE</option></select>
    <label class="sr" for="api-url">URL</label>
    <input id="api-url" data-api-url type="url" value="https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/00006947">
    <button type="button" class="tlacitko tlacitko-hlavni" data-api-posli>{L('Send', 'Odeslat')}</button>
  </div>
  <p class="api-predvolby">{L('Presets:', 'Předvolby:')} <span data-api-predvolby></span></p>
  <label for="api-telo" class="nadpis-pole">{L('Request body (JSON, for POST/PUT)', 'Tělo požadavku (JSON, pro POST/PUT)')}</label>
  <textarea id="api-telo" data-api-telo rows="5" spellcheck="false">{{
  "title": "Credit limit request",
  "body": "Buyer: Rheinwerk Handels GmbH, amount 250000 EUR",
  "userId": 1
}}</textarea>
  <div class="api-odpoved" data-api-odpoved aria-live="polite"></div>
</div>
<h2>{L('What to notice', 'Čeho si všímat')}</h2>
<ul>
<li>{L('The <strong>status code</strong>: 200 OK, 201 Created, 404 Not Found (try a non-existent IČO like 00000001), 400 Bad Request (try letters instead of digits).',
       '<strong>Stavový kód</strong>: 200 OK, 201 Created, 404 Not Found (zkus neexistující IČO, např. 00000001), 400 Bad Request (zkus písmena místo číslic).')}</li>
<li>{L('The <strong>structure</strong> of the JSON: objects <code>{ }</code>, arrays <code>[ ]</code>, nested fields such as <code>sidlo.nazevObce</code>.',
       '<strong>Strukturu</strong> JSONu: objekty <code>{ }</code>, pole <code>[ ]</code>, vnořená pole jako <code>sidlo.nazevObce</code>.')}</li>
<li>{L('The <strong>time</strong> it took – non-functional requirements often say how fast an integration must answer.',
       '<strong>Dobu</strong> odpovědi – nefunkční požadavky často určují, jak rychle musí integrace odpovědět.')}</li>
<li>{L('Which fields you would <strong>map</strong> into the PolicyHub buyer record (module 11, exercise on field mapping).',
       'Která pole bys <strong>namapovala</strong> do záznamu odběratele v PolicyHubu (modul 11, cvičení na mapování polí).')}</li>
</ul>
<p class="pozn">{L('Some APIs block calls from web pages (CORS). Postman does not have that limitation – use it for everything else.',
                   'Některá API volání z webových stránek blokují (CORS). Postman tohle omezení nemá – na ostatní API použij jeho.')}</p>
"""
    return stranka("API lab", telo, "api.html", "api.html", skripty=["assets/api-lab.js"])


# ---------------------------------------------------------------- build

def postav(jazyk: str, cil: Path, kurzy: list, base: str, data: dict) -> list[dict]:
    global JAZYK
    JAZYK = jazyk
    markdown_ba.JAZYK = jazyk
    moduly = nacti_moduly(jazyk)
    projekt = nacti_projekt(jazyk)
    (cil / "m").mkdir(parents=True, exist_ok=True)

    def zapis(nazev: str, obsah: str):
        (cil / nazev).write_text(obsah, encoding="utf-8")

    for m in moduly:
        zapis(f"m/{m['id']}.html", str_modul(m, kurzy, base, data["videa"], data["nastroje"], data["cteni"], moduly))
    zapis("index.html", str_index(moduly, kurzy, data["videa"], projekt))
    zapis("modules.html", str_moduly(moduly, kurzy, data["videa"]))
    zapis("path.html", str_cesta(moduly, kurzy, base, data["cesta"]))
    zapis("courses.html", str_kurzy(kurzy, base, moduly))
    zapis("videos.html", str_videa(data["videa"]))
    zapis("tools.html", str_nastroje(data["nastroje"], data["cteni"]))
    zapis("glossary.html", str_slovnik(moduly))
    zapis("interview.html", str_pohovor(moduly))
    zapis("certifications.html", str_certifikace(data["certs"]))
    zapis("jobs.html", str_pozice(data["jobs"]))
    zapis("sql.html", str_sql())
    zapis("api.html", str_api())
    if projekt:
        zapis("project.html", str_projekt(projekt))
    return moduly


def main() -> int:
    if not list((OBSAH / "moduly").glob("*.md")):
        print("Žádné moduly v obsah/moduly/")
        return 1
    ud = json.loads((DATA / "udemy.json").read_text(encoding="utf-8"))
    kurzy, base = ud["courses"], ud["base"]
    data = {
        "videa": nacti_json("youtube.json", "videos"), "nastroje": nacti_json("tools.json", "tools"),
        "cteni": nacti_json("reading.json", "items"), "certs": nacti_json("certs.json", "certs"),
        "jobs": nacti_json("jobs.json", "jobs"), "cesta": nacti_json("cesta.json", "steps"),
    }

    if WEB.exists():
        shutil.rmtree(WEB)
    WEB.mkdir()
    shutil.copytree(ASSETS, WEB / "assets")
    (WEB / ".nojekyll").write_text("", encoding="utf-8")
    sql = DATA / "sql" / "exportshield.sql"
    if sql.exists():
        (WEB / "assets" / "data").mkdir(exist_ok=True)
        (WEB / "assets" / "data" / "exportshield.js").write_text(
            "window.EXPORTSHIELD_SQL = " + json.dumps(sql.read_text(encoding="utf-8"), ensure_ascii=False) + ";\n",
            encoding="utf-8")

    en = postav("en", WEB, kurzy, base, data)
    cs = postav("cs", WEB / "cs", kurzy, base, data)

    print(f"Moduly: {len(en)} (česky přeloženo {sum(m['prelozeno'] for m in cs)})")
    for m, c in zip(en, cs):
        print(f"  {m['id']} {m['title'][:44]:44} q {m['slova_quick']:4} d {m['slova_deep']:5} cv {len(m['cviceni'])}/{len(c['cviceni'])} "
              f"q {len(m['otazky'])}/{len(c['otazky'])} int {len(m['pohovor'])}/{len(c['pohovor'])} pojmy {len(m['pojmy'])}/{len(c['pojmy'])}"
              f"{'' if c['prelozeno'] else '  (bez CZ)'}")
    print(f"Kurzy: {len(kurzy)}, videa {len(data['videa'])}, nástroje {len(data['nastroje'])}, čtení {len(data['cteni'])}, "
          f"certifikáty {len(data['certs'])}, pozice {len(data['jobs'])}, kroky cesty {len(data['cesta'])}")
    chybi_cs = [n for n, seznam, pole in [("udemy", kurzy, "why"), ("videa", data["videa"], "why"), ("nastroje", data["nastroje"], "what"),
                                          ("cesta", data["cesta"], "title"), ("certs", data["certs"], "verdict"), ("jobs", data["jobs"], "fit")]
                if any(not x.get(pole + "_cs") for x in seznam)]
    if chybi_cs:
        print("Chybí české texty v datech:", ", ".join(chybi_cs))
    return 0


if __name__ == "__main__":
    sys.exit(main())
