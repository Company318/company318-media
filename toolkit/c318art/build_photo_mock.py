from playwright.sync_api import sync_playwright
src=open('/home/claude/c318art/build_aa8.py').read()
exec(src[:src.index("slides=[")])
CSS = CSS + """
.duo{position:absolute;left:0;right:0;top:0;height:760px;display:flex;}
.duo div{flex:1;background-size:cover;background-position:center 20%;}
.fade{position:absolute;left:0;right:0;top:420px;height:360px;background:linear-gradient(180deg,rgba(33,16,25,0),#211019 85%);}
.low{position:absolute;left:120px;right:120px;top:800px;}
.solo{position:absolute;left:0;right:0;top:0;height:820px;background-size:cover;background-position:center 18%;}
.names{display:flex;justify-content:space-between;position:absolute;left:0;right:0;top:700px;padding:0 70px;font-family:InterM;font-size:18px;letter-spacing:0.24em;color:rgba(244,236,222,0.8);}
"""
A = page('<div class="duo"><div style="background-image:url(chris.png);background-size:114%;background-position:50% 0%"></div><div style="background-color:#120b0a;background-image:url(leah.png);background-size:auto 100%;background-position:50% 48px;background-repeat:no-repeat"></div></div><div class="fade"></div><div style="position:absolute;left:0;right:0;top:0;height:150px;background:linear-gradient(180deg,#120b0a 25%,rgba(18,11,10,0))"></div>'
  '<div class="low"><div class="eyebrow" style="margin-bottom:28px">From the book in progress · Chapter 8</div>'
  '<div class="serif big">Intimacy <span class="g">Without Distance</span></div>'
  '<div class="serif small" style="margin-top:24px"><i>Apostolic Architecture</i><br>Leah Ramirez &amp; Chris Berglund</div></div>', 91, f'1 / 9')
A = A.replace('<canvas id="s"','<canvas style="display:none" id="s"')
B = page('<div class="solo" style="background-image:url(leah.png)"></div><div class="fade" style="top:480px"></div>'
  '<div class="low" style="top:860px"><div class="eyebrow" style="margin-bottom:28px">A teaching from Leah Ramirez</div>'
  '<div class="serif big">We aren’t convincing <span class="g">a reluctant God.</span></div></div>', 92)
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files'])
    pg=b.new_page(viewport={'width':1080,'height':1350})
    for n,h in [('mockA',A),('mockB',B)]:
        open(f'{D}/{n}.html','w').write(h); pg.goto(f'file://{D}/{n}.html'); pg.wait_for_timeout(500)
        pg.screenshot(path=f'{D}/out/{n}.png')
    b.close()
from PIL import Image
ims=[Image.open(f'{D}/out/{n}.png').resize((540,675)) for n in ['aa8_1','mockA','mockB']]
sh=Image.new('RGB',(3*550-10,675),'white')
for i,im in enumerate(ims): sh.paste(im,(i*550,0))
sh.save(f'{D}/out/photo_mock_sheet.png'); print('ok')
