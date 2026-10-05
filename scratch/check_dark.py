import re

with open(r"01_Proyectos\assets\css\bitacora-core.css", "r", encoding="utf-8") as f:
    c = f.read()

print("=== DARK THEME ROOT ===")
for m in re.finditer(r'\[data-theme=["\']dark["\']\]\s*\{([^}]+)\}', c):
    print(m.group(0))

print("\n=== DARK THEME CARDS & ELEMENTS ===")
for m in re.finditer(r'(\[data-theme=["\']dark["\']\][^{]+)\{([^}]+)\}', c):
    print(m.group(1).strip())
    print("   ", m.group(2).strip().replace("\n", " "))
