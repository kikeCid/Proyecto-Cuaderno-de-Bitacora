"""
SEARCH INDEX BUILDER - Cuaderno de Bitácora
Genera search_index.json y search_index_data.js para compatibilidad total con protocolo file:///.
"""

import os
import re
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_JSON = os.path.join(BASE_DIR, "assets", "search_index.json")
OUTPUT_JS = os.path.join(BASE_DIR, "assets", "js", "search_index_data.js")
HUB_DIR = os.path.join(BASE_DIR, "Cuaderno de Bitacora (Proyectos)")

PROJECT_CATEGORIES = {
    "Gobierno de Informacion": "Proyectos Cerrados",
    "HCM": "Gestión Directa",
    "IA Area Personas": "Gestión Directa",
    "PMO Perscom": "Gestión Directa",
    "Perseo": "Facilitadores",
    "CRM Operacional": "Estratégicos",
    "Telefonia - Genesis CX": "Estratégicos",
    "Reingenieria Siniestros": "Estratégicos",
    "Gestion de Usuarios": "Servicios",
    "Cuaderno de Bitacora (Proyectos)": "Portal Central"
}

def clean_html_text(text):
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def build_index():
    index_entries = []
    
    for root, dirs, files in os.walk(BASE_DIR):
        if "assets" in root or "scratch" in root or "Backup" in root:
            continue
        for f in files:
            if f.endswith(".html"):
                full_path = os.path.join(root, f)
                rel_from_base = os.path.relpath(full_path, BASE_DIR)
                project_folder = rel_from_base.split(os.sep)[0]
                
                # Relative URL from Hub
                rel_url_from_hub = os.path.relpath(full_path, HUB_DIR).replace(os.sep, "/")
                
                try:
                    with open(full_path, "r", encoding="utf-8", errors="replace") as fp:
                        content = fp.read()
                except Exception as e:
                    print(f"Error reading {full_path}: {e}")
                    continue
                    
                # Extract Title
                title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
                raw_title = title_match.group(1) if title_match else f.replace(".html", "").replace("_", " ").title()
                clean_title = clean_html_text(raw_title).replace("| Proyectos LDAP", "").replace("| LDA", "").strip()
                
                # Extract H1
                h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
                h1 = clean_html_text(h1_match.group(1)) if h1_match else clean_title
                
                # Extract Kicker / Badge
                kicker_match = re.search(r'class=["\'](?:kicker|hero-badge)["\'][^>]*>(.*?)<', content, re.IGNORECASE)
                kicker = clean_html_text(kicker_match.group(1)) if kicker_match else ""
                
                # Extract Paragraph description
                p_match = re.search(r'<p[^>]*class=["\']desc["\'][^>]*>(.*?)</p>', content, re.IGNORECASE | re.DOTALL)
                if not p_match:
                    p_match = re.search(r'<header[^>]*>.*?<p[^>]*>(.*?)</p>', content, re.IGNORECASE | re.DOTALL)
                desc = clean_html_text(p_match.group(1)) if p_match else ""
                if len(desc) > 160:
                    desc = desc[:157] + "..."
                    
                category = PROJECT_CATEGORIES.get(project_folder, "General")
                
                entry = {
                    "id": rel_from_base.replace(os.sep, "/"),
                    "title": clean_title,
                    "h1": h1,
                    "kicker": kicker,
                    "desc": desc,
                    "project": project_folder,
                    "category": category,
                    "url": rel_url_from_hub
                }
                index_entries.append(entry)
                
    index_entries.sort(key=lambda x: (x["project"], x["title"]))
    
    # 1. Guardar JSON
    os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)
    with open(OUTPUT_JSON, "w", encoding="utf-8") as out:
        json.dump(index_entries, out, ensure_ascii=False, indent=2)
        
    # 2. Guardar JS para compatibilidad 100% offline y file:///
    os.makedirs(os.path.dirname(OUTPUT_JS), exist_ok=True)
    with open(OUTPUT_JS, "w", encoding="utf-8") as out_js:
        out_js.write("/** ÍNDICE DE BÚSQUEDA AUTOGENERADO - Cuaderno de Bitácora **/\n")
        out_js.write("window.BITACORA_SEARCH_INDEX = ")
        json.dump(index_entries, out_js, ensure_ascii=False, indent=2)
        out_js.write(";\n")
        
    print(f"[+] Índice de búsqueda JSON generado: {OUTPUT_JSON}")
    print(f"[+] Índice de búsqueda JS generado: {OUTPUT_JS}")
    print(f"    Total de documentos indexados: {len(index_entries)}")

if __name__ == "__main__":
    build_index()
