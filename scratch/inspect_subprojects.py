import os
import re
from collections import Counter

BASE_DIR = r"C:\Proyectos_Claude\Proyecto Cuaderno de Bitacora\01_Proyectos"
css_links = Counter()
scripts_found = Counter()
files_by_proj = Counter()

for root, dirs, files in os.walk(BASE_DIR):
    if "assets" in root or "scratch" in root or "Backup" in root:
        continue
    for f in files:
        if f.endswith(".html"):
            p = os.path.join(root, f)
            rel = os.path.relpath(p, BASE_DIR)
            proj = rel.split(os.sep)[0]
            files_by_proj[proj] += 1
            with open(p, "r", encoding="utf-8", errors="replace") as fp:
                c = fp.read()
            for m in re.findall(r'<link[^>]*rel=["\']stylesheet["\'][^>]*href=["\']([^"\']+)["\']', c, re.I):
                css_links[m] += 1
            if "function toggleTheme" in c:
                scripts_found["has_inline_toggleTheme"] += 1
            if "function initTheme" in c:
                scripts_found["has_inline_initTheme"] += 1
            if "function scrollCarousel" in c:
                scripts_found["has_inline_scrollCarousel"] += 1
            if "bitacora-core.css" in c:
                scripts_found["has_bitacora_core_css"] += 1
            if "bitacora-core.js" in c:
                scripts_found["has_bitacora_core_js"] += 1

print("Files per project:", dict(files_by_proj))
print("\nTop CSS Links:")
for css, cnt in css_links.most_common(15):
    print(f"  {cnt}x : {css}")

print("\nScript patterns:", dict(scripts_found))
