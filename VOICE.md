# 改用真人聲（預錄 mp3）— 所有教具共用做法

老師唔想要電腦本身嘅 speechSynthesis 聲線，要自然人聲。我哋用 Microsoft 神經語音（edge-tts）**預先錄好每一句**。

## 你要做嘅三件事

### 1. 列出所有會讀出嘅句子 → `audio/<NN>/lines.json`
（NN = 你教具編號，例如 `01`。資料夾要自己開。）
```json
[
  {"text": "請點選：葉", "voice": "zh-HK-HiuMaanNeural"},
  {"text": "七八五十六", "voice": "zh-HK-WanLungNeural", "rate": "-5%"},
  {"text": "...", "voice": "...", "say": "（可選）實際送去 TTS 嘅字，用嚟修正讀音"}
]
```
- `text` 必須**同你程式傳入 speak 嘅字串完全一樣**（比對時會刪走所有空白，其他要一模一樣，包括標點）。
- **所有**會讀出嘅字串都要列晒，包括回饋句、提示句、題目、旁白、動態組合。動態組合如果數量有限（例如 2–9 乘法表、葡文替換詞所有組合），就全部列舉出嚟。如果組合太多（例如自由組合嘅句子），就改程式：拆做幾段固定片段，用 `speakSeq([...])` 順序播放，再列出每段。
- 最穩陣嘅做法：寫一個 node 腳本 import / 複製你嘅題目資料，自動產生 lines.json，唔好手抄。
- 唔好列學生自己輸入嘅內容（嗰啲冇得預錄，照用 fallback）。

### 2. 改 speak 函數：有預錄就播 mp3，冇就 fallback 舊 TTS
在 `</body>` 前、你主程式之前加：
```html
<script src="audio/NN/voice.js"></script>
```
（檔案由我哋嘅錄音腳本產生；開檔時未有都唔可以報錯——`window.VOICE_LINES` 可能係 undefined。）

用以下 helper 取代你原本直接用 speechSynthesis 嘅地方（保留你原有嘅 fallback 邏輯）：
```js
const VOICE = (() => {
  let cur = null;
  const norm = s => String(s).replace(/\s+/g, '');
  const lookup = t => (window.VOICE_LINES || {})[norm(t)];
  function stop() { if (cur) { cur.onended = null; cur.pause(); cur = null; } try { speechSynthesis.cancel(); } catch (_) {} }
  // speak(text, {rate, onend}) -> 播預錄；冇就用舊 TTS（ttsFallback 係你原本嘅函數）
  function speak(text, opt = {}) {
    stop();
    const src = lookup(text);
    if (src) {
      const a = new Audio(src); cur = a;
      a.playbackRate = opt.rate || 1; a.preservesPitch = true;
      a.onended = () => { if (cur === a) cur = null; opt.onend && opt.onend(); };
      a.onerror = () => { cur = null; ttsFallback(text, opt); };
      a.play().catch(() => { cur = null; ttsFallback(text, opt); });
      return;
    }
    ttsFallback(text, opt);
  }
  function speakSeq(parts, opt = {}) { // 順序播放多段
    let i = 0; const next = () => { if (i >= parts.length) return opt.onend && opt.onend(); speak(parts[i++], { rate: opt.rate, onend: next }); }; next();
  }
  return { speak, speakSeq, stop, has: t => !!lookup(t) };
})();
```
- 你原本依賴 `utterance.onend` 嘅地方（逐句高亮、嘴巴郁、自動播放下一幕）要改用 `opt.onend`，確保 mp3 同 TTS 兩條路都正常觸發。
- 慢速掣：用 `opt.rate`（例如 0.75），mp3 用 playbackRate。
- 「冇聲線」嘅警告／提示：而家有預錄就唔應該再顯示（只在冇 mp3 又冇聲線時先顯示）。

### 3. 唔好自己跑錄音
列好 lines.json 同改好代碼就停，回報：lines.json 有幾多句、用咗咩聲線、有冇用 speakSeq 拆句。**錄音由統籌負責**（`python3 audio/render_voice.py NN`），之後會叫你喺瀏覽器測試。

## ⚠️ 粵語一定要用粵語字稿（老師要求）
所有 zh-HK 嘅句子，送去錄音嘅字（`say` 欄，冇 say 就係 text）**必須係自然口語粵語字稿**，唔可以係書面語。例如：
- 書面語「葉通常是綠色的，長在莖上。」→ 粵語字稿「葉通常係綠色嘅，生喺莖上面。」
- 「請點選植物的葉」→「你撳一撳植物嘅葉吖。」
- 「答對了！真棒！」→「答啱啦！好叻呀！」
- 「好熱呀！我變得好輕，飛上天啦！」✓（已經係口語）
做法：最好**連畫面顯示嘅字都改成粵語口語**（text 同 say 一樣），咁老師同學生睇到聽到一致；如果畫面一定要保留書面語（例如朗讀練習嘅課文、閱讀文章本身），就 text 保留原文、say 都保留原文——**課文／朗讀題目本身係照字讀，唔改**；其他所有提示、回饋、問題、旁白、講解都要用粵語字稿。
語氣要似老師同小朋友傾偈：用「吖、喎、啦、喇、呀、嘞」等語氣詞要自然，唔好過多。

## 聲線分配
| 教具 | 聲線 |
|---|---|
| 01 植物 | zh-HK-HiuMaanNeural |
| 02 朗讀 | zh-HK-HiuMaanNeural（示範要清晰標準） |
| 03 天氣 | zh-HK-HiuGaaiNeural |
| 04 乘法 | zh-HK-WanLungNeural |
| 05 音樂 | zh-HK-HiuGaaiNeural |
| 06 英文 | en-GB-SoniaNeural（介面中文提示如有讀出就用 zh-HK-HiuMaanNeural） |
| 07 水滴 | zh-HK-HiuGaaiNeural（小水滴語氣，可用 rate "-5%"） |
| 08 閱讀 | 朗讀全文 zh-HK-HiuMaanNeural；貓頭鷹老師 zh-HK-WanLungNeural |
| 09 葡文 | 女角 pt-PT-RaquelNeural；男角 pt-PT-DuarteNeural（按角色分） |

廣東話神經語音讀書面語同口語字（喺、嘅、咗）都得。如果某啲字讀音容易錯（例如「著衫」嘅「著」可能讀錯），就用 `say` 欄寫一個讀音正確嘅替代寫法（例如「着」），或者改句子避開；畫面顯示嘅字唔使改。
