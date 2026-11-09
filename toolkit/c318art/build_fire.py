"""Chris Berglund, The Fire That Never Goes Out. Night sky, Chris photo cover."""
from playwright.sync_api import sync_playwright
src=open('/home/claude/c318art/build_aa8.py').read()
exec(src[:src.index("TAG='Apostolic")])
src2=open('/home/claude/c318art/build_photo_mock.py').read()
exec(src2[src2.index('CSS = CSS + """'):src2.index("A = page(")])
TAG='Chris Berglund · Sunday Message'
N=8
def ex(text, size, seed, n, ref=None, ctx=None):
    r = f'<div class="eyebrow ref">{ref}</div>' if ref else ''
    c = f'<div class="eyebrow" style="margin-bottom:44px">{ctx}</div>' if ctx else ''
    return page(f'<div class="body">{c}<div class="ex {size}">{text}</div>{r}</div>', seed, f'{n} / {N}', TAG)
cover = page('<div class="solo" style="background-color:#120b0a;background-image:url(chris.png);background-size:100%;background-position:50% 8%;background-repeat:no-repeat"></div><div class="fade" style="top:480px"></div>'
  '<div class="low" style="top:860px"><div class="eyebrow" style="margin-bottom:28px">A teaching from Chris Berglund</div>'
  '<div class="serif big">The Fire That<br><span class="g">Never Goes Out</span></div></div>', 101, f'1 / {N}')
slides=[cover,
 ex('“Fire shall be kept burning on the altar continually; it shall not go out.”','e1',102,2,'Leviticus 6:13','The burnt offering'),
 ex('Jesus was that burnt offering. <span class="g">We’re consecrated because we’re in Christ.</span>','e1',103,3,'Hebrews 10:12'),
 ex('If we make it about us, it’s not about Him anymore. It’s about my consecration. It’s about my performance.<br><br><span class="g">He is the fire.</span>','e2',104,4),
 ex('“The glory that you have given me I have given to them, that they may be one even as we are one.”','e2',105,5,'John 17:22','Jesus prays, hours before the cross'),
 ex('We keep praying for what God’s already given to us. <span class="g">Jesus’ prayers always get answered.</span>','e1',106,6),
 ex('Humility is agreement.<br><br><span class="g">We’re participating in His life.</span>','e1',107,7),
 page('<div class="body center"><img class="markbig" src="mark_ivory.png">'
      '<div class="eyebrow" style="margin-bottom:30px">Full message</div>'
      '<div class="bt">The Fire That<br>Never Goes Out</div><div class="ba">Chris Berglund</div><div class="serif small" style="margin-top:22px">Preached at The Gathering<br>Colorado Springs</div>'
      '<div class="rule" style="margin:44px auto"></div>'
      '<div class="serif small">Search Company 318 on YouTube.</div></div>', 108, f'8 / {N}', None, foot='center'),
]
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files'])
    pg=b.new_page(viewport={'width':1080,'height':1350})
    for i,h in enumerate(slides,1):
        open(f'{D}/fire_{i}.html','w').write(h); pg.goto(f'file://{D}/fire_{i}.html'); pg.wait_for_timeout(450)
        pg.screenshot(path=f'{D}/out/fire_{i}.png')
    b.close()
from PIL import Image
ims=[Image.open(f'{D}/out/fire_{i}.png').resize((360,450)) for i in range(1,9)]
sh=Image.new('RGB',(4*370-10,2*460-10),'white')
for i,im in enumerate(ims): sh.paste(im,((i%4)*370,(i//4)*460))
sh.save(f'{D}/out/fire_sheet.png'); print('ok')
