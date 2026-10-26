"""Behold, Chapter One excerpts. Authors: Chris Berglund & Leah Ramirez (Chris first). Verbatim; Scripture in ESV."""
from playwright.sync_api import sync_playwright
src = open('/home/claude/bs/build_notes.py').read()
exec(src[:src.index("N=8")])
BAND_OLD='<div class="band"><span>BEHOLD SCHOOL</span><span class="sep"></span><span>THE GOSPEL FROM WHICH WE LIVE</span></div>'
BAND_NEW='<div class="band"><span>BEHOLD</span><span class="sep"></span><span>CHRIS BERGLUND &amp; LEAH RAMIREZ</span></div>'
_page=page
def page(*a, **k): return _page(*a, **k).replace(BAND_OLD, BAND_NEW)
def s2(*a, **k): return s(*a, **k).replace(BAND_OLD, BAND_NEW)
N=8
slides=[
 page('<div class="body center"><div class="eyebrow">From the book in progress</div>'+ORN+
      '<div class="serif title">Revelation<br><span class="r">Comes First</span></div>'+ORN+
      '<div class="sub">Excerpts from Chapter One of <i>Behold</i><br>by Chris Berglund and Leah Ramirez</div></div>', f'1 / {N}'),
 s2('Somewhere along the way, it can begin to feel as though something depends upon <span class="r">our ability to get God to move.</span>','q1',2,N,'On prayer'),
 s2('In a strange and beautiful way, it is not only the end of our performance; <span class="r">beholding also frees us from requiring God to perform for us.</span>','q2',3,N),
 s2('Biblical beholding does not begin with our imagination. <span class="r">It begins with revelation.</span>','q1',4,N,'Is this just visualization?'),
 s2('God shines in our hearts, and what is revealed is a face.<br><br><span class="r">The face of Christ.</span>','q1',5,N,None,'2 Corinthians 4:6'),
 s2('We may have excellent theology on paper and still carry an inward picture of a God who is disappointed, reluctant, distant, irritated, withholding, or <span class="r">continually waiting for us to improve.</span>','q3',6,N),
 s2('We are not using imagination to decide what God should be like. <span class="r">We are allowing Jesus to correct the God we have imagined.</span>','q2',7,N),
 page('<div class="body center"><div class="eyebrow">Sit with this question</div>'+ORN+
      '<div class="serif q2">What picture of God have I been living from, and <span class="r">does it look like Jesus?</span></div>'+ORN+
      '<div class="sub"><i>Behold</i> is now being written.<br>Be the first to know when it releases:<br>company318.substack.com</div></div>', f'8 / {N}'),
]
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files'])
    pg=b.new_page(viewport={'width':1080,'height':1350})
    for i,html in enumerate(slides,1):
        open(f'{D}/behold1_{i}.html','w').write(html); pg.goto(f'file://{D}/behold1_{i}.html'); pg.wait_for_timeout(400)
        pg.screenshot(path=f'{D}/behold1_{i}.png')
    b.close()
from PIL import Image
ims=[Image.open(f'{D}/behold1_{i}.png').resize((360,450)) for i in range(1,9)]
sh=Image.new('RGB',(4*370-10,2*460-10),'white')
for i,im in enumerate(ims): sh.paste(im,((i%4)*370,(i//4)*460))
sh.save(f'{D}/behold1_sheet.png'); print('ok')
