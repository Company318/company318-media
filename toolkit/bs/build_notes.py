"""Two carousels from Leah's 'A Note from Leah' (Romans 5-8 class), Behold School style. Leah's words verbatim; Scripture quoted from the ESV."""
from playwright.sync_api import sync_playwright
src = open('/home/claude/bs/build_bs_post8.py').read()
exec(src[:src.index("slides = [")])
CSS = CSS + """
.ctx{font-family:InterM;font-size:20px;letter-spacing:0.26em;text-transform:uppercase;color:#a64f30;margin-bottom:40px;}
.ref2{margin-top:40px;font-family:InterM;font-size:19px;letter-spacing:0.24em;text-transform:uppercase;color:#8a7a62;}
.title{font-size:96px;line-height:1.08;color:#1e2735;}
.sub{font-family:InterR;font-size:28px;line-height:1.5;color:#4a423b;}
"""
D='/home/claude/bs'
def s(text, size, n, N, ctx=None, ref=None):
    c=f'<div class="ctx">{ctx}</div>' if ctx else ''
    r=f'<div class="ref2">{ref}</div>' if ref else ''
    return page(f'<div class="body">{c}<div class="serif {size}">{text}</div>{r}</div>', f'{n} / {N}')
def cover(title, n, N):
    return page('<div class="body center"><div class="eyebrow">A note from Leah</div>'+ORN+
        f'<div class="serif title">{title}</div>'+ORN+
        '<div class="sub">From <i>The Gospel From Which We Live</i>,<br>Leah’s Romans 5–8 class at Behold School</div></div>', f'{n} / {N}')
def end(n, N):
    return page('<div class="body center"><img class="bigcrest" src="shield.png">'+ORN+
        '<div class="serif q2">Leah is writing <span class="r">Romans 5–8</span>, a study that grows out of this class.</div>'+ORN+
        '<div class="sub">Be the first to know when it releases:<br>company318.substack.com</div></div>', f'{n} / {N}', crest=False)
N=8
joined=[
 cover('Joined to<br><span class="r">Another</span>',1,N),
 s('He came for me before I knew how to <span class="r">come to Him.</span>','q1',2,N),
 s('She went looking for the one she loved, and she was bruised by those she encountered along the way.','q2',3,N,'The Song of Songs, chapter 5','Song of Songs 5:6–7'),
 s('But there is another part of this story I cannot escape.<br><br><span class="r">I have also been a watchman.</span>','q2',4,N),
 s('Sometimes the familiarity of striving feels safer than <span class="r">the vulnerability of being loved.</span>','q1',5,N),
 s('“You also have died to the law through the body of Christ, so that you may belong to another, <span class="r">to him who has been raised from the dead.</span>”','q2',6,N,None,'Romans 7:4'),
 s('I don’t want to waste any more days looking for myself in His eyes when I could be beholding <span class="r">the One who has never stopped loving me.</span>','q2',7,N),
 end(8,N),
]
pause=[
 cover('Let the Gospel<br><span class="r">create the question</span>',1,N),
 s('Paul seems remarkably unwilling to become <span class="r">nervous about his own Gospel.</span>','q1',2,N),
 s('He lets the Gospel create the question.<br><br><span class="r">And I am beginning to think the question itself may be part of the work.</span>','q2',3,N),
 s('That night I dreamed I was with Paul. I was asking him the question. I wanted to know how he would answer it. And he said nothing.<br><br><span class="r">But his silence did not feel empty. It felt pregnant.</span>','q3',4,N,'A dream during Week 1'),
 s('Then, in the final dream, I remember his face. <span class="r">He looked delighted.</span>','q1',5,N),
 s('Why do we imagine that grace needs law standing behind it with a stick <span class="r">in order to produce holiness?</span>','q2',6,N),
 s('The command never replaces the announcement. <span class="r">It grows out of it.</span>','q1',7,N),
 end(8,N),
]
jobs=[(f'note_joined_{i+1}',h) for i,h in enumerate(joined)]+[(f'note_pause_{i+1}',h) for i,h in enumerate(pause)]
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files'])
    pg=b.new_page(viewport={'width':1080,'height':1350})
    for name,html in jobs:
        open(f'{D}/{name}.html','w').write(html); pg.goto(f'file://{D}/{name}.html'); pg.wait_for_timeout(400)
        pg.screenshot(path=f'{D}/{name}.png')
    b.close()
from PIL import Image
for pre in ['note_joined','note_pause']:
    ims=[Image.open(f'{D}/{pre}_{i}.png').resize((360,450)) for i in range(1,9)]
    sh=Image.new('RGB',(4*370-10,2*460-10),'white')
    for i,im in enumerate(ims): sh.paste(im,((i%4)*370,(i//4)*460))
    sh.save(f'{D}/{pre}_sheet.png')
print('ok')
