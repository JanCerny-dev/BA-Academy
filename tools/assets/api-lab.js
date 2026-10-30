/* API lab: skutečné HTTP volání z prohlížeče (fetch) na veřejná API bez klíče.
   Žádné tokeny ani hlavičky Authorization se tu nezadávají – jen veřejná data. */
(function () {
  "use strict";

  var CS = document.documentElement.lang === "cs";
  function T(en, cs) { return CS ? cs : en; }

  var PREDVOLBY = [
    [T("ARES: company by IČO", "ARES: firma podle IČO"), "GET", "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/00006947"],
    [T("ARES: unknown IČO (404)", "ARES: neexistující IČO (404)"), "GET", "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/00000001"],
    [T("JSONPlaceholder: one post", "JSONPlaceholder: jeden příspěvek"), "GET", "https://jsonplaceholder.typicode.com/posts/1"],
    [T("JSONPlaceholder: comments of post 1", "JSONPlaceholder: komentáře k příspěvku 1"), "GET", "https://jsonplaceholder.typicode.com/posts/1/comments"],
    [T("JSONPlaceholder: create post", "JSONPlaceholder: vytvořit příspěvek"), "POST", "https://jsonplaceholder.typicode.com/posts"],
    [T("JSONPlaceholder: update post", "JSONPlaceholder: upravit příspěvek"), "PUT", "https://jsonplaceholder.typicode.com/posts/1"],
    [T("JSONPlaceholder: delete post", "JSONPlaceholder: smazat příspěvek"), "DELETE", "https://jsonplaceholder.typicode.com/posts/1"],
    [T("JSONPlaceholder: not found (404)", "JSONPlaceholder: nenalezeno (404)"), "GET", "https://jsonplaceholder.typicode.com/posts/9999"]
  ];

  var metoda = document.querySelector("[data-api-metoda]");
  var url = document.querySelector("[data-api-url]");
  var telo = document.querySelector("[data-api-telo]");
  var odpoved = document.querySelector("[data-api-odpoved]");
  var posli = document.querySelector("[data-api-posli]");
  var predvolby = document.querySelector("[data-api-predvolby]");
  if (!metoda || !url) return;

  function el(tag, trida, text) {
    var x = document.createElement(tag);
    if (trida) x.className = trida;
    if (text !== undefined) x.textContent = text;
    return x;
  }

  PREDVOLBY.forEach(function (p) {
    var b = el("button", "odkaz-tlacitko", p[0]);
    b.type = "button";
    b.addEventListener("click", function () { metoda.value = p[1]; url.value = p[2]; odesli(); });
    predvolby.appendChild(b);
  });

  function odesli() {
    var adresa = url.value.trim();
    if (!/^https:\/\//.test(adresa)) {
      odpoved.textContent = "";
      odpoved.appendChild(el("p", "sql-chyba", T("Use a full https:// URL.", "Zadej celou adresu začínající https://.")));
      return;
    }
    var nastaveni = { method: metoda.value, headers: { Accept: "application/json" } };
    if (metoda.value === "POST" || metoda.value === "PUT") {
      try { JSON.parse(telo.value); } catch (e) {
        odpoved.textContent = "";
        odpoved.appendChild(el("p", "sql-chyba", T("The request body is not valid JSON: ", "Tělo požadavku není platný JSON: ") + e.message));
        return;
      }
      nastaveni.body = telo.value;
      nastaveni.headers["Content-Type"] = "application/json; charset=UTF-8";
    }
    odpoved.textContent = "";
    odpoved.appendChild(el("p", "meta", T("Sending ", "Odesílám ") + metoda.value + " " + adresa + " …"));
    var t0 = performance.now();
    fetch(adresa, nastaveni).then(function (r) {
      return r.text().then(function (text) { return { r: r, text: text }; });
    }).then(function (x) {
      var ms = Math.round(performance.now() - t0);
      odpoved.textContent = "";
      var stav = el("p", "api-stav api-stav-" + String(x.r.status).charAt(0) + "xx");
      stav.appendChild(el("strong", "", x.r.status + " " + (x.r.statusText || "")));
      stav.appendChild(el("span", "meta", " · " + ms + " ms · " + (x.r.headers.get("content-type") || "")));
      odpoved.appendChild(stav);
      var vypis = x.text;
      try { vypis = JSON.stringify(JSON.parse(x.text), null, 2); } catch (e) { /* není JSON */ }
      var pre = el("pre", "api-telo");
      pre.appendChild(el("code", "", vypis || T("(empty body)", "(prázdné tělo)")));
      odpoved.appendChild(pre);
    }).catch(function (e) {
      odpoved.textContent = "";
      odpoved.appendChild(el("p", "sql-chyba",
        T("The request failed (", "Požadavek selhal (") + e.message + T("). Either the network is down or the API does not allow calls from web pages (CORS). Try it in Postman.", "). Buď nefunguje síť, nebo API nepovoluje volání z webových stránek (CORS). Zkus to v Postmanu.")));
    });
  }

  posli.addEventListener("click", odesli);
  url.addEventListener("keydown", function (u) { if (u.key === "Enter") odesli(); });
})();
