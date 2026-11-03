"""Customer-facing explanations, kept separate from operational and legal facts."""
import html
import re

# Copy explains the product without inventing credentials, results or service terms.
CONTENT = {
    'P01': ('A clearer place to start', 'Build your understanding before you build a position.', [
        ('Understand the market', 'Explore currencies, metals, indices and shares. Learn what moves each market and how contract specifications differ.', '/markets', 'Explore markets'),
        ('Practise the process', 'Use virtual funds to explore the platform and order types. Demo results do not predict live results or reproduce every live trading condition.', '/demo', 'Explore the demo'),
        ('Know your exposure', 'Understand margin, spread and position size before placing an order. Leverage magnifies both gains and losses.', '/tools/calculators', 'Explore calculators')]),
    'P03': ('Compare the whole cost', 'A spread is one part of the price of a trade.', [
        ('Spread and commission', 'Compare the bid–ask spread together with any per-lot commission. A lower spread does not always mean a lower total cost.', '/trading/spreads', 'Understand spreads'),
        ('Holding a position', 'Positions held overnight may incur financing adjustments. Review the instrument specification and account terms, including any swap-free conditions.', '/trading/swap', 'Review overnight costs'),
        ('Margin and size', 'Margin is collateral for a leveraged position. The value of your exposure can be substantially greater than the amount reserved as margin.', '/trading/leverage', 'Understand margin')]),
    'P18': ('One workflow, wherever you trade', 'Choose a platform around the way you research, place orders and review positions.', [
        ('Prepare your workspace', 'Organise your watchlist, check the trading session and open the contract specification before entering a new market.', '/markets', 'Browse instruments'),
        ('Understand your orders', 'Market orders seek execution at an available price. Pending orders use a price condition. Slippage and market gaps can affect the final execution price.', '/academy', 'Learn the essentials'),
        ('Review your activity', 'Keep track of open positions, available margin and transaction history. Review costs and execution alongside the outcome of each trade.', '/help', 'Visit the help centre')]),
    'P24': ('Learn in a practical order', 'Move from the language of trading to the mechanics of an order.', [
        ('Start with the essentials', 'Learn bid and ask prices, pips, lots and market sessions. Understand what a CFD represents before exploring leveraged products.', '/tools/glossary', 'Open the glossary'),
        ('Work through the numbers', 'Explore the relationship between position size, pip value and margin. Calculator estimates depend on your inputs and instrument specifications.', '/tools/calculators', 'Try the calculators'),
        ('Put learning into practice', 'Explore order placement with virtual funds. Record why you entered, what happened and what you learned from the process.', '/demo', 'Explore the demo')]),
    'P33': ('Find the right help faster', 'A few details make it easier to understand your question.', [
        ('Account access', 'Describe the sign-in issue and any error message. Never send your password, one-time code or recovery codes in a support request.', '/stay-safe', 'Protect your account'),
        ('Payments and transfers', 'Keep the payment reference, currency, amount and date available. Share payment details only through the appropriate secure channel.', '/funding/deposits', 'Explore funding'),
        ('Platform questions', 'Include the platform name, instrument, approximate time and order reference where relevant. Remove sensitive details from screenshots.', '/contact', 'Contact the team')]),
    'P35': ('Before you get in touch', 'Help the team understand your request from the first message.', [
        ('Choose a clear subject', 'Tell us whether your question concerns account access, verification, funding or a trading platform. Include a concise description of the issue.', '/help', 'Browse common questions'),
        ('Keep your information safe', 'Do not include passwords, card security codes or one-time login codes. Documents should be submitted through the secure verification flow.', '/stay-safe', 'Read security guidance'),
        ('Check the available guidance', 'You may find the explanation you need in the help centre, glossary or platform pages while preparing your request.', '/platforms', 'Explore platforms')]),
    'P36': ('Clarity at every step', 'TharwaFx brings market information, platform access and learning into one connected experience.', [
        ('Language that makes sense', 'Trading has its own vocabulary. Our Arabic and English experience helps you explore the terminology and understand the next step.', '/tools/glossary', 'Explore trading terms'),
        ('A view of the whole journey', 'Explore markets, compare account structures and understand the platform before deciding how to proceed.', '/accounts', 'Explore accounts'),
        ('Learning alongside access', 'Use educational resources to understand the mechanics and risks of trading. Educational content is general information, not a personal recommendation.', '/academy', 'Visit the academy')]),
    'P38': ('Pause. Check. Protect.', 'Recognise common warning signs before sharing information or sending money.', [
        ('Check the destination', 'Open the website from a trusted bookmark. Look carefully at the domain before entering credentials, especially after following a message or advertisement.', '/help', 'Get help'),
        ('Keep control of your account', 'Do not share login codes or allow an unexpected caller to control your device. Treat pressure, secrecy and promises of guaranteed returns as warning signs.', '/contact', 'Contact the team'),
        ('Report suspicious contact', 'Save the message and sender details. If you suspect your account has been accessed, contact support through a channel you have independently verified.', '/contact', 'Raise a concern')]),
}

AR_HOME = ('بداية أوضح للتداول', 'افهم السوق وآلية التداول قبل فتح أي صفقة.', [
    ('تعرّف على الأسواق', 'استكشف العملات والمعادن والمؤشرات والأسهم، وتعرّف على العوامل المحركة للأسعار واختلاف مواصفات العقود.', '/markets', 'استكشف الأسواق'),
    ('تدرّب على الخطوات', 'استخدم أموالاً افتراضية لاستكشاف المنصة وأنواع الأوامر. النتائج التجريبية لا تتنبأ بالنتائج الحقيقية ولا تحاكي جميع ظروف التداول الفعلي.', '/demo', 'استكشف الحساب التجريبي'),
    ('افهم حجم التعرض', 'تعرّف على الهامش والفارق السعري وحجم الصفقة. تضاعف الرافعة المالية الأرباح والخسائر على حد سواء.', '/tools/calculators', 'استكشف الحاسبات')])


def enrich(s, sid, lang, localize):
    if sid == 'P01':
        labels = (['فروقات تبدأ من (نقطة)', 'رافعة مالية تصل إلى', 'الحد الأدنى للصفقة (لوت)', 'فئات الأصول', 'دعم بالعربية والإنجليزية']
                  if lang == 'ar' else ['Spreads from (pips)', 'Leverage up to', 'Minimum trade size (lots)', 'Asset classes', 'Support in Arabic & English'])
        note = ('*شروط تداول توضيحية. تختلف الفروقات والرافعة المالية حسب الحساب والأداة والمنطقة.' if lang == 'ar' else
                '*Illustrative trading terms. Spreads and leverage vary by account, instrument and region.')
        cards = ''.join(f'<div><div class="stat"><span class="mono">{value}</span></div><div class="sm mut">{html.escape(label)}</div></div>'
                        for value, label in zip(['0.0*', '1:500*', '0.01', '6', '24/7'], labels))
        s = re.sub(r'<div class="stats">.*?(?=<section)',
                   lambda _: f'<div class="stats"><div class="wrap g5">{cards}</div><p class="wrap stats-note">{note}</p></div>', s, count=1, flags=re.S)
    # Replace layout-only copy with useful wording, without filling unknown business facts.
    if lang == 'en':
        replacements = {
            '[Founding story to be supplied by the client: who started the company, why, and where it is based.]':
                'TharwaFx is built around a straightforward idea: make the trading journey easier to understand. Explore markets, compare account structures and develop your knowledge through a connected Arabic and English experience.',
            'Your first 10 lessons in trading': 'The foundations of trading',
            '12 lessons, beginner': 'Start with the essentials',
            'Live in Arabic, [date]': 'Explore Arabic market education',
            '[Confirm official channels with the client.]': 'Verify contact details independently before sharing personal information. Never share your password or one-time login codes.',
        }
        for old, new in replacements.items():
            s = s.replace(old, new)
        if sid == 'P01':
            s = s.replace('[0,000]+', '6').replace('>instruments<', '>asset classes<')
            s = re.sub(r'<span class="[^"]*">\[(?:000|00)\]\+</span>', '', s)
    content = AR_HOME if lang == 'ar' and sid == 'P01' else CONTENT.get(sid) if lang == 'en' else None
    if not content:
        return s
    title, intro, cards = content
    esc = html.escape
    items = ''.join(f'<a class="editorial-card" href="{localize(path, lang)}"><span class="editorial-index mono">0{i+1}</span><h3>{esc(h)}</h3><p>{esc(p)}</p><span class="editorial-link">{esc(label)} <span aria-hidden="true">←</span></span></a>' if lang == 'ar' else
                    f'<a class="editorial-card" href="{localize(path, lang)}"><span class="editorial-index mono">0{i+1}</span><h3>{esc(h)}</h3><p>{esc(p)}</p><span class="editorial-link">{esc(label)} <span aria-hidden="true">→</span></span></a>'
                    for i, (h, p, path, label) in enumerate(cards))
    section = f'<section class="sec editorial"><div class="wrap"><div class="editorial-heading"><span class="editorial-eyebrow mono">THARWAFX / {"تعرّف أكثر" if lang == "ar" else "EXPLORE"}</span><h2>{esc(title)}</h2><p class="lead">{esc(intro)}</p></div><div class="editorial-grid">{items}</div></div></section>'
    # Keep the final account CTA as the final section on the homepage.
    marker = s.rfind('<section') if sid == 'P01' else -1
    return s[:marker] + section + s[marker:] if marker >= 0 else s + section
