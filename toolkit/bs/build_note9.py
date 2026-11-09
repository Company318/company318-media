"""Week 9 note from Leah: Learning to Be Loved. Words verbatim; Scripture ESV. Photo cover."""
from playwright.sync_api import sync_playwright
src=open('/home/claude/bs/build_parch_covers.py').read()
exec(src[:src.index("jobs={")])
N=8
slides=[
 cover(LE_SOLO,'A note from Leah · Week 9','Learning to <span class="r">Be Loved</span>','From <i>The Gospel From Which We Live</i>, Leah’s Romans 5–8 class at Behold School',f'1 / {N}'),
 s('I began confusing the evidence of extraordinary religious commitment with <span class="r">the evidence of extraordinary intimacy with God.</span>','q2',2,N),
 s('There was no performance left in me. But I could offer Him my broken heart and my broken body.<br><br><span class="r">And what I discovered, day after day, was that He received me.</span>','q3',3,N,'Two years of recovery from a back injury'),
 s('I couldn’t see the value of what He had been offering me <span class="r">until I saw the way He received my broken body.</span>','q2',4,N),
 s('“You have received the Spirit of adoption as sons, by whom we cry, <span class="r">‘Abba! Father!’</span>”','q1',5,N,None,'Romans 8:15'),
 s('I had spent years defending a Gospel that required everything of me, without fully understanding <span class="r">the Gospel that announced everything God had already accomplished in Christ.</span>','q3',6,N),
 s('I understand that older brother more than I would like to admit.<br><br>But his father answered him: <span class="r">“Son, you are always with me, and all that is mine is yours.”</span>','q2',7,N,'Outside the celebration','Luke 15:31'),
 end(8,N),
]
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files'])
    pg=b.new_page(viewport={'width':1080,'height':1350})
    for i,h in enumerate(slides,1):
        open(f'{D}/note9_{i}.html','w').write(h); pg.goto(f'file://{D}/note9_{i}.html'); pg.wait_for_timeout(450)
        pg.screenshot(path=f'{D}/note9_{i}.png')
    b.close()
from PIL import Image
ims=[Image.open(f'{D}/note9_{i}.png').resize((360,450)) for i in range(1,9)]
sh=Image.new('RGB',(4*370-10,2*460-10),'white')
for i,im in enumerate(ims): sh.paste(im,((i%4)*370,(i//4)*460))
sh.save(f'{D}/note9_sheet.png'); print('ok')
