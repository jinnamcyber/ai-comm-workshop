#!/usr/bin/env python3
"""raw/*.png -> art/<name>.jpg (max 1600px wide, q82). Cutouts keep their white background (use mix-blend-mode:multiply on light cards)."""
import os
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
for f in sorted(os.listdir(os.path.join(HERE, 'raw'))):
    if not f.endswith('.png'): continue
    out = os.path.join(HERE, f[:-4] + '.jpg')
    if os.path.exists(out) and os.path.getmtime(out) > os.path.getmtime(os.path.join(HERE, 'raw', f)): continue
    im = Image.open(os.path.join(HERE, 'raw', f)).convert('RGB')
    im.thumbnail((1600, 1600)); im.save(out, quality=82, optimize=True, progressive=True)
    print(f[:-4], im.size, os.path.getsize(out) // 1024, 'KB')
