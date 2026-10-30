/* BA Academy – fajfky, ukazatele postupu, záložky, menu, slovníková hra, kopírování kódu.
   Postup: localStorage, klíč nat-<druh>-<id> = "1" (synchronizuje ucet.js).
   Nastavení vzhledu (poslední záložka, zvolená cesta): natui-*, nesynchronizuje se. */
(function () {
  "use strict";

  function cti(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function zapis(k, v) {
    try { if (v === null) localStorage.removeItem(k); else localStorage.setItem(k, v); } catch (e) { /* soukromý režim */ }
  }
  function vse(sel, koren) { return [].slice.call((koren || document).querySelectorAll(sel)); }
  var CS = document.documentElement.lang === "cs";
  function T(en, cs) { return CS ? cs : en; }

  /* --- fajfky a postup ------------------------------------------------- */

  function obnovPostup() {
    vse("[data-keys]").forEach(function (el) {
      var klice = el.getAttribute("data-keys").split(/\s+/).filter(Boolean);
      var hotovo = klice.filter(function (k) { return cti(k) === "1"; }).length;
      var proc = klice.length ? Math.round(100 * hotovo / klice.length) : 0;
      var pruh = el.querySelector(".postup-pruh span");
      if (pruh) pruh.style.width = proc + "%";
      var text = el.querySelector(".postup-text");
      if (text) {
        if (!text.dataset.popis) text.dataset.popis = text.textContent;
        text.textContent = hotovo + " / " + klice.length + (text.dataset.popis ? " " + text.dataset.popis : "");
      }
      el.classList.toggle("postup-hotovo", klice.length > 0 && hotovo === klice.length);
    });
    var celkem = document.querySelector("[data-celkovy-postup]");
    if (celkem) {
      var n = 0;
      try {
        for (var i = 0; i < localStorage.length; i++) {
          var k = localStorage.key(i);
          if (/^nat-(read|ex|u|v|t|path|iq|r)-/.test(k) && localStorage.getItem(k) === "1") n++;
        }
      } catch (e) { /* nic */ }
      celkem.textContent = n ? "✓ " + n + T(" done", " hotovo") : "";
    }
  }

  vse("input[type=checkbox][data-key]").forEach(function (ch) {
    var k = ch.getAttribute("data-key");
    ch.checked = cti(k) === "1";
    ch.closest(".fajfka") && ch.closest(".fajfka").classList.toggle("zaskrtnuto", ch.checked);
    ch.addEventListener("change", function () {
      zapis(k, ch.checked ? "1" : null);
      /* stejný klíč může být na stránce víckrát (např. kurz u dvou modulů) */
      vse('input[data-key="' + k + '"]').forEach(function (j) {
        j.checked = ch.checked;
        j.closest(".fajfka") && j.closest(".fajfka").classList.toggle("zaskrtnuto", ch.checked);
      });
      obnovPostup();
    });
  });
  obnovPostup();
  window.addEventListener("storage", obnovPostup);

  /* --- menu na mobilu --------------------------------------------------- */

  var menuTl = document.querySelector(".menu-tlacitko");
  if (menuTl) {
    menuTl.addEventListener("click", function () {
      var otevreno = document.body.classList.toggle("menu-otevreno");
      menuTl.setAttribute("aria-expanded", otevreno ? "true" : "false");
    });
  }

  /* --- záložky ---------------------------------------------------------- */

  vse("[data-zalozky]").forEach(function (box) {
    var jmeno = "natui-tab-" + box.getAttribute("data-zalozky");
    var tlacitka = vse("[role=tab]", box);
    function ukaz(id, fokus) {
      tlacitka.forEach(function (t) {
        var ano = t.id === "tab-" + id;
        t.setAttribute("aria-selected", ano ? "true" : "false");
        t.tabIndex = ano ? 0 : -1;
        var p = document.getElementById(t.getAttribute("aria-controls"));
        if (p) p.hidden = !ano;
        if (ano && fokus) t.focus();
      });
      zapis(jmeno, id);
      if (window.mermaid && window.mermaid.run) {
        try { window.mermaid.run({ querySelector: "#panel-" + id + " .mermaid:not([data-processed])" }); } catch (e) { /* nic */ }
      }
    }
    tlacitka.forEach(function (t, i) {
      t.addEventListener("click", function () { ukaz(t.id.slice(4)); });
      t.addEventListener("keydown", function (u) {
        var d = u.key === "ArrowRight" ? 1 : u.key === "ArrowLeft" ? -1 : 0;
        if (!d) return;
        var dalsi = tlacitka[(i + d + tlacitka.length) % tlacitka.length];
        ukaz(dalsi.id.slice(4), true);
      });
    });
    /* odkaz s kotvou do jiné záložky (#m04-gateways, #m04-e1) */
    function podleKotvy() {
      var h = location.hash.slice(1);
      if (!h) return false;
      var cil = document.getElementById(h);
      if (!cil || !box.contains(cil)) return false;
      var panel = cil.closest("[role=tabpanel]");
      if (panel) { ukaz(panel.id.slice(6)); cil.scrollIntoView(); return true; }
      return false;
    }
    if (!podleKotvy()) {
      var ulozena = cti(jmeno);
      if (ulozena && document.getElementById("tab-" + ulozena)) ukaz(ulozena);
    }
    window.addEventListener("hashchange", podleKotvy);
  });

  /* --- cesta: plná / essentials ---------------------------------------- */

  var cestaTl = vse("[data-cesta]");
  if (cestaTl.length) {
    var nastav = function (c) {
      cestaTl.forEach(function (t) { t.setAttribute("aria-pressed", t.getAttribute("data-cesta") === c ? "true" : "false"); });
      document.body.classList.toggle("jen-essentials", c === "essentials");
      vse("[data-jen-essentials]").forEach(function (x) { x.hidden = c !== "essentials"; });
      zapis("natui-cesta", c);
    };
    cestaTl.forEach(function (t) { t.addEventListener("click", function () { nastav(t.getAttribute("data-cesta")); }); });
    nastav(location.hash === "#essentials" ? "essentials" : location.hash === "#full" ? "full" : (cti("natui-cesta") || "full"));
  }

  /* --- kopírování kódu -------------------------------------------------- */

  vse(".kopirovat").forEach(function (b) {
    b.addEventListener("click", function () {
      var kod = b.parentNode.querySelector("code");
      if (!kod || !navigator.clipboard) return;
      navigator.clipboard.writeText(kod.textContent).then(function () {
        var puvodni = b.textContent;
        b.textContent = T("Copied", "Zkopírováno");
        setTimeout(function () { b.textContent = puvodni; }, 1500);
      });
    });
  });

  /* --- slovník: hledání a přiřazování ---------------------------------- */

  var hledani = document.querySelector("[data-hledani]");
  if (hledani) {
    hledani.addEventListener("input", function () {
      var q = hledani.value.trim().toLowerCase();
      vse(".pojem").forEach(function (p) { p.hidden = q && p.getAttribute("data-hledat").indexOf(q) < 0; });
    });
  }

  var hra = document.querySelector("[data-prirazovani]");
  if (hra && window.BA_POJMY && window.BA_POJMY.length >= 6) {
    var skore = document.querySelector("[data-skore]");
    var body = 0, pokusy = 0;
    var zamichej = function (a) {
      for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var x = a[i]; a[i] = a[j]; a[j] = x; }
      return a;
    };
    var kolo = function () {
      hra.textContent = "";
      var vyber = zamichej(window.BA_POJMY.slice()).slice(0, 6);
      var levy = document.createElement("div"), pravy = document.createElement("div");
      levy.className = "hra-sloupec"; pravy.className = "hra-sloupec";
      var zvoleny = null;
      vyber.forEach(function (p, i) {
        var b = document.createElement("button");
        b.type = "button"; b.className = "hra-pojem"; b.textContent = p.t; b.dataset.i = i;
        b.addEventListener("click", function () {
          if (b.classList.contains("sparovano")) return;
          vse(".hra-pojem", levy).forEach(function (x) { x.classList.remove("vybrano"); });
          b.classList.add("vybrano"); zvoleny = b;
        });
        levy.appendChild(b);
      });
      zamichej(vyber.map(function (p, i) { return { d: p.d, i: i }; })).forEach(function (p) {
        var b = document.createElement("button");
        b.type = "button"; b.className = "hra-definice"; b.textContent = p.d.replace(/[*`]/g, ""); b.dataset.i = p.i;
        b.addEventListener("click", function () {
          if (!zvoleny || b.classList.contains("sparovano")) return;
          pokusy++;
          if (zvoleny.dataset.i === b.dataset.i) {
            body++;
            zvoleny.classList.add("sparovano"); b.classList.add("sparovano");
            zvoleny.classList.remove("vybrano"); zvoleny = null;
          } else {
            b.classList.add("chyba");
            setTimeout(function () { b.classList.remove("chyba"); }, 600);
          }
          if (skore) skore.textContent = body + T(" correct out of ", " správně z ") + pokusy + T(" attempts", " pokusů");
        });
        pravy.appendChild(b);
      });
      hra.appendChild(levy); hra.appendChild(pravy);
    };
    kolo();
    var nove = document.querySelector("[data-nove-kolo]");
    if (nove) nove.addEventListener("click", kolo);
  }
})();
