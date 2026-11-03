"""Trade with AI page (/ai), English and Arabic.

Five tools, with automated trading as the centrepiece: a scenario simulator where the visitor sets
the amount, style, risk per trade, horizon and a drawdown stop, and sees a range of outcomes from
1,000 simulated paths (site.js, [data-sim]). The simulator never shows a single "predicted profit":
it shows a spread that includes losses, with its made-up assumptions stated on the page.
"""
import build as B

T = {
    "en": {
        "title": "Trade with AI",
        "desc": "AI tools for market analysis, news sentiment, risk management, automated trading and strategy backtesting, in Arabic and English.",
        "eyebrow": "TharwaFx AI",
        "h1": "A new dimension of market intelligence.",
        "lead": "Explore AI-assisted market analysis, news sentiment and strategy testing. A wider perspective, with your decisions and risk limits at the centre.",
        "cta1": "Try AI on a demo", "cta2": "See automated trading",
        "note": "AI tools are in development and shown here as a preview*. Trading carries risk.",
        "console": "AI engine", "sample": "Sample activity",
        "log": [
            ("scan", "XAUUSD trend up on H4, momentum fading near 2,410*"),
            ("news", "US CPI in 42 min: high impact, pausing new USD entries"),
            ("risk", "Exposure 2.4% of equity, inside your 5% limit"),
            ("trade", "EURUSD buy 0.20 lots, stop 1.0812, target 1.0890*"),
            ("sent", "Gold sentiment 64% positive across today's sources*"),
            ("test", "Breakout v2 backtest done: 3 years, 1,284 trades*"),
            ("trade", "Closed GBPUSD sell, +$38.20*, rule: target hit"),
            ("risk", "Daily loss limit 1.8% of 3% used, trading on"),
        ],
        "features_k": "// The toolkit", "features_h": "Five tools, one assistant",
        "features": [
            ("01", "Market analysis", "Scans the markets you follow for trend, momentum and key levels, then explains what it sees in plain Arabic or English.", ["Trend and momentum", "Support and resistance", "Pattern alerts"]),
            ("02", "News and sentiment", "Reads headlines, central bank statements and the economic calendar, and scores the mood for each market as it changes.", ["Event impact", "Sentiment score", "Arabic news included"]),
            ("03", "Risk management", "Sizes every position from your risk per trade, watches total exposure and steps in before your limits are crossed.", ["Position sizing", "Exposure watch", "Loss limits"]),
            ("04", "Automated trading", "Turns your strategy into rules the AI follows around the clock: entries, exits and position size, always inside the limits you set.", ["Runs 24/5", "Your limits, always", "Pause any time"]),
            ("05", "Strategy backtesting", "Tests a strategy on years of past prices before you risk money, with costs included, and shows where it would have struggled.", ["Years of data", "Costs included", "Drawdown report"]),
        ],
        "featured": "Featured",
        "viz_sent": ("Gold", "Positive"), "viz_risk": "Exposure", "viz_auto": ("Signal", "Check limits", "Execute"),
        "auto_k": "// Automated trading", "auto_h": "Set the rules. The AI does the watching.",
        "auto_lead": "You choose the strategy and the limits. The AI trades inside them, explains every decision, and stops when you say so.",
        "steps": [("Pick a strategy", "Start from a tested template or describe your own."),
                  ("Set your limits", "Risk per trade, daily loss limit and a drawdown stop."),
                  ("Let it trade", "Orders run on your account, with a reason for each one."),
                  ("Review and adjust", "Weekly reports, and a pause button that works instantly.")],
        "sim_k": "// Scenario simulator", "sim_h": "See the range before you start",
        "sim_lead": "Move the sliders to see how 1,000 simulated paths could spread out. This is a what-if tool, not a forecast.",
        "amount": "Amount to invest", "style": "Strategy style", "styles": ["Conservative", "Balanced", "Aggressive"],
        "risk": "Risk per trade", "months": "Time horizon", "stop": "Stop trading if the account falls by", "news": "Pause during high-impact news",
        "unit_m": "months", "unit_m1": "month", "rerun": "Run again",
        "out_mid": "Typical outcome", "out_mid_s": "Median of 1,000 paths",
        "out_good": "Good case", "out_good_s": "1 in 10 paths did better",
        "out_bad": "Bad case", "out_bad_s": "1 in 10 paths did worse",
        "out_max": "Most the stop should allow you to lose", "out_hit": "Paths where the stop was hit",
        "chart": "Account value over time", "legend": ["Middle 80% of paths", "Typical path", "One possible path", "Your stop"],
        "assume": "Illustration only. Assumes an average monthly return of {mu} and monthly swings of {sigma} after costs, figures we made up for this demo. They are not TharwaFx results or a forecast. Real results can be worse, and fast markets can move past a stop.",
        "control_k": "// You stay in control", "control_h": "Guardrails on by default",
        "controls": [("Daily loss limit", "Trading stops for the day once it is reached."), ("Drawdown stop", "Everything pauses if the account falls past your level."),
                     ("Pause button", "One tap stops new trades and keeps open ones protected."), ("Every trade explained", "See the signal, the news and the rule behind each order."),
                     ("Your account only", "The AI trades your account. It can never move your money.")],
        "faq_h": "Questions about AI trading",
        "faq": [("Will the AI make me money?", "No tool can promise that. The AI follows rules and limits, and markets can still move against them. Simulations and backtests show possibilities, not results."),
                ("Can I try it without risking money?", "Yes. Every AI tool will run on a demo account with virtual funds first, so you can watch it work before going live."),
                ("Who is responsible for the trades?", "You are. You choose the strategy and the limits, you can pause it any time, and every order shows the reason it was placed."),
                ("Is it available in Arabic?", "Yes. Analysis, news summaries and trade explanations are written in Arabic or English, your choice.")],
    },
    "ar": {
        "title": "تداول بمساعدة الذكاء الاصطناعي",
        "desc": "أدوات ذكاء اصطناعي لتحليل السوق وقراءة الأخبار وإدارة المخاطر والتداول الآلي واختبار الاستراتيجيات، بالعربية والإنجليزية.",
        "eyebrow": "ذكاء ثروة الاصطناعي",
        "h1": "تداول بمساعدة الذكاء الاصطناعي.",
        "lead": "خمس أدوات ذكاء اصطناعي تقرأ السوق، وتزن الأخبار، وتحمي مخاطرك، وتنفّذ قواعدك، بينما تبقى أنت المتحكّم في كل حد.",
        "cta1": "جرّبه على حساب تجريبي", "cta2": "اكتشف التداول الآلي",
        "note": "أدوات الذكاء الاصطناعي قيد التطوير ومعروضة هنا كمعاينة*. التداول ينطوي على مخاطر.",
        "console": "محرّك الذكاء الاصطناعي", "sample": "نشاط توضيحي",
        "log": [
            ("scan", "XAUUSD اتجاه صاعد على H4، والزخم يتراجع قرب 2,410*"),
            ("news", "مؤشر CPI الأمريكي بعد 42 دقيقة: تأثير مرتفع، إيقاف صفقات USD الجديدة"),
            ("risk", "التعرّض 2.4% من الرصيد، ضمن حدّك البالغ 5%"),
            ("trade", "شراء EURUSD بحجم 0.20 لوت، وقف 1.0812، هدف 1.0890*"),
            ("sent", "معنويات الذهب إيجابية بنسبة 64% عبر مصادر اليوم*"),
            ("test", "اكتمل اختبار Breakout v2: ثلاث سنوات، 1,284 صفقة*"),
            ("trade", "إغلاق بيع GBPUSD بربح 38.20$*، القاعدة: بلوغ الهدف"),
            ("risk", "حد الخسارة اليومي: استُخدم 1.8% من 3%، التداول مستمر"),
        ],
        "features_k": "// الأدوات", "features_h": "خمس أدوات، مساعد واحد",
        "features": [
            ("01", "تحليل السوق", "يفحص الأسواق التي تتابعها بحثاً عن الاتجاه والزخم والمستويات الرئيسية، ثم يشرح ما يراه بلغة عربية أو إنجليزية واضحة.", ["الاتجاه والزخم", "الدعم والمقاومة", "تنبيهات الأنماط"]),
            ("02", "الأخبار والمعنويات", "يقرأ العناوين وبيانات البنوك المركزية والمفكرة الاقتصادية، ويقيس مزاج كل سوق لحظة بلحظة.", ["أثر الأحداث", "مؤشر المعنويات", "يشمل الأخبار العربية"]),
            ("03", "إدارة المخاطر", "يحدد حجم كل صفقة وفق مخاطرتك لكل صفقة، ويراقب إجمالي التعرّض، ويتدخل قبل تجاوز حدودك.", ["تحديد حجم الصفقة", "مراقبة التعرّض", "حدود الخسارة"]),
            ("04", "التداول الآلي", "يحوّل استراتيجيتك إلى قواعد ينفّذها الذكاء الاصطناعي على مدار الساعة: الدخول والخروج وحجم الصفقة، دائماً ضمن حدودك.", ["يعمل 24/5", "حدودك دائماً", "إيقاف في أي وقت"]),
            ("05", "اختبار الاستراتيجيات", "يختبر الاستراتيجية على سنوات من الأسعار السابقة قبل أن تخاطر بأموالك، مع احتساب التكاليف، ويُظهر أين كانت ستتعثر.", ["سنوات من البيانات", "التكاليف محتسبة", "تقرير التراجع"]),
        ],
        "featured": "مميّز",
        "viz_sent": ("الذهب", "إيجابي"), "viz_risk": "التعرّض", "viz_auto": ("إشارة", "فحص الحدود", "تنفيذ"),
        "auto_k": "// التداول الآلي", "auto_h": "ضع القواعد، ودع الذكاء الاصطناعي يراقب.",
        "auto_lead": "أنت تختار الاستراتيجية والحدود. والذكاء الاصطناعي يتداول ضمنها، ويشرح كل قرار، ويتوقف متى طلبت.",
        "steps": [("اختر استراتيجية", "ابدأ بقالب مُختبر أو صِف استراتيجيتك."),
                  ("حدّد حدودك", "المخاطرة لكل صفقة، وحد الخسارة اليومي، ووقف التراجع."),
                  ("دعه يتداول", "تُنفَّذ الأوامر على حسابك، مع سبب لكل أمر."),
                  ("راجع وعدّل", "تقارير أسبوعية، وزر إيقاف يعمل فوراً.")],
        "sim_k": "// محاكي السيناريوهات", "sim_h": "شاهد النطاق قبل أن تبدأ",
        "sim_lead": "حرّك المؤشرات لترى كيف قد تتوزع 1,000 نتيجة محاكاة. هذه أداة لاستكشاف الاحتمالات، وليست توقعاً.",
        "amount": "المبلغ المستثمر", "style": "أسلوب الاستراتيجية", "styles": ["متحفّظ", "متوازن", "جريء"],
        "risk": "المخاطرة لكل صفقة", "months": "المدة", "stop": "أوقف التداول إذا تراجع الحساب بنسبة", "news": "إيقاف مؤقت أثناء الأخبار عالية التأثير",
        "unit_m": "أشهر", "unit_m1": "شهر", "rerun": "أعد المحاكاة",
        "out_mid": "النتيجة المعتادة", "out_mid_s": "الوسيط من 1,000 مسار",
        "out_good": "حالة جيدة", "out_good_s": "مسار من كل 10 كان أفضل",
        "out_bad": "حالة سيئة", "out_bad_s": "مسار من كل 10 كان أسوأ",
        "out_max": "أقصى خسارة يُفترض أن يسمح بها الوقف", "out_hit": "المسارات التي بلغت الوقف",
        "chart": "قيمة الحساب عبر الزمن", "legend": ["80% الوسطى من المسارات", "المسار المعتاد", "مسار محتمل واحد", "حد الوقف"],
        "assume": "للتوضيح فقط. تفترض المحاكاة متوسط عائد شهري {mu} وتقلباً شهرياً {sigma} بعد التكاليف، وهي أرقام افتراضية وضعناها لهذا العرض. ليست نتائج TharwaFx ولا توقعاً. قد تكون النتائج الفعلية أسوأ، وقد تتجاوز الأسواق السريعة حد الوقف.",
        "control_k": "// أنت المتحكّم", "control_h": "ضوابط مفعّلة تلقائياً",
        "controls": [("حد الخسارة اليومي", "يتوقف التداول لبقية اليوم عند بلوغه."), ("وقف التراجع", "يتوقف كل شيء إذا تراجع الحساب إلى ما دون مستواك."),
                     ("زر الإيقاف", "لمسة واحدة توقف الصفقات الجديدة وتُبقي المفتوحة محمية."), ("شرح لكل صفقة", "اطّلع على الإشارة والخبر والقاعدة وراء كل أمر."),
                     ("حسابك فقط", "يتداول الذكاء الاصطناعي في حسابك، ولا يمكنه أبداً تحويل أموالك.")],
        "faq_h": "أسئلة حول التداول بالذكاء الاصطناعي",
        "faq": [("هل سيحقق لي الذكاء الاصطناعي أرباحاً؟", "لا يمكن لأي أداة أن تعد بذلك. يتبع الذكاء الاصطناعي قواعد وحدوداً، وقد يتحرك السوق عكسها. المحاكاة والاختبارات تُظهر احتمالات، لا نتائج."),
                ("هل يمكنني تجربته دون المخاطرة بأموالي؟", "نعم. ستعمل كل أدوات الذكاء الاصطناعي أولاً على حساب تجريبي بأموال افتراضية، لتراها تعمل قبل التداول الحقيقي."),
                ("من المسؤول عن الصفقات؟", "أنت. تختار الاستراتيجية والحدود، ويمكنك الإيقاف في أي وقت، ويُظهر كل أمر سبب تنفيذه."),
                ("هل هو متاح بالعربية؟", "نعم. التحليلات وملخصات الأخبار وشرح الصفقات بالعربية أو الإنجليزية، حسب اختيارك.")],
    },
}

TAG = {"scan": "SCAN", "news": "NEWS", "risk": "RISK", "trade": "TRADE", "sent": "SENT", "test": "TEST"}

# Small inline visuals for the five tool cards.
VIZ = {
    "01": '<svg viewBox="0 0 240 90" class="viz" aria-hidden="true"><path d="M0 70 L30 62 L55 66 L80 48 L105 52 L130 34 L155 40 L180 24 L205 30 L240 14" fill="none" stroke="#34E834" stroke-width="2" class="draw"/><line x1="0" y1="30" x2="240" y2="30" stroke="#34E834" stroke-dasharray="4 5" opacity=".45"/><line x1="0" y1="66" x2="240" y2="66" stroke="#E5484D" stroke-dasharray="4 5" opacity=".45"/><circle cx="180" cy="24" r="4" fill="#34E834" class="pulse"/></svg>',
    "05": '<svg viewBox="0 0 240 90" class="viz" aria-hidden="true"><path d="M0 80 C30 76 40 60 60 62 S90 50 110 54 S140 30 160 36 S200 18 240 12 L240 90 L0 90 Z" fill="url(#bt)" opacity=".35"/><path d="M0 80 C30 76 40 60 60 62 S90 50 110 54 S140 30 160 36 S200 18 240 12" fill="none" stroke="#34E834" stroke-width="2" class="draw"/><defs><linearGradient id="bt" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#34E834"/><stop offset="1" stop-color="#34E834" stop-opacity="0"/></linearGradient></defs></svg>',
}


def viz(num, t):
    if num in VIZ:
        return VIZ[num]
    if num == "02":
        name, mood = t["viz_sent"]
        return (f'<div class="viz senti" aria-hidden="true"><div class="row sb xs"><span>{name}</span><span class="grn">{mood} <b class="mono">64%*</b></span></div>'
                '<div class="bar"><i style="width:64%"></i></div><div class="ticks">' + "".join(f"<span style=\"height:{h}px\"></span>" for h in (8, 14, 10, 18, 22, 12, 26, 20, 16, 24, 30, 18, 22, 28)) + "</div></div>")
    if num == "03":
        return (f'<div class="viz gauge" aria-hidden="true"><svg viewBox="0 0 120 66"><path d="M10 60 A50 50 0 0 1 110 60" fill="none" stroke="#222" stroke-width="10" stroke-linecap="round"/>'
                '<path d="M10 60 A50 50 0 0 1 110 60" fill="none" stroke="#34E834" stroke-width="10" stroke-linecap="round" stroke-dasharray="157" stroke-dashoffset="100" class="sweep"/></svg>'
                f'<div><b class="mono">2.4%</b><span class="xs mut3">{t["viz_risk"]} / 5%</span></div></div>')
    a, b, c = t["viz_auto"]
    return (f'<div class="viz flow" aria-hidden="true"><span>{a}</span><i></i><span>{b}</span><i></i><span class="on">{c}</span></div>')


def slider(name, label, lo, hi, step, val, out):
    return (f'<div class="sl"><div class="row sb"><label for="sim-{name}">{label}</label><output class="mono" for="sim-{name}" data-out="{name}">{out}</output></div>'
            f'<input type="range" id="sim-{name}" name="{name}" min="{lo}" max="{hi}" step="{step}" value="{val}"></div>')


def body(lang):
    t = T[lang]
    L = lambda p: B.localize(p, lang)  # noqa: E731
    log = "".join(f'<li data-tag="{TAG[k]}">{x}</li>' for k, x in t["log"])
    feats = []
    for num, name, text, chips in t["features"]:
        star = num == "04"
        feats.append(
            f'<article class="ai-card{" star" if star else ""}" id="tool-{num}"><div class="row sb"><span class="mono k">{num}</span>'
            f'{f"<span class=\"tg g\">{t['featured']}</span>" if star else ""}</div><h3 class="mt16">{name}</h3><p class="mut mt8">{text}</p>'
            f'{viz(num, t)}<ul class="chips">{"".join(f"<li>{c}</li>" for c in chips)}</ul>'
            f'{f"<a class=\"lk mt16\" href=\"#auto\">{t['cta2']}</a>" if star else ""}</article>')
    steps = "".join(f'<li><span class="mono">0{i + 1}</span><b>{h}</b><p class="sm mut">{p}</p></li>' for i, (h, p) in enumerate(t["steps"]))
    styles = "".join(f'<button type="button" class="{"on" if i == 1 else ""}" aria-pressed="{"true" if i == 1 else "false"}" data-style="{i}">{s}</button>' for i, s in enumerate(t["styles"]))
    controls = "".join(f'<div class="ctl"><b>{h}</b><p class="sm mut mt8">{p}</p></div>' for h, p in t["controls"])
    faq = "".join(f'<details class="faq"><summary>{q}</summary><p>{a}</p></details>' for q, a in t["faq"])
    lg = t["legend"]
    return f'''<section class="ai-hero ai-nexus-hero">{B.media("ai-candles-loop", "ai-candles", "ai-bg", eager=True)}<div class="ai-grid" aria-hidden="true"></div>
<div class="wrap ai-hero-in"><div><span class="ai-eyebrow"><i></i>{t["eyebrow"]}</span><h1 class="mt24">{t["h1"]}</h1><p class="lead mt24">{t["lead"]}</p>
<div class="row wr mt32"><a class="b p lg2" href="{L("/demo")}">{t["cta1"]}</a><a class="b o lg2" href="#auto">{t["cta2"]}</a></div><p class="xs mut3 mt16">{t["note"]}</p></div></div></section>

<section class="ai-live"><div class="wrap"><div class="ai-console" role="img" aria-label="{t["sample"]}"><div class="row sb ai-console-h"><span class="row" style="gap:8px"><i class="live"></i><b class="mono sm">{t["console"]}</b></span><span class="xs mut3">{t["sample"]}</span></div>
<ul class="ai-log" data-log>{log}</ul><div class="ai-meters"><div><span class="xs mut3">CPU</span><div class="bar"><i data-meter style="--m:0.62"></i></div></div><div><span class="xs mut3">{t["viz_risk"]}</span><div class="bar"><i data-meter style="--m:0.48"></i></div></div></div></div></div></section>

<section class="sec"><div class="wrap"><span class="mono k">{t["features_k"]}</span><h2 class="mt16">{t["features_h"]}</h2><div class="ai-bento mt48">{"".join(feats)}</div></div></section>

<section class="sec ai-auto" id="auto"><div class="wrap"><span class="mono k">{t["auto_k"]}</span><h2 class="mt16" style="max-width:760px">{t["auto_h"]}</h2><p class="lead mt16" style="max-width:720px">{t["auto_lead"]}</p>
<ol class="ai-steps mt48">{steps}</ol>

<div class="sim mt64" data-sim data-unit-m="{t["unit_m"]}" data-unit-m1="{t["unit_m1"]}" data-assume="{t["assume"]}">
<div class="sim-head"><span class="mono k">{t["sim_k"]}</span><h3 class="mt8">{t["sim_h"]}</h3><p class="mut mt8">{t["sim_lead"]}</p></div>
<form class="sim-ctl" onsubmit="return false">
{slider("amount", t["amount"], 0, 100, 1, 50, "$5,000")}
<div class="sl"><span class="lab">{t["style"]}</span><div class="seg w3 mt8" role="group" aria-label="{t["style"]}">{styles}</div></div>
{slider("risk", t["risk"], 0.25, 3, 0.25, 1, "1.00%")}
{slider("months", t["months"], 1, 24, 1, 12, "12")}
{slider("stop", t["stop"], 5, 50, 1, 20, "20%")}
<label class="tgl"><input type="checkbox" name="news" checked><i></i><span>{t["news"]}</span></label>
<button type="button" class="b q w" data-rerun>{t["rerun"]}</button>
</form>
<div class="sim-out">
<div class="sim-kpis"><div class="kpi mid"><span class="xs mut3">{t["out_mid"]}</span><b class="mono" data-k="mid">$0</b><span class="xs" data-d="mid"></span><span class="xs mut3">{t["out_mid_s"]}</span></div>
<div class="kpi"><span class="xs mut3">{t["out_good"]}</span><b class="mono" data-k="good">$0</b><span class="xs" data-d="good"></span><span class="xs mut3">{t["out_good_s"]}</span></div>
<div class="kpi"><span class="xs mut3">{t["out_bad"]}</span><b class="mono" data-k="bad">$0</b><span class="xs" data-d="bad"></span><span class="xs mut3">{t["out_bad_s"]}</span></div></div>
<figure class="sim-chart"><figcaption class="row sb wr"><span class="sm">{t["chart"]}</span><span class="legend xs"><i class="lb"></i>{lg[0]}<i class="lm"></i>{lg[1]}<i class="lp"></i>{lg[2]}<i class="ls"></i>{lg[3]}</span></figcaption>
<svg viewBox="0 0 640 260" preserveAspectRatio="none" data-chart aria-hidden="true"></svg></figure>
<div class="sim-risk"><div><span class="xs mut3">{t["out_max"]}</span><b class="mono red" data-k="max">$0</b></div><div><span class="xs mut3">{t["out_hit"]}</span><b class="mono" data-k="hit">0%</b></div></div>
<p class="xs mut3 sim-assume" data-assume-out></p>
</div></div></div></section>

<section class="sec"><div class="wrap"><span class="mono k">{t["control_k"]}</span><h2 class="mt16">{t["control_h"]}</h2><div class="ai-ctls mt48">{controls}</div></div></section>

<section class="sec t"><div class="wrap" style="max-width:860px"><h2>{t["faq_h"]}</h2><div class="mt32">{faq}</div></div></section>
{B.cta_band(lang)}'''


def build_all():
    entries = []
    for lang in ("en", "ar"):
        t = T[lang]
        B.write(lang, "/ai", B.page(lang, "/ai", t["title"], t["desc"], body(lang), "AI"))
        entries.append({"t": t["title"], "d": t["desc"], "u": B.localize("/ai", lang), "l": lang})
    return entries
