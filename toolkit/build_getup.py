from playwright.sync_api import sync_playwright
D='/home/claude/leah'
CSS="""
@font-face{font-family:Bask;src:url('file:///usr/share/fonts/truetype/baskerville/GFSBaskerville.otf');}
@font-face{font-family:InterM;src:url('file:///usr/share/fonts/opentype/inter/Inter-Medium.otf');}
html,body{margin:0;padding:0;}
.c{width:1080px;height:1350px;position:relative;overflow:hidden;background:#f3ebdd;}
"""
A="""<div class="c">
<div style="position:absolute;right:0;top:0;width:540px;height:1350px;background:#111 url(leah_bw.png) 50% 30%/cover no-repeat;"></div>
<div style="position:absolute;left:500px;top:0;width:120px;height:1350px;background:linear-gradient(90deg,#f3ebdd 10%,rgba(243,235,221,0))"></div>
<div style="position:absolute;left:90px;top:120px;width:470px;font-family:InterM;font-size:19px;letter-spacing:0.3em;color:#9a6a3c;text-transform:uppercase">A word from Sunday</div>
<div style="position:absolute;left:90px;top:175px;width:70px;height:1px;background:#9a6a3c"></div>
<div style="position:absolute;left:90px;top:330px;width:410px;font-family:Bask;color:#2f3324;">
  <div style="font-size:90px;line-height:1.06">It’s time<br>to get up.</div>
  <div style="margin-top:56px;font-size:36px;line-height:1.35;font-style:italic;color:#4b4a3c">There comes a point when staying in the hospital bed is no longer recovery.</div>
</div>
<div style="position:absolute;left:90px;bottom:110px;width:440px;font-family:Bask;">
  <div style="font-size:44px;color:#2f3324">Leah Ramirez</div>
  <div style="margin-top:14px;font-family:InterM;font-size:17px;letter-spacing:0.24em;color:#9a6a3c;line-height:1.7">I SURRENDER ALL TO JESUS<br><span style="color:rgba(47,51,36,0.55)">THE GATHERING · COMPANY 318</span></div>
</div></div>"""
B="""<div class="c" style="background:#141414">
<div style="position:absolute;left:0;right:0;top:0;height:880px;background:#111 url(leah_bw_close.png) 50% 22%/cover no-repeat;"></div>
<div style="position:absolute;left:0;right:0;top:560px;height:340px;background:linear-gradient(180deg,rgba(20,20,20,0),#141414 88%)"></div>
<div style="position:absolute;left:0;right:0;top:860px;text-align:center;font-family:Bask;color:#f3ebdd">
  <div style="font-size:120px;line-height:1">It’s time to get up.</div>
  <div style="margin:40px auto 0;width:820px;font-size:40px;line-height:1.35;font-style:italic;color:rgba(243,235,221,0.8)">The bandages have done their work.</div>
  <div style="margin-top:70px;font-family:InterM;font-size:18px;letter-spacing:0.3em;color:#d6b078">LEAH RAMIREZ</div>
</div></div>"""
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files']); pg=b.new_page(viewport={'width':1080,'height':1350})
    for n,h in [('getup_A',A),('getup_B',B)]:
        open(f'{D}/{n}.html','w').write('<!doctype html><html><head><meta charset="utf-8"><style>'+CSS+'</style></head><body>'+h+'</body></html>')
        pg.goto(f'file://{D}/{n}.html'); pg.wait_for_timeout(500); pg.screenshot(path=f'{D}/{n}.png')
    b.close()
from PIL import Image
ims=[Image.open(f'{D}/{n}.png').resize((540,675)) for n in ['getup_A','getup_B']]
sh=Image.new('RGB',(1090,675),'white'); sh.paste(ims[0],(0,0)); sh.paste(ims[1],(550,0)); sh.save(f'{D}/getup_sheet.png'); print('ok')
