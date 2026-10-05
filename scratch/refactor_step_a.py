"""
REFACTOR STEP A - Eliminación de Deuda Técnica y Principio DRY Masivo
Unifica los 102 archivos HTML de subproyectos bajo bitacora-core.css y bitacora-core.js.
Elimina scripts y estilos duplicados garantizando la preservación de lógica de negocio única.
"""

import os
import re

BASE_DIR = r"C:\Proyectos_Claude\Proyecto Cuaderno de Bitacora\01_Proyectos"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

STD_FUNCS = {
    'initTheme',
    'toggleTheme',
    'initCarousels',
    'scrollCarousel',
    'updateCarouselButtons',
    'initDynamicBreadcrumb',
    'initBreadcrumbLogic'
}

# Diccionario específico para los 4 archivos con scripts mixtos
CUSTOM_REPLACEMENTS = {
    os.path.join("Gobierno de Informacion", "Lidia", "orquestador_ia.html"): """
        function showTab(tabId, btn) {
            document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
            document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            document.getElementById('tab-' + tabId).classList.add('active');
            btn.classList.add('active');
        }
    """,
    os.path.join("HCM", "lanzamiento_rfq.html"): """
        function openTab(evt, tabName) {
            var i, tabcontent, tablinks;
            tabcontent = document.getElementsByClassName("tab-content");
            for (i = 0; i < tabcontent.length; i++) {
                tabcontent[i].classList.remove("active");
            }
            tablinks = document.getElementsByClassName("tab-btn");
            for (i = 0; i < tablinks.length; i++) {
                tablinks[i].classList.remove("active");
            }
            document.getElementById(tabName).classList.add("active");
            evt.currentTarget.classList.add("active");
        }
    """,
    os.path.join("HCM", "rfi_productos.html"): """
        function filterVendor(vendor, btn) {
            btn.classList.toggle('active');
            const bars = document.querySelectorAll(`.bar.${vendor}`);
            const isActive = btn.classList.contains('active');

            bars.forEach(bar => {
                if (isActive) {
                    bar.classList.remove('hidden');
                } else {
                    bar.classList.add('hidden');
                }
            });
        }
    """,
    os.path.join("IA Area Personas", "plan_accion_m365.html"): """
        function toggleModal(id, show) {
            const modal = document.getElementById(id);
            if (show) {
                modal.classList.add('active');
                document.body.style.overflow = 'hidden';
            } else {
                modal.classList.remove('active');
                document.body.style.overflow = '';
            }
        }
        function toggleQModal(show) { toggleModal('quest-modal', show); }
    """
}

def clean_css_mojibake():
    css_files = []
    for root, dirs, files in os.walk(BASE_DIR):
        for f in files:
            if f.endswith(".css"):
                css_files.append(os.path.join(root, f))
                
    replacements = [
        ("Ã“", "Ó"), ("Ã‘", "Ñ"), ("Ã¡", "á"), ("Ã©", "é"),
        ("Ã­", "í"), ("Ã³", "ó"), ("Ãº", "ú"), ("Ã±", "ñ"),
        ("DEFINICIÃ“N", "DEFINICIÓN"), ("DISEÃ‘O", "DISEÑO"),
        ("GESTIÃ“N", "GESTIÓN"), ("carbÃ³n", "carbón"),
        ("SEMÃ NTICO", "SEMÁNTICO"), ("línea directÃ¡", "línea directa"),
        ("BOTN", "BOTÓN"), ("BSQUEDA", "BÚSQUEDA"), ("RPIDA", "RÁPIDA"),
        ("NAVEGACIN", "NAVEGACIÓN"), ("Ver ms", "Ver más")
    ]
    
    fixed_count = 0
    for c_path in css_files:
        try:
            with open(c_path, "r", encoding="utf-8", errors="replace") as fp:
                content = fp.read()
            original = content
            for bad, good in replacements:
                content = content.replace(bad, good)
            if content != original:
                with open(c_path, "w", encoding="utf-8") as fp:
                    fp.write(content)
                fixed_count += 1
                print(f"  [CSS FIX] Mojibake limpio en: {os.path.relpath(c_path, BASE_DIR)}")
        except Exception as e:
            print(f"  [ERROR] Procesando CSS {c_path}: {e}")
    print(f"[*] CSS saneados: {fixed_count}/{len(css_files)}")

def refactor_html_file(file_path):
    rel_from_base = os.path.relpath(file_path, BASE_DIR)
    
    # El Hub principal ya está unificado
    if rel_from_base == os.path.join("Cuaderno de Bitacora (Proyectos)", "index.html"):
        return False, "Hub principal"

    dir_of_file = os.path.dirname(file_path)
    rel_assets = os.path.relpath(ASSETS_DIR, dir_of_file).replace(os.sep, "/")
    core_css_url = f"{rel_assets}/css/bitacora-core.css"
    core_js_url = f"{rel_assets}/js/bitacora-core.js"
    search_data_url = f"{rel_assets}/js/search_index_data.js"

    with open(file_path, "r", encoding="utf-8", errors="replace") as fp:
        content = fp.read()

    original = content

    # 1. Eliminar referencias a local_styles.css
    content = re.sub(
        r'\s*<link[^>]*href=["\'][^"\']*local_styles\.css["\'][^>]*>\s*',
        '\n',
        content,
        flags=re.IGNORECASE
    )

    # 2. Reemplazar styles_bitacora.css por bitacora-core.css
    if re.search(r'<link[^>]*href=["\'][^"\']*styles_bitacora\.css["\'][^>]*>', content, re.IGNORECASE):
        content = re.sub(
            r'<link[^>]*href=["\'][^"\']*styles_bitacora\.css["\'][^>]*>',
            f'<link rel="stylesheet" href="{core_css_url}">',
            content,
            count=1,
            flags=re.IGNORECASE
        )

    # Si bitacora-core.css no está presente, insertarlo al inicio de los CSS en head
    if "bitacora-core.css" not in content:
        m = re.search(r'(<link[^>]*rel=["\']stylesheet["\'])', content, re.IGNORECASE)
        if m:
            content = content[:m.start()] + f'<link rel="stylesheet" href="{core_css_url}">\n    ' + content[m.start():]
        elif '</head>' in content:
            content = content.replace('</head>', f'    <link rel="stylesheet" href="{core_css_url}">\n</head>', 1)

    # 3. Eliminar scripts externos redundantes
    ext_patterns = [
        r'\s*<script[^>]*src=["\'][^"\']*theme\.js["\'][^>]*>\s*</script>\s*',
        r'\s*<script[^>]*src=["\'][^"\']*script_bitacora\.js["\'][^>]*>\s*</script>\s*',
        r'\s*<script[^>]*src=["\'][^"\']*breadcrumb_manager\.js["\'][^>]*>\s*</script>\s*',
        r'\s*<script[^>]*src=["\'][^"\']*scripts_infografia\.js["\'][^>]*>\s*</script>\s*'
    ]
    for pat in ext_patterns:
        content = re.sub(pat, '\n', content, flags=re.IGNORECASE)

    # 4. Procesar scripts inline
    if rel_from_base in CUSTOM_REPLACEMENTS:
        # En los archivos con scripts mixtos, reemplazamos el bloque mixto por su lógica pura
        clean_code = CUSTOM_REPLACEMENTS[rel_from_base]
        script_blocks = list(re.finditer(r'<script(?![^>]*src=)[^>]*>(.*?)</script>', content, flags=re.DOTALL | re.IGNORECASE))
        for sb in script_blocks:
            sb_text = sb.group(1)
            funcs = set(re.findall(r'function\s+([a-zA-Z0-9_]+)\s*\(', sb_text))
            if funcs.issubset(STD_FUNCS):
                content = content.replace(sb.group(0), "")
            elif funcs & STD_FUNCS:
                content = content.replace(sb.group(0), f"<script>{clean_code}</script>")
    else:
        # En el resto de archivos, eliminar bloques que sólo contengan funciones estándar
        script_blocks = list(re.finditer(r'<script(?![^>]*src=)[^>]*>(.*?)</script>', content, flags=re.DOTALL | re.IGNORECASE))
        for sb in script_blocks:
            sb_full = sb.group(0)
            sb_text = sb.group(1)
            funcs = set(re.findall(r'function\s+([a-zA-Z0-9_]+)\s*\(', sb_text))
            if funcs and funcs.issubset(STD_FUNCS):
                content = content.replace(sb_full, "")
            elif not funcs and ('DOMContentLoaded' in sb_text and ('initTheme' in sb_text or 'initDynamicBreadcrumb' in sb_text)):
                # Bloque pequeño de sólo listener
                content = content.replace(sb_full, "")

    # 5. Asegurar inclusión de search_index_data.js y bitacora-core.js antes de </body>
    core_scripts_tag = (
        f'    <!-- MOTOR DE BÚSQUEDA Y NÚCLEO TRANSVERSAL -->\n'
        f'    <script src="{search_data_url}"></script>\n'
        f'    <script src="{core_js_url}"></script>\n'
    )

    # Limpiar cualquier inserción previa para evitar duplicados
    content = re.sub(r'\s*<!-- MOTOR DE BÚSQUEDA Y NÚCLEO TRANSVERSAL -->\s*', '\n', content)
    content = re.sub(rf'\s*<script[^>]*src=["\'][^"\']*search_index_data\.js["\'][^>]*>\s*</script>\s*', '\n', content)
    content = re.sub(rf'\s*<script[^>]*src=["\'][^"\']*bitacora-core\.js["\'][^>]*>\s*</script>\s*', '\n', content)

    if '</body>' in content:
        content = content.replace('</body>', f'{core_scripts_tag}</body>', 1)

    # Limpieza de saltos de línea repetidos
    content = re.sub(r'\n{3,}', '\n\n', content)

    if content != original:
        with open(file_path, "w", encoding="utf-8") as fp:
            fp.write(content)
        return True, "Refactorizado"
    return False, "Sin cambios"

def run_step_a():
    print("=" * 60, flush=True)
    print("PASO A: SANEAMIENTO DRY Y CORE UNIFICADO", flush=True)
    print("=" * 60, flush=True)

    print("\n[1/3] Limpieza de Mojibake en CSS...", flush=True)
    clean_css_mojibake()

    print("\n[2/3] Refactorización masiva de HTMLs de subproyectos...", flush=True)
    count_modified = 0
    total = 0
    for root, dirs, files in os.walk(BASE_DIR):
        if "assets" in root or "scratch" in root or "Backup" in root:
            continue
        for f in files:
            if f.endswith(".html"):
                total += 1
                full_path = os.path.join(root, f)
                mod, msg = refactor_html_file(full_path)
                if mod:
                    count_modified += 1
                    rel_p = os.path.relpath(full_path, BASE_DIR)
                    print(f"  [REFACTORED] {rel_p}", flush=True)

    print(f"\n[3/3] Resumen de ejecución:", flush=True)
    print(f"  * Total archivos HTML escaneados: {total}", flush=True)
    print(f"  * Archivos refactorizados a bitacora-core: {count_modified}", flush=True)
    print(f"  * Archivos conservados: {total - count_modified}", flush=True)
    print("=" * 60, flush=True)

if __name__ == "__main__":
    run_step_a()
