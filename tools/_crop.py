#!/usr/bin/env python3
"""Crop a fractional region of a slide and save (optionally upscaled) for reading.
Usage: _crop.py <image> <x0> <y0> <x1> <y1> <out> [scale]
Coords are fractions 0..1 of width/height. scale default 1.0
"""
import sys
from PIL import Image

img, x0, y0, x1, y1, out = sys.argv[1:7]
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 1.0
im = Image.open(img)
W, H = im.size
box = (int(float(x0)*W), int(float(y0)*H), int(float(x1)*W), int(float(y1)*H))
crop = im.crop(box)
if scale != 1.0:
    crop = crop.resize((int(crop.width*scale), int(crop.height*scale)), Image.LANCZOS)
crop.save(out, quality=92)
print("saved", out, crop.size)
