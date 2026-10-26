from playwright.sync_api import sync_playwright
D = '/home/claude/c318art'
src = open(f'{D}/build_slides.py').read()
exec(src[:src.index("TAG = ")])
CSS = CSS + """
.book{margin:0 0 34px;}
.bt{font-family:'GFS Baskerville',serif;font-size:66px;line-height:1.1;color:#f4ecde;}
.ba{margin-top:12px;font-family:InterM;font-size:19px;letter-spacing:0.24em;text-transform:uppercase;color:rgba(214,176,120,0.85);}
"""
html = page('<div class="body center"><div class="eyebrow" style="margin-bottom:56px">Now being written</div>'
  '<div class="book"><div class="bt">Behold</div><div class="ba">Chris Berglund &amp; Leah Ramirez</div></div>'
  '<div class="book"><div class="bt">Apostolic Architecture</div><div class="ba">Leah Ramirez &amp; Chris Berglund</div></div>'
  '<div class="book"><div class="bt">Romans 5–8</div><div class="ba">Leah Ramirez</div></div>'
  '<div class="rule" style="margin:48px auto"></div>'
  '<div class="serif small">Be the first to know when they release.</div>'
  '<div class="eyebrow" style="margin-top:40px;color:rgba(244,236,222,0.7)">company318.substack.com</div></div>',
  61, None, None, foot='center')
with sync_playwright() as p:
    b = p.chromium.launch(args=['--allow-file-access-from-files'])
    pg = b.new_page(viewport={'width':1080,'height':1350})
    open(f'{D}/books.html','w').write(html)
    pg.goto(f'file://{D}/books.html'); pg.wait_for_timeout(500)
    pg.screenshot(path=f'{D}/out/c318_books_waitlist.png')
    b.close()
