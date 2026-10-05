# -*- coding: utf-8 -*-
"""
Script de calibración geométrica y ritmo vertical:
1. Eliminar el salto gigante de 145px entre el menú flotante y el banner Hero (reducido a 26-28px simétrico).
2. Armonizar el Hero: compactar padding interno (30px), centrar y unificar badges de cabecera.
3. Conectar la barra de filtros (.view-controls-bar) de forma fluida con el Hero (20px).
4. Unificar el espaciado entre todas las secciones del portfolio (38px simétrico), eliminando saltos dispares inline (50px/60px/110px).
5. Compactar las cabeceras de sección (.section-header) a 12px 20px de padding y margin-bottom 16px.
6. Calibrar la separación hacia el Footer a 36px.
7. Recompilar bitacora-core.css y styles_bitacora.css.
"""

import os
import re
import subprocess

BASE_DIR = r"C:\Proyectos_Claude\Proyecto Cuaderno de Bitacora"
INDEX_HTML = os.path.join(BASE_DIR, "01_Proyectos", "Cuaderno de Bitacora (Proyectos)", "index.html")
CORE_BUILDER = os.path.join(BASE_DIR, "scratch", "build_unified_core_css.py")

# ==============================================================================
# 1. ACTUALIZAR HTML index.html
# ==============================================================================
print("[1/3] Actualizando clases y estilos inline en index.html...")

with open(INDEX_HTML, "r", encoding="utf-8") as f:
    html = f.read()

# 1.1 Asegurar que <main class="container"> incluya la clase home-container
html = re.sub(
    r'<main\s+class="container(?!\s+home-container)"\s+id="main-content">',
    '<main class="container home-container" id="main-content">',
    html
)

# 1.2 Eliminar estilos inline arbitrarios de margin-top en secciones
html = re.sub(
    r'<section\s+id="seccion-facilitadores"\s+class="portfolio-section"\s+data-category="facilitator"\s+style="margin-top:\s*50px;"',
    '<section id="seccion-facilitadores" class="portfolio-section" data-category="facilitator"',
    html
)

html = re.sub(
    r'<section\s+id="seccion-cerrados"\s+class="portfolio-section"\s+data-category="closed"\s+style="margin-top:\s*50px;"',
    '<section id="seccion-cerrados" class="portfolio-section" data-category="closed"',
    html
)

# 1.3 Calibrar el bloque explicativo de facilitadores
html = re.sub(
    r'<div\s+class="portfolio-section"\s+data-category="facilitator"\s+style="max-width:\s*1200px;\s*margin:\s*0\s+auto\s+50px\s+auto;[^"]*"',
    '<div class="portfolio-section facilitator-callout" data-category="facilitator" style="max-width: 1200px; margin: 20px auto 0 auto; background: var(--bg-card); border-left: 4px solid var(--lda-red); padding: 18px 24px; border-radius: 16px; box-shadow: var(--shadow); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); border: 1px solid var(--glass-border); border-left-width: 4px; border-left-color: var(--lda-red);"',
    html
)

with open(INDEX_HTML, "w", encoding="utf-8") as f:
    f.write(html)

print("  [+] index.html actualizado con home-container y secciones normalizadas.")

# ==============================================================================
# 2. ACTUALIZAR build_unified_core_css.py CON REGLAS DE RITMO Y ESPACIADO
# ==============================================================================
print("[2/3] Integrando calibración matemática de espacios en build_unified_core_css.py...")

with open(CORE_BUILDER, "r", encoding="utf-8") as f:
    css_builder = f.read()

# Bloque maestro de calibración de espacios
spacing_calibration_block = """
/* ==========================================================================
   CALIBRACIÓN MAESTRA DE ESPACIOS Y RITMO VERTICAL (UI/UX DE ÉLITE)
   ========================================================================== */

/* 1. Header flotante: margen superior e inferior equilibrado */
.app-header-island {
    margin: 8px auto 12px auto !important;
}

/* 2. Contenedor Home: elimina el padding excesivo de 120px */
.container.home-container {
    padding-top: 14px !important;
    padding-bottom: 24px !important;
}

/* 3. Hero compacto y elegante */
.hero {
    text-align: center;
    margin-bottom: 20px !important;
    padding: 28px 24px 24px 24px !important;
    background: var(--bg-card);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid var(--glass-border);
    border-radius: 24px !important;
    box-shadow: var(--shadow);
}

.hero-top-badges {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    margin-bottom: 12px !important;
    flex-wrap: wrap;
}

.hero-top-badges .hero-badge {
    margin-bottom: 0 !important;
}

.hero-top-badges .hero-badge-local {
    margin-bottom: 0 !important;
    margin-left: 0 !important;
}

.hero h1 {
    font-size: 2.5rem !important;
    font-weight: 800;
    line-height: 1.1 !important;
    margin-bottom: 10px !important;
    letter-spacing: -0.02em;
}

.hero p {
    font-size: 0.95rem !important;
    line-height: 1.5 !important;
    max-width: 620px !important;
    margin: 0 auto !important;
    color: var(--text-sec);
}

/* 4. Centro de Control de Filtros (Segmented Bar) */
.view-controls-bar {
    max-width: 1200px;
    margin: 0 auto 24px auto !important;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 12px;
    padding: 6px 12px !important;
    background: var(--bg-card);
    border: 1px solid var(--glass-border);
    border-radius: 18px !important;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.03);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    scroll-margin-top: 75px !important;
}

/* 5. Cadencia y ritmo vertical entre Secciones */
.portfolio-section {
    margin-top: 36px !important;
    margin-bottom: 0 !important;
    transition: opacity 0.3s ease, transform 0.3s ease;
}

.portfolio-section:first-of-type {
    margin-top: 0 !important;
}

.section-header {
    display: flex;
    align-items: center;
    gap: 16px;
    margin: 0 0 16px 0 !important;
    padding: 12px 20px !important;
    background: var(--bg-card);
    border-radius: 14px !important;
    border: 1px solid var(--glass-border);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.02);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    scroll-margin-top: 75px !important;
}

.section-title {
    font-size: 1.25rem !important;
    margin: 0 !important;
}

.section-subtitle {
    font-size: 0.84rem !important;
    margin: 2px 0 0 0 !important;
}

/* 6. Pistas de carrusel y tarjetas equilibradas */
.carousel-container {
    position: relative;
    margin: 0 auto !important;
}

.carousel-track {
    display: flex;
    gap: 18px !important;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    scroll-behavior: smooth;
    padding: 6px 4px 16px 4px !important;
    scrollbar-width: none;
    -ms-overflow-style: none;
}

.apple-card {
    height: 430px !important;
    padding: 22px 20px 18px 20px !important;
    border-radius: 20px !important;
}

.apple-card .kicker {
    margin-bottom: 6px !important;
}

.apple-card .title {
    font-size: 1.22rem !important;
    margin-bottom: 6px !important;
}

.apple-card .desc {
    font-size: 0.85rem !important;
    line-height: 1.42 !important;
    margin-bottom: 8px !important;
}

.card-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 5px !important;
    margin: 2px 0 10px 0 !important;
    position: relative;
    z-index: 2;
}

.card-visual {
    flex: 0 0 125px !important;
    height: 125px !important;
    width: 100% !important;
    margin-top: auto !important;
    border-radius: 14px !important;
}

/* 7. Footer compacto con respiro simétrico */
.app-footer {
    margin-top: 38px !important;
    padding: 42px 20px 28px !important;
}

.footer-inner {
    gap: 26px !important;
}

.footer-brand-block {
    padding-bottom: 18px !important;
}
"""

# Inyectar el bloque antes de las comillas triples de clean_addons_css
if "CALIBRACIÓN MAESTRA DE ESPACIOS Y RITMO VERTICAL" in css_builder:
    # Reemplazarlo si ya existía
    css_builder = re.sub(
        r'/\* =+\s*CALIBRACIÓN MAESTRA DE ESPACIOS.*?\.footer-brand-block\s*\{[^}]*\}\s*',
        spacing_calibration_block.strip() + '\n',
        css_builder,
        flags=re.DOTALL
    )
else:
    css_builder = css_builder.replace(
        '"""\n\nfull_core_css = base_css.strip()',
        '\n' + spacing_calibration_block + '\n"""\n\nfull_core_css = base_css.strip()'
    )

with open(CORE_BUILDER, "w", encoding="utf-8") as f:
    f.write(css_builder)

# Recompilar CSS
subprocess.run(["python", CORE_BUILDER], check=True)
print("  [+] build_unified_core_css.py y estilos compilados exitosamente.")

# ==============================================================================
# 3. AUDITORÍA FINAL DE REFERENCIAS
# ==============================================================================
print("[3/3] Ejecutando auditoría de referencias...")
audit_script = os.path.join(BASE_DIR, "scratch", "audit_project.py")
subprocess.run(["python", audit_script], check=True)

print("[OK] ¡Calibración de Espacios y Ritmo Vertical Completada con Éxito!")
