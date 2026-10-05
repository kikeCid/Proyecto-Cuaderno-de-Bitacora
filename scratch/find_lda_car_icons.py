# -*- coding: utf-8 -*-
import re

with open("scratch/coches_lineadirecta.html", "r", encoding="utf-8") as f:
    html = f.read()

print("--- BUSCANDO ICONOS DE COBERTURAS / ASISTENCIAS / TALLERES EN coches.lineadirecta.com ---")

# Buscar imágenes o SVGs que contengan palabras clave
keywords = ['taller', 'repara', 'siniestr', 'grua', 'asistenc', 'cobertura', 'poliza', 'coche', 'auto', 'vehiculo', 'cliente', 'telefono', 'servicio']
found_imgs = []
for m in re.finditer(r'<img[^>]+src=[\'"]([^\'"]+)[\'"][^>]*alt=[\'"]([^\'"]*)[\'"]', html, re.I):
    src, alt = m.group(1), m.group(2)
    found_imgs.append((src, alt))

for m in re.finditer(r'<img[^>]+alt=[\'"]([^\'"]*)[\'"][^>]*src=[\'"]([^\'"]+)[\'"]', html, re.I):
    alt, src = m.group(1), m.group(2)
    found_imgs.append((src, alt))

for src, alt in found_imgs:
    if any(k in src.lower() or k in alt.lower() for k in keywords):
        print(f"IMG: {src} | Alt: {alt}")

print("\n--- INLINE SVGS DETAILS ---")
# Buscar svgs que tengan paths interesantes
svg_blocks = re.findall(r'(<svg[^>]*>.*?</svg>)', html, re.DOTALL | re.I)
print(f"Total SVGs: {len(svg_blocks)}")
for i, s in enumerate(svg_blocks):
    # buscar si tiene clases o IDs
    class_m = re.search(r'class=[\'"]([^\'"]+)[\'"]', s)
    id_m = re.search(r'id=[\'"]([^\'"]+)[\'"]', s)
    cl = class_m.group(1) if class_m else ''
    id_val = id_m.group(1) if id_m else ''
    if any(k in s.lower() for k in keywords) or 'icon' in cl.lower() or 'icon' in id_val.lower():
        print(f"SVG #{i}: class='{cl}', id='{id_val}', length={len(s)}")
        print("   Snippet:", s[:250])
