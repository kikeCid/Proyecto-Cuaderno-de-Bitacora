import glob, os, re

html_files = glob.glob('01_Proyectos/**/index.html', recursive=True)
print(f"Found {len(html_files)} index.html files:")
for f in html_files:
    with open(f, encoding='utf-8') as fp:
        head = fp.read()[:2000]
    css_links = re.findall(r'<link[^>]*rel="stylesheet"[^>]*href="([^"]+)"', head)
    has_font = 'CircularXX' in head or 'bitacora-core.css' in head
    print(f"  {f}")
    print(f"    CSS: {css_links}")
