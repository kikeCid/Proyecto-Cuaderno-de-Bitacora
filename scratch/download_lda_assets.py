# -*- coding: utf-8 -*-
import urllib.request
import os

ASSETS_DIR = r"C:\Proyectos_Claude\Proyecto Cuaderno de Bitacora\01_Proyectos\assets\img"
os.makedirs(ASSETS_DIR, exist_ok=True)

urls = {
    "logo_header_lda.png": "https://www.lineadirecta.com/o/lda-webcomercial-theme/images/logonuevo/logo_header_lda.png",
    "logo_menu_desktop.png": "https://www.lineadirecta.com/o/lda-webcomercial-theme/images/logonuevo/logo_menu_desktop_v2.png",
    "poliza-coche.svg": "https://www.lineadirecta.com/documents/20119/45989/poliza-coche.svg/8fcb9619-ab7d-9252-7939-b14330e543b4?t=1687254183837",
    "poliza-moto.svg": "https://www.lineadirecta.com/documents/20119/45989/poliza-moto.svg/6cc3f9e6-c753-4ace-c999-41eddf157d18?t=1738928272144",
    "poliza-hogar.svg": "https://www.lineadirecta.com/documents/20119/45989/poliza-hogar.svg/23e435b4-dba3-9198-2d68-53068607d486?t=1687254183837",
    "poliza-salud.svg": "https://www.lineadirecta.com/documents/20119/325236/poliza-salud.svg/931cc119-1b7f-bcb4-af48-221d67b8f270?t=1693990714824",
    "poliza-movilidad.svg": "https://www.lineadirecta.com/documents/20119/107668/poliza-movilidad.svg/146457c7-488b-51c7-bb7c-a48323a779e2?t=1706697396738"
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for fname, u in urls.items():
    dest = os.path.join(ASSETS_DIR, fname)
    req = urllib.request.Request(u, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp, open(dest, "wb") as f_out:
            f_out.write(resp.read())
        print(f"[+] Descargado: {fname} ({os.path.getsize(dest)} bytes)")
    except Exception as e:
        print(f"[-] Error descargando {fname}: {e}")

print("[OK] Descarga de assets finalizada.")
