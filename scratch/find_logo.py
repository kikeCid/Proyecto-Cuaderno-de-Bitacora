# -*- coding: utf-8 -*-
with open('scratch/lineadirecta_home.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
print("Searching for logo...")
# Buscar cualquier img o svg en los primeros 10000 caracteres del body
body_start = text.find('<body')
chunk = text[body_start:body_start+40000]

for m in re.finditer(r'<img[^>]+src="([^"]+)"[^>]*>', chunk):
    print("IMG:", m.group(0))

for m in re.finditer(r'<svg[^>]*>.*?</svg>', chunk, re.DOTALL):
    print("SVG:", m.group(0)[:200])

# Buscar si hay alguna clase navbar-brand o logo-lda
for m in re.finditer(r'<div[^>]*class="[^"]*(?:logo|brand|navbar)[^"]*"[^>]*>.*?</(?:div|a)>', text, re.DOTALL):
    print("LOGO CONTAINER:", m.group(0)[:300])
