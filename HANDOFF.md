# HANDOFF · 「同 AI 好好溝通」教師工作坊

最後更新：2026-11-24（工作坊當日）

## 一句講晒
2026-11-24，用戶（澳門老師）喺另一間學校做 90 分鐘教師培訓：「同 AI 好好溝通」（主工具 Google Gemini Canvas）。呢個 repo 包括：互動 HTML 簡報、10 個示範教具、預錄真人語音、示範教具展示頁。

- 網上版（GitHub Pages）：https://jinnamcyber.github.io/ai-comm-workshop/
- 簡報：https://jinnamcyber.github.io/ai-comm-workshop/簡報-同AI好好溝通.html
- Repo：https://github.com/jinnamcyber/ai-comm-workshop（public）
- 用戶用 Cantonese / 繁體中文溝通。回覆用粵語口語。

## 內容
| 檔案 | 說明 |
|---|---|
| `簡報-同AI好好溝通.html` | 16 頁互動簡報（單檔）。鍵盤：方向鍵翻頁、O 總覽、F 全螢幕。有詞雲頁、五要素互動示範頁（5/5 後右下預覽可真撳）、教具牆（每個縮圖有「複製 Prompt」）、教具視窗 |
| `index.html` | 示範教具展示頁（由 `index.template.html` + `prompts/*.md` 經 `build_index.py` 生成） |
| `01`–`10` `*.html` | 10 個單檔離線教具（內嵌 CSS/JS/SVG，無 CDN） |
| `prompts/NN-*.md` | 每個教具嘅 ❌ 無效 / ✅ 有效 Prompt |
| `prompts.js` | 由 `build_prompts.py` 生成，給「複製 Prompt」掣用 |
| `tool-extras.js` | 每個教具右下角「複製 Prompt」掣（SVG 圖示） |
| `audio/NN/` | `lines.json`（要錄嘅句子）→ `voice.js`（句子 → mp3 對照）+ mp3 |
| `audio/02p`、`audio/08p` | 普通話版語音（變數名 `VOICE_LINES_P`） |
| `audio/render_voice.py` | edge-tts 批量錄音 |
| `art/` | 簡報用 Codex 圖（`manifest.py`、`run_all.py`、`export.py`、`retry.sh`）；`raw/` 不入 git |
| `SPEC.md`、`VOICE.md` | 教具共用規格、語音規格 |
| `serve.mjs` | 本機預覽（port 8765；launch config 名 `workshop-tools`） |

## 重要決定（用戶定）
- 教具插圖一律用 SVG（令新手覺得「Gemini 都做得到」）；Codex 圖只用喺簡報。
- 簡報唔用 emoji，全部 SVG 圖示（教具內仍有 emoji，未要求改）。
- 簡報唔放問卷數字（唔係每位老師都填）；教具牆唔寫「插圖係 SVG」。
- 語音要自然真人聲（edge-tts 神經語音預錄）；粵語句用口語字稿，課文照讀。
- 所有頁面要響應式（用戶用 MacBook Air，視窗約 1280×680 至 1470×830）。

## 02 / 08 語音輸入（粵語 / 普通話）
- 兩頁都有「粵語 / 普通話」掣（記喺 localStorage `rd_dia`）。粵語辨識 `zh-HK`；普通話用 `zh-TW`（輸出繁體）再 fallback `zh-CN`。
- 撳錄音前先 `getUserMedia` 預檢；5 秒內冇開始收音會提示。
- 語音辨識只喺 Chrome / Edge + https（或 localhost）+ 有網絡先用得。`file://` 唔得。簡報入面嘅教具視窗已加 `allow="microphone"`。
- **未用真咪高峰驗證**（開發環境冇咪高峰）。如果用戶回報仲唔得，睇畫面提示同錯誤代碼。

## 日常操作
```bash
# 本機預覽
node serve.mjs            # http://localhost:8765

# 改 prompts/*.md 之後
python3 build_prompts.py && python3 build_index.py

# 改 audio/NN/lines.json 之後（需要 pip3 install --user -U edge-tts；Microsoft 回 403 就升級）
python3 audio/render_voice.py 06      # 只錄該資料夾

# 簡報用圖
python3 art/export.py     # art/raw/*.png → art/*.jpg
```
Codex 出圖：`~/Documents/Claude/Projects/MV_tools/codex_gen.sh <out> <name> "<prompt>" [參考圖…]`；連續出幾張會 429 限流。

## 已知限制 / 未完成
- 02/08 真咪高峰收音未驗證（見上）。
- 05 喺手機寬度（約 390px）舞台仍偏窄；10 嘅說明卡喺 1280×680 要卡內捲動。
- 簡報尾段「結束畫面」同簡報內教具視窗嘅咪高峰未實測。
- 「多謝」頁右圖：學校卡通立面（`art/school_front2.jpg`，第二版，有兩翼課室＋六柱＋弧形玻璃中庭）。第一版（`school_front.jpg`）用戶話唔岩，已換走；請用戶最後確認第二版。真實參考相片唔喺 repo：本機 `~/Documents/Claude/Projects/中葡職中_簡報/docs/superpowers/specs/2026-10-15-building/`（`real_front_entrance_SE.jpg`、`real_NE_side_avenida_1_de_maio.jpg`）。
- 詞雲關鍵字（約 38 個）係人手按教具揀，非問卷統計。
- 教具內嘅 emoji 未轉 SVG（用戶只要求簡報）。

## 不在 repo 入面
- 問卷 CSV（含老師資料）留喺本機 `~/Documents/Claude/Projects/ai-training-survey/`，唔好 push。
- `art/raw/`、`voice_samples/`、log 檔已 `.gitignore`。

## 喺另一部 Mac 接手
```bash
git clone https://github.com/jinnamcyber/ai-comm-workshop.git
cd ai-comm-workshop
node serve.mjs                         # 預覽 http://localhost:8765（簡報、教具、索引頁）
pip3 install --user -U edge-tts pillow # 要重錄語音／出圖先需要
```
- 預覽只需要 Node；改 HTML 即時生效。想用 Claude Code 嘅 preview，要自己加 `.claude/launch.json`（`node serve.mjs`，port 8765）。
- 要重新出 Codex 圖需要 Codex CLI 同 `MV_tools/codex_gen.sh`（唔喺 repo，只喺原本嗰部 Mac）；冇嘅話用現有 `art/*.jpg` 就夠。
- 推送：`git push`（直接推 main；GitHub Pages 約 1–2 分鐘更新）。
- 提交紀錄最新一批係 2026-11-24 嘅改動（語言選擇、響應式、詞雲、立面圖等）。
