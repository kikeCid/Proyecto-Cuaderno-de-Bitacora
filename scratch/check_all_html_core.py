import glob, os, re

html_files = glob.glob('01_Proyectos/**/*.html', recursive=True)
print(f"Total HTML files in 01_Proyectos: {len(html_files)}")
missing_core = []
for f in html_files:
    with open(f, encoding='utf-8') as fp:
        content = fp.read()
    if 'bitacora-core.css' not in content:
        missing_core.append(f)

print(f"Files without bitacora-core.css: {len(missing_core)}")
if missing_core:
    for m in missing_core[:10]:
        print(" -", m)
