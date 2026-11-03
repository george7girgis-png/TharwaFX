# Site content that the UI/UX book leaves implicit: routes, menus, link targets,
# extra market and instrument data, missing FAQ answers and the image manifest.
# Values marked with * are sample trading values, as in the book.

# Access pages (register, log in) are built locally; the client area behind them is phase B.
CLIENT = ""

# Book screen id -> public path. Arabic screens share the English template id.
BOOK_PAGES = {
    "P01": "/", "P02": "/why-tharwa", "P03": "/accounts", "P04": "/accounts/raw-spread",
    "P05": "/accounts/compare", "P06": "/accounts/islamic", "P07": "/demo", "P08": "/markets",
    "P09": "/markets/forex", "P10": "/markets/xauusd", "P11": "/trading/conditions",
    "P12": "/trading/spreads", "P13": "/trading/leverage", "P14": "/trading/hours",
    "P15": "/trading/swap", "P16": "/funding/deposits", "P17": "/funding/withdrawals",
    "P18": "/platforms", "P19": "/platforms/mt5", "P20": "/platforms/webtrader",
    "P21": "/platforms/app", "P22": "/platforms/tradingview", "P23": "/platforms/tools",
    "P24": "/academy", "P25": "/academy/forex-basics/3", "P26": "/academy/webinars",
    "P27": "/academy/media", "P28": "/blog", "P29": "/blog/article",
    "P30": "/tools/calculators", "P31": "/tools/calendar", "P32": "/tools/glossary",
    "P33": "/help", "P34": "/help/article", "P35": "/contact", "P36": "/about",
    "P37": "/regulation", "P38": "/stay-safe", "P39": "/careers", "P40": "/partners",
    "P41": "/legal", "P42": "/legal/risk", "P43": "/search",
}

# Label -> path, used for crumbs, footer lists, buttons and context links.
LINKS = {
    "en": {
        "Home": "/", "Trading": "/trading/conditions", "Accounts": "/accounts",
        "Standard": "/accounts/standard", "Raw Spread": "/accounts/raw-spread",
        "Islamic": "/accounts/islamic", "Demo": "/demo", "Compare accounts": "/accounts/compare",
        "Compare": "/accounts/compare", "Markets": "/markets", "All markets": "/markets",
        "Forex": "/markets/forex", "Gold and metals": "/markets/metals", "Indices": "/markets/indices",
        "Stocks": "/markets/stocks", "Commodities": "/markets/commodities", "Crypto": "/markets/crypto",
        "Trading conditions": "/trading/conditions", "Conditions": "/trading/conditions",
        "Spreads": "/trading/spreads", "Leverage and margin": "/trading/leverage",
        "Leverage": "/trading/leverage", "Trading hours": "/trading/hours", "Hours": "/trading/hours",
        "Swap rates": "/trading/swap", "Swap": "/trading/swap", "Deposits": "/funding/deposits",
        "Withdrawals": "/funding/withdrawals", "Platforms": "/platforms",
        "MetaTrader 5": "/platforms/mt5", "WebTrader": "/platforms/webtrader",
        "Tharwa app": "/platforms/app", "TradingView": "/platforms/tradingview",
        "Trading tools": "/platforms/tools", "Tools": "/platforms/tools", "Academy": "/academy",
        "Courses": "/academy", "Webinars": "/academy/webinars", "Videos": "/academy/media",
        "Podcast": "/academy/media", "Videos and podcast": "/academy/media", "Blog": "/blog",
        "Calculators": "/tools/calculators", "Economic calendar": "/tools/calendar",
        "Calendar": "/tools/calendar", "Glossary": "/tools/glossary", "Help centre": "/help",
        "Help": "/help", "Contact": "/contact", "About": "/about", "About Tharwa": "/about",
        "Why Tharwa": "/why-tharwa", "Regulation": "/regulation", "Stay safe": "/stay-safe",
        "Careers": "/careers", "Partners": "/partners", "Legal documents": "/legal", "Legal": "/legal",
        "Risk disclosure": "/legal/risk", "Privacy": "/legal", "Terms": "/legal", "Cookies": "/legal",
        "Traders": "/", "Funding": "/funding/deposits", "Research": "/blog", "VPS": "/platforms/tools",
        "Servers": "/platforms/tools", "Search": "/search", "Forex basics": "/academy/forex-basics/3",
        "Market analysis": "/blog/article", "What a stronger dollar means for gold this week": "/blog/article",
        "Learning": "/academy", "Lesson": "/academy/forex-basics/3", "Article": "/help/article",
        "Virtual private server": "/platforms/tools", "Trading servers": "/platforms/mt5",
        "Market research": "/blog", "Getting started": "/search?q=getting+started",
        "Verification": "/search?q=verification", "MT5 and trading": "/search?q=mt5",
        "Account security": "/search?q=security", "Withdraw your money": "/funding/withdrawals",
        "Gulf time": "/tools/calendar", "Introducing brokers": "/contact#message",
        "Affiliates": "/contact#message", "Money managers": "/contact#message",
    },
    "ar": {
        "الرئيسية": "/", "التداول": "/trading/conditions", "الحسابات": "/accounts",
        "ستاندرد": "/accounts/standard", "رو سبريد": "/accounts/raw-spread", "إسلامي": "/accounts/islamic",
        "قارن الحسابات": "/accounts/compare", "الأسواق": "/markets", "كل الأسواق": "/markets",
        "العملات": "/markets/forex", "الذهب والمعادن": "/markets/metals", "المؤشرات": "/markets/indices",
        "الأسهم": "/markets/stocks", "السلع": "/markets/commodities", "العملات الرقمية": "/markets/crypto",
        "الفروقات السعرية": "/trading/spreads", "الرافعة والهامش": "/trading/leverage",
        "ساعات التداول": "/trading/hours", "رسوم التبييت": "/trading/swap", "الإيداع": "/funding/deposits",
        "السحب": "/funding/withdrawals", "المنصات": "/platforms", "MetaTrader 5": "/platforms/mt5",
        "WebTrader": "/platforms/webtrader", "تطبيق ثروة": "/platforms/app", "TradingView": "/platforms/tradingview",
        "أدوات التداول": "/platforms/tools", "الأدوات": "/platforms/tools", "الأكاديمية": "/academy",
        "أكاديمية ثروة": "/academy", "ابدأ التعلم": "/academy", "المساعدة": "/help",
        "مركز المساعدة": "/help", "الحاسبات": "/tools/calculators", "المصطلحات": "/tools/glossary",
        "المفكرة الاقتصادية": "/tools/calendar", "اتصل بنا": "/contact", "الشركة": "/about",
        "عن ثروة": "/about", "التراخيص": "/regulation", "الوثائق القانونية": "/legal",
        "الحماية من الاحتيال": "/stay-safe", "الوظائف": "/careers", "الشركاء": "/partners",
        "المتداولون": "/", "الخصوصية": "/legal", "الشروط": "/legal", "ملفات الارتباط": "/legal",
        "إفصاح المخاطر": "/legal/risk", "التجريبي": "/demo",
    },
}

# Pages that exist in Arabic. Everything else falls back to the English page.
AR_PAGES = {"/", "/ai", "/accounts", "/markets/forex", "/funding/deposits", "/tools/calculators", "/help", "/register", "/login"}

# Buttons and links whose target does not depend on context.
ACTIONS = {
    "en": {
        "Open account": CLIENT + "/register", "Log in": CLIENT + "/login",
        "Try a free demo": "/demo", "Register": "soon", "Open Standard": CLIENT + "/register?account=standard",
        "Open Raw Spread": CLIENT + "/register?account=raw-spread", "Open Islamic": CLIENT + "/register?account=islamic",
        "Deposit": "/login", "Withdraw": "/login", "Start chat": "chat",
        "Create ticket": "/contact#message", "Become a partner": "/contact#message",
        "Report now": "/contact#message", "Go home": "/", "See status": "soon", "Read why": "/legal",
        "Open MT5": "/platforms/mt5", "Download for Windows": "soon", "App Store": "soon",
        "Google Play": "soon", "Previous": "/academy", "Next lesson": "soon", "Apply": "soon",
        "VPS terms": "/legal", "Server list": "/platforms/mt5", "Read research": "/blog",
        "Open calendar": "/tools/calendar", "Use calculators": "/tools/calculators",
        "Phase 2": None, "Verify on the regulator's site": "soon", "PDF": "soon", "Open": "soon",
        "Spreads": "/trading/spreads", "Trading conditions": "/trading/conditions",
        "Deposits": "/funding/deposits", "Contact": "/contact", "All markets": "/markets",
        "Compare accounts": "/accounts/compare", "Start learning": "/academy",
    },
    "ar": {
        "افتح حساباً": CLIENT + "/register", "تسجيل الدخول": CLIENT + "/login",
        "جرّب حساباً تجريبياً": "/demo", "افتح ستاندرد": CLIENT + "/register?account=standard",
        "افتح رو سبريد": CLIENT + "/register?account=raw-spread", "افتح إسلامي": CLIENT + "/register?account=islamic",
        "ابدأ المحادثة": "chat", "أنشئ طلباً": "/contact#message", "كل الأسواق": "/markets",
        "قارن الحسابات": "/accounts/compare", "ابدأ التعلم": "/academy", "إيداع": "/login",
    },
}

# Generic link labels resolved from the nearest preceding heading.
CONTEXT_LABELS = {"View market", "View", "Learn more", "Details", "عرض السوق", "التفاصيل", "PDF"}

MEGA = {
    "en": [
        ("Trading", [("Accounts", [("Overview", "/accounts"), ("Standard", "/accounts/standard"), ("Raw Spread", "/accounts/raw-spread"), ("Islamic", "/accounts/islamic"), ("Demo", "/demo")]),
                     ("Pricing", [("Conditions", "/trading/conditions"), ("Spreads", "/trading/spreads"), ("Leverage", "/trading/leverage"), ("Hours", "/trading/hours"), ("Swap", "/trading/swap")]),
                     ("Funding", [("Deposits", "/funding/deposits"), ("Withdrawals", "/funding/withdrawals")])]),
        ("Markets", [("Markets", [("All markets", "/markets"), ("Forex", "/markets/forex"), ("Gold and metals", "/markets/metals"), ("Indices", "/markets/indices")]),
                     ("", [("Stocks", "/markets/stocks"), ("Commodities", "/markets/commodities"), ("Crypto", "/markets/crypto")])]),
        ("Platforms", [("Trade", [("MetaTrader 5", "/platforms/mt5"), ("WebTrader", "/platforms/webtrader"), ("Tharwa app", "/platforms/app"), ("TradingView", "/platforms/tradingview"), ("Trade with AI", "/ai")]),
                       ("Tools", [("VPS", "/platforms/tools"), ("Servers", "/platforms/tools"), ("Research", "/blog")])]),
        ("Academy", [("Learn", [("Courses", "/academy"), ("Webinars", "/academy/webinars"), ("Videos", "/academy/media"), ("Podcast", "/academy/media")])]),
        ("Help", [("Support", [("Help centre", "/help"), ("Contact", "/contact")]),
                  ("Tools", [("Calculators", "/tools/calculators"), ("Calendar", "/tools/calendar"), ("Glossary", "/tools/glossary"), ("Blog", "/blog")])]),
        ("Company", [("About", [("Why Tharwa", "/why-tharwa"), ("About", "/about"), ("Careers", "/careers"), ("Partners", "/partners")]),
                     ("Trust", [("Regulation", "/regulation"), ("Stay safe", "/stay-safe"), ("Legal", "/legal")])]),
    ],
    "ar": [
        ("التداول", [("الحسابات", [("نظرة عامة", "/accounts"), ("ستاندرد", "/accounts/standard"), ("رو سبريد", "/accounts/raw-spread"), ("إسلامي", "/accounts/islamic"), ("تجريبي", "/demo")]),
                     ("التسعير", [("الشروط", "/trading/conditions"), ("الفروقات السعرية", "/trading/spreads"), ("الرافعة", "/trading/leverage"), ("الساعات", "/trading/hours"), ("رسوم التبييت", "/trading/swap")]),
                     ("التمويل", [("الإيداع", "/funding/deposits"), ("السحب", "/funding/withdrawals")])]),
        ("الأسواق", [("الأسواق", [("كل الأسواق", "/markets"), ("العملات", "/markets/forex"), ("الذهب والمعادن", "/markets/metals"), ("المؤشرات", "/markets/indices")]),
                     ("", [("الأسهم", "/markets/stocks"), ("السلع", "/markets/commodities"), ("العملات الرقمية", "/markets/crypto")])]),
        ("المنصات", [("تداول", [("MetaTrader 5", "/platforms/mt5"), ("WebTrader", "/platforms/webtrader"), ("تطبيق ثروة", "/platforms/app"), ("TradingView", "/platforms/tradingview"), ("التداول بالذكاء الاصطناعي", "/ai")]),
                     ("الأدوات", [("خادم افتراضي VPS", "/platforms/tools"), ("الخوادم", "/platforms/tools"), ("الأبحاث", "/blog")])]),
        ("الأكاديمية", [("تعلّم", [("الدورات", "/academy"), ("الندوات", "/academy/webinars"), ("الفيديوهات", "/academy/media"), ("البودكاست", "/academy/media")])]),
        ("المساعدة", [("الدعم", [("مركز المساعدة", "/help"), ("اتصل بنا", "/contact")]),
                      ("الأدوات", [("الحاسبات", "/tools/calculators"), ("المفكرة", "/tools/calendar"), ("المصطلحات", "/tools/glossary"), ("المدونة", "/blog")])]),
        ("الشركة", [("عن ثروة", [("لماذا ثروة", "/why-tharwa"), ("من نحن", "/about"), ("الوظائف", "/careers"), ("الشركاء", "/partners")]),
                    ("الثقة", [("التراخيص", "/regulation"), ("الحماية من الاحتيال", "/stay-safe"), ("الوثائق القانونية", "/legal")])]),
    ],
}

# FAQ answers the book leaves collapsed.
FAQ = {
    "Which currencies can I hold?": "Accounts can be held in USD, AED or EUR*. You choose the base currency when you open the account.",
    "Is there a demo for each account?": "Yes. A demo is available for Standard, Raw Spread and Islamic, with the same conditions and virtual funds.",
    "Why was my deposit declined?": "The most common reasons are a card that is not in your name, a bank block on trading payments, or a limit on your card. Try another method or contact us and we will check the reason with the provider.",
    "How do I reset my MT5 password?": "Open your client area, go to Accounts, choose the account and select Reset password. The new password is sent to your registered email.",
    "Can I withdraw to another person's account?": "No. Withdrawals go only to an account or card in your own name. This protects you and is required by anti-money-laundering rules.",
    "ما العملات المتاحة للحساب؟": "يمكن فتح الحساب بالدولار الأمريكي أو الدرهم الإماراتي أو اليورو*. تختار العملة الأساسية عند فتح الحساب.",
    "هل يوجد حساب تجريبي لكل نوع؟": "نعم. يتوفر حساب تجريبي لحسابات ستاندرد ورو سبريد والإسلامي، بنفس الشروط وبأموال افتراضية.",
    "لماذا تم رفض إيداعي؟": "أكثر الأسباب شيوعاً: بطاقة ليست باسمك، أو حظر من البنك على مدفوعات التداول، أو تجاوز حد البطاقة. جرّب طريقة أخرى أو تواصل معنا لنتحقق من السبب مع مزوّد الدفع.",
    "كيف أعيد تعيين كلمة مرور MT5؟": "افتح منطقة العميل، ثم الحسابات، واختر الحساب ثم إعادة تعيين كلمة المرور. تصلك كلمة المرور الجديدة على بريدك المسجّل.",
    "هل يمكنني السحب إلى حساب شخص آخر؟": "لا. يتم السحب فقط إلى حساب أو بطاقة باسمك. هذا يحميك وتفرضه قواعد مكافحة غسل الأموال.",
}

# Sample instruments for market and instrument pages. price, spread, size, tick, leverage, swap, session
INSTR = {
    "EURUSD": ("Euro against the US dollar", "forex", 1.16695, "0.6", "100,000 EUR", "0.00001", 500, "−6.2 / +2.1", "Sun 22:05 to Fri 21:55 GMT"),
    "GBPUSD": ("British pound against the US dollar", "forex", 1.32588, "0.7", "100,000 GBP", "0.00001", 500, "−4.8 / +1.0", "Sun 22:05 to Fri 21:55 GMT"),
    "USDJPY": ("US dollar against the Japanese yen", "forex", 152.418, "0.5", "100,000 USD", "0.001", 500, "+8.3 / −16.4", "Sun 22:05 to Fri 21:55 GMT"),
    "AUDUSD": ("Australian dollar against the US dollar", "forex", 0.65912, "0.7", "100,000 AUD", "0.00001", 500, "−3.9 / +0.6", "Sun 22:05 to Fri 21:55 GMT"),
    "USDCHF": ("US dollar against the Swiss franc", "forex", 0.88341, "0.8", "100,000 USD", "0.00001", 500, "+5.1 / −12.2", "Sun 22:05 to Fri 21:55 GMT"),
    "USDAED": ("US dollar against the UAE dirham", "forex", 3.67250, "6.0", "100,000 USD", "0.00001", 100, "−1.2 / −1.2", "Mon 04:00 to Fri 20:00 GMT"),
    "XAUUSD": ("Gold against the US dollar", "metals", 2398.25, "0.7", "100 oz", "0.01", 200, "−38.4 / +14.2", "Sun 22:05 to Fri 20:55 GMT"),
    "XAGUSD": ("Silver against the US dollar", "metals", 28.415, "2.5", "5,000 oz", "0.001", 100, "−6.1 / +1.8", "Sun 22:05 to Fri 20:55 GMT"),
    "XPTUSD": ("Platinum against the US dollar", "metals", 962.40, "3.0", "100 oz", "0.01", 50, "−11.0 / +2.4", "Sun 23:05 to Fri 20:55 GMT"),
    "US30": ("Wall Street 30 index", "indices", 42319.2, "1.4", "1 × index", "0.1", 200, "−7.9 / +2.2", "Sun 23:05 to Fri 20:55 GMT"),
    "US500": ("US 500 index", "indices", 5842.6, "0.5", "1 × index", "0.1", 200, "−1.1 / +0.3", "Sun 23:05 to Fri 20:55 GMT"),
    "NAS100": ("US Tech 100 index", "indices", 20518.4, "1.0", "1 × index", "0.1", 200, "−3.9 / +1.1", "Sun 23:05 to Fri 20:55 GMT"),
    "GER40": ("Germany 40 index", "indices", 19364.0, "1.0", "1 × index", "0.1", 200, "−3.0 / −0.4", "Mon 06:15 to Fri 20:00 GMT"),
    "UK100": ("UK 100 index", "indices", 8271.5, "1.0", "1 × index", "0.1", 200, "−1.4 / +0.2", "Mon 07:00 to Fri 20:00 GMT"),
    "AAPL": ("Apple Inc.", "stocks", 228.52, "0.08", "1 share", "0.01", 20, "−0.05 / +0.01", "Mon to Fri 14:30 to 21:00 GMT"),
    "MSFT": ("Microsoft Corp.", "stocks", 418.30, "0.12", "1 share", "0.01", 20, "−0.09 / +0.02", "Mon to Fri 14:30 to 21:00 GMT"),
    "NVDA": ("NVIDIA Corp.", "stocks", 138.07, "0.06", "1 share", "0.01", 20, "−0.03 / +0.01", "Mon to Fri 14:30 to 21:00 GMT"),
    "AMZN": ("Amazon.com Inc.", "stocks", 197.12, "0.08", "1 share", "0.01", 20, "−0.04 / +0.01", "Mon to Fri 14:30 to 21:00 GMT"),
    "TSLA": ("Tesla Inc.", "stocks", 251.44, "0.10", "1 share", "0.01", 20, "−0.05 / +0.01", "Mon to Fri 14:30 to 21:00 GMT"),
    "USOIL": ("US crude oil", "commodities", 78.416, "2.3", "1,000 barrels", "0.001", 100, "−9.4 / +3.1", "Sun 23:05 to Fri 20:55 GMT"),
    "UKOIL": ("Brent crude oil", "commodities", 81.902, "2.5", "1,000 barrels", "0.001", 100, "−8.7 / +2.6", "Mon 01:05 to Fri 20:55 GMT"),
    "NATGAS": ("US natural gas", "commodities", 2.814, "8.0", "10,000 MMBtu", "0.001", 50, "−4.2 / +0.8", "Sun 23:05 to Fri 20:55 GMT"),
    "BTCUSD": ("Bitcoin against the US dollar", "crypto", 68426.7, "24.0", "1 BTC", "0.1", 5, "−20% / −20% yearly", "24/7"),
    "ETHUSD": ("Ether against the US dollar", "crypto", 2614.30, "2.4", "1 ETH", "0.01", 5, "−20% / −20% yearly", "24/7"),
    "SOLUSD": ("Solana against the US dollar", "crypto", 158.42, "0.35", "1 SOL", "0.01", 5, "−20% / −20% yearly", "24/7"),
}

# Generated market pages modelled on the forex template (P09).
MARKETS = {
    "metals": dict(name="Gold and metals", title="Trade gold and metals with clear costs",
                   lead="Spot gold, silver and platinum, priced against the US dollar.",
                   pills=["Gold", "Silver", "Platinum"], hours="23 hours, 5 days",
                   hours_t="Metals trade from Sunday evening to Friday evening, with a short daily break.",
                   syms=["XAUUSD", "XAGUSD", "XPTUSD"]),
    "indices": dict(name="Indices", title="Trade global indices in one place",
                    lead="Take a view on a whole market with a single trade.",
                    pills=["US", "Europe", "Asia"], hours="Hours per index",
                    hours_t="Each index follows its home exchange, with extended sessions on US benchmarks.",
                    syms=["US30", "US500", "NAS100", "GER40", "UK100"]),
    "stocks": dict(name="Stocks", title="Trade shares of leading companies",
                   lead="CFDs on US, European and GCC names*, without owning the underlying shares.",
                   pills=["US", "Europe", "GCC"], hours="Exchange hours",
                   hours_t="Stocks trade while their exchange is open. Gaps at the open are common.",
                   syms=["AAPL", "MSFT", "NVDA", "AMZN", "TSLA"]),
    "commodities": dict(name="Commodities", title="Trade oil, gas and softs",
                        lead="Energy and agricultural prices, with costs shown before you trade.",
                        pills=["Energy", "Softs"], hours="Hours per product",
                        hours_t="Each commodity follows its futures venue, with a daily break.",
                        syms=["USOIL", "UKOIL", "NATGAS"]),
    "crypto": dict(name="Crypto", title="Trade crypto where permitted",
                   lead="Bitcoin, Ether and more as CFDs, seven days a week. Availability depends on your region.",
                   pills=["Major coins"], hours="24 hours, 7 days",
                   hours_t="Crypto trades every day, but prices can move sharply at any hour.",
                   syms=["BTCUSD", "ETHUSD", "SOLUSD"]),
}
MARKET_NAMES = {"forex": "Forex", "metals": "Gold and metals", "indices": "Indices",
                "stocks": "Stocks", "commodities": "Commodities", "crypto": "Crypto"}

# Images to generate (Higgsfield). Missing files fall back to the book's gradients.
STYLE = ("Dark, premium fintech brand imagery. Near-black background (#000000 to #0E0E0E), "
         "with signal green (#34E834) as the only accent colour, used sparingly as light and glow. "
         "Clean, minimal, cinematic, high detail, no text, no letters, no logos, no watermarks, no people's faces.")
IMAGES = {
    "home-hero": ("16:9", "Abstract wide scene: a dotted world map globe on the right edge seen in the dark, thin glowing green candlestick chart lines rising across the frame, soft green horizon glow at the bottom, lots of empty black space on the left for headline text."),
    "market-forex": ("16:9", "Abstract macro of overlapping translucent currency symbol-free banknote textures and fine guilloche line patterns, lit in green, dark and moody."),
    "market-metals": ("16:9", "Stack of polished gold bullion bars on black glass, rim-lit with subtle green reflections, shallow depth of field."),
    "market-indices": ("16:9", "Night aerial view of a financial district skyline with glowing green light trails between towers, abstracted and dark."),
    "market-stocks": ("16:9", "Abstract close-up of a glowing market depth ladder made of thin light bars, receding into darkness, green accent light."),
    "market-commodities": ("16:9", "Oil refinery silhouette at night with green-tinted sodium lights and steam, cinematic, very dark."),
    "market-crypto": ("16:9", "Abstract network of glowing nodes and thin connecting lines in a dark void, green highlights, depth of field."),
    "video-first-order": ("16:9", "Close-up of a laptop keyboard and a dark trading chart on screen with a single green candle highlighted, shallow depth of field."),
    "video-stop-loss": ("16:9", "Abstract dark chart with a horizontal glowing red-orange line as a safety level beneath a green price line, minimal."),
    "video-deposit": ("16:9", "A contactless payment card on a dark desk next to a smartphone with a softly glowing green screen, minimal."),
    "video-install-mt5": ("16:9", "Dark desktop workstation with two monitors showing abstract candlestick charts, green ambient light, no readable text."),
    "blog-gold-dollar": ("16:9", "Gold coin and a dollar-green glow balanced on a dark scale, conceptual, dramatic lighting."),
    "about-office": ("21:9", "Modern dark office interior at night overlooking a Gulf city skyline (Dubai style), floor-to-ceiling windows, green accent lighting, empty desks."),
    "careers-team": ("21:9", "Contemporary dark collaborative workspace with long tables, laptops glowing, warm and green accent lighting, no visible faces."),
    "home-ai": ("16:9", "A dark planet Earth on the right half of the frame made of millions of fine green light dots, wrapped in a delicate glowing neural lattice of thin green filaments and bright nodes, luminous arcs of light travelling between the Middle East and the world's financial centres, a soft green atmospheric rim light, deep space black, the whole left half of the frame empty and dark for headline text."),
    "auth-panel": ("3:4", "Cinematic view of the Dubai skyline at blue hour from high above, slender glass towers fading into haze, thin green light trails of traffic far below, deep shadows, quiet and premium, empty dark sky in the upper half."),
    "platform-stage": ("3:4", "Low angle across a smooth, unbroken polished black stone desk at night, a soft pool of light on the empty surface in the centre, soft green rim light from behind, out-of-focus city lights bokeh through a tall window. Nothing on the desk: no objects, no holes, no devices, no screens."),
    "ai-hero": ("16:9", "Abstract futuristic visual: a translucent neural network of fine glowing green filaments and small bright nodes taking shape above a dark candlestick price chart, floating particles, shallow depth of field, a vast empty black area on the left half for headline text."),
    "ai-core": ("16:9", "A floating faceted glass sphere on the right side of the frame with a bright glowing green neural core inside, thin orbiting rings of tiny holographic candlestick bars circling it. Tangled grey noisy price lines stream into the sphere from the far right and leave it as clean, bright green rising trend lines. Black void, fine floating particles, cinematic depth of field, the whole left half of the frame empty and dark for headline text."),
    "cta-desert": ("16:9", "Sweeping desert sand dunes at dusk under a deep near-black sky, the dune crests catching a thin line of soft green light, gentle wind lifting fine sand, vast and calm, empty sky across the top half."),
}
# Ambient loops made from the stills above with Kling 2.5 Turbo (image to video). Muted, decorative only.
VIDEOS = {
    "hero-loop": ("home-hero", "Very slow cinematic push in. The dotted globe turns slowly, the thin green chart lines glow and drift gently upward, faint particles float. Calm, seamless, no camera shake."),
    "home-ai-loop": ("home-ai", "Locked-off camera, very slow drift. The dotted green globe turns slowly. A fine neural network of thin glowing green lines and tiny bright nodes gradually grows across the continents, linking the Middle East to the rest of the world, and small pulses of light race along the connections like synapses firing. The atmospheric green glow breathes softly. The left half of the frame stays empty and pure black, no blue tint. Premium, calm, seamless."),
    # phone-mock is a composite: a Soul phone render with the real site screenshot warped onto its screen.
    "phone-loop": ("phone-mock", "Completely static camera: no zoom, no pan, no push in, no movement of the phone at all. The phone and everything on its screen stay frozen and identical in every frame. Only the light changes: the green ring of the pedestal slowly breathes brighter and dimmer, a soft glint of light slides once along the phone's metal edge, and a few faint particles drift in the dark background. No lightning, no sparks, no electricity. Premium, calm, seamless."),
    "phone-loop-ar": ("phone-mock-ar", "Completely static camera: no zoom, no pan, no push in, no movement of the phone at all. The phone and everything on its screen stay frozen and identical in every frame. Only the light changes: the green ring of the pedestal slowly breathes brighter and dimmer, a soft glint of light slides once along the phone's metal edge, and a few faint particles drift in the dark background. No lightning, no sparks, no electricity. Premium, calm, seamless."),
    "auth-loop": ("auth-panel", "Slow aerial drift over the skyline at blue hour, haze moving softly between the towers, green traffic light trails flowing far below. Calm and smooth."),
    "metals-loop": ("market-metals", "Slow orbiting camera move around the gold bars, reflections sliding across the polished metal, subtle green glints. Smooth and premium."),
    "ai-loop": ("ai-hero", "The neural network slowly pulses, light travels along the green filaments between the nodes, particles drift, very slow push in. Calm, seamless, no camera shake."),
    "ai-core-loop": ("ai-core", "Locked-off camera, no zoom, no pan. The glass sphere rotates very slowly on its axis while light glints across its facets. The green core inside pulses softly like a heartbeat. The fine grey threads on the right keep flowing gently into the sphere, and the small green chart lines inside the sphere shimmer and climb upward. Nothing new appears: the left half of the frame stays empty and pure black, the background stays pure black with no blue. Calm, premium, seamless."),
    "cta-loop": ("cta-desert", "Gentle wind carries fine sand over the dune crests, the thin green light on the ridges shimmers slowly, very slow push forward. Calm and seamless."),
}

# Glossary (P32). The book shows the M entries; the rest follow the same pattern.
GLOSSARY = [
    ("Ask", "سعر الطلب", "The price at which you can buy."),
    ("Balance", "الرصيد", "Money in your account, not counting open positions."),
    ("Base currency", "العملة الأساسية", "The first currency in a pair. In EURUSD it is the euro."),
    ("Bid", "سعر العرض", "The price at which you can sell."),
    ("CFD", "عقد الفروقات", "A contract that pays the change in an asset's price, without owning the asset."),
    ("Commission", "العمولة", "A set fee per lot, charged on Raw Spread accounts."),
    ("Drawdown", "التراجع", "The fall from a peak in your account equity to a low point."),
    ("Equity", "حقوق الملكية", "Your balance plus or minus the profit or loss on open positions."),
    ("Expert advisor", "المستشار الخبير", "An automated trading program that runs inside MetaTrader 5."),
    ("Free margin", "الهامش الحر", "Equity that is not tied up as margin and can open new positions."),
    ("Gap", "الفجوة", "A jump in price between one quote and the next, often at the market open."),
    ("Hedging", "التحوط", "Holding opposite positions to reduce risk."),
    ("Instrument", "الأداة", "Anything you can trade, such as a currency pair, index or stock."),
    ("Leverage", "الرافعة المالية", "Borrowed exposure that lets you control a larger position than your deposit."),
    ("Lot", "اللوت", "The standard trade size. One lot of forex is 100,000 units of the base currency."),
    ("Margin", "الهامش", "Money set aside to keep a leveraged position open."),
    ("Margin call", "نداء الهامش", "A warning that your equity is close to the level needed to hold your positions."),
    ("Market order", "أمر السوق", "An order to buy or sell straight away at the best available price."),
    ("Micro lot", "لوت صغير", "1,000 units of the base currency, or 0.01 of a standard lot."),
    ("Order", "الأمر", "An instruction to open or close a position."),
    ("Pip", "النقطة", "The fourth decimal place on most currency pairs, or the second on yen pairs."),
    ("Pending order", "الأمر المعلّق", "An order that waits until the price reaches a level you set."),
    ("Quote currency", "عملة التسعير", "The second currency in a pair. In EURUSD it is the US dollar."),
    ("Requote", "إعادة التسعير", "A new price offered when the market moves before your order fills."),
    ("Slippage", "الانزلاق السعري", "The difference between the price you asked for and the price you got."),
    ("Spread", "الفارق السعري", "The difference between the bid and ask prices."),
    ("Stop loss", "وقف الخسارة", "An order that closes a position at a set loss."),
    ("Stop-out", "الإغلاق القسري", "Automatic closing of positions when margin level falls too low."),
    ("Swap", "رسوم التبييت", "Interest charged or paid for holding a position overnight."),
    ("Take profit", "جني الأرباح", "An order that closes a position at a set profit."),
    ("Volatility", "التقلب", "How much and how quickly a price moves."),
    ("Volume", "الحجم", "The size of a trade, in lots."),
]

# Calculator data: contract size, pip size and quote currency per instrument.
CALC = {
    "forex": (100000, 0.0001), "metals": (100, 0.1), "indices": (1, 1), "stocks": (1, 0.01),
    "commodities": (1000, 0.01), "crypto": (1, 1),
}
CALC_OVERRIDES = {"USDJPY": (100000, 0.01), "XAGUSD": (5000, 0.01), "NATGAS": (10000, 0.001)}
