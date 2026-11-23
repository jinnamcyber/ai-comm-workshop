#!/usr/bin/env python3
"""Render natural voice clips for every tool.
Reads audio/<NN>/lines.json  -> [{"text": "...", "voice": "zh-HK-HiuGaaiNeural", "rate": "-5%"(optional), "say": "(optional text actually sent to TTS, e.g. pronunciation fix)"}]
Writes audio/<NN>/<hash>.mp3 for each line (skips existing) and audio/<NN>/voice.js:
    window.VOICE_LINES = { "<normalised text>": "audio/NN/<hash>.mp3", ... }
Normalised text = whitespace removed. Usage: python3 render_voice.py [NN ...]"""
import asyncio, hashlib, json, os, re, sys
import edge_tts

HERE = os.path.dirname(os.path.abspath(__file__))
norm = lambda s: re.sub(r'\s+', '', s)

async def one(sem, text, voice, rate, path):
    async with sem:
        for attempt in range(4):
            try:
                await edge_tts.Communicate(text, voice, rate=rate).save(path + '.part')
                os.replace(path + '.part', path); return True
            except Exception as e:
                if attempt == 3: print('FAIL', voice, text[:30], e, flush=True); return False
                await asyncio.sleep(2 + attempt * 3)

async def main(dirs):
    sem = asyncio.Semaphore(6); jobs = []
    for d in dirs:
        lj = os.path.join(HERE, d, 'lines.json')
        if not os.path.exists(lj): continue
        lines = json.load(open(lj, encoding='utf-8')); mp = {}
        for ln in lines:
            text, voice, rate = ln['text'], ln['voice'], ln.get('rate', '+0%')
            say = ln.get('say', text)
            h = hashlib.sha1(f'{voice}|{rate}|{say}'.encode()).hexdigest()[:12]
            path = os.path.join(HERE, d, h + '.mp3')
            mp[norm(text)] = f'audio/{d}/{h}.mp3'
            if not os.path.exists(path): jobs.append(one(sem, say, voice, rate, path))
        with open(os.path.join(HERE, d, 'voice.js'), 'w', encoding='utf-8') as f:
            f.write('window.VOICE_LINES=Object.assign(window.VOICE_LINES||{},' + json.dumps(mp, ensure_ascii=False) + ');\n')
        print(d, len(lines), 'lines', flush=True)
    res = await asyncio.gather(*jobs)
    print('rendered', sum(res), 'new clips;', len(res) - sum(res), 'failed', flush=True)

dirs = sys.argv[1:] or sorted(x for x in os.listdir(HERE) if os.path.isdir(os.path.join(HERE, x)))
asyncio.run(main(dirs))
