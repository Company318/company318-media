#!/bin/sh
# Run once in a new Claude session: installs the fonts and puts the slide templates where the scripts expect them.
set -e
HERE=$(cd "$(dirname "$0")" && pwd)
mkdir -p /usr/share/fonts/truetype/baskerville /usr/share/fonts/opentype/inter
cp "$HERE/fonts/GFSBaskerville.otf" /usr/share/fonts/truetype/baskerville/
cp "$HERE/fonts/Inter-Medium.otf" "$HERE/fonts/Inter-Regular.otf" /usr/share/fonts/opentype/inter/
fc-cache -f >/dev/null 2>&1 || true
for d in c318art bs cover logo; do mkdir -p /home/claude/$d; cp -n "$HERE/$d/"* /home/claude/$d/ 2>/dev/null || true; done
mkdir -p /home/claude/c318art/out
pip install --break-system-packages -q pillow >/dev/null 2>&1 || true
echo "Toolkit ready: /home/claude/c318art (Company 318 night sky), /home/claude/bs (Behold parchment), /home/claude/cover (Leah's Facebook cover)."
