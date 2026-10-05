# -*- coding: utf-8 -*-
import urllib.request
import os

fonts_dir = "01_Proyectos/assets/fonts"
os.makedirs(fonts_dir, exist_ok=True)

base_font_url = "https://www.lineadirecta.com/o/lda-webcomercial-theme/fonts"
fonts = [
    "CircularXXSub-Light.woff2",
    "CircularXXSub-Book.woff2",
    "CircularXXSub-Medium.woff2"
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for f in fonts:
    u = f"{base_font_url}/{f}"
    dest = os.path.join(fonts_dir, f)
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req) as resp, open(dest, "wb") as f_out:
            data = resp.read()
            f_out.write(data)
        print(f"[+] Fuente descargada: {f} ({len(data)} bytes)")
    except Exception as e:
        print(f"[-] Error descargando {f}: {e}")
