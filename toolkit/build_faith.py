from playwright.sync_api import sync_playwright
D='/home/claude/leah'
F="""@font-face{font-family:Bask;src:url('file:///usr/share/fonts/truetype/baskerville/GFSBaskerville.otf');}
@font-face{font-family:InterM;src:url('file:///usr/share/fonts/opentype/inter/Inter-Medium.otf');}
html,body{margin:0;padding:0;}"""
G="""<div style="width:1080px;height:1350px;position:relative;overflow:hidden;background:radial-gradient(ellipse 90% 70% at 50% 35%,#2c3d30 0%,#1f2c23 70%,#18221b 100%);color:#f2ead9">
<div style="position:absolute;left:0;right:0;top:110px;text-align:center;font-family:InterM;font-size:19px;letter-spacing:0.34em;color:#c49a5a">THE GATHERING · SUNDAY</div>
<div style="position:absolute;left:50%;top:190px;width:1px;height:120px;background:linear-gradient(180deg,rgba(196,154,90,0),#c49a5a)"></div>
<div style="position:absolute;left:110px;right:110px;top:360px;text-align:center;font-family:Bask">
 <div style="font-size:104px;line-height:1.08">Faith looks like<br>a cross <span style="color:#c49a5a">and<br>resurrection.</span></div>
 <div style="margin:56px auto 0;width:840px;font-size:36px;line-height:1.45;font-style:italic;color:rgba(242,234,217,0.82)">Faith doesn’t mean I know how everything will turn out. It means I know the One who is asking me to trust Him.</div>
</div>
<div style="position:absolute;left:0;right:0;bottom:120px;display:flex;align-items:center;justify-content:center;gap:28px">
 <div style="width:150px;height:150px;border-radius:50%;background:#111 url(leah_bw_close.png) 50% 28%/cover;box-shadow:0 0 0 2px #c49a5a, 0 0 0 10px rgba(196,154,90,0.18)"></div>
 <div style="font-family:Bask;text-align:left">
  <div style="font-size:46px;line-height:1.05">Leah Ramirez</div>
  <div style="margin-top:12px;font-family:InterM;font-size:16px;letter-spacing:0.26em;color:#c49a5a;line-height:1.7">I SURRENDER ALL TO JESUS<br><span style="color:rgba(242,234,217,0.55)">COLORADO SPRINGS</span></div>
 </div></div></div>"""
def sw(name,cols,note):
    s=''.join(f'<div style="flex:1;background:{c};height:150px;display:flex;align-items:flex-end;padding:10px;font:600 14px Inter,sans-serif;color:{"#fff" if i==0 else "#222"}">{c}</div>' for i,c in enumerate(cols))
    return f'<div style="margin-bottom:34px"><div style="font:600 24px Inter,sans-serif;margin-bottom:6px">{name}</div><div style="font:16px Inter,sans-serif;color:#555;margin-bottom:10px">{note}</div><div style="display:flex;gap:6px">{s}</div></div>'
P=('<div style="width:1080px;padding:60px;box-sizing:border-box;background:#fff">'
 +sw('The Gathering (new)',['#1f2c23','#f2ead9','#c49a5a','#a5583a'],'Forest green, cream, brass, brick. Rooted, warm, local. Real photos stay without text.')
 +sw('Company 318',['#2e1727','#f4ecde','#d6b078','#150a10'],'Night sky: plum, ivory, gold. Teaching, vision, Apostolic Architecture.')
 +sw('Behold School',['#1e2735','#f7f1e6','#a64f30','#b8924a'],'Parchment, navy, rust, gold rules, crest. Class notes and the Behold book.')
 +sw('Leah personal',['#2f3324','#f6efe3','#9a6a3c','#e6d8c2'],'Warm paper, olive ink, copper. Your own writing on your own pages.')
 +'</div>')
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files']); pg=b.new_page(viewport={'width':1080,'height':1350})
    open(f'{D}/faith.html','w').write('<!doctype html><html><head><meta charset="utf-8"><style>'+F+'</style></head><body>'+G+'</body></html>')
    pg.goto(f'file://{D}/faith.html'); pg.wait_for_timeout(500); pg.screenshot(path=f'{D}/faith.png')
    pg.set_viewport_size({'width':1080,'height':900})
    open(f'{D}/palettes.html','w').write('<!doctype html><html><head><meta charset="utf-8"></head><body style="margin:0">'+P+'</body></html>')
    pg.goto(f'file://{D}/palettes.html'); pg.wait_for_timeout(300); pg.screenshot(path=f'{D}/palettes.png',full_page=True)
    b.close()
print('ok')
