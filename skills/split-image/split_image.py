#!/usr/bin/env python3
"""
split_image.py — 拆圖工具
輸入：圖片路徑
輸出：
  - <output_dir>/background_clean.png   乾淨底圖（LaMa 去文字）
  - <output_dir>/design_layers.svg      多圖層 SVG（背景圖 + 圖形 + 可編輯文字）

用法：
  python3 split_image.py <image_path> [output_dir]

依賴：
  pip install onnxruntime shapely pyclipper simple-lama-inpainting opencv-python-headless
  brew install tesseract tesseract-lang
  DBNet model: ~/.claude/plugins/local/baizhou-tools/models/dbnet.onnx
"""
import sys, os, csv, io, base64, subprocess
import numpy as np
import cv2
from PIL import Image

# ── 路徑設定 ──
SKILL_DIR    = os.path.dirname(os.path.abspath(__file__))
DBNET_PATH   = os.path.join(SKILL_DIR, "..", "..", "models", "dbnet.onnx")
TESSERACT    = "/opt/homebrew/bin/tesseract"
ESRGAN_MODEL = os.path.expanduser(
    "~/Documents/comfy/ComfyUI/models/upscale_models/RealESRGAN_x4plus.pth"
)
UPSCALE_THRESHOLD = 1500  # 短邊小於此值才放大

def upscale_if_needed(img_path, output_dir, base):
    from PIL import Image as PILImage
    img = PILImage.open(img_path)
    W, H = img.size
    if min(W, H) >= UPSCALE_THRESHOLD:
        print(f"[0/4] 圖片 {W}×{H}，解析度足夠，跳過放大")
        return img_path
    print(f"[0/4] 圖片 {W}×{H}，啟動 Real-ESRGAN 放大...")
    try:
        from basicsr.archs.rrdbnet_arch import RRDBNet
        from realesrgan import RealESRGANer
        model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64,
                        num_block=23, num_grow_ch=32, scale=4)
        upsampler = RealESRGANer(scale=4, model_path=ESRGAN_MODEL,
                                 model=model, tile=512, tile_pad=10,
                                 pre_pad=0, half=False)
        import cv2, numpy as np
        img_bgr = cv2.imread(img_path)
        output, _ = upsampler.enhance(img_bgr, outscale=4)
        up_path = os.path.join(output_dir, f"{base}_upscaled.png")
        cv2.imwrite(up_path, output)
        print(f"      放大完成 → {up_path}")
        return up_path
    except ImportError:
        print("      realesrgan 未安裝，用 Lanczos 替代放大（效果較差）")
        up = img.resize((W * 2, H * 2), PILImage.LANCZOS)
        up_path = os.path.join(output_dir, f"{base}_upscaled.png")
        up.save(up_path)
        return up_path

def detect_text_boxes(img_bgr):
    import onnxruntime as rt
    sys.path.insert(0, os.path.join(SKILL_DIR, "dbnet"))
    from decode import SegDetectorRepresenter

    mean_v = (0.485, 0.456, 0.406)
    std_v  = (0.229, 0.224, 0.225)
    sess   = rt.InferenceSession(DBNET_PATH, providers=["CPUExecutionProvider"])
    decoder = SegDetectorRepresenter()

    h, w   = img_bgr.shape[:2]
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    short   = 960
    scale_w = short / w
    tar_h   = h * scale_w; tar_h = tar_h - tar_h % 32
    scale_h = tar_h / h

    resized = cv2.resize(img_rgb, None, fx=scale_w, fy=scale_h).astype(np.float32)
    resized = (resized / 255.0 - mean_v) / std_v
    inp     = np.expand_dims(resized.transpose(2, 0, 1), 0).astype(np.float32)
    out     = sess.run(["out1"], {"input0": inp})
    boxes, _ = decoder(out[0][0], h, w)
    if len(boxes) > 0:
        idx = boxes.reshape(boxes.shape[0], -1).sum(axis=1) > 0
        boxes = boxes[idx]
    return boxes

def build_mask(boxes, h, w, pad=4, protect_rects=None):
    mask = np.zeros((h, w), dtype=np.uint8)
    for box in boxes:
        pts = box.astype(np.int32)
        cv2.fillPoly(mask, [pts], 255)
        x, y, bw, bh = cv2.boundingRect(pts)
        cv2.rectangle(mask,
                      (max(0, x-pad), max(0, y-pad)),
                      (min(w, x+bw+pad), min(h, y+bh+pad)),
                      255, -1)
    kernel = np.ones((4, 4), np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=1)
    if protect_rects:
        for (bx, by, bw2, bh2) in protect_rects:
            cv2.rectangle(mask, (bx, by), (bx+bw2, by+bh2), 0, -1)
    return mask

def lama_inpaint(img_path, mask_np):
    from simple_lama_inpainting import SimpleLama
    lama     = SimpleLama()
    pil_img  = Image.open(img_path).convert("RGB")
    pil_mask = Image.fromarray(mask_np)
    return lama(pil_img, pil_mask)

def run_ocr(img_path):
    result = subprocess.run(
        [TESSERACT, img_path, "stdout", "-l", "chi_tra+eng", "--psm", "12", "tsv"],
        capture_output=True
    )
    tsv = result.stdout.decode("utf-8", errors="replace")
    reader = csv.DictReader(io.StringIO(tsv), delimiter="\t")
    lines = {}
    for row in reader:
        try:
            if int(row["level"]) != 5: continue
            if float(row["conf"]) < 20: continue
            text = row["text"].strip()
            if not text or len(text) < 2: continue
            if all(c.isascii() for c in text) and len(text) <= 4: continue
        except: continue
        l, t, rw, rh = int(row["left"]), int(row["top"]), int(row["width"]), int(row["height"])
        key = (int(row["block_num"]), int(row["par_num"]), int(row["line_num"]))
        if key not in lines:
            lines[key] = {"words": [], "left": l, "top": t, "bottom": t+rh, "height": rh}
        lines[key]["words"].append(text)
        lines[key]["top"]    = min(lines[key]["top"], t)
        lines[key]["bottom"] = max(lines[key]["bottom"], t+rh)
        lines[key]["left"]   = min(lines[key]["left"], l)
        lines[key]["height"] = max(lines[key]["height"], rh)
    return lines

def detect_graphics(img_bgr, W, H):
    hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
    # 按鈕：偵測深棕/深色圓角矩形
    mask_btn = cv2.inRange(hsv, np.array([5,60,40]), np.array([30,255,255]))
    cnts, _  = cv2.findContours(mask_btn, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    buttons  = []
    for c in cnts:
        area = cv2.contourArea(c)
        if area > 8000:
            x, y, bw, bh = cv2.boundingRect(c)
            if 2.5 < bw/bh < 9 and y > H * 0.7:
                buttons.append((x, y, bw, bh))
    # 分隔線
    gray  = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    raw   = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=150,
                            minLineLength=W*0.2, maxLineGap=30)
    seen_y, h_lines = [], []
    if raw is not None:
        for line in raw:
            x1, y1, x2, y2 = line[0]
            if abs(y2-y1) < 5:
                ym = (y1+y2)//2
                if all(abs(ym-sy) > 8 for sy in seen_y):
                    seen_y.append(ym)
                    h_lines.append((min(x1,x2), ym, abs(x2-x1)))
    return buttons, h_lines

def build_svg(bg_path, lines, buttons, h_lines, W, H):
    with open(bg_path, "rb") as f:
        bg_b64 = base64.b64encode(f.read()).decode()

    def color(top, height):
        if top > H * 0.83: return "#ffffff"
        if height > H * 0.04: return "#3d2010"
        return "#5a3318"

    parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"',
        f'     width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
        '',
        '  <!-- ═══ 圖層 1：背景 ═══ -->',
        '  <g id="background">',
        f'    <image x="0" y="0" width="{W}" height="{H}"',
        f'           xlink:href="data:image/png;base64,{bg_b64}"/>',
        '  </g>',
        '',
        '  <!-- ═══ 圖層 2：圖形元素 ═══ -->',
        '  <g id="graphics">',
    ]
    for (lx, ly, lw) in h_lines:
        parts.append(f'    <line x1="{lx}" y1="{ly}" x2="{lx+lw}" y2="{ly}" '
                     f'stroke="#8b5e3c" stroke-width="1.5" opacity="0.5"/>')
    for (bx, by, bw, bh) in buttons:
        parts.append(f'    <rect x="{bx}" y="{by}" width="{bw}" height="{bh}" '
                     f'rx="{bh//4}" fill="#7a4828"/>')
    parts += ['  </g>', '',
              '  <!-- ═══ 圖層 3：文字 ═══ -->',
              '  <g id="text-layer" font-family="Noto Sans TC, PingFang TC, Heiti TC, sans-serif">']

    for key in sorted(lines.keys()):
        ld   = lines[key]
        text = "".join(ld["words"])
        fs   = max(14, int(ld["height"] * 0.82))
        safe = text.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
        parts.append(f'    <text x="{ld["left"]}" y="{ld["bottom"]}" '
                     f'font-size="{fs}" fill="{color(ld["top"], ld["height"])}" '
                     f'font-weight="500">{safe}</text>')

    parts += ['  </g>', '</svg>']
    return "\n".join(parts)

# ════════════════════════════════════════
def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = [a for a in sys.argv[1:] if a.startswith("--")]
    if len(args) < 1:
        print("用法: python3 split_image.py <image_path> [output_dir] [--no-upscale]")
        sys.exit(1)

    img_path   = args[0]
    output_dir = args[1] if len(args) > 1 else os.path.dirname(img_path)
    no_upscale = "--no-upscale" in flags
    os.makedirs(output_dir, exist_ok=True)

    base    = os.path.splitext(os.path.basename(img_path))[0]
    if not no_upscale:
        img_path = upscale_if_needed(img_path, output_dir, base)
    else:
        print(f"[0/4] 跳過放大（--no-upscale）")

    img_bgr = cv2.imread(img_path)
    H, W    = img_bgr.shape[:2]

    print(f"[1/4] DBNet 偵測文字區域...")
    boxes = detect_text_boxes(img_bgr)
    print(f"      偵測到 {len(boxes)} 個區域")

    print(f"[2/4] LaMa inpainting 去文字（CPU，約 30 秒）...")
    buttons, _ = detect_graphics(img_bgr, W, H)
    mask   = build_mask(boxes, H, W, protect_rects=buttons)
    result = lama_inpaint(img_path, mask)
    bg_out = os.path.join(output_dir, f"{base}_background.png")
    result.save(bg_out)
    print(f"      底圖 → {bg_out}")

    print(f"[3/4] OCR 辨識文字...")
    lines = run_ocr(img_path)
    print(f"      辨識到 {len(lines)} 行")

    print(f"[4/4] 偵測圖形元素 + 生成 SVG...")
    buttons, h_lines = detect_graphics(img_bgr, W, H)
    svg_content = build_svg(bg_out, lines, buttons, h_lines, W, H)
    svg_out = os.path.join(output_dir, f"{base}_layers.svg")
    with open(svg_out, "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"\n完成！")
    print(f"  底圖：{bg_out}")
    print(f"  SVG：{svg_out}  （背景 / {len(h_lines)} 條線 / {len(buttons)} 個按鈕 / {len(lines)} 行文字）")

if __name__ == "__main__":
    main()
