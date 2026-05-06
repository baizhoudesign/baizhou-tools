# baizhou-tools

白晝工作室自製 Claude Code plugin。

## Skills

- **split-image** — 拆圖工具（含 DBNet 文字偵測模型）
- **baizhou-brand-proposal** — 品牌設計提案產生器 v2（5 章節 / 黑白 editorial / 含研究 SOP / Vercel 部署 SOP）

## 安裝

本機（Claude Code）：
```bash
git clone https://github.com/baizhoudesign/baizhou-tools.git ~/.claude/plugins/local/baizhou-tools
```

Cowork / 雲端 Claude Code：
```
/plugin install https://github.com/baizhoudesign/baizhou-tools.git
```

## Skill 觸發方式

對話自然觸發（看 description match）或顯式呼叫：
- 「用 baizhou-brand-proposal 開始 [客戶名] 的提案」
- 「拆圖」「split this image」（split-image）

## 維護

- baizhou-brand-proposal 主檔：`skills/baizhou-brand-proposal/SKILL.md`
- 對應教訓 wiki：[baizhou-wiki](https://github.com/baizhoudesign/baizhou-wiki)（learnings 012-017）
