from playwright.sync_api import sync_playwright
src=open('/home/claude/leah/build_getup_g.py').read()
exec(src[:src.index("F=\"\"\"@font-face")])
S={
2:'<p class="t2">Years ago, I was standing at a window in Mexico, watching storm clouds roll toward the city, and part of me was hoping it would rain.</p><p class="t3">We were preparing for a large outdoor Gospel event, and just days before it began, I discovered we were nearly <span class="n">$100,000</span> short. We’d announced it everywhere, made all the preparations, and now we couldn’t even pay to turn on the sound system.</p>',
3:'<p class="t2">We called everyone we knew. No one could help.</p><p class="t2">And as I watched those clouds gathering, I wondered if a storm might be <span class="c2">God’s way of saving me from the humiliation of having to cancel.</span></p>',
4:'<p class="t2">But I sensed the Lord asking me something.</p><p class="t1 c2">Was I willing to risk humiliation for His Gospel to go forth, or was I more interested in protecting myself?</p>',
5:'<p class="t3">That question brought me to a place of surrender. I didn’t know how He would provide, and I couldn’t guarantee the outcome. But I knew I belonged to Jesus.</p><p class="t3">So I stood at that window and began declaring that His Gospel would go forth, whatever it might cost me.</p><p class="t1 c2">I surrender all to Jesus.</p>',
6:'<p class="t3">That morning, Larry went to meet a businessman I had dreamed about the night before. When he arrived, the man told him he’d also had a dream.</p><p class="t2">He’d been traveling on a cloud with Jesus over the very regions where we were ministering. <span class="c2">Jesus was laughing, splashing water in his face, and inviting him into His joy.</span></p>',
7:'<p class="t2">When Larry explained why he’d come, the man recognized the invitation to participate in what Jesus was doing.</p><p class="t1 c2">He gave us the money.<br>All of it.</p>',
8:'<p class="t2">I’ve told that story many times as a testimony of God’s provision. But recently I realized something.</p><p class="t1 c2">I thought God had sent me to Mexico to preach the Gospel. He had sent me there to learn the Gospel.</p>',
9:'<p class="t2">I’ve been thinking about that alongside John <span class="n">6</span>, where Jesus asks Philip how they’re going to feed thousands of people. Philip immediately starts calculating the cost.</p><p class="t2 c2">But John tells us Jesus asked him that question because He already knew what He was going to do.</p>',
10:'<p class="t2">I’ve been hearing that question in my own life lately. There are things before me that have sent me back to examining the accounts, the resources, and everything I can reasonably accomplish.</p><p class="t2">And I keep sensing Jesus asking, <span class="c2">Leah, where are you looking?</span></p>',
11:'<p class="t3">After all these years, I’m still learning that the Christian life isn’t about my ability to produce an outcome for God. It’s about knowing Him and participating in His life.</p><p class="t2 c2">Faith doesn’t mean I know how everything will turn out. It means I know the One who is asking me to trust Him.</p><p class="t3">And today, I’m saying yes again. I surrender all to Jesus.</p>',
}
import shutil
shutil.copy(f'{D}/faith.png', f'{D}/faith_ig_1.png')
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files']); pg=b.new_page(viewport={'width':1080,'height':1350})
    jobs=[(n,gs(slide(h,n))) for n,h in S.items()]+[(12,gs(end))]
    for n,h in jobs:
        open(f'{D}/faith_ig_{n}.html','w').write(h); pg.goto(f'file://{D}/faith_ig_{n}.html'); pg.wait_for_timeout(400)
        pg.screenshot(path=f'{D}/faith_ig_{n}.png')
    b.close()
from PIL import Image
ims=[Image.open(f'{D}/faith_ig_{i}.png').resize((300,375)) for i in range(1,13)]
sh=Image.new('RGB',(6*310-10,2*385-10),'white')
for i,im in enumerate(ims): sh.paste(im,((i%6)*310,(i//6)*385))
sh.save(f'{D}/faith_ig_sheet.png'); print('ok')
