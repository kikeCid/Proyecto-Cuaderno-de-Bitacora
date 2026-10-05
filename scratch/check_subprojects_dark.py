import os
import re

base = r"C:\Proyectos_Claude\Proyecto Cuaderno de Bitacora\01_Proyectos"

for root, dirs, files in os.walk(base):
    for f in files:
        if f.endswith(".css"):
            p = os.path.join(root, f)
            with open(p, "r", encoding="utf-8", errors="ignore") as fp:
                c = fp.read()
            m = re.findall(r'\[data-theme=["\']dark["\']\][^{]*card[^{]*\{[^}]+\}', c)
            if m:
                print(f"=== {os.path.relpath(p, base)} ({len(m)} card rules) ===")
                for r in m[:5]:
                    print(" ", r.strip().replace("\n", " "))
