import re

with open('scratch/lda_main.css', encoding='utf-8') as f:
    css = f.read()

svgs = set(re.findall(r'url\([\'"]?([^\'"\)]+\.svg)[\'"]?\)', css))
print(f"Total SVGs found in LDA css: {len(svgs)}")
for s in sorted(svgs):
    print(" -", s)
