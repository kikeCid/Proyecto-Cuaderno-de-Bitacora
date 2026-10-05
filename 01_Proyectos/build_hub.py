"""
BUILD HUB - Generador y Validador del Cuaderno de Bitácora
Lee 'projects_registry.json' (SSOT) y verifica la integridad del catálogo de proyectos.
"""

import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REGISTRY_PATH = os.path.join(BASE_DIR, "projects_registry.json")
HUB_PATH = os.path.join(BASE_DIR, "Cuaderno de Bitacora (Proyectos)", "index.html")

def load_registry():
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def validate_registry():
    data = load_registry()
    projects = data.get("projects", [])
    categories = {c["id"]: c for c in data.get("categories", [])}
    
    print(f"[*] Validando catálogo: {len(projects)} proyectos en {len(categories)} categorías...")
    errors = 0
    
    for p in projects:
        cat_id = p.get("categoryId")
        if cat_id not in categories:
            print(f"[!] Error: Proyecto '{p['title']}' tiene categoría inválida '{cat_id}'")
            errors += 1
            
        # Validar ruta relativa desde Cuaderno de Bitacora
        hub_dir = os.path.dirname(HUB_PATH)
        rel_url = p.get("url")
        target_path = os.path.normpath(os.path.join(hub_dir, rel_url))
        if not os.path.exists(target_path):
            print(f"[!] Error: Ruta inexistente para '{p['title']}': {target_path}")
            errors += 1
        else:
            print(f"  [OK] '{p['title']}' -> {rel_url}")
            
    if errors == 0:
        print("[+] Integridad 100% verificada. Todos los proyectos y rutas del SSOT son válidos.")
    else:
        print(f"[-] Se encontraron {errors} errores de integridad.")
        sys.exit(1)

if __name__ == "__main__":
    validate_registry()
