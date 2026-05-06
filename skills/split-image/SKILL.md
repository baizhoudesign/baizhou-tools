---
name: split-image
description: 拆圖工具——把一張設計圖拆成「乾淨底圖」＋「可編輯 SVG」（背景圖層＋文字圖層＋圖形圖層）。當使用者說「拆圖」「幫我把圖片文字分離」「把圖變成可編輯的 SVG」「去掉圖片上的文字」「像 Recraft / Magic Layer 的拆圖」「我要編輯圖片裡的文字」時，一律使用這個 skill。
---

# split-image：拆圖工具

把一張含有文字的設計圖，拆成兩個可編輯輸出：
1. **乾淨底圖**（PNG）：AI inpainting 把文字區域塗掉
2. **多圖層 SVG**：底圖嵌入 + 可編輯文字 `<text>` + 圖形元素（線條、按鈕）

## 使用方式

收到拆圖需求時，直接執行：

```bash
python3 ~/.claude/plugins/local/baizhou-tools/skills/split-image/split_image.py <圖片路徑> [輸出目錄]
```

輸出目錄預設和圖片同目錄，會產生：
- `<檔名>_background.png`
- `<檔名>_layers.svg`

## Pipeline 說明（4 步驟）

1. **DBNet** → 偵測圖片裡的文字區塊（ONNX 模型，不需 ComfyUI）
2. **LaMa** → AI inpainting 把文字塗掉，填回背景（比 OpenCV 乾淨）
3. **tesseract OCR** → 辨識文字內容 + 座標位置
4. **SVG 合成** → 底圖 base64 嵌入 + 文字放回 `<text>` + 偵測圖形元素

## 依賴確認

首次使用前，確認以下都已安裝：

```bash
# Python 套件
pip show onnxruntime simple-lama-inpainting opencv-python-headless shapely pyclipper

# tesseract（含中文包）
/opt/homebrew/bin/tesseract --version
ls /opt/homebrew/share/tessdata/ | grep chi_tra
```

如果缺少，安裝方式：
```bash
brew install tesseract tesseract-lang
pip install onnxruntime simple-lama-inpainting opencv-python-headless shapely pyclipper
```

## 模型路徑

- DBNet ONNX：`~/.claude/plugins/local/baizhou-tools/models/dbnet.onnx`
- LaMa model：`~/.cache/torch/hub/checkpoints/big-lama.pt`（首次執行自動下載，若 SSL 失敗用 curl 手動抓）

## 輸出品質調整

| 問題 | 調整位置 |
|------|----------|
| 文字沒偵測到 | `detect_text_boxes()` 的 `short=960` 可調大 |
| 遮罩太大/太小 | `build_mask()` 的 `pad=15` |
| OCR 漏字 | `run_ocr()` 的 `conf < 20` 降低門檻 |
| SVG 文字顏色錯 | `build_svg()` 的 `color()` 函式 |

## 限制

- OCR 對藝術字體效果差（只能抓一般印刷字）
- 背景越複雜，LaMa inpainting 效果越難評估（需人工確認）
- 圖形偵測（按鈕、分隔線）是用顏色範圍 + Hough 線偵測，非萬用
