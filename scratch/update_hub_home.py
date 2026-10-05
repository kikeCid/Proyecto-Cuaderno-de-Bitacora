# -*- coding: utf-8 -*-
"""
Script para actualizar 01_Proyectos/Cuaderno de Bitacora (Proyectos)/index.html
incorporando la FASE 1:
- Header Flotante Isla Glassmorphism (Floating Island Header)
- Segmented Control & Switcher de Vistas (Carrusel Showcase vs Bento Grid Matrix)
- Atajos de teclado profesionales (B para Bento Grid, D para Dark mode, Ctrl+K para Spotlight)
"""
import os

HUB_HTML_PATH = os.path.join(
    r"C:\Proyectos_Claude\Proyecto Cuaderno de Bitacora",
    "01_Proyectos", "Cuaderno de Bitacora (Proyectos)", "index.html"
)

# SVGs Simétricos 80x80 a escala 96x96
SVG_HCM = '''<svg width="96" height="96" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M22 36 C16.5 36 12 31.5 12 26 C12 21 16 17 21 16.2 C23.5 9.5 30 5 38 5 C39 5 39.5 5.1 40 5.2 C40.5 5.1 41 5 42 5 C50 5 56.5 9.5 59 16.2 C64 17 68 21 68 26 C68 31.5 63.5 36 58 36 Z" 
          stroke="currentColor" stroke-width="2.4" stroke-linejoin="round" fill="currentColor" fill-opacity="0.10"/>
    <circle cx="40" cy="40" r="5.5" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.3"/>
    <path d="M31 52 C31 47 35 44 40 44 C45 44 49 47 49 52" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>
    <circle cx="21" cy="59" r="4.5" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.2"/>
    <path d="M14 69 C14 65 17 63 21 63 C25 63 28 65 28 69" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
    <circle cx="59" cy="59" r="4.5" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.2"/>
    <path d="M52 69 C52 65 55 63 59 63 C63 63 66 65 66 69" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
    <line x1="34" y1="46" x2="26" y2="55" stroke="currentColor" stroke-width="1.8" stroke-dasharray="3 2"/>
    <line x1="46" y1="46" x2="54" y2="55" stroke="currentColor" stroke-width="1.8" stroke-dasharray="3 2"/>
    <line x1="28" y1="66" x2="52" y2="66" stroke="currentColor" stroke-width="1.8" stroke-dasharray="3 3"/>
</svg>'''

SVG_IA_RRHH = '''<svg width="96" height="96" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M40 12 Q40 40 68 40 Q40 40 40 68 Q40 40 12 40 Q40 40 40 12 Z" 
          stroke="currentColor" stroke-width="2.4" stroke-linejoin="round" fill="currentColor" fill-opacity="0.14"/>
    <circle cx="40" cy="40" r="22" stroke="currentColor" stroke-width="1.8" stroke-dasharray="4 3" stroke-linecap="round"/>
    <circle cx="40" cy="40" r="5" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.35"/>
    <circle cx="25" cy="25" r="2.5" fill="currentColor"/>
    <circle cx="55" cy="25" r="2.5" fill="currentColor"/>
    <circle cx="25" cy="55" r="2.5" fill="currentColor"/>
    <circle cx="55" cy="55" r="2.5" fill="currentColor"/>
</svg>'''

SVG_PERSEO = '''<svg width="96" height="96" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M19 40 C19 23 28 14 40 14 C52 14 61 23 61 40" stroke="currentColor" stroke-width="2.8" stroke-linecap="round"/>
    <rect x="14" y="34" width="8" height="18" rx="4" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.2"/>
    <rect x="58" y="34" width="8" height="18" rx="4" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.2"/>
    <circle cx="40" cy="38" r="14" stroke="currentColor" stroke-width="1.8" stroke-dasharray="3 2"/>
    <circle cx="40" cy="38" r="7" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.15"/>
    <circle cx="40" cy="38" r="2.5" fill="currentColor"/>
    <path d="M21 48 C24 58 32 63 36 63 H44 C48 63 56 58 59 48" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
    <rect x="35" y="61" width="10" height="4.5" rx="2.2" fill="currentColor"/>
</svg>'''

SVG_CRM = '''<svg width="96" height="96" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M40 12 L68 28 V52 L40 68 L12 52 V28 L40 12 Z" 
          stroke="currentColor" stroke-width="2.4" stroke-linejoin="round" fill="currentColor" fill-opacity="0.10"/>
    <circle cx="40" cy="34" r="5.5" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.3"/>
    <path d="M30 48 C30 43 34.5 40 40 40 C45.5 40 50 43 50 48" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>
    <circle cx="40" cy="12" r="3.5" fill="currentColor"/>
    <circle cx="68" cy="28" r="3.5" fill="currentColor"/>
    <circle cx="68" cy="52" r="3.5" fill="currentColor"/>
    <circle cx="40" cy="68" r="3.5" fill="currentColor"/>
    <circle cx="12" cy="52" r="3.5" fill="currentColor"/>
    <circle cx="12" cy="28" r="3.5" fill="currentColor"/>
    <line x1="40" y1="21" x2="40" y2="28" stroke="currentColor" stroke-width="1.8" stroke-dasharray="2 2"/>
    <line x1="40" y1="52" x2="40" y2="59" stroke="currentColor" stroke-width="1.8" stroke-dasharray="2 2"/>
</svg>'''

SVG_TELEFONIA = '''<svg width="96" height="96" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="38" y="24" width="4" height="32" rx="2" fill="currentColor"/>
    <rect x="31" y="28" width="4" height="24" rx="2" fill="currentColor" fill-opacity="0.75"/>
    <rect x="45" y="28" width="4" height="24" rx="2" fill="currentColor" fill-opacity="0.75"/>
    <rect x="24" y="34" width="4" height="12" rx="2" fill="currentColor" fill-opacity="0.5"/>
    <rect x="52" y="34" width="4" height="12" rx="2" fill="currentColor" fill-opacity="0.5"/>
    <path d="M19 28 C14 34 14 46 19 52" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>
    <path d="M61 28 C66 34 66 46 61 52" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>
    <path d="M13 22 C6 30 6 50 13 58" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-opacity="0.6"/>
    <path d="M67 22 C74 30 74 50 67 58" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-opacity="0.6"/>
    <path d="M30 18 C33 15 47 15 50 18" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-dasharray="2 2"/>
</svg>'''

SVG_SINIESTROS = '''<svg width="96" height="96" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M40 13 L64 21 V39 C64 53 53 63 40 68 C27 63 16 39 V21 L40 13 Z" 
          stroke="currentColor" stroke-width="2.4" stroke-linejoin="round" fill="currentColor" fill-opacity="0.12"/>
    <circle cx="40" cy="37" r="11" stroke="currentColor" stroke-width="2" stroke-dasharray="4 2"/>
    <line x1="40" y1="26" x2="40" y2="48" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>
    <path d="M34 43 L40 49 L46 43" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
    <line x1="28" y1="37" x2="52" y2="37" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
</svg>'''

SVG_GUS = '''<svg width="96" height="96" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="20" y="14" width="40" height="52" rx="7" stroke="currentColor" stroke-width="2.4" fill="currentColor" fill-opacity="0.12"/>
    <rect x="33" y="19" width="14" height="3.5" rx="1.75" fill="currentColor"/>
    <circle cx="40" cy="32" r="6.5" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.25"/>
    <path d="M28 47 C28 41 33 38 40 38 C47 38 52 41 52 47" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>
    <rect x="33" y="52" width="14" height="10" rx="2.5" fill="var(--bg-card, #ffffff)" stroke="currentColor" stroke-width="2"/>
    <path d="M36 52 V48 C36 45.8 37.8 44 40 44 C42.2 44 44 45.8 44 48 V52" stroke="currentColor" stroke-width="1.8"/>
    <circle cx="40" cy="56.5" r="1.5" fill="currentColor"/>
</svg>'''

SVG_GIN_LIDIA = '''<svg width="96" height="96" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M40 13 L66 28 L40 43 L14 28 Z" stroke="#8B5CF6" stroke-width="2.2" stroke-linejoin="round" fill="#8B5CF6" fill-opacity="0.12"/>
    <path d="M14 28 L40 43 L40 72 L14 58 Z" stroke="#8B5CF6" stroke-width="2.2" stroke-linejoin="round" fill="#8B5CF6" fill-opacity="0.18"/>
    <path d="M40 43 L66 28 L66 58 L40 72 Z" stroke="#8B5CF6" stroke-width="2.2" stroke-linejoin="round" fill="#8B5CF6" fill-opacity="0.26"/>
    <circle cx="40" cy="43" r="4.5" fill="#8B5CF6"/>
    <circle cx="40" cy="13" r="3" fill="#8B5CF6"/>
    <circle cx="66" cy="28" r="3" fill="#8B5CF6"/>
    <circle cx="14" cy="28" r="3" fill="#8B5CF6"/>
    <circle cx="40" cy="72" r="3" fill="#8B5CF6"/>
    <circle cx="27" cy="35.5" r="2.5" fill="#8B5CF6" fill-opacity="0.7"/>
    <circle cx="53" cy="35.5" r="2.5" fill="#8B5CF6" fill-opacity="0.7"/>
</svg>'''

SVG_SERVICES_FUTURE = '''<svg width="96" height="96" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="16" y="16" width="19" height="19" rx="4" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.2"/>
    <rect x="45" y="16" width="19" height="19" rx="4" stroke="currentColor" stroke-width="2.2" stroke-dasharray="3 3"/>
    <rect x="16" y="45" width="19" height="19" rx="4" stroke="currentColor" stroke-width="2.2" stroke-dasharray="3 3"/>
    <rect x="45" y="45" width="19" height="19" rx="4" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.2"/>
    <line x1="35" y1="25.5" x2="45" y2="25.5" stroke="currentColor" stroke-width="2"/>
    <line x1="35" y1="54.5" x2="45" y2="54.5" stroke="currentColor" stroke-width="2"/>
    <line x1="25.5" y1="35" x2="25.5" y2="45" stroke="currentColor" stroke-width="2"/>
    <line x1="54.5" y1="35" x2="54.5" y2="45" stroke="currentColor" stroke-width="2"/>
    <circle cx="40" cy="40" r="4" fill="currentColor"/>
</svg>'''

SVG_SERVICES_COMPASS = '''<svg width="96" height="96" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <circle cx="40" cy="40" r="26" stroke="currentColor" stroke-width="2.2" stroke-dasharray="4 3"/>
    <circle cx="40" cy="40" r="6" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.25"/>
    <line x1="40" y1="14" x2="40" y2="22" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>
    <line x1="40" y1="58" x2="40" y2="66" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>
    <line x1="14" y1="40" x2="22" y2="40" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>
    <line x1="58" y1="40" x2="66" y2="40" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>
</svg>'''

SVG_SERVICES_LAYERS = '''<svg width="96" height="96" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M40 18 L64 30 L40 42 L16 30 Z" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round" fill="currentColor" fill-opacity="0.18"/>
    <path d="M16 41 L40 53 L64 41" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/>
    <path d="M16 52 L40 64 L64 52" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/>
</svg>'''

SVG_VAULT = '''<svg width="96" height="96" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="16" y="14" width="48" height="52" rx="6" stroke="currentColor" stroke-width="2.4" fill="currentColor" fill-opacity="0.12"/>
    <circle cx="22" cy="20" r="1.5" fill="currentColor"/>
    <circle cx="58" cy="20" r="1.5" fill="currentColor"/>
    <circle cx="22" cy="60" r="1.5" fill="currentColor"/>
    <circle cx="58" cy="60" r="1.5" fill="currentColor"/>
    <circle cx="40" cy="40" r="13" stroke="currentColor" stroke-width="2.2"/>
    <circle cx="40" cy="40" r="5" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.35"/>
    <line x1="40" y1="27" x2="40" y2="53" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
    <line x1="27" y1="40" x2="53" y2="40" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
    <rect x="11" y="32" width="5" height="16" rx="2" fill="currentColor"/>
    <rect x="64" y="32" width="5" height="16" rx="2" fill="currentColor"/>
</svg>'''

SVG_ARCHIVE_BOOK = '''<svg width="96" height="96" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="18" y="16" width="44" height="48" rx="5" stroke="currentColor" stroke-width="2.4" fill="currentColor" fill-opacity="0.12"/>
    <line x1="26" y1="16" x2="26" y2="64" stroke="currentColor" stroke-width="2"/>
    <path d="M37 16 V34 L41 30 L45 34 V16" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.3"/>
    <line x1="33" y1="44" x2="52" y2="44" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
    <line x1="33" y1="52" x2="48" y2="52" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
</svg>'''

full_html = f'''<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cuaderno de Bitácora - Portfolio de Proyectos</title>
    <!-- Core CSS Unificado -->
    <link rel="stylesheet" href="../assets/css/bitacora-core.css">
    <link rel="stylesheet" href="styles_bitacora.css">
    <!-- Lucide Icons para componentes dinámicos -->
    <script src="https://unpkg.com/lucide@latest"></script>
    <script>
        // Init theme immediately to prevent flashing
        const savedTheme = localStorage.getItem('bitacora-theme') || 'light';
        document.documentElement.setAttribute('data-theme', savedTheme);
    </script>
</head>

<body>
    <!-- FASE 1: CABECERA ISLA FLOTANTE GLASSMORPHISM -->
    <header class="app-header-island">
        <!-- Identidad Corporativa -->
        <a href="#" class="island-brand" title="Inicio - Cuaderno de Bitácora">
            <div class="island-logo">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                    <polygon points="12 2 2 7 12 12 22 7 12 2"></polygon>
                    <polyline points="2 17 12 22 22 17"></polyline>
                    <polyline points="2 12 12 17 22 12"></polyline>
                </svg>
            </div>
            <div class="island-title">
                <span>Bitácora OS</span>
                <span class="island-badge">Command Center</span>
            </div>
        </a>

        <!-- Enlaces Rápidos de Navegación -->
        <nav class="island-nav">
            <a href="#seccion-directa" class="island-nav-link" onclick="scrollToSection(event, 'seccion-directa')">
                <span class="island-dot dot-red"></span>
                <span>Directa</span>
            </a>
            <a href="#seccion-facilitadores" class="island-nav-link" onclick="scrollToSection(event, 'seccion-facilitadores')">
                <span class="island-dot dot-amber"></span>
                <span>Facilitadores</span>
            </a>
            <a href="#seccion-servicios" class="island-nav-link" onclick="scrollToSection(event, 'seccion-servicios')">
                <span class="island-dot dot-blue"></span>
                <span>Servicios</span>
            </a>
            <a href="#seccion-cerrados" class="island-nav-link" onclick="scrollToSection(event, 'seccion-cerrados')">
                <span class="island-dot dot-purple"></span>
                <span>Histórico</span>
            </a>
        </nav>

        <!-- Utilidades de Acción -->
        <div class="island-actions">
            <button class="island-search-btn open-search-trigger" title="Buscar en proyectos (Ctrl + K)">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="11" cy="11" r="8"></circle>
                    <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
                <span>Buscar</span>
                <span class="kbd-hint">Ctrl K</span>
            </button>

            <button class="island-theme-btn" id="theme-toggle-btn" onclick="toggleTheme()" title="Alternar Modo Oscuro (D)">
                <svg class="theme-icon-moon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
                </svg>
                <svg class="theme-icon-sun" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="12" cy="12" r="5"></circle>
                    <line x1="12" y1="1" x2="12" y2="3"></line>
                    <line x1="12" y1="21" x2="12" y2="23"></line>
                    <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
                    <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
                    <line x1="1" y1="12" x2="3" y2="12"></line>
                    <line x1="21" y1="12" x2="23" y2="12"></line>
                    <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
                    <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
                </svg>
            </button>

            <a href="perfil.html" class="island-avatar" title="Mi CV / Portfolio">
                <img src="avatar.png" alt="Avatar" style="width: 100%; height: 100%; object-fit: cover;"
                    onerror="this.onerror=null; this.src='data:image/svg+xml;utf8,<svg xmlns=\\'http://www.w3.org/2000/svg\\' viewBox=\\'0 0 24 24\\' fill=\\'%23e4002b\\'><path d=\\'M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 3c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3zm0 14.2c-2.5 0-4.71-1.28-6-3.22.03-1.99 4-3.08 6-3.08 1.99 0 5.97 1.09 6 3.08-1.29 1.94-3.5 3.22-6 3.22z\\'/></svg>'">
            </a>
        </div>
    </header>

    <main class="container" id="main-content">
        <!-- HERO SEGMENT -->
        <header class="hero">
            <span class="hero-badge">Command Center v1.0</span>
            <span class="hero-badge-local">Recurso en Local</span>
            <h1>Cuaderno de <br><span>Bitácora</span></h1>
            <p>Ecosistema centralizado para la gestión de proyectos, información y desarrollo estratégico de todos los proyectos abordados.</p>

            <!-- BARRA DE TELEMETRÍA DE PORFOLIO -->
            <div class="telemetry-bar">
                <div class="telemetry-chip">
                    <span class="telemetry-dot dot-red"></span>
                    <span><strong>2</strong> Gestión Directa</span>
                </div>
                <div class="telemetry-chip">
                    <span class="telemetry-dot dot-amber"></span>
                    <span><strong>4</strong> Facilitadores</span>
                </div>
                <div class="telemetry-chip">
                    <span class="telemetry-dot dot-blue"></span>
                    <span><strong>4</strong> Servicios</span>
                </div>
                <div class="telemetry-chip">
                    <span class="telemetry-dot dot-purple"></span>
                    <span><strong>1</strong> Proyecto Histórico</span>
                </div>
                <div class="telemetry-chip">
                    <span class="telemetry-dot dot-green"></span>
                    <span>100% Offline / Local</span>
                </div>
            </div>
        </header>

        <!-- FASE 1: BARRA DE CONTROL DE VISUALIZACIÓN Y FILTROS -->
        <div class="view-controls-bar">
            <!-- Segmented Control de Filtrado por Carril -->
            <div class="filter-segments">
                <button class="filter-chip active" onclick="filterPortfolio('all', this)">
                    <span>Todos</span>
                    <span class="filter-count">11</span>
                </button>
                <button class="filter-chip" onclick="filterPortfolio('direct', this)">
                    <span class="island-dot dot-red"></span>
                    <span>Directa</span>
                    <span class="filter-count">2</span>
                </button>
                <button class="filter-chip" onclick="filterPortfolio('facilitator', this)">
                    <span class="island-dot dot-amber"></span>
                    <span>Facilitadores</span>
                    <span class="filter-count">4</span>
                </button>
                <button class="filter-chip" onclick="filterPortfolio('services', this)">
                    <span class="island-dot dot-blue"></span>
                    <span>Servicios</span>
                    <span class="filter-count">4</span>
                </button>
                <button class="filter-chip" onclick="filterPortfolio('closed', this)">
                    <span class="island-dot dot-purple"></span>
                    <span>Histórico</span>
                    <span class="filter-count">1</span>
                </button>
            </div>

            <!-- Switcher de Vistas (Carrusel vs Bento Grid) -->
            <div class="view-mode-toggle">
                <button class="view-btn active" id="btn-view-carousel" onclick="setViewMode('carousel')" title="Vista Carrusel Showcase">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <rect x="2" y="7" width="20" height="10" rx="2" ry="2"></rect>
                        <line x1="7" y1="17" x2="7" y2="7"></line>
                        <line x1="17" y1="17" x2="17" y2="7"></line>
                    </svg>
                    <span>Carrusel</span>
                </button>
                <button class="view-btn" id="btn-view-grid" onclick="setViewMode('grid')" title="Vista Bento Grid Matriz (B)">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <rect x="3" y="3" width="7" height="7"></rect>
                        <rect x="14" y="3" width="7" height="7"></rect>
                        <rect x="14" y="14" width="7" height="7"></rect>
                        <rect x="3" y="14" width="7" height="7"></rect>
                    </svg>
                    <span>Bento Grid</span>
                    <span class="kbd-hint">B</span>
                </button>
            </div>
        </div>

        <!-- SECCIÓN 1: GESTIÓN DIRECTA (PO / PM) -->
        <section id="seccion-directa" class="portfolio-section" data-category="direct">
            <div class="section-header" style="border-left: 4px solid var(--lda-red);">
                <div class="section-icon" style="color: var(--lda-red);">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                        stroke-linecap="round" stroke-linejoin="round">
                        <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"></path>
                    </svg>
                </div>
                <div class="section-title-wrapper">
                    <h2 class="section-title">Gestión Directa (PO / PM)</h2>
                    <p class="section-subtitle">Proyectos liderados por el área de Personas</p>
                </div>
                <div class="section-counter">2</div>
            </div>
            <div class="carousel-container">
                <button class="carousel-btn left hidden" onclick="scrollCarousel(this, -340)"
                    aria-label="Desplazar a la izquierda">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"
                        stroke-linejoin="round">
                        <polyline points="15 18 9 12 15 6"></polyline>
                    </svg>
                </button>
                <div class="carousel-track" id="track-direct" onscroll="updateCarouselButtons(this)">

                    <!-- Evolución HCM Cloud -->
                    <a href="../HCM/index.html" class="apple-card">
                        <div class="kicker" style="color: var(--lda-red);"><span class="kicker-dot"></span> LICITACIÓN (ARRANQUE 2027)</div>
                        <h3 class="title">Evolución HCM Cloud</h3>
                        <p class="desc">Migración estratégica de PeopleSoft RR.HH. a arquitectura Cloud para digitalizar procesos y habilitar capacidades de IA y analítica avanzada.</p>
                        <div class="card-visual">
                            {SVG_HCM}
                        </div>
                    </a>

                    <!-- Transformación y Eficiencia RRHH -->
                    <a href="../IA Area Personas/index.html" class="apple-card">
                        <div class="kicker" style="color: var(--lda-red);"><span class="kicker-dot"></span> PENDIENTE DE APROBACIÓN</div>
                        <h3 class="title">Transformación y Eficiencia RRHH</h3>
                        <p class="desc">Proyecto en fase de definición, pendiente de presentar para aprobación. Iniciativa estratégica para optimizar procesos y elevar la eficiencia operativa.</p>
                        <div class="card-visual">
                            {SVG_IA_RRHH}
                        </div>
                    </a>

                </div>
                <button class="carousel-btn right hidden" onclick="scrollCarousel(this, 340)"
                    aria-label="Desplazar a la derecha">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"
                        stroke-linejoin="round">
                        <polyline points="9 18 15 12 9 6"></polyline>
                    </svg>
                </button>
            </div>
        </section>

        <!-- SECCIÓN 2: FACILITADORES / AFECTADOS -->
        <section id="seccion-facilitadores" class="portfolio-section" data-category="facilitator" style="margin-top: 50px;">
            <div class="section-header" style="border-left: 4px solid #f59e0b;">
                <div class="section-icon" style="color: #f59e0b;">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                        stroke-linecap="round" stroke-linejoin="round">
                        <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                        <circle cx="9" cy="7" r="4"></circle>
                        <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                        <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
                    </svg>
                </div>
                <div class="section-title-wrapper">
                    <h2 class="section-title">Facilitadores / Afectados</h2>
                    <p class="section-subtitle">Iniciativas transversales de compañía donde RRHH actúa como palanca</p>
                </div>
                <div class="section-counter">4</div>
            </div>
            <div class="carousel-container">
                <button class="carousel-btn left hidden" onclick="scrollCarousel(this, -340)"
                    aria-label="Desplazar a la izquierda">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"
                        stroke-linejoin="round">
                        <polyline points="15 18 9 12 15 6"></polyline>
                    </svg>
                </button>
                <div class="carousel-track" id="track-facilitator" onscroll="updateCarouselButtons(this)">

                    <!-- Proyecto Perseo -->
                    <a href="../Perseo/index.html" class="apple-card">
                        <div class="kicker" style="color: #f59e0b;"><span class="kicker-dot"></span> EN EJECUCIÓN</div>
                        <h3 class="title">Proyecto Perseo</h3>
                        <p class="desc">Definición del modelo organizativo, optimización de roles y planes de coaching para el Contact Center.</p>
                        <div class="card-visual">
                            {SVG_PERSEO}
                        </div>
                    </a>

                    <!-- CRM Operacional -->
                    <a href="../CRM Operacional/index.html" class="apple-card">
                        <div class="kicker" style="color: #f59e0b;"><span class="kicker-dot"></span> EVALUACIÓN DE OFERTAS</div>
                        <h3 class="title">CRM Operacional</h3>
                        <p class="desc">Licitación estratégica del nuevo CRM operativo para reemplazar a "Galgo" y unificar la visión del cliente.</p>
                        <div class="card-visual">
                            {SVG_CRM}
                        </div>
                    </a>

                    <!-- Telefonía CX -->
                    <a href="../Telefonia - Genesis CX/index.html" class="apple-card">
                        <div class="kicker" style="color: #f59e0b;"><span class="kicker-dot"></span> EN PRODUCCIÓN</div>
                        <h3 class="title">Telefonía CX</h3>
                        <p class="desc">Evolución de la plataforma de voz y omnicanalidad para Contact Center.</p>
                        <div class="card-visual">
                            {SVG_TELEFONIA}
                        </div>
                    </a>

                    <!-- Reingeniería Siniestros -->
                    <a href="../Reingenieria Siniestros/index.html" class="apple-card">
                        <div class="kicker" style="color: #f59e0b;"><span class="kicker-dot"></span> PILOTO ACTIVO</div>
                        <h3 class="title">Reingeniería Siniestros</h3>
                        <p class="desc">Optimización y rediseño de procesos críticos en la tramitación operativa de siniestros.</p>
                        <div class="card-visual">
                            {SVG_SINIESTROS}
                        </div>
                    </a>

                </div>
                <button class="carousel-btn right hidden" onclick="scrollCarousel(this, 340)"
                    aria-label="Desplazar a la derecha">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"
                        stroke-linejoin="round">
                        <polyline points="9 18 15 12 9 6"></polyline>
                    </svg>
                </button>
            </div>
        </section>

        <!-- EXPLICACIÓN ESTRATÉGICA DE FACILITADORES / AFECTADOS -->
        <div class="portfolio-section" data-category="facilitator" style="max-width: 1200px; margin: 0 auto 50px auto; background: var(--bg-card); border-left: 4px solid var(--lda-red); padding: 24px 30px; border-radius: 16px; box-shadow: var(--shadow); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); border: 1px solid var(--glass-border); border-left-width: 4px; border-left-color: var(--lda-red);">
            <h4 style="margin: 0 0 10px 0; font-size: 1.05rem; font-weight: 800; color: var(--lda-red); display: flex; align-items: center; gap: 8px;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                    <circle cx="9" cy="7" r="4"></circle>
                    <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                    <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
                </svg>
                El Rol de RRHH: Gestión del Cambio y Acompañamiento
            </h4>
            <p style="margin: 0 0 10px 0; color: var(--text-main); font-size: 0.95rem; line-height: 1.6;">
                Como área de Personas, nuestro papel estratégico en estos proyectos transversales es <strong>asegurar el éxito en la adopción por parte de los equipos</strong>. Estos despliegues tecnológicos conllevan un profundo impacto organizativo que requiere una fuerte Gestión del Cambio.
            </p>
            <p style="margin: 0; color: var(--text-main); font-size: 0.95rem; line-height: 1.6;">
                Nuestro foco está siempre en las <strong>personas afectadas</strong>: facilitamos el acompañamiento humano durante la transición, lideramos los programas de <em>reskilling</em> (reciclaje profesional) ante la evolución de funciones, y diseñamos la creación de los nuevos puestos de trabajo que emergen a raíz del cambio.
            </p>
        </div>

        <!-- SECCIÓN 3: SERVICIOS Y OPERATIVAS -->
        <section id="seccion-servicios" class="portfolio-section" data-category="services">
            <div class="section-header" style="border-left: 4px solid #3b82f6;">
                <div class="section-icon" style="color: #3b82f6;">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                        stroke-linecap="round" stroke-linejoin="round">
                        <rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect>
                        <line x1="8" y1="21" x2="16" y2="21"></line>
                        <line x1="12" y1="17" x2="12" y2="21"></line>
                    </svg>
                </div>
                <div class="section-title-wrapper">
                    <h2 class="section-title">Servicios y Operativas</h2>
                    <p class="section-subtitle">Catálogo de servicios transversales y documentación funcional</p>
                </div>
                <div class="section-counter">1</div>
            </div>
            <div class="carousel-container">
                <button class="carousel-btn left hidden" onclick="scrollCarousel(this, -340)"
                    aria-label="Desplazar a la izquierda">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"
                        stroke-linejoin="round">
                        <polyline points="15 18 9 12 15 6"></polyline>
                    </svg>
                </button>
                <div class="carousel-track" onscroll="updateCarouselButtons(this)">

                    <!-- Gestión de Usuarios -->
                    <a href="../Gestion de Usuarios/index.html" class="apple-card blue-card">
                        <div class="kicker" style="color: #2563eb;"><span class="kicker-dot"></span> SERVICIO ACTIVO</div>
                        <h3 class="title">Gestión de Usuarios</h3>
                        <p class="desc">Documentación sobre el funcionamiento, arquitectura operativa y servicios vinculados al sistema de Gestión de Usuarios y sus integraciones.</p>
                        <div class="card-visual">
                            {SVG_GUS}
                        </div>
                    </a>

                    <!-- Demo Card 3 -->
                    <div class="apple-card disabled-card">
                        <div class="kicker">PRÓXIMA OPERATIVA</div>
                        <h3 class="title">Nuevo Servicio</h3>
                        <p class="desc">Espacio reservado para documentar futuras operativas transversales del sistema.</p>
                        <div class="card-visual" style="opacity: 0.65;">
                            {SVG_SERVICES_FUTURE}
                        </div>
                    </div>

                    <!-- Demo Card 4 -->
                    <div class="apple-card disabled-card">
                        <div class="kicker">EN DISEÑO</div>
                        <h3 class="title">Nueva Operativa</h3>
                        <p class="desc">Tarjetón genérico preparado para alojar servicios organizacionales futuros.</p>
                        <div class="card-visual" style="opacity: 0.65;">
                            {SVG_SERVICES_COMPASS}
                        </div>
                    </div>

                    <!-- Demo Card 5 -->
                    <div class="apple-card disabled-card">
                        <div class="kicker">PENDIENTE</div>
                        <h3 class="title">Próxima Operativa</h3>
                        <p class="desc">Módulo no definido, espacio visual concebido para balancear el carrusel de servicios.</p>
                        <div class="card-visual" style="opacity: 0.65;">
                            {SVG_SERVICES_LAYERS}
                        </div>
                    </div>

                </div>
                <button class="carousel-btn right hidden" onclick="scrollCarousel(this, 340)"
                    aria-label="Desplazar a la derecha">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"
                        stroke-linejoin="round">
                        <polyline points="9 18 15 12 9 6"></polyline>
                    </svg>
                </button>
            </div>
        </section>

        <!-- SECCIÓN 4: PROYECTOS CERRADOS (HISTÓRICO) -->
        <section id="seccion-cerrados" class="portfolio-section" data-category="closed" style="margin-top: 50px;">
            <div class="section-header" style="border-left: 4px solid #8B5CF6;">
                <div class="section-icon" style="color: #8B5CF6;">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                        stroke-linecap="round" stroke-linejoin="round">
                        <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                        <line x1="16" y1="2" x2="16" y2="6"></line>
                        <line x1="8" y1="2" x2="8" y2="6"></line>
                        <line x1="3" y1="10" x2="21" y2="10"></line>
                    </svg>
                </div>
                <div class="section-title-wrapper">
                    <h2 class="section-title">Proyectos Cerrados (Histórico)</h2>
                    <p class="section-subtitle">Repositorio de proyectos completados o transferidos para preservar historial y contexto</p>
                </div>
                <div class="section-counter">1</div>
            </div>
            <div class="carousel-container">
                <button class="carousel-btn left hidden" onclick="scrollCarousel(this, -340)"
                    aria-label="Desplazar a la izquierda">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"
                        stroke-linejoin="round">
                        <polyline points="15 18 9 12 15 6"></polyline>
                    </svg>
                </button>
                <div class="carousel-track" id="track-closed" onscroll="updateCarouselButtons(this)">

                    <!-- Gestión de la Información (Traspasado a Transformación) -->
                    <a href="../Gobierno de Informacion/index.html" class="apple-card" style="border-color: rgba(139, 92, 246, 0.4); background: linear-gradient(135deg, var(--bg-card) 0%, rgba(139, 92, 246, 0.05) 100%);">
                        <div class="kicker" style="color: #8B5CF6;"><span class="kicker-dot"></span> TRASPASADO (HISTÓRICO Y CONTEXTO)</div>
                        <h3 class="title">Gestión de la Información</h3>
                        <p class="desc">Proyecto de <strong>Inteligencia LidIA</strong> y metodología <strong>GIN</strong> transferido al Área de Transformación. Se mantiene aquí todo el contexto, historial y wiki funcional para consulta permanente.</p>
                        <div class="card-visual">
                            {SVG_GIN_LIDIA}
                        </div>
                    </a>

                    <!-- Archivo Histórico Card 1 -->
                    <div class="apple-card disabled-card">
                        <div class="kicker" style="color: var(--text-muted);">HISTORIAL ARCHIVADO</div>
                        <h3 class="title" style="color: var(--text-muted);">Archivo de Porfolio</h3>
                        <p class="desc">Espacio reservado para almacenar el historial de proyectos concluidos en ciclos anteriores.</p>
                        <div class="card-visual" style="opacity: 0.5;">
                            {SVG_VAULT}
                        </div>
                    </div>

                    <!-- Archivo Histórico Card 2 -->
                    <div class="apple-card disabled-card">
                        <div class="kicker" style="color: var(--text-muted);">REPOSITORIO</div>
                        <h3 class="title" style="color: var(--text-muted);">Registro Histórico</h3>
                        <p class="desc">Conservación de memorias técnicas, lecciones aprendidas y acuerdos de gobernanza pasados.</p>
                        <div class="card-visual" style="opacity: 0.5;">
                            {SVG_ARCHIVE_BOOK}
                        </div>
                    </div>

                </div>
                <button class="carousel-btn right hidden" onclick="scrollCarousel(this, 340)"
                    aria-label="Desplazar a la derecha">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"
                        stroke-linejoin="round">
                        <polyline points="9 18 15 12 9 6"></polyline>
                    </svg>
                </button>
            </div>
        </section>

    </main>

    <footer>
        <p>&copy; 2026 Línea Directa Aseguradora S.A. &bull; Cuaderno de Bitácora Corporativo</p>
    </footer>

    <!-- MODAL DE BÚSQUEDA GLOBAL -->
    <div class="search-modal-backdrop" id="search-modal">
        <div class="search-modal-dialog">
            <div class="search-input-wrapper">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="11" cy="11" r="8"></circle>
                    <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
                <input type="text" id="global-search-input" placeholder="Buscar por proyecto, módulo, término o tecnología..." autocomplete="off">
                <span class="search-badge">ESC para cerrar</span>
            </div>
            <div class="search-results-list" id="search-results">
                <!-- Se poblará dinámicamente con search_index_data.js -->
            </div>
        </div>
    </div>

    <!-- Scripts Esenciales -->
    <script src="../assets/js/search_index_data.js"></script>
    <script src="../assets/js/bitacora-core.js"></script>
    <script>
        // ==========================================
        // 1. TEMA CLARO / OSCURO (CON ATRIBUTOS Y PERSISTENCIA)
        // ==========================================
        function toggleTheme() {{
            const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            localStorage.setItem('bitacora-theme', newTheme);
        }}

        // ==========================================
        // 2. SWITCHER DE VISTAS (CARRUSEL VS BENTO GRID)
        // ==========================================
        function setViewMode(mode) {{
            const container = document.getElementById('main-content');
            const btnCarousel = document.getElementById('btn-view-carousel');
            const btnGrid = document.getElementById('btn-view-grid');

            if (!container || !btnCarousel || !btnGrid) return;

            if (mode === 'grid') {{
                container.classList.add('view-mode-grid');
                btnGrid.classList.add('active');
                btnCarousel.classList.remove('active');
                localStorage.setItem('bitacora-view-mode', 'grid');
            }} else {{
                container.classList.remove('view-mode-grid');
                btnCarousel.classList.add('active');
                btnGrid.classList.remove('active');
                localStorage.setItem('bitacora-view-mode', 'carousel');
                // Re-inicializar botones de carrusel
                document.querySelectorAll('.carousel-track').forEach(track => {{
                    updateCarouselButtons(track);
                }});
            }}
        }}

        // ==========================================
        // 3. SEGMENTED CONTROL: FILTRADO POR CARRILES
        // ==========================================
        function filterPortfolio(category, btn) {{
            // Actualizar botones de filtro
            document.querySelectorAll('.filter-chip').forEach(c => c.classList.remove('active'));
            if (btn) btn.classList.add('active');

            const sections = document.querySelectorAll('.portfolio-section');
            sections.forEach(sec => {{
                const secCat = sec.getAttribute('data-category');
                if (category === 'all' || secCat === category) {{
                    sec.classList.remove('section-hidden');
                }} else {{
                    sec.classList.add('section-hidden');
                }}
            }});
        }}

        // ==========================================
        // 4. DESPLAZAMIENTO SUAVE A SECCIONES
        // ==========================================
        function scrollToSection(e, secId) {{
            e.preventDefault();
            const target = document.getElementById(secId);
            if (target) {{
                // Asegurar que si estaba oculto por filtro, se muestre
                target.classList.remove('section-hidden');
                target.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
            }}
        }}

        // ==========================================
        // 5. ATAJOS DE TECLADO DE ÉLITE (B para Grid, D para Dark, etc.)
        // ==========================================
        document.addEventListener('keydown', (e) => {{
            // Si el foco está en un input o el modal está abierto, ignorar
            if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;

            if (e.key === 'b' || e.key === 'B') {{
                e.preventDefault();
                const isGrid = document.getElementById('main-content').classList.contains('view-mode-grid');
                setViewMode(isGrid ? 'carousel' : 'grid');
            }} else if (e.key === 'd' || e.key === 'D') {{
                e.preventDefault();
                toggleTheme();
            }}
        }});

        // ==========================================
        // 6. INICIALIZACIÓN COMPLETA DOM
        // ==========================================
        document.addEventListener('DOMContentLoaded', () => {{
            // Restaurar modo de vista (Carrusel o Bento Grid)
            const savedView = localStorage.getItem('bitacora-view-mode') || 'carousel';
            setViewMode(savedView);

            // Inicializar botones de todos los carruseles
            document.querySelectorAll('.carousel-track').forEach(track => {{
                updateCarouselButtons(track);
            }});
        }});

        // Control de desplazamiento del Carrusel
        function scrollCarousel(btn, amount) {{
            const container = btn.closest('.carousel-container');
            const track = container.querySelector('.carousel-track');
            track.scrollBy({{ left: amount, behavior: 'smooth' }});
        }}

        // Actualizar visibilidad de botones del carrusel
        function updateCarouselButtons(track) {{
            const container = track.closest('.carousel-container');
            const leftBtn = container.querySelector('.carousel-btn.left');
            const rightBtn = container.querySelector('.carousel-btn.right');
            
            if (!leftBtn || !rightBtn) return;

            const scrollLeft = track.scrollLeft;
            const maxScroll = track.scrollWidth - track.clientWidth;

            if (scrollLeft <= 5) {{
                leftBtn.classList.add('hidden');
            }} else {{
                leftBtn.classList.remove('hidden');
            }}

            if (scrollLeft >= maxScroll - 5) {{
                rightBtn.classList.add('hidden');
            }} else {{
                rightBtn.classList.remove('hidden');
            }}
        }}

        // Inicializar Lucide si hay iconos dinámicos
        if (window.lucide) {{
            lucide.createIcons();
        }}
    </script>
</body>

</html>
'''

with open(HUB_HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(full_html)

print(f"[+] Hub index.html actualizado con FASE 1 (Header Isla Flotante & Bento Grid View Controls).")
