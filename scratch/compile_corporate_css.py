import os
import re

BASE_DIR = r"C:\Proyectos_Claude\Proyecto Cuaderno de Bitacora\01_Proyectos"
STYLES_BITACORA = os.path.join(BASE_DIR, "Cuaderno de Bitacora (Proyectos)", "styles_bitacora.css")
BITACORA_CORE = os.path.join(BASE_DIR, "assets", "css", "bitacora-core.css")

with open(BITACORA_CORE, "r", encoding="utf-8") as f:
    css = f.read()

# 1. Update line 38: * { font-family: 'Inter', ... } -> var(--font-family-primary)
css = re.sub(
    r'\*\s*\{\s*margin:\s*0;\s*padding:\s*0;\s*box-sizing:\s*border-box;\s*font-family:\s*[^;]+;\s*\}',
    '* {\n    margin: 0;\n    padding: 0;\n    box-sizing: border-box;\n    font-family: var(--font-family-primary, \'CircularXX\', sans-serif);\n}',
    css
)

# 2. Neutralize non-red halo colors in card-visual::after
css = re.sub(
    r'\[data-accent="amber"\] \.card-visual::after\s*\{\s*background:\s*[^;]+;\s*\}',
    '[data-accent="amber"] .card-visual::after { background: var(--lda-red); opacity: 0.08 !important; }',
    css
)
css = re.sub(
    r'\[data-accent="blue"\] \.card-visual::after\s*\{\s*background:\s*[^;]+;\s*\}',
    '[data-accent="blue"] .card-visual::after { background: var(--lda-red); opacity: 0.08 !important; }',
    css
)
css = re.sub(
    r'\[data-accent="purple"\] \.card-visual::after\s*\{\s*background:\s*[^;]+;\s*\}',
    '[data-accent="purple"] .card-visual::after { background: var(--lda-red); opacity: 0.08 !important; }',
    css
)

# 3. Neutralize non-red spotlights
css = re.sub(
    r'\[data-accent="amber"\]\s*\{\s*--card-spotlight:\s*[^;]+;\s*\}',
    '[data-accent="amber"] { --card-spotlight: rgba(204, 51, 51, 0.08); }',
    css
)
css = re.sub(
    r'\[data-accent="blue"\]\s*\{\s*--card-spotlight:\s*[^;]+;\s*\}',
    '[data-accent="blue"] { --card-spotlight: rgba(204, 51, 51, 0.08); }',
    css
)
css = re.sub(
    r'\[data-accent="purple"\]\s*\{\s*--card-spotlight:\s*[^;]+;\s*\}',
    '[data-accent="purple"] { --card-spotlight: rgba(204, 51, 51, 0.08); }',
    css
)

css = re.sub(
    r'\[data-theme="dark"\]\s*\[data-accent="amber"\]\s*\{\s*--card-spotlight:\s*[^;]+;\s*\}',
    '[data-theme="dark"] [data-accent="amber"] { --card-spotlight: rgba(204, 51, 51, 0.18); }',
    css
)
css = re.sub(
    r'\[data-theme="dark"\]\s*\[data-accent="blue"\]\s*\{\s*--card-spotlight:\s*[^;]+;\s*\}',
    '[data-theme="dark"] [data-accent="blue"] { --card-spotlight: rgba(204, 51, 51, 0.18); }',
    css
)
css = re.sub(
    r'\[data-theme="dark"\]\s*\[data-accent="purple"\]\s*\{\s*--card-spotlight:\s*[^;]+;\s*\}',
    '[data-theme="dark"] [data-accent="purple"] { --card-spotlight: rgba(204, 51, 51, 0.18); }',
    css
)

# 4. Remove previous tail if present
tail_marker = "/* ==========================================================================\n   TIPOGRAFÍA OFICIAL CIRCULAR XX (LÍNEA DIRECTA ASEGURADORA)"
if tail_marker in css:
    css = css[:css.find(tail_marker)].strip()

corporate_tail_core = """
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

:root {
    --font-family-primary: 'CircularXX', 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

*, *::before, *::after {
    font-family: var(--font-family-primary);
}

html, body, button, input, select, textarea, .title, h1, h2, h3, h4, h5, h6, p, span, a, li, .kicker, .desc, .tech-tag, .filter-chip {
    font-family: var(--font-family-primary) !important;
}

/* ==========================================================================
   UNIFICACIÓN CROMÁTICA CORPORATIVA LÍNEA DIRECTA (100% ROJO)
   ========================================================================== */
.card-visual {
    color: var(--lda-red) !important;
}

.card-visual svg {
    color: var(--lda-red) !important;
}

.card-visual svg path[fill]:not([fill="none"]),
.card-visual svg circle[fill]:not([fill="none"]),
.card-visual svg rect[fill]:not([fill="none"]) {
    fill: currentColor !important;
}

.card-visual svg path[stroke],
.card-visual svg circle[stroke],
.card-visual svg rect[stroke],
.card-visual svg line[stroke] {
    stroke: currentColor !important;
}

/* Halos de iconos 100% Línea Directa (Cero amarillo/azul/morado) */
.card-visual::after,
[data-accent="red"] .card-visual::after,
[data-accent="amber"] .card-visual::after,
[data-accent="blue"] .card-visual::after,
[data-accent="purple"] .card-visual::after {
    background: var(--lda-red) !important;
    opacity: 0.08 !important;
}

/* Spotlights de tarjeta 100% Línea Directa */
.apple-card,
[data-accent="red"],
[data-accent="amber"],
[data-accent="blue"],
[data-accent="purple"] {
    --card-spotlight: rgba(204, 51, 51, 0.08) !important;
}

[data-theme="dark"] .apple-card,
[data-theme="dark"] [data-accent="red"],
[data-theme="dark"] [data-accent="amber"],
[data-theme="dark"] [data-accent="blue"],
[data-theme="dark"] [data-accent="purple"] {
    --card-spotlight: rgba(204, 51, 51, 0.18) !important;
}

/* Puntos indicadores y kickers en Rojo Línea Directa */
.kicker-dot {
    background: var(--lda-red) !important;
    box-shadow: 0 0 8px rgba(204, 51, 51, 0.6) !important;
}
"""

core_css = css.strip() + "\n\n" + corporate_tail_core.strip() + "\n"

# For styles_bitacora.css, adjust font path if needed or keep both compatible
styles_css = core_css.replace("url('../fonts/CircularXXSub-", "url('../assets/fonts/CircularXXSub-")

with open(BITACORA_CORE, "w", encoding="utf-8") as f:
    f.write(core_css)
print(f"[+] bitacora-core.css saved: {len(core_css.splitlines())} lines")

with open(STYLES_BITACORA, "w", encoding="utf-8") as f:
    f.write(styles_css)
print(f"[+] styles_bitacora.css saved: {len(styles_css.splitlines())} lines")
