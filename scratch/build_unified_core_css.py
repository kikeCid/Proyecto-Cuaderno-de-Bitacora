"""
Asamblea de bitacora-core.css:
Une styles_bitacora.css (diseño visual completo, 100% UTF-8) +
Módulos avanzados:
- Buscador Spotlight (Ctrl+K)
- Breadcrumbs Smart Collapse (.breadcrumb-dropdown, .collapsed-trigger)
- Top controls y avatar (.top-controls-wrapper, .avatar-link)
- Badges dinámicos (.hero-badge-local)
- Empty State Card (.empty-state-card)
"""

import os

BASE_DIR = r"C:\Proyectos_Claude\Proyecto Cuaderno de Bitacora\01_Proyectos"
STYLES_BITACORA = os.path.join(BASE_DIR, "Cuaderno de Bitacora (Proyectos)", "styles_bitacora.css")
BITACORA_CORE = os.path.join(BASE_DIR, "assets", "css", "bitacora-core.css")

with open(STYLES_BITACORA, "r", encoding="utf-8") as f:
    base_css = f.read()

# Addons necesarios para bitacora-core
addons = """
/* ==========================================================================
   MÓDULOS TRANSVERSALES ADICIONALES (BITÁCORA CORE)
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
    background: rgba(0, 0, 0, 0.6);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
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
    box-shadow: 0 24px 64px rgba(0, 0, 0, 0.4);
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
    background: rgba(255, 255, 255, 0.06);
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
"""

full_core_css = base_css.strip() + "\n\n" + addons.strip() + "\n"

# Escribir en assets
with open(BITACORA_CORE, "w", encoding="utf-8") as f:
    f.write(full_core_css)

print(f"[+] bitacora-core.css generado con éxito ({len(full_core_css.splitlines())} líneas)")
