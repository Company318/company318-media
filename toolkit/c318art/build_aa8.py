"""Apostolic Architecture, Chapter 8 excerpts. Verbatim. Night-sky style."""
from playwright.sync_api import sync_playwright
src=open('/home/claude/c318art/build_aa7.py').read()
exec(src[:src.index("carousel = [")])
TAG='Apostolic Architecture · Chapter 8'
N=9
def ex(text, size, seed, n, ref=None, ctx=None):
    r = f'<div class="eyebrow ref">{ref}</div>' if ref else ''
    c = f'<div class="eyebrow" style="margin-bottom:44px">{ctx}</div>' if ctx else ''
    return page(f'<div class="body">{c}<div class="ex {size}">{text}</div>{r}</div>', seed, f'{n} / {N}', TAG)
slides=[
 page('<div class="body"><div class="eyebrow" style="margin-bottom:48px">From the book in progress</div>'
      '<div class="serif big">Intimacy<br><span class="g">Without Distance</span></div>'
      '<div class="rule"></div><div class="serif small">Excerpts from Chapter 8 of <i>Apostolic Architecture</i> by Leah Ramirez and Chris Berglund.</div></div>', 91, f'1 / {N}'),
 ex('Somewhere along the way, receiving a promise could become <span class="g">assuming responsibility for its fulfillment.</span>','e1',92,2),
 ex('We measured our authority by our sacrifice and our intimacy by the intensity we could sustain. <span class="g">Spiritual practices had become currency.</span>','e2',93,3),
 ex('We aren’t convincing a reluctant God. <span class="g">He is convincing us, a reluctant people, concerning our full inclusion in His life.</span>','e2',94,4),
 ex('Jesus prayed. He fasted. He withdrew to be with His Father and gave Himself in obedience. <span class="g">He did these things as the beloved Son.</span>','e2',95,5),
 ex('Perhaps you sit down to pray and realize how tired you are. … Today you tell Him you are tired. You tell Him you miss enjoying Him. … <span class="g">You let that confession become your prayer.</span>','e3',96,6),
 ex('We can give ourselves freely to someone we love. <span class="g">We can also exhaust ourselves attempting to become someone worth loving.</span>','e2',97,7),
 ex('We have spent so much of our lives wondering what we must bring. <span class="g">Here, He gives us Himself.</span>','e1',98,8),
 page('<div class="body center"><img class="markbig" src="mark_ivory.png">'
      '<div class="eyebrow" style="margin-bottom:30px">Now being written</div>'
      '<div class="bt">Apostolic Architecture</div><div class="ba">Leah Ramirez &amp; Chris Berglund</div>'
      '<div class="rule" style="margin:44px auto"></div>'
      '<div class="serif small">Be the first to know when it releases.</div>'
      '<div class="eyebrow" style="margin-top:36px;color:rgba(244,236,222,0.7)">company318.substack.com</div></div>', 99, f'9 / {N}', None, foot='center'),
]
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files'])
    pg=b.new_page(viewport={'width':1080,'height':1350})
    for i,h in enumerate(slides,1):
        open(f'{D}/aa8_{i}.html','w').write(h); pg.goto(f'file://{D}/aa8_{i}.html'); pg.wait_for_timeout(400)
        pg.screenshot(path=f'{D}/out/aa8_{i}.png')
    b.close()
from PIL import Image
ims=[Image.open(f'{D}/out/aa8_{i}.png').resize((300,375)) for i in range(1,10)]
sh=Image.new('RGB',(5*310-10,2*385-10),'white')
for i,im in enumerate(ims): sh.paste(im,((i%5)*310,(i//5)*385))
sh.save(f'{D}/out/aa8_sheet.png'); print('ok')
