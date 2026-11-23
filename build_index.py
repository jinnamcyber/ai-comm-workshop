#!/usr/bin/env python3
"""Build index.html (the workshop gallery) from the tool list below + prompts/*.md.
Run again whenever a prompt file changes: python3 build_index.py"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))

TOOLS = [
    ("01-植物的組成", "常識", "小三", "學生操作", "學生按指示點選植物的各個組成部分、可以點選後看到植物成長過程動畫"),
    ("02-朗讀即時回饋", "中文", "小二至小三", "學生操作", "朗讀後，系統自動給予即時回饋"),
    ("03-天氣與衣物", "全科", "幼兒至小一", "教師操作", "觀察天氣，選衣物並練習表達。"),
    ("04-乘法口訣晨操", "數學", "小二至小三", "教師操作", "一個乘法口訣互動遊戲，教師每天早上運動遊戲與學生進行互動"),
    ("05-音樂聽辨", "音樂", "小一至小三", "課題活動", "老師提問題題，學生點選圖示或動畫選項"),
    ("06-分層工作紙-時態", "英文", "小五至小六", "學生操作＋列印", "英文科 - Mixed Tenses／利用AI製作分層工作紙"),
    ("07-小水滴去旅行", "幼兒", "K2至K3", "學生操作", "以AI製作動畫介紹一些較難的知識點"),
    ("08-閱讀口語對答", "中文", "小三至小四", "回家複習", "可讓學生回家進行複習，設計對答類的口語練習。"),
    ("09-葡文情境對話", "葡文", "初中 A1", "教師操作", "葡文科，主要是不同類型對話（例子也不錯）"),
    ("10-地球自轉與公轉", "常識", "小五至小六", "教師示範", "地球自轉和圍繞太陽公轉"),
]

def sections(md):
    out, cur = {}, None
    for line in md.splitlines():
        m = re.match(r'^##\s+(.*)', line)
        if m: cur = m.group(1).strip(); out[cur] = []; continue
        if cur is not None: out[cur].append(line)
    return {k: '\n'.join(v).strip() for k, v in out.items()}

def pick(sec, *keys):
    for k, v in sec.items():
        if any(x in k for x in keys): return v
    return ''

items = []
for slug, subj, grade, kind, quote in TOOLS:
    p = os.path.join(HERE, 'prompts', slug + '.md')
    sec = sections(open(p, encoding='utf-8').read()) if os.path.exists(p) else {}
    items.append(dict(slug=slug, num=slug[:2], name=slug[3:], subj=subj, grade=grade, kind=kind, quote=quote,
                      bad=pick(sec, '無效'), good=pick(sec, '有效'), fix=pick(sec, '回饋'), use=pick(sec, '課堂'),
                      ready=os.path.exists(os.path.join(HERE, slug + '.html'))))

tpl = open(os.path.join(HERE, 'index.template.html'), encoding='utf-8').read()
data = json.dumps(items, ensure_ascii=False).replace('</', '<\\/')
open(os.path.join(HERE, 'index.html'), 'w', encoding='utf-8').write(tpl.replace('/*__DATA__*/[]', data))
print('index.html built:', sum(i['ready'] for i in items), 'tools ready,', sum(bool(i['good']) for i in items), 'prompts')
