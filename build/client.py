"""Client area and onboarding pages (book screens A01 to A21, C06 to C10).

Front end only, with the book's sample client (Ahmed, accounts 8120 4471 and 8120 4502).
Forms validate and move through each flow; nothing is stored or sent. Called from build.py.
"""
import html
import re

import build as B
from client_ar import AR

ROUTES = {
    "A01": "/client/home", "A02": "/client/accounts", "A03": "/client/accounts/81204471",
    "A04": "/client/accounts/new", "A05": "/client/platforms", "A06": "/client/deposit",
    "A07": "/client/deposit/amount", "A08": "/client/deposit/result", "A09": "/client/withdraw",
    "A10": "/client/withdraw/methods", "A11": "/client/withdraw/wd-20391", "A12": "/client/transfer",
    "A13": "/client/transactions", "A14": "/client/transactions/tx-88412", "A15": "/client/statements",
    "A16": "/client/verification", "A17": "/client/security", "A18": "/client/profile",
    "A19": "/client/notifications", "A20": "/client/support", "A21": "/client/support/40213",
    "C06": "/client/onboarding/details", "C07": "/client/onboarding/suitability",
    "C08": "/client/onboarding/documents", "C09": "/client/security/2fa", "C10": "/client/welcome",
}
# The book draws home, deposit and withdraw in Arabic; the rest are translated from client_ar.AR.
AR_ROUTES = set(ROUTES.values())

# Sidebar items in book order, and which item each screen belongs to.
SIDEBAR = ["/client/home", "/client/accounts", "/client/deposit", "/client/withdraw", "/client/transfer",
           "/client/transactions", "/client/statements", "/client/platforms", "/client/verification",
           "/client/security", "/client/profile", "/client/notifications", "/client/support"]
SECTION = {"A03": "/client/accounts", "A04": "/client/accounts", "A07": "/client/deposit", "A08": "/client/deposit",
           "A10": "/client/withdraw", "A11": "/client/withdraw", "A14": "/client/transactions",
           "A21": "/client/support", "C09": "/client/security", "C10": "/client/home"}

ACTIONS = {
    "Deposit": "/client/deposit", "إيداع": "/client/deposit", "Withdraw": "/client/withdraw", "سحب": "/client/withdraw",
    "Trade": "/client/platforms", "تداول": "/client/platforms", "Open WebTrader": "/platforms/webtrader",
    "افتح WebTrader": "/platforms/webtrader", "Launch WebTrader": "/platforms/webtrader", "Launch": "/platforms/webtrader",
    "New account": "/client/accounts/new", "Details": "/client/accounts/81204471", "Start trading": "/client/platforms",
    "View transaction": "/client/transactions/tx-88412", "Try another method": "/client/deposit",
    "Get help": "/client/support", "Open demo": "/demo", "Set up": "/client/security/2fa",
    "Finish later": "/client/welcome", "New ticket": "/contact#message", "Make a deposit": "/client/deposit",
    "Continue verification": "/client/verification", "Download": "soon", "Reset password": "toast",
    "PDF": "soon", "Change": "soon",
}
PAGE_ACTIONS = {("A20", "Open"): "/client/support/40213", ("A05", "Open"): "soon", ("A17", "View"): "/client/security/2fa",
                ("A10", "View"): "soon"}
# Buttons that submit the screen's form.
SUBMITS = {"Continue", "متابعة", "Create account", "Turn on", "Submit for review", "Transfer", "Save changes",
           "Add account", "Send", "Confirm", "Mark all as read", "Upload again", "Export CSV", "Download receipt",
           "Sign out", "Sign out everywhere", "Cancel"}

OPTIONS = {
    "To account": ["8120 4471, USD", "8120 4502, AED"], "إلى الحساب": ["8120 4471, USD", "8120 4502, AED"],
    "From account": ["8120 4471, USD", "8120 4502, AED"], "من الحساب": ["8120 4471, USD", "8120 4502, AED"],
    "From": ["8120 4471, USD", "8120 4502, AED"], "To": ["8120 4502, AED", "8120 4471, USD"],
    "Account": ["8120 4471, Raw Spread", "8120 4502, Islamic", "5007 1183, Demo"],
    "Currency": ["USD", "AED", "EUR"], "Leverage": ["1:500", "1:200", "1:100", "1:50"],
    "Nationality": ["Emirati", "Saudi", "Qatari", "Kuwaiti", "Bahraini", "Omani", "Egyptian", "Jordanian", "Other"],
    "Source of funds": ["Salary", "Business income", "Savings", "Investments", "Inheritance", "Other"],
    "Annual income band": ["Choose a band", "Under $25,000", "$25,000 to $75,000", "$75,000 to $150,000", "Over $150,000"],
    "Language": ["English", "العربية"], "Time zone": ["Gulf time (GMT+4)", "GMT", "Riyadh (GMT+3)", "Cairo (GMT+2)"],
    "Type": ["Raw Spread", "Standard", "Islamic", "Demo"],
}


def screens():
    for m in re.finditer(r'<section class="pg" id="([AC]\d\d)-(en|ar)">', B.book):
        sid, lang = m.group(1), m.group(2)
        if sid not in ROUTES:
            continue
        root = B.book.find(f'<div dir="{"rtl" if lang == "ar" else "ltr"}" lang="{lang}">', m.end())
        body = B.book[root:B.div_end(B.book, root)]
        yield sid, lang, body[body.find(">") + 1:-len("</div>")]


def loc(path, lang):
    if path.startswith("/client") and lang == "ar" and path.split("?")[0] not in AR_ROUTES:
        lang = "en"
    return B.localize(path, lang)


def sidebar(sd, sid, lang):
    current = SECTION.get(sid, ROUTES[sid])
    items = iter(SIDEBAR)

    def item(m):
        path = next(items)
        on = " on" if path == current else ""
        cur = ' aria-current="page"' if path == current else ""
        return f'<a class="it{on}" href="{loc(path, lang)}"{cur}>{m.group(1)}</a>'
    sd = re.sub(r'<div class="it ?(?:on)?">(.*?)</div>', item, sd, flags=re.S)
    sd = re.sub(r'<div style="padding:6px 10px 20px">(<span class="lg">.*?</span></span>)</div>',
                lambda m: f'<div style="padding:6px 10px 20px"><a href="{loc("/client/home", lang)}" aria-label="{"منطقة عميل TharwaFx" if lang == "ar" else "TharwaFx client area"}">{m.group(1)}</a></div>',
                sd, count=1, flags=re.S)
    back = "العودة إلى الموقع" if lang == "ar" else "Back to website"
    sd = sd.replace('<div class="gx"></div>', f'<div class="gx"></div><a class="it" href="{B.localize("/", lang)}">{back}</a>', 1)
    return sd.replace('<div class="sd">', f'<nav class="sd" id="sd" aria-label="{"منطقة العميل" if lang == "ar" else "Client area"}">', 1)[:-len("</div>")] + "</nav>"


def topbar(ah, sid, lang):
    path = ROUTES[sid]
    other = "en" if lang == "ar" else "ar"
    other_url = loc(path if path in AR_ROUTES else "/client/home", other)
    menu = "القائمة" if lang == "ar" else "Menu"
    ah = ah.replace('<div class="ah">', f'<div class="ah"><button type="button" class="burger app-burger" aria-expanded="false" aria-controls="sd" aria-label="{menu}"><i></i><i></i><i></i></button>', 1)
    ah = re.sub(r'<span class="sm">(العربية|English)</span>',
                lambda m: f'<a class="sm hide-s" href="{other_url}" hreflang="{other}">{"English" if lang == "ar" else "العربية"}</a>', ah)
    # The bell opens notifications.
    ah = re.sub(r'(<svg class="ico" width="20" height="20".*?</svg>)',
                lambda m: f'<a class="bell" href="{loc("/client/notifications", lang)}" aria-label="{"الإشعارات" if lang == "ar" else "Notifications"}">{m.group(1)}</a>',
                ah, count=1, flags=re.S)
    labels = (("الملف الشخصي", "الأمان", "تسجيل الخروج") if lang == "ar" else ("Profile", "Security", "Sign out"))
    ah = re.sub(r'<span style="width:36px;height:36px;border-radius:50%;([^"]*)">([^<]{1,3})</span>',
                lambda m: (f'<div class="me"><button type="button" class="me-b" style="width:36px;height:36px;border-radius:50%;{m.group(1)}" aria-expanded="false" aria-controls="me-m" aria-label="{"أحمد المنصوري" if lang == "ar" else "Ahmed Al Mansoori"}">{m.group(2)}</button>'
                           f'<div class="me-m" id="me-m" hidden><a href="{loc("/client/profile", lang)}">{labels[0]}</a><a href="{loc("/client/security", lang)}">{labels[1]}</a>'
                           f'<a href="{B.localize("/login", lang)}" data-signout>{labels[2]}</a></div></div>'), ah)
    return ah


def fields(s, sid, lang):
    def field(m):
        label, cls, style, inner = m.group(1), m.group(2), m.group(3) or "", m.group(4)
        lab = B.text(label)
        name = re.sub(r"[^a-z0-9]+", "-", lab.lower()).strip("-") or f"f{abs(hash(lab)) % 997}"
        cid = f"c-{sid.lower()}-{name}"
        val = B.text(re.sub(r"<svg.*?</svg>", "", inner, flags=re.S))
        # A new client fills in their own details, so the book's sample values become hints.
        ph = " ph" in cls or sid == "C06"
        if "chev" in inner:
            opts = OPTIONS.get(lab, [val])
            if val and val not in opts:
                opts = [val] + opts
            o = "".join(f'<option{" selected" if x == val else ""}{" value=\"\"" if x.startswith("Choose") else ""}>{x}</option>' for x in opts)
            return f'<div class="f"><label for="{cid}">{label}</label><select class="i" id="{cid}" name="{name}" dir="auto" required>{o}</select>'
        if "height:" in style and "120" in style:
            return f'<div class="f"><label for="{cid}">{label}</label><textarea class="i" id="{cid}" name="{name}" rows="4" placeholder="{val}" required></textarea>'
        kind = "email" if "mail" in name else ("tel" if "mobile" in name else "text")
        code = "code" in name
        amount = "amount" in name or "المبلغ" in lab
        if amount:
            val = val.replace("$", "").strip()
        attrs = ' inputmode="numeric" maxlength="6" autocomplete="one-time-code" pattern="[0-9]{6}"' if code else (' inputmode="decimal"' if amount else "")
        value = "" if ph or code else val
        holder = "" if not ph else val
        pre = '<span class="cur">$</span>' if amount else ""
        ctl = f'<input class="i{" amt" if amount else ""}" id="{cid}" name="{name}" type="{kind}" value="{value}" placeholder="{holder}" dir="ltr" required{attrs}>'
        return f'<div class="f"><label for="{cid}">{label}</label>{"<div class=\"amt-w\">" + pre + ctl + "</div>" if amount else ctl}'
    # The closing </div> of .f is left in place, so hints after the field stay inside it.
    s = re.sub(r'<div class="f"><label>(.*?)</label><div class="i([^"]*)"( style="[^"]*")?>(.*?)</div>', field, s, flags=re.S)
    return s


def radios(s):
    """Book radios become real ones; siblings that touch share a group."""
    out, pos, n, last_end = [], 0, 0, -1
    for m in re.finditer(r'<div class="rad( on| )?">', s):
        if m.start() < pos:
            continue
        end = B.div_end(s, m.start())
        if m.start() != last_end:
            n += 1
        on = m.group(1) == " on"
        inner = s[m.end():end - len("</div>")].replace("<i></i>", "", 1)
        out.append(s[pos:m.start()])
        out.append(f'<label class="rad{" on" if on else ""}"><input type="radio" name="opt{n}" value="{B.text(inner)}"{" checked" if on else ""} required><i></i>{inner}</label>')
        pos = last_end = end
    out.append(s[pos:])
    return "".join(out)


def controls(s, sid, lang):
    s = re.sub(r'<div class="chk( on)?"><i></i><span>(.*?)</span></div>',
               lambda m: f'<label class="chk"><input type="checkbox"{" checked" if m.group(1) else ""} required><i></i><span>{m.group(2)}</span></label>', s)
    s = re.sub(r'<div class="otp">.*?</div>', '<div class="otp" role="group">' + "".join(
        f'<input inputmode="numeric" maxlength="1" aria-label="Digit {i + 1}"{" autocomplete=\"one-time-code\"" if i == 0 else ""}>' for i in range(6)) + "</div>", s, count=1, flags=re.S)
    s = re.sub(r'<span class="pill([^"]*)">([^<]*)</span>',
               lambda m: f'<button type="button" class="pill{m.group(1)}" aria-pressed="{"true" if "on" in m.group(1) else "false"}">{m.group(2)}</button>', s)
    s = re.sub(r'(<div class="(?:seg|tabs)[^"]*"[^>]*>)(.*?)(</div>)',
               lambda m: m.group(1) + re.sub(r'<span( class="([^"]*)")?>([^<]*)</span>',
                                             lambda t: f'<button type="button" class="{t.group(2) or ""}" aria-pressed="{"true" if t.group(2) == "on" else "false"}">{t.group(3)}</button>',
                                             m.group(2)) + m.group(3), s, flags=re.S)
    # File drop zone (documents) becomes a real file picker.
    s = re.sub(r'<div style="border:1.5px dashed #555;border-radius:12px;padding:28px;text-align:center">(.*?)</div>',
               r'<label class="drop" style="border:1.5px dashed #555;border-radius:12px;padding:28px;text-align:center;display:block;cursor:pointer">\1'
               r'<input type="file" name="document" accept=".jpg,.jpeg,.png,.pdf" required><span class="sm grn" data-file></span></label>', s, count=1, flags=re.S)
    return s


def links(s, sid, lang):
    def sub(m):
        cls, label = m.group(1), m.group(2)
        if label in SUBMITS or label.startswith("Pay "):
            kind = "submit" if label not in ("Cancel", "Sign out", "Sign out everywhere", "Export CSV", "Download receipt", "Upload again", "Mark all as read") else "button"
            act = f' data-act="{re.sub(r"[^a-z]+", "-", label.lower()).strip("-")}"' if kind == "button" else ""
            return f'<button type="{kind}" class="{cls}"{act}>{label}</button>'
        target = PAGE_ACTIONS.get((sid, label)) or ACTIONS.get(label)
        if target is None:
            return m.group(0)
        if target == "toast":
            return f'<button type="button" class="{cls}" data-act="reset">{label}</button>'
        if target == "soon":
            return f'<a class="{cls}" href="#" data-soon>{label}</a>'
        return f'<a class="{cls}" href="{loc(target, lang)}">{label}</a>'
    return re.sub(r'<span class="(b [^"]*|lk)">([^<]*)</span>', sub, s)


def rows(s, sid, lang):
    """Transaction and account rows open their detail screen."""
    if sid == "A13":
        def row(m):
            target = "/client/withdraw/wd-20391" if m.group(2).startswith("WD-") else "/client/transactions/tx-88412"
            kind = {"TX": "deposit", "WD": "withdrawal", "TR": "transfer"}[m.group(2)[:2]]
            return f'<tr class="" data-href="{loc(target, lang)}" data-type="{kind}" tabindex="0">{m.group(1)}'
        s = re.sub(r'<tr class="">(<td class=""><span class="mono">([A-Z]+-\d+))', row, s)
    return s


def wrap_form(s, sid):
    """Each screen with inputs gets one form around its working area."""
    if sid.startswith("C") and sid != "C10":
        r = s.find('<div class="r">')
        end = B.div_end(s, r)
        return s[:r] + f'<form class="r" data-flow="{sid}" novalidate>' + s[r + len('<div class="r">'):end - 6] + "</form>" + s[end:]
    a = s.find('<div class="ac">')
    if a < 0:
        return s
    end = B.div_end(s, a)
    return s[:a] + f'<form class="ac" data-flow="{sid}" novalidate>' + s[a + len('<div class="ac">'):end - 6] + "</form>" + s[end:]


def extras(s, sid, lang):
    if sid == "A06":
        label = "متابعة" if lang == "ar" else "Continue"
        s = s.replace('<div class="card"><h3 class="mb16">', f'<div class="card"><h3 class="mb16">', 1)
        s = re.sub(r'(<div class="col gap8 sm mut">.*?</div>)', rf'\1<button type="submit" class="b p w mt24">{label}</button>', s, count=1, flags=re.S)
    if sid == "A08":
        # One outcome at a time; ?status=pending or failed shows the others.
        states = iter(["completed", "pending", "failed"])
        s = re.sub(r'<div class="card c" style="padding:44px 28px">', lambda m: f'<div class="card c" style="padding:44px 28px" data-state="{next(states)}">', s)
    if sid == "C09":
        s = s.replace('<div style="width:190px;height:190px;background:#fff;', '<div role="img" aria-label="QR code" style="width:190px;height:190px;background:#fff;', 1)
    if sid == "C10":
        s = s.replace('<div class="card dg">', '<div class="card dg has-media">' + B.media("cta-loop", "cta-desert", "card-bg"), 1)
    if sid == "A21":
        s = re.sub(r'<div class="i ph"><span>Write a reply</span>.*?</svg></div>',
                   '<label class="sr" for="c-reply">Write a reply</label><textarea class="i" id="c-reply" name="reply" rows="3" placeholder="Write a reply" required></textarea>', s, count=1, flags=re.S)
    if sid in ("A11",):
        s = s.replace('<div class="tl">', '<div class="tl" data-timeline>', 1)
    return s


def transform(body, sid, lang):
    if sid.startswith("C") and sid != "C10":
        body = body.replace('<div class="l">', '<div class="l">' + B.media("auth-loop", "auth-panel", "auth-bg", eager=True), 1)
        s = re.sub(r'<div><span class="lg">(.*?)</span></span></div>',
                   lambda m: f'<div class="row sb"><a href="{B.localize("/", lang)}" aria-label="TharwaFx home"><span class="lg">{m.group(1)}</span></span></a></div>', body, count=1, flags=re.S)
    else:
        sd_start = body.find('<div class="sd">')
        sd = body[sd_start:B.div_end(body, sd_start)]
        rest = body[B.div_end(body, sd_start):]
        ah_start = rest.find('<div class="ah">')
        ah = rest[ah_start:B.div_end(rest, ah_start)]
        rest = rest[:ah_start] + topbar(ah, sid, lang) + rest[B.div_end(rest, ah_start):]
        s = body[:sd_start] + sidebar(sd, sid, lang) + rest
        s = s.replace('<div class="app">', '<div class="app"><div class="sd-veil" hidden></div>', 1)
    s = fields(s, sid, lang)
    s = radios(s)
    s = controls(s, sid, lang)
    s = links(s, sid, lang)
    s = rows(s, sid, lang)
    s = extras(s, sid, lang)
    s = wrap_form(s, sid)
    s = re.sub(r'<svg width="(\d+(?:\.\d+)?)" height="(\d+)"( style)', r'<svg class="ill" width="\1" height="\2"\3', s)
    s = re.sub(r'<div class="tbl">(<table>.*?</table>)</div>', r'<div class="tbl"><div class="tscroll">\1</div></div>', s, flags=re.S)
    return s


def translate(s):
    """English screen to Arabic: swap whole text runs and labelled attributes from client_ar.AR."""
    def run(m):
        t = html.unescape(m.group(2))
        return m.group(1) + AR.get(t, m.group(2)) + m.group(3)
    s = re.sub(r'(>\s*)([^<>]*?[A-Za-z][^<>]*?)(\s*<)', run, s)
    s = re.sub(r'((?:placeholder|aria-label|value)=")([^"]*[A-Za-z][^"]*)(")', run, s)
    # Text that is now Arabic no longer needs its left-to-right isolate.
    return re.sub(r'<bdi dir="ltr">([^<]*[\u0600-\u06FF][^<]*)</bdi>', r"\1", s)


def build_all():
    B.AR_PAGES.update(AR_ROUTES)
    native = {(sid, lang) for sid, lang, _ in screens()}
    jobs = list(screens()) + [(sid, "ar", body) for sid, lang, body in screens() if (sid, "ar") not in native]
    count = 0
    for sid, lang, body in jobs:
        path = ROUTES[sid]
        s = transform(body, sid, lang)
        if (sid, lang) not in native:
            s = translate(s)
        h = re.search(r'<div class="ah">.*?<h3>(.*?)</h3>', s, re.S) or re.search(r"<h2[^>]*>(.*?)</h2>", s[s.find('class="r"'):], re.S)
        title = B.text(h.group(1)) if h else "Client area"
        doc = B.page(lang, path, title, title, s, sid, shell=False)
        doc = doc.replace('<link rel="canonical"', '<meta name="robots" content="noindex"><link rel="canonical"')
        B.write(lang, path, doc)
        count += 1
    return count
