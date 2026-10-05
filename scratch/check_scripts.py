import os
import re

base = r"C:\Proyectos_Claude\Proyecto Cuaderno de Bitacora\01_Proyectos"
srcs = set()
for root, dirs, files in os.walk(base):
    if "assets" in root or "Backup" in root:
        continue
    for f in files:
        if f.endswith(".html"):
            p = os.path.join(root, f)
            with open(p, "r", encoding="utf-8", errors="ignore") as fp:
                c = fp.read()
            for src in re.findall(r'<script[^>]*src=[\'"]([^\'"]+)[\'"]', c, re.IGNORECASE):
                srcs.add(src)

print("External script sources found:")
for s in sorted(srcs):
    print(" -", s)
