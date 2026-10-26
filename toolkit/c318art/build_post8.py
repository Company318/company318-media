"""Post 8: Behold School, in students' own words. Quotes verbatim, anonymous."""
from playwright.sync_api import sync_playwright

D = '/home/claude/c318art'
src = open(f'{D}/build_slides.py').read()
exec(src[:src.index("TAG = ")])  # reuse CSS, STARS and page()

EXTRA = """
.qmark{font-family:'GFS Baskerville',serif;font-size:220px;line-height:0.6;color:#d6b078;opacity:0.55;height:96px;}
.quote{font-family:'GFS Baskerville',serif;color:#f4ecde;}
.q1{font-size:66px;line-height:1.24;}
.q2{font-size:54px;line-height:1.3;}
.q3{font-size:46px;line-height:1.36;}
.who{margin-top:52px;font-family:InterM;font-size:20px;letter-spacing:0.26em;text-transform:uppercase;color:rgba(244,236,222,0.6);}
"""
CSS_ORIG = CSS
CSS = CSS_ORIG + EXTRA  # page() reads the module-level CSS

TAG = 'Behold School · In their own words'
N = 7


def testimony(text, size, theme, seed, n):
    return page(f'<div class="body"><div class="eyebrow" style="margin-bottom:40px">{theme}</div>'
                f'<div class="qmark">“</div><div class="quote {size}">{text}”</div>'
                f'<div class="who">A Behold School student</div></div>', seed, f'{n} / {N}', TAG)


slides = [
    page('<div class="body"><div class="eyebrow" style="margin-bottom:48px">Behold School · In their own words</div>'
         '<div class="serif big">What changes when you begin to see <span class="g">what Christ has finished?</span></div>'
         '<div class="rule"></div><div class="serif small">Students from our ABIDE track, shared anonymously.</div></div>',
         51, f'1 / {N}'),
    testimony('I have been living as though it’s not really finished.', 'q1', 'On the finished work', 52, 2),
    testimony('Almost, like I’ve had to accomplish my healing rather than just receive it and participate in it.', 'q2', 'On healing', 53, 3),
    testimony('Even the way I pray has changed.', 'q1', 'On prayer', 54, 4),
    testimony('The real Gospel convinces me that God is undeniably good. I need not fear his wrath or even his displeasure… He has accepted me.', 'q3', 'On the goodness of God', 55, 5),
    testimony('Life is too full of checklist and striving… I’m going to stop and take time to behold the Holy Spirit… because of Jesus, I already have peace with God.', 'q3', 'On rest', 56, 6),
    page('<div class="body center"><img class="markbig" src="mark_ivory.png">'
         '<div class="eyebrow" style="margin-bottom:36px">Behold School</div>'
         '<div class="serif mid">A place to remain with Jesus long enough for <span class="g">revelation to become formation.</span></div>'
         '<div class="serif small" style="margin-top:36px">Learn more · Behold School link in bio</div></div>',
         57, f'7 / {N}', None, foot='center'),
]

with sync_playwright() as p:
    b = p.chromium.launch(args=['--allow-file-access-from-files'])
    pg = b.new_page(viewport={'width': 1080, 'height': 1350})
    for i, html in enumerate(slides, 1):
        path = f'{D}/p8_{i}.html'
        open(path, 'w').write(html)
        pg.goto(f'file://{path}')
        pg.wait_for_timeout(400)
        pg.screenshot(path=f'{D}/p8_{i}.png')
    b.close()
print('ok')
