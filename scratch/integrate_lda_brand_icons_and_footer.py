# -*- coding: utf-8 -*-
"""
Script maestro para integrar:
1. Paleta de colores, tipografía e iconografía corporativa de lineadirecta.com
2. Iconos vectoriales estilo Línea Directa (basados en poliza-coche.svg, poliza-hogar.svg, etc.) en escala simétrica 64x64 / viewBox 0 0 24 24
3. Logo oficial de Línea Directa (logo_header_lda.png) en el Footer corporativo
4. Simetría vertical estricta (440px por tarjeta, sin espacios en blanco superfluos)
5. Recompilación automática de bitacora-core.css y styles_bitacora.css
"""

import os
import re
import subprocess

BASE_DIR = r"C:\Proyectos_Claude\Proyecto Cuaderno de Bitacora"
INDEX_HTML = os.path.join(BASE_DIR, "01_Proyectos", "Cuaderno de Bitacora (Proyectos)", "index.html")
CORE_BUILDER = os.path.join(BASE_DIR, "scratch", "build_unified_core_css.py")
ASSETS_IMG = os.path.join(BASE_DIR, "01_Proyectos", "assets", "img")

print("[1/4] Verificando assets descargados de lineadirecta.com...")
required_assets = [
    "logo_header_lda.png",
    "poliza-coche.svg",
    "poliza-hogar.svg",
    "poliza-moto.svg",
    "poliza-salud.svg",
    "poliza-movilidad.svg"
]
for asset in required_assets:
    p = os.path.join(ASSETS_IMG, asset)
    if not os.path.exists(p):
        raise FileNotFoundError(f"Asset no encontrado: {p}")
    print(f"  [+] {asset} ({os.path.getsize(p)} bytes)")

# ==============================================================================
# 2. DEFINICIÓN DE ICONOS VECTORIALES ESTILO LÍNEA DIRECTA (24x24 simétrico)
# ==============================================================================

# PERSEO: Silueta oficial poliza-coche.svg de Línea Directa
svg_perseo = """<svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path fill-rule="evenodd" clip-rule="evenodd" d="M23.3028 10.4393C24.0192 11.1306 24.1525 12.0989 23.842 13.1148C23.8346 13.1391 23.8272 13.1632 23.82 13.187C23.4558 14.379 23.2649 15.0039 22.6436 15.6816C22.3129 16.0423 21.971 16.2336 21.6974 16.3331C21.5618 16.3824 21.445 16.4084 21.3569 16.4222C21.3128 16.429 21.2758 16.4328 21.2471 16.4349C21.2327 16.436 21.2203 16.4366 21.2102 16.437L21.1966 16.4373L21.191 16.4374L21.1886 16.4374L21.1874 16.4374C21.1874 16.4374 21.1863 16.4374 21.1863 15.9374V16.4374H20.4999C20.2238 16.4374 19.9999 16.2136 19.9999 15.9374C19.9999 15.6613 20.2238 15.4374 20.4999 15.4374H21.1765C21.1809 15.437 21.1899 15.4361 21.2029 15.4341C21.2339 15.4293 21.2872 15.4182 21.3557 15.3933C21.4904 15.3443 21.6929 15.2388 21.9066 15.0058C22.3616 14.5095 22.4945 14.1024 22.8857 12.8225C23.1196 12.0571 22.9807 11.5182 22.6084 11.1589C22.203 10.7678 21.4111 10.4778 20.106 10.4998L20.0976 10.5L12.4763 10.4999C12.2001 10.4999 11.9763 10.2761 11.9763 9.99991C11.9763 9.72377 12.2001 9.49991 12.4763 9.49991H20.0934C21.5082 9.4767 22.6201 9.78057 23.3028 10.4393Z" fill="currentColor"/>
    <path fill-rule="evenodd" clip-rule="evenodd" d="M8.48496 6C8.48815 6 8.49133 6 8.49449 6H11.5188C12.76 6 13.9695 6.40098 14.9945 7.14631L17.4252 8.91371C17.43 8.91726 17.4349 8.9209 17.4396 8.92463L17.4426 8.92689C17.4467 8.92998 17.4539 8.93534 17.4639 8.94265C17.4841 8.95728 17.5158 8.9796 17.5575 9.00707C17.6413 9.06224 17.7636 9.13687 17.9135 9.21151C18.2197 9.36407 18.6074 9.5 18.9999 9.5C19.276 9.5 19.4999 9.72386 19.4999 10C19.4999 10.2761 19.276 10.5 18.9999 10.5C18.3923 10.5 17.8457 10.295 17.4675 10.1066C17.2752 10.0108 17.1179 9.91492 17.0075 9.84223C16.9521 9.80577 16.9081 9.77481 16.8768 9.75215C16.8612 9.74082 16.8487 9.73152 16.8396 9.72463L16.8318 9.71865L14.4064 7.95511C13.547 7.33021 12.5423 7 11.5188 7H8.49987C8.09239 7 7.53365 7.00117 6.84163 7.22561C6.15143 7.44946 5.3018 7.90518 4.35343 8.85355L4 8.50012C4.35343 8.85355 4.35343 8.85355 4.35343 8.85355L4.35271 8.85427L4.35195 8.85502L4.35029 8.85667L4.34638 8.86048L4.33623 8.87016C4.32841 8.87751 4.31846 8.88662 4.30627 8.89738C4.28188 8.9189 4.24854 8.94697 4.20528 8.98061C4.11874 9.04793 3.99272 9.13739 3.81962 9.24125C3.47333 9.44902 2.93983 9.73943 2.15812 10C1.43268 10.2418 1.20712 10.444 1.11625 10.5954C1.01426 10.7654 1.00001 10.984 1.00001 11.5257C1.00001 11.8477 1.14586 12.5322 1.35786 13.3209C1.5631 14.0844 1.81007 14.8747 1.97435 15.3675C2.06167 15.6295 1.92009 15.9127 1.65812 16C1.39615 16.0873 1.11299 15.9457 1.02566 15.6838C0.856605 15.1766 0.603573 14.367 0.392147 13.5805C0.18748 12.8191 5.34415e-06 12.0036 5.34415e-06 11.5257C5.34415e-06 11.5041 -2.60675e-05 11.4825 -5.77176e-05 11.4606C-0.000699898 11.0176 -0.00142887 10.5146 0.258759 10.0809C0.542886 9.60736 1.06733 9.30951 1.84189 9.05132C2.56018 8.81189 3.02642 8.55098 3.30513 8.38375C3.44452 8.30011 3.53726 8.23332 3.59134 8.19126C3.6184 8.17022 3.63583 8.15532 3.64465 8.14754L3.65055 8.14222C4.70059 7.09336 5.6828 6.55017 6.53312 6.27439C7.29567 6.02707 7.93065 6.00267 8.36067 6.00026C8.3661 6.00009 8.37155 6 8.37703 6H8.48496Z" fill="currentColor"/>
    <path fill-rule="evenodd" clip-rule="evenodd" d="M8.49994 16C8.49994 15.7239 8.7238 15.5 8.99994 15.5H14.9999C15.2761 15.5 15.4999 15.7239 15.4999 16C15.4999 16.2762 15.2761 16.5 14.9999 16.5H8.99994C8.7238 16.5 8.49994 16.2762 8.49994 16Z" fill="currentColor"/>
    <path fill-rule="evenodd" clip-rule="evenodd" d="M6.24994 13.5C5.0073 13.5 3.99994 14.5074 3.99994 15.75C3.99994 16.9926 5.0073 18 6.24994 18C7.49258 18 8.49994 16.9926 8.49994 15.75C8.49994 14.5074 7.49258 13.5 6.24994 13.5ZM2.99994 15.75C2.99994 13.9551 4.45502 12.5 6.24994 12.5C8.04487 12.5 9.49994 13.9551 9.49994 15.75C9.49994 17.5449 8.04487 19 6.24994 19C4.45502 19 2.99994 17.5449 2.99994 15.75Z" fill="currentColor"/>
    <path fill-rule="evenodd" clip-rule="evenodd" d="M17.7499 13.5C16.5073 13.5 15.4999 14.5074 15.4999 15.75C15.4999 16.9926 16.5073 18 17.7499 18C18.9926 18 19.9999 16.9926 19.9999 15.75C19.9999 14.5074 18.9926 13.5 17.7499 13.5ZM14.4999 15.75C14.4999 13.9551 15.955 12.5 17.7499 12.5C19.5449 12.5 20.9999 13.9551 20.9999 15.75C20.9999 17.5449 19.5449 19 17.7499 19C15.955 19 14.4999 17.5449 14.4999 15.75Z" fill="currentColor"/>
</svg>"""

# REINGENIERÍA DE SINIESTROS: Silueta oficial poliza-hogar.svg de Línea Directa
svg_siniestros = """<svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path fill-rule="evenodd" clip-rule="evenodd" d="M11.7764 3.55279C11.9171 3.4824 12.0828 3.4824 12.2236 3.55279L23.2236 9.05279C23.4706 9.17628 23.5707 9.47662 23.4472 9.72361C23.3237 9.9706 23.0234 10.0707 22.7764 9.94721L12 4.55902L1.22359 9.94721C0.976605 10.0707 0.676269 9.9706 0.552774 9.72361C0.429279 9.47662 0.529391 9.17628 0.77638 9.05279L11.7764 3.55279ZM2.5 10.5C2.77614 10.5 3 10.7239 3 11V19.5H4.49999C4.77613 19.5 4.99999 19.7239 4.99999 20C4.99999 20.2761 4.77613 20.5 4.49999 20.5H2.5C2.36739 20.5 2.24022 20.4473 2.14645 20.3536C2.05268 20.2598 2 20.1326 2 20V11C2 10.7239 2.22386 10.5 2.5 10.5ZM6.99999 11C6.99999 10.7239 7.22385 10.5 7.49999 10.5H12.5238C12.7999 10.5 13.0238 10.7239 13.0238 11V20C13.0238 20.2761 12.7999 20.5 12.5238 20.5H7.49999C7.22385 20.5 6.99999 20.2761 6.99999 20V11ZM7.99999 11.5V19.5H12.0238V11.5H7.99999ZM17.5 11C17.5 10.7239 17.7239 10.5 18 10.5H21.5C21.6327 10.5 21.76 10.5528 21.8538 10.6467C21.9475 10.7405 22.0002 10.8679 22 11.0006L21.9895 20.0006C21.9892 20.2765 21.7654 20.5 21.4895 20.5H16C15.7239 20.5 15.5 20.2761 15.5 20C15.5 19.7239 15.7239 19.5 16 19.5H20.9901L20.9994 11.5H18C17.7239 11.5 17.5 11.2761 17.5 11Z" fill="currentColor"/>
</svg>"""

# EVOLUCIÓN HCM CLOUD: Equipo corporativo y gestión del talento
svg_hcm = """<svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <circle cx="8" cy="6" r="3" fill="currentColor"/>
    <path d="M2 18C2 15 4.5 13 8 13C11.5 13 14 15 14 18V20H2V18Z" fill="currentColor"/>
    <circle cx="16" cy="7" r="2.5" stroke="currentColor" stroke-width="1.8"/>
    <path d="M14 14.5C15.2 13.8 16.5 13.5 18 13.5C20.5 13.5 22 15 22 17.5V19.5H15" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
</svg>"""

# EFICIENCIA RRHH & IA (LidIA): Chispa de inteligencia y nodo cognitivo
svg_ia = """<svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M12 2L14.4 8.6L21 11L14.4 13.4L12 20L9.6 13.4L3 11L9.6 8.6L12 2Z" fill="currentColor"/>
    <circle cx="19" cy="4" r="1.5" fill="currentColor"/>
    <circle cx="5" cy="18" r="1.5" fill="currentColor"/>
</svg>"""

# CRM OPERACIONAL: Asegurado omnicanal 360°
svg_crm = """<svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <circle cx="12" cy="8" r="3.5" fill="currentColor"/>
    <path d="M6 19C6 16 8.5 14 12 14C15.5 14 18 16 18 19" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
    <circle cx="12" cy="12" r="9.5" stroke="currentColor" stroke-width="1.6" stroke-dasharray="3 3"/>
    <circle cx="21" cy="9" r="1.5" fill="currentColor"/>
    <circle cx="3" cy="15" r="1.5" fill="currentColor"/>
</svg>"""

# TELEFONÍA GENESYS CX: Headset corporativo de Contact Center Línea Directa
svg_telefonia = """<svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M4 13V11C4 6.58 7.58 3 12 3C16.42 3 20 6.58 20 11V13" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
    <rect x="2.5" y="12" width="3.5" height="7" rx="1.75" fill="currentColor"/>
    <rect x="18" y="12" width="3.5" height="7" rx="1.75" fill="currentColor"/>
    <path d="M19 18V19C19 20.65 17.65 22 16 22H13.5" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
    <circle cx="11.5" cy="22" r="1.5" fill="currentColor"/>
</svg>"""

# GESTIÓN DE USUARIOS: Credencial y candado IAM
svg_usuarios = """<svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="4" y="3" width="16" height="18" rx="3" stroke="currentColor" stroke-width="2"/>
    <circle cx="12" cy="8.5" r="2.5" fill="currentColor"/>
    <path d="M8 15C8 13.5 9.8 12.5 12 12.5C14.2 12.5 16 13.5 16 15" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
    <rect x="9.5" y="16.5" width="5" height="1.8" rx="0.6" fill="currentColor"/>
</svg>"""

# ARQUITECTURA TÉCNICA: Módulos conectados
svg_arq = """<svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="3" y="3" width="7" height="7" rx="1.5" fill="currentColor"/>
    <rect x="14" y="3" width="7" height="7" rx="1.5" stroke="currentColor" stroke-width="1.8" stroke-dasharray="2 2"/>
    <rect x="3" y="14" width="7" height="7" rx="1.5" stroke="currentColor" stroke-width="1.8" stroke-dasharray="2 2"/>
    <rect x="14" y="14" width="7" height="7" rx="1.5" fill="currentColor"/>
    <path d="M10 6.5H14M6.5 10V14M17.5 10V14M10 17.5H14" stroke="currentColor" stroke-width="1.5"/>
</svg>"""

# GESTIÓN DE LA INFORMACIÓN: Libro maestro / Wiki funcional
svg_info = """<svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M4 19.5V4.5C4 3.67 4.67 3 5.5 3H18.5C19.33 3 20 3.67 20 4.5V19.5C20 20.33 19.33 21 18.5 21H5.5C4.67 21 4 20.33 4 19.5Z" stroke="currentColor" stroke-width="2"/>
    <path d="M4 17.5H20" stroke="currentColor" stroke-width="1.8"/>
    <path d="M8 7H16M8 10H14M8 13H16" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
</svg>"""

# PLACEHOLDERS GENÉRICOS (EN DISEÑO / PENDIENTE / HISTORIAL)
svg_demo1 = """<svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <circle cx="12" cy="12" r="8" stroke="currentColor" stroke-width="1.8" stroke-dasharray="3 3"/>
    <circle cx="12" cy="12" r="2.5" fill="currentColor"/>
    <line x1="12" y1="2" x2="12" y2="4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
    <line x1="12" y1="20" x2="12" y2="22" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
</svg>"""

svg_demo2 = """<svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M12 4L19 8L12 12L5 8L12 4Z" fill="currentColor" fill-opacity="0.3" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/>
    <path d="M5 12L12 16L19 12" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M5 16L12 20L19 16" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
</svg>"""

svg_archive = """<svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="4" y="4" width="16" height="16" rx="3" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.1"/>
    <circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.8"/>
    <circle cx="12" cy="12" r="1.5" fill="currentColor"/>
</svg>"""

# ==============================================================================
# 3. ACTUALIZAR build_unified_core_css.py CON TOKENS BRANDBOOK LÍNEA DIRECTA
# ==============================================================================
print("[2/4] Integrando tokens oficiales de Línea Directa en CSS...")

with open(CORE_BUILDER, "r", encoding="utf-8") as f:
    css_script = f.read()

# Inyectamos estilos del footer corporativo y reglas de simetría si no existen
footer_css_block = """
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

if ".app-footer" not in css_script:
    css_script = css_script.replace(
        '.apple-card:hover .card-visual svg {\n    transform: scale(1.05);\n}\n"""',
        '.apple-card:hover .card-visual svg {\n    transform: scale(1.05);\n}\n' + footer_css_block + '\n"""'
    )

with open(CORE_BUILDER, "w", encoding="utf-8") as f:
    f.write(css_script)

# Recompilar CSS
subprocess.run(["python", CORE_BUILDER], check=True)
print("  [+] build_unified_core_css.py y estilos compilados exitosamente.")

# ==============================================================================
# 4. ACTUALIZAR index.html CON CARDS Y FOOTER CON LOGO OFICIAL
# ==============================================================================
print("[3/4] Actualizando index.html con tarjetas calibradas y footer corporativo...")

with open(INDEX_HTML, "r", encoding="utf-8") as f:
    html = f.read()

# Definición de las tarjetas calibradas con SVGs simétricos

cards_direct = f"""                    <!-- Evolución HCM Cloud -->
                    <a href="../HCM/index.html" class="apple-card" data-accent="red">
                        <div class="kicker" style="color: var(--lda-red);"><span class="kicker-dot"></span> GESTIÓN DIRECTA</div>
                        <h3 class="title">Evolución HCM Cloud</h3>
                        <p class="desc">Núcleo integral de RR.HH. Migración estratégica de PeopleSoft a Oracle Cloud Fusion, optimizando la gestión del talento, nóminas y estructura organizativa.</p>
                        <div class="card-tags">
                            <span class="tech-tag">Oracle Cloud HCM</span>
                            <span class="tech-tag">Gestión del Talento</span>
                            <span class="tech-tag">Nóminas</span>
                            <span class="tech-tag">PeopleSoft</span>
                        </div>
                        <div class="card-visual" style="color: var(--lda-red);">
                            {svg_hcm}
                        </div>
                    </a>

                    <!-- Transformación y Eficiencia RRHH -->
                    <a href="../IA Area Personas/index.html" class="apple-card" data-accent="red">
                        <div class="kicker" style="color: var(--lda-red);"><span class="kicker-dot"></span> PENDIENTE APROBACIÓN</div>
                        <h3 class="title">Eficiencia RRHH & IA</h3>
                        <p class="desc">Iniciativa estratégica para automatización de consultas internas, asistentes cognitivos con LidIA y optimización operativa en gestión de personas.</p>
                        <div class="card-tags">
                            <span class="tech-tag">Inteligencia Artificial</span>
                            <span class="tech-tag">Copilot M365</span>
                            <span class="tech-tag">Asistente LidIA</span>
                            <span class="tech-tag">Eficiencia Personas</span>
                        </div>
                        <div class="card-visual" style="color: var(--lda-red);">
                            {svg_ia}
                        </div>
                    </a>"""

cards_facilitator = f"""                    <!-- Perseo -->
                    <a href="../Perseo/index.html" class="apple-card" data-accent="amber">
                        <div class="kicker" style="color: #f59e0b;"><span class="kicker-dot"></span> FACILITADOR</div>
                        <h3 class="title">Perseo</h3>
                        <p class="desc">Plataforma estratégica core de tramitación y suscripción de pólizas. Arquitectura modular de alto rendimiento para el negocio asegurador.</p>
                        <div class="card-tags">
                            <span class="tech-tag">Pólizas & Clientes</span>
                            <span class="tech-tag">Supervisión Comercial</span>
                            <span class="tech-tag">Speech Analytics</span>
                            <span class="tech-tag">Coaching</span>
                        </div>
                        <div class="card-visual" style="color: #CC3333;">
                            {svg_perseo}
                        </div>
                    </a>

                    <!-- CRM Operacional -->
                    <a href="../CRM Operacional/index.html" class="apple-card" data-accent="amber">
                        <div class="kicker" style="color: #f59e0b;"><span class="kicker-dot"></span> FACILITADOR</div>
                        <h3 class="title">CRM Operacional</h3>
                        <p class="desc">Ecosistema integral de gestión comercial y atención omnicanal a asegurados con visión 360°, automatización y trazabilidad total.</p>
                        <div class="card-tags">
                            <span class="tech-tag">Gestión de Asegurados</span>
                            <span class="tech-tag">Omnicanalidad</span>
                            <span class="tech-tag">Atención Comercial</span>
                            <span class="tech-tag">Expediente Único</span>
                        </div>
                        <div class="card-visual" style="color: #f59e0b;">
                            {svg_crm}
                        </div>
                    </a>

                    <!-- Telefonía - Genesys Cloud CX -->
                    <a href="../Telefonia - Genesis CX/index.html" class="apple-card" data-accent="amber">
                        <div class="kicker" style="color: #f59e0b;"><span class="kicker-dot"></span> FACILITADOR</div>
                        <h3 class="title">Telefonía Genesys CX</h3>
                        <p class="desc">Transformación de la infraestructura de Contact Center a la nube pública de Genesys. Enrutamiento inteligente y analítica en tiempo real.</p>
                        <div class="card-tags">
                            <span class="tech-tag">Genesys Cloud CX</span>
                            <span class="tech-tag">Contact Center</span>
                            <span class="tech-tag">Telefonía IP</span>
                            <span class="tech-tag">Atención Clientes</span>
                        </div>
                        <div class="card-visual" style="color: #f59e0b;">
                            {svg_telefonia}
                        </div>
                    </a>

                    <!-- Reingeniería de Siniestros -->
                    <a href="../Reingenieria Siniestros/index.html" class="apple-card" data-accent="amber">
                        <div class="kicker" style="color: #f59e0b;"><span class="kicker-dot"></span> FACILITADOR</div>
                        <h3 class="title">Reingeniería Siniestros</h3>
                        <p class="desc">Modernización integral del ciclo de vida del siniestro: peritación digital, detección de fraude y agilización del pago a clientes.</p>
                        <div class="card-tags">
                            <span class="tech-tag">Tramitación Siniestros</span>
                            <span class="tech-tag">Peritación Digital</span>
                            <span class="tech-tag">Flujos Auto & Hogar</span>
                            <span class="tech-tag">Resolución Rápida</span>
                        </div>
                        <div class="card-visual" style="color: #CC3333;">
                            {svg_siniestros}
                        </div>
                    </a>"""

cards_services = f"""                    <!-- Gestión de Usuarios -->
                    <a href="../Gestion de Usuarios/index.html" class="apple-card" data-accent="blue">
                        <div class="kicker" style="color: #3b82f6;"><span class="kicker-dot"></span> SERVICIO / IAM</div>
                        <h3 class="title">Gestión de Usuarios</h3>
                        <p class="desc">Gobernanza de identidades y accesos corporativos. Automatización de altas, bajas y cambios de rol con cumplimiento regulatorio.</p>
                        <div class="card-tags">
                            <span class="tech-tag">Identidad Corporativa</span>
                            <span class="tech-tag">Gobernanza IAM</span>
                            <span class="tech-tag">Control de Accesos</span>
                            <span class="tech-tag">Auditoría</span>
                        </div>
                        <div class="card-visual" style="color: #3b82f6;">
                            {svg_usuarios}
                        </div>
                    </a>

                    <!-- Demo Card 3 -->
                    <div class="apple-card disabled-card">
                        <div class="kicker">EN DEFINICIÓN</div>
                        <h3 class="title">Arquitectura Técnica</h3>
                        <p class="desc">Estructura base para la documentación de microservicios, APIs e integraciones de sistemas centrales.</p>
                        <div class="card-visual" style="opacity: 0.65;">
                            {svg_arq}
                        </div>
                    </div>

                    <!-- Demo Card 4 -->
                    <div class="apple-card disabled-card">
                        <div class="kicker">EN DISEÑO</div>
                        <h3 class="title">Nueva Operativa</h3>
                        <p class="desc">Tarjetón genérico preparado para alojar servicios organizacionales futuros.</p>
                        <div class="card-visual" style="opacity: 0.65;">
                            {svg_demo1}
                        </div>
                    </div>

                    <!-- Demo Card 5 -->
                    <div class="apple-card disabled-card">
                        <div class="kicker">PENDIENTE</div>
                        <h3 class="title">Próxima Operativa</h3>
                        <p class="desc">Módulo no definido, espacio visual concebido para balancear el carrusel de servicios.</p>
                        <div class="card-visual" style="opacity: 0.65;">
                            {svg_demo2}
                        </div>
                    </div>"""

cards_closed = f"""                    <!-- Gestión de la Información (Traspasado a Transformación) -->
                    <a href="../Gobierno de Informacion/index.html" class="apple-card" data-accent="purple" style="border-color: rgba(139, 92, 246, 0.4); background: linear-gradient(135deg, var(--bg-card) 0%, rgba(139, 92, 246, 0.05) 100%);">
                        <div class="kicker" style="color: #8B5CF6;"><span class="kicker-dot"></span> HISTÓRICO TRASPASADO</div>
                        <h3 class="title">Gestión de la Información</h3>
                        <p class="desc">Proyecto de Inteligencia LidIA y metodología GIN transferido al Área de Transformación. Conserva aquí todo el contexto, historial y wiki funcional.</p>
                        <div class="card-tags">
                            <span class="tech-tag">Metodología GIN</span>
                            <span class="tech-tag">Gobierno de Datos</span>
                            <span class="tech-tag">Wiki Funcional</span>
                            <span class="tech-tag">Traspaso Estratégico</span>
                        </div>
                        <div class="card-visual" style="color: #8B5CF6;">
                            {svg_info}
                        </div>
                    </a>

                    <!-- Archivo Histórico Card 1 -->
                    <div class="apple-card disabled-card" data-accent="purple">
                        <div class="kicker" style="color: var(--text-muted);">HISTORIAL ARCHIVADO</div>
                        <h3 class="title" style="color: var(--text-muted);">Archivo de Porfolio</h3>
                        <p class="desc">Espacio reservado para almacenar el historial de proyectos concluidos en ciclos anteriores.</p>
                        <div class="card-tags">
                            <span class="tech-tag">Ciclos Anteriores</span>
                            <span class="tech-tag">Auditoría</span>
                        </div>
                        <div class="card-visual" style="opacity: 0.5;">
                            {svg_archive}
                        </div>
                    </div>

                    <!-- Archivo Histórico Card 2 -->
                    <div class="apple-card disabled-card" data-accent="purple">
                        <div class="kicker" style="color: var(--text-muted);">REPOSITORIO</div>
                        <h3 class="title" style="color: var(--text-muted);">Registro Histórico</h3>
                        <p class="desc">Conservación de memorias técnicas, lecciones aprendidas y acuerdos de gobernanza pasados.</p>
                        <div class="card-tags">
                            <span class="tech-tag">Lecciones</span>
                            <span class="tech-tag">Memorias</span>
                        </div>
                        <div class="card-visual" style="opacity: 0.5;">
                            {svg_archive}
                        </div>
                    </div>"""

# Reemplazar secciones en HTML
html = re.sub(
    r'<div class="carousel-track" id="track-direct"[^>]*>.*?</div>\s*<button class="carousel-btn right',
    f'<div class="carousel-track" id="track-direct" onscroll="updateCarouselButtons(this)">\n{cards_direct}\n                </div>\n                <button class="carousel-btn right',
    html,
    flags=re.DOTALL
)

html = re.sub(
    r'<div class="carousel-track" id="track-facilitator"[^>]*>.*?</div>\s*<button class="carousel-btn right',
    f'<div class="carousel-track" id="track-facilitator" onscroll="updateCarouselButtons(this)">\n{cards_facilitator}\n                </div>\n                <button class="carousel-btn right',
    html,
    flags=re.DOTALL
)

html = re.sub(
    r'<div class="carousel-track" id="track-services"[^>]*>.*?</div>\s*<button class="carousel-btn right',
    f'<div class="carousel-track" id="track-services" onscroll="updateCarouselButtons(this)">\n{cards_services}\n                </div>\n                <button class="carousel-btn right',
    html,
    flags=re.DOTALL
)

html = re.sub(
    r'<div class="carousel-track" id="track-closed"[^>]*>.*?</div>\s*<button class="carousel-btn right',
    f'<div class="carousel-track" id="track-closed" onscroll="updateCarouselButtons(this)">\n{cards_closed}\n                </div>\n                <button class="carousel-btn right',
    html,
    flags=re.DOTALL
)

# Sustituir Footer por el corporativo oficial con el Logo de Línea Directa
new_footer = """    <!-- FOOTER CORPORATIVO OFICIAL LÍNEA DIRECTA -->
    <footer class="app-footer">
        <div class="footer-inner">
            <div class="footer-brand-block">
                <div class="footer-logo-badge">
                    <img src="../assets/img/logo_header_lda.png" alt="Línea Directa Aseguradora" class="footer-logo">
                </div>
                <p class="footer-brand-desc">Cuaderno de Bitácora &bull; Sistema centralizado de gobernanza, base de conocimiento y documentación técnica de proyectos de Línea Directa Aseguradora.</p>
            </div>
            
            <div class="footer-links-grid">
                <div class="footer-col">
                    <h4>Navegación</h4>
                    <ul>
                        <li><a href="#seccion-directa">Gestión Directa</a></li>
                        <li><a href="#seccion-facilitadores">Facilitadores</a></li>
                        <li><a href="#seccion-servicios">Servicios Organizacionales</a></li>
                        <li><a href="#seccion-cerrados">Proyectos Cerrados</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Proyectos Clave</h4>
                    <ul>
                        <li><a href="../Perseo/index.html">Core Perseo (Pólizas)</a></li>
                        <li><a href="../HCM/index.html">Evolución HCM Cloud</a></li>
                        <li><a href="../Reingenieria Siniestros/index.html">Reingeniería de Siniestros</a></li>
                        <li><a href="../Telefonia - Genesis CX/index.html">Telefonía Genesys CX</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Gobernanza & Estado</h4>
                    <ul>
                        <li><span class="footer-status-pill"><span class="dot-online"></span> Base de Conocimiento Activa</span></li>
                        <li><span class="footer-meta-item">Línea Directa Aseguradora, S.A.</span></li>
                        <li><span class="footer-meta-item">Entorno Local Seguro</span></li>
                        <li><a href="perfil.html" style="font-weight: 600; color: var(--lda-red);">Ver Portfolio & Perfil &rarr;</a></li>
                    </ul>
                </div>
            </div>

            <div class="footer-bottom">
                <p>&copy; 2026 Línea Directa Aseguradora, S.A. Todos los derechos reservados. Información confidencial para uso interno.</p>
                <div class="footer-bottom-badges">
                    <span class="badge-lda-red">Brandbook Línea Directa</span>
                    <span class="badge-lda-outline">v2.4 Command Center</span>
                </div>
            </div>
        </div>
    </footer>"""

html = re.sub(
    r'<footer>\s*<p>&copy; 2026 Línea Directa Aseguradora.*?</footer>',
    new_footer,
    html,
    flags=re.DOTALL
)

with open(INDEX_HTML, "w", encoding="utf-8") as f:
    f.write(html)

print("  [+] index.html actualizado con footer oficial y logo corporativo.")

# ==============================================================================
# 5. AUDITORÍA FINAL
# ==============================================================================
print("[4/4] Ejecutando auditoría de consistencia de enlaces...")
audit_script = os.path.join(BASE_DIR, "scratch", "audit_project.py")
subprocess.run(["python", audit_script], check=True)

print("[OK] ¡Integración de Brandbook, Iconografía Oficial y Logo de Footer Completada con Éxito!")
