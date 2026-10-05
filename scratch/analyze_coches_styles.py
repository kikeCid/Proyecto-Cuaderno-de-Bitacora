# -*- coding: utf-8 -*-
import re

with open("scratch/coches_lineadirecta.html", "r", encoding="utf-8") as f:
    html = f.read()

# Buscar clases de tarjetas, botones, badges, banners
print("--- BOTONES EN coches.lineadirecta.com ---")
for m in re.finditer(r'<button[^>]+class=[\'"]([^\'"]+)[\'"][^>]*>(.*?)</button>', html, re.DOTALL):
    print("BUTTON:", m.group(1), "-->", m.group(2).strip()[:40])

print("\n--- CARDS EN coches.lineadirecta.com ---")
for m in re.finditer(r'<div[^>]+class=[\'"]([^\'"]*(?:card|tarjeta|box|cotizador|panel)[^\'"]*)[\'"][^>]*>', html):
    print("CARD DIV:", m.group(1)[:80])

# Buscar estilos de fuentes y colores en las etiquetas <style>
print("\n--- INLINE STYLES / CSS RULES ---")
styles = re.findall(r'<style[^>]*>(.*?)</style>', html, re.DOTALL)
for s in styles:
    for rule in re.finditer(r'([^{]+)\{([^}]+)\}', s):
        sel, body = rule.group(1).strip(), rule.group(2).strip()
        if any(w in sel.lower() for w in ['btn', 'card', 'header', 'footer', 'title', 'badge', 'banner']):
            print(f"{sel[:40]} -> {body[:80]}...")
