"""Leah personal text carousel: 'Our message is a Man.' Editorial paper style. Her words verbatim."""
from playwright.sync_api import sync_playwright
D='/home/claude/leah'
CSS="""
@font-face{font-family:Bask;src:url('file:///usr/share/fonts/truetype/baskerville/GFSBaskerville.otf');}
@font-face{font-family:InterM;src:url('file:///usr/share/fonts/opentype/inter/Inter-Medium.otf');}
html,body{margin:0;padding:0;}
.c{width:1080px;height:1350px;position:relative;overflow:hidden;color:#2f3324;
   background:radial-gradient(ellipse 85% 80% at 50% 42%, #f8f2e7 0%, #f1e7d6 70%, #e8dac4 100%);}
.top{position:absolute;top:74px;left:110px;right:110px;display:flex;justify-content:space-between;
     font-family:InterM;font-size:19px;letter-spacing:0.28em;text-transform:uppercase;color:#9a6a3c;}
.top span:last-child{color:rgba(47,51,36,0.45);letter-spacing:0.16em}
.rule{position:absolute;top:122px;left:110px;width:70px;height:1px;background:rgba(154,106,60,0.6);}
.body{position:absolute;left:110px;right:110px;top:50%;transform:translateY(-50%);font-family:Bask;}
.body p{margin:0 0 34px;}
.body,.c{font-variant-numeric:lining-nums;font-feature-settings:"lnum" 1;}
.t1{font-size:70px;line-height:1.2;}
.t2{font-size:52px;line-height:1.32;}
.t3{font-size:45px;line-height:1.36;}
.c2{color:#9a6a3c;}
.n{font-family:"DejaVu Math TeX Gyre",serif;font-size:0.92em;}
.ref{font-family:InterM;font-size:18px;letter-spacing:0.22em;color:rgba(47,51,36,0.5);text-transform:uppercase;}
.foot{position:absolute;bottom:70px;left:110px;right:110px;display:flex;justify-content:space-between;
      font-family:InterM;font-size:17px;letter-spacing:0.26em;color:rgba(47,51,36,0.5);}
.photo{position:absolute;left:0;right:0;top:0;height:900px;background:#120b0a url(leah.png) center 18%/cover no-repeat;}
.fade{position:absolute;left:0;right:0;top:620px;height:300px;background:linear-gradient(180deg,rgba(241,231,214,0),#f1e7d6 92%);}
.sig{position:absolute;left:110px;right:110px;top:930px;text-align:center;}
.name{font-family:Bask;font-size:84px;line-height:1;color:#2f3324;}
.role{margin-top:20px;font-family:InterM;font-size:20px;letter-spacing:0.34em;text-transform:uppercase;color:#9a6a3c;}
.line{margin-top:34px;font-family:Bask;font-style:italic;font-size:38px;color:#4b4a3c;}
"""
N=9
def slide(inner,n):
    return ('<!doctype html><html><head><meta charset="utf-8"><style>'+CSS+'</style></head><body><div class="c">'
      f'<div class="top"><span>Leah Ramirez</span><span>{n} / {N}</span></div><div class="rule"></div>'
      f'<div class="body">{inner}</div><div class="foot"><span>@LEAHRAMIREZ247</span><span>SWIPE</span></div></div></body></html>')
S=[
 slide('<p class="t1">We have become so consumed with being apostolic and prophetic that I wonder if we have lost sight of <span class="c2">what the apostles themselves were consumed with.</span></p>',1),
 slide('<p class="t2">Paul wasn’t obsessed with establishing his apostolic identity. He had determined to know nothing among the people except Jesus Christ and Him crucified.</p><p class="ref">1 Corinthians 2:2</p><p class="t2 c2" style="margin-top:44px">Jesus saves. Jesus heals. Jesus delivers. He is our message!</p>',2),
 slide('<p class="t2">We have not been sent to herald our calling, establish our importance, or convince the world of our spiritual authority. We have been sent to herald the extraordinary Gift the Father has given to humanity: <span class="c2">His Son.</span></p><p class="t2 c2">And what a Gospel we have been entrusted to proclaim!</p>',3),
 slide('<p class="t2">Paul writes in <span class="n">2</span> Corinthians <span class="n">5</span> that if anyone is in Christ, there is a new creation. The old has passed away, and the new has come.</p><p class="t2">And then he tells us something astonishing: <span class="c2">All this is from God!</span></p>',4),
 slide('<p class="t2">God was in Christ reconciling the world to Himself, not counting people’s sins against them. And now He has entrusted to us the ministry and the message of reconciliation.</p><p class="t2">Think about that. <span class="c2">We have been entrusted with the announcement of what God has accomplished in Jesus Christ!</span></p>',5),
 slide('<p class="t2">We are His ambassadors, and through us the Father is making His appeal to the world: Be reconciled to God!</p><p class="ref">2 Corinthians 5:17–20</p><p class="t2" style="margin-top:44px">We don’t have to manufacture an apostolic movement. <span class="c2">We have been given an apostolic Gospel!</span></p>',6),
 slide('<p class="t3">And when we preach Jesus, when we announce His finished work, His resurrection, His victory, and the new life that has been opened to humanity through Him, we will discover what genuine apostolic fruit looks like.</p><p class="t3">People encountering Christ. People receiving His life. People discovering the Father who has reconciled them to Himself. And the Church being built upon the only foundation the apostles ever intended to lay.</p><p class="t2 c2">Jesus Christ.</p>',7),
 slide('<p class="t2">Our message is not our ministry. Our message is not our calling. Our message is not even the movement we hope to establish.</p><p class="t1 c2">Our message is a Man. Jesus Christ, crucified and risen!</p><p class="t2">And He is still the Good News for the whole world.</p>',8),
 ('<!doctype html><html><head><meta charset="utf-8"><style>'+CSS+'</style></head><body><div class="c"><div class="photo"></div><div class="fade"></div>'
  '<div class="sig"><div class="name">Leah Ramirez</div><div class="role">Writer &amp; Teacher</div><div class="line">“Our message is a Man.”</div></div>'
  f'<div class="foot" style="justify-content:center"><span>@LEAHRAMIREZ247</span></div></div></body></html>'),
]
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files'])
    pg=b.new_page(viewport={'width':1080,'height':1350})
    for i,h in enumerate(S,1):
        open(f'{D}/msg_{i}.html','w').write(h); pg.goto(f'file://{D}/msg_{i}.html'); pg.wait_for_timeout(450)
        pg.screenshot(path=f'{D}/msg_{i}.png')
    b.close()
from PIL import Image
ims=[Image.open(f'{D}/msg_{i}.png').resize((360,450)) for i in range(1,10)]
sh=Image.new('RGB',(5*370-10,2*460-10),'white')
for i,im in enumerate(ims): sh.paste(im,((i%5)*370,(i//5)*460))
sh.save(f'{D}/msg_sheet.png'); print('ok')
