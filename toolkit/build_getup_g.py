"""'It's time to get up' in The Gathering palette: cover + 11 text slides."""
from playwright.sync_api import sync_playwright
src=open('/home/claude/leah/build_getup_ig.py').read()
exec(src[:src.index("import shutil")])
GCSS=CSS.replace('#2f3324','#1f2c23').replace('#9a6a3c','#a5583a').replace('#4b4a3c','#33433a').replace('rgba(47,51,36','rgba(31,44,35').replace('rgba(154,106,60','rgba(165,88,58')
GCSS=GCSS.replace('background:radial-gradient(ellipse 85% 80% at 50% 42%, #f8f2e7 0%, #f1e7d6 70%, #e8dac4 100%);','background:radial-gradient(ellipse 85% 80% at 50% 42%, #f6efe1 0%, #f2ead9 70%, #e7dcc5 100%);')
BAND='<div style="position:absolute;left:0;right:0;bottom:0;height:110px;background:#1f2c23;display:flex;align-items:center;justify-content:space-between;padding:0 110px;font-family:InterM;font-size:18px;letter-spacing:0.28em;color:#c49a5a"><span>THE GATHERING</span><span style="color:rgba(242,234,217,0.6)">LEAH RAMIREZ</span></div>'
import re
def gs(h):
    h=re.sub(r'<div class="foot"[^>]*>.*?</div>', BAND, h, flags=re.S)
    return gs0(h)
def gs0(h): return h.replace(CSS,GCSS).replace('<span>Leah Ramirez</span>','<span>The Gathering · Sunday</span>').replace('<span>@LEAHRAMIREZ247</span><span>SWIPE</span>','<span>LEAH RAMIREZ</span><span>SWIPE</span>').replace('<span>@LEAHRAMIREZ247</span>','<span>THE GATHERING · COLORADO SPRINGS</span>')
F="""@font-face{font-family:Bask;src:url('file:///usr/share/fonts/truetype/baskerville/GFSBaskerville.otf');}
@font-face{font-family:InterM;src:url('file:///usr/share/fonts/opentype/inter/Inter-Medium.otf');}html,body{margin:0;padding:0;}"""
cover="""<div style="width:1080px;height:1350px;position:relative;overflow:hidden;background:radial-gradient(ellipse 90% 70% at 30% 35%,#2c3d30 0%,#1f2c23 70%,#18221b 100%);color:#f2ead9">
<div style="position:absolute;right:0;top:0;width:540px;height:1350px;background:#111 url(leah_bw.png) 50% 30%/cover no-repeat;"></div>
<div style="position:absolute;left:480px;top:0;width:140px;height:1350px;background:linear-gradient(90deg,#1f2c23 15%,rgba(31,44,35,0))"></div>
<div style="position:absolute;left:90px;top:120px;font-family:InterM;font-size:19px;letter-spacing:0.3em;color:#c49a5a">THE GATHERING · SUNDAY</div>
<div style="position:absolute;left:90px;top:175px;width:70px;height:1px;background:#c49a5a"></div>
<div style="position:absolute;left:90px;top:330px;width:410px;font-family:Bask;">
  <div style="font-size:90px;line-height:1.06">It’s time<br>to <span style="color:#c49a5a">get up.</span></div>
  <div style="margin-top:56px;font-size:36px;line-height:1.35;font-style:italic;color:rgba(242,234,217,0.82)">There comes a point when staying in the hospital bed is no longer recovery.</div>
</div>
<div style="position:absolute;left:90px;bottom:110px;width:440px;font-family:Bask;">
  <div style="font-size:44px">Leah Ramirez</div>
  <div style="margin-top:14px;font-family:InterM;font-size:17px;letter-spacing:0.24em;color:#c49a5a;line-height:1.7">I SURRENDER ALL TO JESUS<br><span style="color:rgba(242,234,217,0.55)">COLORADO SPRINGS</span></div>
</div></div>"""
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files']); pg=b.new_page(viewport={'width':1080,'height':1350})
    open(f'{D}/getup_g_1.html','w').write('<!doctype html><html><head><meta charset="utf-8"><style>'+F+'</style></head><body>'+cover+'</body></html>')
    pg.goto(f'file://{D}/getup_g_1.html'); pg.wait_for_timeout(500); pg.screenshot(path=f'{D}/getup_g_1.png')
    jobs=[(n,gs(slide(h,n))) for n,h in S.items()]+[(12,gs(end))]
    for n,h in jobs:
        open(f'{D}/getup_g_{n}.html','w').write(h); pg.goto(f'file://{D}/getup_g_{n}.html'); pg.wait_for_timeout(400)
        pg.screenshot(path=f'{D}/getup_g_{n}.png')
    b.close()
from PIL import Image
ims=[Image.open(f'{D}/getup_g_{i}.png').resize((300,375)) for i in range(1,13)]
sh=Image.new('RGB',(6*310-10,2*385-10),'white')
for i,im in enumerate(ims): sh.paste(im,((i%6)*310,(i//6)*385))
sh.save(f'{D}/getup_g_sheet.png'); print('ok')
