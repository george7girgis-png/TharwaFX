// TharwaFx public site: navigation, banners, toggles, forms, calculators,
// glossary and search. No dependencies; every feature checks for its markup.
(function () {
  "use strict";
  var doc = document.documentElement;
  var AR = doc.lang === "ar";
  var page = document.body.getAttribute("data-page") || "";
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var L = AR ? {
    soon: "قريباً. سيُضاف هذا الرابط قبل الإطلاق.",
    thanks: "شكراً على ملاحظتك.",
    required: "هذا الحقل مطلوب.",
    email: "أدخل بريداً إلكترونياً كاملاً.",
    demoDone: "تم استلام طلبك. ستصلك تفاصيل الدخول إلى الحساب التجريبي على بريدك الإلكتروني.",
    contactDone: "وصلت رسالتك. سيرد عليك فريقنا قريباً.",
    margin: "الهامش", pip: "قيمة النقطة", swap: "التبييت", profit: "الربح", currency: "العملات",
    marginReq: "الهامش المطلوب", contract: "قيمة العقد", pipValue: "قيمة النقطة", swapCost: "تكلفة التبييت",
    result: "الربح أو الخسارة", converted: "المبلغ المحوّل", note: "التقديرات تستخدم أسعاراً نموذجية وقد تختلف القيم الفعلية.",
    acc: "عملة الحساب", inst: "الأداة", lots: "اللوتات", lev: "الرافعة", nights: "عدد الليالي", side: "الاتجاه",
    buy: "شراء", sell: "بيع", open: "سعر الفتح", close: "سعر الإغلاق", amount: "المبلغ", from: "من", to: "إلى", calc: "احسب",
    perNight: "لكل ليلة", none: "لا توجد نتائج لـ", results: "نتيجة", resultsFor: "نتائج البحث عن"
  } : {
    soon: "Coming soon. This link will be added before launch.",
    thanks: "Thanks for your feedback.",
    required: "This field is required.",
    email: "Enter a full email address.",
    demoDone: "Request received. Your demo login details will arrive by email.",
    contactDone: "Message received. Our team will reply soon.",
    margin: "Margin", pip: "Pip value", swap: "Swap", profit: "Profit", currency: "Currency",
    marginReq: "Margin required", contract: "Contract value", pipValue: "Pip value", swapCost: "Swap cost",
    result: "Profit or loss", converted: "Converted amount", note: "Estimates use sample prices. Live values can differ.",
    acc: "Account currency", inst: "Instrument", lots: "Lots", lev: "Leverage", nights: "Nights held", side: "Direction",
    buy: "Buy", sell: "Sell", open: "Open price", close: "Close price", amount: "Amount", from: "From", to: "To", calc: "Calculate",
    perNight: "per night", none: "No results for", results: "results", resultsFor: "Results for"
  };

  // ---------------------------------------------------------------- toast
  var toastEl = $("#toast"), toastTimer;
  function toast(msg) {
    if (!toastEl) return;
    toastEl.textContent = msg;
    toastEl.hidden = false;
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { toastEl.hidden = true; }, 3200);
  }
  document.addEventListener("click", function (e) {
    var soon = e.target.closest("[data-soon]");
    if (soon) { e.preventDefault(); toast(L.soon); }
    var fb = e.target.closest("[data-feedback]");
    if (fb) { fb.parentNode.innerHTML = '<span class="sm mut">' + L.thanks + "</span>"; }
  });

  // ---------------------------------------------------------------- header
  var triggers = $$(".nav-t");
  function closeMega(except) {
    triggers.forEach(function (t) {
      if (t === except) return;
      t.setAttribute("aria-expanded", "false");
      var p = document.getElementById(t.getAttribute("aria-controls"));
      if (p) p.hidden = true;
    });
  }
  function openMega(t) {
    closeMega(t);
    t.setAttribute("aria-expanded", "true");
    document.getElementById(t.getAttribute("aria-controls")).hidden = false;
  }
  var hoverTimer;
  triggers.forEach(function (t) {
    t.addEventListener("click", function () {
      t.getAttribute("aria-expanded") === "true" ? closeMega() : openMega(t);
    });
    t.parentNode.addEventListener("mouseenter", function () {
      if (!matchMedia("(hover:hover)").matches) return;
      clearTimeout(hoverTimer);
      hoverTimer = setTimeout(function () { openMega(t); }, 90);
    });
  });
  var nav = $("#nav");
  if (nav) {
    nav.addEventListener("mouseleave", function () { clearTimeout(hoverTimer); if (matchMedia("(hover:hover)").matches) closeMega(); });
    $$(".mega").forEach(function (m) { m.addEventListener("mouseenter", function () { clearTimeout(hoverTimer); }); });
  }
  document.addEventListener("keydown", function (e) {
    if (e.key !== "Escape") return;
    var open = triggers.filter(function (t) { return t.getAttribute("aria-expanded") === "true"; })[0];
    closeMega();
    if (open) open.focus();
    setDrawer(false);
  });
  document.addEventListener("click", function (e) { if (!e.target.closest("#nav")) closeMega(); });

  var burger = $(".burger:not(.app-burger)"), drawer = $("#drawer");
  function setDrawer(on) {
    if (!burger || !drawer) return;
    burger.setAttribute("aria-expanded", on ? "true" : "false");
    drawer.hidden = !on;
    document.body.classList.toggle("lock", on);
  }
  if (burger && drawer) burger.addEventListener("click", function () { setDrawer(drawer.hidden); });

  // ---------------------------------------------------------------- cookies
  var cookie = $("#cookie"), consent = null;
  try { consent = localStorage.getItem("tfx-consent"); } catch (e) {}
  if (cookie && !consent) cookie.hidden = false;
  $$("[data-cookie]").forEach(function (b) {
    b.addEventListener("click", function () {
      try { localStorage.setItem("tfx-consent", b.getAttribute("data-cookie")); } catch (e) {}
      cookie.hidden = true;
    });
  });

  // ---------------------------------------------------------------- toggles
  function group(selector, onChange) {
    $$(selector).forEach(function (wrap) {
      var btns = $$(":scope > button:not([type=submit]):not([data-act])", wrap);
      btns.forEach(function (b) {
        b.addEventListener("click", function () {
          btns.forEach(function (x) { x.classList.toggle("on", x === b); x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
          if (onChange) onChange(b, wrap);
        });
      });
    });
  }
  // Spreads page: filter rows by asset class.
  var CAT = { EURUSD: "Forex", GBPUSD: "Forex", USDJPY: "Forex", AUDUSD: "Forex", USDCHF: "Forex", USDAED: "Forex",
    XAUUSD: "Metals", XAGUSD: "Metals", US30: "Indices", US500: "Indices", NAS100: "Indices", USOIL: "Energy", UKOIL: "Energy", BTCUSD: "Crypto", ETHUSD: "Crypto" };
  group(".row:not([data-letters])", function (b, wrap) {
    if (page !== "P12" || !b.classList.contains("pill")) return;
    var want = b.textContent.trim();
    var table = wrap.closest(".wrap").querySelector("table");
    $$("tr", table).slice(1).forEach(function (tr) {
      var sym = tr.querySelector("b.mono");
      tr.hidden = want !== "All" && sym && CAT[sym.textContent.trim()] !== want;
    });
  });
  group(".seg");
  group(".tabs");

  // ---------------------------------------------------------------- forms
  function validate(form) {
    var ok = true;
    $$(".err-t", form).forEach(function (n) { n.remove(); });
    $$("[required]", form).forEach(function (f) {
      var bad = !f.value.trim() || (f.type === "email" && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(f.value.trim()));
      f.setAttribute("aria-invalid", bad ? "true" : "false");
      if (bad) {
        var msg = document.createElement("span");
        msg.className = "err-t";
        msg.id = f.id + "-err";
        msg.textContent = f.value.trim() ? L.email : L.required;
        f.setAttribute("aria-describedby", msg.id);
        f.parentNode.appendChild(msg);
        if (ok) f.focus();
        ok = false;
      }
    });
    return ok;
  }
  $$("form[data-form]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!validate(form)) return;
      // No backend yet: the client area (phase B) will receive these submissions.
      var kind = form.getAttribute("data-form");
      form.innerHTML = '<div class="done"><div class="ok" aria-hidden="true">✓</div><h3>' +
        (kind === "demo" ? (AR ? "تم" : "You are all set") : (AR ? "شكراً لك" : "Thank you")) +
        '</h3><p class="mut sm mt8">' + (kind === "demo" ? L.demoDone : L.contactDone) + "</p></div>";
    });
  });

  // ---------------------------------------------------------------- calculators
  var calcForm = $("form[data-calc]");
  if (calcForm) {
    fetch("/assets/instruments.json").then(function (r) { return r.json(); }).then(function (D) { calculators(calcForm, D); });
  }
  var FX = { USD: 1, EUR: 1 / 1.16695, GBP: 1 / 1.32588, AED: 3.6725, JPY: 152.418, CHF: 0.88341, AUD: 1 / 0.65912 };
  function num(v) { return parseFloat(String(v).replace(/[^0-9.\-]/g, "")) || 0; }
  function money(v, cur) {
    var sign = v < 0 ? "−" : "";
    var s = Math.abs(v).toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
    return sign + (cur === "USD" ? "$" + s : s + " " + cur);
  }
  function toUSD(amount, quote, price) {
    // Quote-currency amount to USD using sample rates.
    if (quote === "USD") return amount;
    return amount / (FX[quote] || price);
  }
  function contractUSD(sym, d, lots, price) {
    if (d.q === "USD") return price * d.c * lots;
    if (sym.indexOf("USD") === 0) return d.c * lots;
    return toUSD(price * d.c * lots, d.q, price);
  }
  function calculators(form, D) {
    var syms = Object.keys(D);
    if (page === "P13") {
      var go13 = function () {
        var s = form.querySelector("select[name=instrument]").value;
        var lots = num(form.querySelector("input[name=lots]").value);
        var lev = num(form.querySelector("select[name=leverage]").value.split(":")[1]);
        var d = D[s] || D.EURUSD;
        var cv = contractUSD(s, d, lots, s === "EURUSD" ? 1.16692 : d.p);
        form.querySelector("[data-calc-margin]").textContent = money(cv / lev, "USD");
      };
      form.addEventListener("input", go13);
      form.addEventListener("change", go13);
      form.addEventListener("submit", function (e) { e.preventDefault(); go13(); });
      return;
    }
    var out = $("[data-calc-out]");
    var tabs = $$(".tabs button");
    var modes = ["margin", "pip", "swap", "profit", "currency"];
    var mode = "margin";
    var state = { acc: "USD", sym: "XAUUSD", lots: "0.50", lev: "1:200", nights: "1", side: "buy", open: "", close: "", amount: "1000", from: "USD", to: "AED" };
    function sel(name, label, opts, val) {
      return '<div class="f"><label for="c-' + name + '">' + label + '</label><select class="i" id="c-' + name + '" name="' + name + '">' +
        opts.map(function (o) { var v = o[0] || o, t = o[1] || o; return "<option value=\"" + v + "\"" + (v === val ? " selected" : "") + ">" + t + "</option>"; }).join("") + "</select></div>";
    }
    function inp(name, label, val) {
      return '<div class="f"><label for="c-' + name + '">' + label + '</label><input class="i" id="c-' + name + '" name="' + name + '" inputmode="decimal" value="' + val + '" dir="ltr"></div>';
    }
    var curs = ["USD", "EUR", "AED", "GBP"];
    var levs = ["1:500", "1:400", "1:200", "1:100", "1:50", "1:30"];
    function render() {
      var d = D[state.sym];
      if (!state.open) state.open = String(d.p);
      if (!state.close) state.close = String(+(d.p * 1.005).toPrecision(6));
      var h = "";
      if (mode === "currency") {
        h = inp("amount", L.amount, state.amount) + '<div class="g2">' + sel("from", L.from, Object.keys(FX), state.from) + sel("to", L.to, Object.keys(FX), state.to) + "</div>";
      } else {
        h = sel("acc", L.acc, curs, state.acc) + sel("sym", L.inst, syms, state.sym) + '<div class="g2">' + inp("lots", L.lots, state.lots);
        if (mode === "margin") h += sel("lev", L.lev, levs, state.lev);
        if (mode === "swap") h += inp("nights", L.nights, state.nights);
        if (mode === "profit") h += sel("side", L.side, [["buy", L.buy], ["sell", L.sell]], state.side);
        h += "</div>";
        if (mode === "swap") h += sel("side", L.side, [["buy", L.buy], ["sell", L.sell]], state.side);
        if (mode === "profit") h += '<div class="g2">' + inp("open", L.open, state.open) + inp("close", L.close, state.close) + "</div>";
      }
      h += '<button type="submit" class="b p w">' + L.calc + "</button>";
      form.innerHTML = h;
      compute();
    }
    function read() {
      $$("[name]", form).forEach(function (f) {
        var k = f.name;
        if (k === "sym" && f.value !== state.sym) { state.open = ""; state.close = ""; }
        state[k] = f.value;
      });
    }
    function rows(list) {
      return list.map(function (r) { return '<div class="row sb"><span class="mut">' + r[0] + '</span><span class="mono">' + r[1] + "</span></div>"; }).join("");
    }
    function compute() {
      var d = D[state.sym], lots = num(state.lots), acc = state.acc, conv = FX[acc] || 1;
      var pipUSD = toUSD(d.pip * d.c * lots, d.q, d.p);
      var cvUSD = contractUSD(state.sym, d, lots, d.p);
      var big, label, extra = [];
      if (mode === "margin") {
        var lev = num(state.lev.split(":")[1]) || 1;
        label = L.marginReq; big = cvUSD / lev * conv;
        extra = [[L.contract, money(cvUSD * conv, acc)], [L.pipValue, money(pipUSD * conv, acc)]];
      } else if (mode === "pip") {
        label = L.pipValue; big = pipUSD * conv;
        extra = [[L.contract, money(cvUSD * conv, acc)]];
      } else if (mode === "swap") {
        var rate = state.side === "buy" ? d.sl : d.ss;
        label = L.swapCost; big = rate * lots * num(state.nights) * conv;
        extra = [[L.swap + ", " + L.perNight, money(rate * lots * conv, acc)]];
      } else if (mode === "profit") {
        var diff = (num(state.close) - num(state.open)) * (state.side === "buy" ? 1 : -1);
        label = L.result; big = toUSD(diff * d.c * lots, d.q, num(state.close) || d.p) * conv;
        extra = [[L.contract, money(cvUSD * conv, acc)]];
      } else {
        label = L.converted; acc = state.to;
        big = num(state.amount) / (FX[state.from] || 1) * (FX[state.to] || 1);
        extra = [["1 " + state.from, (FX[state.to] / FX[state.from]).toFixed(4) + " " + state.to]];
      }
      out.innerHTML = '<div class="sm mut">' + label + '</div><div class="stat mono ' + (big < 0 ? "red" : "grn") + ' mt8" style="font-size:52px">' + money(big, acc) + "</div>" +
        '<div class="col gap8 mt24 sm">' + rows(extra) + '</div><p class="xs mut3 mt24">' + L.note + "</p>";
    }
    tabs.forEach(function (t, i) {
      t.addEventListener("click", function () { read(); mode = modes[i]; render(); });
    });
    form.addEventListener("submit", function (e) { e.preventDefault(); read(); compute(); });
    form.addEventListener("change", function (e) { read(); if (e.target.name === "sym") render(); else compute(); });
    form.addEventListener("input", function () { read(); compute(); });
    render();
  }

  // ---------------------------------------------------------------- access pages
  // Front-end only: nothing is sent; each step moves on to the next screen.
  var authForm = $("form[data-auth]");
  function base() { return AR ? "/ar" : "/en"; }
  function go(path) { location.href = base() + path + "/"; }
  function remember(key, val) { try { sessionStorage.setItem(key, val); } catch (e) {} }
  function recall(key) { try { return sessionStorage.getItem(key); } catch (e) { return null; } }
  function fieldError(f, msg) {
    var e = document.createElement("span");
    e.className = "err-t"; e.id = (f.id || f.name) + "-err"; e.textContent = msg;
    f.setAttribute("aria-invalid", "true");
    f.setAttribute("aria-describedby", e.id);
    (f.closest(".f") || f.closest(".chk").parentNode).appendChild(e);
  }
  // One-digit code boxes: type, paste, backspace.
  function otp(scope) {
    var digits = $$(".otp input", scope);
    digits.forEach(function (d, i) {
      d.addEventListener("input", function () {
        d.value = d.value.replace(/\D/g, "").slice(-1);
        if (d.value && digits[i + 1]) digits[i + 1].focus();
      });
      d.addEventListener("keydown", function (e) {
        if (e.key === "Backspace" && !d.value && digits[i - 1]) digits[i - 1].focus();
      });
      d.addEventListener("paste", function (e) {
        var t = (e.clipboardData || window.clipboardData).getData("text").replace(/\D/g, "").slice(0, 6);
        if (!t) return;
        e.preventDefault();
        t.split("").forEach(function (c, k) { if (digits[k]) digits[k].value = c; });
        digits[Math.min(t.length, 5)].focus();
      });
    });
    if (digits.length) digits[0].focus();
    return digits;
  }
  function access(form, kind) {
    var A = AR ? {
      pass: "استخدم 10 أحرف على الأقل، مع رقم ورمز.", terms: "يجب الموافقة على اتفاقية العميل وإفصاح المخاطر.",
      code: "أدخل الرمز المكوّن من 6 أرقام.", show: "إظهار كلمة المرور", hide: "إخفاء كلمة المرور", resend: "أعد الإرسال", resendIn: "أعد الإرسال خلال ",
      sent: "أرسلنا رمزاً جديداً.", verified: "تم التحقق من بريدك", signed: "تم تسجيل الدخول"
    } : {
      pass: "Use at least 10 characters, with a number and a symbol.", terms: "Please accept the client agreement and risk disclosure.",
      code: "Enter the 6-digit code.", show: "Show password", hide: "Hide password", resend: "Resend code", resendIn: "Resend in ",
      sent: "We sent a new code.", verified: "Email verified", signed: "You are signed in"
    };
    // Password visibility.
    $$(".pw-t", form).forEach(function (b) {
      b.addEventListener("click", function () {
        var i = b.parentNode.querySelector("input"), show = i.type === "password";
        i.type = show ? "text" : "password";
        b.setAttribute("aria-pressed", show ? "true" : "false");
        b.setAttribute("aria-label", show ? A.hide : A.show);
      });
    });
    // Live or demo on the register page: demo has its own sign-up form.
    $$(".seg button", form).forEach(function (b, i) {
      b.addEventListener("click", function () { if (i === 1) location.href = "/en/demo/"; });
    });
    var digits = otp(form);
    var shown = $("[data-email]", form), email = recall("tfx-email");
    if (shown && email) shown.textContent = email.replace(/^(.)(.*)(.@.*)$/, function (m, a, mid, b) { return a + mid.replace(/./g, "•") + b; });
    // Resend countdown.
    var resend = $("[data-resend]", form), timer;
    function countdown() {
      var left = 45;
      resend.disabled = true;
      clearInterval(timer);
      timer = setInterval(function () {
        left--;
        resend.innerHTML = A.resendIn + '<span class="mono">0:' + String(left).padStart(2, "0") + "</span>";
        if (left <= 0) { clearInterval(timer); resend.disabled = false; resend.textContent = A.resend; }
      }, 1000);
    }
    if (resend) {
      countdown();
      resend.addEventListener("click", function () { toast(A.sent); countdown(); });
    }
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      $$(".err-t", form).forEach(function (n) { n.remove(); });
      $$("[aria-invalid]", form).forEach(function (n) { n.removeAttribute("aria-invalid"); });
      var bad = [];
      $$("input[type=email]", form).forEach(function (f) {
        if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(f.value.trim())) { fieldError(f, f.value.trim() ? L.email : L.required); bad.push(f); }
      });
      $$("input[name=password]", form).forEach(function (f) {
        var weak = kind === "register" && !(f.value.length >= 10 && /\d/.test(f.value) && /[^A-Za-z0-9]/.test(f.value));
        if (!f.value || weak) { fieldError(f, f.value ? A.pass : L.required); bad.push(f); }
      });
      $$("input[name=terms]", form).forEach(function (f) { if (!f.checked) { fieldError(f, A.terms); bad.push(f); } });
      if (digits.length && !/^\d{6}$/.test(digits.map(function (d) { return d.value; }).join(""))) {
        var otp = $(".otp", form), m = document.createElement("span");
        otp.setAttribute("aria-invalid", "true");
        m.className = "err-t"; m.textContent = A.code;
        otp.parentNode.insertBefore(m, otp.nextSibling);
        bad.push(digits.filter(function (d) { return !d.value; })[0] || digits[0]);
      }
      if (bad.length) { bad[0].focus(); return; }
      var em = $("input[type=email]", form);
      if (em) remember("tfx-email", em.value.trim());
      if (kind === "register") go("/verify-email");
      else if (kind === "login") go("/login/2fa");
      else if (kind === "verify") { remember("tfx-flash", A.verified); location.href = base() + "/client/onboarding/details/"; }
      else if (kind === "2fa") { remember("tfx-flash", A.signed); location.href = base() + "/client/home/"; }
      else if (kind === "recover") $("[data-sent]", form).hidden = false;
    });
  }
  if (authForm) access(authForm, authForm.getAttribute("data-auth"));

  // ---------------------------------------------------------------- live sample board
  var board = $$(".qt tr").slice(1);
  if (board.length && !matchMedia("(prefers-reduced-motion: reduce)").matches) {
    setInterval(function () {
      if (document.hidden) return;
      var tr = board[Math.floor(Math.random() * board.length)];
      var cells = $$("td.num", tr);
      if (cells.length < 2) return;
      var bid = cells[0].textContent.replace(/,/g, ""), dec = (bid.split(".")[1] || "").length;
      var step = Math.pow(10, -dec) * (1 + Math.floor(Math.random() * 4)) * (Math.random() < 0.5 ? -1 : 1);
      [0, 1].forEach(function (i) {
        var v = parseFloat(cells[i].textContent.replace(/,/g, "")) + step;
        cells[i].textContent = v.toLocaleString("en-US", { minimumFractionDigits: dec, maximumFractionDigits: dec });
        cells[i].classList.remove("up", "dn");
        void cells[i].offsetWidth;
        cells[i].classList.add(step > 0 ? "up" : "dn");
      });
    }, 1400);
  }

  // ---------------------------------------------------------------- glossary
  var gform = $("form[data-filter=glossary]");
  if (gform) {
    var terms = $$("[data-terms] .term"), empty = $("[data-empty]"), chips = $$("[data-letters] .chip");
    var filter = function (q, letter) {
      var n = 0;
      terms.forEach(function (t) {
        var txt = t.textContent.toLowerCase(), term = t.querySelector("b").textContent;
        var show = letter ? term.charAt(0) === letter : txt.indexOf(q) > -1;
        t.hidden = !show; if (show) n++;
      });
      empty.hidden = n > 0;
    };
    var input = gform.querySelector("input");
    gform.addEventListener("submit", function (e) { e.preventDefault(); });
    input.addEventListener("input", function () {
      chips.forEach(function (c) { c.classList.remove("on"); });
      filter(input.value.trim().toLowerCase());
    });
    chips.forEach(function (c) {
      c.addEventListener("click", function () {
        var on = !c.classList.contains("on");
        chips.forEach(function (x) { x.classList.toggle("on", on && x === c); });
        input.value = "";
        filter("", on ? c.getAttribute("data-letter") : "");
      });
    });
  }

  // ---------------------------------------------------------------- search
  var results = $("[data-results]");
  var q = new URLSearchParams(location.search).get("q");
  if (results && !q) {
    var sh1 = $(".hero h1"), slead = $(".hero .lead");
    if (sh1) sh1.textContent = AR ? "ابحث في الموقع" : "Search the site";
    if (slead) slead.textContent = AR ? "ابحث في الحسابات والأسواق والمساعدة." : "Find accounts, markets, pricing and help.";
    results.innerHTML = "";
  }
  if (results && q) {
    var esc = function (s) { return s.replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); };
    fetch("/assets/search.json").then(function (r) { return r.json(); }).then(function (idx) {
      var words = q.toLowerCase().split(/\s+/).filter(Boolean);
      var hits = idx.filter(function (p) {
        var hay = (p.t + " " + p.d + " " + p.u).toLowerCase();
        return p.l === (AR ? "ar" : "en") || p.l === "en" ? words.every(function (w) { return hay.indexOf(w) > -1; }) : false;
      }).slice(0, 30);
      var h1 = $(".hero h1"), lead = $(".hero .lead");
      if (h1) h1.textContent = L.resultsFor + " “" + q + "”";
      if (lead) lead.textContent = hits.length + " " + L.results;
      results.innerHTML = hits.length ? hits.map(function (p) {
        return '<a href="' + p.u + '" style="display:block;padding:18px 0;border-bottom:1px solid var(--gr)"><div class="xs grn">' +
          esc(p.u.split("/")[2] || "home") + '</div><b class="mt8" style="display:block">' + esc(p.t) + '</b><p class="sm mut mt8">' + esc(p.d) + "</p></a>";
      }).join("") : '<p class="mut">' + L.none + " “" + esc(q) + "”.</p>";
      $$("form[role=search] input").forEach(function (i) { i.value = q; });
    });
  }

  // ---------------------------------------------------------------- client area
  // Front-end only, with the book's sample client. Each form validates, then moves to the next
  // screen or confirms in place; nothing is stored or sent.
  var app = $(".app"), flowForm = $("form[data-flow]");
  var C = AR ? {
    required: "هذا الحقل مطلوب.", choose: "اختر خياراً.", file: "أرفق ملفاً.", code: "أدخل الرمز المكوّن من 6 أرقام.",
    amount: "أدخل مبلغاً صحيحاً.", min: "الحد الأدنى ", max: "الحد الأقصى ", avail: "المبلغ أكبر من الرصيد المتاح.",
    transferred: "تم التحويل بين حساباتك.", saved: "تم حفظ التغييرات.", created: "تم فتح الحساب الجديد.", added: "أضفنا الحساب البنكي، وسنراجعه خلال يوم عمل.",
    confirmed: "تم تأكيد طلب السحب.", read: "تم تعليم الكل كمقروء.", reset: "أرسلنا رابط إعادة تعيين كلمة مرور المنصة إلى بريدك.",
    signedOut: "تم تسجيل خروج الجهاز.", signedOutAll: "تم تسجيل الخروج من الأجهزة الأخرى.", uploaded: "استلمنا الملف وسنراجعه.",
    twofa: "تم تفعيل التحقق بخطوتين.", submitted: "استلمنا وثائقك.", you: "أنت، الآن", pay: "ادفع "
  } : {
    required: "This field is required.", choose: "Choose an option.", file: "Attach a file.", code: "Enter the 6-digit code.",
    amount: "Enter a valid amount.", min: "The minimum is ", max: "The maximum is ", avail: "That is more than your available balance.",
    transferred: "Transfer done between your accounts.", saved: "Changes saved.", created: "Your new account is open.", added: "Bank account added. We check it within 1 business day.",
    confirmed: "Withdrawal confirmed.", read: "All marked as read.", reset: "We emailed you a link to reset the platform password.",
    signedOut: "That device is signed out.", signedOutAll: "Other devices are signed out.", uploaded: "File received. We will review it.",
    twofa: "Two-step login is on.", submitted: "Documents received.", you: "You, just now", pay: "Pay "
  };
  function clientUrl(path) { return (AR ? "/ar" : "/en") + path + "/"; }
  function flash(msg, path) { try { sessionStorage.setItem("tfx-flash", msg); } catch (e) {} location.href = clientUrl(path); }
  try {
    var waiting = sessionStorage.getItem("tfx-flash");
    if (waiting) { sessionStorage.removeItem("tfx-flash"); setTimeout(function () { toast(waiting); }, 300); }
  } catch (e) {}

  if (app) {
    // Sidebar becomes a drawer on small screens.
    var sd = $("#sd"), veil = $(".sd-veil"), sideBtn = $(".app-burger");
    var setSide = function (open) {
      sd.classList.toggle("open", open);
      veil.hidden = !open;
      sideBtn.setAttribute("aria-expanded", open ? "true" : "false");
      document.body.style.overflow = open ? "hidden" : "";
    };
    sideBtn.addEventListener("click", function () { setSide(!sd.classList.contains("open")); });
    veil.addEventListener("click", function () { setSide(false); });
    // Avatar menu.
    var meB = $(".me-b"), meM = $("#me-m");
    meB.addEventListener("click", function (e) {
      e.stopPropagation();
      meM.hidden = !meM.hidden;
      meB.setAttribute("aria-expanded", meM.hidden ? "false" : "true");
    });
    doc.addEventListener("click", function (e) { if (!meM.hidden && !e.target.closest(".me")) { meM.hidden = true; meB.setAttribute("aria-expanded", "false"); } });
    doc.addEventListener("keydown", function (e) {
      if (e.key !== "Escape") return;
      if (!meM.hidden) { meM.hidden = true; meB.focus(); }
      if (sd.classList.contains("open")) { setSide(false); sideBtn.focus(); }
    });
    $$("[data-signout]").forEach(function (a) {
      a.addEventListener("click", function () { try { sessionStorage.removeItem("tfx-email"); } catch (e) {} });
    });
    // Table rows that open a detail screen.
    $$("tr[data-href]").forEach(function (tr) {
      tr.addEventListener("click", function () { location.href = tr.getAttribute("data-href"); });
      tr.addEventListener("keydown", function (e) { if (e.key === "Enter") location.href = tr.getAttribute("data-href"); });
    });
  }

  // Deposit result: one outcome at a time (?status=pending or failed shows the others).
  var states = $$("[data-state]");
  if (states.length) {
    var want = new URLSearchParams(location.search).get("status") || "completed";
    states.forEach(function (c) { c.hidden = c.getAttribute("data-state") !== want; });
    states[0].parentNode.classList.add("one");
  }

  function amountOf(input) { return parseFloat(String(input.value).replace(/[^0-9.]/g, "")); }
  function money(n) { return "$" + n.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 }); }

  function clientFlow(form, sid) {
    // Radios keep the book's .on styling in step with the real input.
    $$(".rad input", form).forEach(function (r) {
      r.addEventListener("change", function () {
        $$('input[name="' + r.name + '"]', form).forEach(function (x) { x.closest(".rad").classList.toggle("on", x.checked); });
      });
    });
    var digits = $(".otp", form) ? otp(form) : [];
    $$("input[type=file]", form).forEach(function (f) {
      f.addEventListener("change", function () {
        var out = $("[data-file]", f.closest("label"));
        if (out) out.textContent = f.files.length ? "✓ " + f.files[0].name : "";
      });
    });
    var amount = $("input.amt", form);
    // Quick amounts and the live "Pay" label on the deposit amount screen.
    var pay = $$("button[type=submit]", form).filter(function (b) { return /^(Pay|ادفع) /.test(b.textContent); })[0];
    var syncPay = function () { if (pay) { var n = amountOf(amount); pay.textContent = C.pay + money(n > 0 ? n : 0); } };
    if (amount) {
      $$(".pill", form).forEach(function (p) {
        if (!/^\$[\d,]+$/.test(p.textContent.trim())) return;
        p.addEventListener("click", function () { amount.value = p.textContent.replace(/[^0-9]/g, "") + ".00"; syncPay(); });
      });
      amount.addEventListener("input", syncPay);
    }
    // Transactions: filter by type.
    if (sid === "A13") {
      $$(".pill", form).slice(0, 4).forEach(function (p, i) {
        p.addEventListener("click", function () {
          var type = ["", "deposit", "withdrawal", "transfer"][i];
          $$("tr[data-href]", form).forEach(function (tr) { tr.hidden = !!type && tr.getAttribute("data-type") !== type; });
        });
      });
    }
    // Buttons that act in place.
    form.addEventListener("click", function (e) {
      var b = e.target.closest("[data-act]");
      if (!b) return;
      var act = b.getAttribute("data-act");
      if (act === "cancel") location.href = clientUrl("/client/withdraw");
      else if (act === "reset") toast(C.reset);
      else if (act === "sign-out") { b.closest("tr").remove(); toast(C.signedOut); }
      else if (act === "sign-out-everywhere") { $$("[data-act=sign-out]", form).forEach(function (x) { x.closest("tr").remove(); }); toast(C.signedOutAll); }
      else if (act === "mark-all-as-read") { $$(".card .row.sb b", form).forEach(function (x) { x.style.fontWeight = "500"; }); toast(C.read); }
      else if (act === "download-receipt") window.print();
      else if (act === "upload-again") {
        var pick = document.createElement("input");
        pick.type = "file"; pick.accept = ".jpg,.jpeg,.png,.pdf";
        pick.addEventListener("change", function () { if (pick.files.length) toast(C.uploaded); });
        pick.click();
      } else if (act === "export-csv") {
        var csv = $$("tr", form).filter(function (tr) { return !tr.hidden; }).map(function (tr) {
          return $$("th,td", tr).map(function (c) { return '"' + c.textContent.trim().replace(/"/g, '""') + '"'; }).join(",");
        }).join("\r\n");
        var a = document.createElement("a");
        a.href = URL.createObjectURL(new Blob(["﻿" + csv], { type: "text/csv" }));
        a.download = "tharwafx-transactions.csv";
        a.click();
      }
    });
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      $$(".err-t", form).forEach(function (n) { n.remove(); });
      $$("[aria-invalid]", form).forEach(function (n) { n.removeAttribute("aria-invalid"); });
      var bad = [];
      function err(f, msg, after) {
        var m = document.createElement("span");
        m.className = "err-t"; m.textContent = msg;
        if (f.id) { m.id = f.id + "-err"; f.setAttribute("aria-describedby", m.id); }
        f.setAttribute("aria-invalid", "true");
        (after || f.closest(".f") || f.parentNode).appendChild(m);
        bad.push(f);
      }
      $$("input.i, select.i, textarea.i", form).forEach(function (f) {
        if (!f.value.trim()) err(f, C.required);
        else if (f.name.indexOf("code") > -1 && !/^\d{6}$/.test(f.value.replace(/\s/g, ""))) err(f, C.code);
      });
      var seen = {};
      $$(".rad input", form).forEach(function (r) {
        if (seen[r.name]) return;
        seen[r.name] = true;
        if (!$('input[name="' + r.name + '"]:checked', form)) err(r, C.choose, r.closest(".rad").parentNode);
      });
      $$(".chk input[required]", form).forEach(function (c) { if (!c.checked) err(c, C.required, c.closest(".chk").parentNode); });
      $$("input[type=file][required]", form).forEach(function (f) { if (!f.files.length) err(f, C.file, f.closest("label")); });
      if (digits.length && !/^\d{6}$/.test(digits.map(function (d) { return d.value; }).join(""))) {
        var box = $(".otp", form), m = document.createElement("span");
        box.setAttribute("aria-invalid", "true");
        m.className = "err-t"; m.textContent = C.code;
        box.parentNode.insertBefore(m, box.nextSibling);
        bad.push(digits.filter(function (d) { return !d.value; })[0] || digits[0]);
      }
      if (amount && amount.value.trim()) {
        var n = amountOf(amount), limit = { A07: [50, 10000], A09: [1, 11902.10], A12: [1, 11902.10] }[sid];
        if (!(n > 0)) err(amount, C.amount);
        else if (limit && n < limit[0]) err(amount, C.min + money(limit[0]) + ".");
        else if (limit && n > limit[1]) err(amount, sid === "A07" ? C.max + money(limit[1]) + "." : C.avail);
      }
      if (bad.length) { bad[0].focus(); return; }
      var next = { C06: "/client/onboarding/suitability", C07: "/client/onboarding/documents", A06: "/client/deposit/amount", A09: "/client/withdraw/wd-20391" }[sid];
      if (next) location.href = clientUrl(next);
      else if (sid === "C08") flash(C.submitted, "/client/welcome");
      else if (sid === "C09") flash(C.twofa, "/client/security");
      else if (sid === "A04") flash(C.created, "/client/accounts");
      else if (sid === "A07") location.href = clientUrl("/client/deposit/result") + "?status=completed";
      else if (sid === "A10") { toast(C.added); form.reset(); }
      else if (sid === "A12") toast(C.transferred + " " + money(amountOf(amount)));
      else if (sid === "A18") toast(C.saved);
      else if (sid === "A11") {
        var card = $("[name=email-code]", form).closest(".card"), ok = document.createElement("p");
        $$(".f, .row", card).forEach(function (x) { x.remove(); });
        ok.className = "grn"; ok.setAttribute("role", "status"); ok.textContent = "✓ " + C.confirmed;
        card.appendChild(ok);
      } else if (sid === "A21") {
        var reply = $("textarea", form), msg = document.createElement("div");
        msg.className = "card s";
        msg.style.cssText = "padding:14px 16px;margin-inline-start:auto;max-width:80%;background:var(--gs)";
        msg.innerHTML = '<p></p><div class="xs mut3 mt8"></div>';
        msg.querySelector("p").textContent = reply.value.trim();
        msg.querySelector("div").textContent = C.you;
        var lab = reply.previousElementSibling;
        reply.parentNode.insertBefore(msg, lab && lab.tagName === "LABEL" ? lab : reply);
        reply.value = "";
      }
    });
  }
  if (flowForm) clientFlow(flowForm, flowForm.getAttribute("data-flow"));

  // ---------------------------------------------------------------- ambient video
  // Decorative Higgsfield loops play only while on screen, and never with reduced motion.
  var clips = $$("video[data-ambient]");
  if (clips.length && !matchMedia("(prefers-reduced-motion: reduce)").matches && "IntersectionObserver" in window) {
    var start = function (v) {
      v.preload = "auto";
      var p = v.play();
      // A play() at page load can be refused before the clip is ready; try again once it can play.
      if (p) p.catch(function () { v.addEventListener("canplay", function () { if (v.inView) v.play().catch(function () {}); }, { once: true }); });
    };
    var watch = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        e.target.inView = e.isIntersecting;
        if (e.isIntersecting) start(e.target); else e.target.pause();
      });
    }, { rootMargin: "100px" });
    clips.forEach(function (v) {
      watch.observe(v);
      // Start what is already on screen without waiting for the first observer callback.
      var r = v.getBoundingClientRect();
      if (r.bottom > 0 && r.top < innerHeight) { v.inView = true; start(v); }
    });
    document.addEventListener("visibilitychange", function () {
      if (document.visibilityState === "visible") clips.forEach(function (v) { if (v.inView && v.paused) start(v); });
    });
  }

  // ---------------------------------------------------------------- trade with AI
  // Sample console: a rolling feed of the lines in the page, one new line every couple of seconds.
  var feed = $("[data-log]");
  if (feed) {
    var lines = $$("li", feed).map(function (li) { return { tag: li.getAttribute("data-tag"), text: li.textContent }; });
    var still = matchMedia("(prefers-reduced-motion: reduce)").matches, n = 0;
    var stamp = function () { var d = new Date(); return [d.getHours(), d.getMinutes(), d.getSeconds()].map(function (x) { return String(x).padStart(2, "0"); }).join(":"); };
    var add = function (animate) {
      var l = lines[n++ % lines.length], li = document.createElement("li");
      li.setAttribute("data-tag", l.tag);
      li.innerHTML = '<span class="ts mono"></span><span class="tag mono"></span><span class="tx"></span>';
      li.querySelector(".ts").textContent = stamp();
      li.querySelector(".tag").textContent = l.tag;
      feed.appendChild(li);
      while (feed.children.length > 6) feed.removeChild(feed.firstChild);
      var tx = li.querySelector(".tx");
      if (!animate) { tx.textContent = l.text; return; }
      li.classList.add("new");
      var i = 0, typing = setInterval(function () { i += 2; tx.textContent = l.text.slice(0, i); if (i >= l.text.length) clearInterval(typing); }, 18);
    };
    feed.innerHTML = "";
    for (var k = 0; k < 5; k++) add(false);
    if (!still) {
      setInterval(function () { if (document.visibilityState === "visible") add(true); }, 2200);
      setInterval(function () { $$("[data-meter]").forEach(function (m) { m.style.width = (35 + Math.random() * 50).toFixed(0) + "%"; }); }, 1600);
    }
  }

  // Scenario simulator: 1,000 monthly paths with a drawdown stop. The returns are made-up
  // illustration figures, stated on the page, never a forecast.
  var sim = $("[data-sim]");
  if (sim) {
    var PROFILES = [{ mu: 0.25, sigma: 2.5 }, { mu: 0.45, sigma: 4.5 }, { mu: 0.6, sigma: 7.5 }]; // % per month at 1% risk per trade
    var style = 1, seed = 7;
    var field = function (n) { return sim.querySelector('[name="' + n + '"]'); };
    var out = function (n, v) { sim.querySelector('[data-out="' + n + '"]').textContent = v; };
    var amountOf = function () { var v = 100 * Math.pow(1000, field("amount").value / 100), p = Math.pow(10, Math.floor(Math.log10(v)) - 1); return Math.round(v / p) * p; };
    var usd = function (x) { return "$" + Math.round(x).toLocaleString("en-US"); };
    var rng = function (s) { return function () { s |= 0; s = s + 0x6D2B79F5 | 0; var t = Math.imul(s ^ s >>> 15, 1 | s); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }; };
    var NS = "http://www.w3.org/2000/svg", chart = sim.querySelector("[data-chart]");
    var el = function (tag, attrs) { var e = document.createElementNS(NS, tag); for (var a in attrs) e.setAttribute(a, attrs[a]); return e; };

    var run = function () {
      var amount = amountOf(), risk = +field("risk").value, months = +field("months").value, stop = +field("stop").value / 100, news = field("news").checked;
      var p = PROFILES[style], mu = (p.mu - 0.1) * risk / 100, sigma = p.sigma * risk / 100;
      if (news) { sigma *= 0.9; mu *= 0.97; }
      out("amount", usd(amount)); out("risk", risk.toFixed(2) + "%"); out("stop", Math.round(stop * 100) + "%");
      out("months", months + " " + (months === 1 ? sim.getAttribute("data-unit-m1") : sim.getAttribute("data-unit-m")));
      var rand = rng(seed), N = 1000, paths = [], hits = 0;
      var normal = function () { var u = 1 - rand(), v = rand(); return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v); };
      for (var i = 0; i < N; i++) {
        var eq = amount, peak = amount, halted = false, row = [amount];
        for (var m = 1; m <= months; m++) {
          if (!halted) {
            eq *= Math.exp(mu - sigma * sigma / 2 + sigma * normal());
            peak = Math.max(peak, eq);
            if (eq <= peak * (1 - stop)) { eq = peak * (1 - stop); halted = true; hits++; }
          }
          row.push(eq);
        }
        paths.push(row);
      }
      var pct = function (arr, q) { var s = arr.slice().sort(function (a, b) { return a - b; }); return s[Math.min(s.length - 1, Math.floor(q * s.length))]; };
      var bands = [];
      for (var t = 0; t <= months; t++) { var col = paths.map(function (r) { return r[t]; }); bands.push([pct(col, 0.1), pct(col, 0.5), pct(col, 0.9)]); }
      var last = bands[months];
      [["bad", last[0]], ["mid", last[1]], ["good", last[2]]].forEach(function (k) {
        var d = k[1] - amount;
        sim.querySelector('[data-k="' + k[0] + '"]').textContent = usd(k[1]);
        var dd = sim.querySelector('[data-d="' + k[0] + '"]');
        dd.textContent = (d >= 0 ? "+" : "−") + usd(Math.abs(d)).replace("$", "$") + " (" + (d >= 0 ? "+" : "−") + Math.abs(d / amount * 100).toFixed(1) + "%)";
        dd.className = "xs mono " + (d >= 0 ? "grn" : "red");
      });
      sim.querySelector('[data-k="max"]').textContent = usd(amount * stop);
      sim.querySelector('[data-k="hit"]').textContent = (hits / N * 100).toFixed(1) + "%";
      sim.querySelector("[data-assume-out]").textContent = sim.getAttribute("data-assume")
        .replace("{mu}", (mu * 100).toFixed(2) + "%").replace("{sigma}", (sigma * 100).toFixed(1) + "%");

      // Chart: band of the middle 80%, the median, one sample path, the stop level and the start line.
      var W = 640, H = 260, pad = 8, floor = amount * (1 - stop);
      var pick = paths[Math.floor(rand() * N)];
      var lo = Math.min(floor, Math.min.apply(null, pick), bands.reduce(function (a, b) { return Math.min(a, b[0]); }, Infinity)) * 0.96;
      var hi = Math.max(Math.max.apply(null, pick), Math.max.apply(null, bands.map(function (b) { return b[2]; }))) * 1.03;
      var X = function (t) { return pad + (W - 2 * pad) * t / months; }, Y = function (v) { return H - pad - (H - 2 * pad) * (v - lo) / (hi - lo); };
      var line = function (vals) { return vals.map(function (v, t) { return (t ? "L" : "M") + X(t).toFixed(1) + " " + Y(v).toFixed(1); }).join(" "); };
      chart.innerHTML = "";
      for (var g = 1; g < 4; g++) chart.appendChild(el("line", { x1: 0, x2: W, y1: H * g / 4, y2: H * g / 4, class: "grid" }));
      chart.appendChild(el("line", { x1: 0, x2: W, y1: Y(amount), y2: Y(amount), class: "base" }));
      chart.appendChild(el("line", { x1: 0, x2: W, y1: Y(floor), y2: Y(floor), class: "stopl" }));
      var top = bands.map(function (b, t) { return X(t).toFixed(1) + " " + Y(b[2]).toFixed(1); }), bot = bands.map(function (b, t) { return X(t).toFixed(1) + " " + Y(b[0]).toFixed(1); }).reverse();
      chart.appendChild(el("path", { d: "M" + top.join(" L") + " L" + bot.join(" L") + " Z", class: "band" }));
      chart.appendChild(el("path", { d: line(bands.map(function (b) { return b[1]; })), class: "med" }));
      // The sample path draws in from the left behind a widening clip (dashes would break with non-scaling strokes).
      var clip = el("clipPath", { id: "sim-clip" }), wipe = el("rect", { x: 0, y: 0, width: W, height: H });
      clip.appendChild(wipe); chart.appendChild(clip);
      chart.appendChild(el("path", { d: line(pick), class: "one", "clip-path": "url(#sim-clip)" }));
      if (!matchMedia("(prefers-reduced-motion: reduce)").matches) {
        var t0 = performance.now();
        wipe.setAttribute("width", 0);
        requestAnimationFrame(function grow(now) { var k = Math.min(1, (now - t0) / 1200); wipe.setAttribute("width", W * (1 - Math.pow(1 - k, 3))); if (k < 1) requestAnimationFrame(grow); });
      }
    };
    $$("input", sim).forEach(function (i) { i.addEventListener("input", run); });
    $$("[data-style]", sim).forEach(function (b) { b.addEventListener("click", function () { style = +b.getAttribute("data-style"); run(); }); });
    sim.querySelector("[data-rerun]").addEventListener("click", function () { seed = Math.floor(Math.random() * 1e9); run(); });
    run();
  }
})();
