# -*- coding: utf-8 -*-
"""
Script para actualizar los iconos de las tarjetas en todos los subproyectos (Nivel 2)
con iconografía vectorial duotono profesional (64x64).
"""
import os
import re

BASE_DIR = r"C:\Proyectos_Claude\Proyecto Cuaderno de Bitacora\01_Proyectos"

# SVGs duotono para HCM
SVG_HCM_CRONOGRAMA = '''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="14" y="16" width="36" height="36" rx="6" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.12"/>
    <line x1="14" y1="26" x2="50" y2="26" stroke="currentColor" stroke-width="2"/>
    <line x1="24" y1="12" x2="24" y2="18" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>
    <line x1="40" y1="12" x2="40" y2="18" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>
    <!-- Líneas de Gantt e hitos -->
    <rect x="20" y="32" width="12" height="4" rx="2" fill="currentColor"/>
    <rect x="26" y="40" width="16" height="4" rx="2" fill="currentColor" fill-opacity="0.5"/>
</svg>'''

SVG_HCM_ESTRATEGIA = '''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M16 48L28 34L36 40L48 24" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M40 24H48V32" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M14 52H50" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
    <circle cx="28" cy="34" r="3" fill="currentColor"/>
    <circle cx="36" cy="40" r="3" fill="currentColor"/>
    <circle cx="48" cy="24" r="3" fill="currentColor"/>
    <path d="M16 48L28 34L36 40L48 24V48H16Z" fill="currentColor" fill-opacity="0.10"/>
</svg>'''

SVG_HCM_EJECUCION = '''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M32 12C32 12 44 20 44 36L38 42L32 40L26 42L20 36C20 20 32 12 32 12Z" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round" fill="currentColor" fill-opacity="0.14"/>
    <circle cx="32" cy="28" r="4" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.3"/>
    <path d="M20 36L14 42V48L22 45L26 42" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/>
    <path d="M44 36L50 42V48L42 45L38 42" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/>
    <path d="M32 46V54M28 50L32 54L36 50" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''

SVG_HCM_CONEXION = '''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
    <circle cx="32" cy="32" r="8" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.2"/>
    <circle cx="16" cy="20" r="5" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.12"/>
    <circle cx="48" cy="20" r="5" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.12"/>
    <circle cx="16" cy="44" r="5" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.12"/>
    <circle cx="48" cy="44" r="5" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.12"/>
    <line x1="20" y1="23" x2="26" y2="28" stroke="currentColor" stroke-width="2"/>
    <line x1="44" y1="23" x2="38" y2="28" stroke="currentColor" stroke-width="2"/>
    <line x1="20" y1="41" x2="26" y2="36" stroke="currentColor" stroke-width="2"/>
    <line x1="44" y1="41" x2="38" y2="36" stroke="currentColor" stroke-width="2"/>
</svg>'''

SVG_HCM_PERSONAS = '''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
    <circle cx="32" cy="24" r="6" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.2"/>
    <path d="M20 44C20 37.3726 25.3726 32 32 32C38.6274 32 44 37.3726 44 44" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>
    <circle cx="46" cy="28" r="4.5" stroke="currentColor" stroke-width="1.8" fill="currentColor" fill-opacity="0.1"/>
    <path d="M42 46C43.5 42 46.5 40 50 40C51.5 40 53 41 54 42" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
    <circle cx="18" cy="28" r="4.5" stroke="currentColor" stroke-width="1.8" fill="currentColor" fill-opacity="0.1"/>
    <path d="M22 46C20.5 42 17.5 40 14 40C12.5 40 11 41 10 42" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
</svg>'''

# SVGs duotono para CRM Operacional
SVG_CRM_CONTEXTO = '''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="14" y="14" width="36" height="36" rx="5" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.10"/>
    <line x1="14" y1="26" x2="50" y2="26" stroke="currentColor" stroke-width="2"/>
    <rect x="20" y="32" width="10" height="12" rx="2" stroke="currentColor" stroke-width="1.8"/>
    <path d="M35 34H44M35 40H42" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
</svg>'''

SVG_CRM_ADJUDICACION = '''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M20 18H44V32C44 38.6274 38.6274 44 32 44C25.3726 44 20 38.6274 20 32V18Z" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.14"/>
    <path d="M20 22H15C13.8954 22 13 22.8954 13 24V28C13 31.3137 15.6863 34 19 34H20" stroke="currentColor" stroke-width="2"/>
    <path d="M44 22H49C50.1046 22 51 22.8954 51 24V28C51 31.3137 48.3137 34 45 34H44" stroke="currentColor" stroke-width="2"/>
    <path d="M32 44V50M24 50H40" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>
    <path d="M27 30L30.5 33.5L37 27" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''

SVG_CRM_GOBIERNO = '''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="14" y="16" width="36" height="34" rx="4" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.10"/>
    <line x1="26" y1="16" x2="26" y2="50" stroke="currentColor" stroke-width="1.8"/>
    <line x1="38" y1="16" x2="38" y2="50" stroke="currentColor" stroke-width="1.8"/>
    <rect x="18" y="22" width="5" height="8" rx="1.5" fill="currentColor"/>
    <rect x="30" y="28" width="5" height="12" rx="1.5" fill="currentColor"/>
    <rect x="42" y="20" width="5" height="16" rx="1.5" fill="currentColor"/>
</svg>'''

# SVGs duotono para Perseo
SVG_PERSEO_VISION = '''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
    <circle cx="32" cy="32" r="18" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.08"/>
    <circle cx="32" cy="32" r="10" stroke="currentColor" stroke-width="2" stroke-dasharray="4 2"/>
    <circle cx="32" cy="32" r="3.5" fill="currentColor"/>
    <line x1="32" y1="10" x2="32" y2="16" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>
    <line x1="32" y1="48" x2="32" y2="54" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>
    <line x1="10" y1="32" x2="16" y2="32" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>
    <line x1="48" y1="32" x2="54" y2="32" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>
</svg>'''

SVG_PERSEO_RRLL = '''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M32 12L47 18V31C47 41.5 40.5 49 32 52C23.5 49 17 41.5 17 31V18L32 12Z" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round" fill="currentColor" fill-opacity="0.12"/>
    <circle cx="32" cy="27" r="4.5" stroke="currentColor" stroke-width="2"/>
    <path d="M25 41C25 37 28.5 35 32 35C35.5 35 39 37 39 41" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
</svg>'''

SVG_PERSEO_COACHING = '''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M16 48V42M26 48V34M36 48V26M46 48V18" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>
    <path d="M18 36L28 28L36 32L46 16" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M40 16H46V22" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''

SVG_PERSEO_ROLES = '''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="14" y="14" width="36" height="36" rx="5" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.10"/>
    <line x1="14" y1="26" x2="50" y2="26" stroke="currentColor" stroke-width="2"/>
    <line x1="28" y1="26" x2="28" y2="50" stroke="currentColor" stroke-width="1.8"/>
    <rect x="18" y="31" width="6" height="5" rx="1.5" fill="currentColor"/>
    <rect x="33" y="31" width="12" height="5" rx="1.5" fill="currentColor" fill-opacity="0.5"/>
    <rect x="33" y="40" width="8" height="4" rx="1" fill="currentColor" fill-opacity="0.5"/>
</svg>'''

SVG_PERSEO_CASOS = '''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
    <circle cx="32" cy="32" r="18" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.08"/>
    <circle cx="32" cy="32" r="11" stroke="currentColor" stroke-width="1.8"/>
    <circle cx="32" cy="32" r="4" fill="currentColor"/>
    <line x1="32" y1="32" x2="45" y2="20" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>
    <circle cx="42" cy="23" r="2.5" fill="currentColor"/>
</svg>'''

# SVGs duotono para Gestión de Usuarios
SVG_GUS_ARQUITECTURA = '''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="15" y="15" width="34" height="14" rx="3" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.12"/>
    <rect x="15" y="35" width="34" height="14" rx="3" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.12"/>
    <circle cx="22" cy="22" r="2" fill="currentColor"/>
    <circle cx="28" cy="22" r="2" fill="currentColor"/>
    <circle cx="22" cy="42" r="2" fill="currentColor"/>
    <circle cx="28" cy="42" r="2" fill="currentColor"/>
    <line x1="32" y1="29" x2="32" y2="35" stroke="currentColor" stroke-width="2"/>
</svg>'''

SVG_GUS_FLUJOS = '''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
    <circle cx="20" cy="24" r="5" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.15"/>
    <rect x="36" y="20" width="14" height="8" rx="2" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.15"/>
    <circle cx="32" cy="44" r="5" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.15"/>
    <path d="M25 24H36" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
    <path d="M43 28V36L37 42" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''

SVG_GUS_INTEGRACIONES = '''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M22 24H16C14.8954 24 14 24.8954 14 26V38C14 39.1046 14.8954 40 16 40H22" stroke="currentColor" stroke-width="2.2"/>
    <path d="M42 24H48C49.1046 24 50 24.8954 50 26V38C50 39.1046 49.1046 40 48 40H42" stroke="currentColor" stroke-width="2.2"/>
    <line x1="22" y1="28" x2="30" y2="28" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
    <line x1="22" y1="36" x2="30" y2="36" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
    <line x1="34" y1="28" x2="42" y2="28" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
    <line x1="34" y1="36" x2="42" y2="36" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
    <circle cx="32" cy="32" r="3" fill="currentColor"/>
</svg>'''

# SVGs duotono para Gobierno de Información
SVG_GIN_LIDIA_HUB = '''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M32 12C20.9543 12 12 20.9543 12 32C12 43.0457 20.9543 52 32 52C43.0457 52 52 43.0457 52 32C52 20.9543 43.0457 12 32 12Z" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.08"/>
    <circle cx="32" cy="32" r="8" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.25"/>
    <circle cx="32" cy="19" r="3" fill="currentColor"/>
    <circle cx="32" cy="45" r="3" fill="currentColor"/>
    <circle cx="19" cy="32" r="3" fill="currentColor"/>
    <circle cx="45" cy="32" r="3" fill="currentColor"/>
    <line x1="32" y1="22" x2="32" y2="24" stroke="currentColor" stroke-width="2"/>
    <line x1="32" y1="40" x2="32" y2="42" stroke="currentColor" stroke-width="2"/>
    <line x1="22" y1="32" x2="24" y2="32" stroke="currentColor" stroke-width="2"/>
    <line x1="40" y1="32" x2="42" y2="32" stroke="currentColor" stroke-width="2"/>
</svg>'''

SVG_GIN_MARCO = '''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M18 14H46V46L32 39L18 46V14Z" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round" fill="currentColor" fill-opacity="0.14"/>
    <line x1="24" y1="22" x2="40" y2="22" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
    <line x1="24" y1="28" x2="36" y2="28" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
</svg>'''

# SVGs duotono para Telefonía Genesys CX
SVG_TEL_ESTADO = '''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="14" y="16" width="36" height="34" rx="4" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.12"/>
    <line x1="14" y1="26" x2="50" y2="26" stroke="currentColor" stroke-width="2"/>
    <circle cx="20" cy="21" r="2" fill="currentColor"/>
    <circle cx="26" cy="21" r="2" fill="currentColor"/>
    <path d="M22 34H36M22 40H42" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
</svg>'''

SVG_TEL_ROADMAP = '''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
    <line x1="20" y1="14" x2="20" y2="50" stroke="currentColor" stroke-width="2.2"/>
    <circle cx="20" cy="20" r="4" stroke="currentColor" stroke-width="2" fill="currentColor"/>
    <circle cx="20" cy="34" r="4" stroke="currentColor" stroke-width="2" fill="currentColor"/>
    <circle cx="20" cy="46" r="4" stroke="currentColor" stroke-width="2" fill="currentColor"/>
    <path d="M26 20H44M26 34H38M26 46H48" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>
</svg>'''


def replace_card_visual_svg(content, card_identifier, new_svg):
    """Reemplaza el svg dentro del card-visual para una tarjeta específica."""
    card_idx = content.find(card_identifier)
    if card_idx == -1:
        print(f"[-] Identificador no encontrado: {card_identifier}")
        return content

    visual_idx = content.find('class="card-visual"', card_idx)
    if visual_idx == -1 or visual_idx > card_idx + 1200:
        print(f"[-] card-visual no encontrado para: {card_identifier}")
        return content

    svg_start = content.find('<svg', visual_idx)
    svg_end = content.find('</svg>', svg_start)
    if svg_start == -1 or svg_end == -1:
        print(f"[-] SVG tag no encontrado para: {card_identifier}")
        return content
    svg_end += len('</svg>')

    return content[:svg_start] + new_svg + content[svg_end:]


# 1. ACTUALIZAR HCM/index.html
hcm_path = os.path.join(BASE_DIR, "HCM", "index.html")
if os.path.exists(hcm_path):
    with open(hcm_path, 'r', encoding='utf-8') as f:
        c = f.read()
    c = replace_card_visual_svg(c, 'cronograma.html', SVG_HCM_CRONOGRAMA)
    c = replace_card_visual_svg(c, 'universo_estrategico.html', SVG_HCM_ESTRATEGIA)
    c = replace_card_visual_svg(c, 'Universo de <span>Ejecución</span>', SVG_HCM_EJECUCION)
    c = replace_card_visual_svg(c, 'Universo de <span>Conexión</span>', SVG_HCM_CONEXION)
    c = replace_card_visual_svg(c, 'Universo de <span>Personas</span>', SVG_HCM_PERSONAS)
    with open(hcm_path, 'w', encoding='utf-8') as f:
        f.write(c)
    print("[+] HCM/index.html actualizado")

# 2. ACTUALIZAR CRM Operacional/index.html
crm_path = os.path.join(BASE_DIR, "CRM Operacional", "index.html")
if os.path.exists(crm_path):
    with open(crm_path, 'r', encoding='utf-8') as f:
        c = f.read()
    c = replace_card_visual_svg(c, 'contexto_proyecto.html', SVG_CRM_CONTEXTO)
    c = replace_card_visual_svg(c, 'hub_licitacion.html', SVG_CRM_ADJUDICACION)
    c = replace_card_visual_svg(c, 'Metodología y <span>Gobierno</span>', SVG_CRM_GOBIERNO)
    with open(crm_path, 'w', encoding='utf-8') as f:
        f.write(c)
    print("[+] CRM Operacional/index.html actualizado")

# 3. ACTUALIZAR Perseo/index.html
perseo_path = os.path.join(BASE_DIR, "Perseo", "index.html")
if os.path.exists(perseo_path):
    with open(perseo_path, 'r', encoding='utf-8') as f:
        c = f.read()
    c = replace_card_visual_svg(c, 'vision_objetivos.html', SVG_PERSEO_VISION)
    c = replace_card_visual_svg(c, 'gestion_rrll.html', SVG_PERSEO_RRLL)
    c = replace_card_visual_svg(c, 'planes_coaching.html', SVG_PERSEO_COACHING)
    c = replace_card_visual_svg(c, 'roles_dashboard.html', SVG_PERSEO_ROLES)
    c = replace_card_visual_svg(c, 'casos_uso.html', SVG_PERSEO_CASOS)
    with open(perseo_path, 'w', encoding='utf-8') as f:
        f.write(c)
    print("[+] Perseo/index.html actualizado")

# 4. ACTUALIZAR Gestion de Usuarios/index.html
gus_path = os.path.join(BASE_DIR, "Gestion de Usuarios", "index.html")
if os.path.exists(gus_path):
    with open(gus_path, 'r', encoding='utf-8') as f:
        c = f.read()
    c = replace_card_visual_svg(c, 'arquitectura_gus.html', SVG_GUS_ARQUITECTURA)
    c = replace_card_visual_svg(c, 'sistema_contratacion_gus.html', SVG_GUS_FLUJOS)
    c = replace_card_visual_svg(c, 'integraciones_gus.html', SVG_GUS_INTEGRACIONES)
    with open(gus_path, 'w', encoding='utf-8') as f:
        f.write(c)
    print("[+] Gestion de Usuarios/index.html actualizado")

# 5. ACTUALIZAR Gobierno de Informacion/index.html
gin_path = os.path.join(BASE_DIR, "Gobierno de Informacion", "index.html")
if os.path.exists(gin_path):
    with open(gin_path, 'r', encoding='utf-8') as f:
        c = f.read()
    c = replace_card_visual_svg(c, 'hub_lidia.html', SVG_GIN_LIDIA_HUB)
    c = replace_card_visual_svg(c, 'hub_gin.html', SVG_GIN_MARCO)
    with open(gin_path, 'w', encoding='utf-8') as f:
        f.write(c)
    print("[+] Gobierno de Informacion/index.html actualizado")

# 6. ACTUALIZAR Telefonia - Genesis CX/index.html
tel_path = os.path.join(BASE_DIR, "Telefonia - Genesis CX", "index.html")
if os.path.exists(tel_path):
    with open(tel_path, 'r', encoding='utf-8') as f:
        c = f.read()
    c = replace_card_visual_svg(c, 'contexto_proyecto.html', SVG_TEL_ESTADO)
    c = replace_card_visual_svg(c, 'roadmap.html', SVG_TEL_ROADMAP)
    with open(tel_path, 'w', encoding='utf-8') as f:
        f.write(c)
    print("[+] Telefonia - Genesis CX/index.html actualizado")

print("\n[OK] Todos los subproyectos actualizados exitosamente con SVGs duotono.")
