"""Apostolic Architecture, Chapter 7 excerpts. Verbatim from the manuscript. No Juniah material."""
from playwright.sync_api import sync_playwright
D = '/home/claude/c318art'
src = open(f'{D}/build_slides.py').read()
exec(src[:src.index("TAG = ")])
CSS = CSS + """
.ex{font-family:'GFS Baskerville',serif;color:#f4ecde;}
.e1{font-size:64px;line-height:1.24;}
.e2{font-size:54px;line-height:1.3;}
.e3{font-size:46px;line-height:1.38;}
.src{margin-top:52px;font-family:InterM;font-size:19px;letter-spacing:0.24em;text-transform:uppercase;color:rgba(244,236,222,0.55);}
.bt{font-family:'GFS Baskerville',serif;font-size:72px;line-height:1.12;}
.ba{margin-top:18px;font-family:InterM;font-size:20px;letter-spacing:0.24em;text-transform:uppercase;color:rgba(214,176,120,0.9);}
"""
TAG = 'Apostolic Architecture · Chapter 7'
N = 8
SRC = '<div class="src">From Apostolic Architecture</div>'
def ex(text, size, seed, n, ref=None, ctx=None):
    r = f'<div class="eyebrow ref">{ref}</div>' if ref else ''
    c = f'<div class="eyebrow" style="margin-bottom:44px">{ctx}</div>' if ctx else ''
    return page(f'<div class="body">{c}<div class="ex {size}">{text}</div>{r}</div>', seed, f'{n} / {N}', TAG)

carousel = [
  page('<div class="body"><div class="eyebrow" style="margin-bottom:48px">From the book in progress</div>'
       '<div class="serif big">Grace That<br><span class="g">Forms Us</span></div>'
       '<div class="rule"></div><div class="serif small">Excerpts from Chapter 7 of <i>Apostolic Architecture</i> by Leah Ramirez and Chris Berglund.</div></div>',
       71, f'1 / {N}'),
  ex('Many of us learned early to hesitate at the doorway. We watched a face and listened to a tone of voice before deciding whether it was a good time to need something.', 'e2', 72, 2),
  ex('We may have known we were loved while remaining uncertain <span class="g">whether we were welcome.</span>', 'e1', 73, 3),
  ex('We need to know more than whether our Father’s door is open. <span class="g">We need to know the Father who is waiting there.</span>', 'e1', 74, 4),
  ex('The impulse to hide reaches all the way back to the garden. When God called, Adam explained that he had been afraid because he was naked.<br><br>He had always been naked before God. <span class="g">Now he was afraid to be seen.</span>', 'e3', 75, 5, 'Genesis 3:7–10', 'Adam and Eve in the garden'),
  ex('He made garments of skins and clothed them. <span class="g">The people who were hiding were clothed by the One from whom they hid.</span>', 'e2', 76, 6, 'Genesis 3:21', 'God clothes Adam and Eve'),
  ex('We aren’t transformed so that we can come. <span class="g">We come so that we can be transformed.</span>', 'e1', 77, 7),
  page('<div class="body center"><img class="markbig" src="mark_ivory.png">'
       '<div class="eyebrow" style="margin-bottom:30px">Now being written</div>'
       '<div class="bt">Apostolic Architecture</div><div class="ba">Leah Ramirez &amp; Chris Berglund</div>'
       '<div class="rule" style="margin:44px auto"></div>'
       '<div class="serif small">Be the first to know when it releases.</div>'
       '<div class="eyebrow" style="margin-top:36px;color:rgba(244,236,222,0.7)">company318.substack.com</div></div>',
       78, f'8 / {N}', None, foot='center'),
]
def card(text, size, seed, ref=None):
    r = f'<div class="eyebrow ref">{ref}</div>' if ref else ''
    return page(f'<div class="body"><div class="eyebrow" style="margin-bottom:56px">From Apostolic Architecture</div>'
                f'<div class="ex {size}">{text}</div>{r}'
                '<div class="src">Leah Ramirez &amp; Chris Berglund · Now being written</div></div>', seed)
cards = {
  'aa7_card_rename': card('Our feelings cannot tell us what Christ accomplished. And our failure does not have the authority to <span class="g">rename the person He has joined to Himself.</span>', 'e2', 81),
  'aa7_card_perfected': card('Perfected for all time, and being sanctified. <span class="g">Christ’s offering is complete. Our learning continues.</span>', 'e1', 82, 'Hebrews 10:14'),
  'aa7_card_responsibility': card('Grace allows us to take responsibility that is ours. <span class="g">It also allows us to let go of responsibility that is not ours.</span>', 'e2', 83),
  'aa7_card_near': card('Everything is seen, <span class="g">and we are invited near.</span>', 'e1', 84, 'Hebrews 4:13–16'),
}
jobs = [(f'aa7_{i+1}', h) for i, h in enumerate(carousel)] + list(cards.items())
with sync_playwright() as p:
    b = p.chromium.launch(args=['--allow-file-access-from-files'])
    pg = b.new_page(viewport={'width':1080,'height':1350})
    for name, html in jobs:
        open(f'{D}/{name}.html','w').write(html)
        pg.goto(f'file://{D}/{name}.html'); pg.wait_for_timeout(400)
        pg.screenshot(path=f'{D}/out/{name}.png')
    b.close()
from PIL import Image
for fname, names in [('aa7_carousel_sheet', [f'aa7_{i}' for i in range(1,9)]), ('aa7_cards_sheet', list(cards))]:
    ims=[Image.open(f'{D}/out/{n}.png').resize((360,450)) for n in names]
    cols=4
    rows=(len(ims)+cols-1)//cols
    sheet=Image.new('RGB',(360*cols+10*(cols-1),450*rows+10*(rows-1)),'white')
    for i,im in enumerate(ims): sheet.paste(im,((i%cols)*370,(i//cols)*460))
    sheet.save(f'{D}/out/{fname}.png'); print('ok',len(jobs))
