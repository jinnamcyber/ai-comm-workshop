#!/usr/bin/env python3
"""prompts/*.md -> prompts.js (window.TOOL_PROMPTS = {slug: {good, bad}}) for the 複製 Prompt button."""
import os, re, json
HERE = os.path.dirname(os.path.abspath(__file__))
out = {}
for f in sorted(os.listdir(os.path.join(HERE, 'prompts'))):
    if not f.endswith('.md'): continue
    t = open(os.path.join(HERE, 'prompts', f), encoding='utf-8').read()
    def sec(mark):
        m = re.search(r'^## ' + mark + r'[^\n]*\n(.*?)(?=^## |\Z)', t, re.S | re.M)
        return m.group(1).strip() if m else ''
    out[f[:-3]] = {'good': sec('✅'), 'bad': sec('❌'), 'title': t.splitlines()[0].lstrip('# ').strip()}
open(os.path.join(HERE, 'prompts.js'), 'w', encoding='utf-8').write('window.TOOL_PROMPTS=' + json.dumps(out, ensure_ascii=False) + ';\n')
print(len(out), 'prompts')
