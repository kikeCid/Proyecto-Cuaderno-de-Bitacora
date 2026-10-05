#!/usr/bin/env python3
"""
Generador de PDF Export Estático — Proyecto Evolución HCM Cloud
================================================================
Este script lee todas las páginas HTML del proyecto HCM y genera
un único archivo HTML autónomo (export_estatico.html) con todo el
contenido embebido, listo para abrir en el navegador y exportar a PDF
sin necesidad de servidor web.

Uso:
    python generar_pdf_export.py

Salida:
    export_estatico.html  ← Ábrelo en Chrome/Edge y pulsa Ctrl+P
"""

import os
import re
from pathlib import Path
from datetime import datetime
from html.parser import HTMLParser

# ─── CONFIGURACIÓN ───────────────────────────────────────────────
BASE_DIR = Path(__file__).parent
FECHA = datetime.now().strftime("%d de %B de %Y")

PAGINAS = [
    {
        "archivo": "universo_estrategico.html",
        "titulo": "Universo Estratégico",
        "descripcion": "Roadmap cronológico del proyecto. Nueve fases desde la obsolescencia hasta la licitación.",
        "seccion": "Fase 1 — Estrategia"
    },
    {
        "archivo": "levantamiento_necesidad.html",
        "titulo": "Levantamiento de Necesidad",
        "descripcion": "Identificación de obsolescencia en PeopleSoft y evaluación de riesgos.",
        "seccion": "Fase 1 — Análisis"
    },
    {
        "archivo": "estrategia_ecosistema.html",
        "titulo": "Decisión de Ecosistema",
        "descripcion": "Análisis macro: Arquitectura Global Unificada vs Best-of-Breed funcionales.",
        "seccion": "Fase 1 — Arquitectura"
    },
    {
        "archivo": "evaluacion_mercado.html",
        "titulo": "Evaluación del Mercado HCM",
        "descripcion": "Estudio de las principales plataformas Cloud HCM del mercado.",
        "seccion": "Fase 2 — Mercado"
    },
    {
        "archivo": "vision_general.html",
        "titulo": "Business Case & Viabilidad",
        "descripcion": "Análisis financiero, comparativa Oracle vs Workday y justificación del TCO.",
        "seccion": "Fase 2 — Financiero"
    },
    {
        "archivo": "rfi_productos.html",
        "titulo": "RFI Productos — Funciones y Licencias",
        "descripcion": "Petición formal a fabricantes sobre alcance funcional y licenciamiento.",
        "seccion": "Fase 3 — RFI"
    },
    {
        "archivo": "rfi_implantacion.html",
        "titulo": "RFI Implantación de Producto",
        "descripcion": "Información a integradores sobre tiempos, modelo y estrategia de despliegue.",
        "seccion": "Fase 3 — RFI"
    },
]

# ─── EXTRACTOR DE CONTENIDO ───────────────────────────────────────
def extraer_contenido(html_text: str) -> str:
    """Extrae el contenido útil del HTML de una página."""

    # Eliminar scripts
    html_text = re.sub(r'<script[^>]*>.*?</script>', '', html_text, flags=re.DOTALL | re.IGNORECASE)

    # Eliminar <style> embebidos
    html_text = re.sub(r'<style[^>]*>.*?</style>', '', html_text, flags=re.DOTALL | re.IGNORECASE)

    # Buscar <main> o .container
    main_match = re.search(r'<main[^>]*>(.*?)</main>', html_text, re.DOTALL | re.IGNORECASE)
    if main_match:
        contenido = main_match.group(1)
    else:
        body_match = re.search(r'<body[^>]*>(.*?)</body>', html_text, re.DOTALL | re.IGNORECASE)
        contenido = body_match.group(1) if body_match else html_text

    # Eliminar elementos no deseados en el contenido
    tags_eliminar = [
        r'<nav[^>]*>.*?</nav>',
        r'<footer[^>]*>.*?</footer>',
        r'<div[^>]*class="[^"]*theme-toggle[^"]*"[^>]*>.*?</div>',
        r'<div[^>]*class="[^"]*bg-mesh[^"]*"[^>]*>.*?</div>',
        r'<button[^>]*class="[^"]*carousel-btn[^"]*"[^>]*>.*?</button>',
        r'<div[^>]*class="[^"]*export-fab[^"]*"[^>]*>.*?</div>',
    ]

    for patron in tags_eliminar:
        contenido = re.sub(patron, '', contenido, flags=re.DOTALL | re.IGNORECASE)

    # Limpiar hrefs que serían inútiles en el PDF
    contenido = re.sub(r' href="[^"]*"', ' href="#"', contenido)

    return contenido.strip()


def leer_titulo_pagina(html_text: str) -> str:
    """Extrae el <title> de la página."""
    match = re.search(r'<title[^>]*>(.*?)</title>', html_text, re.IGNORECASE)
    return match.group(1).strip() if match else "Sin título"


# ─── CONSTRUIR HTML EXPORTADOR ────────────────────────────────────
def construir_pagina_contenido(numero, total, kicker, titulo, contenido, fecha):
    return f'''
    <div class="pdf-page page-content">
        <div class="page-header">
            <div>
                <div class="page-section-label">{kicker}</div>
                <div class="page-section-title">{titulo}</div>
            </div>
            <div class="page-number">Pág. {numero} / {total}</div>
        </div>
        <div class="extracted-content">
{contenido}
        </div>
        <div class="page-footer">
            <div class="page-footer-brand">
                <div class="page-footer-dot"></div>
                Evolución HCM Cloud · Cuaderno de Bitácora
            </div>
            <div class="page-footer-right">{fecha} · Documento Confidencial</div>
        </div>
    </div>
'''


def construir_portada(fecha, num_secciones):
    return f'''
    <div class="pdf-page page-cover">
        <div class="cover-header">
            <div class="cover-logo">
                <div class="cover-logo-dot"></div>
                <div class="cover-logo-text">Cuaderno de Bitácora · Portal de Proyectos</div>
            </div>
            <div class="cover-date">{fecha}</div>
        </div>
        <div class="cover-body">
            <div class="cover-badge">ROADMAP 2026</div>
            <div class="cover-title">Evolución<br><span>HCM Cloud</span></div>
            <div class="cover-description">
                Migración estratégica de PeopleSoft RR.HH. a arquitectura Cloud para digitalizar
                procesos y habilitar capacidades de IA y analítica avanzada. Documento completo
                del proyecto con todas las fases, análisis y evidencias generadas.
            </div>
        </div>
        <div class="cover-meta-bar">
            <div class="cover-meta-item">
                <div class="cover-meta-label">Área</div>
                <div class="cover-meta-value">Recursos Humanos / IT</div>
            </div>
            <div class="cover-meta-item">
                <div class="cover-meta-label">Responsable</div>
                <div class="cover-meta-value">Gestión de Personas & Tecnología</div>
            </div>
            <div class="cover-meta-item">
                <div class="cover-meta-label">Secciones</div>
                <div class="cover-meta-value">{num_secciones} documentos</div>
            </div>
            <div class="cover-meta-item">
                <div class="cover-meta-label">Estado</div>
                <div class="cover-meta-value" style="color:#10B981;">● Activo · En Progreso</div>
            </div>
        </div>
    </div>
'''


def construir_indice(paginas, total, fecha):
    items = ""
    for i, p in enumerate(paginas):
        items += f'''
            <div class="index-item">
                <div class="index-num">{i + 1}</div>
                <div class="index-info">
                    <div class="index-name">{p["titulo"]}</div>
                    <div class="index-desc">{p["descripcion"]}</div>
                </div>
            </div>
'''
    return f'''
    <div class="pdf-page page-index">
        <div class="page-header">
            <div>
                <div class="page-section-label">Índice del Documento</div>
                <div class="page-section-title">Contenido del Proyecto</div>
            </div>
            <div class="page-number">Pág. 2 / {total}</div>
        </div>
        <div class="index-grid">
{items}
        </div>
        <div class="page-footer">
            <div class="page-footer-brand">
                <div class="page-footer-dot"></div>
                Evolución HCM Cloud · Cuaderno de Bitácora
            </div>
            <div class="page-footer-right">{fecha} · Documento Confidencial</div>
        </div>
    </div>
'''


# ─── PLANTILLA CSS COMPLETA ───────────────────────────────────────
CSS = """
    :root {
        --lda-red: #E4002B;
        --hcm-green: #10B981;
        --hcm-green-soft: #ECFDF5;
        --text-main: #111827;
        --text-sec: #4B5563;
        --border: #E5E7EB;
        --bg: #F9FAFB;
        --white: #FFFFFF;
    }

    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
        font-family: 'Inter', Arial, sans-serif;
        background: #D1D5DB;
    }

    /* === PDF CONTROLS === */
    .pdf-controls {
        position: fixed;
        top: 0; left: 0; right: 0;
        height: 64px;
        background: #1a1a2e;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 32px;
        z-index: 100;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    }

    .pdf-controls-left { display: flex; align-items: center; gap: 16px; }

    .pdf-brand-dot { width:10px; height:10px; background:var(--lda-red); border-radius:50%; }
    .pdf-brand-title { color:white; font-size:0.9rem; font-weight:700; }
    .pdf-brand-sub { color:rgba(255,255,255,.4); font-size:0.72rem; }

    .pdf-divider { width:1px; height:32px; background:rgba(255,255,255,.1); }

    .pdf-badge {
        padding: 5px 14px;
        background: rgba(16,185,129,.15);
        border: 1px solid rgba(16,185,129,.3);
        border-radius: 50px;
        color: var(--hcm-green);
        font-size: 0.7rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: .5px;
    }

    .btn-print {
        display: flex; align-items: center; gap: 8px;
        padding: 10px 24px;
        background: var(--lda-red);
        color: white; border: none; border-radius: 50px;
        font-family: inherit; font-size: 0.82rem; font-weight: 700;
        cursor: pointer; letter-spacing: .5px; text-transform: uppercase;
        transition: all .2s;
    }
    .btn-print:hover { background: #c2001f; transform: scale(1.03); }

    .btn-close {
        display: flex; align-items: center; gap: 8px;
        padding: 10px 20px;
        background: rgba(255,255,255,.08);
        color: rgba(255,255,255,.7);
        border: 1px solid rgba(255,255,255,.1);
        border-radius: 50px;
        font-family: inherit; font-size: 0.82rem; font-weight: 600;
        cursor: pointer; transition: all .2s;
    }
    .btn-close:hover { background: rgba(255,255,255,.15); color:white; }

    /* === PDF WRAPPER === */
    .pdf-wrapper {
        padding: 80px 0 40px;
        min-height: 100vh;
    }

    /* === PÁGINAS A4 LANDSCAPE === */
    .pdf-page {
        width: 297mm;
        min-height: 210mm;
        background: white;
        margin: 0 auto 24px;
        box-shadow: 0 8px 32px rgba(0,0,0,.15);
        position: relative;
        overflow: hidden;
        page-break-after: always;
        border-radius: 4px;
        display: flex;
        flex-direction: column;
    }

    /* PORTADA */
    .page-cover {
        background: linear-gradient(135deg, #0a0a0b 0%, #1a1a2e 50%, #0f3460 100%);
        padding: 50px 60px;
        justify-content: space-between;
    }

    .cover-header { display:flex; justify-content:space-between; align-items:flex-start; }
    .cover-logo { display:flex; align-items:center; gap:12px; }
    .cover-logo-dot { width:14px; height:14px; background:var(--lda-red); border-radius:50%; }
    .cover-logo-text { color:rgba(255,255,255,.6); font-size:.72rem; font-weight:700; letter-spacing:2px; text-transform:uppercase; }
    .cover-date { color:rgba(255,255,255,.4); font-size:.72rem; }
    .cover-body { flex:1; display:flex; flex-direction:column; justify-content:center; padding:30px 0; }
    .cover-badge {
        display:inline-block; padding:6px 16px;
        background:rgba(16,185,129,.15); border:1px solid rgba(16,185,129,.4);
        border-radius:50px; color:var(--hcm-green);
        font-size:.72rem; font-weight:800; letter-spacing:2px; text-transform:uppercase;
        margin-bottom:28px; width:fit-content;
    }
    .cover-title { font-size:4rem; font-weight:900; color:white; line-height:1.05; letter-spacing:-2px; margin-bottom:20px; }
    .cover-title span { color:var(--hcm-green); }
    .cover-description { font-size:1.05rem; color:rgba(255,255,255,.6); max-width:580px; line-height:1.7; }
    .cover-meta-bar { display:flex; gap:40px; padding-top:30px; border-top:1px solid rgba(255,255,255,.1); }
    .cover-meta-label { font-size:.62rem; color:rgba(255,255,255,.3); font-weight:700; letter-spacing:1.5px; text-transform:uppercase; margin-bottom:4px; }
    .cover-meta-value { font-size:.88rem; color:rgba(255,255,255,.8); font-weight:600; }

    /* PÁGINAS NORMALES */
    .page-content, .page-index { padding: 40px 60px; }

    .page-header {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        margin-bottom: 28px;
        padding-bottom: 18px;
        border-bottom: 2px solid var(--border);
    }
    .page-section-label { font-size:.62rem; font-weight:800; letter-spacing:2px; text-transform:uppercase; color:var(--hcm-green); }
    .page-section-title { font-size:1.8rem; font-weight:900; color:var(--text-main); letter-spacing:-1px; margin-top:4px; }
    .page-number { font-size:.72rem; color:var(--text-sec); font-weight:600; white-space:nowrap; padding-top:4px; }

    /* INDEX */
    .index-grid { display:grid; grid-template-columns:1fr 1fr; gap:14px; }
    .index-item { display:flex; align-items:center; gap:14px; padding:18px 20px; background:var(--bg); border-radius:12px; border:1px solid var(--border); }
    .index-num { width:34px; height:34px; background:var(--hcm-green); border-radius:50%; color:white; font-size:.82rem; font-weight:800; display:flex; align-items:center; justify-content:center; flex-shrink:0; }
    .index-name { font-size:.9rem; font-weight:700; color:var(--text-main); margin-bottom:2px; }
    .index-desc { font-size:.72rem; color:var(--text-sec); line-height:1.4; }

    /* FOOTER */
    .page-footer {
        display:flex; align-items:center; justify-content:space-between;
        padding:14px 60px; border-top:1px solid var(--border);
        background:#FAFAFA; flex-shrink:0; margin-top:auto;
    }
    .page-footer-brand { display:flex; align-items:center; gap:8px; font-size:.68rem; color:var(--text-sec); font-weight:600; letter-spacing:1px; text-transform:uppercase; }
    .page-footer-dot { width:8px; height:8px; background:var(--lda-red); border-radius:50%; }
    .page-footer-right { font-size:.68rem; color:var(--text-sec); }

    /* === CONTENIDO EXTRAÍDO === */
    .extracted-content {
        font-size: 0.82rem;
        color: var(--text-main);
        line-height: 1.6;
        flex: 1;
        overflow: hidden;
    }

    .extracted-content h1, .extracted-content h2, .extracted-content h3 {
        margin-bottom: 10px;
        margin-top: 18px;
        line-height: 1.2;
        color: var(--text-main);
    }
    .extracted-content h1:first-child, .extracted-content h2:first-child { margin-top: 0; }
    .extracted-content h1 { font-size:1.4rem; font-weight:900; }
    .extracted-content h2 { font-size:1.1rem; font-weight:800; }
    .extracted-content h3 { font-size:.95rem; font-weight:700; }
    .extracted-content p { margin-bottom:8px; color:var(--text-sec); }

    /* Ocultar elementos de navegación */
    .extracted-content nav,
    .extracted-content .global-nav-wrapper,
    .extracted-content .theme-toggle-wrapper,
    .extracted-content .bg-mesh,
    .extracted-content footer,
    .extracted-content .carousel-btn,
    .extracted-content .export-fab { display:none !important; }

    /* Hero compacto */
    .extracted-content .hero {
        padding: 24px 28px !important;
        margin-bottom: 20px !important;
        border-radius: 14px !important;
        border: 1px solid var(--border) !important;
        background: var(--hcm-green-soft) !important;
        box-shadow: none !important;
    }
    .extracted-content .hero h1 { font-size:1.6rem !important; margin-bottom:6px !important; }
    .extracted-content .hero p { font-size:.85rem !important; }
    .extracted-content .hero-badge { font-size:.65rem !important; padding:3px 10px !important; margin-bottom:10px !important; }
    .extracted-content .container { padding:0 !important; max-width:100% !important; }

    /* Carrusel a grid */
    .extracted-content .carousel-container { overflow:visible !important; position:static !important; }
    .extracted-content .carousel-track {
        display:flex !important; flex-wrap:wrap !important;
        overflow:visible !important; gap:10px !important;
    }
    .extracted-content .apple-card {
        flex: 0 0 auto !important;
        width: 148px !important; height: auto !important;
        min-height: 140px !important; padding: 14px !important;
        border-radius: 10px !important; font-size: .75rem !important;
    }
    .extracted-content .apple-card .card-visual { display:none !important; }
    .extracted-content .apple-card .title { font-size:.88rem !important; margin-bottom:4px !important; }
    .extracted-content .apple-card .desc { font-size:.72rem !important; }

    /* Roadmap compacto */
    .extracted-content .roadmap-container { margin: 20px auto !important; }
    .extracted-content .milestone { padding-left: 55px !important; margin-bottom: 14px !important; }
    .extracted-content .milestone-node { width:26px !important; height:26px !important; font-size:.7rem !important; left:14px !important; }
    .extracted-content .milestone-content { padding:12px 16px !important; border-radius:10px !important; }
    .extracted-content .milestone-title { font-size:.85rem !important; }
    .extracted-content .milestone-desc { font-size:.72rem !important; }
    .extracted-content .action-icon { width:26px !important; height:26px !important; }
    .extracted-content .status-badge { font-size:.62rem !important; padding:3px 7px !important; }

    /* Tablas */
    .extracted-content table { width:100%; border-collapse:collapse; font-size:.72rem; margin:10px 0; }
    .extracted-content th, .extracted-content td { border:1px solid var(--border); padding:6px 10px; text-align:left; }
    .extracted-content th { background:var(--hcm-green-soft); font-weight:700; }

    /* Grid/flex genérico */
    .extracted-content [style*="display: grid"] { display:grid !important; }
    .extracted-content [style*="display: flex"] { display:flex !important; flex-wrap:wrap !important; }

    /* === PRINT === */
    @media print {
        @page { size: A4 landscape; margin: 0; }
        body { background: white !important; }
        .pdf-controls { display: none !important; }
        .pdf-wrapper { padding: 0 !important; background: white !important; }
        .pdf-page {
            width: 100% !important; min-height: 100vh !important;
            margin: 0 !important; box-shadow: none !important;
            border-radius: 0 !important;
            page-break-after: always !important; break-after: page !important;
        }
        .pdf-page:last-child { page-break-after: avoid !important; break-after: avoid !important; }
    }
"""


# ─── FUNCIÓN PRINCIPAL ────────────────────────────────────────────
def main():
    print("=" * 60)
    print("  Generador de PDF Export — Evolución HCM Cloud")
    print("=" * 60)
    print()

    total_paginas = len(PAGINAS) + 2  # portada + índice + contenido
    secciones_html = []

    # Portada e índice
    secciones_html.append(construir_portada(FECHA, len(PAGINAS)))
    secciones_html.append(construir_indice(PAGINAS, total_paginas, FECHA))

    # Contenido de cada página
    for i, p in enumerate(PAGINAS):
        ruta = BASE_DIR / p["archivo"]
        num = i + 3

        if not ruta.exists():
            print(f"  ⚠ AVISO: No encontrado → {p['archivo']}")
            secciones_html.append(f'''
    <div class="pdf-page page-content">
        <div class="page-header">
            <div>
                <div class="page-section-label">{p["seccion"]}</div>
                <div class="page-section-title">{p["titulo"]}</div>
            </div>
            <div class="page-number">Pág. {num} / {total_paginas}</div>
        </div>
        <div style="display:flex;align-items:center;justify-content:center;flex:1;padding:40px;">
            <div style="text-align:center;padding:40px;background:#FEF2F2;border-radius:16px;border:1px solid #FECACA;max-width:400px;">
                <div style="font-size:2rem;margin-bottom:16px;">⚠️</div>
                <h3 style="color:#DC2626;margin-bottom:8px;">Archivo no encontrado</h3>
                <p style="color:#6B7280;font-size:0.85rem;">{p["archivo"]}</p>
            </div>
        </div>
        <div class="page-footer">
            <div class="page-footer-brand"><div class="page-footer-dot"></div> Evolución HCM Cloud · Cuaderno de Bitácora</div>
            <div class="page-footer-right">{FECHA} · Documento Confidencial</div>
        </div>
    </div>
''')
            continue

        print(f"  ✓ Procesando ({i+1}/{len(PAGINAS)}): {p['archivo']}")

        try:
            with open(ruta, 'r', encoding='utf-8', errors='replace') as f:
                html = f.read()

            contenido = extraer_contenido(html)
            secciones_html.append(
                construir_pagina_contenido(num, total_paginas, p["seccion"], p["titulo"], contenido, FECHA)
            )
        except Exception as e:
            print(f"    ERROR: {e}")

    # Ensamblar HTML final
    html_final = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Evolución HCM Cloud — Exportación Completa del Proyecto</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800;900&display=swap" rel="stylesheet">
    <style>
{CSS}
    </style>
</head>
<body>

    <!-- BARRA DE CONTROLES -->
    <div class="pdf-controls">
        <div class="pdf-controls-left">
            <div style="display:flex;align-items:center;gap:12px;">
                <div class="pdf-brand-dot"></div>
                <div>
                    <div class="pdf-brand-title">Evolución HCM Cloud</div>
                    <div class="pdf-brand-sub">Documento Completo del Proyecto</div>
                </div>
            </div>
            <div class="pdf-divider"></div>
            <div class="pdf-badge">{len(PAGINAS)} secciones · 2026</div>
        </div>
        <div style="display:flex;align-items:center;gap:12px;">
            <button class="btn-close" onclick="window.history.back()">← Volver</button>
            <button class="btn-print" onclick="window.print()">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16">
                    <polyline points="6 9 6 2 18 2 18 9"></polyline>
                    <path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path>
                    <rect x="6" y="14" width="12" height="8"></rect>
                </svg>
                Imprimir / Guardar PDF
            </button>
        </div>
    </div>

    <!-- PÁGINAS -->
    <div class="pdf-wrapper">
{''.join(secciones_html)}
    </div>

</body>
</html>
"""

    # Guardar
    salida = BASE_DIR / "export_estatico.html"
    with open(salida, 'w', encoding='utf-8') as f:
        f.write(html_final)

    size_kb = salida.stat().st_size // 1024
    print()
    print(f"  ✅ Exportación generada: {salida.name} ({size_kb} KB)")
    print()
    print("  📄 INSTRUCCIONES:")
    print(f"  1. Abre '{salida}' en Chrome o Edge")
    print("  2. Pulsa el botón 'Imprimir / Guardar PDF' o usa Ctrl+P")
    print("  3. En el diálogo, selecciona 'Guardar como PDF'")
    print("  4. Orientación: Horizontal (Landscape) — tamaño A4")
    print()


if __name__ == "__main__":
    main()
