# Company 318 social media: handoff for a new Claude session

Last updated: October 26, 2026. Read this first, together with the saved skills
`company318-weekly-posts` and `leah-ramirez-ministry-brand`.

## Start-up checklist for Claude

1. Connect this repo: add_repo Company318/company318-media with access "push", clone it to
   /home/claude/company318-media.
2. Run `sh /home/claude/company318-media/toolkit/setup.sh`. That step installs the fonts (GFS Baskerville, Inter)
   and copies the slide templates to /home/claude/c318art, /home/claude/bs and /home/claude/cover.
3. Read the live schedule from Metricool (getScheduledPosts) for both brands: 7575484 (Company 318 / The Gathering)
   and 7673336 (Leah Ramirez). Metricool is the source of truth for what is scheduled.
4. Only schedule what Leah approves. Draft, show, wait for "approved", then schedule.

## Slide templates

| Folder | Look | Start from |
| --- | --- | --- |
| c318art | Company 318 night sky (plum, ivory, gold, C318 mark) | `build_slides.py` defines CSS, stars and `page()`. Examples: `build_aa7.py` (book excerpt carousel plus quote cards), `build_post7.py` (teaching carousel), `build_books.py` (single slide) |
| bs | Behold School parchment (navy, rust, gold rules, crest) | `build_bs_post8.py` defines `page()`. Examples: `build_notes.py` (Leah's class notes), `build_behold1.py` (Behold book; the band reads BEHOLD / CHRIS BERGLUND & LEAH RAMIREZ) |
| cover | Leah's Facebook cover, 1640x924 | `build.py` (option B was chosen) |
| logo | Company 318 profile images | |

Slides are 1080x1350. The scripts reuse each other with `exec(src[:src.index("...")])`, so keep them together.
Always look at a contact sheet before showing Leah. Show carousels on their own sheet, 4 across, so it is clear
where a carousel ends.

To publish images, copy them to `posts/YYYY-MM-DD-slug/`, commit as Claude <noreply@anthropic.com>, push, and pass
`https://raw.githubusercontent.com/Company318/company318-media/main/<path>` to Metricool as media. The workspace
cannot fetch raw.githubusercontent.com itself, which is normal; Metricool can.

## Weekly rhythm (7:00 pm unless noted, America/Denver)

- Monday: book excerpt slot. Alternate Apostolic Architecture and Behold.
- Thursday: Romans 5–8 slot (Leah's class notes, "A Note from Leah").
- Reels from Sunday's message: about 5 a week (2 of Leah's at 12:00 pm, 3 of Chris's), placed around the fixed
  slots so no account gets two posts at once.
- Saturday 10:00 am: community or Gathering photo post when there is one.

## Scheduled as of October 26

- Oct 27: Chris Reel (7:00 pm); book waitlist announcement on all four accounts (4:30 pm, after Leah's Substack
  email at 3:45 pm).
- Oct 28: Leah's "Dust" Reel (12:00 pm); "Where are you located?" carousel (7:00 pm).
- Oct 29: Chris Reel. Oct 30: Leah Reel (12:00 pm). Oct 31: prayer photo (10:00 am). Nov 1: Chris Reel.
- Nov 2: Apostolic Architecture Chapter 7 carousel ("Grace That Forms Us"), all four accounts.
- Nov 5: Romans note "Let the Gospel create the question", all four accounts.
- Nov 9: Behold Chapter One carousel ("Revelation Comes First"), all four accounts, with Chris as collaborator on Company 318 Instagram.
- Nov 12: Romans note "Joined to Another", all four accounts.
- Nov 16, 23, 30, Dec 7: Apostolic Architecture quote cards on Company 318 Instagram and The Gathering Facebook.
- Open: Reels for the week of Nov 2 onward (from the Nov 1 Sunday message), Thursdays from Nov 19.

## Content library: available, used and on hold

- OpusClip project P3092819oK37 (Leah, "The Love That Descends", 39 clips) and P3102619h9Vx (Chris, "Kings and
  Priests: One Life, Two Expressions", 37 clips). Five clips have been used; the rest can fill gaps.
- Behold Chapter One: the John 8 section (Jesus writing in the dust, "Neither do I condemn you", and the beholding
  practice) is unused. Good to post a few weeks after Leah's Oct 28 "Dust" Reel.
- Behold Chapter One: Bryan Olsen's insight is on hold until he gives permission to be named.
- Apostolic Architecture Chapter 7: the story of Chris's desk and his son, and the story of Larry embracing
  students in Virginia, need Chris's and Larry's OK before use.
- Unused Behold School testimonies are listed in the company318-weekly-posts skill.

## Rules learned while making excerpts

- Excerpts are word for word. Context labels (small caps above a quote) are Claude's words and help when a passage
  needs setting, for example "Adam and Eve in the garden".
- Scripture on slides is always ESV, even where the manuscript quotes another translation.
- Stories about Leah's children or family conflict stay off social media. Stories about other named people need
  their permission.
- Book author order: Behold is Chris Berglund and Leah Ramirez (Chris first). Apostolic Architecture is Leah
  Ramirez and Chris Berglund. Romans 5–8 is Leah Ramirez.
- Every book post says the book is being written and points to company318.substack.com to hear when it releases.
  Never imply it can be bought.

## Open items

- A stale OpusClip publish request (The Gathering Facebook, "dust" clip) must never be approved.
- Chris accepts each Instagram collaborator invite himself.
- Voice enhancement is turned on by Leah in the OpusClip editor; Claude cannot do it through the API.
