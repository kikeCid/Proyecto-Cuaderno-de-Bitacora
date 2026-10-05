# -*- coding: utf-8 -*-
import urllib.request
import os

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
base_url = 'https://www.lineadirecta.com'

icons_to_fetch = {
    'taller.svg': '/documents/d/guest/taller?imagePreview=1',
    'taller-colaboradores.svg': '/documents/d/guest/taller-colaboradores?imagePreview=1',
    'asistencias-informatica.svg': '/documents/d/guest/asistencias-informatica?imagePreview=1',
    'asistencia-viaje-personas.svg': '/documents/d/guest/asistencia-viaje-personas?imagePreview=1',
    'poliza-otros-seguros-1.svg': '/documents/d/guest/poliza-otros-seguros-1?imagePreview=1',
}

for name, rel_url in icons_to_fetch.items():
    u = base_url + rel_url
    dest = os.path.join("scratch", name)
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req) as resp, open(dest, "wb") as f_out:
            data = resp.read()
            f_out.write(data)
        print(f"[+] Descargado {name}: {len(data)} bytes, tipo: {data[:60]}")
    except Exception as e:
        print(f"[-] Error en {name}: {e}")
