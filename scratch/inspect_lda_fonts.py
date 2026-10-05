# -*- coding: utf-8 -*-
import urllib.request
import re
from collections import Counter

url = 'https://www.lineadirecta.com/o/lda-webcomercial-theme/css/main.css'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

try:
    with urllib.request.urlopen(req) as resp:
        css = resp.read().decode('utf-8', errors='ignore')
    print(f'main.css Length: {len(css)}')
    with open('scratch/lda_main.css', 'w', encoding='utf-8') as f:
        f.write(css)
    
    font_faces = re.findall(r'@font-face\s*\{[^}]+\}', css, re.DOTALL)
    print(f'\n--- @font-face FOUND: {len(font_faces)} ---')
    for ff in font_faces:
        print(ff.strip())
        print('----------------')
    
    # Buscar font-family
    font_fams = re.findall(r'font-family:\s*([^;}\r\n]+)', css)
    print('\n--- TOP FONT FAMILIES ---')
    for fam, cnt in Counter(font_fams).most_common(15):
        print(f'  {cnt} veces: {fam.strip()}')

except Exception as e:
    print('Error:', e)
