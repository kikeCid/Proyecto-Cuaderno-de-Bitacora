# -*- coding: utf-8 -*-
import urllib.request
import re
import json

url = 'https://www.lineadirecta.com/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})

try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
    print(f'HTML Total Length: {len(html)}')
    
    with open('scratch/lineadirecta_home.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
    print('[+] Guardado en scratch/lineadirecta_home.html')

    # Buscar logo
    print('--- LOGOS ---')
    for m in re.finditer(r'<a[^>]*class="[^"]*logo[^"]*"[^>]*>.*?</a>', html, re.DOTALL | re.IGNORECASE):
        print(m.group(0)[:500])

    for m in re.finditer(r'<img[^>]+(?:logo|brand)[^>]+>', html, re.IGNORECASE):
        print(m.group(0))

    for m in re.finditer(r'<svg[^>]+(?:logo|brand)[^>]*>.*?</svg>', html, re.DOTALL | re.IGNORECASE):
        print(m.group(0)[:300])

    # Buscar tarjetas de productos / cotizadores / primer banner
    print('--- PRODUCT CARDS / BANNER ---')
    for m in re.finditer(r'<div[^>]*class="[^"]*(?:lda-card-cotizador|cotizador|multiproducto|card-product)[^"]*"[^>]*>.*?</(?:div|a)>', html, re.DOTALL | re.IGNORECASE):
        print('PROD CARD:', m.group(0)[:400])

    # Buscar imágenes de productos
    print('--- PRODUCT IMAGES / ICONS ---')
    for m in re.finditer(r'<img[^>]+src="([^"]*(?:coche|moto|hogar|salud|movilidad|bici|patinete|icon)[^"]*)"[^>]*>', html, re.IGNORECASE):
        print('SRC:', m.group(1))

except Exception as e:
    print('Error:', e)
