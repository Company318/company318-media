"""Week 10 note from Leah: The Harvest Is Ready (+ Romans 8:18-25 commentary). Words verbatim; Scripture ESV. Photo cover."""
from playwright.sync_api import sync_playwright
src=open('/home/claude/bs/build_parch_covers.py').read()
exec(src[:src.index("jobs={")])
CSS = CSS + '''
.softp{position:absolute;left:0;right:0;top:0;height:820px;background:url(leah.png) 50% 18%/cover no-repeat;
-webkit-mask-image:linear-gradient(180deg,#000 0%,#000 36%,rgba(0,0,0,.75) 55%,rgba(0,0,0,.4) 72%,rgba(0,0,0,.15) 86%,rgba(0,0,0,0) 100%);mask-image:linear-gradient(180deg,#000 0%,#000 36%,rgba(0,0,0,.75) 55%,rgba(0,0,0,.4) 72%,rgba(0,0,0,.15) 86%,rgba(0,0,0,0) 100%);}
'''
def softcover(eyebrow,title,sub,count):
    return page(f'<div class="softp"></div><div class="lowp" style="top:862px;display:flex;flex-direction:column;align-items:center"><div class="eyebrow">{eyebrow}</div>'+ORN+
             f'<div class="serif tp">{title}</div><div class="sub" style="margin-top:16px">{sub}</div></div>', count, crest=False)
N=10
slides=[
 softcover('A note from Leah · Week 10','The Harvest <span class="r">Is Ready</span>','From <i>The Gospel From Which We Live</i>,<br>Leah’s Romans 5–8 class at Behold School',f'1 / {N}'),
 s('Paul doesn’t describe this groaning as merely the suffering of a world falling apart. He describes it as childbirth. <span class="r">He sees expectation.</span>','q2',2,N),
 s('“For we know that the whole creation has been groaning together in the pains of childbirth until now. And not only the creation, but we ourselves, who have the firstfruits of the Spirit, <span class="r">groan inwardly as we wait eagerly for adoption as sons, the redemption of our bodies.</span>”','q3',3,N,None,'Romans 8:22–23'),
 s('A mother does not labor to create the child she carries. The child is already there.<br><br><span class="r">Labor belongs to the process of bringing into view a life that has been growing, hidden from sight.</span>','q3',4,N),
 s('In my imagination, the whole city became a field of standing grain. <span class="r">An entire city standing in the Father’s harvest field.</span>','q2',5,N,'Driving through Colorado Springs'),
 s('“Look, I tell you, lift up your eyes, and see that the fields are <span class="r">white for harvest.</span>”','q1',6,N,None,'John 4:35'),
 s('Our groaning is not necessarily evidence of what we lack. <span class="r">Sometimes it is the expression of a life we have already begun to share.</span>','q2',7,N),
 s('The Spirit has not made me indifferent to what Christ loves. <span class="r">My longing does not contradict my belonging.</span>','q2',8,N,'What the Gospel is announcing'),
 s('The firstfruits have been given, and the harvest is coming. <span class="r">While we wait, the life of the One whose return we await is already finding expression in us.</span>','q2',9,N),
 end(10,N),
]
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files'])
    pg=b.new_page(viewport={'width':1080,'height':1350})
    for i,h in enumerate(slides,1):
        open(f'{D}/note10_{i}.html','w').write(h); pg.goto(f'file://{D}/note10_{i}.html'); pg.wait_for_timeout(450)
        pg.screenshot(path=f'{D}/note10_{i}.png')
    b.close()
from PIL import Image
ims=[Image.open(f'{D}/note10_{i}.png').resize((360,450)) for i in range(1,N+1)]
sh=Image.new('RGB',(5*370-10,2*460-10),'white')
for i,im in enumerate(ims): sh.paste(im,((i%5)*370,(i//5)*460))
sh.save(f'{D}/note10_sheet.png'); print('ok')
