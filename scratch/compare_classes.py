import re

with open(r"01_Proyectos\Cuaderno de Bitacora (Proyectos)\index.html", "r", encoding="utf-8") as f:
    html = f.read()
with open(r"01_Proyectos\assets\css\bitacora-core.css", "r", encoding="utf-8") as f:
    css = f.read()

# Find all classes in index.html
classes_in_html = set()
for m in re.finditer(r'class=[\'"]([^\'"]+)[\'"]', html):
    for c in m.group(1).split():
        classes_in_html.add(c)

print(f"Total classes in index.html: {len(classes_in_html)}")
missing_in_css = []
for c in sorted(classes_in_html):
    # check if .c is defined in css
    if not re.search(r'\.' + re.escape(c) + r'[\s,\.:\{]', css):
        missing_in_css.append(c)

print(f"Classes used in index.html but NOT in bitacora-core.css ({len(missing_in_css)}):")
for mc in missing_in_css:
    print(f"  - {mc}")
