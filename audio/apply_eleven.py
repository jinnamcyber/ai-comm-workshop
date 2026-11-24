#!/usr/bin/env python3
"""Download ElevenLabs clips (index -> url) for audio/<NN>/lines.json and point voice.js at them.
Usage: python3 apply_eleven.py <NN> <urls.json> [tag]   urls.json = {"0": "https://...mp3", ...}
Old edge-tts clips stay on disk (git history) so a revert is just `git checkout audio/<NN>/voice.js`."""
import hashlib, json, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
nn, urls_file = sys.argv[1], sys.argv[2]; tag = sys.argv[3] if len(sys.argv) > 3 else 'eleven'
norm = lambda s: re.sub(r'\s+', '', s)
lines = json.load(open(os.path.join(HERE, nn, 'lines.json'), encoding='utf-8'))
urls = json.load(open(urls_file))
assert len(urls) == len(lines), (len(urls), len(lines))
mp = {}
for i, ln in enumerate(lines):
    h = hashlib.sha1(f'{tag}|{ln["text"]}'.encode()).hexdigest()[:12]
    path = os.path.join(HERE, nn, h + '.mp3')
    if not os.path.exists(path):
        subprocess.run(['curl', '-s', '-f', '-o', path, urls[str(i)]], check=True)
    mp[norm(ln['text'])] = f'audio/{nn}/{h}.mp3'
vn = 'VOICE_LINES_P' if nn.endswith('p') else 'VOICE_LINES'
with open(os.path.join(HERE, nn, 'voice.js'), 'w', encoding='utf-8') as f:
    f.write(f'window.{vn}=Object.assign(window.{vn}||{{}},' + json.dumps(mp, ensure_ascii=False) + ');\n')
print(nn, len(mp), 'clips switched to', tag)
