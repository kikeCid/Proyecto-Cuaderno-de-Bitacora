# -*- coding: utf-8 -*-
"""
Script para aplicar las correcciones de Brandbook de Línea Directa:
1. Reemplazar etiquetas no pertinentes (como 'hexagonal') por etiquetas 100% reales de la wiki de cada proyecto.
2. Posicionar las etiquetas inmediatamente debajo de la descripción del proyecto, eliminando espacios en blanco innecesarios.
3. Calibrar la simetría y proporciones de las tarjetas (altura armónica de 440px).
4. Rediseñar los iconos vectoriales con el estilo del Brandbook de Línea Directa:
   - Perseo: Vehículo Línea Directa con Escudo de Cobertura Aseguradora.
   - HCM Cloud: Ecosistema de Personas/Talento con Nube Corporativa.
   - Eficiencia RRHH & IA: Chispa de Innovación LidIA con nodo cognitivo de Personas.
   - CRM Operacional: Ficha 360° del Asegurado con órbita omnicanal.
   - Telefonía Genesys CX: Auriculares Headset de Contact Center Línea Directa.
   - Reingeniería de Siniestros: Escudo de Asistencia en Siniestros y Peritación.
   - Gestión de Usuarios: Credencial corporativa de empleado con candado IAM.
   - Gestión de la Información: Libro Maestro de Gobernanza GIN con wiki permanente.
"""

import os
import re
import subprocess

BASE_DIR = r"C:\Proyectos_Claude\Proyecto Cuaderno de Bitacora"
CORE_PY = os.path.join(BASE_DIR, "scratch", "build_unified_core_css.py")
INDEX_HTML = os.path.join(BASE_DIR, "01_Proyectos", "Cuaderno de Bitacora (Proyectos)", "index.html")

# ==============================================================================
# 1. ACTUALIZAR CSS PARA SIMETRÍA PERFECTA EN TARJETAS
# ==============================================================================
with open(CORE_PY, "r", encoding="utf-8") as f:
    css_py = f.read()

# Actualizamos la regla .apple-card en clean_addons_css para altura 440px y espaciados armoniosos
css_py = re.sub(
    r"\.apple-card\s*\{[^}]*height:\s*\d+px;[^}]*\}",
    """.apple-card {
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
}""",
    css_py,
    flags=re.DOTALL
)

# Actualizamos .card-tags para que esté inmediatamente debajo de la descripción
css_py = re.sub(
    r"\.card-tags\s*\{[^}]*\}",
    """.card-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin: 4px 0 14px 0;
    position: relative;
    z-index: 2;
}""",
    css_py
)

# Actualizamos .apple-card .desc para que el texto respire pero no cree espacios vacíos
css_py = re.sub(
    r"\.apple-card \.desc\s*\{[^}]*\}",
    """.apple-card .desc {
    font-size: 0.86rem;
    line-height: 1.45;
    color: var(--text-sec);
    margin-bottom: 8px;
    position: relative;
    z-index: 2;
}""",
    css_py
)

# Actualizamos .card-visual para altura 140px perfectamente simétrica
css_py = re.sub(
    r"\.card-visual\s*\{[^}]*\}",
    """.card-visual {
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
}""",
    css_py
)

with open(CORE_PY, "w", encoding="utf-8") as f:
    f.write(css_py)

print("[+] build_unified_core_css.py ajustado con simetría y proporciones de tarjeta.")
subprocess.run(["python", CORE_PY], check=True)
print("[+] CSS unificados recompilados exitosamente.")

# ==============================================================================
# 2. ICONOS BRANDBOOK LÍNEA DIRECTA Y ETIQUETAS REALES DEL VAULT
# ==============================================================================

# SVG 1: HCM Cloud (Talento / Personas y Nube Corporativa)
svg_hcm = """<svg width="80" height="80" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M25 34 C21 34 18 31 18 27 C18 23 21 20 25 20 C26 15 31 11 37 11 C43 11 48 14 49 19 C51 18 53 18 55 18 C60 18 64 22 64 27 C64 31 61 34 57 34" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" fill="currentColor" fill-opacity="0.08"/>
    <circle cx="40" cy="40" r="6" stroke="currentColor" stroke-width="2.3" fill="currentColor" fill-opacity="0.25"/>
    <path d="M30 58 C30 52 34 49 40 49 C46 49 50 52 50 58" stroke="currentColor" stroke-width="2.3" stroke-linecap="round"/>
    <circle cx="24" cy="46" r="4.5" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.15"/>
    <path d="M16 63 C16 58 19 56 24 56 C27 56 29 57 31 59" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
    <circle cx="56" cy="46" r="4.5" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.15"/>
    <path d="M49 59 C51 57 53 56 56 56 C61 56 64 58 64 63" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
    <line x1="20" y1="67" x2="60" y2="67" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
</svg>"""

# SVG 2: Eficiencia RRHH & Asistente IA (Chispa de Innovación LidIA y Nodo Cognitivo)
svg_ia = """<svg width="80" height="80" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M40 16 C40 29 42 38 55 40 C42 42 40 51 40 64 C40 51 38 42 25 40 C38 38 40 29 40 16 Z" stroke="currentColor" stroke-width="2.3" fill="currentColor" fill-opacity="0.22" stroke-linejoin="round"/>
    <circle cx="40" cy="40" r="4" fill="currentColor"/>
    <circle cx="21" cy="21" r="3" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.2"/>
    <circle cx="59" cy="21" r="3" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.2"/>
    <circle cx="21" cy="59" r="3" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.2"/>
    <circle cx="59" cy="59" r="3" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.2"/>
    <line x1="24" y1="24" x2="31" y2="31" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-dasharray="3 3"/>
    <line x1="56" y1="24" x2="49" y2="31" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-dasharray="3 3"/>
    <line x1="24" y1="56" x2="31" y2="49" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-dasharray="3 3"/>
    <line x1="56" y1="56" x2="49" y2="49" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-dasharray="3 3"/>
</svg>"""

# SVG 3: Perseo (Vehículo Línea Directa con Escudo de Cobertura Aseguradora)
svg_perseo = """<svg width="80" height="80" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M22 44 L26 28 C27 24 30 22 34 22 L46 22 C50 22 53 24 54 28 L58 44" stroke="currentColor" stroke-width="2.3" stroke-linecap="round"/>
    <path d="M16 44 C16 41 18 39 21 39 L59 39 C62 39 64 41 64 44 L64 56 C64 59 62 61 59 61 L21 61 C18 61 16 59 16 56 Z" stroke="currentColor" stroke-width="2.3" fill="currentColor" fill-opacity="0.10" stroke-linejoin="round"/>
    <circle cx="24" cy="48" r="3.5" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.3"/>
    <circle cx="56" cy="48" r="3.5" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.3"/>
    <rect x="18" y="61" width="8" height="6" rx="2" fill="currentColor"/>
    <rect x="54" y="61" width="8" height="6" rx="2" fill="currentColor"/>
    <path d="M27 38 L29 28 C30 26 31 25 34 25 L46 25 C49 25 50 26 51 28 L53 38 Z" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.15"/>
    <path d="M40 9 L48 13 V19 C48 24 44 27 40 29 C36 27 32 24 32 19 V13 Z" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.25" stroke-linejoin="round"/>
    <path d="M37 19 L39 21 L43 17" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>"""

# SVG 4: CRM Operacional (Ficha 360° del Asegurado)
svg_crm = """<svg width="80" height="80" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="18" y="16" width="44" height="42" rx="6" stroke="currentColor" stroke-width="2.3" fill="currentColor" fill-opacity="0.10"/>
    <line x1="18" y1="26" x2="62" y2="26" stroke="currentColor" stroke-width="2"/>
    <circle cx="24" cy="21" r="1.5" fill="currentColor"/>
    <circle cx="29" cy="21" r="1.5" fill="currentColor"/>
    <circle cx="32" cy="37" r="4.5" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.3"/>
    <path d="M24 49 C24 45 28 44 32 44 C36 44 40 45 40 49" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
    <line x1="44" y1="35" x2="55" y2="35" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
    <line x1="44" y1="41" x2="52" y2="41" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
    <line x1="44" y1="47" x2="55" y2="47" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
    <path d="M34 58 L32 66 H48 L46 58" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>
</svg>"""

# SVG 5: Telefonía Genesys CX (Auriculares de Atención al Cliente de Línea Directa)
svg_telefonia = """<svg width="80" height="80" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M22 42 C22 28 29 18 40 18 C51 18 58 28 58 42" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>
    <rect x="18" y="38" width="8" height="16" rx="4" stroke="currentColor" stroke-width="2.3" fill="currentColor" fill-opacity="0.3"/>
    <rect x="54" y="38" width="8" height="16" rx="4" stroke="currentColor" stroke-width="2.3" fill="currentColor" fill-opacity="0.3"/>
    <path d="M58 48 C58 58 50 63 42 63 H38" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>
    <circle cx="36" cy="63" r="3" fill="currentColor"/>
    <path d="M12 36 C10 39 10 45 12 48" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
    <path d="M68 36 C70 39 70 45 68 48" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
</svg>"""

# SVG 6: Reingeniería de Siniestros (Escudo de Asistencia y Peritación)
svg_siniestros = """<svg width="80" height="80" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M40 14 L62 23 V43 C62 55 52 64 40 68 C28 64 18 55 18 43 V23 Z" stroke="currentColor" stroke-width="2.4" fill="currentColor" fill-opacity="0.10" stroke-linejoin="round"/>
    <circle cx="40" cy="32" r="7" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.25"/>
    <line x1="40" y1="39" x2="40" y2="55" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>
    <line x1="40" y1="47" x2="45" y2="47" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>
    <line x1="40" y1="52" x2="44" y2="52" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>
</svg>"""

# SVG 7: Gestión de Usuarios (Credencial Corporativa & Candado IAM)
svg_usuarios = """<svg width="80" height="80" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="20" y="16" width="40" height="50" rx="5" stroke="currentColor" stroke-width="2.3" fill="currentColor" fill-opacity="0.10"/>
    <rect x="34" y="21" width="12" height="3" rx="1.5" fill="currentColor"/>
    <circle cx="40" cy="35" r="5.5" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.25"/>
    <rect x="32" y="47" width="16" height="12" rx="2.5" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.4"/>
    <path d="M35 47 V43 C35 40 37 38 40 38 C43 38 45 40 45 43 V47" stroke="currentColor" stroke-width="2"/>
    <circle cx="40" cy="53" r="1.5" fill="currentColor"/>
</svg>"""

# SVG 8: Gestión de la Información (Libro Maestro / Wiki GIN)
svg_info = """<svg width="80" height="80" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M40 24 C40 24 48 20 62 20 V56 C48 56 40 60 40 60 C40 60 32 56 18 56 V20 C32 20 40 24 40 24 Z" stroke="currentColor" stroke-width="2.3" fill="currentColor" fill-opacity="0.12" stroke-linejoin="round"/>
    <line x1="40" y1="24" x2="40" y2="60" stroke="currentColor" stroke-width="2.2"/>
    <line x1="24" y1="28" x2="34" y2="28" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
    <line x1="24" y1="35" x2="34" y2="35" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
    <line x1="24" y1="42" x2="31" y2="42" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
    <line x1="46" y1="28" x2="56" y2="28" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
    <line x1="46" y1="35" x2="56" y2="35" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
    <line x1="46" y1="42" x2="53" y2="42" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
</svg>"""

# ==============================================================================
# 3. ACTUALIZAR index.html CON CARDS PERFECTAMENTE SIMÉTRICAS Y ETIQUETAS REALES
# ==============================================================================
with open(INDEX_HTML, "r", encoding="utf-8") as f:
    html = f.read()

# SECCIÓN 1: GESTIÓN DIRECTA
sec1_cards = f"""                    <!-- Evolución HCM Cloud -->
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

sec1_pattern = r"(<div class=\"carousel-track\" id=\"track-direct\"[^>]*>).*?(</div>\s*<button class=\"carousel-btn right)"
html = re.sub(sec1_pattern, r"\1\n" + sec1_cards + r"\n                \2", html, flags=re.DOTALL)

# SECCIÓN 2: FACILITADORES (Perseo con etiquetas reales de negocio: Coaching, Supervisión, Pólizas, Clientes)
sec2_cards = f"""                    <!-- Perseo -->
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
                        <div class="card-visual" style="color: #f59e0b;">
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
                        <div class="card-visual" style="color: #f59e0b;">
                            {svg_siniestros}
                        </div>
                    </a>"""

sec2_pattern = r"(<div class=\"carousel-track\" id=\"track-facilitator\"[^>]*>).*?(</div>\s*<button class=\"carousel-btn right)"
html = re.sub(sec2_pattern, r"\1\n" + sec2_cards + r"\n                \2", html, flags=re.DOTALL)

# SECCIÓN 3: SERVICIOS TRANSVERSALES
sec3_cards = f"""                    <!-- Gestión de Usuarios y Accesos -->
                    <a href="../Gestion de Usuarios/index.html" class="apple-card" data-accent="blue">
                        <div class="kicker" style="color: #2563eb;"><span class="kicker-dot"></span> SERVICIO TRANSVERSAL</div>
                        <h3 class="title">Gestión de Usuarios</h3>
                        <p class="desc">Plataforma transversal de control de accesos, autenticación multifactor, roles de usuario y gobierno de identidad corporativa.</p>
                        <div class="card-tags">
                            <span class="tech-tag">Directorio Activo</span>
                            <span class="tech-tag">Control de Accesos</span>
                            <span class="tech-tag">Roles y Permisos</span>
                            <span class="tech-tag">Seguridad IAM</span>
                        </div>
                        <div class="card-visual" style="color: #2563eb;">
                            {svg_usuarios}
                        </div>
                    </a>

                    <!-- Arquitectura & Plataforma (Reservado) -->
                    <div class="apple-card disabled-card" data-accent="blue">
                        <div class="kicker" style="color: var(--text-muted);">INFRAESTRUCTURA</div>
                        <h3 class="title" style="color: var(--text-muted);">Arquitectura Base</h3>
                        <p class="desc">Estándares corporativos de integración, catálogos de APIs y directrices de seguridad técnica.</p>
                        <div class="card-tags">
                            <span class="tech-tag">Integraciones</span>
                            <span class="tech-tag">Catálogo APIs</span>
                            <span class="tech-tag">Seguridad</span>
                        </div>
                        <div class="card-visual" style="opacity: 0.5;">
                            <svg width="80" height="80" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
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
                        <div class="kicker" style="color: var(--text-muted);">DATA OFFICE</div>
                        <h3 class="title" style="color: var(--text-muted);">Calidad de Datos</h3>
                        <p class="desc">Modelos maestros de datos, linaje analítico y catálogo para auditorías regulatorias.</p>
                        <div class="card-tags">
                            <span class="tech-tag">Modelos de Datos</span>
                            <span class="tech-tag">Linaje Analítico</span>
                            <span class="tech-tag">Catálogo</span>
                        </div>
                        <div class="card-visual" style="opacity: 0.5;">
                            <svg width="80" height="80" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <ellipse cx="40" cy="22" rx="24" ry="9" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.25"/>
                                <path d="M16 22 V39 C16 44 27 48 40 48 C53 48 64 44 64 39 V22" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.15"/>
                                <path d="M16 39 V56 C16 61 27 65 40 65 C53 65 64 61 64 56 V39" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.08"/>
                            </svg>
                        </div>
                    </div>

                    <!-- Oficina Técnica QA (Reservado) -->
                    <div class="apple-card disabled-card" data-accent="blue">
                        <div class="kicker" style="color: var(--text-muted);">CALIDAD & TESTING</div>
                        <h3 class="title" style="color: var(--text-muted);">Oficina Técnica QA</h3>
                        <p class="desc">Automatización de pruebas funcionales, rendimiento y control de regresión antes de paso a producción.</p>
                        <div class="card-tags">
                            <span class="tech-tag">Pruebas Funcionales</span>
                            <span class="tech-tag">Regresión</span>
                            <span class="tech-tag">Calidad Software</span>
                        </div>
                        <div class="card-visual" style="opacity: 0.5;">
                            <svg width="80" height="80" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <circle cx="40" cy="40" r="26" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.10"/>
                                <path d="M28 40 L36 48 L52 32" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                        </div>
                    </div>"""

sec3_pattern = r"(<div class=\"carousel-track\" id=\"track-services\"[^>]*>).*?(</div>\s*<button class=\"carousel-btn right)"
html = re.sub(sec3_pattern, r"\1\n" + sec3_cards + r"\n                \2", html, flags=re.DOTALL)

# SECCIÓN 4: HISTÓRICO
sec4_cards = f"""                    <!-- Gestión de la Información (Traspasado a Transformación) -->
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
                            <svg width="80" height="80" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <rect x="16" y="14" width="48" height="52" rx="6" stroke="currentColor" stroke-width="2.4" fill="currentColor" fill-opacity="0.12"/>
                                <circle cx="40" cy="40" r="13" stroke="currentColor" stroke-width="2.2"/>
                                <circle cx="40" cy="40" r="5" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.35"/>
                            </svg>
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
                            <svg width="80" height="80" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <rect x="18" y="16" width="44" height="48" rx="5" stroke="currentColor" stroke-width="2.4" fill="currentColor" fill-opacity="0.12"/>
                                <line x1="26" y1="16" x2="26" y2="64" stroke="currentColor" stroke-width="2"/>
                                <path d="M37 16 V34 L41 30 L45 34 V16" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.3"/>
                            </svg>
                        </div>
                    </div>"""

sec4_pattern = r"(<div class=\"carousel-track\" id=\"track-closed\"[^>]*>).*?(</div>\s*<button class=\"carousel-btn right)"
html = re.sub(sec4_pattern, r"\1\n" + sec4_cards + r"\n                \2", html, flags=re.DOTALL)

with open(INDEX_HTML, "w", encoding="utf-8") as f:
    f.write(html)

print("[+] index.html actualizado con iconos Brandbook Línea Directa y etiquetas reales del vault.")
print("[OK] Finalizado con éxito.")
