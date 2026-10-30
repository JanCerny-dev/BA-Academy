/* SQL lab: SQLite v prohlížeči (sql.js z cdnjs) s datovou sadou ExportShield (assets/data/exportshield.js).
   Nic se neodesílá, data žijí jen v paměti stránky. */
(function () {
  "use strict";

  var CS = document.documentElement.lang === "cs";
  function T(en, cs) { return CS ? cs : en; }

  var VERZE = "1.10.3";
  var PRIKLADY = [
    [T("All exporters", "Všichni exportéři"), "SELECT * FROM customers;"],
    [T("Open claims", "Otevřené škody"), "SELECT id, invoice_id, notified_on, status, claimed_amount\nFROM claims\nWHERE status IN ('NOTIFIED', 'IN_REVIEW')\nORDER BY notified_on;"],
    [T("Credit limits by status", "Limity podle stavu"), "SELECT status, COUNT(*) AS limits, SUM(approved_amount) AS approved_total\nFROM credit_limits\nGROUP BY status;"],
    [T("Unpaid overdue invoices", "Nezaplacené faktury po splatnosti"), "SELECT i.invoice_no, b.name AS buyer, i.amount, i.currency, i.due_date\nFROM invoices i\nJOIN buyers b ON b.id = i.buyer_id\nWHERE i.paid_date IS NULL AND i.due_date < '2026-09-30'  -- dataset snapshot date\nORDER BY i.due_date;"],
    [T("Buyers without a country (data quality)", "Odběratelé bez země (kvalita dat)"), "SELECT * FROM buyers WHERE country_code IS NULL OR country_code = '';"],
    [T("Exposure by country", "Angažovanost podle země"), "SELECT co.name AS country, co.risk_category, SUM(cl.approved_amount) AS approved\nFROM credit_limits cl\nJOIN buyers b ON b.id = cl.buyer_id\nLEFT JOIN countries co ON co.code = b.country_code\nWHERE cl.status IN ('APPROVED', 'REDUCED')\nGROUP BY co.name, co.risk_category\nORDER BY approved DESC;"],
    [T("Days to decide a credit limit", "Dny do rozhodnutí o limitu"), "SELECT underwriter,\n       COUNT(*) AS decided,\n       ROUND(AVG(julianday(decided_on) - julianday(requested_on)), 1) AS avg_days\nFROM credit_limits\nWHERE decided_on IS NOT NULL\nGROUP BY underwriter;"]
  ];

  var vysledek = document.querySelector("[data-sql-vysledek]");
  var schema = document.querySelector("[data-sql-schema]");
  var pole = document.getElementById("sql-dotaz");
  var tlacitko = document.querySelector("[data-sql-spust]");
  var priklady = document.querySelector("[data-sql-priklady]");
  if (!vysledek || !pole) return;

  var db = null;

  function el(tag, trida, text) {
    var x = document.createElement(tag);
    if (trida) x.className = trida;
    if (text !== undefined) x.textContent = text;
    return x;
  }

  function chyba(text) {
    vysledek.textContent = "";
    vysledek.appendChild(el("p", "sql-chyba", text));
  }

  function vykresliSchema() {
    var r = db.exec("SELECT name FROM sqlite_master WHERE type = 'table' ORDER BY name");
    schema.textContent = "";
    schema.appendChild(el("h2", "", T("Tables", "Tabulky")));
    (r[0] ? r[0].values : []).forEach(function (row) {
      var t = row[0];
      var d = el("details");
      var s = el("summary");
      var pocet = db.exec("SELECT COUNT(*) FROM \"" + t + "\"")[0].values[0][0];
      s.appendChild(el("code", "", t));
      s.appendChild(el("span", "meta", " " + pocet + T(" rows", " řádků")));
      d.appendChild(s);
      var ul = el("ul");
      var sl = db.exec("PRAGMA table_info(\"" + t + "\")")[0].values;
      sl.forEach(function (c) {
        var li = el("li");
        li.appendChild(el("code", "", c[1]));
        li.appendChild(el("span", "meta", " " + (c[2] || "") + (c[5] ? " · PK" : "")));
        ul.appendChild(li);
      });
      d.appendChild(ul);
      var b = el("button", "odkaz-tlacitko", "SELECT * FROM " + t);
      b.type = "button";
      b.addEventListener("click", function () { pole.value = "SELECT * FROM " + t + " LIMIT 50;"; spust(); });
      d.appendChild(b);
      schema.appendChild(d);
    });
  }

  function spust() {
    if (!db) return;
    var dotaz = pole.value.trim();
    if (!dotaz) return;
    var t0 = performance.now();
    var vysl;
    try { vysl = db.exec(dotaz); } catch (e) { chyba(T("Error: ", "Chyba: ") + e.message); return; }
    var ms = Math.round(performance.now() - t0);
    vysledek.textContent = "";
    if (!vysl.length) {
      var zmen = db.getRowsModified();
      vysledek.appendChild(el("p", "meta", zmen ? zmen + T(" rows changed (reload the page to reset the data).", " řádků změněno (obnovením stránky se data vrátí).") : T("No rows returned. (", "Dotaz nevrátil žádné řádky. (") + ms + " ms)"));
      return;
    }
    vysl.forEach(function (r) {
      vysledek.appendChild(el("p", "meta", r.values.length + T(" rows · ", " řádků · ") + ms + " ms" + (r.values.length > 500 ? T(" · showing first 500", " · zobrazeno prvních 500") : "")));
      var obal = el("div", "tabulka");
      var tab = el("table");
      var th = el("tr");
      r.columns.forEach(function (c) { th.appendChild(el("th", "", c)); });
      var thead = el("thead"); thead.appendChild(th); tab.appendChild(thead);
      var tb = el("tbody");
      r.values.slice(0, 500).forEach(function (row) {
        var tr = el("tr");
        row.forEach(function (v) {
          var td = el("td", v === null ? "null" : "", v === null ? "NULL" : String(v));
          tr.appendChild(td);
        });
        tb.appendChild(tr);
      });
      tab.appendChild(tb); obal.appendChild(tab); vysledek.appendChild(obal);
    });
  }

  PRIKLADY.forEach(function (p, i) {
    var o = el("option", "", p[0]);
    o.value = String(i);
    priklady.appendChild(o);
  });
  priklady.addEventListener("change", function () {
    if (priklady.value === "") return;
    pole.value = PRIKLADY[+priklady.value][1];
    priklady.value = "";
    spust();
  });
  tlacitko.addEventListener("click", spust);
  pole.addEventListener("keydown", function (u) {
    if (u.key === "Enter" && (u.ctrlKey || u.metaKey)) { u.preventDefault(); spust(); }
  });

  if (!window.initSqlJs || !window.EXPORTSHIELD_SQL) {
    chyba(T("The SQL engine or the dataset could not be loaded. Check your internet connection (the engine comes from cdnjs).", "Nepodařilo se načíst SQL engine nebo data. Zkontroluj připojení k internetu (engine se stahuje z cdnjs)."));
    return;
  }
  window.initSqlJs({ locateFile: function (f) { return "https://cdnjs.cloudflare.com/ajax/libs/sql.js/" + VERZE + "/" + f; } })
    .then(function (SQL) {
      db = new SQL.Database();
      db.exec(window.EXPORTSHIELD_SQL);
      vykresliSchema();
      spust();
    })
    .catch(function (e) { chyba(T("Could not start the SQL engine: ", "SQL engine se nepodařilo spustit: ") + e.message); });
})();
