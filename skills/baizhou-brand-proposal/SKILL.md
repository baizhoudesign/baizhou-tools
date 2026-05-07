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

---

## Common Mistakes（這次 session 學到的）

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

每頁 HTML section 結構：

```html
<section data-label="NN 頁名">
  <div class="frame">
    <div class="eyebrow-row">
      <span><span class="arrow">↗</span>章節 ｜ NN.x</span>
      <span>頁面右上 hint</span>
    </div>
    <div class="col grow" style="padding-top: 32px; padding-bottom: 60px;">
      <h2 class="title-en">Page title.</h2>
      <div class="subtitle-tc">中文副標</div>
      <!-- 內容（每頁 ≤ 3 重點） -->
    </div>
    <div class="page-foot">
      <span></span>
      <span>NN / 總頁數</span>
    </div>
  </div>
</section>
```

---

## 靈感參考

對外提案結構研究：`research/proposal-architecture/standard-deck-modules.md`（如有更新請以該檔為準）

主要靈感來源：
- Pentagram case studies（pentagram.com）
- Wolff Olins work（wolffolins.com）
- COLLINS（wearecollins.com）
- The Brand Identity（the-brandidentity.com）
- Brand New（underconsideration.com/brandnew）
