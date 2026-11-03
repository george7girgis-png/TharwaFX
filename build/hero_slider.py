"""Home feature carousel: existing market hero and the new AI campaign."""
import build as B


def render(s, lang):
    start = s.index('<div')
    end = B.div_end(s, start)
    original = s[start:end].replace('<div ', '<div class="home-primary" ', 1)
    ar = lang == 'ar'
    heading = 'ذكاء يوسّع رؤيتك.' if ar else 'A new dimension<br>of market intelligence.'
    lead = ('استكشف أدوات لتحليل الأسواق وقراءة الأخبار واختبار الاستراتيجيات، مع بقاء القرار وحدود المخاطر بين يديك.' if ar else
            'Explore AI-assisted analysis, news sentiment and strategy testing. Your decisions. Your limits. A wider perspective.')
    first, second = ('الأسواق', 'ذكاء ثروة') if ar else ('The markets', 'TharwaFx AI')
    next_label, prev_label = ('الشريحة التالية', 'الشريحة السابقة') if ar else ('Next slide', 'Previous slide')
    ai = (f'<article class="hero-panel ai-home-hero" id="feature-ai" role="group" aria-roledescription="slide" aria-label="2 / 2 — {second}" hidden inert>'
          f'{B.media("ai-candles-loop", "ai-candles", "ai-home-art", eager=True)}<div class="ai-home-grid" aria-hidden="true"></div>'
          f'<div class="wrap ai-home-inner"><div class="ai-home-copy">'
          f'<h2>{heading}</h2><p>{lead}</p><div class="row wr mt32"><a class="b p lg2" href="{B.localize("/ai", lang)}">'
          f'{"اكتشف ذكاء ثروة" if ar else "Discover TharwaFx AI"} <span aria-hidden="true">{"←" if ar else "→"}</span></a>'
          f'<a class="b o lg2" href="{B.localize("/ai", lang)}#auto">{"استكشف المحاكاة" if ar else "Explore the simulator"}</a></div>'
          f'<div class="ai-home-pills"><span>{"تحليل السوق" if ar else "Market analysis"}</span><span>{"قراءة الأخبار" if ar else "News sentiment"}</span>'
          f'<span>{"اختبار الاستراتيجيات" if ar else "Strategy testing"}</span></div>'
          f'<p class="ai-home-note">{"معاينة لأدوات قيد التطوير. التداول ينطوي على مخاطر." if ar else "Tools in development. Preview only. Trading involves risk."}</p></div></div></article>')
    arrows = (f'<div class="hero-arrows" data-hero-arrows hidden><button type="button" data-hero-prev aria-label="{prev_label}">←</button><button type="button" data-hero-next aria-label="{next_label}">→</button></div>')
    controls = (f'<div class="hero-controls hero-controls-minimal" data-hero-controls hidden>'
                f'<span class="sr-only" data-hero-status aria-live="polite" aria-atomic="true"></span></div>')
    return (s[:start] + f'<section class="hero-deck" aria-label="{"أبرز المزايا" if ar else "Featured experiences"}" aria-roledescription="carousel" data-hero-deck>'
            f'<div class="hero-slides"><div class="hero-panel is-active" id="feature-markets" role="group" aria-roledescription="slide" aria-label="1 / 2 — {first}">{original}</div>{ai}{arrows}{controls}</div></section>' + s[end:])
