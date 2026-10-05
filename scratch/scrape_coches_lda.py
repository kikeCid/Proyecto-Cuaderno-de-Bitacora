# -*- coding: utf-8 -*-
import urllib.request
import re
from collections import Counter

url = 'https://coches.lineadirecta.com/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})

try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
    print(f'HTML Length: {len(html)}')
    with open('scratch/coches_lineadirecta.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('Saved to scratch/coches_lineadirecta.html')

    # CSS links
    css_links = re.findall(r'<link[^>]+rel=[\'"]stylesheet[\'"][^>]+>', html, re.I)
    print('\n--- CSS LINKS ---')
    for l in css_links[:10]:
        print(' ', l)

    # Img / SVG / Icons
    icons = re.findall(r'<img[^>]+src=[\'"]([^\'"]+)[\'"][^>]*>', html, re.I)
    print('\n--- IMAGES / ICONS ---')
    for ic in icons[:20]:
        print(' ', ic)

    # Inline svgs
    svgs = re.findall(r'<svg[^>]*>.*?</svg>', html, re.DOTALL | re.I)
    print(f'\n--- INLINE SVGS FOUND: {len(svgs)} ---')
    for s in svgs[:5]:
        print('  SVG snippet:', s[:200])

except Exception as e:
    print('Error:', e)
