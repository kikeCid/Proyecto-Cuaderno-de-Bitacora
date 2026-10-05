# -*- coding: utf-8 -*-
import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

# Buscar en lineadirecta.com enlaces a iconos de area de clientes, login, etc.
with open("scratch/lineadirecta_home.html", "r", encoding="utf-8") as f:
    text = f.read()

imgs = re.findall(r'src=[\'"]([^\'"]*(?:client|user|login|area|perfil|acceso|seguro|gest|poliza)[^\'"]*)[\'"]', text, re.I)
print("Icons in lineadirecta_home.html:")
for img in set(imgs):
    print(" ", img)
