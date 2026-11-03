"""Home page (P01) redesigns layered over the book markup: the platforms phone, the sign-up roadmap,
the deposit methods and the safety cards. Each function finds its section in the built HTML, reads the
copy out of it (so English and Arabic stay in step with the book) and swaps in the new markup."""
import re

import build as B

ICONS = {
    "user": '<path d="M15 19a6 6 0 0 0-12 0M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM19 8v6M22 11h-6"/>',
    "id": '<path d="M3 5h18v14H3zM7 15c.6-1.4 1.7-2 3-2s2.4.6 3 2M10 11a1.8 1.8 0 1 0 0-3.6 1.8 1.8 0 0 0 0 3.6zM15 9h3M15 12h3"/>',
    "wallet": '<path d="M3 7h16a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2zM3 7l13-3v3M16 13h2"/>',
    "chart": '<path d="M7 4v16M17 4v16M4 8h6v7H4zM14 7h6v9h-6z"/>',
}
CTA = {"en": "Start with step 1", "ar": "ابدأ بالخطوة الأولى"}
KICK = {"en": ("// Four steps", "// Funding", "// Safety"), "ar": ("أربع خطوات", "التمويل", "الأمان")}


def svg(name, size=22):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


def block(s, start):
    """End index of the <div> that opens at start."""
    depth, i = 0, start
    for m in re.compile(r"<div\b|</div>").finditer(s, start):
        depth += 1 if m.group(0) == "<div" else -1
        if depth == 0:
            return m.end()
    raise ValueError("unbalanced div")


def platforms(s, lang):
    """A cinematic platform showcase; accepts a replacement landscape video when supplied."""
    marker = s.index('<div><div class="phone" style="min-height:520px;width:300px;margin:0 auto">')
    a = s.rfind('<section', 0, marker)
    end = s.index('</section>', marker) + len('</section>')
    original = s[a:end]
    cards = re.search(r'<div class="g2 mt32">(.*)</div></div><div><div class="phone"', original, re.S).group(1)
    suffix = "-ar" if lang == "ar" else ""
    supplied = B.os.path.exists(B.os.path.join(B.SRC, 'assets', 'video', 'platform-showcase.mp4'))
    has_mockup = bool(B.img_url('platform-showcase'))
    video = 'platform-showcase' if supplied or has_mockup else 'phone-loop'
    poster = 'platform-showcase' if B.img_url('platform-showcase') else 'phone-mock' + suffix
    kicker, title, description, cta = (
        ('منصات التداول', 'سوقك. على شاشتك.', 'من التحليل على مكتبك إلى متابعة الأسواق أثناء تنقلك، استكشف المنصة التي تناسب طريقة تداولك.', 'استكشف المنصات') if lang == 'ar' else
        ('YOUR TRADING WORKSPACE', 'Your market.\nYour screen.', 'From focused analysis at your desk to following the markets on the move. Find the platform that fits the way you trade.', 'Explore platforms'))
    media = B.media(video, poster, 'platform-film' + (' platform-composite' if has_mockup else '' if supplied else ' platform-preview'), eager=False)
    # Keep a real video in both languages while the Arabic-specific poster supplies the fallback.
    title = title.replace('\n', '<br>')
    section = (f'<section class="sec platform-showcase" id="platform-showcase"><div class="wrap"><div class="platform-stage">{media}'
               f'<div class="platform-copy"><span class="platform-kicker mono">{kicker}</span><h2>{title}</h2><p>{description}</p>'
               f'<a class="b p" href="{B.localize("/platforms", lang)}">{cta}<span aria-hidden="true">{"←" if lang == "ar" else "→"}</span></a></div>'
               '<div class="platform-stage-line" aria-hidden="true"></div></div>'
               f'<div class="platform-options plat">{cards}</div></div></section>')
    return s[:a] + section + s[end:]


def roadmap(s, lang):
    m = re.search(r'<section class="sec "><div class="wrap"><h2 class="mb48">([^<]*)</h2><div style="position:relative"><svg.*?</section>', s, re.S)
    steps = re.findall(r'<div class="sn">(\d)</div><h3 class="mt8">(.*?)</h3><p class="sm mut mt8">(.*?)</p>', m.group(0))
    icons = ["user", "id", "wallet", "chart"]
    items = "".join(
        f'<li class="road-step" style="--n:{i}"><div class="road-node">{svg(icons[i])}<span class="mono">0{n}</span></div>'
        f'<div class="road-card"><span class="road-no mono" aria-hidden="true">0{n}</span><h3>{h}</h3><p class="sm mut mt8">{p}</p></div></li>'
        for i, (n, h, p) in enumerate(steps))
    html = (f'<section class="sec road"><div class="road-grid" aria-hidden="true"></div><div class="wrap">'
            f'<span class="mono k">{KICK[lang][0]}</span><h2 class="mt16">{m.group(1)}</h2>'
            f'<div class="road-wrap mt48" data-road><div class="road-rail" aria-hidden="true"><i class="road-fill"></i><i class="road-pulse"></i></div>'
            f'<ol class="road-track">{items}</ol></div>'
            f'<a class="b p lg2 mt48" href="{B.localize("/register", lang)}">{CTA[lang]} <span aria-hidden="true">→</span></a></div></section>')
    return s[:m.start()] + html + s[m.end():]


def deposits_and_safety(s, lang):
    m = re.search(r'<section class="sec t" style="border-top:1px solid #1e1e1e"><div class="wrap row sb wr"><h3>([^<]*)</h3>'
                  r'<div class="row wr">((?:<span class="chip">[^<]*</span>)+)</div></div></section>', s)
    chips = re.findall(r'<span class="chip">([^<]*)</span>', m.group(2))
    logos = {'Visa': 'visa', 'Mastercard': 'mastercard', 'Apple Pay': 'applepay', 'Google Pay': 'googlepay', 'Skrill': 'skrill', 'Neteller': 'neteller', 'USDT': 'tether'}
    tiles = []
    for c in chips:
        if c in logos:
            visual = f'<img src="/assets/img/payments/{logos[c]}.svg" alt="{c}" width="100" height="32" loading="lazy">'
            if c == 'USDT':
                visual += '<span aria-hidden="true">USDT</span>'
        else:
            visual = '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M3 9h18L12 3 3 9ZM5 11v8m7-8v8m7-8v8M3 21h18"/></svg>' + f'<span>{c}</span>'
        tiles.append(f'<li class="payment-logo">{visual}</li>')
    info = 'طرق التمويل' if lang == 'ar' else 'Explore funding'
    note = 'تختلف طرق الدفع المتاحة حسب المنطقة والحساب.' if lang == 'ar' else 'Available payment methods depend on your region and account.'
    pay = (f'<section class="pay"><div class="wrap pay-in"><div class="pay-h"><span class="mono k">{KICK[lang][1]}</span><h3 class="mt8">{m.group(1)}</h3></div>'
           f'<a class="lk" href="{B.localize("/funding/deposits", lang)}">{info} <span aria-hidden="true">{"←" if lang == "ar" else "→"}</span></a>'
           f'<ul class="payment-logos" aria-label="{"طرق الدفع" if lang == "ar" else "Payment methods"}">{"".join(tiles)}</ul>'
           f'<div class="payment-note"><p>{note}</p><a href="/assets/img/payments/CREDITS.txt">{"مصادر الشعارات" if lang == "ar" else "Logo credits"}</a></div></div></section>')
    s = s[:m.start()] + pay + s[m.end():]

    t = re.compile(r'<section class="sec "><div class="wrap"><h2 class="mb32">([^<]*)</h2><div class="g3">(.*?)</div></div></section>', re.S)
    m = t.search(s, s.index('class="pay"'))
    cards = re.findall(r'<div class="card">(<svg.*?</svg>)<h3 class="mt16">(.*?)</h3><p class="mut sm mt8">(.*?)</p></div>', m.group(2), re.S)
    out = "".join(
        f'<div class="vault-card"><div class="vault-top"><span class="vault-ico">{ico.replace(" stroke=\"#34E834\"", " stroke=\"currentColor\"")}</span>'
        f'<span class="mono xs mut3">0{i + 1}</span></div><h3 class="mt24">{h}</h3><p class="mut sm mt8">{p}</p><i class="vault-scan" aria-hidden="true"></i></div>'
        for i, (ico, h, p) in enumerate(cards))
    safe = (f'<section class="sec vault"><div class="wrap"><span class="mono k">{KICK[lang][2]}</span><h2 class="mt16 mb32">{m.group(1)}</h2>'
            f'<div class="vault-g">{out}</div></div></section>')
    return s[:m.start()] + safe + s[m.end():]


def redesign(s, lang):
    return navigation_cards(deposits_and_safety(roadmap(platforms(s, lang), lang), lang), lang)


def navigation_cards(s, lang):
    """Give the home page's product and learning cards real destinations."""
    groups = [
        (r'<div class="card (?:hl)?"><div class="row sb"><h3>',
         ["/accounts/standard", "/accounts/raw-spread", "/accounts/islamic"],
         "استكشف الحساب" if lang == "ar" else "Explore account"),
        (r'<div class="card s row sb">',
         ["/platforms/mt5", "/platforms/webtrader", "/platforms/app", "/platforms/tradingview"], None),
        (r'<div class="card s"><span class="tg g">',
         ["/academy", "/academy/webinars", "/tools/calculators"],
         "اكتشف المزيد" if lang == "ar" else "Explore resource"),
    ]
    for pattern, paths, label in groups:
        matches = list(re.finditer(pattern, s))
        if len(matches) != len(paths):
            raise ValueError(f"Home navigation cards: expected {len(paths)}, got {len(matches)}")
        for match, path in reversed(list(zip(matches, paths))):
            start, end = match.start(), block(s, match.start())
            card = s[start:end]
            if path.startswith('/accounts/'):
                copy = {
                    '/accounts/standard': (
                        'Straightforward pricing, with trading costs included in the spread.',
                        ['Spread-based pricing', 'No separate dealing commission', 'Check costs in the instrument specification'],
                        'View Standard account'),
                    '/accounts/raw-spread': (
                        'Raw spreads and a separate commission, shown side by side.',
                        ['Spread and commission priced separately', 'Commission charged per lot', 'Compare the combined cost of each trade'],
                        'View Raw Spread account'),
                    '/accounts/islamic': (
                        'Explore swap-free trading and the conditions that apply to your account.',
                        ['Swap-free account structure', 'Eligibility and conditions apply', 'Review holding-period terms before trading'],
                        'View Islamic account'),
                }
                ar_copy = {
                    '/accounts/standard': ('تسعير واضح تُحتسب فيه تكاليف التداول ضمن الفارق السعري.', ['تسعير يعتمد على الفارق السعري', 'دون عمولة تداول منفصلة', 'راجع التكاليف في مواصفات الأداة'], 'استكشف حساب ستاندرد'),
                    '/accounts/raw-spread': ('فروقات خام وعمولة منفصلة، لتتمكن من مقارنة عناصر التكلفة.', ['تسعير الفارق والعمولة بشكل منفصل', 'تُحتسب العمولة لكل لوت', 'قارن التكلفة الإجمالية لكل صفقة'], 'استكشف حساب رو سبريد'),
                    '/accounts/islamic': ('تعرّف على التداول دون رسوم تبييت والشروط المطبقة على حسابك.', ['هيكل حساب دون رسوم تبييت', 'تُطبق شروط الأهلية والحساب', 'راجع شروط الاحتفاظ بالصفقات قبل التداول'], 'استكشف الحساب الإسلامي'),
                }
                description, benefits, label = (ar_copy if lang == 'ar' else copy)[path]
                card = re.sub(r'<p class="sm mut mt8">.*?</p>',
                              lambda _: f'<p class="sm mut mt8 account-summary">{description}</p>', card, count=1)
                card = card.replace('Most chosen', 'Spread + commission').replace('الأكثر اختياراً', 'الفارق والعمولة')
                benefit_list = '<ul class="account-benefits">' + ''.join(f'<li>{benefit}</li>' for benefit in benefits) + '</ul>'
                card = card[:-6] + benefit_list + '</div>'
            card = card.replace('<div class="card', '<a href="' + B.localize(path, lang) + '" class="home-link card', 1)
            if label:
                card = card[:-6] + f'<span class="home-card-cta">{label}<span aria-hidden="true">→</span></span></a>'
            else:
                title = re.search(r'<b>(.*?)</b>', card).group(1)
                detail = re.search(r'<div class="sm mut3">(.*?)</div>', card).group(1)
                icons = {
                    '/platforms/mt5': '<rect x="3" y="4" width="18" height="13" rx="2"/><path d="M8 21h8m-4-4v4M6 13l3-3 3 2 5-5"/>',
                    '/platforms/webtrader': '<rect x="2" y="3" width="20" height="18" rx="3"/><path d="M2 8h20m-16-3h.01M9 5h.01M8 12l-3 3 3 3m8-6 3 3-3 3m-3-7-2 8"/>',
                    '/platforms/app': '<rect x="6" y="2" width="12" height="20" rx="3"/><path d="M10 5h4m-4 14 2-3 2 1 2-4m-5 7h2"/>',
                    '/platforms/tradingview': '<path d="M3 3v18h18M6 15l4-5 4 3 6-8m-5 0h5v5"/><circle cx="10" cy="10" r="1"/>',
                }
                icon = f'<svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{icons[path]}</svg>'
                opening = card[:card.index('>') + 1].replace('home-link card s row sb', 'home-link card platform-card vault-card')
                number = f'{paths.index(path) + 1:02d}'
                card = (opening + f'<div class="platform-card-top"><span class="platform-icon">{icon}</span><span class="platform-card-number mono mut3" aria-hidden="true">{number}</span></div>'
                        f'<div class="platform-card-copy"><h3>{title}</h3><p>{detail}</p></div></a>')
            s = s[:start] + card + s[end:]
    return s
