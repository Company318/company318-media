"""Week 8 note from Leah (Romans 8), Behold School style. Leah's words verbatim; Scripture ESV."""
from playwright.sync_api import sync_playwright
src = open('/home/claude/bs/build_notes.py').read()
exec(src[:src.index("N=8")])
N=8
slides=[
 page('<div class="body center"><div class="eyebrow">A note from Leah · Week 8</div>'+ORN+
      '<div class="serif title">The Gospel Is<br><span class="r">Ultimate Reality</span></div>'+ORN+
      '<div class="sub">From <i>The Gospel From Which We Live</i>,<br>Leah’s Romans 5–8 class at Behold School</div></div>', f'1 / {N}'),
 s('Their assessment wasn’t unreasonable. There really were thousands of hungry people, and their resources really were insufficient.<br><br><span class="r">But John tells us something extraordinary. Jesus already knew what He intended to do.</span>','q3',2,N,'Jesus feeds the multitude','John 6:5–11'),
 s('Our assessment of our resources may be entirely accurate and still be <span class="r">an incomplete assessment of reality.</span>','q1',3,N),
 s('“For God has done what the law, weakened by the flesh, could not do.”<br><br><span class="r">We were never intended to become the source of what only God can accomplish.</span>','q2',4,N,None,'Romans 8:3'),
 s('Everything about their natural circumstances testified to their inability, yet Abraham became persuaded of the faithfulness of the One who had promised.<br><br><span class="r">His confidence rested upon the God who gives life to the dead.</span>','q3',5,N,'Abraham and Sarah','Romans 4:17–21'),
 s('He had discovered that the end of his resources was <span class="r">not the end of God’s life.</span>','q1',6,N,'Paul, who boasted in his weaknesses','2 Corinthians 12:9'),
 s('We aren’t celebrating our inability. <span class="r">We are celebrating His sufficiency.</span>','q1',7,N),
 end(8,N),
]
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files'])
    pg=b.new_page(viewport={'width':1080,'height':1350})
    for i,html in enumerate(slides,1):
        open(f'{D}/note8_{i}.html','w').write(html); pg.goto(f'file://{D}/note8_{i}.html'); pg.wait_for_timeout(400)
        pg.screenshot(path=f'{D}/note8_{i}.png')
    b.close()
from PIL import Image
ims=[Image.open(f'{D}/note8_{i}.png').resize((360,450)) for i in range(1,9)]
sh=Image.new('RGB',(4*370-10,2*460-10),'white')
for i,im in enumerate(ims): sh.paste(im,((i%4)*370,(i//4)*460))
sh.save(f'{D}/note8_sheet.png'); print('ok')
