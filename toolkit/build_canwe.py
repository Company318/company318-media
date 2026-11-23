from playwright.sync_api import sync_playwright
H="""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:Bask;src:url('file:///usr/share/fonts/truetype/baskerville/GFSBaskerville.otf');}
@font-face{font-family:InterM;src:url('file:///usr/share/fonts/opentype/inter/Inter-Medium.otf');}
html,body{margin:0}
.c{width:1080px;height:1350px;position:relative;background:#f2ead9;color:#1f2c23;font-family:Bask}
.b{position:absolute;left:120px;right:110px;top:50%;transform:translateY(-50%)}
p{margin:0;font-size:39px;line-height:1.42}
.h{font-family:InterM;font-size:20px;letter-spacing:0.3em;color:#a5583a;margin:0 0 18px}
.big{font-size:60px;line-height:1.2;margin:46px 0 46px}
.q{margin-top:50px;font-size:37px;font-style:italic;color:#33433a}
.f{position:absolute;left:0;right:0;bottom:90px;text-align:center;font-family:InterM;font-size:20px;letter-spacing:0.36em;color:#1f2c23}
</style></head><body><div class="c"><div class="b">
<p class="h">WE CANNOT</p>
<p>change another person’s heart.</p>
<p>manufacture a response to the Gospel.</p>
<p>produce the life of Christ through greater determination.</p>
<p class="big">But we can <span style="color:#a5583a">agree with Him.</span></p>
<p class="h">WE CAN</p>
<p>hear His Word and trust His faithfulness.</p>
<p>speak the Gospel again, even when we have spoken it many times before.</p>
<p>pray for the sick, love the wounded, and enter the conversations we would usually avoid.</p>
<p class="q" style="font-style:normal;color:#1f2c23">Our faith does not create His faithfulness.<br><span style="color:#a5583a">It lays hold of the Faithful One.</span></p>
</div><div class="f">LEAH RAMIREZ</div></div></body></html>"""
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files']); pg=b.new_page(viewport={'width':1080,'height':1350})
    open('/home/claude/leah/canwe.html','w').write(H); pg.goto('file:///home/claude/leah/canwe.html'); pg.wait_for_timeout(400)
    pg.screenshot(path='/home/claude/leah/canwe.png'); b.close()
print('ok')
