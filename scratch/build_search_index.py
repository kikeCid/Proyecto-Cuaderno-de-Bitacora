"""
BUILD SEARCH INDEX
Indexa todos los documentos HTML de los proyectos activos y genera:
- 01_Proyectos/assets/search_index.json
- 01_Proyectos/assets/js/search_index_data.js (para soporte offline file:///)
"""

import os
import re
import json

BASE_DIR = r"C:\Proyectos_Claude\Proyecto Cuaderno de Bitacora\01_Proyectos"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

def build_index():
    index_entries = []
    
    for root, dirs, files in os.walk(BASE_DIR):
        if "assets" in root or "scratch" in root or "Backup" in root:
            continue
        for f in files:
            if f.endswith(".html"):
                full_path = os.path.join(root, f)
                rel_path = os.path.relpath(full_path, BASE_DIR).replace(os.sep, "/")
                
                with open(full_path, "r", encoding="utf-8", errors="replace") as fp:
                    content = fp.read()
                    
                # Extraer título
                m_title = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
                raw_title = m_title.group(1).strip() if m_title else f
                title = re.sub(r'\s+', ' ', raw_title)
                
                # Extraer H1
                m_h1 = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
                h1 = ""
                if m_h1:
                    h1 = re.sub(r'<[^>]+>', '', m_h1.group(1)).strip()
                    h1 = re.sub(r'\s+', ' ', h1)
                
                # Extraer kicker o badge si existe
                m_kicker = re.search(r'class=["\'][^"\']*(?:kicker|hero-badge|badge)[^"\']*["\'][^>]*>(.*?)<', content, re.IGNORECASE)
                kicker = m_kicker.group(1).strip() if m_kicker else ""
                
                # Extraer descripción o párrafo hero
                m_desc = re.search(r'class=["\'][^"\']*(?:subtitle|hero-desc|hero-p|lead)[^"\']*["\'][^>]*>(.*?)<', content, re.IGNORECASE)
                desc = ""
                if m_desc:
                    desc = re.sub(r'<[^>]+>', '', m_desc.group(1)).strip()
                    desc = re.sub(r'\s+', ' ', desc)
                if not desc and len(h1) > 0:
                    desc = h1
                
                # Determinar proyecto y categoría
                parts = rel_path.split("/")
                proj_folder = parts[0]
                
                category_map = {
                    "CRM Operacional": "Facilitadores",
                    "Cuaderno de Bitacora (Proyectos)": "Core Platform",
                    "Gestion de Usuarios": "Tecnología",
                    "Gobierno de Informacion": "Estratégico",
                    "HCM": "Corporativo",
                    "IA Area Personas": "Innovación",
                    "Perseo": "Estratégico",
                    "Reingenieria Siniestros": "Operaciones",
                    "Telefonia - Genesis CX": "Infraestructura"
                }
                
                cat = category_map.get(proj_folder, "Proyecto")
                
                index_entries.append({
                    "id": rel_path,
                    "title": title,
                    "h1": h1,
                    "kicker": kicker,
                    "desc": desc[:160] + ("..." if len(desc) > 160 else ""),
                    "project": proj_folder,
                    "category": cat,
                    "url": f"../{rel_path}"
                })
                
    # Ordenar por proyecto y título
    index_entries.sort(key=lambda x: (x["project"], x["title"]))
    
    # 1. Guardar JSON
    json_path = os.path.join(ASSETS_DIR, "search_index.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(index_entries, f, ensure_ascii=False, indent=2)
        
    # 2. Guardar JS para carga local sin CORS
    js_path = os.path.join(ASSETS_DIR, "js", "search_index_data.js")
    with open(js_path, "w", encoding="utf-8") as f:
        f.write("/** ÍNDICE DE BÚSQUEDA AUTOGENERADO - Cuaderno de Bitácora **/\n")
        f.write("window.BITACORA_SEARCH_INDEX = ")
        json.dump(index_entries, f, ensure_ascii=False, indent=2)
        f.write(";\n")
        
    print(f"[+] Índice de búsqueda generado exitosamente:")
    print(f"    Total documentos indexados: {len(index_entries)}")
    print(f"    Archivo JSON: {json_path}")
    print(f"    Archivo JS:   {js_path}")

if __name__ == "__main__":
    build_index()
