import os
import re
from urllib.parse import unquote
from collections import defaultdict

BASE_DIR = r"C:\Proyectos_Claude\Proyecto Cuaderno de Bitacora"

def audit_detailed():
    html_files = []
    for root, dirs, files in os.walk(os.path.join(BASE_DIR, "01_Proyectos")):
        if "Backup" in root:
            continue
        for f in files:
            if f.endswith(".html"):
                html_files.append(os.path.join(root, f))

    broken_links = []
    projects = defaultdict(list)
    css_references = defaultdict(set)
    js_references = defaultdict(set)
    title_tags = {}

    for file_path in html_files:
        rel_file = os.path.relpath(file_path, BASE_DIR)
        proj = rel_file.split(os.sep)[1]
        projects[proj].append(rel_file)

        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()

        t_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
        title_tags[rel_file] = t_match.group(1).strip() if t_match else "NO TITLE"

        # Check stylesheet links
        for css in re.findall(r'<link[^>]*rel=["\']stylesheet["\'][^>]*href=["\']([^"\']+)["\']', content, re.IGNORECASE):
            css_references[rel_file].add(css)
            clean_css = unquote(css.split("?")[0].split("#")[0])
            if not clean_css.startswith(("http://", "https://")):
                target = os.path.normpath(os.path.join(os.path.dirname(file_path), clean_css))
                if not os.path.exists(target):
                    broken_links.append((rel_file, css, "CSS"))

        # Check script tags
        for js in re.findall(r'<script[^>]*src=["\']([^"\']+)["\']', content, re.IGNORECASE):
            js_references[rel_file].add(js)
            clean_js = unquote(js.split("?")[0].split("#")[0])
            if not clean_js.startswith(("http://", "https://")):
                target = os.path.normpath(os.path.join(os.path.dirname(file_path), clean_js))
                if not os.path.exists(target):
                    broken_links.append((rel_file, js, "JS"))

        # Check regular links <a>
        for href in re.findall(r'<a[^>]*href=["\']([^"\']+)["\']', content, re.IGNORECASE):
            if href.startswith(("#", "javascript:", "mailto:", "data:", "http://", "https://")):
                continue
            clean = unquote(href.split("?")[0].split("#")[0])
            if not clean:
                continue
            target = os.path.normpath(os.path.join(os.path.dirname(file_path), clean))
            if not os.path.exists(target):
                broken_links.append((rel_file, href, "A_HREF"))

    print(f"=== AUDIT OF ACTIVE PROJECTS (Total: {len(html_files)} HTML files) ===")
    for p, files in projects.items():
        print(f"Project: {p} ({len(files)} files)")

    print(f"\nTotal broken references in active projects: {len(broken_links)}")
    for src, ref, kind in broken_links:
        print(f"[{kind}] {src} -> {ref}")

if __name__ == "__main__":
    audit_detailed()
