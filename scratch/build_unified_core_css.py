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
    flex: 0 0 170px;
    height: 170px;
    width: 100%;
    margin-top: 18px;
    border-radius: 20px;
    background: rgba(0, 0, 0, 0.025);
    border: 1px solid rgba(0, 0, 0, 0.06);
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--text-sec);
    transition: all 0.35s cubic-bezier(0.165, 0.84, 0.44, 1);
    position: relative;
    overflow: hidden;
}

/* Hover de tarjeta roja (Gestión Directa / HCM / Eficiencia RRHH) */
#track-direct .apple-card .card-visual {
    background: rgba(228, 0, 43, 0.04);
    border: 1px solid rgba(228, 0, 43, 0.12);
    color: var(--lda-red);
}

#track-direct .apple-card:hover .card-visual {
    background: rgba(228, 0, 43, 0.10);
    border-color: rgba(228, 0, 43, 0.35);
    color: var(--lda-red);
    box-shadow: 0 10px 28px rgba(228, 0, 43, 0.18);
    transform: scale(1.04) translateY(-2px);
}

/* Hover de tarjetas ámbar (Facilitadores / Perseo, CRM, Telefonía, Siniestros) */
#track-facilitator .apple-card .card-visual {
    background: rgba(217, 119, 6, 0.04);
    border: 1px solid rgba(217, 119, 6, 0.14);
    color: #d97706;
}

#track-facilitator .apple-card:hover .card-visual {
    background: rgba(217, 119, 6, 0.12);
    border-color: rgba(217, 119, 6, 0.35);
    color: #b45309;
    box-shadow: 0 10px 28px rgba(217, 119, 6, 0.18);
    transform: scale(1.04) translateY(-2px);
}

/* Hover de tarjetas azules (Servicios y Operativas / Gestión de Usuarios) */
.apple-card.blue-card .card-visual {
    background: rgba(37, 99, 235, 0.05);
    border: 1px solid rgba(37, 99, 235, 0.16);
    color: #2563eb;
}

.apple-card.blue-card:hover .card-visual {
    background: rgba(37, 99, 235, 0.13);
    border-color: rgba(37, 99, 235, 0.38);
    color: #1d4ed8;
    box-shadow: 0 10px 28px rgba(37, 99, 235, 0.20);
    transform: scale(1.04) translateY(-2px);
}

/* Hover de tarjetas púrpuras (Proyectos Cerrados / Gestión de la Información) */
#track-closed .apple-card[style*="139, 92, 246"] .card-visual {
    background: rgba(139, 92, 246, 0.06);
    border: 1px solid rgba(139, 92, 246, 0.22);
    color: #8b5cf6;
}

#track-closed .apple-card[style*="139, 92, 246"]:hover .card-visual {
    background: rgba(139, 92, 246, 0.16);
    border-color: rgba(139, 92, 246, 0.45);
    color: #7c3aed;
    box-shadow: 0 10px 28px rgba(139, 92, 246, 0.24);
    transform: scale(1.04) translateY(-2px);
}

/* Hover de tarjetas disabled en modo claro */
.apple-card.disabled-card .card-visual {
    background: rgba(0, 0, 0, 0.02);
    border: 1px dashed rgba(0, 0, 0, 0.08);
    color: var(--text-muted);
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
    color: #cbd5e1 !important;
    font-size: 0.95rem !important;
    line-height: 1.55 !important;
}

[data-theme="dark"] .apple-card .kicker {
    font-weight: 800 !important;
    letter-spacing: 1px !important;
}

[data-theme="dark"] .card-visual {
    background: rgba(255, 255, 255, 0.08) !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
    color: #f1f5f9 !important;
}

[data-theme="dark"] .card-visual svg {
    width: 96px !important;
    height: 96px !important;
}

[data-theme="dark"] .apple-card:hover .card-visual {
    background: rgba(228, 0, 43, 0.18) !important;
    border-color: rgba(228, 0, 43, 0.5) !important;
    color: #ffffff !important;
    box-shadow: 0 0 20px rgba(228, 0, 43, 0.3) !important;
}

[data-theme="dark"] #track-facilitator .apple-card:hover .card-visual {
    background: rgba(245, 158, 11, 0.25) !important;
    border-color: rgba(245, 158, 11, 0.7) !important;
    color: #ffffff !important;
    box-shadow: 0 0 20px rgba(245, 158, 11, 0.35) !important;
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
    background: rgba(59, 130, 246, 0.2) !important;
    border: 1px solid rgba(59, 130, 246, 0.35) !important;
    color: #93c5fd !important;
}

[data-theme="dark"] .apple-card.blue-card:hover .card-visual {
    background: rgba(59, 130, 246, 0.38) !important;
    border-color: rgba(59, 130, 246, 0.7) !important;
    color: #ffffff !important;
    box-shadow: 0 0 20px rgba(59, 130, 246, 0.35) !important;
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
    background: rgba(255, 255, 255, 0.04) !important;
    border: 1px dashed rgba(255, 255, 255, 0.1) !important;
    color: #64748b !important;
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
    background: rgba(139, 92, 246, 0.2) !important;
    border: 1px solid rgba(139, 92, 246, 0.35) !important;
    color: #c4b5fd !important;
}

[data-theme="dark"] .apple-card[style*="139, 92, 246"]:hover .card-visual {
    background: rgba(139, 92, 246, 0.4) !important;
    border-color: rgba(139, 92, 246, 0.7) !important;
    color: #ffffff !important;
    box-shadow: 0 0 20px rgba(139, 92, 246, 0.4) !important;
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
"""

full_core_css = base_css.strip() + "\n\n" + addons.strip() + "\n"

# Escribir en assets/css/bitacora-core.css
with open(BITACORA_CORE, "w", encoding="utf-8") as f:
    f.write(full_core_css)

# Escribir también en Cuaderno de Bitacora (Proyectos)/styles_bitacora.css
with open(STYLES_BITACORA, "w", encoding="utf-8") as f:
    f.write(full_core_css)

print(f"[+] bitacora-core.css generado con éxito ({len(full_core_css.splitlines())} líneas)")
print(f"[+] styles_bitacora.css sincronizado con éxito ({len(full_core_css.splitlines())} líneas)")
