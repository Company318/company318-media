"""Night-sky cover with Chris and Leah side by side. Usage: python3 build_duo_cover.py out.png 'Eyebrow' 'Title html' 'Book' 'Authors' 'count'"""
import sys
from playwright.sync_api import sync_playwright
src=open('/home/claude/c318art/build_photo_mock.py').read()
exec(src[:src.index("A = page(")])
out,eyebrow,title,book,authors,count=sys.argv[1:7]
h = page('<div class="duo"><div style="background-image:url(chris.png);background-size:114%;background-position:50% 0%"></div>'
  '<div style="background-color:#120b0a;background-image:url(leah.png);background-size:auto 100%;background-position:50% 48px;background-repeat:no-repeat"></div></div>'
  '<div class="fade"></div><div style="position:absolute;left:0;right:0;top:0;height:150px;background:linear-gradient(180deg,#120b0a 25%,rgba(18,11,10,0))"></div>'
  f'<div class="low"><div class="eyebrow" style="margin-bottom:28px">{eyebrow}</div><div class="serif big">{title}</div>'
  f'<div class="serif small" style="margin-top:24px"><i>{book}</i><br>{authors}</div></div>', 7, count)
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files'])
    pg=b.new_page(viewport={'width':1080,'height':1350})
    open(f'{D}/duo_tmp.html','w').write(h); pg.goto(f'file://{D}/duo_tmp.html'); pg.wait_for_timeout(500)
    pg.screenshot(path=out); b.close()
print('ok')
