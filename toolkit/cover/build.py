"""Two Facebook cover options for Leah Ramirez, 1640x924 (shows fully on phones; desktop crops to the middle ~624px)."""
from playwright.sync_api import sync_playwright
from PIL import Image, ImageDraw

D = '/home/claude/cover'
FONTS = """
@font-face{font-family:Bask;src:url('file:///usr/share/fonts/truetype/baskerville/GFSBaskerville.otf');}
@font-face{font-family:InterM;src:url('file:///usr/share/fonts/opentype/inter/Inter-Medium.otf');}
html,body{margin:0;padding:0;}
.c{width:1640px;height:924px;position:relative;overflow:hidden;}
"""

# Option A: portrait on the right, warm dark room, text left-center (kept above the desktop profile-photo overlap).
A = """<!doctype html><html><head><meta charset="utf-8"><style>""" + FONTS + """
.c{background:#1c120c;}
.photo{position:absolute;right:0;top:-40px;height:1004px;
  -webkit-mask-image:linear-gradient(90deg,transparent 0%,#000 38%);mask-image:linear-gradient(90deg,transparent 0%,#000 38%);}
.glow{position:absolute;inset:0;background:radial-gradient(ellipse 50% 70% at 22% 50%, rgba(196,140,80,0.10), rgba(0,0,0,0) 70%);}
.txt{position:absolute;left:150px;top:300px;width:720px;color:#f3e9da;}
.name{font-family:Bask;font-size:96px;line-height:1;letter-spacing:0.01em;}
.role{margin-top:26px;font-family:InterM;font-size:22px;letter-spacing:0.34em;text-transform:uppercase;color:#c99a62;}
.rule{width:70px;height:1px;background:rgba(201,154,98,0.7);margin:34px 0 30px;}
.line{font-family:Bask;font-style:italic;font-size:40px;line-height:1.3;color:rgba(243,233,218,0.88);}
.ref{margin-top:14px;font-family:InterM;font-size:17px;letter-spacing:0.26em;color:rgba(243,233,218,0.5);}
</style></head><body><div class="c">
<img class="photo" src="portrait.png"><div class="glow"></div>
<div class="txt"><div class="name">Leah Ramirez</div><div class="role">Writer &amp; Teacher</div><div class="rule"></div>
<div class="line">“We were joined to a Person.”</div><div class="ref">ON ROMANS 7:4</div></div>
</div></body></html>"""

# Option B: editorial type only, on warm paper with a deep olive panel; centered so it survives every crop.
B = """<!doctype html><html><head><meta charset="utf-8"><style>""" + FONTS + """
.c{background:radial-gradient(ellipse 80% 90% at 50% 45%, #f6efe3 0%, #efe5d4 70%, #e6d8c2 100%);}
.frame{position:absolute;left:60px;right:60px;top:170px;bottom:170px;border-top:1px solid rgba(58,64,44,0.35);border-bottom:1px solid rgba(58,64,44,0.35);}
.txt{position:absolute;left:0;right:0;top:50%;transform:translateY(-50%);text-align:center;color:#2f3324;}
.role{font-family:InterM;font-size:21px;letter-spacing:0.38em;text-transform:uppercase;color:#9a6a3c;}
.name{margin-top:22px;font-family:Bask;font-size:120px;line-height:1;letter-spacing:0.02em;color:#2f3324;}
.line{margin-top:30px;font-family:Bask;font-style:italic;font-size:40px;line-height:1.3;color:#4b4a3c;}
.ref{margin-top:14px;font-family:InterM;font-size:16px;letter-spacing:0.26em;color:rgba(47,51,36,0.5);}
</style></head><body><div class="c"><div class="frame"></div>
<div class="txt"><div class="role">Writer &amp; Teacher</div><div class="name">Leah Ramirez</div>
<div class="line">“We were joined to a Person.”</div><div class="ref">ON ROMANS 7:4</div></div>
</div></body></html>"""

with sync_playwright() as p:
    b = p.chromium.launch(args=['--allow-file-access-from-files'])
    pg = b.new_page(viewport={'width': 1640, 'height': 924})
    for name, html in [('cover_A', A), ('cover_B', B)]:
        open(f'{D}/{name}.html', 'w').write(html)
        pg.goto(f'file://{D}/{name}.html'); pg.wait_for_timeout(500)
        pg.screenshot(path=f'{D}/{name}.png')
    b.close()

# Preview: how each looks on a phone (full) and a computer (middle band), with the profile photo circle where Facebook puts it.
for name in ['cover_A', 'cover_B']:
    im = Image.open(f'{D}/{name}.png').convert('RGB')
    desk = im.crop((0, 150, 1640, 774)).resize((820, 312))
    phone = im.resize((640, 360))
    sheet = Image.new('RGB', (820, 312 + 30 + 360 + 60), (240, 242, 245))
    sheet.paste(desk, (0, 0))
    dr = ImageDraw.Draw(sheet)
    dr.ellipse((30, 230, 200, 400), fill=(255, 255, 255), outline=(24, 119, 242), width=4)  # desktop profile photo overlap
    sheet.paste(phone, (90, 312 + 50))
    sheet.save(f'{D}/{name}_preview.png')
print('ok')
