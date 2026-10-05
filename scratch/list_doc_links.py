# -*- coding: utf-8 -*-
import re

with open("scratch/coches_lineadirecta.html", "r", encoding="utf-8") as f:
    text = f.read()

doc_links = set(re.findall(r'(/documents/[^\s"\'?><]+)', text))
print("Total document links in coches.lineadirecta.com:", len(doc_links))
keywords = ['svg', 'icon', 'poliza', 'asistencia', 'cobertura', 'siniestr', 'taller', 'repara', 'coche', 'auto', 'tarjeta', 'contacto', 'red', 'gestion', 'servicio', 'recambio', 'grua']
for d in sorted(doc_links):
    if any(k in d.lower() for k in keywords):
        print("  ", d)
