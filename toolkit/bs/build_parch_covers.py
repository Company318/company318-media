"""Parchment covers with framed photos: Behold (Chris & Leah) and Romans notes (Leah)."""
import sys
from playwright.sync_api import sync_playwright
src=open('/home/claude/bs/build_notes.py').read()
exec(src[:src.index("N=8")])
CSS = CSS + """
.frame2{position:absolute;left:96px;right:96px;top:150px;height:560px;display:flex;gap:10px;border:1px solid #b8924a;padding:10px;background:#efe5d4;}
.frame2 div{flex:1;background-color:#120b0a;background-repeat:no-repeat;}
.lowp{position:absolute;left:96px;right:96px;top:770px;text-align:center;}
.tp{font-size:84px;line-height:1.08;color:#1e2735;}
"""
BAND_OLD='<div class="band"><span>BEHOLD SCHOOL</span><span class="sep"></span><span>THE GOSPEL FROM WHICH WE LIVE</span></div>'
BAND_NEW='<div class="band"><span>BEHOLD</span><span class="sep"></span><span>CHRIS BERGLUND &amp; LEAH RAMIREZ</span></div>'
def cover(photos, eyebrow, title, sub, count, band=None):
    h = page(f'<div class="frame2">{photos}</div><div class="lowp"><div class="eyebrow">{eyebrow}</div>'+ORN+
             f'<div class="serif tp">{title}</div><div class="sub" style="margin-top:26px">{sub}</div></div>', count, crest=False)
    return h.replace(BAND_OLD, band) if band else h
CH='<div style="background-image:url(chris.png);background-size:118%;background-position:50% 0%"></div>'
LE='<div style="background-image:url(leah_padded.png);background-size:120%;background-position:50% -46px"></div>'
LE_SOLO='<div style="background-image:url(leah_padded.png);background-size:100%;background-position:50% -215px"></div>'
jobs={
 'behold1_1_photo': cover(CH+LE,'From the book in progress · Chapter One','Revelation <span class="r">Comes First</span>','<i>Behold</i> by Chris Berglund and Leah Ramirez','1 / 8',BAND_NEW),
 'note_pause_1_photo': cover(LE_SOLO,'A note from Leah','Let the Gospel <span class="r">create the question</span>','From <i>The Gospel From Which We Live</i>, Leah’s Romans 5–8 class at Behold School','1 / 8'),
 'note_joined_1_photo': cover(LE_SOLO,'A note from Leah','Joined to <span class="r">Another</span>','From <i>The Gospel From Which We Live</i>, Leah’s Romans 5–8 class at Behold School','1 / 8'),
 'note8_1_photo': cover(LE_SOLO,'A note from Leah · Week 8','The Gospel Is <span class="r">Ultimate Reality</span>','From <i>The Gospel From Which We Live</i>, Leah’s Romans 5–8 class at Behold School','1 / 8'),
}
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files'])
    pg=b.new_page(viewport={'width':1080,'height':1350})
    for n,h in jobs.items():
        open(f'{D}/{n}.html','w').write(h); pg.goto(f'file://{D}/{n}.html'); pg.wait_for_timeout(500)
        pg.screenshot(path=f'{D}/{n}.png')
    b.close()
from PIL import Image
ims=[Image.open(f'{D}/{n}.png').resize((405,506)) for n in jobs]
sh=Image.new('RGB',(4*415-10,506),'white')
for i,im in enumerate(ims): sh.paste(im,(i*415,0))
sh.save(f'{D}/parch_covers_sheet.png'); print('ok')
