# -*- coding: utf-8 -*-
"""
Script de Transformación Visual Integral - Nivel Estudio de Diseño (Idital / Stripe / Linear tier)
1. Inserta las reglas de Smart Auto-Hide, Hero Cockpit, Executive Cards, Pipelines y Spotlight dentro de addons en build_unified_core_css.py.
2. Recompila bitacora-core.css y styles_bitacora.css.
3. Actualiza index.html con Hero Cockpit (4 KPIs), las 11 Executive Cards enriquecidas y los scripts reactivos de Spotlight y Smart Auto-Hide.
"""

import os
import re
import subprocess

BASE_DIR = r"C:\Proyectos_Claude\Proyecto Cuaderno de Bitacora"
CORE_PY = os.path.join(BASE_DIR, "scratch", "build_unified_core_css.py")
INDEX_HTML = os.path.join(BASE_DIR, "01_Proyectos", "Cuaderno de Bitacora (Proyectos)", "index.html")

# ==============================================================================
# 1. LIMPIAR Y REPARAR build_unified_core_css.py
# ==============================================================================
with open(CORE_PY, "r", encoding="utf-8") as f:
    py_text = f.read()

# Cortamos cualquier contenido agregado indebidamente después de print(styles_bitacora...)
cut_marker = 'print(f"[+] styles_bitacora.css sincronizado con éxito ({len(full_core_css.splitlines())} líneas)")'
if cut_marker in py_text:
    idx = py_text.find(cut_marker) + len(cut_marker)
    py_text = py_text[:idx].strip() + "\n"

extra_css_block = """
/* ==========================================================================
   SMART AUTO-HIDE TOPBAR (SAFARI / LINEAR STYLE)
   ========================================================================== */
.app-header-island.header-hidden {
    transform: translateY(-130%) !important;
    opacity: 0 !important;
    pointer-events: none !important;
}

/* ==========================================================================
   HERO COCKPIT & KPI GRID (PANEL DE MANDO EJECUTIVO)
   ========================================================================== */
.hero {
    position: relative;
    overflow: hidden;
    background: var(--bg-card);
    border: 1px solid var(--glass-border);
    border-radius: 36px;
    padding: 44px 40px 36px 40px;
    box-shadow: var(--shadow);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
}

.hero::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-image: radial-gradient(rgba(0, 0, 0, 0.06) 1px, transparent 1px);
    background-size: 24px 24px;
    opacity: 0.6;
    pointer-events: none;
}

[data-theme="dark"] .hero::before {
    background-image: radial-gradient(rgba(255, 255, 255, 0.08) 1px, transparent 1px);
    opacity: 0.4;
}

.hero-top-badges {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    flex-wrap: wrap;
    margin-bottom: 20px;
    position: relative;
    z-index: 2;
}

.hero h1 {
    position: relative;
    z-index: 2;
}

.hero p {
    position: relative;
    z-index: 2;
    max-width: 680px;
}

.hero-kpi-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
    margin-top: 36px;
    text-align: left;
    position: relative;
    z-index: 2;
}

@media (max-width: 960px) {
    .hero-kpi-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 520px) {
    .hero-kpi-grid {
        grid-template-columns: 1fr;
    }
}

.kpi-card {
    background: rgba(255, 255, 255, 0.55);
    border: 1px solid var(--glass-border);
    border-radius: 20px;
    padding: 18px 20px;
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    transition: var(--transition);
    position: relative;
    overflow: hidden;
}

[data-theme="dark"] .kpi-card {
    background: rgba(255, 255, 255, 0.035);
    border-color: rgba(255, 255, 255, 0.08);
}

.kpi-card:hover {
    transform: translateY(-3px);
    border-color: var(--lda-red);
    box-shadow: 0 10px 28px rgba(0, 0, 0, 0.08);
}

[data-theme="dark"] .kpi-card:hover {
    box-shadow: 0 12px 32px rgba(0, 0, 0, 0.45);
}

.kpi-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 8px;
}

.kpi-title {
    font-size: 0.74rem;
    font-weight: 700;
    color: var(--text-sec);
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.kpi-badge {
    font-size: 0.62rem;
    font-weight: 800;
    padding: 2px 8px;
    border-radius: 12px;
    letter-spacing: 0.3px;
    text-transform: uppercase;
}

.kpi-badge-green { background: rgba(16, 185, 129, 0.12); color: #10b981; border: 1px solid rgba(16, 185, 129, 0.25); }
.kpi-badge-red { background: rgba(228, 0, 43, 0.12); color: var(--lda-red); border: 1px solid rgba(228, 0, 43, 0.25); }
.kpi-badge-blue { background: rgba(37, 99, 235, 0.12); color: #2563eb; border: 1px solid rgba(37, 99, 235, 0.25); }
.kpi-badge-purple { background: rgba(139, 92, 246, 0.12); color: #8b5cf6; border: 1px solid rgba(139, 92, 246, 0.25); }

.kpi-number {
    font-size: 2.2rem;
    font-weight: 900;
    color: var(--text-main);
    line-height: 1.1;
    letter-spacing: -0.03em;
    font-variant-numeric: tabular-nums;
}

.kpi-desc {
    font-size: 0.74rem;
    color: var(--text-sec);
    margin-top: 6px;
    line-height: 1.35;
}

/* ==========================================================================
   EXECUTIVE CARDS: ANATOMÍA ENRIQUECIDA & SPOTLIGHT MOUSE TRACKING
   ========================================================================== */
.apple-card {
    flex: 0 0 auto;
    width: 335px;
    height: 520px;
    background: var(--bg-card);
    border-radius: 24px;
    padding: 26px 26px 22px 26px;
    scroll-snap-align: start;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.05);
    display: flex;
    flex-direction: column;
    position: relative;
    overflow: hidden;
    cursor: pointer;
    text-decoration: none;
    transition: transform 0.35s cubic-bezier(0.165, 0.84, 0.44, 1),
                box-shadow 0.35s cubic-bezier(0.165, 0.84, 0.44, 1),
                border-color 0.35s ease;
    border: 1px solid var(--glass-border);
}

.apple-card:hover {
    transform: translateY(-6px) scale(1.015);
    box-shadow: 0 20px 48px rgba(0, 0, 0, 0.12);
}

[data-theme="dark"] .apple-card {
    background: rgba(22, 24, 35, 0.75);
    border-color: rgba(255, 255, 255, 0.10);
    box-shadow: 0 10px 32px rgba(0, 0, 0, 0.4);
}

[data-theme="dark"] .apple-card:hover {
    box-shadow: 0 22px 55px rgba(0, 0, 0, 0.7);
    border-color: rgba(255, 255, 255, 0.22);
}

/* Spotlight Glow dinámico al mover el ratón */
.apple-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    border-radius: inherit;
    background: radial-gradient(
        400px circle at var(--mouse-x, -200px) var(--mouse-y, -200px),
        var(--card-spotlight, rgba(228, 0, 43, 0.14)),
        transparent 65%
    );
    opacity: 0;
    transition: opacity 0.3s ease;
    pointer-events: none;
    z-index: 1;
}

.apple-card:hover::before {
    opacity: 1;
}

[data-accent="red"] { --card-spotlight: rgba(228, 0, 43, 0.16); }
[data-accent="amber"] { --card-spotlight: rgba(245, 158, 11, 0.16); }
[data-accent="blue"] { --card-spotlight: rgba(37, 99, 235, 0.16); }
[data-accent="purple"] { --card-spotlight: rgba(139, 92, 246, 0.16); }

[data-theme="dark"] [data-accent="red"] { --card-spotlight: rgba(228, 0, 43, 0.28); }
[data-theme="dark"] [data-accent="amber"] { --card-spotlight: rgba(245, 158, 11, 0.28); }
[data-theme="dark"] [data-accent="blue"] { --card-spotlight: rgba(37, 99, 235, 0.28); }
[data-theme="dark"] [data-accent="purple"] { --card-spotlight: rgba(139, 92, 246, 0.28); }

/* Header de la tarjeta: Kicker + Status Pill */
.card-meta-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 10px;
    position: relative;
    z-index: 2;
}

.card-meta-top .kicker {
    margin-bottom: 0;
}

.status-pill {
    font-size: 0.65rem;
    font-weight: 700;
    padding: 3px 9px;
    border-radius: 12px;
    letter-spacing: 0.3px;
    text-transform: uppercase;
}

.status-healthy { background: rgba(16, 185, 129, 0.12); color: #10b981; border: 1px solid rgba(16, 185, 129, 0.25); }
.status-amber { background: rgba(245, 158, 11, 0.12); color: #f59e0b; border: 1px solid rgba(245, 158, 11, 0.25); }
.status-blue { background: rgba(37, 99, 235, 0.12); color: #2563eb; border: 1px solid rgba(37, 99, 235, 0.25); }
.status-purple { background: rgba(139, 92, 246, 0.12); color: #8b5cf6; border: 1px solid rgba(139, 92, 246, 0.25); }

.apple-card .title {
    position: relative;
    z-index: 2;
    margin-bottom: 8px;
}

.apple-card .desc {
    position: relative;
    z-index: 2;
    font-size: 0.88rem;
    line-height: 1.45;
    margin-bottom: 12px;
}

/* Pipeline / Barra de Progreso */
.card-pipeline {
    margin: 4px 0 10px 0;
    position: relative;
    z-index: 2;
}

.pipeline-bar {
    width: 100%;
    height: 4px;
    background: rgba(0, 0, 0, 0.06);
    border-radius: 4px;
    overflow: hidden;
}

[data-theme="dark"] .pipeline-bar {
    background: rgba(255, 255, 255, 0.08);
}

.pipeline-fill {
    height: 100%;
    border-radius: 4px;
    transition: width 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}

.pipeline-labels {
    display: flex;
    justify-content: space-between;
    font-size: 0.68rem;
    font-weight: 600;
    color: var(--text-sec);
    margin-top: 5px;
}

.pipeline-val {
    font-weight: 800;
}

/* Tech Tags */
.card-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-bottom: 12px;
    position: relative;
    z-index: 2;
}

.tech-tag {
    font-size: 0.66rem;
    font-weight: 600;
    padding: 3px 8px;
    border-radius: 6px;
    background: rgba(0, 0, 0, 0.035);
    color: var(--text-sec);
    border: 1px solid rgba(0, 0, 0, 0.06);
    transition: all 0.2s ease;
}

[data-theme="dark"] .tech-tag {
    background: rgba(255, 255, 255, 0.05);
    color: #94a3b8;
    border-color: rgba(255, 255, 255, 0.08);
}

.apple-card:hover .tech-tag {
    border-color: rgba(0, 0, 0, 0.15);
    color: var(--text-main);
}

[data-theme="dark"] .apple-card:hover .tech-tag {
    border-color: rgba(255, 255, 255, 0.20);
    color: #ffffff;
}

/* Visual Holográfico */
.card-visual {
    flex: 0 0 140px !important;
    height: 140px !important;
    width: 100% !important;
    margin-top: auto !important;
    border-radius: 18px !important;
    background: linear-gradient(145deg, rgba(0, 0, 0, 0.02) 0%, rgba(0, 0, 0, 0.05) 100%) !important;
    border: 1px solid rgba(0, 0, 0, 0.06) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    position: relative !important;
    overflow: hidden !important;
    transition: all 0.35s cubic-bezier(0.165, 0.84, 0.44, 1) !important;
    z-index: 2 !important;
}

[data-theme="dark"] .card-visual {
    background: linear-gradient(145deg, rgba(255, 255, 255, 0.02) 0%, rgba(255, 255, 255, 0.05) 100%) !important;
    border-color: rgba(255, 255, 255, 0.08) !important;
}

.card-visual::after {
    content: '';
    position: absolute;
    width: 120px;
    height: 120px;
    border-radius: 50%;
    filter: blur(28px);
    opacity: 0.12;
    pointer-events: none;
    transition: all 0.35s ease;
}

.apple-card:hover .card-visual::after {
    opacity: 0.35;
    transform: scale(1.2);
}

[data-accent="red"] .card-visual::after { background: var(--lda-red); }
[data-accent="amber"] .card-visual::after { background: #f59e0b; }
[data-accent="blue"] .card-visual::after { background: #2563eb; }
[data-accent="purple"] .card-visual::after { background: #8b5cf6; }

.card-visual svg {
    position: relative;
    z-index: 2;
    filter: drop-shadow(0 4px 10px rgba(0, 0, 0, 0.08));
    transition: transform 0.35s cubic-bezier(0.165, 0.84, 0.44, 1);
}

.apple-card:hover .card-visual svg {
    transform: scale(1.08) translateY(-2px);
}
"""

# Insertar extra_css_block antes del cierre de addons: .section-hidden { display: none !important; }
if "SMART AUTO-HIDE TOPBAR" not in py_text:
    target = ".section-hidden {\n    display: none !important;\n}"
    replacement = target + "\n" + extra_css_block
    py_text = py_text.replace(target, replacement)
    with open(CORE_PY, "w", encoding="utf-8") as f:
        f.write(py_text)
    print("[+] build_unified_core_css.py reparado y enriquecido con extra_css.")

# Ejecutar build_unified_core_css.py
subprocess.run(["python", CORE_PY], check=True)
print("[+] CSS unificados recompilados exitosamente.")

# ==============================================================================
# 2. ACTUALIZAR index.html
# ==============================================================================
with open(INDEX_HTML, "r", encoding="utf-8") as f:
    html = f.read()

# Actualizar Hero
hero_replacement = """        <!-- HERO SEGMENT (EXECUTIVE COCKPIT) -->
        <header class="hero">
            <div class="hero-top-badges">
                <span class="hero-badge">Command Center v2.0</span>
                <span class="hero-badge-local">
                    <span class="telemetry-dot dot-green"></span>
                    100% Offline / Resiliencia Local
                </span>
            </div>
            <h1>Cuaderno de <br><span>Bitácora</span></h1>
            <p>Centro de Mando Digital para el seguimiento ejecutivo, arquitectura técnica y gobierno integral del portfolio de proyectos estratégicos.</p>

            <!-- KPI Cockpit Grid (4 Paneles Ejecutivos en Cristal) -->
            <div class="hero-kpi-grid">
                <div class="kpi-card">
                    <div class="kpi-header">
                        <span class="kpi-title">Entregables & Actas</span>
                        <span class="kpi-badge kpi-badge-green">100% Trazable</span>
                    </div>
                    <div class="kpi-number">102</div>
                    <div class="kpi-desc">Documentos técnicos y estratégicos indexados</div>
                </div>

                <div class="kpi-card">
                    <div class="kpi-header">
                        <span class="kpi-title">Proyectos en Radar</span>
                        <span class="kpi-badge kpi-badge-red">Portfolio Activo</span>
                    </div>
                    <div class="kpi-number">11</div>
                    <div class="kpi-desc">Iniciativas distribuidas en 4 carriles de gestión</div>
                </div>

                <div class="kpi-card">
                    <div class="kpi-header">
                        <span class="kpi-title">Disponibilidad</span>
                        <span class="kpi-badge kpi-badge-blue">Autónomo</span>
                    </div>
                    <div class="kpi-number">100%</div>
                    <div class="kpi-desc">Ejecución local garantizada sin dependencias de red</div>
                </div>

                <div class="kpi-card">
                    <div class="kpi-header">
                        <span class="kpi-title">Ejes Estratégicos</span>
                        <span class="kpi-badge kpi-badge-purple">Gobernanza</span>
                    </div>
                    <div class="kpi-number">4</div>
                    <div class="kpi-desc">Gestión Directa, Facilitadores, Servicios e Histórico</div>
                </div>
            </div>
        </header>"""

hero_pattern = r"<!-- HERO SEGMENT.*?-->\s*<header class=\"hero\">.*?</header>"
html = re.sub(hero_pattern, hero_replacement, html, flags=re.DOTALL)

# SECCIÓN 1: GESTIÓN DIRECTA
sec1_cards = """                    <!-- Evolución HCM Cloud -->
                    <a href="../HCM/index.html" class="apple-card" data-accent="red">
                        <div class="card-meta-top">
                            <div class="kicker" style="color: var(--lda-red);"><span class="kicker-dot"></span> EN PRODUCCIÓN</div>
                            <span class="status-pill status-healthy">100% Activo</span>
                        </div>
                        <h3 class="title">Evolución HCM Cloud</h3>
                        <p class="desc">Núcleo integral de RR.HH. Migración estratégica de PeopleSoft a Oracle Cloud Fusion, optimizando la gestión del talento, nóminas y estructura organizativa.</p>
                        
                        <div class="card-pipeline">
                            <div class="pipeline-bar"><div class="pipeline-fill" style="width: 100%; background: #10b981;"></div></div>
                            <div class="pipeline-labels"><span>Fase 4: Go-Live</span><span class="pipeline-val" style="color: #10b981;">100%</span></div>
                        </div>

                        <div class="card-tags">
                            <span class="tech-tag">Oracle Cloud</span>
                            <span class="tech-tag">HCM Fusion</span>
                            <span class="tech-tag">REST APIs</span>
                            <span class="tech-tag">PeopleSoft</span>
                        </div>

                        <div class="card-visual" style="color: var(--lda-red);">
                            <svg width="84" height="84" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M22 36 C16.5 36 12 31.5 12 26 C12 21 16 17 21 16.2 C23.5 9.5 30 5 38 5 C39 5 39.5 5.1 40 5.2 C40.5 5.1 41 5 42 5 C50 5 56.5 9.5 59 16.2 C64 17 68 21 68 26 C68 31.5 63.5 36 58 36 Z" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round" fill="currentColor" fill-opacity="0.10"/>
                                <circle cx="40" cy="40" r="5.5" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.3"/>
                                <path d="M31 52 C31 47 35 44 40 44 C45 44 49 47 49 52" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>
                                <circle cx="21" cy="59" r="4.5" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.2"/>
                                <path d="M14 69 C14 65 17 63 21 63 C25 63 28 65 28 69" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
                                <circle cx="59" cy="59" r="4.5" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.2"/>
                                <path d="M52 69 C52 65 55 63 59 63 C63 63 66 65 66 69" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
                                <line x1="34" y1="46" x2="26" y2="55" stroke="currentColor" stroke-width="1.8" stroke-dasharray="3 2"/>
                                <line x1="46" y1="46" x2="54" y2="55" stroke="currentColor" stroke-width="1.8" stroke-dasharray="3 2"/>
                                <line x1="28" y1="66" x2="52" y2="66" stroke="currentColor" stroke-width="1.8" stroke-dasharray="3 3"/>
                            </svg>
                        </div>
                    </a>

                    <!-- Transformación y Eficiencia RRHH -->
                    <a href="../IA Area Personas/index.html" class="apple-card" data-accent="red">
                        <div class="card-meta-top">
                            <div class="kicker" style="color: var(--lda-red);"><span class="kicker-dot"></span> PENDIENTE APROBACIÓN</div>
                            <span class="status-pill status-amber">Fase 1</span>
                        </div>
                        <h3 class="title">Eficiencia RRHH & IA</h3>
                        <p class="desc">Iniciativa estratégica para automatización de consultas internas, asistentes cognitivos con LidIA y optimización operativa en gestión de personas.</p>
                        
                        <div class="card-pipeline">
                            <div class="pipeline-bar"><div class="pipeline-fill" style="width: 25%; background: var(--lda-red);"></div></div>
                            <div class="pipeline-labels"><span>Definición & Business Case</span><span class="pipeline-val" style="color: var(--lda-red);">25%</span></div>
                        </div>

                        <div class="card-tags">
                            <span class="tech-tag">IA Generativa</span>
                            <span class="tech-tag">LidIA MCP</span>
                            <span class="tech-tag">Python</span>
                            <span class="tech-tag">FastAPI</span>
                        </div>

                        <div class="card-visual" style="color: var(--lda-red);">
                            <svg width="84" height="84" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M40 12 Q40 40 68 40 Q40 40 40 68 Q40 40 12 40 Q40 40 40 12 Z" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round" fill="currentColor" fill-opacity="0.14"/>
                                <circle cx="40" cy="40" r="22" stroke="currentColor" stroke-width="1.8" stroke-dasharray="4 3" stroke-linecap="round"/>
                                <circle cx="40" cy="40" r="5" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.35"/>
                                <circle cx="25" cy="25" r="2.5" fill="currentColor"/>
                                <circle cx="55" cy="25" r="2.5" fill="currentColor"/>
                                <circle cx="25" cy="55" r="2.5" fill="currentColor"/>
                                <circle cx="55" cy="55" r="2.5" fill="currentColor"/>
                            </svg>
                        </div>
                    </a>"""

sec1_pattern = r"(<div class=\"carousel-track\" id=\"track-direct\"[^>]*>).*?(</div>\s*<button class=\"carousel-btn right)"
html = re.sub(sec1_pattern, r"\1\n" + sec1_cards + r"\n                \2", html, flags=re.DOTALL)

# SECCIÓN 2: FACILITADORES
sec2_cards = """                    <!-- Perseo -->
                    <a href="../Perseo/index.html" class="apple-card" data-accent="amber">
                        <div class="card-meta-top">
                            <div class="kicker" style="color: #f59e0b;"><span class="kicker-dot"></span> EN EVOLUCIÓN</div>
                            <span class="status-pill status-amber">Sprint Q4</span>
                        </div>
                        <h3 class="title">Perseo</h3>
                        <p class="desc">Plataforma estratégica core de tramitación y suscripción de pólizas. Arquitectura modular de alto rendimiento para el negocio asegurador.</p>
                        
                        <div class="card-pipeline">
                            <div class="pipeline-bar"><div class="pipeline-fill" style="width: 85%; background: #f59e0b;"></div></div>
                            <div class="pipeline-labels"><span>Evolutivo 2026</span><span class="pipeline-val" style="color: #f59e0b;">85%</span></div>
                        </div>

                        <div class="card-tags">
                            <span class="tech-tag">Core Seguros</span>
                            <span class="tech-tag">Oracle DB</span>
                            <span class="tech-tag">Hexagonal</span>
                            <span class="tech-tag">Alta Disponibilidad</span>
                        </div>

                        <div class="card-visual" style="color: #f59e0b;">
                            <svg width="84" height="84" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <circle cx="40" cy="40" r="30" stroke="currentColor" stroke-width="2.4" fill="currentColor" fill-opacity="0.08"/>
                                <path d="M40 18 L58 40 L40 62 L22 40 Z" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round" fill="currentColor" fill-opacity="0.18"/>
                                <circle cx="40" cy="40" r="6" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.4"/>
                                <circle cx="40" cy="18" r="2.5" fill="currentColor"/>
                                <circle cx="58" cy="40" r="2.5" fill="currentColor"/>
                                <circle cx="40" cy="62" r="2.5" fill="currentColor"/>
                                <circle cx="22" cy="40" r="2.5" fill="currentColor"/>
                            </svg>
                        </div>
                    </a>

                    <!-- CRM Operacional -->
                    <a href="../CRM Operacional/index.html" class="apple-card" data-accent="amber">
                        <div class="card-meta-top">
                            <div class="kicker" style="color: #f59e0b;"><span class="kicker-dot"></span> EN PRODUCCIÓN</div>
                            <span class="status-pill status-healthy">Omnicanal</span>
                        </div>
                        <h3 class="title">CRM Operacional</h3>
                        <p class="desc">Ecosistema integral de gestión comercial y atención omnicanal a asegurados con visión 360°, automatización y trazabilidad total.</p>
                        
                        <div class="card-pipeline">
                            <div class="pipeline-bar"><div class="pipeline-fill" style="width: 90%; background: #10b981;"></div></div>
                            <div class="pipeline-labels"><span>Operación Continua</span><span class="pipeline-val" style="color: #10b981;">90%</span></div>
                        </div>

                        <div class="card-tags">
                            <span class="tech-tag">Salesforce</span>
                            <span class="tech-tag">Omnicanal</span>
                            <span class="tech-tag">Event-Driven</span>
                            <span class="tech-tag">Kafka</span>
                        </div>

                        <div class="card-visual" style="color: #f59e0b;">
                            <svg width="84" height="84" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <circle cx="40" cy="40" r="14" stroke="currentColor" stroke-width="2.4" fill="currentColor" fill-opacity="0.22"/>
                                <circle cx="40" cy="40" r="5" fill="currentColor"/>
                                <circle cx="16" cy="24" r="7" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.12"/>
                                <circle cx="64" cy="24" r="7" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.12"/>
                                <circle cx="16" cy="56" r="7" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.12"/>
                                <circle cx="64" cy="56" r="7" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.12"/>
                                <line x1="22" y1="28" x2="30" y2="34" stroke="currentColor" stroke-width="1.8"/>
                                <line x1="58" y1="28" x2="50" y2="34" stroke="currentColor" stroke-width="1.8"/>
                                <line x1="22" y1="52" x2="30" y2="46" stroke="currentColor" stroke-width="1.8"/>
                                <line x1="58" y1="52" x2="50" y2="46" stroke="currentColor" stroke-width="1.8"/>
                            </svg>
                        </div>
                    </a>

                    <!-- Telefonía - Genesys Cloud CX -->
                    <a href="../Telefonia - Genesis CX/index.html" class="apple-card" data-accent="amber">
                        <div class="card-meta-top">
                            <div class="kicker" style="color: #f59e0b;"><span class="kicker-dot"></span> DESPLIEGUE FINAL</div>
                            <span class="status-pill status-healthy">Cloud CX</span>
                        </div>
                        <h3 class="title">Telefonía Genesys CX</h3>
                        <p class="desc">Transformación de la infraestructura de Contact Center a la nube pública de Genesys. Enrutamiento inteligente y analítica en tiempo real.</p>
                        
                        <div class="card-pipeline">
                            <div class="pipeline-bar"><div class="pipeline-fill" style="width: 95%; background: #10b981;"></div></div>
                            <div class="pipeline-labels"><span>Migración Global</span><span class="pipeline-val" style="color: #10b981;">95%</span></div>
                        </div>

                        <div class="card-tags">
                            <span class="tech-tag">Genesys Cloud</span>
                            <span class="tech-tag">WebRTC</span>
                            <span class="tech-tag">VoIP</span>
                            <span class="tech-tag">IVR Inteligente</span>
                        </div>

                        <div class="card-visual" style="color: #f59e0b;">
                            <svg width="84" height="84" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <circle cx="40" cy="40" r="28" stroke="currentColor" stroke-width="2" stroke-dasharray="4 3" opacity="0.4"/>
                                <path d="M40 20 A20 20 0 0 1 60 40" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/>
                                <path d="M40 26 A14 14 0 0 1 54 40" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                                <path d="M26 32 C26 44 36 54 48 54 L52 50 L47 44 L42 46 C38 43 37 42 34 38 L36 33 L30 28 Z" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round" fill="currentColor" fill-opacity="0.25"/>
                            </svg>
                        </div>
                    </a>

                    <!-- Reingeniería de Siniestros -->
                    <a href="../Reingenieria Siniestros/index.html" class="apple-card" data-accent="amber">
                        <div class="card-meta-top">
                            <div class="kicker" style="color: #f59e0b;"><span class="kicker-dot"></span> EN REINGENIERÍA</div>
                            <span class="status-pill status-amber">Procesos</span>
                        </div>
                        <h3 class="title">Reingeniería Siniestros</h3>
                        <p class="desc">Modernización integral del ciclo de vida del siniestro: peritación digital, detección de fraude y agilización del pago a clientes.</p>
                        
                        <div class="card-pipeline">
                            <div class="pipeline-bar"><div class="pipeline-fill" style="width: 70%; background: #f59e0b;"></div></div>
                            <div class="pipeline-labels"><span>Rediseño de Procesos</span><span class="pipeline-val" style="color: #f59e0b;">70%</span></div>
                        </div>

                        <div class="card-tags">
                            <span class="tech-tag">BPMN 2.0</span>
                            <span class="tech-tag">Automatización</span>
                            <span class="tech-tag">Workflow Engine</span>
                            <span class="tech-tag">Fraude</span>
                        </div>

                        <div class="card-visual" style="color: #f59e0b;">
                            <svg width="84" height="84" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M40 12 L64 24 V44 C64 57 53 66 40 70 C27 66 16 57 16 44 V24 Z" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round" fill="currentColor" fill-opacity="0.10"/>
                                <path d="M40 18 L58 28 V44 C58 53 49 61 40 64 C31 61 22 53 22 44 V28 Z" stroke="currentColor" stroke-width="1.6" fill="currentColor" fill-opacity="0.15"/>
                                <path d="M30 40 L37 47 L51 33" stroke="currentColor" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                        </div>
                    </a>"""

sec2_pattern = r"(<div class=\"carousel-track\" id=\"track-facilitator\"[^>]*>).*?(</div>\s*<button class=\"carousel-btn right)"
html = re.sub(sec2_pattern, r"\1\n" + sec2_cards + r"\n                \2", html, flags=re.DOTALL)

# SECCIÓN 3: SERVICIOS
sec3_cards = """                    <!-- Gestión de Usuarios y Accesos -->
                    <a href="../Gestion de Usuarios/index.html" class="apple-card" data-accent="blue">
                        <div class="card-meta-top">
                            <div class="kicker" style="color: #2563eb;"><span class="kicker-dot"></span> SERVICIO ACTIVO</div>
                            <span class="status-pill status-blue">IAM / SSO</span>
                        </div>
                        <h3 class="title">Gestión de Usuarios</h3>
                        <p class="desc">Plataforma transversal de control de accesos, autenticación multifactor, roles de usuario y gobierno de identidad corporativa.</p>
                        
                        <div class="card-pipeline">
                            <div class="pipeline-bar"><div class="pipeline-fill" style="width: 100%; background: #2563eb;"></div></div>
                            <div class="pipeline-labels"><span>Gobierno de Accesos</span><span class="pipeline-val" style="color: #2563eb;">100%</span></div>
                        </div>

                        <div class="card-tags">
                            <span class="tech-tag">Active Directory</span>
                            <span class="tech-tag">IAM / SSO</span>
                            <span class="tech-tag">RBAC</span>
                            <span class="tech-tag">Auditoría</span>
                        </div>

                        <div class="card-visual" style="color: #2563eb;">
                            <svg width="84" height="84" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <circle cx="33" cy="30" r="9" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.25"/>
                                <path d="M18 55 C18 46 25 43 33 43 C41 43 48 46 48 55" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>
                                <circle cx="53" cy="27" r="7" stroke="currentColor" stroke-width="1.8" fill="currentColor" fill-opacity="0.15"/>
                                <path d="M48 41 C52 41 62 43 62 51" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
                                <rect x="36" y="56" width="22" height="15" rx="3.5" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.3"/>
                                <path d="M41 56 V50 C41 47 43 45 47 45 C51 45 53 47 53 50 V56" stroke="currentColor" stroke-width="2"/>
                                <circle cx="47" cy="63" r="1.8" fill="currentColor"/>
                            </svg>
                        </div>
                    </a>

                    <!-- Arquitectura & Plataforma (Reservado) -->
                    <div class="apple-card disabled-card" data-accent="blue">
                        <div class="card-meta-top">
                            <div class="kicker" style="color: var(--text-muted);">INFRAESTRUCTURA</div>
                            <span class="status-pill" style="background: rgba(125,125,125,0.1); color: var(--text-muted);">Framework</span>
                        </div>
                        <h3 class="title" style="color: var(--text-muted);">Arquitectura Base</h3>
                        <p class="desc">Estándares corporativos de integración, catálogos de APIs y directrices de seguridad técnica.</p>
                        
                        <div class="card-tags">
                            <span class="tech-tag">CI/CD</span>
                            <span class="tech-tag">Docker</span>
                            <span class="tech-tag">API Gateway</span>
                        </div>

                        <div class="card-visual" style="opacity: 0.5;">
                            <svg width="84" height="84" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <rect x="18" y="16" width="44" height="12" rx="3" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.25"/>
                                <rect x="18" y="34" width="44" height="12" rx="3" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.18"/>
                                <rect x="18" y="52" width="44" height="12" rx="3" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.10"/>
                                <circle cx="26" cy="22" r="2" fill="currentColor"/>
                                <circle cx="26" cy="40" r="2" fill="currentColor"/>
                                <circle cx="26" cy="58" r="2" fill="currentColor"/>
                            </svg>
                        </div>
                    </div>

                    <!-- Gobernanza de Datos (Reservado) -->
                    <div class="apple-card disabled-card" data-accent="blue">
                        <div class="card-meta-top">
                            <div class="kicker" style="color: var(--text-muted);">DATA OFFICE</div>
                            <span class="status-pill" style="background: rgba(125,125,125,0.1); color: var(--text-muted);">Gobernanza</span>
                        </div>
                        <h3 class="title" style="color: var(--text-muted);">Calidad de Datos</h3>
                        <p class="desc">Modelos maestros de datos, linaje analítico y catálogo para auditorías regulatorias.</p>
                        
                        <div class="card-tags">
                            <span class="tech-tag">Data Quality</span>
                            <span class="tech-tag">GDPR</span>
                            <span class="tech-tag">Linaje</span>
                        </div>

                        <div class="card-visual" style="opacity: 0.5;">
                            <svg width="84" height="84" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <ellipse cx="40" cy="22" rx="24" ry="9" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.25"/>
                                <path d="M16 22 V39 C16 44 27 48 40 48 C53 48 64 44 64 39 V22" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.15"/>
                                <path d="M16 39 V56 C16 61 27 65 40 65 C53 65 64 61 64 56 V39" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.08"/>
                            </svg>
                        </div>
                    </div>

                    <!-- Oficina Técnica QA (Reservado) -->
                    <div class="apple-card disabled-card" data-accent="blue">
                        <div class="card-meta-top">
                            <div class="kicker" style="color: var(--text-muted);">CALIDAD & TESTING</div>
                            <span class="status-pill" style="background: rgba(125,125,125,0.1); color: var(--text-muted);">QA Suite</span>
                        </div>
                        <h3 class="title" style="color: var(--text-muted);">Oficina Técnica QA</h3>
                        <p class="desc">Automatización de pruebas funcionales, rendimiento y control de regresión antes de paso a producción.</p>
                        
                        <div class="card-tags">
                            <span class="tech-tag">Cypress</span>
                            <span class="tech-tag">SonarQube</span>
                            <span class="tech-tag">Testing</span>
                        </div>

                        <div class="card-visual" style="opacity: 0.5;">
                            <svg width="84" height="84" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <circle cx="40" cy="40" r="26" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.10"/>
                                <path d="M28 40 L36 48 L52 32" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                        </div>
                    </div>"""

sec3_pattern = r"(<div class=\"carousel-track\" id=\"track-services\"[^>]*>).*?(</div>\s*<button class=\"carousel-btn right)"
html = re.sub(sec3_pattern, r"\1\n" + sec3_cards + r"\n                \2", html, flags=re.DOTALL)

# SECCIÓN 4: HISTÓRICO
sec4_cards = """                    <!-- Gestión de la Información (Traspasado a Transformación) -->
                    <a href="../Gobierno de Informacion/index.html" class="apple-card" data-accent="purple" style="border-color: rgba(139, 92, 246, 0.4); background: linear-gradient(135deg, var(--bg-card) 0%, rgba(139, 92, 246, 0.05) 100%);">
                        <div class="card-meta-top">
                            <div class="kicker" style="color: #8B5CF6;"><span class="kicker-dot"></span> TRASPASADO</div>
                            <span class="status-pill status-purple">Histórico Activo</span>
                        </div>
                        <h3 class="title">Gestión de la Información</h3>
                        <p class="desc">Proyecto de Inteligencia LidIA y metodología GIN transferido al Área de Transformación. Conserva aquí todo el contexto, historial y wiki funcional.</p>
                        
                        <div class="card-pipeline">
                            <div class="pipeline-bar"><div class="pipeline-fill" style="width: 100%; background: #8B5CF6;"></div></div>
                            <div class="pipeline-labels"><span>Wiki & Contexto GIN</span><span class="pipeline-val" style="color: #8B5CF6;">Permanente</span></div>
                        </div>

                        <div class="card-tags">
                            <span class="tech-tag">Inteligencia LidIA</span>
                            <span class="tech-tag">Metodología GIN</span>
                            <span class="tech-tag">Data Governance</span>
                            <span class="tech-tag">Histórico</span>
                        </div>

                        <div class="card-visual" style="color: #8B5CF6;">
                            <svg width="84" height="84" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M40 13 L66 28 L40 43 L14 28 Z" stroke="#8B5CF6" stroke-width="2.2" stroke-linejoin="round" fill="#8B5CF6" fill-opacity="0.12"/>
                                <path d="M14 28 L40 43 L40 72 L14 58 Z" stroke="#8B5CF6" stroke-width="2.2" stroke-linejoin="round" fill="#8B5CF6" fill-opacity="0.18"/>
                                <path d="M40 43 L66 28 L66 58 L40 72 Z" stroke="#8B5CF6" stroke-width="2.2" stroke-linejoin="round" fill="#8B5CF6" fill-opacity="0.26"/>
                                <circle cx="40" cy="43" r="4.5" fill="#8B5CF6"/>
                                <circle cx="40" cy="13" r="3" fill="#8B5CF6"/>
                                <circle cx="66" cy="28" r="3" fill="#8B5CF6"/>
                                <circle cx="14" cy="28" r="3" fill="#8B5CF6"/>
                                <circle cx="40" cy="72" r="3" fill="#8B5CF6"/>
                            </svg>
                        </div>
                    </a>

                    <!-- Archivo Histórico Card 1 -->
                    <div class="apple-card disabled-card" data-accent="purple">
                        <div class="card-meta-top">
                            <div class="kicker" style="color: var(--text-muted);">HISTORIAL ARCHIVADO</div>
                            <span class="status-pill" style="background: rgba(125,125,125,0.1); color: var(--text-muted);">Registro</span>
                        </div>
                        <h3 class="title" style="color: var(--text-muted);">Archivo de Porfolio</h3>
                        <p class="desc">Espacio reservado para almacenar el historial de proyectos concluidos en ciclos anteriores.</p>
                        
                        <div class="card-tags">
                            <span class="tech-tag">Ciclos Anteriores</span>
                            <span class="tech-tag">Auditoría</span>
                        </div>

                        <div class="card-visual" style="opacity: 0.5;">
                            <svg width="84" height="84" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <rect x="16" y="14" width="48" height="52" rx="6" stroke="currentColor" stroke-width="2.4" fill="currentColor" fill-opacity="0.12"/>
                                <circle cx="40" cy="40" r="13" stroke="currentColor" stroke-width="2.2"/>
                                <circle cx="40" cy="40" r="5" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.35"/>
                            </svg>
                        </div>
                    </div>

                    <!-- Archivo Histórico Card 2 -->
                    <div class="apple-card disabled-card" data-accent="purple">
                        <div class="card-meta-top">
                            <div class="kicker" style="color: var(--text-muted);">REPOSITORIO</div>
                            <span class="status-pill" style="background: rgba(125,125,125,0.1); color: var(--text-muted);">Memoria</span>
                        </div>
                        <h3 class="title" style="color: var(--text-muted);">Registro Histórico</h3>
                        <p class="desc">Conservación de memorias técnicas, lecciones aprendidas y acuerdos de gobernanza pasados.</p>
                        
                        <div class="card-tags">
                            <span class="tech-tag">Lecciones</span>
                            <span class="tech-tag">Memorias</span>
                        </div>

                        <div class="card-visual" style="opacity: 0.5;">
                            <svg width="84" height="84" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <rect x="18" y="16" width="44" height="48" rx="5" stroke="currentColor" stroke-width="2.4" fill="currentColor" fill-opacity="0.12"/>
                                <line x1="26" y1="16" x2="26" y2="64" stroke="currentColor" stroke-width="2"/>
                                <path d="M37 16 V34 L41 30 L45 34 V16" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.3"/>
                            </svg>
                        </div>
                    </div>"""

sec4_pattern = r"(<div class=\"carousel-track\" id=\"track-closed\"[^>]*>).*?(</div>\s*<button class=\"carousel-btn right)"
html = re.sub(sec4_pattern, r"\1\n" + sec4_cards + r"\n                \2", html, flags=re.DOTALL)

# JAVASCRIPT CON SMART AUTO-HIDE Y SPOTLIGHT
js_script_replacement = """        // ==========================================
        // SMART AUTO-HIDE & LIQUID GLASS TOPBAR (SAFARI / LINEAR STYLE)
        // ==========================================
        let lastScrollY = window.scrollY;
        let ticking = false;
        const islandHeader = document.querySelector('.app-header-island');
        const scrollThreshold = 8; // Sensibilidad al scroll

        function handleScrollDynamics() {
            const currentScrollY = window.scrollY;

            if (islandHeader) {
                // 1. Estado Liquid Glass Ultra-Translúcido
                if (currentScrollY > 35) {
                    islandHeader.classList.add('is-scrolled');
                } else {
                    islandHeader.classList.remove('is-scrolled');
                }

                // 2. Smart Auto-Hide al bajar / Smart Reveal al subir
                if (currentScrollY > 100) {
                    if (currentScrollY > lastScrollY + scrollThreshold) {
                        // Desplazamiento hacia ABAJO: deslizar hacia arriba y ocultar
                        islandHeader.classList.add('header-hidden');
                    } else if (currentScrollY < lastScrollY - scrollThreshold) {
                        // Desplazamiento hacia ARRIBA: revelar de inmediato
                        islandHeader.classList.remove('header-hidden');
                    }
                } else {
                    // Cerca del tope: siempre visible
                    islandHeader.classList.remove('header-hidden');
                }
            }

            lastScrollY = currentScrollY;
            ticking = false;
        }

        window.addEventListener('scroll', () => {
            if (!ticking) {
                window.requestAnimationFrame(handleScrollDynamics);
                ticking = true;
            }
        }, { passive: true });

        // ==========================================
        // SPOTLIGHT INTERACTIVO QUE SIGUE AL RATÓN (STRIPE / LINEAR STYLE)
        // ==========================================
        function initCardSpotlights() {
            document.querySelectorAll('.apple-card').forEach(card => {
                card.addEventListener('mousemove', (e) => {
                    const rect = card.getBoundingClientRect();
                    const x = e.clientX - rect.left;
                    const y = e.clientY - rect.top;
                    card.style.setProperty('--mouse-x', `${x}px`);
                    card.style.setProperty('--mouse-y', `${y}px`);
                });
            });
        }

        // Inicialización
        document.addEventListener('DOMContentLoaded', () => {
            initCardSpotlights();
            handleScrollDynamics();
        });"""

if "handleScrollDynamics" not in html:
    html = html.replace("// Inicializar Lucide si hay iconos dinámicos", js_script_replacement + "\n\n        // Inicializar Lucide si hay iconos dinámicos")

with open(INDEX_HTML, "w", encoding="utf-8") as f:
    f.write(html)

print("[+] index.html actualizado con Hero Cockpit, Cards Enriquecidas, Spotlight y Smart Auto-Hide.")
print("[OK] Proceso de transformación visual completado exitosamente.")
