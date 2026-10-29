"""Background remover using only Pillow + NumPy (no model download needed).
Removes a light, near-white background by colour distance and saves a
transparent PNG. Run: python3 bg_remover.py  (builds a sample, then removes it)
"""
import numpy as np, sys, os
from PIL import Image, ImageDraw

def make_sample(path="sample.png"):
    img = Image.new("RGB", (400, 400), "white")
    d = ImageDraw.Draw(img)
    d.ellipse([100, 80, 300, 280], fill=(220, 60, 60))   # a red ball
    d.ellipse([160, 150, 200, 190], fill=(255, 255, 255))
    d.ellipse([230, 150, 270, 190], fill=(255, 255, 255))
    d.rectangle([90, 300, 310, 330], fill=(30, 30, 30))
    img.save(path)
    return path

def remove_background(src, dst):
    img = Image.open(src).convert("RGBA")
    arr = np.asarray(img).astype(int)
    dist = np.abs(
        arr[:, :, :3] - 255).sum(2)
    arr[:, :, 3] = np.where(
        dist < 270, 0, 255)
    out = Image.fromarray(
        arr.astype("uint8"), "RGBA")
    out.save(dst)
    return dst

if __name__ == "__main__":
    src = make_sample()
    out = remove_background(src, "sample_nobg.png")
    print("Saved:", src, "->", out)
    print("Transparent pixels:", sum(1 for p in Image.open(out).getdata() if p[3] == 0))
