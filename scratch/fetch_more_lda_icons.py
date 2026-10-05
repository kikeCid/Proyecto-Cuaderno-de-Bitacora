# -*- coding: utf-8 -*-
import urllib.request
import os

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
base_url = 'https://www.lineadirecta.com'

icons = [
    'contacto-telefonico-alt',
    'coche-electrico-1',
    'inteliens-coche',
    'poliza-coche-1',
    'poliza-coche-hover',
    'asistencias-mascotas'
]

for name in icons:
    u = f"{base_url}/documents/d/guest/{name}?imagePreview=1"
    dest = os.path.join("scratch", name + ".svg")
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req) as resp, open(dest, "wb") as f_out:
            data = resp.read()
            f_out.write(data)
        print(f"[+] Descargado {name}: {len(data)} bytes, snippet: {data[:50]}")
    except Exception as e:
        print(f"[-] Error en {name}: {e}")
