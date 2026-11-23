# 示範教具 — 共用規格（所有教具必須遵守）

背景：明天（2026-11-24）有一個 90 分鐘教師工作坊，主題係「同 AI 溝通：點樣有效、點樣無效」，主要工具係 Google Gemini（Canvas）。
學校係澳門一間中小幼一條龍學校（中葡職業技術學校）。課前問卷入面，老師寫咗佢哋想做嘅教具；每個教具都係按其中一位老師嘅諗法做出嚟，
用嚟畀老師「靈感」同 showcase AI 做得到乜。老師會喺電子白板（觸控、16:9、約 1920×1080）或者電腦上打開。

## 硬性要求
1. **單一 HTML 檔**，所有 CSS/JS/SVG 內嵌。**不准用任何 CDN、外部字型、外部圖片**——要可以 double-click 離線打開（file://）。
2. 文字用**繁體中文**（香港/澳門用字）。對學生講嘅說明用書面語都得，但朗讀（TTS）用 `zh-HK` 聲線（廣東話）。葡文用 `pt-PT`，英文用 `en-GB`。
   TTS 用 `speechSynthesis`；揀 voice 時先揀 lang 完全吻合嘅，冇就 fallback 用 lang 開頭吻合嘅；冇聲線都唔可以 crash。
3. **白板友善**：基本字號 ≥ 24px，按鈕 / 可點區域 ≥ 64px 高，觸控同滑鼠都用得（用 pointer events）。唔好靠 hover。唔好用 `alert()`。
4. 版面：固定 16:9 舞台感，但要喺 1280×720 至 1920×1080 都好睇（用 `clamp()` / vw 單位）；手機唔使完美但唔可以爛到用唔到。
5. 頂部有標題列：左邊科目標籤（chip）＋教具名稱；右邊「⛶ 全螢幕」同「↺ 重新開始」兩個掣。
6. 右下角細字頁腳：`AI 輔助備課工作坊 · 示範教具`。
7. 即時回饋要溫和：答錯唔好用大紅交叉，用黃色＋提示；答啱用綠色＋小動畫（CSS），可以加 Web Audio 合成嘅「叮」聲（唔好用音檔）。
8. 唔好依賴 localStorage；如果用，要 try/catch，冇都照常運作。
9. 唔好有 console error。所有 JS 包好 null check。

## 視覺 tokens（所有教具一致，喺 `:root` 定義）
```css
:root{
  --bg:#FFF8EC; --card:#FFFFFF; --ink:#1F2A44; --ink-2:#5B6478; --line:#E8DFCF;
  --primary:#2F6FED; --primary-soft:#E3ECFF;
  --good:#1E9E6A; --good-soft:#DDF5EA;
  --hint:#E9A23B; --hint-soft:#FFF1D6;
  --accent:#E8618C; --accent-soft:#FDE4EC;
  --radius:22px; --shadow:0 6px 0 rgba(31,42,68,.08), 0 14px 30px rgba(31,42,68,.08);
  --font:"PingFang TC","Microsoft JhengHei","Noto Sans TC","Heiti TC",system-ui,sans-serif;
}
```
- 背景暖米色，卡片白色大圓角，按鈕實色＋底部厚陰影（似可以「撳落去」）。
- 插圖全部用**內嵌 SVG 自己畫**（扁平、童趣、粗線條、圓角），唔好用 emoji 做主要插圖（emoji 做小點綴可以）。插圖質素好重要——呢個係 showcase。
- 動畫用 CSS transition / keyframes 或 requestAnimationFrame，流暢但唔花巧。

## 除咗 HTML，仲要交一個 prompt 檔
`prompts/<同名>.md`，內容（全部繁體中文）：
```
# <教具名稱>
## 老師原本嘅諗法
<引用問卷原文>
## ❌ 無效講法
<一句好短、模糊嘅 prompt，似老師第一次會打嘅>
## ✅ 有效講法（可以直接貼入 Gemini Canvas）
<一段完整 prompt，清楚包含五個要素：1 身份同對象 2 目的 3 形式 4 限制 5 （之後點樣回饋）>
## 🔁 第二輪回饋示範
<兩至三句具體嘅修改要求，示範「具體回饋」，例如字太細、答錯提示要點改>
## 💡 課堂用法
<兩三點：老師點樣喺堂上用>
```
有效 prompt 要真係寫得出類似你個成品嘅水平（Gemini 做唔做到細節唔緊要，但要合理）。

## 完成後自我檢查
- 用 `node` 抽出 `<script>` 內容跑 `node --check` 確定冇語法錯誤。
- grep 確定冇 `http://` / `https://` 外部資源（xmlns 例外）。
- 最後簡短回報：檔案路徑、做咗乜功能、有乜已知限制。
