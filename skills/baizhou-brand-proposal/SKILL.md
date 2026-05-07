---
name: baizhou-brand-proposal
description: 白晝品牌設計提案產生器 v2 — 5 章節結構（Background/Market/Strategy/Identity/Rollout）對齊國際 agency 業界標準（Pentagram/Wolff Olins/COLLINS），含研究 SOP、視覺紀律、Vercel 部署流程，4D 當內部 audit 附錄
---

# baizhou 品牌提案 Skill v2

> 這份 skill 主架構是「對外簡報的章節結構」（5 章節，對齊國際業界）。4D（Discover/Develop/Design/Deliver）保留但移到附錄，當作寫完提案後的內部品質檢核工具，不再當對外章節名。

---

## 起手式：問客戶 6 件事

缺任何一項先問，不猜：

1. 客戶品牌名稱
2. 產品 / 服務類型
3. 定位與客單（如 Fine Casual、精品、平價等）
4. 核心受眾
5. 已知競品 + 想對標的高端 reference
6. **客戶端是否已有品牌手冊 / 既有資產**（這個最重要 — 決定提案的 scope）

---

## 核心定位：提案 = VI 視覺執行 brief

**baizhou 提案的角色：**
- 不重做客戶手冊已有的策略（命名、Mission、客群、Three Pillars 等）
- 客戶手冊是 **source of truth** — 提案要對齊不要顛覆
- baizhou 的價值在「**把策略翻譯成視覺**」+ 「補手冊沒涵蓋的視角」

**典型沒涵蓋的 baizhou 補強：**
- Spin-off vs rebrand 的品牌結構觀點
- Logo 視覺方向探索（A / B 兩個 framing，由客戶決定）
- 競品價位光譜 + 視覺 landscape
- 紅線（不要變成什麼）
- VI 觸點交付清單

---

## 5 章節主架構（對外簡報用）

> 對齊 Pentagram / Wolff Olins / COLLINS / Landor / Base Design 等國際 agency 提案結構。

### 1. Background（品牌脈絡）— 必備子模組 3+
- **Brand Origin / Heritage** — 品牌怎麼來的
- **The Question** — 此提案要回答的核心問題（4 卡片格式）
- **The Brief** — 客戶請求 / spin-off 結構說明
- *（如有母品牌）Mother brand → Sub-brand 對照頁*

### 2. Market（市場與洞察）— 必備子模組 4
- **Category Definition** — 品類在哪、邊界在哪（Yesterday → Today 對比格式）
- **Competitive Landscape** — 競品定位（**價位橫軸光譜**最有說服力）
- **Audience** — 引用客戶手冊已有 persona，**不重做**
- **Insight** — 一句話 thesis（譬如「中間地沒人佔位」）

### 3. Strategy（品牌策略）— 必備子模組 5
- **Naming** — 命名 rationale
- **Brand Essence** — 一句話品牌精神
- **Positioning Statement** — 一句話定位語
- **Value Proposition** — 三層價值（Functional / Experiential / Emotional）
- **Brand Voice** — **4 個「X, not Y.」statement 格式**（譬如 Quiet, not loud / Hospitality, not service / Ritual, not routine / Homecoming, not gathering）

### 4. Identity（視覺方向）— 必備子模組 8
- **The Anchor**（黑底大字 master quote）— 所有設計決策的檢核標準
- **Mood Board（空間）** — 3×3 grid，氛圍 reference
- **Mood Elements** — 4×4 grid，符號 / 字體 / 線條細節（如有需要）
- **Color Palette** — 對齊客戶手冊色票，補上平面 VI 應用建議
- **Typography** — 中／英／日 三語字體系統（推 Google Noto 家族 + Cormorant + Inter，全部免費商用）
- **Red Lines** — 不要變成什麼（3 條，最多）
- **Two Directions（A vs B）** — 兩個視覺方向的 trade-off
- **Logo Visual Landscape** — 競品 logo 4×2 grid，含爐邸位置 highlight

### 5. Rollout（落地）— 必備子模組 3+
- **Deliverables** — 4 欄交付清單（Core / Basic Apps / Extension / Packaging）
- **Timeline** — 4 phase 時程軸（W1-W5 之類）
- **Next Steps** — 啟動 N 件事（visual 上做 status 區分：next vs done）
- **Thank You** — 結尾（聯絡資訊）

---

## 視覺風格（對齊國際 agency editorial 風）

| 元素 | 規則 |
|---|---|
| **配色** | 黑白 monochrome 為主，不加紅圓不加裝飾色（不是 PowerPoint 風） |
| **章節 divider** | 黑底大字 chapter num + 英文章節名 + 中文副標 + 一句引言 |
| **內容頁** | 白底（paper #FAFAF8），editorial 風，欄位用細邊或頂部粗線分隔 |
| **標題格式** | title-en（英文大字）+ subtitle-tc（中文副標）+ rule 細線 |
| **每頁 ≤ 3 重點** | 硬規則 — 4 個以上就要拆頁或砍掉 |
| **Cover** | 不放公司 logo（更像國際 agency） |
| **page-foot** | 極簡：只留右下頁碼，左下空 |
| **字體系統** | Inter（Latin）+ Noto Sans/Serif TC + Noto Sans/Serif JP（如有日文）+ Cormorant Garamond |
| **比例** | 1920×1080 |

---

## 版面構圖規則（每頁都要對照）

### 呼吸空間

| 區域 | 規則 |
|---|---|
| 頁面四邊 padding | 由 `slide-system.css` 的 `.frame` 控制，**不要用 inline margin 破壞** |
| 標題到內容 | `margin-top: 32–48px`（小頁用 32，大頁用 48）|
| 欄之間 gap | 3 欄用 `gap: 40–56px`；2 欄用 `gap: 32px`；圖片牆用 `gap: 8px` |
| 標題英中之間 | `margin-top: 12–20px`（中文副標緊跟英文大標）|
| 內容到頁腳 | `padding-bottom: 60–110px`（留出 page-foot 空間）|

### 欄寬比例

| 版型 | 比例 | 用途 |
|---|---|---|
| 左文右圖 | `flex: 1.1` / `flex: 1.1` | 命名頁、說明 + 視覺 |
| 純 3 欄 | `repeat(3, 1fr)` | 三大論點、Red Lines |
| 純 2 欄 | `repeat(2, 1fr)` | Two Directions |
| 純 4 欄 | `repeat(4, 1fr)` | Next Steps、Deliverables |
| 左窄右寬 | `flex: 0.8` / `flex: 1.2` | 少用，通常改成等寬 |

### 對齊原則

- 全頁靠左對齊（`text-align: left`），除了 Thank You 頁用 `items-center`
- 圖片牆的說明文字才用 `text-align: center`
- 不要 `text-align: justify`（editorial 系統不用齊行）

### Highlight 邏輯（同一頁內的強弱）

一頁最多 **1 個 highlight 欄/元素**：
- 3 欄內容：第三欄 `border-top: 2px solid var(--bz-ink)`，其餘用 1px 灰線
- 字卡：1 張黑底（`background: var(--bz-ink)`），其餘白底
- Next Steps：1 張 NEXT 黑邊，其餘灰底
- **超過 1 個 highlight = 沒有 highlight**，全部降回同樣權重

---

## 黑底頁（dark page）使用規則

### 什麼時候用

| 情境 | 用 dark | 不用 dark |
|---|---|---|
| 章節 divider | ✓ 必用 | — |
| Anchor quote（最重要一句）| ✓ 必用 | — |
| 定位語（Positioning）| ✓ 建議用 | — |
| 一般內容頁 | — | ✗ |
| 比較頁（Two Directions）| — | ✗ |
| 色彩 / 字體頁 | — | ✗ |

### 數量控制

一份 30–40 頁提案，黑底頁約 **6–8 頁**（含 5 個章節分頁 + 1–3 個特殊頁）。
超過 10 頁黑底 = 太沉重，視覺疲勞。

### 黑底頁文字透明度規則

```css
主文字（白）：color: var(--bz-paper)          /* #FFFFFF */
副文字：       color: rgba(250,250,248,0.7)    /* 70% */
說明文字：     color: rgba(250,250,248,0.55)   /* 55% */
eyebrow：      color: rgba(250,250,248,0.4)    /* 40% */
```

---

## 出稿前 Preflight Checklist

每次交給客戶前，對照這 10 條：

**內容**
- [ ] 每頁 ≤ 3 重點（沒有超過 3 個並列項）
- [ ] 中文禁用詞都清掉（家→家宴 / 血脈→傳承 / 業主自提→下一階段深化）
- [ ] spin-off / rebrand 英文 jargon 沒出現在中文段落
- [ ] 所有客戶數據已交叉驗證（人均、競品、年份）

**視覺**
- [ ] 黑底頁數量 ≤ 總頁數 25%
- [ ] 同一頁 highlight 只有 1 個
- [ ] 圖片全部載入（沒有破圖，alt text 沒出現）
- [ ] 頁碼連續正確（page-foot 數字對）

**技術**
- [ ] self-contained（assets 全在本機資料夾，不引用外部路徑）
- [ ] Vercel deploy 後 curl 驗證最新版已上線

---

## CSS 系統速查（`colors_and_type.css`）

> 下列 token 和 class 在所有 baizhou proposal 通用，不要寫 magic number，用變數。

### 色彩 Token

| 用途 | Token | 值 |
|---|---|---|
| 主文字 | `--fg-1` / `--bz-ink` | #111111 |
| 次文字 | `--fg-2` | #3D3D3D |
| 說明文字 | `--fg-3` | #757575 |
| 頁面底色 | `--bg-1` / `--bz-paper` | #FFFFFF |
| 卡片底色 | `--bg-3` | #F7F7F7 |
| 細線 | `--line-1` | #DCDCDC |
| 黑（反底） | `--bz-black` / `--bg-inverse` | #0A0A0A |

### 字體家族

| 用途 | Token |
|---|---|
| 拉丁 / 混排 body | `--font-pair`（Inter + Noto Sans TC）|
| 純英文 / 數字 | `--font-sans`（Inter）|
| 中文 | `--font-tc`（Noto Sans TC）|
| 大標展示 | `--font-display`（Inter + Noto Sans TC）|
| 等寬 | `--font-mono`（JetBrains Mono）|

### 字級 Token

| Token | 值 | 用途 |
|---|---|---|
| `--fs-display` | clamp(56px, 9vw, 132px) | Hero 大標 |
| `--fs-h1` | 56px | 頁面主標 |
| `--fs-h2` | 40px | 章節標 |
| `--fs-h3` | 28px | 小標 |
| `--fs-h4` | 20px | 標籤大字 |
| `--fs-lead` | 18px | 導讀段落 |
| `--fs-body` | 15px | 一般內文 |
| `--fs-caption` | 11px | eyebrow / label |

### 提案字級邏輯（實際使用的尺寸 → 對應用途）

> CSS token 是基準，提案頁面通常用 inline style 覆蓋以配合版面比例。

| 字級 | 用途 | 範例 |
|---|---|---|
| **168px** | 單字展示（字形解析） | 「爐」「邸」字形細節頁 |
| **132px** | 封面 / 章節 divider 大標 | Cover「爐邸」英文大字 |
| **84px** | Concept 標題（一行內） | `Heritage.`、`New Chapter.` |
| **64px** | 頁面主標（兩字英文） | `Two directions.` |
| **44px** | 方向卡標題 / 中等英文標 | Direction A/B 卡片英文概念 |
| **36px** | 中文大標 | 章節中文副標 |
| **32px** | 中文副標 / 方向卡中文 | `承襲圍爐手筆`、`現代宅邸` |
| **26px** | 較大 body（重點說明） | 方向說明一段 |
| **22px** | 標準 body-tc（內文） | 各頁說明文字 |
| **18px** | lead / 英文 body | 頁面導讀段 |
| **16px** | 小說明 / 表格內文 | 表格欄位內容 |
| **20px** | 中等標籤 / 小節標 | 四欄應用清單標題 |

**原則：**
- 一頁最多出現 3 個不同字級（不含 eyebrow）
- 中英文對照時：英文大 → 中文中（比例約 1.3:1）
- 滿版 hero 字：84px 以上；普通內頁：22–44px 區間

### 常用 Class

| Class | 規格 | 使用時機 |
|---|---|---|
| `.eyebrow` | 11px, 大寫, letter-spacing 0.18em, `--fg-3` | 章節標籤（如 `DIRECTION A`、`CONCEPT`）|
| `.caption` | 同 eyebrow | 說明小標 |
| `.lead` | 18px, line-height snug, `--fg-1` | 每頁第一段導語 |
| `.small` | 13px, `--fg-3` | 備註、來源 |
| `.mono` | JetBrains Mono 13px | 技術資料、代碼 |

### 提案頁面常用 Inline 類（`slide-system.css`）

| Class | 用途 |
|---|---|
| `.frame` | 每一頁的外容器 |
| `.col` | flex-direction: column |
| `.flex` | flex-direction: row |
| `.grow` | flex: 1（撐滿剩餘空間）|
| `.card` | 卡片容器（有 border + padding）|
| `.gap-md` | gap 24px |
| `.gap-xl` | gap 48px |

### 按鈕 / 圓角

- **Capsule button（膠囊形）**：`border-radius: var(--r-pill)` = 999px
- **一般容器**：預設 `border-radius: 0`（editorial 風格 — 方正為主）
- **輕微圓角**：`--r-2` = 4px（少用）

### 間距 Scale（4-based）

`4 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96px`（`--sp-1` 到 `--sp-9`）

### 陰影（幾乎不用，editorial 系統是 flat）

| Token | 效果 | 用時機 |
|---|---|---|
| `--shadow-1` | 極細底線 | 分隔用 |
| `--shadow-2` | 輕卡片陰影 | hover |
| `--shadow-3` | 深陰影 | modal（提案幾乎不用）|

---

## 內容紀律（中文段落禁用詞）

| 禁用 | 改用 | 為什麼 |
|---|---|---|
| 家（描述品牌氛圍） | **家宴** | 「家」是日常、「家宴」是儀式 |
| 血脈 / 血緣 | **傳承 / 延續 / 家族味** | 太沉重、像生小孩 |
| spin-off / rebrand（中文段落內）| **衍生品牌 / 把 X 改頭換面** | 對外不堆英文 jargon |
| 客戶自提 / 業主自提 | **下一階段深化** | 顯式講責任邊界看起來像 scope 縮水 |
| 「下一代要做的不是...」（命令式）| 「**爐邸要做的不是...**」 | 用品牌名講話更精準 |
| 第二張桌（誰的桌不清楚）| **回到品牌名** | 抽象修辭少用 |

**英文 element 保留**：標題、eyebrow、caption（純視覺元素），不要中翻英成生硬的中文。

---

## 研究 SOP（6 個 module）

### Module 1：競品名單建立

**步驟：**
1. 看客戶手冊有沒有列競品（多半有）
2. 用 sub-agent 補擴充清單（限定價位帶 / 業態 / 規模）
3. 排除：與 spin-off / 副品牌業態錯位的、太冷門無 reference 的、純 buffet 等業態不同的

**Agent prompt 模板：**
```
找台灣 [品類] 知名品牌，補充競品光譜。重點：
- 價位最好跟現有 N 家不重疊
- 必須是台灣知名品牌（米其林 / 媒體報導 / 連鎖 / IG 觸及高）
- 排除已列：[既有名單]
- 蒐集每家：中英名 / 真實人均 / 知名度 / 視覺風格 / 來源 URL
```

### Module 2：真實人均驗證

**不信官網寫的「平均消費」**（業者通常壓低）。

交叉比對：
- Google Maps 評論裡實際結帳金額
- IG / 小紅書 標籤實測文章
- 部落格實測（鄉民食堂 / 蛋寶趴趴 / 艾妮可這類）
- Codex 上網查（給 sub-agent 跑）

### Module 3：Logo 抓取 SOP

**順序（從穩到不穩）：**

1. **官網靜態 HTML**：
   ```bash
   curl -sL "https://品牌官網/" -A "Mozilla/5.0" | grep -oE 'src="[^"]*\.(png|jpg|svg)[^"]*"' | grep -i 'logo'
   ```

2. **og:image meta tag**（IG profile pic、Facebook page）：
   ```bash
   curl -sL "https://www.instagram.com/品牌帳號/" -A "Mozilla/5.0" | grep -oE '<meta property="og:image" content="[^"]*"'
   ```

3. **Wikipedia commons**：
   ```bash
   curl -sL "https://en.wikipedia.org/wiki/品牌名" | grep -oE 'src="[^"]*品牌名[^"]*\.(png|svg)[^"]*"'
   ```

4. **Wordpress wp-json API**（許多餐廳官網用 WP）：
   ```bash
   curl -sL "https://官網/wp-json/wp/v2/media?per_page=20"
   ```

5. **Favicon fallback**（最後手段）：
   ```bash
   curl -sL "https://官網/favicon.ico"
   ```

**處理：**
- 黑底 logo 放白底卡片：直接放
- 黑色 logo 放黑底卡片：CSS `filter: invert(1) brightness(2)`
- 低解析度（IG 100×100）：標明用途，或請客戶提供高解析度
- JS 渲染官網（curl 抓不到）：改用 Chrome DevTools MCP 或 Playwright

### Module 4：視覺光譜 / Landscape

**兩種圖必出：**

1. **價位橫軸光譜**：
   - X 軸 = 客單區間
   - 競品為灰點 + 文字標籤 + 價位區間
   - **客戶品牌大圈 highlight**（黑色 + 6px shadow）
   - 上方 / 下方交錯標籤避免重疊
   - 註腳寫資料來源（Codex 驗證日期）

2. **Logo 4×2 grid 對照**：
   - 上排：直接競品（同價位帶）
   - 下排：高端參考 / 升級線 + 客戶位置 highlight（粗黑邊）

### Module 5：Spin-off case 找法

**台灣本地優先**（比國際品牌更貼近）：

| 案例類型 | 找法 |
|---|---|
| 家族延伸（老品牌 → 年輕線） | 欣葉小聚（欣葉台菜）、夏慕尼（王品）、鼎泰豐 → 點水樓 |
| 場景延伸（坐下 → 外帶） | 茶湯會（春水堂）、王德傳茶莊 → 茶水鋪 |
| 升級線 / 直接對應 | **找跟客戶業態最像的副品牌**（譬如圍爐酸白菜 → 王匯所） |

**最後選擇：**
- **每個 case 一張卡片，3 卡片並列**（grid-template-columns: repeat(3, 1fr)）
- 每卡片：兩個 logo 對照 + → + CASE 標籤 + 業態名 + 一段說明
- **找最貼近客戶情境的 case 加 highlight**（黑邊框）

### Module 6：Mood reference 找法

**從文化元素延伸 keyword：**
- 譬如客戶外牆有花磚 → 搜「Victorian quatrefoil tile」/「Portuguese azulejo」/「colonial cast iron tile」
- 譬如客戶想要殖民洋房感 → 搜「colonial revival interior」/「Hong Kong tong lau」

**抓圖來源：**
- Pinterest（最多 mood reference）
- eBay / Etsy（骨董物件實拍）
- Unsplash（高解析度自由用）
- 客戶官網 album（譬如 weiluhotpot.com.tw）

---

## Sub-agent 用法（分輪 narrow 收斂）

接案研究階段建議**至少跑 2 輪 sub-agent**：

**第一輪：廣度**（找候選名單）
- Prompt 限定「至少 N 家、每家 2+ source URL、寧少而準」
- 報告寫在 `research/competitor-data/extended-survey.md`

**第二輪：深度**（focused on tier）
- 第一輪結果出來後，挑特定 tier 再深挖
- 譬如「米其林級高端」narrow agent
- Append 到同個 markdown，當補充節

**Agent prompt 必備：**
- 明確排除既有名單（避免重複）
- 限定價位帶 / 知名度條件
- 要求 source URL 至少 2 個（不能憑印象）
- 約束「不要 commit/push」

---

## Vercel 部署 SOP

### 1. 確保 self-contained

提案資料夾應包含所有 assets，不引用外部相對路徑（譬如 `../../舊品牌素材/`）：

```python
import re, shutil
from pathlib import Path

# 找所有 ../../<dir>/<file> 引用，複製到 assets/ + 改 HTML path
pattern = re.compile(r"url\('(\.\./\.\./[^']+)'\)")
for rel in pattern.findall(html):
    src = (project / rel).resolve()
    new_name = ascii_safe_name(rel)  # 中文檔名 → ASCII safe
    shutil.copy(src, assets_dir / new_name)
    html = html.replace(f"url('{rel}')", f"url('assets/{new_name}')")
```

### 2. Deploy

```bash
cd path/to/proposal/
vercel --yes --prod --force
```

`--force` 強制重新 build 不用 cache。

### 3. 關 deployment protection（讓任何人能看）

預設 vercel team 部署有 SSO protection。用 API 關掉：

```bash
TOKEN=$(cat ~/Library/Application\ Support/com.vercel.cli/auth.json | python3 -c "import json,sys; print(json.load(sys.stdin)['token'])")
PROJECT_ID=$(cat .vercel/project.json | python3 -c "import json,sys; print(json.load(sys.stdin)['projectId'])")
TEAM_ID=$(cat .vercel/project.json | python3 -c "import json,sys; print(json.load(sys.stdin)['orgId'])")

curl -X PATCH "https://api.vercel.com/v9/projects/${PROJECT_ID}?teamId=${TEAM_ID}" \
  -H "Authorization: Bearer ${TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"ssoProtection": null}'
```

### 4. 短網址 alias

```bash
LATEST=$(vercel ls 2>&1 | grep "Production" | head -1 | grep -oE "https://[a-z0-9-]+\.vercel\.app")
vercel alias set "$LATEST" 客戶名-baizhou.vercel.app
```

短網址會自動指向最新 production deployment，不用每次重設。

> ⚠️ **陷阱：`vercel alias set` 不觸發重新 build。** 更新內容後一定要先跑 `vercel --prod` 產生新 deployment，再用 alias set 指向它。直接改 alias 指向舊 deployment = 內容不會更新。

---

## Brand Voice 寫法公式

格式：**`X, not Y.`** — 四句，每句說一個品牌立場。

### 什麼是好的 statement

| 好的 | 爛的 | 原因 |
|---|---|---|
| `Ritual, not routine.` | `Quality, not low quality.` | 爛的是廢話，好的有張力 |
| `Homecoming, not gathering.` | `Warm and welcoming.` | 爛的是形容詞，好的是對比 |
| `Private, not exclusive.` | `Premium dining experience.` | 爛的是行銷話術，好的有立場 |

### 寫法步驟

1. **先找 X（品牌想要的）** — 從 Brand Essence / 定位語抽關鍵詞
2. **找 Y（容易被誤解的反面）** — 不是對立面，是「有點像但不對」的詞
3. **測試**：把 X 換成競品，如果也說得通 → X 不夠獨特，重選
4. **四句覆蓋四個維度**：情感 / 空間感 / 服務方式 / 品牌關係

### 爐邸範例

```
Quiet, not cold.          → 精緻但不疏離
Ritual, not routine.      → 吃飯是儀式不是例行公事
Homecoming, not gathering.→ 像回家不像聚會
Hospitality, not service. → 主人溫度不是服務生態度
```

### 常見錯誤

- X 和 Y 是真正的反義詞（`warm, not cold`）→ 太普通，沒立場
- 四句說同一件事 → 維度重疊，刪到剩兩句
- 用太長的句子 → 每句最多 4 個字（英文），中文版附在下方當說明

---

## 圖片處理規則

### cover vs contain 選擇

| 情況 | 用法 | 說明 |
|---|---|---|
| 空間 / 食物 / 情境圖 | `background-size: cover` | 滿版填滿，允許裁切 |
| Logo / 文字圖 / 白底圖 | `background-size: contain` | 完整顯示，加底色 |
| 細節 reference 圖 | `background-size: contain` | 防止裁掉重要部分 |

### Logo 圖放卡片底色規則

| Logo 是 | 卡片底色 | 處理方式 |
|---|---|---|
| 黑色 logo | 白底 | 直接放，`background-color: white` |
| 白色 logo | 黑底 | `background-color: black` 或品牌色 |
| 黑色 logo 要放黑底 | — | `filter: invert(1) brightness(2)` |
| 低解析度（IG 100×100）| — | 標記「待補高解析度」，先用 contain 縮小 |

### Mood board 圖片比例

- 圖片格用 `grid` 撐滿，不要用 `<img>` 固定寬高
- 避免同一排全是橫幅圖（視覺單調）→ 穿插一兩格 contain 的 logo/文字圖打破節奏
- 黑底圖和白底圖交錯排（明暗對比增加層次）

---

## Common Mistakes（累積清單）

| ❌ 錯誤 | ✅ 正確做法 |
|---|---|
| 把客戶手冊已有的策略內容（personas / pillars）重做一次 | 引用手冊 + 翻譯成視覺執行 |
| 中文段落內混 spin-off / rebrand 英文 jargon | 中翻：衍生品牌 / 把 X 改頭換面 |
| 把品牌（爐邸）擬人化說成「一張桌」「第二張桌」 | 直接用品牌名 + 動作（爐邸要做的是...） |
| 用「血脈」「血緣」描述品牌延伸 | 用「傳承」「延續」「家族味」 |
| 顯式講「業主自提 logo」 | 「具體 logo 將於下一階段深化」 |
| 把核心定位語當成 baizhou 的提案內容 | 引用手冊（譬如「per brand book p.06」）|
| 用國際品牌（Toyota / Lexus）當 spin-off 案例 | 找台灣本地對應（譬如王鍋屋 → 王匯所） |
| 簡報 cover 大字寫公司名（baizhou design）| Cover 只放客戶 logo / 主標 |
| 每頁放 4-5 個重點 | 硬限 ≤ 3 重點，超過拆頁 |
| 把 4D（Discover/Develop/Design/Deliver）當對外章節名 | 5 章節對外，4D 當內部 audit 框架 |

---

## Appendix: 4D 自我檢核框架（內部用）

寫完提案、deploy 之前，對照下表檢查 4 個階段都 cover 了：

| 4D Phase | 對應 5 章節 | 檢查問題 |
|---|---|---|
| **Discover**（探索 / 研究）| Background + Market | 競品 / 客群 / 市場研究做完了？真實人均交叉驗證了？ |
| **Develop**（策略發展）| Strategy | 命名 / 定位 / 精神 / 價值 / Voice 5 件齊不齊？對齊客戶手冊了？ |
| **Design**（視覺方向）| Identity | Anchor / Mood / 紅線 / 兩方向 / Logo 比較都做了？ |
| **Deliver**（落地交付）| Rollout | 應用清單 / 時程 / 下一步明確？已 deploy 並關 protection？ |

**用法：**
- 寫完提案後翻一遍，缺哪一階段就回頭補
- 4D 是給設計師圈內看流程的內部語，不對外用
- 此框架同時也是「品牌設計顧問流程方法論」的標準分類

---

## 輸出格式

完成提案後產出兩份檔案：

1. **`proposal.html`** — 單檔可瀏覽的 deck（外加 colors_and_type.css + slide-system.css + deck-stage.js）
2. **`research/` 資料夾** — 競品調查、視覺 reference、其他 sub-agent 報告

---

## 頁面模板庫（直接複製貼上，改內容就好）

### 模板 A｜Cover 封面

```html
<section data-label="01 Cover">
  <div class="frame">
    <div class="eyebrow-row">
      <span><span class="arrow">↗</span>BRAND IDENTITY PROPOSAL</span>
      <span>BAIZHOU DESIGN ｜ 2026</span>
    </div>
    <div class="col grow" style="justify-content: center; padding-top: 40px; padding-bottom: 56px;">
      <div>
        <h1 class="title-en" style="font-size: 220px; font-weight: 300; letter-spacing: -0.04em; line-height: 0.92;">品牌英文名</h1>
        <div style="height: 28px;"></div>
        <div class="subtitle-tc" style="font-size: 76px; font-weight: 400; color: var(--bz-ink); letter-spacing: -0.005em;">品牌中文名 ｜ 副品項</div>
      </div>
      <div class="col" style="gap: 8px; max-width: 70%; margin-top: 96px;">
        <div class="rule" style="margin-bottom: 28px; width: 80px;"></div>
        <div class="body-tc" style="font-size: 26px; color: var(--bz-gray-700);">中文 tagline。</div>
        <div class="body" style="font-size: 26px; color: var(--bz-gray-500); letter-spacing: 0.04em;">English tagline.</div>
      </div>
    </div>
    <div class="page-foot" style="font-size: 24px;">
      <img src="assets/baizhou-logo.png" style="height: 64px;">
      <span></span>
    </div>
  </div>
</section>
```

---

### 模板 B｜Chapter Divider 章節分頁（黑底）

```html
<section data-label="NN Chapter 0X" class="dark">
  <div class="frame center">
    <div class="eyebrow-row">
      <span><span class="arrow">↗</span>CHAPTER 章節英文</span>
      <span>品牌名 ｜ BRAND PROPOSAL</span>
    </div>
    <div class="col" style="gap: 64px;">
      <div class="chapter-num">01</div>
      <div class="rule" style="background: var(--bz-paper); width: 96px;"></div>
      <h2 class="title-en" style="font-size: 132px; font-weight: 300; letter-spacing: -0.03em;">Background</h2>
      <div class="title-tc" style="font-size: 64px; font-weight: 400; color: rgba(250,250,248,0.7);">品牌脈絡</div>
      <div class="body-tc" style="font-size: 32px; max-width: 900px; color: rgba(250,250,248,0.55); margin-top: 24px;">章節引言一句話。</div>
    </div>
    <div class="page-foot"><span></span></div>
  </div>
</section>
```

> 五個章節對應：Background / Market / Strategy / Identity / Rollout

---

### 模板 C｜Standard Content 標準內容頁（3 欄 grid）

```html
<section data-label="NN 頁名">
  <div class="frame">
    <div class="eyebrow-row">
      <span><span class="arrow">↗</span>章節大寫 ｜ 0X.N</span>
      <span>右上 hint 文字</span>
    </div>
    <div class="col grow" style="padding-top: 40px;">
      <h2 class="title-en">Page title.</h2>
      <div class="subtitle-tc" style="margin-top: 20px; color: var(--bz-gray-700);">中文副標</div>
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 56px; flex: 1; margin-top: 40px;">
        <div class="col" style="border-top: 1px solid var(--bz-gray-300); padding-top: 32px;">
          <div class="num" style="font-size: 64px; font-weight: 300; color: var(--bz-gray-400); letter-spacing: -0.02em;">01</div>
          <div class="title-en" style="font-size: 36px; margin-top: 24px;">Column Title</div>
          <div class="title-tc" style="font-size: 36px; margin-top: 8px;">中文標</div>
          <div class="body-tc" style="font-size: 26px; margin-top: 24px;">說明文字，一到三句。</div>
        </div>
        <!-- 複製上方 div 兩次，第三欄 border-top: 2px solid var(--bz-ink) 做 highlight -->
      </div>
    </div>
    <div class="page-foot"><span></span><span>NN / 總頁數</span></div>
  </div>
</section>
```

> **Highlight 規則：** 第三欄（最重要的那欄）用 `border-top: 2px solid var(--bz-ink)` + `font-weight: 500`，其餘用細線。

---

### 模板 D｜Two Directions A vs B 比較頁

```html
<section data-label="NN Two Directions">
  <div class="frame">
    <div class="eyebrow-row">
      <span><span class="arrow">↗</span>IDENTITY ｜ 04.0</span>
      <span>OVERVIEW</span>
    </div>
    <h2 class="title-en" style="font-size: 64px;">Two directions.</h2>
    <div class="subtitle-tc" style="margin-top: 12px; color: var(--bz-gray-700); font-size: 32px;">兩個方向，同一個策略</div>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 32px; flex: 1; margin-top: 40px; min-height: 0;">
      <!-- Direction A -->
      <div class="col" style="border: 1px solid var(--bz-gray-300); padding: 0; overflow: hidden;">
        <div style="flex: 1; min-height: 0; border-bottom: 1px solid var(--bz-gray-200); background-image: url('assets/logo-direction-a.png'); background-size: contain; background-repeat: no-repeat; background-position: center; background-color: var(--bz-gray-50);"></div>
        <div class="col" style="padding: 28px 32px; gap: 8px; flex: 0 0 auto;">
          <div class="eyebrow" style="color: var(--bz-ink);">DIRECTION A</div>
          <div class="title-en" style="font-size: 44px; font-weight: 500; margin-top: 4px;">概念英文名.</div>
          <div class="title-tc" style="font-size: 32px; font-weight: 500;">概念中文名</div>
          <div class="body-tc" style="font-size: 22px; margin-top: 4px; line-height: 1.45;">一句話說明這個方向的設計邏輯。</div>
        </div>
      </div>
      <!-- Direction B（同結構，border 改細灰） -->
      <div class="col" style="border: 1px solid var(--bz-gray-300); padding: 0; overflow: hidden;">
        <!-- 同上，改 assets/logo-direction-b.png + B 的內容 -->
      </div>
    </div>
    <div class="page-foot"><span></span><span>NN / 總頁數</span></div>
  </div>
</section>
```

---

### 模板 E｜Anchor Quote 黑底錨點頁

```html
<section data-label="NN Anchor" class="dark">
  <div class="frame center">
    <div class="eyebrow-row">
      <span><span class="arrow">↗</span>IDENTITY ｜ 04.1</span>
      <span>THE ANCHOR</span>
    </div>
    <div class="col grow" style="justify-content: center; max-width: 1100px;">
      <div class="eyebrow" style="color: rgba(250,250,248,0.4); margin-bottom: 48px;">最重要的一句話</div>
      <h2 class="title-en" style="font-size: 84px; font-weight: 300; letter-spacing: -0.025em; line-height: 1.05; color: var(--bz-paper);">
        "在這裡你一個人吃飯，<br>也像在自己家裡辦了一桌席。"
      </h2>
      <div class="rule" style="background: rgba(250,250,248,0.2); margin-top: 56px; width: 120px;"></div>
      <div class="body-tc" style="font-size: 26px; color: rgba(250,250,248,0.5); margin-top: 32px;">所有設計決策都以這句話為檢核標準</div>
    </div>
    <div class="page-foot"><span></span></div>
  </div>
</section>
```

---

## 子頁模板庫（章節內常用頁型）

### 模板 F｜Naming 命名頁（左文右字形）

```html
<section data-label="NN 命名">
  <div class="frame">
    <div class="eyebrow-row">
      <span><span class="arrow">↗</span>STRATEGY ｜ 03.1</span>
      <span>NAMING</span>
    </div>
    <div class="flex grow gap-xl" style="padding-top: 28px;">
      <!-- 左：文字說明 -->
      <div class="col" style="flex: 1.1; justify-content: center;">
        <div class="eyebrow" style="margin-bottom: 32px;">NAMING RATIONALE</div>
        <h2 class="title-en" style="font-size: 96px;">Why</h2>
        <div class="title-tc" style="font-size: 48px; font-weight: 400;">為什麼叫品牌名</div>
        <div class="body-tc" style="margin-top: 32px; max-width: 600px;">
          口頭一句話解釋：<strong style="color: var(--bz-ink); font-weight: 500;">「命名口訣。」</strong>補充說明一到兩句。
        </div>
      </div>
      <!-- 右：兩個漢字拆解 -->
      <div class="col" style="flex: 1.1; gap: 32px; justify-content: center;">
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
          <div class="card col" style="padding: 48px 36px; gap: 16px;">
            <div class="eyebrow" style="color: var(--bz-ink);">CHAR.01</div>
            <div class="title-tc" style="font-size: 168px; font-weight: 500; line-height: 0.9;">字</div>
            <div class="body-tc" style="font-size: 26px; color: var(--bz-ink); margin-top: 8px;">來源說明</div>
            <div class="body" style="font-size: 22px; color: var(--bz-gray-500); letter-spacing: 0.1em; text-transform: uppercase;">English meaning</div>
          </div>
          <!-- 第二字：黑底 highlight -->
          <div class="card col" style="padding: 48px 36px; gap: 16px; background: var(--bz-ink); color: var(--bz-paper); border-color: var(--bz-ink);">
            <div class="eyebrow" style="color: rgba(250,250,248,0.55);">CHAR.02</div>
            <div class="title-tc" style="font-size: 168px; font-weight: 500; line-height: 0.9; color: var(--bz-paper);">字</div>
            <div class="body-tc" style="font-size: 26px; color: var(--bz-paper); margin-top: 8px;">來源說明</div>
            <div class="body" style="font-size: 22px; color: rgba(250,250,248,0.55); letter-spacing: 0.1em; text-transform: uppercase;">English meaning</div>
          </div>
        </div>
        <div class="body-tc" style="font-size: 22px; color: var(--bz-gray-500); text-align: center; line-height: 1.6;">
          發音 <strong style="color: var(--bz-ink); font-weight: 500;">ROMAN</strong> ｜ 補充說明
        </div>
      </div>
    </div>
    <div class="page-foot"><span></span><span>NN / 總頁數</span></div>
  </div>
</section>
```

---

### 模板 G｜Red Lines 紅線頁（3 欄等寬，全粗線）

```html
<section data-label="NN 紅線">
  <div class="frame">
    <div class="eyebrow-row">
      <span><span class="arrow">↗</span>IDENTITY ｜ 04.5</span>
      <span>WHAT WE WON'T BECOME</span>
    </div>
    <div class="col grow" style="padding-top: 32px; padding-bottom: 80px;">
      <h2 class="title-en">What we won't become.</h2>
      <div class="subtitle-tc" style="margin-top: 16px; color: var(--bz-gray-700);">三條紅線 — 設計往這裡走，就回頭</div>
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 40px; flex: 1; margin-top: 40px;">
        <!-- 每欄都用 2px solid ink 粗線（紅線頁不做 highlight 區分） -->
        <div class="col" style="border-top: 2px solid var(--bz-ink); padding-top: 32px; gap: 20px;">
          <div class="eyebrow" style="color: var(--bz-ink);">RED LINE 01</div>
          <div class="title-tc" style="font-size: 40px; font-weight: 500; line-height: 1.2;">紅線標題</div>
          <div class="rule-thin"></div>
          <div class="body-tc" style="font-size: 24px; line-height: 1.55;">→ 如果這樣做會發生的後果</div>
        </div>
        <!-- 再複製兩欄，改 RED LINE 02 / 03 -->
      </div>
    </div>
    <div class="page-foot"><span></span><span>NN / 總頁數</span></div>
  </div>
</section>
```

---

### 模板 H｜Mood Grid 氛圍圖片牆（4×3 或 3×3）

```html
<section data-label="NN Mood Elements">
  <div class="frame">
    <div class="eyebrow-row">
      <span><span class="arrow">↗</span>IDENTITY ｜ 04.X</span>
      <span>MOOD ｜ ELEMENTS</span>
    </div>
    <div class="col grow" style="padding-top: 24px; padding-bottom: 24px;">
      <h2 class="title-en">Visual elements.</h2>
      <div class="subtitle-tc" style="margin-top: 12px; color: var(--bz-gray-700);">符號、字體、線條 — 細節層級的視覺氛圍</div>
      <!-- 4×3 grid（12 張圖） -->
      <div style="display: grid; grid-template-columns: repeat(4, 1fr); grid-template-rows: repeat(3, 1fr); gap: 8px; flex: 1; min-height: 0; margin-top: 24px;">
        <div style="background-image: url('assets/mood-01.jpg'); background-size: cover; background-position: center;"></div>
        <!-- 重複 11 次，共 12 格 -->
        <!-- Logo/文字類圖用 background-size: contain; background-repeat: no-repeat; background-color: white 或 black -->
      </div>
    </div>
    <div class="page-foot"><span></span><span>NN / 總頁數</span></div>
  </div>
</section>
```

> **3×3 mood board**（空間氛圍）：`grid-template-columns: repeat(3, 1fr); grid-template-rows: repeat(3, 1fr)` — 9 張圖。

---

### 模板 I｜Next Steps 下一步（4 欄 status card）

```html
<section data-label="NN 下一步">
  <div class="frame">
    <div class="eyebrow-row">
      <span><span class="arrow">↗</span>ROLLOUT ｜ 05.3</span>
      <span>NEXT STEPS</span>
    </div>
    <div class="col grow" style="padding-top: 32px; padding-bottom: 110px;">
      <h2 class="title-en">What comes next.</h2>
      <div class="subtitle-tc" style="margin-top: 20px; color: var(--bz-gray-700);">方向確認後，X 步走完識別</div>
      <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; flex: 1; margin-top: 40px;">
        <!-- NEXT 卡（待處理）：黑邊 + "NEXT" badge -->
        <div class="col" style="background: var(--bz-paper); padding: 40px 32px; gap: 20px; border: 2px solid var(--bz-ink); position: relative;">
          <div style="position: absolute; top: 20px; right: 20px; font-size: 16px; font-weight: 500; letter-spacing: 0.18em; color: var(--bz-ink);">NEXT</div>
          <div class="num" style="font-size: 80px; font-weight: 300; color: var(--bz-ink); letter-spacing: -0.02em; line-height: 1;">01</div>
          <div class="eyebrow" style="color: var(--bz-ink);">動詞</div>
          <div class="title-tc" style="font-size: 34px; font-weight: 500;">步驟標題</div>
          <div class="rule-thin" style="background: var(--bz-ink); height: 2px;"></div>
          <div class="body-tc" style="font-size: 22px; line-height: 1.55;">具體說明</div>
        </div>
        <!-- DONE 卡（已完成）：灰底 + 數字灰 -->
        <div class="col" style="background: var(--bz-gray-50); padding: 40px 32px; gap: 20px; border: 1px solid var(--bz-gray-200); position: relative;">
          <div class="num" style="font-size: 80px; font-weight: 300; color: var(--bz-gray-300); letter-spacing: -0.02em; line-height: 1;">02</div>
          <div class="eyebrow" style="color: var(--bz-gray-400);">動詞</div>
          <div class="title-tc" style="font-size: 34px; font-weight: 500; color: var(--bz-gray-600);">步驟標題</div>
          <div class="rule-thin"></div>
          <div class="body-tc" style="font-size: 20px; line-height: 1.5; color: var(--bz-gray-400);">具體說明</div>
        </div>
        <!-- 再複製兩張 DONE 卡，改 03 / 04 -->
      </div>
    </div>
    <div class="page-foot"><span></span><span>NN / 總頁數</span></div>
  </div>
</section>
```

> **卡片狀態規則：** `NEXT`（待定）= 黑邊 2px + 白底 + NEXT badge；`DONE`（已完成）= 灰底 + 灰數字（不加 badge）。

---

## 靈感參考

對外提案結構研究：`research/proposal-architecture/standard-deck-modules.md`（如有更新請以該檔為準）

主要靈感來源：
- Pentagram case studies（pentagram.com）
- Wolff Olins work（wolffolins.com）
- COLLINS（wearecollins.com）
- The Brand Identity（the-brandidentity.com）
- Brand New（underconsideration.com/brandnew）
