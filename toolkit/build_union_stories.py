import re
src=open('build_stories.py').read()
F=re.search(r'F="""(.*?)"""',src,re.S).group(0); exec(F)
D='/home/claude/leah'
BG="background:radial-gradient(ellipse 90% 70% at 50% 40%,#2c3d30 0%,#1f2c23 70%,#18221b 100%);color:#f2ead9"
def top(photo,pos,eyebrow,title,sub,foot):
    return f"""<div style="width:1080px;height:1920px;position:relative;overflow:hidden;{BG}">
<div style="position:absolute;left:0;right:0;top:0;height:1100px;background:#111 url({photo}) {pos}/cover no-repeat;filter:grayscale(1)"></div>
<div style="position:absolute;left:0;right:0;top:760px;height:360px;background:linear-gradient(180deg,rgba(31,44,35,0),#1f2c23 88%)"></div>
<div style="position:absolute;left:0;right:0;top:1210px;text-align:center;font-family:Bask">
 <div style="font-family:InterM;font-size:22px;letter-spacing:0.34em;color:#c49a5a">{eyebrow}</div>
 <div style="margin-top:52px;font-size:112px;line-height:1.04">{title}</div>
 <div style="margin:44px auto 0;width:820px;font-size:42px;line-height:1.35;font-style:italic;color:rgba(242,234,217,0.82)">{sub}</div>
 <div style="margin-top:64px;font-family:InterM;font-size:22px;letter-spacing:0.28em;color:rgba(242,234,217,0.6)">{foot}</div>
</div></div>"""
S={'story_union_chris':top('chris_bw.png','50% 25%','THE GATHERING · SUNDAY','The Scandal<br><span style="color:#c49a5a">of Union</span>','The vessel was never intended<br>to be the source of the light.','CHRIS BERGLUND · NEW POST'),
 'story_union_leah':top('leah_bw.png','50% 22%','THE GATHERING · SUNDAY','But we can<br><span style="color:#c49a5a">agree with Him.</span>','Our faith does not create His faithfulness.<br>It lays hold of the Faithful One.','LEAH RAMIREZ · NEW POST')}
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files']); pg=b.new_page(viewport={'width':1080,'height':1920})
    for n,h in S.items():
        open(f'{D}/{n}.html','w').write('<!doctype html><html><head><meta charset="utf-8">'+F+'</head><body>'+h+'</body></html>')
        pg.goto(f'file://{D}/{n}.html'); pg.wait_for_timeout(500); pg.screenshot(path=f'{D}/{n}.png')
    b.close()
from PIL import Image
c=Image.open(f'{D}/canwe.png').convert('RGB'); print(c.size)
col=c.getpixel((5,c.size[1]//2)); st=Image.new('RGB',(1080,1920),col); st.paste(c,(0,(1920-c.size[1])//2)); st.save(f'{D}/story_canwe.png')
ims=[Image.open(f'{D}/{n}.png').resize((360,640)) for n in ['story_union_chris','story_union_leah','story_canwe']]
sh=Image.new('RGB',(1100,640),'white');[sh.paste(im,(i*370,0)) for i,im in enumerate(ims)]; sh.save(f'{D}/stories_union_sheet.png')
