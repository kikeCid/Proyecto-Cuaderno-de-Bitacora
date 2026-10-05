# -*- coding: utf-8 -*-
"""
Script para implementar el efecto Apple Liquid Glass en el Topbar Flotante.
- Reduce la opacidad y aumenta el desenfoque óptico (frosted blur) al hacer scroll.
- Compacta la isla (Slim Dynamic Pill) para liberar hasta un 35% más de pantalla útil.
- Proporciona 'Focus on Hover' al pasar el cursor sobre la barra.
- Sincroniza CSS unificado y JS core.
"""

import os
import re
import subprocess

BASE_DIR = r"C:\Proyectos_Claude\Proyecto Cuaderno de Bitacora"
CORE_PY = os.path.join(BASE_DIR, "scratch", "build_unified_core_css.py")
CORE_JS = os.path.join(BASE_DIR, "01_Proyectos", "assets", "js", "bitacora-core.js")
INDEX_HTML = os.path.join(BASE_DIR, "01_Proyectos", "Cuaderno de Bitacora (Proyectos)", "index.html")

# 1. ACTUALIZAR build_unified_core_css.py CON LAS NUEVAS REGLAS LIQUID GLASS
with open(CORE_PY, "r", encoding="utf-8") as f:
    core_py_content = f.read()

liquid_glass_css_block = """/* 1. Header Flotante Ejecutivo - Edición Apple Liquid Glass */
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
.island-brand {"""

# Reemplazamos la sección antigua de .app-header-island
pattern = r"/\* 1\. Header Flotante Ejecutivo \(Executive Topbar\) \*/\s*\.app-header-island\s*\{.*?\/\* Brand Section \*\/\s*\.island-brand \{"
new_core_py = re.sub(pattern, liquid_glass_css_block, core_py_content, flags=re.DOTALL)

with open(CORE_PY, "w", encoding="utf-8") as f:
    f.write(new_core_py)

print("[+] build_unified_core_css.py actualizado con Liquid Glass.")

# 2. RECOMPILAR CSS CON PYTHON
subprocess.run(["python", CORE_PY], check=True)
print("[+] CSS unificados recompilados con éxito.")

# 3. ACTUALIZAR bitacora-core.js CON initIslandLiquidGlass()
with open(CORE_JS, "r", encoding="utf-8") as f:
    core_js = f.read()

liquid_glass_js_func = """
// ==========================================
// 5. EFECTO APPLE LIQUID GLASS (SCROLL-AWARE GLASS)
// ==========================================
function initIslandLiquidGlass() {
    const island = document.querySelector('.app-header-island');
    if (!island) return;

    let ticking = false;

    function updateGlass() {
        const currentScrollY = window.scrollY;
        if (currentScrollY > 35) {
            island.classList.add('is-scrolled');
        } else {
            island.classList.remove('is-scrolled');
        }
        ticking = false;
    }

    window.addEventListener('scroll', () => {
        if (!ticking) {
            window.requestAnimationFrame(updateGlass);
            ticking = true;
        }
    }, { passive: true });

    // Ejecución inicial por si carga con scroll previo
    updateGlass();
}
"""

if "initIslandLiquidGlass" not in core_js:
    # Añadimos la función y su llamada al final
    core_js += liquid_glass_js_func
    core_js += "\n// Auto-inicializar Liquid Glass al cargar\ndocument.addEventListener('DOMContentLoaded', initIslandLiquidGlass);\n"
    with open(CORE_JS, "w", encoding="utf-8") as f:
        f.write(core_js)
    print("[+] bitacora-core.js actualizado con initIslandLiquidGlass.")
else:
    print("[=] bitacora-core.js ya contenía initIslandLiquidGlass.")

# 4. ACTUALIZAR index.html PARA ASEGURAR QUE SE INICIALIZA INMEDIATAMENTE
with open(INDEX_HTML, "r", encoding="utf-8") as f:
    index_html = f.read()

# Verificamos si index.html tiene la llamada explícita
if "initIslandLiquidGlass()" not in index_html:
    index_html = index_html.replace(
        "document.querySelectorAll('.carousel-track').forEach(track => {",
        "initIslandLiquidGlass();\n            document.querySelectorAll('.carousel-track').forEach(track => {"
    )
    with open(INDEX_HTML, "w", encoding="utf-8") as f:
        f.write(index_html)
    print("[+] index.html actualizado con llamada explícita a initIslandLiquidGlass().")

print("[OK] Proceso Liquid Glass completado con exito.")
