# -*- coding: utf-8 -*-
"""
Script para actualizar los iconos de las tarjetas en todos los subproyectos (Nivel 2)
con iconografía vectorial simétrica profesional a escala proporcional (96x96 en viewBox 0 0 80 80).
"""
import os

BASE_DIR = r"C:\Proyectos_Claude\Proyecto Cuaderno de Bitacora\01_Proyectos"

# ==============================================================================
# SVGs PROPORCIONALES Y SIMÉTRICOS PARA SUBPROYECTOS (96x96, viewBox 0 0 80 80)
# ==============================================================================

# HCM
SVG_HCM_CRONOGRAMA = '''<svg width="96" height="96" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="16" y="16" width="48" height="48" rx="7" stroke="currentColor" stroke-width="2.4" fill="currentColor" fill-opacity="0.10"/>
    <line x1="16" y1="28" x2="64" y2="28" stroke="currentColor" stroke-width="2.2"/>
    <line x1="28" y1="11" x2="28" y2="19" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>
    <line x1="52" y1="11" x2="52" y2="19" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>
    <!-- Barras de Gantt simétricas y ordenadas -->
    <rect x="23" y="36" width="16" height="5" rx="2.5" fill="currentColor"/>
    <rect x="32" y="45" width="22" height="5" rx="2.5" fill="currentColor" fill-opacity="0.55"/>
    <rect x="42" y="54" width="15" height="5" rx="2.5" fill="currentColor" fill-opacity="0.3"/>
</svg>'''

SVG_HCM_ESTRATEGIA = '''<svg width="96" height="96" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <!-- Marco de Análisis Estratégico y Business Case (Eje X=40) -->
    <rect x="16" y="15" width="48" height="50" rx="6" stroke="currentColor" stroke-width="2.4" fill="currentColor" fill-opacity="0.10"/>
    <!-- Curva de Retorno de Inversión y TCO -->
    <path d="M24 53 L34 41 L44 47 L56 31" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M47 31 H56 V40" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
    <circle cx="34" cy="41" r="3" fill="currentColor"/>
    <circle cx="44" cy="47" r="3" fill="currentColor"/>
    <circle cx="56" cy="31" r="3" fill="currentColor"/>
    <line x1="22" y1="57" x2="58" y2="57" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
</svg>'''

SVG_HCM_EJECUCION = '''<svg width="96" height="96" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <!-- Cohete / Motor de Despliegue de Simetría Bilateral (Eje X=40) -->
    <path d="M40 13 C40 13 54 22 54 41 L47 48 L40 46 L33 48 L26 41 C26 22 40 13 40 13 Z" 
          stroke="currentColor" stroke-width="2.4" stroke-linejoin="round" fill="currentColor" fill-opacity="0.14"/>
    <circle cx="40" cy="31" r="5" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.3"/>
    <!-- Toberas Gemelas Simétricas -->
    <path d="M26 41 L18 49 V56 L28 52 L33 48" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>
    <path d="M54 41 L62 49 V56 L52 52 L47 48" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>
    <!-- Propulsión Central -->
    <line x1="40" y1="52" x2="40" y2="65" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>
    <path d="M35 59 L40 65 L45 59" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''

SVG_HCM_CONEXION = '''<svg width="96" height="96" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <!-- Núcleo Central de Integración -->
    <circle cx="40" cy="40" r="10" stroke="currentColor" stroke-width="2.4" fill="currentColor" fill-opacity="0.2"/>
    <!-- 4 Nodos Satélites de Conexión en Cuadrantes Simétricos -->
    <circle cx="21" cy="24" r="6" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.12"/>
    <circle cx="59" cy="24" r="6" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.12"/>
    <circle cx="21" cy="56" r="6" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.12"/>
    <circle cx="59" cy="56" r="6" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.12"/>
    <!-- Enlaces Diagonales Simétricos -->
    <line x1="26" y1="28" x2="33" y2="34" stroke="currentColor" stroke-width="2.2"/>
    <line x1="54" y1="28" x2="47" y2="34" stroke="currentColor" stroke-width="2.2"/>
    <line x1="26" y1="52" x2="33" y2="46" stroke="currentColor" stroke-width="2.2"/>
    <line x1="54" y1="52" x2="47" y2="46" stroke="currentColor" stroke-width="2.2"/>
</svg>'''

SVG_HCM_PERSONAS = '''<svg width="96" height="96" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <!-- Trío de Talento Humano Simétrico (Eje X=40) -->
    <!-- Líder Central -->
    <circle cx="40" cy="29" r="7.5" stroke="currentColor" stroke-width="2.4" fill="currentColor" fill-opacity="0.25"/>
    <path d="M26 53 C26 44 32.5 38 40 38 C47.5 38 54 44 54 53" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>
    <!-- Gemelo Izquierdo -->
    <circle cx="20" cy="35" r="5.5" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.12"/>
    <path d="M11 58 C11 51 15 47 20 47 C23 47 25 48.5 27 51" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
    <!-- Gemelo Derecho -->
    <circle cx="60" cy="35" r="5.5" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.12"/>
    <path d="M53 51 C55 48.5 57 47 60 47 C65 47 69 51 69 58" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
    <line x1="16" y1="65" x2="64" y2="65" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-dasharray="3 3"/>
</svg>'''

# CRM Operacional
SVG_CRM_CONTEXTO = '''<svg width="96" height="96" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <!-- Blueprint de Arquitectura CRM Simétrico (Eje X=40) -->
    <rect x="17" y="16" width="46" height="48" rx="6" stroke="currentColor" stroke-width="2.4" fill="currentColor" fill-opacity="0.10"/>
    <line x1="17" y1="30" x2="63" y2="30" stroke="currentColor" stroke-width="2.2"/>
    <!-- Módulos de Servidores y Capas de Datos -->
    <rect x="24" y="38" width="13" height="15" rx="3" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.2"/>
    <rect x="43" y="38" width="13" height="15" rx="3" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.2"/>
    <line x1="28" y1="58" x2="52" y2="58" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
</svg>'''

SVG_CRM_ADJUDICACION = '''<svg width="96" height="96" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <!-- Trofeo de Adjudicación con Simetría Bilateral Perfecta (Eje X=40) -->
    <path d="M26 21 H54 V37 C54 44.7 47.7 51 40 51 C32.3 51 26 44.7 26 37 V21 Z" 
          stroke="currentColor" stroke-width="2.4" fill="currentColor" fill-opacity="0.14"/>
    <!-- Asas Gemelas Simétricas -->
    <path d="M26 26 H19 C17.3 26 16 27.3 16 29 V34 C16 38 19.5 41 23.5 41 H26" stroke="currentColor" stroke-width="2.2"/>
    <path d="M54 26 H61 C62.7 26 64 27.3 64 29 V34 C64 38 60.5 41 56.5 41 H54" stroke="currentColor" stroke-width="2.2"/>
    <!-- Pedestal Central -->
    <line x1="40" y1="51" x2="40" y2="59" stroke="currentColor" stroke-width="2.4"/>
    <rect x="29" y="59" width="22" height="6" rx="2" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.2"/>
    <!-- Checkmark de Aprobación en el Centro del Trofeo -->
    <path d="M34 35 L38 39 L46 31" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''

SVG_CRM_GOBIERNO = '''<svg width="96" height="96" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <!-- Tablero de Gobernanza Ágil de 3 Columnas Simétricas (Eje X=40) -->
    <rect x="16" y="16" width="48" height="48" rx="6" stroke="currentColor" stroke-width="2.4" fill="currentColor" fill-opacity="0.10"/>
    <line x1="32" y1="16" x2="32" y2="64" stroke="currentColor" stroke-width="2"/>
    <line x1="48" y1="16" x2="48" y2="64" stroke="currentColor" stroke-width="2"/>
    <!-- Tarjetas de Tareas Simétricas -->
    <rect x="20" y="24" width="8" height="10" rx="2" fill="currentColor"/>
    <rect x="36" y="24" width="8" height="15" rx="2" fill="currentColor"/>
    <rect x="36" y="43" width="8" height="10" rx="2" fill="currentColor" fill-opacity="0.5"/>
    <rect x="52" y="24" width="8" height="20" rx="2" fill="currentColor" fill-opacity="0.75"/>
</svg>'''

# Perseo
SVG_PERSEO_VISION = '''<svg width="96" height="96" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <!-- Retícula Analítica de Visión y Objetivos (Eje X=40, Y=40) -->
    <circle cx="40" cy="40" r="24" stroke="currentColor" stroke-width="2.4" fill="currentColor" fill-opacity="0.08"/>
    <circle cx="40" cy="40" r="14" stroke="currentColor" stroke-width="2" stroke-dasharray="4 2"/>
    <circle cx="40" cy="40" r="4.5" fill="currentColor"/>
    <line x1="40" y1="11" x2="40" y2="18" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>
    <line x1="40" y1="62" x2="40" y2="69" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>
    <line x1="11" y1="40" x2="18" y2="40" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>
    <line x1="62" y1="40" x2="69" y2="40" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>
</svg>'''

SVG_PERSEO_RRLL = '''<svg width="96" height="96" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <!-- Escudo de Relaciones Laborales y Bienestar (Eje X=40) -->
    <path d="M40 14 L62 22 V39 C62 52 52 61 40 66 C28 61 18 39 V22 L40 14 Z" 
          stroke="currentColor" stroke-width="2.4" stroke-linejoin="round" fill="currentColor" fill-opacity="0.12"/>
    <circle cx="40" cy="33" r="5.5" stroke="currentColor" stroke-width="2"/>
    <path d="M31 49 C31 44 35 41 40 41 C45 41 49 44 49 49" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
</svg>'''

SVG_PERSEO_COACHING = '''<svg width="96" height="96" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <!-- Escala de Evolución y Coaching Ascendente -->
    <rect x="18" y="16" width="44" height="48" rx="6" stroke="currentColor" stroke-width="2.4" fill="currentColor" fill-opacity="0.10"/>
    <rect x="24" y="46" width="6" height="12" rx="2" fill="currentColor"/>
    <rect x="34" y="38" width="6" height="20" rx="2" fill="currentColor"/>
    <rect x="44" y="30" width="6" height="28" rx="2" fill="currentColor"/>
    <!-- Flecha de Progresión -->
    <path d="M26 38 L36 30 L46 22 L54 18" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>
    <path d="M47 18 H54 V25" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''

SVG_PERSEO_ROLES = '''<svg width="96" height="96" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <!-- Cuadro de Mando Ejecutivo Simétrico -->
    <rect x="16" y="16" width="48" height="48" rx="6" stroke="currentColor" stroke-width="2.4" fill="currentColor" fill-opacity="0.10"/>
    <line x1="16" y1="30" x2="64" y2="30" stroke="currentColor" stroke-width="2.2"/>
    <line x1="36" y1="30" x2="36" y2="64" stroke="currentColor" stroke-width="2"/>
    <!-- Indicadores -->
    <circle cx="26" cy="47" r="6" stroke="currentColor" stroke-width="2"/>
    <rect x="42" y="37" width="16" height="5" rx="2" fill="currentColor"/>
    <rect x="42" y="47" width="12" height="5" rx="2" fill="currentColor" fill-opacity="0.5"/>
</svg>'''

SVG_PERSEO_CASOS = '''<svg width="96" height="96" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <!-- Radar de Casos de Uso Analíticos y Detección de Frecuencia -->
    <circle cx="40" cy="40" r="24" stroke="currentColor" stroke-width="2.4" fill="currentColor" fill-opacity="0.08"/>
    <circle cx="40" cy="40" r="15" stroke="currentColor" stroke-width="2"/>
    <circle cx="40" cy="40" r="5" fill="currentColor"/>
    <line x1="40" y1="40" x2="57" y2="23" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>
    <circle cx="53" cy="27" r="3" fill="currentColor"/>
</svg>'''

# Gestión de Usuarios
SVG_GUS_ARQUITECTURA = '''<svg width="96" height="96" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <!-- Servidores Racks Simétricos en Eje X=40 -->
    <rect x="18" y="16" width="44" height="18" rx="4" stroke="currentColor" stroke-width="2.4" fill="currentColor" fill-opacity="0.12"/>
    <rect x="18" y="46" width="44" height="18" rx="4" stroke="currentColor" stroke-width="2.4" fill="currentColor" fill-opacity="0.12"/>
    <circle cx="27" cy="25" r="2.5" fill="currentColor"/>
    <circle cx="35" cy="25" r="2.5" fill="currentColor"/>
    <circle cx="27" cy="55" r="2.5" fill="currentColor"/>
    <circle cx="35" cy="55" r="2.5" fill="currentColor"/>
    <line x1="40" y1="34" x2="40" y2="46" stroke="currentColor" stroke-width="2.4"/>
</svg>'''

SVG_GUS_FLUJOS = '''<svg width="96" height="96" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <!-- Diagrama de Flujos Operativos y Decisiones Simétricas -->
    <circle cx="24" cy="26" r="6" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.18"/>
    <rect x="46" y="21" width="18" height="10" rx="3" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.18"/>
    <circle cx="40" cy="56" r="6" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.18"/>
    <path d="M30 26 H46" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>
    <path d="M55 31 V44 L45 52" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''

SVG_GUS_INTEGRACIONES = '''<svg width="96" height="96" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <!-- Conectores de APIs e Integraciones Simétricas -->
    <rect x="14" y="28" width="14" height="24" rx="4" stroke="currentColor" stroke-width="2.4" fill="currentColor" fill-opacity="0.15"/>
    <rect x="52" y="28" width="14" height="24" rx="4" stroke="currentColor" stroke-width="2.4" fill="currentColor" fill-opacity="0.15"/>
    <line x1="28" y1="35" x2="36" y2="35" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>
    <line x1="28" y1="45" x2="36" y2="45" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>
    <line x1="44" y1="35" x2="52" y2="35" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>
    <line x1="44" y1="45" x2="52" y2="45" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>
    <circle cx="40" cy="40" r="4" fill="currentColor"/>
</svg>'''

# Gobierno de Información
SVG_GIN_LIDIA_HUB = '''<svg width="96" height="96" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <!-- Núcleo de Red Neuronal Profunda LidIA (Simetría en 4 Ejes) -->
    <circle cx="40" cy="40" r="25" stroke="currentColor" stroke-width="2.4" fill="currentColor" fill-opacity="0.08"/>
    <circle cx="40" cy="40" r="10" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.25"/>
    <circle cx="40" cy="22" r="3.5" fill="currentColor"/>
    <circle cx="40" cy="58" r="3.5" fill="currentColor"/>
    <circle cx="22" cy="40" r="3.5" fill="currentColor"/>
    <circle cx="58" cy="40" r="3.5" fill="currentColor"/>
    <line x1="40" y1="26" x2="40" y2="30" stroke="currentColor" stroke-width="2.2"/>
    <line x1="40" y1="50" x2="40" y2="54" stroke="currentColor" stroke-width="2.2"/>
    <line x1="26" y1="40" x2="30" y2="40" stroke="currentColor" stroke-width="2.2"/>
    <line x1="50" y1="40" x2="54" y2="40" stroke="currentColor" stroke-width="2.2"/>
</svg>'''

SVG_GIN_MARCO = '''<svg width="96" height="96" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <!-- Estandarte y Constitución Normativa GIN -->
    <path d="M22 15 H58 V57 L40 48 L22 57 V15 Z" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round" fill="currentColor" fill-opacity="0.14"/>
    <line x1="30" y1="25" x2="50" y2="25" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>
    <line x1="30" y1="33" x2="46" y2="33" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>
</svg>'''

# Telefonía Genesys CX
SVG_TEL_ESTADO = '''<svg width="96" height="96" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="18" y="16" width="44" height="48" rx="6" stroke="currentColor" stroke-width="2.4" fill="currentColor" fill-opacity="0.12"/>
    <line x1="18" y1="30" x2="62" y2="30" stroke="currentColor" stroke-width="2.2"/>
    <circle cx="26" cy="23" r="2.5" fill="currentColor"/>
    <circle cx="34" cy="23" r="2.5" fill="currentColor"/>
    <path d="M26 40 H44 M26 48 H52" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>
</svg>'''

SVG_TEL_ROADMAP = '''<svg width="96" height="96" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
    <line x1="24" y1="16" x2="24" y2="64" stroke="currentColor" stroke-width="2.4"/>
    <circle cx="24" cy="24" r="5" stroke="currentColor" stroke-width="2" fill="currentColor"/>
    <circle cx="24" cy="40" r="5" stroke="currentColor" stroke-width="2" fill="currentColor"/>
    <circle cx="24" cy="56" r="5" stroke="currentColor" stroke-width="2" fill="currentColor"/>
    <path d="M32 24 H54 M32 40 H46 M32 56 H58" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>
</svg>'''


def replace_card_visual_svg(content, card_identifier, new_svg):
    card_idx = content.find(card_identifier)
    if card_idx == -1:
        return content

    visual_idx = content.find('class="card-visual"', card_idx)
    if visual_idx == -1 or visual_idx > card_idx + 1200:
        return content

    svg_start = content.find('<svg', visual_idx)
    svg_end = content.find('</svg>', svg_start)
    if svg_start == -1 or svg_end == -1:
        return content
    svg_end += len('</svg>')

    return content[:svg_start] + new_svg + content[svg_end:]


# Actualizar subproyectos
files_map = {
    os.path.join(BASE_DIR, "HCM", "index.html"): [
        ('cronograma.html', SVG_HCM_CRONOGRAMA),
        ('universo_estrategico.html', SVG_HCM_ESTRATEGIA),
        ('Universo de <span>Ejecución</span>', SVG_HCM_EJECUCION),
        ('Universo de <span>Conexión</span>', SVG_HCM_CONEXION),
        ('Universo de <span>Personas</span>', SVG_HCM_PERSONAS)
    ],
    os.path.join(BASE_DIR, "CRM Operacional", "index.html"): [
        ('contexto_proyecto.html', SVG_CRM_CONTEXTO),
        ('hub_licitacion.html', SVG_CRM_ADJUDICACION),
        ('Metodología y <span>Gobierno</span>', SVG_CRM_GOBIERNO)
    ],
    os.path.join(BASE_DIR, "Perseo", "index.html"): [
        ('vision_objetivos.html', SVG_PERSEO_VISION),
        ('gestion_rrll.html', SVG_PERSEO_RRLL),
        ('planes_coaching.html', SVG_PERSEO_COACHING),
        ('roles_dashboard.html', SVG_PERSEO_ROLES),
        ('casos_uso.html', SVG_PERSEO_CASOS)
    ],
    os.path.join(BASE_DIR, "Gestion de Usuarios", "index.html"): [
        ('arquitectura_gus.html', SVG_GUS_ARQUITECTURA),
        ('sistema_contratacion_gus.html', SVG_GUS_FLUJOS),
        ('integraciones_gus.html', SVG_GUS_INTEGRACIONES)
    ],
    os.path.join(BASE_DIR, "Gobierno de Informacion", "index.html"): [
        ('hub_lidia.html', SVG_GIN_LIDIA_HUB),
        ('hub_gin.html', SVG_GIN_MARCO)
    ],
    os.path.join(BASE_DIR, "Telefonia - Genesis CX", "index.html"): [
        ('contexto_proyecto.html', SVG_TEL_ESTADO),
        ('roadmap.html', SVG_TEL_ROADMAP)
    ]
}

for path, updates in files_map.items():
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            c = f.read()
        for ident, svg in updates:
            c = replace_card_visual_svg(c, ident, svg)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"[+] Actualizado: {os.path.basename(os.path.dirname(path))}")

print("[OK] Subproyectos sincronizados con la nueva escala e iconografia simetrica.")
