# -*- coding: utf-8 -*-
"""Malý převodník Markdownu na HTML pro moduly BA Academy (jen standardní knihovna).

Pokrývá formát z PRAVIDLA_ZPRACOVANI.md: nadpisy ## a ### (značka [P1]/[P2]/[P3] na konci),
odstavce, **tučně**, *kurzíva*, `kód`, [odkaz](url), seznamy (vnoření o jednu úroveň),
GFM tabulky, citace >, linka ---, bloky kódu (```mermaid se vykreslí jako diagram),
bloky :::exercise / :::q / :::interview / :::tip / :::warning.
"""

from __future__ import annotations

import html
import re

_ODKAZ = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
_TUCNE = re.compile(r"\*\*(.+?)\*\*")
_KURZIVA = re.compile(r"(?<![*\w])\*(?!\s)([^*\n]+?)(?<!\s)\*(?![*\w])")
_KOD = re.compile(r"`([^`]+)`")
_SEZNAM = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$")
_NADPIS = re.compile(r"^(#{2,4})\s+(.*?)\s*$")
_PRIORITA = re.compile(r"\s*\[(P[123])\]\s*$")
_PLOT = re.compile(r"^\s*(```+|~~~+)\s*([\w+-]*)")
_BLOK = re.compile(r"^:::\s*([\w-]+)(.*)$")
_ATRIBUT = re.compile(r'(\w+)\s*=\s*"([^"]*)"')


JAZYK = "en"  # popisky prvků (tlačítka, rámečky); nastavuje build.py pro každou jazykovou verzi


def slug(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s or "x"


def inline(text: str) -> str:
    """Inline formátování; kód se chrání před ostatními úpravami."""
    kousky: list[str] = []

    def schovej(m: re.Match) -> str:
        kousky.append("<code>" + html.escape(m.group(1)) + "</code>")
        return f"\x00{len(kousky) - 1}\x00"

    t = _KOD.sub(schovej, text)
    t = html.escape(t, quote=False)

    def odkaz(m: re.Match) -> str:
        url = m.group(2)
        cizi = url.startswith("http")
        attr = ' target="_blank" rel="noopener"' if cizi else ""
        return f'<a href="{html.escape(url, quote=True)}"{attr}>{m.group(1)}</a>'

    t = _ODKAZ.sub(odkaz, t)
    t = _TUCNE.sub(r"<strong>\1</strong>", t)
    t = _KURZIVA.sub(r"<em>\1</em>", t)
    t = re.sub(r"\x00(\d+)\x00", lambda m: kousky[int(m.group(1))], t)
    return t


def _bunky(radek: str) -> list[str]:
    r = radek.strip()
    if r.startswith("|"):
        r = r[1:]
    if r.endswith("|"):
        r = r[:-1]
    return [b.strip() for b in re.split(r"(?<!\\)\|", r)]


def _je_oddelovac(radek: str) -> bool:
    return bool(re.match(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$", radek))


def _tabulka(radky: list[str]) -> str:
    hlava = _bunky(radky[0])
    zarovnani = []
    for b in _bunky(radky[1]):
        if b.startswith(":") and b.endswith(":"):
            zarovnani.append("center")
        elif b.endswith(":"):
            zarovnani.append("right")
        else:
            zarovnani.append("")

    def td(tag: str, i: int, obsah: str) -> str:
        z = zarovnani[i] if i < len(zarovnani) and zarovnani[i] else ""
        styl = f' style="text-align:{z}"' if z else ""
        return f"<{tag}{styl}>{inline(obsah)}</{tag}>"

    out = ['<div class="tabulka"><table><thead><tr>']
    out += [td("th", i, b) for i, b in enumerate(hlava)]
    out.append("</tr></thead><tbody>")
    for r in radky[2:]:
        out.append("<tr>" + "".join(td("td", i, b) for i, b in enumerate(_bunky(r))) + "</tr>")
    out.append("</tbody></table></div>")
    return "".join(out)


def _seznam(radky: list[str]) -> str:
    """Seznam s jednou úrovní vnoření (odsazení ≥ 2 mezery)."""
    polozky: list[tuple[int, bool, str]] = []
    for r in radky:
        m = _SEZNAM.match(r)
        if m:
            polozky.append((len(m.group(1).replace("\t", "    ")), m.group(2)[0].isdigit(), m.group(3)))
        elif polozky:  # pokračování položky
            hl, cis, t = polozky[-1]
            polozky[-1] = (hl, cis, t + " " + r.strip())
    if not polozky:
        return ""
    zaklad = polozky[0][0]
    out: list[str] = []
    tag = "ol" if polozky[0][1] else "ul"
    out.append(f"<{tag}>")
    otevreno_vnoreni = None
    for i, (hl, cis, t) in enumerate(polozky):
        if hl > zaklad:
            if otevreno_vnoreni is None:
                otevreno_vnoreni = "ol" if cis else "ul"
                out.append(f"<{otevreno_vnoreni}>")
            out.append(f"<li>{inline(t)}</li>")
            continue
        if otevreno_vnoreni:
            out.append(f"</{otevreno_vnoreni}></li>")
            otevreno_vnoreni = None
        elif i > 0:
            out.append("</li>")
        out.append(f"<li>{inline(t)}")
    if otevreno_vnoreni:
        out.append(f"</{otevreno_vnoreni}>")
    out.append(f"</li></{tag}>")
    return "".join(out)


class Prevod:
    """Převod jednoho kusu Markdownu. Sbírá nadpisy (pro obsah) a obsah bloků."""

    def __init__(self, predpona_kotvy: str = ""):
        self.predpona = predpona_kotvy
        self.nadpisy: list[tuple[int, str, str, str]] = []  # (úroveň, text, kotva, priorita)
        self.cviceni: list[dict] = []
        self.otazky: list[dict] = []
        self.pohovor: list[dict] = []
        self.mermaid = False

    def html(self, zdroj: str) -> str:
        return self._bloky(zdroj.replace("\r\n", "\n").split("\n"))

    def _bloky(self, radky: list[str]) -> str:
        out: list[str] = []
        i = 0
        odstavec: list[str] = []

        def zavri_odstavec():
            if odstavec:
                out.append("<p>" + inline(" ".join(s.strip() for s in odstavec)) + "</p>")
                odstavec.clear()

        while i < len(radky):
            r = radky[i]
            if not r.strip():
                zavri_odstavec()
                i += 1
                continue
            m = _PLOT.match(r)
            if m:
                zavri_odstavec()
                plot, jazyk = m.group(1), m.group(2)
                kod = []
                i += 1
                while i < len(radky) and not radky[i].strip().startswith(plot[:3]):
                    kod.append(radky[i])
                    i += 1
                i += 1
                text = "\n".join(kod)
                if jazyk == "mermaid":
                    self.mermaid = True
                    out.append(f'<pre class="mermaid">{html.escape(text)}</pre>')
                else:
                    trida = f' class="jazyk-{jazyk}"' if jazyk else ""
                    out.append(f'<div class="kod"><pre><code{trida}>{html.escape(text)}</code></pre>'
                               f'<button type="button" class="kopirovat">{"Kopírovat" if JAZYK == "cs" else "Copy"}</button></div>')
                continue
            m = _BLOK.match(r.strip())
            if m and m.group(1) != "":
                zavri_odstavec()
                druh, attrs = m.group(1), dict(_ATRIBUT.findall(m.group(2)))
                vnitrek = []
                i += 1
                hloubka = 0
                while i < len(radky):
                    s = radky[i].strip()
                    if s == ":::" and hloubka == 0:
                        break
                    if _BLOK.match(s) and s != ":::":
                        hloubka += 1
                    elif s == ":::":
                        hloubka -= 1
                    vnitrek.append(radky[i])
                    i += 1
                i += 1
                out.append(self._blok(druh, attrs, vnitrek))
                continue
            m = _NADPIS.match(r)
            if m:
                zavri_odstavec()
                uroven = len(m.group(1))
                text = m.group(2)
                pr = _PRIORITA.search(text)
                priorita = pr.group(1) if pr else ""
                if pr:
                    text = text[: pr.start()]
                kotva = self.predpona + slug(text)
                self.nadpisy.append((uroven, text, kotva, priorita))
                znacka = f' <span class="prio prio-{priorita.lower()}">{priorita}</span>' if priorita else ""
                out.append(f'<h{uroven} id="{kotva}">{inline(text)}{znacka}</h{uroven}>')
                i += 1
                continue
            if r.strip() in ("---", "***"):
                zavri_odstavec()
                out.append("<hr>")
                i += 1
                continue
            if r.lstrip().startswith("|") and i + 1 < len(radky) and _je_oddelovac(radky[i + 1]):
                zavri_odstavec()
                tab = [r, radky[i + 1]]
                i += 2
                while i < len(radky) and radky[i].strip().startswith("|"):
                    tab.append(radky[i])
                    i += 1
                out.append(_tabulka(tab))
                continue
            if _SEZNAM.match(r):
                zavri_odstavec()
                sez = []
                while i < len(radky) and radky[i].strip() and (
                        _SEZNAM.match(radky[i]) or radky[i].startswith("  ")):
                    sez.append(radky[i])
                    i += 1
                out.append(_seznam(sez))
                continue
            if r.lstrip().startswith(">"):
                zavri_odstavec()
                cit = []
                while i < len(radky) and radky[i].lstrip().startswith(">"):
                    cit.append(radky[i].lstrip()[1:].lstrip())
                    i += 1
                out.append("<blockquote>" + self._bloky(cit) + "</blockquote>")
                continue
            odstavec.append(r)
            i += 1
        zavri_odstavec()
        return "\n".join(out)

    def _rozdel(self, vnitrek: list[str]) -> tuple[list[str], list[str]]:
        for j, r in enumerate(vnitrek):
            if r.strip() == "---":
                return vnitrek[:j], vnitrek[j + 1:]
        return vnitrek, []

    def _blok(self, druh: str, attrs: dict, vnitrek: list[str]) -> str:
        if druh == "exercise":
            cid = attrs.get("id", f"ex-{len(self.cviceni) + 1}")
            nazev = attrs.get("title", "Exercise")
            minuty = attrs.get("min", "")
            nastroj = attrs.get("tool", "")
            self.cviceni.append({"id": cid, "title": nazev, "min": minuty, "tool": nastroj})
            meta = []
            if minuty:
                meta.append(f"{minuty} min")
            if nastroj:
                meta.append(html.escape(nastroj))
            return (f'<div class="cviceni" id="{cid}"><div class="cviceni-hlava">'
                    f'<label class="fajfka"><input type="checkbox" data-key="nat-ex-{cid}"> '
                    f'<span>{inline(nazev)}</span></label>'
                    f'<span class="meta">{" · ".join(meta)}</span></div>'
                    f'<div class="cviceni-telo">{self._bloky(vnitrek)}</div></div>')
        if druh in ("q", "interview"):
            otazka, odpoved = self._rozdel(vnitrek)
            text_otazky = " ".join(s.strip() for s in otazka if s.strip())
            seznam = self.otazky if druh == "q" else self.pohovor
            seznam.append({"q": text_otazky, "a": "\n".join(odpoved)})
            trida = "otazka" if druh == "q" else "pohovor"
            cs = JAZYK == "cs"
            popisek = (("Zobrazit odpověď" if cs else "Show answer") if druh == "q"
                       else ("Co má obsahovat silná odpověď" if cs else "What a strong answer covers"))
            return (f'<details class="{trida}"><summary><span class="q">{inline(text_otazky)}</span>'
                    f'<span class="ukaz">{popisek}</span></summary>'
                    f'<div class="odpoved">{self._bloky(odpoved)}</div></details>')
        if druh in ("tip", "warning", "note"):
            nadpis = ({"tip": "Tip", "warning": "Pozor", "note": "Poznámka"} if JAZYK == "cs"
                      else {"tip": "Tip", "warning": "Watch out", "note": "Note"})[druh]
            return (f'<aside class="box box-{druh}"><strong class="box-nadpis">{nadpis}</strong>'
                    f'{self._bloky(vnitrek)}</aside>')
        return self._bloky(vnitrek)


def frontmatter(zdroj: str) -> tuple[dict[str, str], str]:
    zdroj = zdroj.replace("\r\n", "\n")
    if not zdroj.startswith("---\n"):
        return {}, zdroj
    konec = zdroj.find("\n---", 4)
    hlava = zdroj[4:konec]
    telo = zdroj[konec + 4:].lstrip("\n")
    meta: dict[str, str] = {}
    for r in hlava.split("\n"):
        r = re.sub(r"\s+#.*$", "", r)
        if ":" in r:
            k, v = r.split(":", 1)
            meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta, telo


def sekce(telo: str) -> dict[str, str]:
    """Rozdělí tělo modulu podle nadpisů ## na pojmenované sekce."""
    out: dict[str, str] = {}
    aktualni = "_uvod"
    buf: list[str] = []
    v_kodu = False
    for r in telo.split("\n"):
        if _PLOT.match(r):
            v_kodu = not v_kodu
        if not v_kodu and r.startswith("## "):
            out[aktualni] = "\n".join(buf).strip()
            aktualni = r[3:].strip()
            buf = []
        else:
            buf.append(r)
    out[aktualni] = "\n".join(buf).strip()
    return out


def slova(text: str) -> int:
    t = re.sub(r"```.*?```", " ", text, flags=re.S)
    t = re.sub(r"[#*`|>:\-\[\]()]", " ", t)
    return len(re.findall(r"\w+", t))
