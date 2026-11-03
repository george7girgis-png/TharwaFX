"""Arabic text for the client screens the book draws only in English.

Keys are the exact English text as it appears on the built page (text between tags, or a
placeholder, aria-label or value). Wording follows the book's own Arabic screens (A01, A06,
A09): Modern Standard Arabic, Western digits, brand and instrument names left in Latin script.
Text not listed here (symbols, account numbers, card masks) stays as it is.
"""

AR = {
    # Shell
    "Home": "الرئيسية", "Accounts": "حساباتي", "Deposit": "إيداع", "Withdraw": "سحب", "Transfer": "تحويل",
    "Transactions": "المعاملات", "Statements": "الكشوف", "Platforms": "المنصات", "Your profile": "ملفك",
    "Verification": "التحقق", "Security": "الأمان", "Profile": "الملف الشخصي", "Notifications": "الإشعارات",
    "Support": "الدعم", "Back to website": "العودة إلى الموقع", "Verified": "موثّق", "All limits available": "جميع الحدود متاحة",
    "AM": "أم", "Sign out": "تسجيل الخروج", "Client area": "منطقة العميل", "TharwaFx client area": "منطقة عميل TharwaFx",
    "Menu": "القائمة", "Ahmed Al Mansoori": "أحمد المنصوري", "TharwaFx home": "الصفحة الرئيسية لـ TharwaFx",
    "Risk warning:": "تحذير المخاطر:",
    "CFDs are leveraged products. You can lose more than you deposit. Trade only with money you can afford to lose.":
        "عقود الفروقات منتجات بالرافعة المالية وقد تخسر أكثر من إيداعك. تداول فقط بأموال يمكنك تحمّل خسارتها.",
    "*Sample values.": "*قيم توضيحية.",

    # Accounts (A02 to A04)
    "My trading accounts": "حسابات التداول", "New account": "حساب جديد", "Live 2": "حقيقي 2", "Demo 1": "تجريبي 1",
    "Archived 0": "مؤرشف 0", "Live": "حقيقي", "Demo": "تجريبي", "Trade": "تداول", "Details": "التفاصيل",
    "Raw Spread, USD, 1:500": "Raw Spread، USD، 1:500", "Islamic, AED, 1:200": "إسلامي، AED، 1:200",
    "Account 8120 4471": "الحساب 8120 4471", "Balance": "الرصيد", "Equity": "الصافي", "Free margin": "الهامش الحر",
    "Margin level": "مستوى الهامش", "Open positions": "المراكز المفتوحة", "Symbol": "الأداة", "Side": "الاتجاه",
    "Lots": "اللوت", "Open": "فتح", "Current": "الحالي", "P/L": "الربح/الخسارة", "Buy": "شراء", "Sell": "بيع",
    "Login details": "بيانات الدخول", "Login": "رقم الدخول", "Server": "الخادم", "Password": "كلمة المرور",
    "Reset password": "إعادة تعيين كلمة المرور", "Launch WebTrader": "تشغيل WebTrader",
    "Open a new account": "افتح حساباً جديداً", "Type": "النوع", "Standard": "قياسي", "Raw Spread": "Raw Spread",
    "From 0.8 pips*, no commission": "من 0.8 نقطة*، بدون عمولة",
    "From 0.0 pips*, $3.50 per lot, per side*": "من 0.0 نقطة*، 3.50$ لكل لوت لكل جهة*",
    "Islamic": "إسلامي", "No overnight swap": "بدون رسوم تبييت", "Currency": "العملة", "Leverage": "الرافعة",
    "Limited by your region and experience": "تحددها منطقتك وخبرتك",
    "I understand that higher leverage increases my risk.": "أفهم أن الرافعة الأعلى تزيد من مخاطري.",
    "Create account": "افتح الحساب",

    # Platforms (A05)
    "Platforms and downloads": "المنصات والتنزيلات", "Opens in a new tab": "يفتح في تبويب جديد", "Launch": "تشغيل",
    "MT5 for Windows": "MT5 لنظام Windows", "MT5 for macOS": "MT5 لنظام macOS", "MT5 for iOS": "MT5 لنظام iOS",
    "MT5 for Android": "MT5 لنظام Android", "Download": "تنزيل", "Your login": "بيانات دخولك",
    "8120 4471, Raw Spread": "8120 4471، Raw Spread", "8120 4502, Islamic": "8120 4502، إسلامي", "5007 1183, Demo": "5007 1183، تجريبي",
    "Your password is never shown. Reset it if you have lost it.": "لا نعرض كلمة المرور أبداً. أعد تعيينها إن نسيتها.",

    # Deposit (A06 to A08)
    "Deposit funds": "إيداع الأموال", "Method": "الطريقة", "Amount": "المبلغ", "Pay": "الدفع", "Done": "تم",
    "Minimum $50*, maximum $10,000* per transaction": "الحد الأدنى 50$*، والحد الأقصى 10,000$* لكل عملية",
    "Review": "المراجعة", "To": "إلى", "Fee": "الرسوم", "You pay": "ستدفع", "Pay $500.00": "ادفع $500.00",
    "Next, you confirm with your card provider.": "بعد ذلك، تؤكد الدفع مع مزوّد بطاقتك.",
    "To account": "إلى الحساب", "8120 4471, USD": "8120 4471، USD", "8120 4502, AED": "8120 4502، AED",
    "Instant, fee $0*": "فوري، بدون رسوم*", "Local bank transfer": "تحويل بنكي محلي", "Within 1 business day": "خلال يوم عمل",
    "Network fee applies": "تُطبق رسوم الشبكة", "Before you pay": "قبل الدفع",
    "Pay from an account in your own name.": "ادفع من حساب باسمك.", "Your bank may charge its own fees.": "قد يفرض بنكك رسوماً خاصة به.",
    "Continue": "متابعة", "Deposit result": "نتيجة الإيداع", "$500.00 added": "تمت إضافة $500.00",
    "Your balance is ready to trade.": "رصيدك جاهز للتداول.", "Completed": "مكتمل", "Start trading": "ابدأ التداول",
    "Waiting for your bank": "بانتظار بنكك",
    "We will update you when it arrives, usually within 1 business day.": "سنبلغك عند وصوله، عادة خلال يوم عمل.",
    "Pending": "قيد التنفيذ", "View transaction": "عرض المعاملة", "Payment declined": "رُفض الدفع",
    "Your card provider declined this payment. You were not charged.": "رفض مزوّد بطاقتك هذه العملية، ولم يُخصم منك أي مبلغ.",
    "Failed": "فشل", "Try another method": "جرّب طريقة أخرى",

    # Overview and notifications (A01, A19)
    "Overview": "نظرة عامة", "Account": "الحساب", "Status": "الحالة", "Quick actions": "إجراءات سريعة",
    "Open WebTrader": "افتح WebTrader", "Recent activity": "آخر النشاطات", "Deposit, Visa": "إيداع، Visa",
    "Today, 09:40": "اليوم، 09:40", "Withdrawal, bank": "سحب، بنك", "Yesterday": "أمس", "In review": "قيد المراجعة",
    "All": "الكل", "Money": "الأموال", "Mark all as read": "تعليم الكل كمقروء", "Deposit completed": "اكتمل الإيداع",
    "$1,000.00 added to 8120 4471": "أضيف $1,000.00 إلى 8120 4471", "Withdrawal in review": "طلب السحب قيد المراجعة",
    "WD-20391 is with compliance": "WD-20391 لدى فريق الامتثال", "Document rejected": "رُفضت وثيقة",
    "Upload a newer proof of address": "ارفع إثبات عنوان أحدث", "[Date]": "[التاريخ]", "New login": "تسجيل دخول جديد",
    "Chrome on Windows, Dubai": "Chrome على Windows، دبي",

    # Onboarding (C06 to C10)
    "Your wealth, in motion.": "ثروتك، في حركة.",
    "One login for your accounts, funding and platforms, in Arabic or English.": "دخول واحد لحساباتك وتمويلك ومنصاتك، بالعربية أو الإنجليزية.",
    "Suitability": "الملاءمة", "Verify": "التحقق", "Your details": "بياناتك",
    "Enter them exactly as shown on your ID.": "أدخلها تماماً كما تظهر في هويتك.",
    "First name": "الاسم الأول", "Last name": "اسم العائلة", "Date of birth": "تاريخ الميلاد", "Nationality": "الجنسية",
    "Emirati": "إماراتي", "Saudi": "سعودي", "Qatari": "قطري", "Kuwaiti": "كويتي", "Bahraini": "بحريني", "Omani": "عُماني",
    "Egyptian": "مصري", "Jordanian": "أردني", "Other": "أخرى", "Mobile": "الجوال",
    "We will send a code to confirm it": "سنرسل رمزاً لتأكيده", "Address": "العنوان", "Ahmed": "أحمد",
    "Al Mansoori": "المنصوري", "Sheikh Zayed Road, Dubai": "شارع الشيخ زايد، دبي",
    "Verify your identity": "وثّق هويتك", "Emirates ID or passport": "الهوية الإماراتية أو جواز السفر",
    "Both sides, all corners visible": "الوجهان، وجميع الزوايا ظاهرة", "Proof of address": "إثبات العنوان",
    "Issued in the last 3 months": "صادر خلال آخر 3 أشهر", "Needed": "مطلوب", "Upload or take a photo": "ارفع ملفاً أو التقط صورة",
    "JPG, PNG or PDF, up to 10 MB": "JPG أو PNG أو PDF، حتى 10 ميغابايت",
    "Your documents are encrypted and seen only by our compliance team.": "وثائقك مشفّرة ولا يطّلع عليها إلا فريق الامتثال لدينا.",
    "Submit for review": "أرسل للمراجعة", "Finish later": "أكمل لاحقاً", "Your trading experience": "خبرتك في التداول",
    "We ask this to check that these products suit you.": "نسأل هذا لنتأكد من أن هذه المنتجات تناسبك.",
    "How often have you traded CFDs or forex?": "كم مرة تداولت عقود الفروقات أو العملات؟",
    "Never": "أبداً", "A few times": "بضع مرات", "Regularly": "بانتظام",
    "If EURUSD falls and you bought with 1:100 leverage, what happens?": "إذا انخفض EURUSD وكنت قد اشتريت برافعة 1:100، ماذا يحدث؟",
    "Loss is capped at the spread": "تقتصر الخسارة على الفارق السعري", "Loss grows with the leverage used": "تكبر الخسارة مع الرافعة المستخدمة",
    "Source of funds": "مصدر الأموال", "Salary": "راتب", "Business income": "دخل تجاري", "Savings": "مدخرات",
    "Investments": "استثمارات", "Inheritance": "إرث", "Annual income band": "فئة الدخل السنوي", "Choose a band": "اختر فئة",
    "Under $25,000": "أقل من 25,000$", "$25,000 to $75,000": "من 25,000$ إلى 75,000$",
    "$75,000 to $150,000": "من 75,000$ إلى 150,000$", "Over $150,000": "أكثر من 150,000$",
    "Welcome, Ahmed": "أهلاً، أحمد", "Your progress": "تقدّمك", "Account created": "تم إنشاء الحساب",
    "Today, 10:12": "اليوم، 10:12", "Details and suitability complete": "اكتملت البيانات وتقييم الملاءمة", "Today, 10:20": "اليوم، 10:20",
    "Documents in review": "الوثائق قيد المراجعة", "Usually within 1 business day": "عادة خلال يوم عمل",
    "Fund your account": "موّل حسابك", "Available once verified": "متاح بعد التحقق",
    "While you wait, try a demo": "أثناء الانتظار، جرّب حساباً تجريبياً", "$10,000 of virtual funds, ready now.": "10,000$ أموال افتراضية، جاهزة الآن.",
    "Open demo": "افتح حساباً تجريبياً", "Secure your account": "أمّن حسابك", "Turn on two-step login.": "فعّل التحقق بخطوتين.",
    "Set up": "إعداد",

    # Profile and security (A17, A18, C09)
    "Personal": "شخصي", "Preferences": "التفضيلات", "Documents": "الوثائق", "Consents": "الموافقات",
    "Locked after verification": "مقفل بعد التحقق", "Email": "البريد الإلكتروني", "Language": "اللغة", "English": "English",
    "Time zone": "المنطقة الزمنية", "Gulf time, GMT+4": "توقيت الخليج، GMT+4", "Gulf time (GMT+4)": "توقيت الخليج (GMT+4)",
    "Riyadh (GMT+3)": "الرياض (GMT+3)", "Cairo (GMT+2)": "القاهرة (GMT+2)", "Save changes": "حفظ التغييرات",
    "Turn on two-step login": "فعّل التحقق بخطوتين", "Scan this code with an authenticator app.": "امسح هذا الرمز بتطبيق المصادقة.",
    "Or enter this key:": "أو أدخل هذا المفتاح:", "Turn on": "تفعيل", "Next, save your backup codes.": "بعد ذلك، احفظ رموزك الاحتياطية.",
    "Each works once if you lose your phone.": "يعمل كل رمز مرة واحدة إذا فقدت هاتفك.", "QR code": "رمز QR",
    "Digit 1": "الرقم 1", "Digit 2": "الرقم 2", "Digit 3": "الرقم 3", "Digit 4": "الرقم 4", "Digit 5": "الرقم 5", "Digit 6": "الرقم 6",
    "Last changed [date]": "آخر تغيير [التاريخ]", "Change": "تغيير", "Two-step login": "التحقق بخطوتين",
    "Authenticator app": "تطبيق المصادقة", "On": "مفعّل", "Backup codes": "الرموز الاحتياطية", "6 of 10 left": "متبقٍ 6 من 10",
    "View": "عرض", "Login alerts": "تنبيهات الدخول", "Email and app": "البريد والتطبيق", "Active devices": "الأجهزة النشطة",
    "Device": "الجهاز", "Location": "الموقع", "Last active": "آخر نشاط", "Chrome, Windows": "Chrome، Windows",
    "Dubai": "دبي", "Now": "الآن", "This device": "هذا الجهاز", "iPhone, Tharwa app": "iPhone، تطبيق ثروة",
    "Safari, macOS": "Safari، macOS", "Abu Dhabi": "أبوظبي", "Sign out everywhere": "تسجيل الخروج من كل الأجهزة",

    # Statements, verification (A15, A16)
    "Trading history and statements": "سجل التداول والكشوف", "Closed trades": "الصفقات المغلقة", "Close": "الإغلاق",
    "Monthly statements": "الكشوف الشهرية", "[Month] 2026": "[الشهر] 2026", "Identity": "الهوية", "Emirates ID": "الهوية الإماراتية",
    "Utility bill, [date]": "فاتورة خدمات، [التاريخ]", "Rejected": "مرفوض", "Upload again": "ارفع مجدداً", "Rejected:": "مرفوض:",
    "the document is older than three months. Upload one issued in the last 3 months.": "الوثيقة أقدم من ثلاثة أشهر. ارفع وثيقة صادرة خلال آخر 3 أشهر.",
    "Needed for deposits above [limit]": "مطلوب للإيداعات فوق [الحد]",

    # Support (A20, A21)
    "Ticket #40213": "التذكرة رقم 40213", "When will my withdrawal reach my card?": "متى يصل مبلغ السحب إلى بطاقتي؟",
    "You, 11:10": "أنت، 11:10",
    "Your request is in compliance review. Once approved, cards usually take 3 to 7 business days.":
        "طلبك قيد مراجعة الامتثال. بعد الموافقة، يستغرق الوصول إلى البطاقة عادة من 3 إلى 7 أيام عمل.",
    "Sara, Support, 11:14": "سارة، الدعم، 11:14", "Write a reply": "اكتب رداً", "Send": "إرسال", "Linked": "مرتبط بـ",
    "Arabic": "العربية", "New ticket": "تذكرة جديدة", "Live chat": "المحادثة المباشرة", "Around the clock": "على مدار الساعة",
    "Help centre": "مركز المساعدة", "Guides and answers": "أدلة وإجابات", "Phone": "الهاتف", "+971 [number]": "+971 [الرقم]",
    "Ticket": "التذكرة", "Subject": "الموضوع", "Updated": "آخر تحديث", "Withdrawal WD-20391": "السحب WD-20391",
    "Today": "اليوم", "Reset MT5 password": "إعادة تعيين كلمة مرور MT5",

    # Transactions (A13, A14)
    "Transaction history": "سجل المعاملات", "Deposits": "الإيداعات", "Withdrawals": "السحوبات", "Transfers": "التحويلات",
    "Last 30 days": "آخر 30 يوماً", "Export CSV": "تصدير CSV", "Reference": "المرجع", "Date": "التاريخ",
    "Withdrawal": "سحب", "To 8120 4502": "إلى 8120 4502", "Transaction TX-88412": "المعاملة TX-88412",
    "[Date], 09:40 GST": "[التاريخ]، 09:40 بتوقيت الخليج", "Provider reference": "مرجع المزوّد", "[ref]": "[المرجع]",
    "Download receipt": "تنزيل الإيصال", "Get help": "اطلب المساعدة", "Timeline": "المراحل", "Payment started": "بدأ الدفع",
    "Provider confirmed": "أكّد المزوّد", "Added to your account": "أضيف إلى حسابك",

    # Transfer (A12)
    "Transfer between accounts": "التحويل بين الحسابات", "From": "من", "8120 4471, USD, $12,480.60": "8120 4471، USD، $12,480.60",
    "Exchange rate": "سعر الصرف", "You receive": "ستستلم",
    "Check your free margin. Moving funds can lower your margin level.": "تحقق من الهامش الحر. قد يؤدي نقل الأموال إلى خفض مستوى الهامش.",

    # Withdraw (A09 to A11)
    "Withdraw funds": "سحب الأموال", "Confirm": "التأكيد", "Paid": "تم الدفع", "From account": "من الحساب",
    "Available $11,902.10": "المتاح $11,902.10", "Send to": "إرسال إلى", "Refund up to $1,000.00 deposited": "استرداد حتى $1,000.00 تم إيداعها",
    "Verified account in your name": "حساب موثّق باسمك",
    "Funds return to your deposit method first, then to a verified account in your name.": "تعود الأموال أولاً إلى طريقة الإيداع، ثم إلى حساب موثّق باسمك.",
    "Summary": "الملخص", "Expected": "الوقت المتوقع", "3 to 7 business days*": "3 إلى 7 أيام عمل*",
    "Payout methods": "طرق السحب", "Card": "بطاقة", "Bank": "بنك", "Add bank account": "أضف حساباً بنكياً",
    "Account holder": "صاحب الحساب", "Must match your verified name": "يجب أن يطابق اسمك الموثّق", "Bank statement": "كشف حساب بنكي",
    "Upload": "رفع", "Add account": "أضف الحساب", "Confirm withdrawal": "تأكيد السحب",
    "$500.00 to Visa •••• 4242. Enter the code from your email and your authenticator.":
        "$500.00 إلى Visa •••• 4242. أدخل الرمز من بريدك ومن تطبيق المصادقة.",
    "Email code": "رمز البريد", "Authenticator code": "رمز تطبيق المصادقة", "Cancel": "إلغاء", "Request submitted": "تم إرسال الطلب",
    "Today, 11:02": "اليوم، 11:02", "Confirmed by email and 2FA": "تم التأكيد بالبريد والتحقق بخطوتين", "Today, 11:03": "اليوم، 11:03",
    # Access steps (C02, C04, C05)
    "Check your email": "تحقق من بريدك", "Enter the 6-digit code sent to": "أدخل الرمز المكوّن من 6 أرقام المرسل إلى",
    "your email": "بريدك", "Verify email": "تأكيد البريد", "Didn't get it?": "لم يصلك؟", "Resend in": "أعد الإرسال خلال",
    "Two-step verification": "التحقق بخطوتين", "Enter the 6-digit code from your authenticator app.": "أدخل الرمز المكوّن من 6 أرقام من تطبيق المصادقة.",
    "Use a backup code": "استخدم رمزاً احتياطياً", "Reset your password": "أعد تعيين كلمة المرور",
    "We will email you a secure link. It works once and expires in 30 minutes.": "سنرسل إلى بريدك رابطاً آمناً يعمل مرة واحدة وتنتهي صلاحيته خلال 30 دقيقة.",
    "Send reset link": "أرسل رابط إعادة التعيين", "If that email is registered, a link is on its way.": "إذا كان هذا البريد مسجلاً، فالرابط في طريقه إليك.",
    "Back to log in": "العودة إلى تسجيل الدخول",

    "Compliance review": "مراجعة الامتثال", "Processing": "قيد المعالجة", "With payment provider": "لدى مزوّد الدفع",
}
