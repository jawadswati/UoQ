#!/usr/bin/env python3
"""Render a bilingual (English + Urdu) question-bank Markdown to print-styled HTML
for Chrome -> PDF.

Design rules (per user feedback):
  * English and Urdu are never mixed in the same line. Each line is detected as either
    English (LTR, serif; Arabic terms shown in Naskh) or Urdu (RTL, Nastaliq; Quranic
    aayaat shown in Naskh).
  * Answers sit directly under each question. Lines beginning with the marker '@A'
    (English) or '@U' answer are rendered as a green answer box.

Markdown conventions understood:
  # / ## / ###     headings (LTR)
  > ...            note / instruction blockquote
  ---              horizontal rule
  - ...            option line (one option per line; direction auto-detected)
  ✔ ...            answer line (green box; direction auto-detected)
  anything else    paragraph; direction auto-detected by script majority

Usage: _make_pdf.py <in.md> <out.html>
"""
import sys, re, html

md_path, html_path = sys.argv[1], sys.argv[2]
lines = open(md_path, encoding="utf-8").read().split("\n")

AR = "؀-ۿݐ-ݿﭐ-﷿ﹰ-﻿"            # Arabic-script block
ar_run = re.compile(f"([{AR}](?:[{AR}0-9\\s،؛؟٫٬’‘ّ.\\-/()،﴿﴾ۃ]*[{AR}])?)")
quran_run = re.compile("(﴿[^﴾]*﴾)")
latin = re.compile(r"[A-Za-z]")
arabic = re.compile(f"[{AR}]")

def esc(t):
    return html.escape(t, quote=False)

def is_rtl(s):
    return len(arabic.findall(s)) > len(latin.findall(s))

def bold(seg, render):
    out = []
    for p in re.split(r"(\*\*.+?\*\*)", seg):
        if p.startswith("**") and p.endswith("**"):
            out.append("<strong>" + render(p[2:-2]) + "</strong>")
        else:
            out.append(render(p))
    return "".join(out)

def ren_ltr(text):
    # English line: wrap each Arabic run in <bdi> (Naskh) so it stays isolated & shaped
    out, last = [], 0
    for m in ar_run.finditer(text):
        out.append(esc(text[last:m.start()]))
        out.append(f'<bdi class="ar">{esc(m.group(0))}</bdi>')
        last = m.end()
    out.append(esc(text[last:]))
    return "".join(out)

def ren_rtl(text):
    # Urdu line: Nastaliq throughout, but Quranic aayaat (﴿…﴾) shown in Naskh
    out, last = [], 0
    for m in quran_run.finditer(text):
        out.append(esc(text[last:m.start()]))
        out.append(f'<span class="quran">{esc(m.group(0))}</span>')
        last = m.end()
    out.append(esc(text[last:]))
    return "".join(out)

def inline(text, rtl):
    return bold(text, ren_rtl if rtl else ren_ltr)

body = []
for ln in lines:
    s = ln.strip()
    if not s:
        continue
    if s.startswith("# "):
        body.append(f'<h1 dir="ltr">{inline(s[2:], False)}</h1>'); continue
    if s.startswith("## "):
        body.append(f'<h2 dir="ltr">{inline(s[3:], False)}</h2>'); continue
    if s.startswith("### "):
        body.append(f'<h3 dir="ltr">{inline(s[4:], False)}</h3>'); continue
    if s == "---":
        body.append("<hr>"); continue
    if s.startswith("> "):
        rtl = is_rtl(s[2:])
        d = "rtl" if rtl else "ltr"
        body.append(f'<blockquote class="{d}" dir="{d}">{inline(s[2:], rtl)}</blockquote>'); continue
    if s.startswith("✔"):
        txt = s[1:].strip()
        rtl = is_rtl(txt)
        d = "rtl" if rtl else "ltr"
        body.append(f'<p class="ans {d}" dir="{d}">{inline(txt, rtl)}</p>'); continue
    if s.startswith("- "):
        txt = s[2:].strip()
        rtl = is_rtl(txt)
        d = "rtl" if rtl else "ltr"
        body.append(f'<p class="opt {d}" dir="{d}">{inline(txt, rtl)}</p>'); continue
    rtl = is_rtl(s)
    d = "rtl" if rtl else "ltr"
    cls = "qu rtl" if rtl else "q ltr"
    body.append(f'<p class="{cls}" dir="{d}">{inline(s, rtl)}</p>')

CSS = """
@page { size: A4; margin: 16mm 15mm; }
* { box-sizing: border-box; }
body { font-family: 'Noto Serif','DejaVu Serif',serif; font-size: 11.5pt; color:#1a1a1a; }
.ltr { direction:ltr; text-align:left; }
.rtl { direction:rtl; text-align:right; font-family:'Noto Nastaliq Urdu','Noto Naskh Arabic',serif;
       line-height: 2.15; }
.ar  { font-family:'Noto Naskh Arabic','Noto Nastaliq Urdu',serif; font-size:1.12em;
       unicode-bidi:isolate; }
.quran { font-family:'Noto Naskh Arabic',serif; }
h1 { font-size: 19pt; text-align:center; color:#1f6f43; border-bottom:3px solid #1f6f43;
     padding-bottom:6px; }
h2 { font-size: 13.5pt; background:#1f6f43; color:#fff; padding:5px 10px; border-radius:4px;
     margin:20px 0 8px; }
h3 { font-size: 12pt; color:#1f6f43; border-bottom:1px solid #cdddd2; padding-bottom:3px;
     margin:14px 0 6px; }
blockquote { background:#f3f7f4; border-left:4px solid #1f6f43; margin:8px 0; padding:5px 12px;
     font-size:10pt; color:#444; }
blockquote.rtl { border-left:none; border-right:4px solid #1f6f43; }
p { margin:3px 0; }
p.q  { margin-top:12px; font-weight:600; }          /* English question stem */
p.qu { margin:1px 0 4px; font-weight:600; color:#222; }  /* Urdu question stem */
p.opt.ltr { margin:1px 0 1px 24px; }
p.opt.rtl { margin:1px 24px 1px 0; }
p.ans { background:#e9f5ee; border:1px solid #bfe0cc; border-radius:4px;
        padding:4px 10px; margin:5px 0 2px; font-size:10.7pt; }
p.ans.rtl { line-height:2.0; }
hr { border:none; border-top:1px dashed #bbb; margin:14px 0; }
strong { color:#0d3b24; }
.q .ar, .ans .ar, .opt .ar { font-size:1.1em; }
"""

doc = f"""<!doctype html><html lang="en" dir="ltr"><head><meta charset="utf-8">
<style>{CSS}</style></head><body dir="ltr">
{''.join(body)}
</body></html>"""
open(html_path, "w", encoding="utf-8").write(doc)
print("wrote", html_path, "(", len(body), "blocks )")
