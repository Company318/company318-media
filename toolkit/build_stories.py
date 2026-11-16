from playwright.sync_api import sync_playwright
D='/home/claude/leah'
F="""<style>@font-face{font-family:Bask;src:url('file:///usr/share/fonts/truetype/baskerville/GFSBaskerville.otf');}
@font-face{font-family:InterM;src:url('file:///usr/share/fonts/opentype/inter/Inter-Medium.otf');}html,body{margin:0;padding:0;}</style>"""
BG="background:radial-gradient(ellipse 90% 70% at 50% 40%,#2c3d30 0%,#1f2c23 70%,#18221b 100%);color:#f2ead9"
A=f"""<div style="width:1080px;height:1920px;position:relative;overflow:hidden;{BG}">
<div style="position:absolute;left:0;right:0;top:0;height:1100px;background:#111 url(leah_bw.png) 50% 22%/cover no-repeat;"></div>
<div style="position:absolute;left:0;right:0;top:760px;height:360px;background:linear-gradient(180deg,rgba(31,44,35,0),#1f2c23 88%)"></div>
<div style="position:absolute;left:0;right:0;top:1120px;text-align:center;font-family:Bask">
 <div style="font-family:InterM;font-size:22px;letter-spacing:0.34em;color:#c49a5a">THE GATHERING · SUNDAY</div>
 <div style="margin-top:40px;font-size:118px;line-height:1.04">It’s time<br>to <span style="color:#c49a5a">get up.</span></div>
 <div style="margin:44px auto 0;width:820px;font-size:42px;line-height:1.35;font-style:italic;color:rgba(242,234,217,0.82)">There comes a point when staying in the hospital bed is no longer recovery.</div>
 <div style="margin-top:70px;font-family:InterM;font-size:22px;letter-spacing:0.28em;color:rgba(242,234,217,0.6)">LEAH RAMIREZ · NEW POST</div>
</div></div>"""
B=f"""<div style="width:1080px;height:1920px;position:relative;overflow:hidden;{BG}">
<div style="position:absolute;left:0;right:0;top:300px;text-align:center;font-family:InterM;font-size:22px;letter-spacing:0.34em;color:#c49a5a">THE GATHERING · SUNDAY</div>
<div style="position:absolute;left:50%;top:380px;width:1px;height:150px;background:linear-gradient(180deg,rgba(196,154,90,0),#c49a5a)"></div>
<div style="position:absolute;left:90px;right:90px;top:590px;text-align:center;font-family:Bask">
 <div style="font-size:118px;line-height:1.08">Faith looks like<br>a cross <span style="color:#c49a5a">and<br>resurrection.</span></div>
 <div style="margin:64px auto 0;width:860px;font-size:42px;line-height:1.42;font-style:italic;color:rgba(242,234,217,0.82)">Faith doesn’t mean I know how everything will turn out. It means I know the One who is asking me to trust Him.</div>
</div>
<div style="position:absolute;left:0;right:0;bottom:300px;display:flex;align-items:center;justify-content:center;gap:30px">
 <div style="width:170px;height:170px;border-radius:50%;background:#111 url(leah_bw_close.png) 50% 28%/cover;box-shadow:0 0 0 2px #c49a5a, 0 0 0 11px rgba(196,154,90,0.18)"></div>
 <div style="font-family:Bask;text-align:left"><div style="font-size:52px">Leah Ramirez</div>
 <div style="margin-top:12px;font-family:InterM;font-size:19px;letter-spacing:0.26em;color:#c49a5a">NEW POST</div></div></div></div>"""
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files']); pg=b.new_page(viewport={'width':1080,'height':1920})
    for n,h in [('story_getup',A),('story_faith',B)]:
        open(f'{D}/{n}.html','w').write('<!doctype html><html><head><meta charset="utf-8">'+F+'</head><body>'+h+'</body></html>')
        pg.goto(f'file://{D}/{n}.html'); pg.wait_for_timeout(500); pg.screenshot(path=f'{D}/{n}.png')
    b.close()
from PIL import Image
ims=[Image.open(f'{D}/{n}.png').resize((405,720)) for n in ['story_getup','story_faith']]
sh=Image.new('RGB',(820,720),'white'); sh.paste(ims[0],(0,0)); sh.paste(ims[1],(415,0)); sh.save(f'{D}/stories_sheet.png'); print('ok')
