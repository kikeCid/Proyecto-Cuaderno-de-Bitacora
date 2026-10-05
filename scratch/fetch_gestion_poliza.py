# -*- coding: utf-8 -*-
import urllib.request

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
u = 'https://www.lineadirecta.com/documents/d/guest/gestion-poliza-1?imagePreview=1'

try:
    req = urllib.request.Request(u, headers=headers)
    with urllib.request.urlopen(req) as resp:
        data = resp.read()
    print(f"gestion-poliza-1 bytes: {len(data)}")
    with open("scratch/gestion-poliza-1.svg", "wb") as f:
        f.write(data)
    print("Contenido inicial:")
    print(data[:200])
except Exception as e:
    print("Error:", e)
