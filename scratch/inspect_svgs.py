import glob, os, re

for path in glob.glob('01_Proyectos/assets/img/*.svg'):
    with open(path, encoding='utf-8') as f:
        c = f.read()
    vb = re.search(r'viewBox="([^"]+)"', c)
    w = re.search(r'width="([^"]+)"', c)
    h = re.search(r'height="([^"]+)"', c)
    viewbox_val = vb.group(1) if vb else 'none'
    width_val = w.group(1) if w else '-'
    height_val = h.group(1) if h else '-'
    print(f"{os.path.basename(path):30} | viewBox: {viewbox_val:15} | {width_val}x{height_val}")
