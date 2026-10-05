"""
Asamblea de bitacora-core.css y styles_bitacora.css con:
- Iluminación cromática reactiva de iconos (.card-visual) en Modo Claro y Modo Oscuro
- Sistema de telemetría ejecutiva en el Hero (.telemetry-bar, .telemetry-chip, .telemetry-dot)
- Micro-pulsos vivos en kickers (.kicker-dot, animaciones de respiración)
- Iconografía duotono con capas vectoriales
- Cobertura transversal para todos los 102 documentos
"""

import os

BASE_DIR = r"C:\Proyectos_Claude\Proyecto Cuaderno de Bitacora\01_Proyectos"
STYLES_BITACORA = os.path.join(BASE_DIR, "Cuaderno de Bitacora (Proyectos)", "styles_bitacora.css")
BITACORA_CORE = os.path.join(BASE_DIR, "assets", "css", "bitacora-core.css")

with open(STYLES_BITACORA, "r", encoding="utf-8") as f:
    base_css = f.read()

# Si base_css ya tenía una sección previa de MÓDULOS TRANSVERSALES ADICIONALES, limpiarla para no duplicar
idx = base_css.find("/* ==========================================================================\n   MÓDULOS TRANSVERSALES ADICIONALES")
if idx != -1:
    base_css = base_css[:idx].strip()

# Addons completos para bitacora-core y styles_bitacora
addons = """
/* ==========================================================================
   MÓDULOS TRANSVERSALES ADICIONALES (BITÁCORA CORE v2.0)
   ========================================================================== */

/* CONTROLES SUPERIORES (AVATAR + BUSCADOR + TEMA) */
.top-controls-wrapper {
    position: fixed;
    top: 30px;
    right: 30px;
    display: flex;
    align-items: center;
    gap: 15px;
    z-index: 100;
}

.avatar-link {
    width: 48px;
    height: 48px;
    border-radius: 50%;
    background: var(--bg-card);
    border: 2px solid var(--lda-red);
    padding: 2px;
    box-shadow: var(--shadow);
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    text-decoration: none;
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
}

.avatar-link:hover {
    transform: scale(1.1) rotate(5deg);
    border-color: var(--text-main);
}

/* HERO LOCAL BADGE CON PULSO */
.hero-badge-local {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 6px 16px;
    background: rgba(16, 185, 129, 0.1);
    color: #10b981;
    border: 1px solid rgba(16, 185, 129, 0.3);
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 24px;
    margin-left: 8px;
    vertical-align: middle;
}

.hero-badge-local::before {
    content: '';
    width: 8px;
    height: 8px;
    background: #10b981;
    border-radius: 50%;
    display: inline-block;
    box-shadow: 0 0 8px #10b981;
    animation: pulse-green 2s infinite;
}

@keyframes pulse-green {
    0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }
    70% { transform: scale(1); box-shadow: 0 0 0 6px rgba(16, 185, 129, 0); }
    100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
}

/* ==========================================================================
   TELEMETRÍA EJECUTIVA EN EL HERO (PORTFOLIO STATUS CHIPS)
   ========================================================================== */
.telemetry-bar {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    flex-wrap: wrap;
    margin: 10px auto 0 auto;
    max-width: 860px;
}

.telemetry-chip {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 18px;
    background: var(--bg-card);
    border: 1px solid var(--glass-border);
    border-radius: 30px;
    font-size: 0.82rem;
    color: var(--text-sec);
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    transition: var(--transition);
}

.telemetry-chip:hover {
    transform: translateY(-2px);
    border-color: var(--lda-red);
    color: var(--text-main);
    box-shadow: 0 8px 24px rgba(228, 0, 43, 0.12);
}

.telemetry-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    display: inline-block;
}

.dot-green { background: #10b981; box-shadow: 0 0 8px rgba(16, 185, 129, 0.7); animation: pulse-dot 2s infinite; }
.dot-red { background: var(--lda-red); box-shadow: 0 0 8px var(--lda-red-glow); animation: pulse-dot 2s infinite 0.5s; }
.dot-purple { background: #8b5cf6; box-shadow: 0 0 8px rgba(139, 92, 246, 0.7); animation: pulse-dot 2s infinite 1s; }
.dot-amber { background: #f59e0b; box-shadow: 0 0 8px rgba(245, 158, 11, 0.7); animation: pulse-dot 2s infinite 0.75s; }
.dot-blue { background: #2563eb; box-shadow: 0 0 8px rgba(37, 99, 235, 0.7); animation: pulse-dot 2s infinite 1.5s; }

@keyframes pulse-dot {
    0%, 100% { transform: scale(0.9); opacity: 0.85; }
    50% { transform: scale(1.25); opacity: 1; }
}

[data-theme="dark"] .telemetry-chip {
    background: rgba(28, 30, 42, 0.85);
    border: 1px solid rgba(255, 255, 255, 0.14);
    color: #cbd5e1;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4);
}

[data-theme="dark"] .telemetry-chip:hover {
    border-color: var(--lda-red);
    color: #ffffff;
    box-shadow: 0 8px 25px rgba(228, 0, 43, 0.25);
}

/* ==========================================================================
   MICRO-PULSOS VIVOS EN KICKER BADGES
   ========================================================================== */
.kicker {
    display: inline-flex;
    align-items: center;
    gap: 7px;
}

.kicker-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: currentColor;
    display: inline-block;
    animation: kicker-pulse 1.8s infinite ease-in-out;
}

@keyframes kicker-pulse {
    0%, 100% { opacity: 0.65; transform: scale(0.9); }
    50% { opacity: 1; transform: scale(1.35); }
}

/* ==========================================================================
   ILUMINACIÓN CROMÁTICA REACTIVA DE ICONOS (.card-visual) EN MODO CLARO
   ========================================================================== */
.card-visual {
    flex: 0 0 135px !important;
    height: 135px !important;
    width: 100% !important;
    margin-top: auto !important;
    border-radius: 16px !important;
    background: rgba(0, 0, 0, 0.02) !important;
    border: 1px solid rgba(0, 0, 0, 0.05) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    position: relative !important;
    overflow: hidden !important;
    transition: all 0.3s ease !important;
    z-index: 2 !important;
}

/* Hover de tarjeta roja (Gestión Directa / HCM / Eficiencia RRHH) */
#track-direct .apple-card .card-visual {
    flex: 0 0 135px !important;
    height: 135px !important;
    width: 100% !important;
    margin-top: auto !important;
    border-radius: 16px !important;
    background: rgba(0, 0, 0, 0.02) !important;
    border: 1px solid rgba(0, 0, 0, 0.05) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    position: relative !important;
    overflow: hidden !important;
    transition: all 0.3s ease !important;
    z-index: 2 !important;
}

#track-direct .apple-card:hover .card-visual {
    flex: 0 0 135px !important;
    height: 135px !important;
    width: 100% !important;
    margin-top: auto !important;
    border-radius: 16px !important;
    background: rgba(0, 0, 0, 0.02) !important;
    border: 1px solid rgba(0, 0, 0, 0.05) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    position: relative !important;
    overflow: hidden !important;
    transition: all 0.3s ease !important;
    z-index: 2 !important;
}

/* Hover de tarjetas ámbar (Facilitadores / Perseo, CRM, Telefonía, Siniestros) */
#track-facilitator .apple-card .card-visual {
    flex: 0 0 135px !important;
    height: 135px !important;
    width: 100% !important;
    margin-top: auto !important;
    border-radius: 16px !important;
    background: rgba(0, 0, 0, 0.02) !important;
    border: 1px solid rgba(0, 0, 0, 0.05) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    position: relative !important;
    overflow: hidden !important;
    transition: all 0.3s ease !important;
    z-index: 2 !important;
}

#track-facilitator .apple-card:hover .card-visual {
    flex: 0 0 135px !important;
    height: 135px !important;
    width: 100% !important;
    margin-top: auto !important;
    border-radius: 16px !important;
    background: rgba(0, 0, 0, 0.02) !important;
    border: 1px solid rgba(0, 0, 0, 0.05) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    position: relative !important;
    overflow: hidden !important;
    transition: all 0.3s ease !important;
    z-index: 2 !important;
}

/* Hover de tarjetas azules (Servicios y Operativas / Gestión de Usuarios) */
.apple-card.blue-card .card-visual {
    flex: 0 0 135px !important;
    height: 135px !important;
    width: 100% !important;
    margin-top: auto !important;
    border-radius: 16px !important;
    background: rgba(0, 0, 0, 0.02) !important;
    border: 1px solid rgba(0, 0, 0, 0.05) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    position: relative !important;
    overflow: hidden !important;
    transition: all 0.3s ease !important;
    z-index: 2 !important;
}

.apple-card.blue-card:hover .card-visual {
    flex: 0 0 135px !important;
    height: 135px !important;
    width: 100% !important;
    margin-top: auto !important;
    border-radius: 16px !important;
    background: rgba(0, 0, 0, 0.02) !important;
    border: 1px solid rgba(0, 0, 0, 0.05) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    position: relative !important;
    overflow: hidden !important;
    transition: all 0.3s ease !important;
    z-index: 2 !important;
}

/* Hover de tarjetas púrpuras (Proyectos Cerrados / Gestión de la Información) */
#track-closed .apple-card[style*="139, 92, 246"] .card-visual {
    flex: 0 0 135px !important;
    height: 135px !important;
    width: 100% !important;
    margin-top: auto !important;
    border-radius: 16px !important;
    background: rgba(0, 0, 0, 0.02) !important;
    border: 1px solid rgba(0, 0, 0, 0.05) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    position: relative !important;
    overflow: hidden !important;
    transition: all 0.3s ease !important;
    z-index: 2 !important;
}

#track-closed .apple-card[style*="139, 92, 246"]:hover .card-visual {
    flex: 0 0 135px !important;
    height: 135px !important;
    width: 100% !important;
    margin-top: auto !important;
    border-radius: 16px !important;
    background: rgba(0, 0, 0, 0.02) !important;
    border: 1px solid rgba(0, 0, 0, 0.05) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    position: relative !important;
    overflow: hidden !important;
    transition: all 0.3s ease !important;
    z-index: 2 !important;
}

/* Hover de tarjetas disabled en modo claro */
.apple-card.disabled-card .card-visual {
    flex: 0 0 135px !important;
    height: 135px !important;
    width: 100% !important;
    margin-top: auto !important;
    border-radius: 16px !important;
    background: rgba(0, 0, 0, 0.02) !important;
    border: 1px solid rgba(0, 0, 0, 0.05) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    position: relative !important;
    overflow: hidden !important;
    transition: all 0.3s ease !important;
    z-index: 2 !important;
}

/* Transición suave para SVGs en card-visual - Tamaño Proporcional y Simétrico */
.card-visual svg {
    width: 96px;
    height: 96px;
    max-width: 100px;
    max-height: 100px;
    display: block;
    margin: auto;
    transition: transform 0.4s cubic-bezier(0.165, 0.84, 0.44, 1), filter 0.4s ease;
}

.apple-card:hover .card-visual svg {
    transform: scale(1.06);
    filter: drop-shadow(0 6px 14px rgba(0, 0, 0, 0.14));
}

/* BREADCRUMB - Smart Collapse Dropdown */
.breadcrumb-dropdown {
    position: absolute;
    top: 100%;
    left: 0;
    background: var(--bg-card);
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    border: 1px solid var(--glass-border);
    border-radius: 12px;
    box-shadow: var(--shadow);
    display: none;
    flex-direction: column;
    min-width: 180px;
    padding: 8px;
    z-index: 1001;
    margin-top: 10px;
    animation: slideDown 0.3s cubic-bezier(0.165, 0.84, 0.44, 1);
}

.breadcrumb-dropdown.active {
    display: flex;
}

.breadcrumb-dropdown-item {
    padding: 10px 15px;
    font-size: 0.75rem;
    font-weight: 600;
    color: var(--text-sec);
    text-decoration: none;
    border-radius: 8px;
    transition: all 0.2s;
    white-space: nowrap;
}

.breadcrumb-dropdown-item:hover {
    background: rgba(228, 0, 43, 0.08);
    color: var(--lda-red);
}

.collapsed-trigger {
    cursor: pointer;
    font-weight: 900;
    letter-spacing: 2px;
}

@keyframes slideDown {
    from {
        opacity: 0;
        transform: translateY(-10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* BOTÓN DE BÚSQUEDA RÁPIDA (SPOTLIGHT TRIGGER) */
.search-trigger-btn {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: var(--bg-card);
    border: 1px solid var(--glass-border);
    border-radius: 30px;
    padding: 8px 16px;
    color: var(--text-sec);
    font-size: 0.85rem;
    font-weight: 600;
    cursor: pointer;
    box-shadow: var(--shadow);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    transition: var(--transition);
}

.search-trigger-btn:hover {
    border-color: var(--lda-red);
    color: var(--text-main);
    transform: translateY(-1px);
    box-shadow: 0 12px 30px rgba(228, 0, 43, 0.15);
}

.search-kbd-shortcut {
    background: rgba(0, 0, 0, 0.06);
    border-radius: 6px;
    padding: 2px 6px;
    font-size: 0.72rem;
    font-weight: 700;
    color: var(--text-muted);
    border: 1px solid var(--glass-border);
}

[data-theme="dark"] .search-kbd-shortcut {
    background: rgba(255, 255, 255, 0.08);
}

/* EMPTY STATE ELEGANTE */
.empty-state-card {
    width: 100%;
    background: var(--bg-card);
    border: 1px dashed var(--glass-border);
    border-radius: 20px;
    padding: 36px 24px;
    text-align: center;
    color: var(--text-muted);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 10px;
}

.empty-state-card svg {
    width: 40px;
    height: 40px;
    color: var(--text-muted);
    opacity: 0.5;
}

.empty-state-card h4 {
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--text-sec);
}

.empty-state-card p {
    font-size: 0.9rem;
    max-width: 460px;
    line-height: 1.5;
}

/* MODAL DE BÚSQUEDA SPOTLIGHT (CTRL + K) */
.bitacora-search-backdrop {
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(0, 0, 0, 0.65);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    z-index: 2000;
    display: flex;
    align-items: flex-start;
    justify-content: center;
    padding-top: 15vh;
    opacity: 0;
    visibility: hidden;
    transition: all 0.25s ease;
}

.bitacora-search-backdrop.active {
    opacity: 1;
    visibility: visible;
}

.bitacora-search-modal {
    width: 100%;
    max-width: 640px;
    background: var(--bg-header);
    border: 1px solid var(--glass-border);
    border-radius: 20px;
    box-shadow: 0 24px 64px rgba(0, 0, 0, 0.5);
    overflow: hidden;
    animation: modalSlideIn 0.2s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes modalSlideIn {
    from { opacity: 0; transform: translateY(-20px) scale(0.98); }
    to { opacity: 1; transform: translateY(0) scale(1); }
}

.search-input-wrapper {
    display: flex;
    align-items: center;
    padding: 16px 20px;
    border-bottom: 1px solid var(--glass-border);
    gap: 12px;
}

.search-input-wrapper svg {
    color: var(--lda-red);
    flex-shrink: 0;
}

.search-input-field {
    flex-grow: 1;
    background: transparent;
    border: none;
    font-size: 1.05rem;
    color: var(--text-main);
    outline: none;
}

.search-results-list {
    max-height: 380px;
    overflow-y: auto;
    padding: 8px;
}

.search-result-item {
    display: block;
    padding: 12px 16px;
    border-radius: 12px;
    text-decoration: none;
    color: var(--text-main);
    transition: background 0.15s ease;
    margin-bottom: 4px;
}

.search-result-item:hover,
.search-result-item.selected {
    background: rgba(228, 0, 43, 0.08);
}

[data-theme="dark"] .search-result-item:hover,
[data-theme="dark"] .search-result-item.selected {
    background: rgba(255, 255, 255, 0.08);
}

.search-result-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 4px;
}

.search-result-badge {
    font-size: 0.68rem;
    font-weight: 800;
    padding: 2px 8px;
    border-radius: 12px;
    background: var(--lda-red);
    color: white;
    text-transform: uppercase;
}

.search-result-title {
    font-size: 0.95rem;
    font-weight: 700;
    margin-bottom: 2px;
}

.search-result-desc {
    font-size: 0.8rem;
    color: var(--text-sec);
    line-height: 1.4;
}

.search-footer-info {
    padding: 10px 20px;
    background: var(--bg-card);
    border-top: 1px solid var(--glass-border);
    font-size: 0.75rem;
    color: var(--text-muted);
    display: flex;
    justify-content: space-between;
}

/* ==========================================================================
   PERFECCIONAMIENTO DE MODO OSCURO (DARK MODE VISIBILITY & DEPTH)
   ========================================================================== */

/* AMBIENT MESH MODO OSCURO */
[data-theme="dark"] .bg-mesh {
    background: radial-gradient(circle at 15% 20%, rgba(228, 0, 43, 0.16) 0%, transparent 45%),
                radial-gradient(circle at 85% 75%, rgba(59, 130, 246, 0.14) 0%, transparent 45%),
                radial-gradient(circle at 50% 50%, rgba(139, 92, 246, 0.08) 0%, transparent 60%) !important;
    opacity: 0.95 !important;
}

/* HERO SECTION MODO OSCURO */
[data-theme="dark"] .hero {
    background: linear-gradient(145deg, rgba(28, 30, 42, 0.9) 0%, rgba(18, 20, 28, 0.96) 100%) !important;
    border: 1px solid rgba(255, 255, 255, 0.13) !important;
    box-shadow: 0 16px 48px rgba(0, 0, 0, 0.5) !important;
}

[data-theme="dark"] .hero h1 {
    background: linear-gradient(135deg, #ffffff 15%, #ff4d6d 100%) !important;
    -webkit-background-clip: text !important;
    background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
}

[data-theme="dark"] .hero p {
    color: #cbd5e1 !important;
}

/* ENCABEZADOS DE SECCIÓN Y CONTADORES */
[data-theme="dark"] .section-header {
    background: linear-gradient(135deg, rgba(28, 30, 42, 0.85) 0%, rgba(20, 22, 30, 0.92) 100%) !important;
    border: 1px solid rgba(255, 255, 255, 0.13) !important;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4) !important;
}

[data-theme="dark"] .section-icon {
    background: rgba(255, 255, 255, 0.06) !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
}

[data-theme="dark"] .section-title {
    color: #ffffff !important;
}

[data-theme="dark"] .section-subtitle {
    color: #94a3b8 !important;
}

[data-theme="dark"] .section-counter {
    background: rgba(255, 255, 255, 0.08) !important;
    color: #e2e8f0 !important;
    border: 1px solid rgba(255, 255, 255, 0.16) !important;
    box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.3) !important;
}

/* BOTONES DE NAVEGACIÓN DE CARRUSEL */
[data-theme="dark"] .carousel-btn {
    background: rgba(30, 32, 44, 0.95) !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    color: #f8fafc !important;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.6) !important;
}

[data-theme="dark"] .carousel-btn:hover {
    background: var(--lda-red) !important;
    border-color: var(--lda-red) !important;
    color: #ffffff !important;
    box-shadow: 0 6px 25px var(--lda-red-glow) !important;
}

/* TARJETAS APPLE CARD PRINCIPALES EN MODO OSCURO */
[data-theme="dark"] .apple-card {
    background: linear-gradient(145deg, rgba(32, 34, 46, 0.94) 0%, rgba(22, 24, 32, 0.98) 100%) !important;
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    box-shadow: 0 10px 32px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.1) !important;
    backdrop-filter: blur(16px) !important;
    -webkit-backdrop-filter: blur(16px) !important;
}

[data-theme="dark"] .apple-card:hover {
    background: linear-gradient(145deg, rgba(40, 44, 60, 0.96) 0%, rgba(28, 30, 42, 1) 100%) !important;
    border-color: rgba(228, 0, 43, 0.7) !important;
    transform: translateY(-6px) scale(1.02) !important;
    box-shadow: 0 20px 48px rgba(0, 0, 0, 0.7), 0 0 30px rgba(228, 0, 43, 0.24), inset 0 1px 0 rgba(255, 255, 255, 0.2) !important;
}

[data-theme="dark"] .apple-card .title {
    color: #ffffff !important;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.4) !important;
}

[data-theme="dark"] .apple-card .desc {
    font-size: 0.86rem;
    line-height: 1.45;
    color: var(--text-sec);
    margin-bottom: 8px;
    position: relative;
    z-index: 2;
}

[data-theme="dark"] .apple-card .kicker {
    font-weight: 800 !important;
    letter-spacing: 1px !important;
}

[data-theme="dark"] .card-visual {
    flex: 0 0 135px !important;
    height: 135px !important;
    width: 100% !important;
    margin-top: auto !important;
    border-radius: 16px !important;
    background: rgba(0, 0, 0, 0.02) !important;
    border: 1px solid rgba(0, 0, 0, 0.05) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    position: relative !important;
    overflow: hidden !important;
    transition: all 0.3s ease !important;
    z-index: 2 !important;
}

[data-theme="dark"] .card-visual svg {
    width: 96px !important;
    height: 96px !important;
}

[data-theme="dark"] .apple-card:hover .card-visual {
    flex: 0 0 135px !important;
    height: 135px !important;
    width: 100% !important;
    margin-top: auto !important;
    border-radius: 16px !important;
    background: rgba(0, 0, 0, 0.02) !important;
    border: 1px solid rgba(0, 0, 0, 0.05) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    position: relative !important;
    overflow: hidden !important;
    transition: all 0.3s ease !important;
    z-index: 2 !important;
}

[data-theme="dark"] #track-facilitator .apple-card:hover .card-visual {
    flex: 0 0 135px !important;
    height: 135px !important;
    width: 100% !important;
    margin-top: auto !important;
    border-radius: 16px !important;
    background: rgba(0, 0, 0, 0.02) !important;
    border: 1px solid rgba(0, 0, 0, 0.05) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    position: relative !important;
    overflow: hidden !important;
    transition: all 0.3s ease !important;
    z-index: 2 !important;
}

/* TARJETAS BLUE-CARD (GESTIÓN DE USUARIOS) EN MODO OSCURO */
[data-theme="dark"] .apple-card.blue-card {
    background: linear-gradient(145deg, rgba(16, 42, 77, 0.94) 0%, rgba(10, 26, 50, 0.98) 100%) !important;
    border: 1px solid rgba(59, 130, 246, 0.4) !important;
    box-shadow: 0 10px 32px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(59, 130, 246, 0.25) !important;
}

[data-theme="dark"] .apple-card.blue-card:hover {
    background: linear-gradient(145deg, rgba(22, 56, 102, 0.96) 0%, rgba(14, 36, 68, 1) 100%) !important;
    border-color: rgba(59, 130, 246, 0.8) !important;
    box-shadow: 0 20px 48px rgba(0, 0, 0, 0.7), 0 0 30px rgba(59, 130, 246, 0.35), inset 0 1px 0 rgba(255, 255, 255, 0.2) !important;
}

[data-theme="dark"] .apple-card.blue-card .title {
    color: #ffffff !important;
}

[data-theme="dark"] .apple-card.blue-card .desc {
    color: #bfdbfe !important;
}

[data-theme="dark"] .blue-card .card-visual {
    flex: 0 0 135px !important;
    height: 135px !important;
    width: 100% !important;
    margin-top: auto !important;
    border-radius: 16px !important;
    background: rgba(0, 0, 0, 0.02) !important;
    border: 1px solid rgba(0, 0, 0, 0.05) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    position: relative !important;
    overflow: hidden !important;
    transition: all 0.3s ease !important;
    z-index: 2 !important;
}

[data-theme="dark"] .apple-card.blue-card:hover .card-visual {
    flex: 0 0 135px !important;
    height: 135px !important;
    width: 100% !important;
    margin-top: auto !important;
    border-radius: 16px !important;
    background: rgba(0, 0, 0, 0.02) !important;
    border: 1px solid rgba(0, 0, 0, 0.05) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    position: relative !important;
    overflow: hidden !important;
    transition: all 0.3s ease !important;
    z-index: 2 !important;
}

/* TARJETAS DISABLED (SLOTS VACÍOS / PRÓXIMAS OPERATIVAS) EN MODO OSCURO */
[data-theme="dark"] .apple-card.disabled-card {
    background: rgba(24, 26, 36, 0.7) !important;
    border: 1px dashed rgba(255, 255, 255, 0.2) !important;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.35) !important;
    opacity: 0.9 !important;
}

[data-theme="dark"] .apple-card.disabled-card:hover {
    transform: none !important;
    background: rgba(28, 32, 44, 0.8) !important;
    border-color: rgba(255, 255, 255, 0.3) !important;
}

[data-theme="dark"] .apple-card.disabled-card .title {
    color: #94a3b8 !important;
}

[data-theme="dark"] .apple-card.disabled-card .desc {
    color: #64748b !important;
}

[data-theme="dark"] .apple-card.disabled-card .card-visual {
    flex: 0 0 135px !important;
    height: 135px !important;
    width: 100% !important;
    margin-top: auto !important;
    border-radius: 16px !important;
    background: rgba(0, 0, 0, 0.02) !important;
    border: 1px solid rgba(0, 0, 0, 0.05) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    position: relative !important;
    overflow: hidden !important;
    transition: all 0.3s ease !important;
    z-index: 2 !important;
}

/* TARJETA PROYECTO CERRADO (HISTÓRICO / GESTIÓN INFORMACIÓN) */
[data-theme="dark"] .apple-card[style*="139, 92, 246"] {
    background: linear-gradient(145deg, rgba(38, 26, 61, 0.94) 0%, rgba(22, 15, 38, 0.98) 100%) !important;
    border: 1px solid rgba(139, 92, 246, 0.45) !important;
    box-shadow: 0 10px 32px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(139, 92, 246, 0.25) !important;
}

[data-theme="dark"] .apple-card[style*="139, 92, 246"]:hover {
    background: linear-gradient(145deg, rgba(50, 32, 82, 0.98) 0%, rgba(30, 20, 52, 1) 100%) !important;
    border-color: rgba(139, 92, 246, 0.85) !important;
    box-shadow: 0 20px 48px rgba(0, 0, 0, 0.7), 0 0 30px rgba(139, 92, 246, 0.35), inset 0 1px 0 rgba(255, 255, 255, 0.2) !important;
}

[data-theme="dark"] .apple-card[style*="139, 92, 246"] .card-visual {
    flex: 0 0 135px !important;
    height: 135px !important;
    width: 100% !important;
    margin-top: auto !important;
    border-radius: 16px !important;
    background: rgba(0, 0, 0, 0.02) !important;
    border: 1px solid rgba(0, 0, 0, 0.05) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    position: relative !important;
    overflow: hidden !important;
    transition: all 0.3s ease !important;
    z-index: 2 !important;
}

[data-theme="dark"] .apple-card[style*="139, 92, 246"]:hover .card-visual {
    flex: 0 0 135px !important;
    height: 135px !important;
    width: 100% !important;
    margin-top: auto !important;
    border-radius: 16px !important;
    background: rgba(0, 0, 0, 0.02) !important;
    border: 1px solid rgba(0, 0, 0, 0.05) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    position: relative !important;
    overflow: hidden !important;
    transition: all 0.3s ease !important;
    z-index: 2 !important;
}

/* BANNER DE INFORMACIÓN / ROL DE RRHH */
[data-theme="dark"] div[style*="border-left: 4px solid var(--lda-red)"] {
    background: linear-gradient(145deg, rgba(32, 34, 46, 0.92) 0%, rgba(22, 24, 32, 0.96) 100%) !important;
    border: 1px solid rgba(255, 255, 255, 0.14) !important;
    border-left: 4px solid var(--lda-red) !important;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.45) !important;
}

[data-theme="dark"] div[style*="border-left: 4px solid var(--lda-red)"] p {
    color: #cbd5e1 !important;
}

/* CONTROLES SUPERIORES (BUSCADOR, TEMA, AVATAR) */
[data-theme="dark"] .theme-toggle-wrapper {
    background: rgba(28, 30, 42, 0.92) !important;
    border: 1px solid rgba(255, 255, 255, 0.16) !important;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.5) !important;
}

[data-theme="dark"] .search-trigger-btn {
    background: rgba(28, 30, 42, 0.92) !important;
    border: 1px solid rgba(255, 255, 255, 0.16) !important;
    color: #cbd5e1 !important;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.5) !important;
}

[data-theme="dark"] .search-trigger-btn:hover {
    border-color: var(--lda-red) !important;
    color: #ffffff !important;
    box-shadow: 0 10px 30px rgba(228, 0, 43, 0.3) !important;
}

[data-theme="dark"] .avatar-link {
    background: rgba(28, 30, 42, 0.92) !important;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.5) !important;
}

/* NAVEGACIÓN FLOTANTE / DYNAMIC ISLAND */
[data-theme="dark"] .global-nav-wrapper {
    background: rgba(28, 30, 42, 0.92) !important;
    border: 1px solid rgba(255, 255, 255, 0.16) !important;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.5) !important;
}

[data-theme="dark"] .nav-breadcrumb-item {
    color: #cbd5e1 !important;
}

[data-theme="dark"] .nav-breadcrumb-item.current {
    color: #ffffff !important;
}

[data-theme="dark"] .nav-btn {
    color: #cbd5e1 !important;
}

/* COMPATIBILIDAD CON TARJETAS DE TODOS LOS SUBPROYECTOS */
[data-theme="dark"] .process-card,
[data-theme="dark"] .problem-card,
[data-theme="dark"] .feature-card,
[data-theme="dark"] .vendor-card,
[data-theme="dark"] .decision-card,
[data-theme="dark"] .diagnostic-card,
[data-theme="dark"] .stat-card,
[data-theme="dark"] .metric-card,
[data-theme="dark"] .roadmap-card,
[data-theme="dark"] .role-card,
[data-theme="dark"] .info-card,
[data-theme="dark"] .insight-card,
[data-theme="dark"] .bp-card,
[data-theme="dark"] .capability-card,
[data-theme="dark"] .highlight-card,
[data-theme="dark"] .inventory-card,
[data-theme="dark"] .philosophy-card,
[data-theme="dark"] .pillar-card {
    background: linear-gradient(145deg, rgba(32, 34, 46, 0.92) 0%, rgba(22, 24, 32, 0.96) 100%) !important;
    border: 1px solid rgba(255, 255, 255, 0.14) !important;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.45), inset 0 1px 0 rgba(255, 255, 255, 0.08) !important;
    color: #f8fafc !important;
}

[data-theme="dark"] .process-card:hover,
[data-theme="dark"] .problem-card:hover,
[data-theme="dark"] .feature-card:hover,
[data-theme="dark"] .vendor-card:hover,
[data-theme="dark"] .decision-card:hover,
[data-theme="dark"] .diagnostic-card:hover,
[data-theme="dark"] .stat-card:hover,
[data-theme="dark"] .metric-card:hover,
[data-theme="dark"] .roadmap-card:hover,
[data-theme="dark"] .role-card:hover,
[data-theme="dark"] .info-card:hover,
[data-theme="dark"] .insight-card:hover,
[data-theme="dark"] .bp-card:hover,
[data-theme="dark"] .capability-card:hover,
[data-theme="dark"] .highlight-card:hover,
[data-theme="dark"] .inventory-card:hover,
[data-theme="dark"] .philosophy-card:hover,
[data-theme="dark"] .pillar-card:hover {
    border-color: rgba(228, 0, 43, 0.65) !important;
    box-shadow: 0 18px 40px rgba(0, 0, 0, 0.65), 0 0 25px rgba(228, 0, 43, 0.2) !important;
    transform: translateY(-4px) !important;
}

/* ==========================================================================
   FASE 1 REFINADA: EXECUTIVE TOPBAR, BENTO GRID & SCROLL-MARGIN-TOP
   ========================================================================== */

/* Solución definitiva para que los encabezados de sección NUNCA se tapen */
.portfolio-section,
[id^="seccion-"],
.section-header {
    scroll-margin-top: 85px !important;
}

/* Aura de Fondo Ambiental Sutil (Ambient Mesh Glow) */
body::before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    pointer-events: none;
    z-index: -1;
    background: radial-gradient(circle at 10% 8%, rgba(228, 0, 43, 0.025) 0%, transparent 40%),
                radial-gradient(circle at 90% 92%, rgba(37, 99, 235, 0.025) 0%, transparent 40%);
}

[data-theme="dark"] body::before {
    background: radial-gradient(circle at 10% 8%, rgba(228, 0, 43, 0.045) 0%, transparent 45%),
                radial-gradient(circle at 90% 92%, rgba(139, 92, 246, 0.045) 0%, transparent 45%);
}

/* 1. Header Flotante Ejecutivo - Edición Apple Liquid Glass */
.app-header-island {
    position: sticky;
    top: 12px;
    z-index: 1000;
    max-width: 1080px;
    width: calc(100% - 32px);
    margin: 8px auto 25px auto;
    padding: 6px 18px;
    background: rgba(255, 255, 255, 0.68);
    backdrop-filter: blur(20px) saturate(180%);
    -webkit-backdrop-filter: blur(20px) saturate(180%);
    border: 1px solid var(--glass-border);
    border-radius: 999px;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.04), 0 1px 2px rgba(0, 0, 0, 0.02);
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    transition: max-width 0.35s cubic-bezier(0.16, 1, 0.3, 1),
                padding 0.35s cubic-bezier(0.16, 1, 0.3, 1),
                background 0.35s ease,
                backdrop-filter 0.35s ease,
                border-color 0.35s ease,
                box-shadow 0.35s cubic-bezier(0.16, 1, 0.3, 1),
                top 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    will-change: transform, background, max-width;
}

[data-theme="dark"] .app-header-island {
    background: rgba(18, 20, 30, 0.74);
    border-color: rgba(255, 255, 255, 0.12);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
}

/* ==========================================================================
   ESTADO SCROLLED: APPLE LIQUID GLASS (Ultra-transparente y desenfocado al pasar sobre secciones)
   ========================================================================== */
.app-header-island.is-scrolled {
    max-width: 920px !important;
    top: 8px !important;
    padding: 4px 14px !important;
    background: rgba(255, 255, 255, 0.22) !important;
    backdrop-filter: blur(32px) saturate(220%) contrast(102%) !important;
    -webkit-backdrop-filter: blur(32px) saturate(220%) contrast(102%) !important;
    border-color: rgba(255, 255, 255, 0.38) !important;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.03), inset 0 1px 0 rgba(255, 255, 255, 0.6) !important;
}

[data-theme="dark"] .app-header-island.is-scrolled {
    background: rgba(12, 14, 24, 0.28) !important;
    backdrop-filter: blur(32px) saturate(220%) contrast(105%) !important;
    -webkit-backdrop-filter: blur(32px) saturate(220%) contrast(105%) !important;
    border-color: rgba(255, 255, 255, 0.10) !important;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.35), inset 0 1px 0 rgba(255, 255, 255, 0.08) !important;
}

/* RECUPERACIÓN TÁCTIL (Hover durante scroll: se solidifica para dar foco) */
.app-header-island.is-scrolled:hover {
    background: rgba(255, 255, 255, 0.90) !important;
    border-color: var(--glass-border) !important;
    box-shadow: 0 12px 36px rgba(0, 0, 0, 0.08) !important;
}

[data-theme="dark"] .app-header-island.is-scrolled:hover {
    background: rgba(20, 22, 32, 0.94) !important;
    border-color: rgba(255, 255, 255, 0.18) !important;
    box-shadow: 0 14px 44px rgba(0, 0, 0, 0.65) !important;
}

/* Micro-compactación armónica de los componentes internos */
.app-header-island.is-scrolled .island-logo {
    width: 26px !important;
    height: 26px !important;
    border-radius: 7px !important;
}

.app-header-island.is-scrolled .island-logo svg {
    width: 14px !important;
    height: 14px !important;
}

.app-header-island.is-scrolled .island-title {
    font-size: 0.86rem !important;
}

.app-header-island.is-scrolled .island-badge {
    padding: 1px 6px !important;
    font-size: 0.58rem !important;
}

.app-header-island.is-scrolled .island-search-btn {
    padding: 4px 10px !important;
    font-size: 0.76rem !important;
    background: rgba(255, 255, 255, 0.3) !important;
}

[data-theme="dark"] .app-header-island.is-scrolled .island-search-btn {
    background: rgba(255, 255, 255, 0.06) !important;
}

.app-header-island.is-scrolled .island-theme-btn,
.app-header-island.is-scrolled .island-avatar {
    width: 30px !important;
    height: 30px !important;
}

/* Brand Section */
.island-brand {
    display: flex;
    align-items: center;
    gap: 10px;
    text-decoration: none;
    color: var(--text-main);
}

.island-logo {
    width: 30px;
    height: 30px;
    border-radius: 8px;
    background: var(--lda-red);
    display: flex;
    align-items: center;
    justify-content: center;
    color: #fff;
    box-shadow: 0 3px 10px var(--lda-red-glow);
}

.island-logo svg {
    width: 16px;
    height: 16px;
}

.island-title {
    font-size: 0.92rem;
    font-weight: 800;
    letter-spacing: -0.02em;
    display: flex;
    align-items: center;
    gap: 8px;
}

.island-badge {
    font-size: 0.65rem;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 12px;
    background: rgba(16, 185, 129, 0.12);
    color: #10b981;
    border: 1px solid rgba(16, 185, 129, 0.25);
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

/* Island Action Utilities */
.island-actions {
    display: flex;
    align-items: center;
    gap: 10px;
}

.island-search-btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 6px 14px;
    border-radius: 30px;
    background: var(--bg-card);
    border: 1px solid var(--glass-border);
    color: var(--text-sec);
    font-size: 0.82rem;
    cursor: pointer;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.03);
    transition: var(--transition);
}

.island-search-btn:hover {
    color: var(--text-main);
    border-color: var(--lda-red);
    transform: translateY(-1px);
}

.island-theme-btn {
    width: 34px;
    height: 34px;
    border-radius: 50%;
    background: var(--bg-card);
    border: 1px solid var(--glass-border);
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    color: var(--text-main);
    transition: var(--transition);
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.03);
}

.island-theme-btn:hover {
    transform: rotate(20deg) scale(1.05);
    border-color: var(--lda-red);
}

.theme-icon-sun { display: none; }
.theme-icon-moon { display: block; }

[data-theme="dark"] .theme-icon-sun { display: block; color: #f59e0b; }
[data-theme="dark"] .theme-icon-moon { display: none; }

.island-avatar {
    width: 34px;
    height: 34px;
    border-radius: 50%;
    overflow: hidden;
    border: 2px solid var(--glass-border);
    transition: var(--transition);
    display: block;
}

.island-avatar:hover {
    transform: scale(1.08);
    border-color: var(--lda-red);
    box-shadow: 0 4px 14px var(--lda-red-glow);
}

/* 2. Control de Visualización y Filtros (View Controls Bar) */
.view-controls-bar {
    max-width: 1200px;
    margin: 20px auto 35px auto;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 16px;
    padding: 8px 14px;
    background: var(--bg-card);
    border: 1px solid var(--glass-border);
    border-radius: 24px;
    box-shadow: var(--shadow);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
}

.filter-segments {
    display: flex;
    align-items: center;
    gap: 6px;
    flex-wrap: wrap;
}

.filter-chip {
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
    color: var(--text-sec);
    background: transparent;
    border: 1px solid transparent;
    cursor: pointer;
    transition: var(--transition);
    display: inline-flex;
    align-items: center;
    gap: 6px;
}

.filter-chip:hover {
    color: var(--text-main);
    background: rgba(0, 0, 0, 0.03);
}

[data-theme="dark"] .filter-chip:hover {
    background: rgba(255, 255, 255, 0.06);
}

.filter-chip.active {
    background: var(--text-main);
    color: var(--bg-card);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.filter-count {
    font-size: 0.72rem;
    padding: 1px 6px;
    border-radius: 10px;
    background: rgba(125, 125, 125, 0.15);
}

.filter-chip.active .filter-count {
    background: rgba(255, 255, 255, 0.25);
    color: inherit;
}

.filter-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    display: inline-block;
}

/* Switcher de Vistas (Carrusel vs Bento Grid) */
.view-mode-toggle {
    display: flex;
    align-items: center;
    gap: 4px;
    background: rgba(0, 0, 0, 0.04);
    padding: 3px;
    border-radius: 16px;
}

[data-theme="dark"] .view-mode-toggle {
    background: rgba(255, 255, 255, 0.06);
}

.view-btn {
    padding: 6px 12px;
    border-radius: 12px;
    font-size: 0.8rem;
    font-weight: 600;
    color: var(--text-sec);
    background: transparent;
    border: none;
    cursor: pointer;
    transition: var(--transition);
    display: inline-flex;
    align-items: center;
    gap: 6px;
}

.view-btn svg {
    width: 15px;
    height: 15px;
}

.view-btn.active {
    background: var(--bg-card);
    color: var(--text-main);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.kbd-hint {
    font-size: 0.65rem;
    padding: 1px 5px;
    border-radius: 4px;
    background: rgba(125, 125, 125, 0.2);
    font-family: ui-monospace, monospace;
}

/* 3. Transformación Dinámica a Bento Grid */
.view-mode-grid .carousel-container {
    overflow: visible;
}

.view-mode-grid .carousel-track {
    display: grid !important;
    grid-template-columns: repeat(auto-fill, minmax(310px, 1fr)) !important;
    gap: 24px !important;
    overflow-x: visible !important;
    padding: 10px 0 20px 0 !important;
    width: 100% !important;
    scroll-snap-type: none !important;
}

.view-mode-grid .carousel-btn {
    display: none !important;
}

.view-mode-grid .apple-card {
    width: 100% !important;
    max-width: 100% !important;
    height: auto !important;
    min-height: 440px !important;
}

/* Filtrado Dinámico de Secciones */
.section-hidden {
    display: none !important;
}

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
    width: 320px;
    height: 440px;
    background: var(--bg-card);
    border-radius: 22px;
    padding: 24px 22px 20px 22px;
    scroll-snap-align: start;
    box-shadow: 0 4px 18px rgba(0, 0, 0, 0.04);
    display: flex;
    flex-direction: column;
    position: relative;
    overflow: hidden;
    cursor: pointer;
    text-decoration: none;
    transition: transform 0.3s cubic-bezier(0.165, 0.84, 0.44, 1),
                box-shadow 0.3s cubic-bezier(0.165, 0.84, 0.44, 1),
                border-color 0.3s ease;
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
    font-size: 0.86rem;
    line-height: 1.45;
    color: var(--text-sec);
    margin-bottom: 8px;
    position: relative;
    z-index: 2;
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
    margin: 4px 0 14px 0;
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
    flex: 0 0 135px !important;
    height: 135px !important;
    width: 100% !important;
    margin-top: auto !important;
    border-radius: 16px !important;
    background: rgba(0, 0, 0, 0.02) !important;
    border: 1px solid rgba(0, 0, 0, 0.05) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    position: relative !important;
    overflow: hidden !important;
    transition: all 0.3s ease !important;
    z-index: 2 !important;
}

[data-theme="dark"] .card-visual {
    flex: 0 0 135px !important;
    height: 135px !important;
    width: 100% !important;
    margin-top: auto !important;
    border-radius: 16px !important;
    background: rgba(0, 0, 0, 0.02) !important;
    border: 1px solid rgba(0, 0, 0, 0.05) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    position: relative !important;
    overflow: hidden !important;
    transition: all 0.3s ease !important;
    z-index: 2 !important;
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

clean_addons_css = """
/* ==========================================================================
   BARRA SUPERIOR FLOTANTE ESTABLE Y SERENA (SIN AUTO-HIDE / SIN PARPADEOS)
   ========================================================================== */
.app-header-island {
    position: sticky;
    top: 12px;
    z-index: 1000;
    max-width: 1080px;
    width: calc(100% - 32px);
    margin: 8px auto 25px auto;
    padding: 6px 18px;
    background: rgba(255, 255, 255, 0.72);
    backdrop-filter: blur(20px) saturate(180%);
    -webkit-backdrop-filter: blur(20px) saturate(180%);
    border: 1px solid var(--glass-border);
    border-radius: 999px;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.03), 0 1px 2px rgba(0, 0, 0, 0.02);
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    transition: background 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
}

[data-theme="dark"] .app-header-island {
    background: rgba(18, 20, 30, 0.78);
    border-color: rgba(255, 255, 255, 0.12);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4);
}

/* ==========================================================================
   HERO LIMPIO Y SOBRIO (BASE DE CONOCIMIENTO)
   ========================================================================== */
.hero {
    text-align: center;
    margin-bottom: 35px;
    padding: 40px 30px;
    background: var(--bg-card);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid var(--glass-border);
    border-radius: 32px;
    box-shadow: var(--shadow);
}

.hero-top-badges {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    margin-bottom: 20px;
    flex-wrap: wrap;
}

.hero h1 {
    font-size: 3.2rem;
    font-weight: 900;
    line-height: 1.1;
    margin-bottom: 16px;
    background: linear-gradient(135deg, var(--text-main) 0%, var(--lda-red) 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero p {
    font-size: 1.15rem;
    color: var(--text-sec);
    max-width: 660px;
    margin: 0 auto;
    line-height: 1.5;
}

/* ==========================================================================
   BARRA DE FILTROS SEGMENTADA (CON RESPIRO DE SCROLL Y ACCESO PERMANENTE)
   ========================================================================== */
.view-controls-bar {
    max-width: 1200px;
    margin: 15px auto 35px auto;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 16px;
    padding: 8px 14px;
    background: var(--bg-card);
    border: 1px solid var(--glass-border);
    border-radius: 20px;
    box-shadow: var(--shadow);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    scroll-margin-top: 80px !important;
}

/* ==========================================================================
   CARDS DE BASE DE CONOCIMIENTO: SIMÉTRICAS, LIMPIAS Y SIN DATOS FICTICIOS
   ========================================================================== */
.apple-card {
    flex: 0 0 auto;
    width: 320px;
    height: 440px;
    background: var(--bg-card);
    border-radius: 22px;
    padding: 24px 22px 20px 22px;
    scroll-snap-align: start;
    box-shadow: 0 4px 18px rgba(0, 0, 0, 0.04);
    display: flex;
    flex-direction: column;
    position: relative;
    overflow: hidden;
    cursor: pointer;
    text-decoration: none;
    transition: transform 0.3s cubic-bezier(0.165, 0.84, 0.44, 1),
                box-shadow 0.3s cubic-bezier(0.165, 0.84, 0.44, 1),
                border-color 0.3s ease;
    border: 1px solid var(--glass-border);
}

.apple-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 16px 36px rgba(0, 0, 0, 0.09);
    border-color: rgba(228, 0, 43, 0.3);
}

[data-theme="dark"] .apple-card {
    background: rgba(22, 24, 35, 0.7);
    border-color: rgba(255, 255, 255, 0.09);
    box-shadow: 0 6px 24px rgba(0, 0, 0, 0.3);
}

[data-theme="dark"] .apple-card:hover {
    box-shadow: 0 16px 40px rgba(0, 0, 0, 0.6);
    border-color: rgba(255, 255, 255, 0.2);
}

/* Spotlight sutil que sigue al ratón */
.apple-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    border-radius: inherit;
    background: radial-gradient(
        350px circle at var(--mouse-x, -200px) var(--mouse-y, -200px),
        var(--card-spotlight, rgba(228, 0, 43, 0.10)),
        transparent 65%
    );
    opacity: 0;
    transition: opacity 0.25s ease;
    pointer-events: none;
    z-index: 1;
}

.apple-card:hover::before {
    opacity: 1;
}

[data-accent="red"] { --card-spotlight: rgba(228, 0, 43, 0.12); }
[data-accent="amber"] { --card-spotlight: rgba(245, 158, 11, 0.12); }
[data-accent="blue"] { --card-spotlight: rgba(37, 99, 235, 0.12); }
[data-accent="purple"] { --card-spotlight: rgba(139, 92, 246, 0.12); }

[data-theme="dark"] [data-accent="red"] { --card-spotlight: rgba(228, 0, 43, 0.22); }
[data-theme="dark"] [data-accent="amber"] { --card-spotlight: rgba(245, 158, 11, 0.22); }
[data-theme="dark"] [data-accent="blue"] { --card-spotlight: rgba(37, 99, 235, 0.22); }
[data-theme="dark"] [data-accent="purple"] { --card-spotlight: rgba(139, 92, 246, 0.22); }

.apple-card .kicker {
    margin-bottom: 8px;
    font-size: 0.72rem;
    font-weight: 800;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    position: relative;
    z-index: 2;
}

.apple-card .title {
    font-size: 1.35rem;
    font-weight: 800;
    margin-bottom: 8px;
    line-height: 1.25;
    position: relative;
    z-index: 2;
}

.apple-card .desc {
    font-size: 0.86rem;
    line-height: 1.45;
    color: var(--text-sec);
    margin-bottom: 8px;
    position: relative;
    z-index: 2;
}

/* Tags temáticas de la Base de Conocimiento */
.card-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin: 4px 0 14px 0;
    position: relative;
    z-index: 2;
}

.tech-tag {
    font-size: 0.68rem;
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

/* Visual vectorial inferior simétrico */
.card-visual {
    flex: 0 0 135px !important;
    height: 135px !important;
    width: 100% !important;
    margin-top: auto !important;
    border-radius: 16px !important;
    background: rgba(0, 0, 0, 0.02) !important;
    border: 1px solid rgba(0, 0, 0, 0.05) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    position: relative !important;
    overflow: hidden !important;
    transition: all 0.3s ease !important;
    z-index: 2 !important;
}

[data-theme="dark"] .card-visual {
    flex: 0 0 135px !important;
    height: 135px !important;
    width: 100% !important;
    margin-top: auto !important;
    border-radius: 16px !important;
    background: rgba(0, 0, 0, 0.02) !important;
    border: 1px solid rgba(0, 0, 0, 0.05) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    position: relative !important;
    overflow: hidden !important;
    transition: all 0.3s ease !important;
    z-index: 2 !important;
}

.card-visual svg {
    filter: drop-shadow(0 2px 6px rgba(0, 0, 0, 0.06));
    transition: transform 0.3s ease;
}

.apple-card:hover .card-visual svg {
    transform: scale(1.05);
}

/* ==========================================================================
   FOOTER CORPORATIVO OFICIAL LÍNEA DIRECTA
   ========================================================================== */
.app-footer {
    margin-top: 80px;
    background: var(--bg-card);
    border-top: 1px solid var(--glass-border);
    padding: 60px 20px 40px;
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    position: relative;
    z-index: 10;
}

.footer-inner {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: 40px;
}

.footer-brand-block {
    display: flex;
    align-items: center;
    gap: 24px;
    flex-wrap: wrap;
    padding-bottom: 24px;
    border-bottom: 1px solid var(--glass-border);
}

.footer-logo-badge {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background: #FFFFFF;
    padding: 10px 22px;
    border-radius: 12px;
    border: 1px solid rgba(0, 0, 0, 0.08);
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04);
}

.footer-logo {
    height: 38px;
    width: auto;
    display: block;
    object-fit: contain;
}

.footer-brand-desc {
    font-size: 0.92rem;
    color: var(--text-sec);
    line-height: 1.5;
    margin: 0;
    max-width: 650px;
}

.footer-links-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 30px;
}

.footer-col h4 {
    font-size: 0.88rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: var(--lda-red);
    margin-bottom: 14px;
}

.footer-col ul {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.footer-col a {
    color: var(--text-sec);
    text-decoration: none;
    font-size: 0.88rem;
    transition: color 0.2s ease, transform 0.2s ease;
    display: inline-block;
}

.footer-col a:hover {
    color: var(--lda-red);
    transform: translateX(3px);
}

.footer-status-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(16, 185, 129, 0.1);
    color: #10B981;
    border: 1px solid rgba(16, 185, 129, 0.3);
    padding: 4px 12px;
    border-radius: 16px;
    font-size: 0.8rem;
    font-weight: 600;
}

.footer-status-pill .dot-online {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #10B981;
    box-shadow: 0 0 6px #10B981;
}

.footer-meta-item {
    font-size: 0.82rem;
    color: var(--text-muted);
}

.footer-bottom {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 16px;
    padding-top: 20px;
    border-top: 1px solid var(--glass-border);
    font-size: 0.82rem;
    color: var(--text-sec);
}

.footer-bottom-badges {
    display: flex;
    gap: 10px;
    align-items: center;
}

.badge-lda-red {
    background: var(--lda-red);
    color: #FFFFFF;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    padding: 3px 10px;
    border-radius: 8px;
}

.badge-lda-outline {
    border: 1px solid var(--glass-border);
    color: var(--text-sec);
    font-size: 0.72rem;
    font-weight: 600;
    padding: 3px 10px;
    border-radius: 8px;
}

"""

full_core_css = base_css.strip() + "\n\n" + addons.strip() + "\n\n" + clean_addons_css.strip() + "\n"

# Escribir en assets/css/bitacora-core.css
with open(BITACORA_CORE, "w", encoding="utf-8") as f:
    f.write(full_core_css)

# Escribir también en Cuaderno de Bitacora (Proyectos)/styles_bitacora.css
with open(STYLES_BITACORA, "w", encoding="utf-8") as f:
    f.write(full_core_css)

print(f"[+] bitacora-core.css generado con éxito ({len(full_core_css.splitlines())} líneas)")
print(f"[+] styles_bitacora.css sincronizado con éxito ({len(full_core_css.splitlines())} líneas)")
