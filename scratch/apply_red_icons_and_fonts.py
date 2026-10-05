# -*- coding: utf-8 -*-
"""
Script maestro para:
1. Declarar @font-face con los archivos locales descargados de Línea Directa:
   - CircularXXSub-Light.woff2
   - CircularXXSub-Book.woff2
   - CircularXXSub-Medium.woff2
2. Forzar que TODOS los iconos de las tarjetas sean de LÍNEAS ROJAS CORPORATIVAS (#CC3333 / var(--lda-red)).
   Cero amarillos, azules o morados en los iconos.
3. Actualizar el icono de CRM Operacional con el vector oficial gestion-poliza-1.svg de Línea Directa (expediente y trazabilidad del asegurado).
4. Recompilar bitacora-core.css y styles_bitacora.css.
5. Ejecutar la auditoría de enlaces.
"""

import os
import re
import subprocess

BASE_DIR = r"C:\Proyectos_Claude\Proyecto Cuaderno de Bitacora"
INDEX_HTML = os.path.join(BASE_DIR, "01_Proyectos", "Cuaderno de Bitacora (Proyectos)", "index.html")
CORE_BUILDER = os.path.join(BASE_DIR, "scratch", "build_unified_core_css.py")
ASSETS_DIR = os.path.join(BASE_DIR, "01_Proyectos", "assets")

# ==============================================================================
# 1. ACTUALIZAR SVG DE CRM OPERACIONAL (gestion-poliza-1.svg oficial)
# ==============================================================================
print("[1/3] Actualizando iconografía en index.html a líneas rojas corporativas y nuevo icono CRM...")

svg_crm_official = """<svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path fill-rule="evenodd" clip-rule="evenodd" d="M4.6 2.5C4.54477 2.5 4.5 2.54477 4.5 2.6V21.4C4.5 21.4552 4.54477 21.5 4.6 21.5H11C11.2761 21.5 11.5 21.7239 11.5 22C11.5 22.2761 11.2761 22.5 11 22.5H4.6C3.99249 22.5 3.5 22.0075 3.5 21.4V2.6C3.5 1.99249 3.99249 1.5 4.6 1.5H16.2515C16.5432 1.5 16.823 1.61589 17.0293 1.82218L20.1778 4.97071C20.3841 5.177 20.5 5.45679 20.5 5.74853V10C20.5 10.2761 20.2761 10.5 20 10.5C19.7239 10.5 19.5 10.2761 19.5 10V6.5H16.6C15.9925 6.5 15.5 6.00751 15.5 5.4V2.5H4.6ZM16.5 2.70711V5.4C16.5 5.45523 16.5448 5.5 16.6 5.5H19.2929L16.5 2.70711ZM7.5 7C7.5 6.72386 7.72386 6.5 8 6.5H12C12.2761 6.5 12.5 6.72386 12.5 7C12.5 7.27614 12.2761 7.5 12 7.5H8C7.72386 7.5 7.5 7.27614 7.5 7ZM7.5 11C7.5 10.7239 7.72386 10.5 8 10.5H16C16.2761 10.5 16.5 10.7239 16.5 11C16.5 11.2761 16.2761 11.5 16 11.5H8C7.72386 11.5 7.5 11.2761 7.5 11ZM7.5 15C7.5 14.7239 7.72386 14.5 8 14.5H11C11.2761 14.5 11.5 14.7239 11.5 15C11.5 15.2761 11.2761 15.5 11 15.5H8C7.72386 15.5 7.5 15.2761 7.5 15ZM20.6464 14.6464C20.8417 14.4512 21.1583 14.4512 21.3536 14.6464C21.5488 14.8417 21.5488 15.1583 21.3536 15.3536L16.3585 20.3486L16.3577 20.3494L16.3558 20.3513L16.3548 20.3523L16.3539 20.3532C16.1586 20.5485 15.8417 20.5488 15.6464 20.3536L13.6464 18.3536C13.4512 18.1583 13.4512 17.8417 13.6464 17.6464C13.8417 17.4512 14.1583 17.4512 14.3536 17.6464L16 19.2929L20.6464 14.6464Z" fill="currentColor"/>
</svg>"""

with open(INDEX_HTML, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Asegurar que TODAS las tarjetas tengan el color de icono en rojo Línea Directa (#CC3333 / var(--lda-red))
html = re.sub(
    r'<div class="card-visual"[^>]*>',
    '<div class="card-visual" style="color: var(--lda-red);">',
    html
)

# 2. Reemplazar el icono de CRM Operacional en index.html
html = re.sub(
    r'(<h3 class="title">CRM Operacional</h3>.*?<div class="card-visual"[^>]*>)\s*<svg[^>]*>.*?</svg>',
    r'\1\n                            ' + svg_crm_official,
    html,
    flags=re.DOTALL
)

with open(INDEX_HTML, "w", encoding="utf-8") as f:
    f.write(html)

print("  [+] index.html actualizado: todos los iconos en rojo corporativo y nuevo icono CRM integrado.")

# ==============================================================================
# 2. INTEGRAR @font-face WOFF2 Y REGLAS DE COLOR EN build_unified_core_css.py
# ==============================================================================
print("[2/3] Integrando @font-face de CircularXX y paleta en build_unified_core_css.py...")

with open(CORE_BUILDER, "r", encoding="utf-8") as f:
    css_builder = f.read()

# Declaraciones oficiales de @font-face de CircularXX
font_face_declarations = """
/* ==========================================================================
   TIPOGRAFÍA OFICIAL CIRCULAR XX (LÍNEA DIRECTA ASEGURADORA)
   ========================================================================== */
@font-face {
    font-family: 'CircularXX';
    src: url('../fonts/CircularXXSub-Light.woff2') format('woff2');
    font-weight: 300;
    font-style: normal;
    font-display: swap;
}

@font-face {
    font-family: 'CircularXX';
    src: url('../fonts/CircularXXSub-Book.woff2') format('woff2');
    font-weight: 400;
    font-style: normal;
    font-display: swap;
}

@font-face {
    font-family: 'CircularXX';
    src: url('../fonts/CircularXXSub-Medium.woff2') format('woff2');
    font-weight: 500;
    font-style: normal;
    font-display: swap;
}

@font-face {
    font-family: 'CircularXX';
    src: url('../fonts/CircularXXSub-Medium.woff2') format('woff2');
    font-weight: 700;
    font-style: normal;
    font-display: swap;
}

/* Forzar que todos los iconos vectoriales de tarjeta sean siempre ROJOS LÍNEA DIRECTA */
.card-visual {
    color: var(--lda-red) !important;
}

.card-visual svg {
    color: var(--lda-red) !important;
    fill: currentColor !important;
}
"""

if "TIPOGRAFÍA OFICIAL CIRCULAR XX" in css_builder:
    css_builder = re.sub(
        r'/\* =+\s*TIPOGRAFÍA OFICIAL CIRCULAR XX.*?\.card-visual svg\s*\{[^}]*\}\s*',
        font_face_declarations.strip() + '\n',
        css_builder,
        flags=re.DOTALL
    )
else:
    css_builder = css_builder.replace(
        '"""\n\nfull_core_css = base_css.strip()',
        '\n' + font_face_declarations + '\n"""\n\nfull_core_css = base_css.strip()'
    )

with open(CORE_BUILDER, "w", encoding="utf-8") as f:
    f.write(css_builder)

# Recompilar CSS unificado
subprocess.run(["python", CORE_BUILDER], check=True)
print("  [+] bitacora-core.css y styles_bitacora.css compilados con @font-face CircularXX y reglas de color rojo.")

# ==============================================================================
# 3. AUDITORÍA FINAL
# ==============================================================================
print("[3/3] Ejecutando auditoría de referencias...")
audit_script = os.path.join(BASE_DIR, "scratch", "audit_project.py")
subprocess.run(["python", audit_script], check=True)

print("[OK] ¡Líneas rojas en todos los iconos, fuente oficial CircularXX y nuevo icono CRM aplicados con éxito!")
