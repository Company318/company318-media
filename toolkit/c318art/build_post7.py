"""Post 7: Where are you located? (Leah Ramirez, Getting Set In), 8 slides."""
from playwright.sync_api import sync_playwright

D = '/home/claude/c318art'
src = open(f'{D}/build_slides.py').read()
exec(src[:src.index("TAG = ")])  # reuse CSS, STARS and page()

TAG = 'Leah Ramirez · Getting Set In'
N = 8
slides = [
    page('<div class="body"><div class="eyebrow" style="margin-bottom:48px">A teaching from Leah Ramirez</div>'
         '<div class="serif big">Do you know where<br><span class="g">you are located?</span></div>'
         '<div class="rule"></div><div class="serif small">Before we ask what to do, the Gospel asks where God has already placed us.</div></div>',
         41, f'1 / {N}'),
    page('<div class="body"><div class="serif verse">“For as in Adam all die, so in Christ all will be made alive.”</div>'
         '<div class="eyebrow ref">1 Corinthians 15:22</div></div>', 42, f'2 / {N}', TAG),
    page('<div class="body"><div class="serif mid">Paul describes two locations:<br>in Adam, or in Christ.</div>'
         '<div class="rule"></div><div class="serif mid g">The Christian life starts with where God has placed you.</div></div>',
         43, f'3 / {N}', TAG),
    page('<div class="body"><div class="serif mid">In Genesis 15, God alone passes between the covenant pieces while Abram sleeps.</div>'
         '<div class="rule"></div><div class="serif big g">The Gospel is covenant, not contract.</div></div>',
         44, f'4 / {N}', TAG),
    page('<div class="body"><div class="serif mid">Jesus finishes redemption the same way.</div>'
         '<div class="rule"></div><div class="serif big g">“He goes alone.”</div></div>',
         45, f'5 / {N}', TAG),
    page('<div class="body"><div class="serif mid">So Paul calls us to count ourselves dead to sin and alive to God in Christ Jesus,</div>'
         '<div class="rule"></div><div class="serif mid g">raised with Him and seated with Him.</div>'
         '<div class="eyebrow ref">Romans 6:11 · Ephesians 2:6</div></div>', 46, f'6 / {N}', TAG),
    page('<div class="body"><div class="serif big">“Open your eyes and see where Christ has already <span class="g">brought you.</span>”</div>'
         '<div class="eyebrow ref">Leah Ramirez</div></div>', 47, f'7 / {N}', TAG),
    page('<div class="body center"><img class="markbig" src="mark_ivory.png">'
         '<div class="eyebrow" style="margin-bottom:36px">From Leah Ramirez</div>'
         '<div class="serif big">Getting Set In</div>'
         '<div class="serif small" style="margin-top:28px">Leah is writing a study of Romans 5–8,<br>coming out of Behold School.</div></div>',
         48, f'8 / {N}', None, foot='center'),
]

with sync_playwright() as p:
    b = p.chromium.launch(args=['--allow-file-access-from-files'])
    pg = b.new_page(viewport={'width': 1080, 'height': 1350})
    for i, html in enumerate(slides, 1):
        path = f'{D}/p7_{i}.html'
        open(path, 'w').write(html)
        pg.goto(f'file://{path}')
        pg.wait_for_timeout(400)
        pg.screenshot(path=f'{D}/p7_{i}.png')
    b.close()
print('ok')
