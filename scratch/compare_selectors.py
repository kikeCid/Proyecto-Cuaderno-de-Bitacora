with open(r"01_Proyectos\Cuaderno de Bitacora (Proyectos)\styles_bitacora.css", "r", encoding="utf-8", errors="replace") as f:
    orig_css = f.read()

with open(r"01_Proyectos\assets\css\bitacora-core.css", "r", encoding="utf-8", errors="replace") as f:
    core_css = f.read()

print(f"styles_bitacora.css length: {len(orig_css)} chars, {len(orig_css.splitlines())} lines")
print(f"bitacora-core.css length:   {len(core_css)} chars, {len(core_css.splitlines())} lines")

import re
orig_rules = re.findall(r'([^{]+)\{([^}]+)\}', orig_css)
core_rules = re.findall(r'([^{]+)\{([^}]+)\}', core_css)

orig_selectors = set(r[0].strip() for r in orig_rules)
core_selectors = set(r[0].strip() for r in core_rules)

missing_selectors = orig_selectors - core_selectors
print(f"\nSelectors in styles_bitacora.css but not in bitacora-core.css ({len(missing_selectors)}):")
for s in sorted(missing_selectors)[:50]:
    print(f"  {s}")
