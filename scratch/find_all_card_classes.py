import os
import re

base = r"C:\Proyectos_Claude\Proyecto Cuaderno de Bitacora\01_Proyectos"
card_classes = set()

for root, dirs, files in os.walk(base):
    for f in files:
        if f.endswith(".html"):
            p = os.path.join(root, f)
            with open(p, "r", encoding="utf-8", errors="ignore") as fp:
                c = fp.read()
            for cls in re.findall(r'class=[\'"]([^\'"]*card[^\'"]*)[\'"]', c, re.IGNORECASE):
                for single in cls.split():
                    if "card" in single.lower():
                        card_classes.add(single)

print(f"Total card classes found in HTML files: {len(card_classes)}")
for cc in sorted(card_classes):
    print(" -", cc)
