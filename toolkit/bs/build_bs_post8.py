"""Post 8 in the Behold School identity: parchment, rust, navy, gold, crest. Quotes verbatim."""
from playwright.sync_api import sync_playwright

D = '/home/claude/bs'
CSS = """
@font-face{font-family:InterM;src:url('file:///usr/share/fonts/opentype/inter/Inter-Medium.otf');}
@font-face{font-family:InterR;src:url('file:///usr/share/fonts/opentype/inter/Inter-Regular.otf');}
html,body{margin:0;padding:0;}
.c{width:1080px;height:1350px;position:relative;overflow:hidden;color:#2a2522;
   background:radial-gradient(ellipse 90% 70% at 50% 40%, #f7f1e6 0%, #f1e8d8 60%, #e8dcc6 100%);}
.serif{font-family:'GFS Baskerville',serif;}
.crest{position:absolute;top:84px;left:50%;transform:translateX(-50%);width:132px;}
.count{position:absolute;top:96px;right:96px;font-family:InterM;font-size:20px;letter-spacing:0.18em;color:rgba(30,39,53,0.45);}
.body{position:absolute;left:120px;right:120px;top:52%;transform:translateY(-50%);}
.eyebrow{font-family:InterM;font-size:21px;letter-spacing:0.3em;text-transform:uppercase;color:#a64f30;}
.orn{display:flex;align-items:center;gap:18px;margin:34px 0;color:#b8924a;}
.orn i{display:block;height:1px;width:90px;background:#b8924a;}
.orn b{font-size:22px;font-weight:400;}
.center{text-align:center;}
.center .orn{justify-content:center;}
.qmark{font-family:'GFS Baskerville',serif;font-size:200px;line-height:0.6;color:#a64f30;opacity:0.35;height:86px;}
.q1{font-size:68px;line-height:1.22;color:#1e2735;}
.q2{font-size:56px;line-height:1.3;color:#1e2735;}
.q3{font-size:47px;line-height:1.38;color:#1e2735;}
.who{margin-top:48px;font-family:InterM;font-size:20px;letter-spacing:0.26em;text-transform:uppercase;color:#8a7a62;}
.big{font-size:80px;line-height:1.12;color:#1e2735;}
.r{color:#a64f30;}
.small{font-family:InterR;font-size:30px;line-height:1.5;color:#4a423b;}
.band{position:absolute;left:0;right:0;bottom:0;height:118px;background:#1e2735;display:flex;align-items:center;justify-content:center;gap:28px;
      font-family:InterM;font-size:19px;letter-spacing:0.28em;color:#d8bf8a;}
.band span.sep{width:1px;height:34px;background:rgba(216,191,138,0.5);}
.bigcrest{display:block;width:300px;margin:0 auto 10px;}
"""
N = 7


def page(inner, count, crest=True):
    return ('<!doctype html><html><head><meta charset="utf-8"><style>' + CSS + '</style></head><body><div class="c">'
            + ('<img class="crest" src="shield.png">' if crest else '')
            + f'<div class="count">{count}</div>' + inner
            + '<div class="band"><span>BEHOLD SCHOOL</span><span class="sep"></span><span>THE GOSPEL FROM WHICH WE LIVE</span></div>'
            + '</div></body></html>')


ORN = '<div class="orn"><i></i><b>✦</b><i></i></div>'


def testimony(text, size, theme, n):
    return page(f'<div class="body"><div class="eyebrow">{theme}</div>{ORN}'
                f'<div class="qmark">“</div><div class="serif {size}">{text}”</div>'
                f'<div class="who">A Behold School student</div></div>', f'{n} / {N}')


slides = [
    page('<div class="body center"><div class="eyebrow">In their own words</div>' + ORN +
         '<div class="serif big">What changes when you begin to see <span class="r">what Christ has finished?</span></div>' + ORN +
         '<div class="small">Students from our ABIDE track, shared anonymously.</div></div>', f'1 / {N}'),
    testimony('I have been living as though it’s not really finished.', 'q1', 'On the finished work', 2),
    testimony('Almost, like I’ve had to accomplish my healing rather than just receive it and participate in it.', 'q2', 'On healing', 3),
    testimony('Even the way I pray has changed.', 'q1', 'On prayer', 4),
    testimony('The real Gospel convinces me that God is undeniably good. I need not fear his wrath or even his displeasure… He has accepted me.', 'q3', 'On the goodness of God', 5),
    testimony('Life is too full of checklist and striving… I’m going to stop and take time to behold the Holy Spirit… because of Jesus, I already have peace with God.', 'q3', 'On rest', 6),
    page('<div class="body center"><img class="bigcrest" src="shield.png">' + ORN +
         '<div class="serif q2">A place to remain with Jesus long enough for <span class="r">revelation to become formation.</span></div>' + ORN +
         '<div class="eyebrow" style="color:#1e2735">beholdschool.com</div></div>', f'7 / {N}', crest=False),
]

with sync_playwright() as p:
    b = p.chromium.launch(args=['--allow-file-access-from-files'])
    pg = b.new_page(viewport={'width': 1080, 'height': 1350})
    for i, html in enumerate(slides, 1):
        path = f'{D}/bs8_{i}.html'
        open(path, 'w').write(html)
        pg.goto(f'file://{path}')
        pg.wait_for_timeout(400)
        pg.screenshot(path=f'{D}/bs8_{i}.png')
    b.close()
print('ok')
