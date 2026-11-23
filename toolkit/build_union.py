"""Nov 22 Sunday message 'The Scandal of Union': Chris carousel (C318 IG, Gathering FB) and Leah carousel (all four). Gathering palette."""
from playwright.sync_api import sync_playwright
src=open('/home/claude/leah/build_getup_g.py').read()
exec(src[:src.index("F=\"\"\"@font-face")])
F="""@font-face{font-family:Bask;src:url('file:///usr/share/fonts/truetype/baskerville/GFSBaskerville.otf');}
@font-face{font-family:InterM;src:url('file:///usr/share/fonts/opentype/inter/Inter-Medium.otf');}html,body{margin:0;padding:0;}"""
def cover(photo, pos, eyebrow, title, sub, name, line2, gray=True):
    filt='filter:grayscale(1) contrast(1.05);' if gray else ''
    return ('<!doctype html><html><head><meta charset="utf-8"><style>'+F+'</style></head><body>'
    """<div style="width:1080px;height:1350px;position:relative;overflow:hidden;background:radial-gradient(ellipse 90% 70% at 30% 35%,#2c3d30 0%,#1f2c23 70%,#18221b 100%);color:#f2ead9">"""
    f'<div style="position:absolute;right:0;top:0;width:540px;height:1350px;background:#111 url({photo}) {pos}/cover no-repeat;{filt}"></div>'
    '<div style="position:absolute;left:480px;top:0;width:140px;height:1350px;background:linear-gradient(90deg,#1f2c23 15%,rgba(31,44,35,0))"></div>'
    f'<div style="position:absolute;left:90px;top:120px;font-family:InterM;font-size:19px;letter-spacing:0.3em;color:#c49a5a">{eyebrow}</div>'
    '<div style="position:absolute;left:90px;top:175px;width:70px;height:1px;background:#c49a5a"></div>'
    f'<div style="position:absolute;left:90px;top:330px;width:420px;font-family:Bask;"><div style="font-size:86px;line-height:1.08">{title}</div>'
    f'<div style="margin-top:50px;font-size:36px;line-height:1.35;font-style:italic;color:rgba(242,234,217,0.82)">{sub}</div></div>'
    f'<div style="position:absolute;left:90px;bottom:110px;width:440px;font-family:Bask;"><div style="font-size:44px">{name}</div>'
    f'<div style="margin-top:14px;font-family:InterM;font-size:17px;letter-spacing:0.24em;color:#c49a5a;line-height:1.7">{line2}<br><span style="color:rgba(242,234,217,0.55)">COLORADO SPRINGS</span></div></div></div></body></html>')
def gsN(h, n, total, who):
    return gs(h).replace(f'{n} / 12', f'{n} / {total}').replace('LEAH RAMIREZ</span></div>', f'{who}</span></div>')
def endslide(n,total,who):
    h=('<!doctype html><html><head><meta charset="utf-8"><style>'+CSS+'</style></head><body><div class="c">'
     f'<div class="top"><span>Leah Ramirez</span><span>{n} / {total}</span></div><div class="rule"></div>'
     '<div class="body" style="text-align:center"><p class="ref" style="color:#9a6a3c">Sunday’s message</p>'
     '<p class="t1" style="margin-top:30px">The Scandal of Union</p><p class="t2" style="font-style:italic;color:#4b4a3c">When Christ Lives Through Us</p>'
     '<p class="ref" style="margin-top:60px">Read the full article · Company 318 on Substack<br>Watch the message · search Company 318 on YouTube</p>'
     '<p class="ref" style="margin-top:40px">The Gathering · Colorado Springs</p></div>'
     '<div class="foot"><span>@LEAHRAMIREZ247</span><span>SWIPE</span></div></div></body></html>')
    return gsN(h,n,total,who)
def S(inner,n,total,who): return gsN(slide(inner,n),n,total,who)
CH=[
 ('cover', cover('chris_bw.png','46% 30%','THE GATHERING · SUNDAY','The Scandal<br><span style="color:#c49a5a">of Union</span>','When Christ lives<br>through us.','Chris Berglund','THE SCANDAL OF UNION')),
 '<p class="t1">Union with Christ does not eliminate our participation.</p><p class="t1 c2">It eliminates our independence.</p>',
 '<p class="t3">Hebrews <span class="n">11</span> is often called the Hall of Faith. Yet some of the people named there, like Samson, Gideon and Jephthah, are among the most complicated characters in the Old Testament.</p><p class="t2">Perhaps we have been reading this chapter with our attention on the wrong person.</p><p class="t2 c2">God remains faithful, even as deeply flawed people learn to trust what He has spoken.</p>',
 '<p class="t1">Faith is not our ability to become sufficient for God’s purposes.</p><p class="t1 c2">It is our response to the One who is faithful.</p>',
 '<p class="t3">Gideon gathered <span class="n">32,000</span> men. God reduced them to <span class="n">300</span>, so Israel would not mistake the victory for their own strength.</p><p class="t2">They surrounded the camp with trumpets, empty clay jars and torches. At the signal, <span class="c2">they broke the jars and the light was revealed.</span></p><p class="ref">Judges 7</p>',
 '<p class="t2">“But we have this treasure in jars of clay, to show that the surpassing power belongs to God and not to us.”</p><p class="ref">2 Corinthians 4:7</p><p class="t1 c2" style="margin-top:44px">The vessel was never intended to be the source of the light.</p>',
 '<p class="t2">We no longer pray to convince a reluctant God to become involved.</p><p class="t2 c2">We pray because we have been brought into communion with the Father through His Son.</p>',
 '<p class="t1">What God has accomplished in Jesus comes first.</p><p class="t2 c2">Our participation is a response to His grace, not an attempt to produce it.</p>',
]
LE=[
 ('cover', cover('leah_bw.png','50% 30%','THE GATHERING · SUNDAY','But we can <span style="color:#c49a5a">agree with Him.</span>','We cannot change another person’s heart.','Leah Ramirez','THE SCANDAL OF UNION',gray=False)),
 '<p class="t2">Today many of us will sit around a table with people we love, and some of them are people we have been praying for for years.</p><p class="t3">I know how little power I have to change another person’s heart. I can’t manufacture a response to the Gospel. I can’t produce the life of Christ in someone through more determination.</p><p class="t1 c2">But I can agree with Him.</p>',
 '<p class="t3">On Sunday I found myself thinking about the difference between faithfully maintaining something and actually participating in the faith of Christ concerning it. Both matter.</p><p class="t2">We can keep praying for our families and keep showing up. <span class="c2">And He keeps inviting us to expect Him to do what He has placed on our hearts.</span></p>',
 '<p class="t2">The things God deposits in us tend to bring us face to face with our weakness. And the temptation is to shrink back into something we know we can manage.</p><p class="t3">Paul learned to boast in his weaknesses, because that is where the power of Christ rested on him. <span class="c2">For Paul, weakness became the place where he discovered the sufficiency of Christ.</span></p><p class="ref">2 Corinthians 12:9</p>',
 '<p class="t2">So today I’m coming to the table with no pressure to make anything happen, only the confidence that <span class="c2">Christ lives in me and wants to make Himself known.</span></p>',
 '<p class="t1">Our faith does not create His faithfulness.</p><p class="t1 c2">It lays hold of the Faithful One.</p>',
]
def build(prefix, items, who):
    total=len(items)+1
    pages=[]
    for i,it in enumerate(items,1):
        pages.append(it[1] if isinstance(it,tuple) else S(it,i,total,who))
    pages.append(endslide(total,total,who))
    with sync_playwright() as p:
        b=p.chromium.launch(args=['--allow-file-access-from-files']); pg=b.new_page(viewport={'width':1080,'height':1350})
        for i,h in enumerate(pages,1):
            open(f'{D}/{prefix}_{i}.html','w').write(h); pg.goto(f'file://{D}/{prefix}_{i}.html'); pg.wait_for_timeout(450)
            pg.screenshot(path=f'{D}/{prefix}_{i}.png')
        b.close()
    from PIL import Image
    ims=[Image.open(f'{D}/{prefix}_{i}.png').resize((300,375)) for i in range(1,total+1)]
    cols=5; rows=(total+cols-1)//cols
    sh=Image.new('RGB',(cols*310-10,rows*385-10),'white')
    for i,im in enumerate(ims): sh.paste(im,((i%cols)*310,(i//cols)*385))
    sh.save(f'{D}/{prefix}_sheet.png')
build('union_chris', CH, 'CHRIS BERGLUND')
build('union_leah', LE, 'LEAH RAMIREZ')
print('ok')
