"""Render Company 318 Instagram slides (1080x1350) in the night-sky style."""
import json, os
from playwright.sync_api import sync_playwright

D = '/home/claude/c318art'

CSS = """
@font-face{font-family:InterM;src:url('file:///usr/share/fonts/opentype/inter/Inter-Medium.otf');}
html,body{margin:0;padding:0;}
.c{width:1080px;height:1350px;position:relative;overflow:hidden;color:#f4ecde;
   background:
     radial-gradient(ellipse 75% 40% at 50% 8%, rgba(214,176,120,0.20) 0%, rgba(214,176,120,0.05) 45%, rgba(0,0,0,0) 75%),
     linear-gradient(180deg,#2e1727 0%,#211019 50%,#150a10 100%);}
canvas{position:absolute;inset:0;}
.serif{font-family:'GFS Baskerville',serif;}
.eyebrow{font-family:InterM;font-size:21px;letter-spacing:0.3em;color:#d6b078;text-transform:uppercase;}
.count{position:absolute;top:84px;right:96px;font-family:InterM;font-size:20px;letter-spacing:0.18em;color:rgba(244,236,222,0.45);}
.tag{position:absolute;top:84px;left:96px;}
.body{position:absolute;left:120px;right:120px;top:50%;transform:translateY(-50%);}
.big{font-size:74px;line-height:1.16;}
.mid{font-size:58px;line-height:1.26;}
.verse{font-size:60px;line-height:1.3;}
.ref{margin-top:44px;}
.g{color:#d6b078;}
.rule{width:64px;height:1px;background:rgba(214,176,120,0.7);margin:44px 0;}
.foot{position:absolute;bottom:84px;left:96px;right:96px;display:flex;justify-content:space-between;align-items:center;
      font-family:InterM;font-size:19px;letter-spacing:0.22em;color:rgba(244,236,222,0.5);}
.foot img{width:92px;opacity:0.85;}
.center{text-align:center;}
.markbig{display:block;width:360px;margin:0 auto 60px;filter:drop-shadow(0 0 16px rgba(244,226,190,0.22));}
.small{font-size:36px;line-height:1.45;color:rgba(244,236,222,0.82);}
"""

STARS = """
<script>
let seed=%d; const r=()=>{seed=(seed*16807)%%2147483647;return (seed-1)/2147483646;};
const c=document.getElementById('s').getContext('2d');
for(let i=0;i<200;i++){const x=r()*1080,y=r()*480;const s=r()*1.2+0.3,a=(r()*0.35+0.06)*(1-y/520);
c.beginPath();c.arc(x,y,s,0,Math.PI*2);c.fillStyle=`rgba(244,232,210,${a})`;c.fill();}
</script>"""


def page(inner, seed, count=None, tag=None, foot=True):
    parts = [f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="c">',
             '<canvas id="s" width="1080" height="1350"></canvas>']
    if tag:
        parts.append(f'<div class="tag eyebrow">{tag}</div>')
    if count:
        parts.append(f'<div class="count">{count}</div>')
    parts.append(inner)
    if foot == 'center':
        parts.append('<div class="foot" style="justify-content:center"><span>@WEARECOMPANY318</span></div>')
    elif foot:
        parts.append('<div class="foot"><span>@WEARECOMPANY318</span><img src="mark_ivory.png"></div>')
    parts.append('</div>' + STARS % seed + '</body></html>')
    return ''.join(parts)


TAG = 'Leah Ramirez · The Offense of the Cross'
N = 8
carousel = [
    # 1 cover
    page('<div class="body"><div class="eyebrow" style="margin-bottom:48px">A teaching from Leah Ramirez</div>'
         '<div class="serif big">Take up your cross daily?<br><span class="g">Or already crucified with Christ?</span></div>'
         '<div class="rule"></div><div class="serif small">Two verses many of us have kept in separate drawers. Swipe through.</div></div>',
         11, f'1 / {N}'),
    page('<div class="body"><div class="serif verse">“If anyone wants to come after Me, he must deny himself and take up his cross daily and follow Me.”</div>'
         '<div class="eyebrow ref">Luke 9:23</div></div>', 12, f'2 / {N}', TAG),
    page('<div class="body"><div class="serif verse">“We know that our old self was crucified with Him.”</div>'
         '<div class="eyebrow ref">Romans 6:6</div></div>', 13, f'3 / {N}', TAG),
    page('<div class="body"><div class="serif big">If we’ve already died with Christ, <span class="g">what does it mean to deny ourselves?</span></div></div>',
         14, f'4 / {N}', TAG),
    page('<div class="body"><div class="serif mid">Since the Garden, humanity has reached for a life independent of God.</div>'
         '<div class="rule"></div><div class="serif mid g">Jesus didn’t come to make us better at that. He came to bring us into the life He has always shared with His Father.</div></div>',
         15, f'5 / {N}', TAG),
    page('<div class="body"><div class="serif mid">The cross is not another system of religious self‑management.</div>'
         '<div class="rule"></div><div class="serif mid">It announces an accomplished death, a new relationship, and <span class="g">Christ living in us.</span></div>'
         '<div class="eyebrow ref">Galatians 2:20</div></div>', 16, f'6 / {N}', TAG),
    page('<div class="body"><div class="serif mid">We don’t take up our cross to accomplish our death with Christ.</div>'
         '<div class="rule"></div><div class="serif mid g">We take it up as those who have already died with Him, learning to follow Him in the life we now share.</div></div>',
         17, f'7 / {N}', TAG),
    page('<div class="body center"><img class="markbig" src="mark_ivory.png">'
         '<div class="eyebrow" style="margin-bottom:36px">Watch the full message</div>'
         '<div class="serif big">The Offense of the Cross</div>'
         '<div class="serif small" style="margin-top:28px">Leah Ramirez · Link in bio</div></div>',
         18, f'8 / {N}', None, foot='center')
    + '',
]
# final slide gets the handle under the text
carousel[-1] = carousel[-1].replace('</div></div><script>', '</div><div class="foot" style="justify-content:center"><span>@WEARECOMPANY318</span></div></div><script>', 1)

substack = page(
    '<div class="body center"><img class="markbig" src="mark_ivory.png">'
    '<div class="eyebrow" style="margin-bottom:40px">Free · Every week · On Substack</div>'
    '<div class="serif big">Teaching you can<br><span class="g">return to.</span></div>'
    '<div class="rule" style="margin:44px auto"></div>'
    '<div class="serif small">Written teaching, biblical reflection and prophetic insight from Leah Ramirez and Chris Berglund.</div>'
    '<div class="eyebrow" style="margin-top:48px;color:rgba(244,236,222,0.7)">company318.substack.com</div></div>',
    21, None, None, foot='center')
substack = substack.replace('</div></div><script>', '</div><div class="foot" style="justify-content:center"><span>@WEARECOMPANY318</span></div></div><script>', 1)

jobs = [(f'carousel_{i+1:02d}', h) for i, h in enumerate(carousel)] + [('substack_invite', substack)]
with sync_playwright() as p:
    b = p.chromium.launch(args=['--allow-file-access-from-files'])
    pg = b.new_page(viewport={'width': 1080, 'height': 1350})
    for name, html in jobs:
        path = f'{D}/{name}.html'
        open(path, 'w').write(html)
        pg.goto(f'file://{path}')
        pg.wait_for_timeout(400)
        pg.screenshot(path=f'{D}/{name}.png')
    b.close()
print('ok', len(jobs))
