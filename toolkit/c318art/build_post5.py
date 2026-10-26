"""Post 5: Living From Another Order (Chris Berglund), 7 slides, same night-sky style."""
from playwright.sync_api import sync_playwright

D = '/home/claude/c318art'
src = open(f'{D}/build_slides.py').read()
exec(src[:src.index("TAG = ")])  # reuse CSS, STARS and page()

TAG = 'Chris Berglund · Living From Another Order'
N = 7
slides = [
    page('<div class="body"><div class="eyebrow" style="margin-bottom:48px">A teaching from Chris Berglund</div>'
         '<div class="serif big">Why does Hebrews care so much about <span class="g">Melchizedek?</span></div>'
         '<div class="rule"></div><div class="serif small">A priest-king who appears in a few verses of Genesis 14, and a window into who Jesus is.</div></div>',
         31, f'1 / {N}'),
    page('<div class="body"><div class="serif mid">The old priesthood rested on ancestry.</div>'
         '<div class="rule"></div><div class="serif mid g">And every priest’s service ended at death.</div></div>',
         32, f'2 / {N}', TAG),
    page('<div class="body"><div class="serif verse">Jesus became a priest “by the power of an indestructible life.”</div>'
         '<div class="eyebrow ref">Hebrews 7:16</div></div>', 33, f'3 / {N}', TAG),
    page('<div class="body"><div class="serif mid">The Gospel reaches beyond forgiveness.</div>'
         '<div class="rule"></div><div class="serif mid g">The Father’s purpose is to bring us into the Son’s own life and communion.</div>'
         '<div class="eyebrow ref">Ephesians 1 · John 17</div></div>', 34, f'4 / {N}', TAG),
    page('<div class="body"><div class="serif mid">Hebrews shows the order. Romans 5–8 shows how we live in it:</div>'
         '<div class="rule"></div><div class="serif mid g">joined to Christ in death and resurrection, alive by the Spirit, free from condemnation.</div></div>',
         35, f'5 / {N}', TAG),
    page('<div class="body"><div class="serif big">“Communion comes before expression.”</div>'
         '<div class="rule"></div><div class="serif mid g">What we carry flows from what we first receive.</div>'
         '<div class="eyebrow ref">1 Peter 2:9</div></div>', 36, f'6 / {N}', TAG),
    page('<div class="body center"><img class="markbig" src="mark_ivory.png">'
         '<div class="eyebrow" style="margin-bottom:36px">Go deeper</div>'
         '<div class="serif big">Living From Another Order</div>'
         '<div class="serif small" style="margin-top:28px">Chris Berglund · Explored further in<br>Behold School’s Melchizedek Lens</div></div>',
         37, f'7 / {N}', None, foot='center'),
]

with sync_playwright() as p:
    b = p.chromium.launch(args=['--allow-file-access-from-files'])
    pg = b.new_page(viewport={'width': 1080, 'height': 1350})
    for i, html in enumerate(slides, 1):
        path = f'{D}/p5_{i}.html'
        open(path, 'w').write(html)
        pg.goto(f'file://{path}')
        pg.wait_for_timeout(400)
        pg.screenshot(path=f'{D}/p5_{i}.png')
    b.close()
print('ok')
