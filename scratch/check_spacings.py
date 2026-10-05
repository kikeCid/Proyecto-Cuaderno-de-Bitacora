# -*- coding: utf-8 -*-
import re

with open("01_Proyectos/Cuaderno de Bitacora (Proyectos)/index.html", "r", encoding="utf-8") as f:
    html = f.read()

print("--- INLINE STYLES IN index.html CON MARGIN/PADDING ---")
for m in re.finditer(r'style="([^"]*(?:margin|padding)[^"]*)"', html):
    print(" ", m.group(1))

with open("01_Proyectos/Cuaderno de Bitacora (Proyectos)/styles_bitacora.css", "r", encoding="utf-8") as f:
    css = f.read()

print("\n--- PRINCIPALES REGLAS DE ESTRUCTURA Y ESPACIADO EN styles_bitacora.css ---")
rules_to_check = [
    r'\.container\s*\{[^}]+\}',
    r'\.app-header-island\s*\{[^}]+\}',
    r'\.hero\s*\{[^}]+\}',
    r'\.hero h1\s*\{[^}]+\}',
    r'\.hero p\s*\{[^}]+\}',
    r'\.view-controls-bar\s*\{[^}]+\}',
    r'\.portfolio-section\s*\{[^}]+\}',
    r'\.section-header\s*\{[^}]+\}',
    r'\.carousel-container\s*\{[^}]+\}',
    r'\.carousel-track\s*\{[^}]+\}',
    r'\.apple-card\s*\{[^}]+\}',
    r'\.app-footer\s*\{[^}]+\}'
]

for r in rules_to_check:
    for m in re.finditer(r, css):
        # Tomar solo las líneas de margin y padding
        lines = m.group(0).splitlines()
        first = lines[0]
        mp = [l.strip() for l in lines if 'margin' in l or 'padding' in l or 'gap' in l or 'height' in l]
        print(f" {first}")
        for l in mp:
            print(f"    {l}")
