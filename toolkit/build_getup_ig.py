from playwright.sync_api import sync_playwright
src=open('/home/claude/leah/build_message.py').read()
exec(src[:src.index("N=9")])
N=12
def slide(inner,n):
    return ('<!doctype html><html><head><meta charset="utf-8"><style>'+CSS+'</style></head><body><div class="c">'
      f'<div class="top"><span>Leah Ramirez</span><span>{n} / {N}</span></div><div class="rule"></div>'
      f'<div class="body">{inner}</div><div class="foot"><span>@LEAHRAMIREZ247</span><span>SWIPE</span></div></div></body></html>')
S={
2:'<p class="t2">During worship on Sunday, the Lord began showing me something.</p><p class="t3">I was being asked to dress a wounded leg. As I began unwrapping the bandages, I discovered that the dressing underneath was perfectly white and clean. <span class="c2">The healing was complete. Nothing more needed to be done. No new dressings were necessary.</span></p>',
3:'<p class="t2">And I knew it was time to make an announcement.</p><p class="t1 c2">It’s time to get up.</p><p class="t2">I’ve been thinking about this in my own life, and I believe it’s a word for many of us.</p>',
4:'<p class="t3">There are seasons when healing happens in a bed. When we’ve been wounded, we need rest. We need tenderness. We need time for the Lord to restore what has been damaged. I have known those seasons, and I am deeply grateful for the kindness of Jesus in them.</p><p class="t2">But here’s something I’ve been considering. <span class="c2">Some recovery can only happen when we begin walking again.</span></p>',
5:'<p class="t3">There are muscles that won’t regain their strength while we’re lying down. There is confidence that returns only as we begin putting weight on what has been healed. We have to learn to move again, sometimes with trembling legs, discovering that what once couldn’t bear our weight is becoming strong.</p><p class="t2"><span class="c2">And I wonder how many of us have stayed in a season of recovery long after the Lord began calling us to walk.</span></p><p class="t2">I know I have.</p>',
6:'<p class="t3">I’ve found myself looking back at earlier seasons of my life, remembering the faith I had, the risks I took, the things I believed God for. And somewhere along the way, I began calling some of my hesitation wisdom. I learned how to calculate the cost, consider the obstacles, and find enough reasons to remain where I was.</p><p class="t3">I’ve even discovered that when I don’t want to step out, I know exactly which people to ask for advice. <span class="c2">The ones who will tell me not to!</span></p><p class="t3">Hahahaha. I’m telling on myself here.</p>',
7:'<p class="t2 c2">But I have been hearing the Lord inviting me to believe Him again.</p><p class="t3">Not because I need to manufacture more faith or prove something to Him. But because the same Jesus who met me in my darkest moments is still my Savior today.</p><p class="t3">We are quick to proclaim that Jesus can save someone out of addiction, deliver someone from darkness, or completely transform a life. And I believe every word of it!</p>',
8:'<p class="t2">But what about the things we’ve carried for twenty or thirty years? What about the places where disappointment has shaped our expectations? What about the dreams we’ve quietly stopped believing could ever come to pass?</p><p class="t1 c2">Today is the day of salvation for us, too.</p>',
9:'<p class="t3">We were never meant to come into the Father’s house through Christ and then spend the rest of our lives figuring out how to heal and transform ourselves.</p><p class="t3">The Gospel is still inviting us to Jesus. Today. For our healing, our deliverance, and our complete salvation.</p><p class="t3">I keep thinking about Jeremiah <span class="n">12:5</span>, where the Lord asks Jeremiah how he will compete with horses if running with men has wearied him.</p><p class="t2 c2">Oh, I want to run with the horses!</p>',
10:'<p class="t3">I believe the Lord is preparing us for more than simply surviving what we’ve been through. There are things He’s deposited in our hearts that haven’t expired. There are people He intends to reach, places He’s calling us to go, and a life of participation in Christ that is far greater than anything we could accomplish in our own strength.</p><p class="t2 c2">And I don’t want to spend the next twenty years rehearsing the reasons I stopped believing.</p>',
11:'<p class="t2">The bandages have done their work. The Lord has been faithful in our recovery.</p><p class="t2">I believe He’s inviting us to get up.</p><p class="t2 c2">And not only will we walk again, I believe we’re going to run with the horses.</p><p class="t3">Our Gospel is for full recovery and full participation in the life of Jesus Christ.</p>',
}
end=('<!doctype html><html><head><meta charset="utf-8"><style>'+CSS+'</style></head><body><div class="c">'
 f'<div class="top"><span>Leah Ramirez</span><span>12 / {N}</span></div><div class="rule"></div>'
 '<div class="body" style="text-align:center"><p class="ref" style="color:#9a6a3c">Sunday’s message</p>'
 '<p class="t1" style="margin-top:30px">I Surrender All to Jesus</p><p class="t2" style="font-style:italic;color:#4b4a3c">Today Is the Day of Salvation</p>'
 '<p class="ref" style="margin-top:60px">Full message on YouTube<br>search Company 318</p>'
 '<p class="ref" style="margin-top:40px">The Gathering · Colorado Springs</p></div>'
 '<div class="foot" style="justify-content:center"><span>@LEAHRAMIREZ247</span></div></div></body></html>')
import shutil
shutil.copy(f'{D}/getup_A.png', f'{D}/getup_ig_1.png')
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files']); pg=b.new_page(viewport={'width':1080,'height':1350})
    jobs=[(n,slide(h,n)) for n,h in S.items()]+[(12,end)]
    for n,h in jobs:
        open(f'{D}/getup_ig_{n}.html','w').write(h); pg.goto(f'file://{D}/getup_ig_{n}.html'); pg.wait_for_timeout(450)
        pg.screenshot(path=f'{D}/getup_ig_{n}.png')
    b.close()
from PIL import Image
ims=[Image.open(f'{D}/getup_ig_{i}.png').resize((300,375)) for i in range(1,13)]
sh=Image.new('RGB',(6*310-10,2*385-10),'white')
for i,im in enumerate(ims): sh.paste(im,((i%6)*310,(i//6)*385))
sh.save(f'{D}/getup_ig_sheet.png'); print('ok')
