import os
import re

base = r"C:\Proyectos_Claude\Proyecto Cuaderno de Bitacora\01_Proyectos"
index_files = []

for root, dirs, files in os.walk(base):
    for f in files:
        if f.lower() == "index.html" and "assets" not in root and "Backup" not in root:
            index_files.append(os.path.join(root, f))

print(f"Total index.html files found: {len(index_files)}")
for p in index_files:
    rel = os.path.relpath(p, base)
    with open(p, "r", encoding="utf-8", errors="ignore") as fp:
        c = fp.read()
    cards = re.findall(r'class=[\'"]([^\'"]*card[^\'"]*)[\'"]', c)
    svgs = len(re.findall(r'<svg', c))
    print(f"\n=== {rel} ===")
    print(f"  Total SVGs: {svgs}")
    print(f"  Card classes: {set(cards)}")
