import subprocess

with open(r"C:\Proyectos_Claude\Proyecto Cuaderno de Bitacora\scratch\orig_hub_index.html", "r", encoding="utf-8") as f:
    orig = f.read()

with open(r"C:\Proyectos_Claude\Proyecto Cuaderno de Bitacora\01_Proyectos\Cuaderno de Bitacora (Proyectos)\index.html", "r", encoding="utf-8") as f:
    curr = f.read()

print(f"Orig lines: {len(orig.splitlines())}")
print(f"Curr lines: {len(curr.splitlines())}")

# Let's see what sections exist in orig vs curr
import re
orig_sections = re.findall(r'<h2 class="section-title">(.*?)</h2>', orig)
curr_sections = re.findall(r'<h2 class="section-title">(.*?)</h2>', curr)

print("\nOrig sections:")
for s in orig_sections:
    print(" -", s)

print("\nCurr sections:")
for s in curr_sections:
    print(" -", s)

# Cards in each section
orig_cards = re.findall(r'<h3 class="title">(.*?)</h3>', orig)
curr_cards = re.findall(r'<h3 class="title">(.*?)</h3>', curr)

print(f"\nOrig cards ({len(orig_cards)}):")
for c in orig_cards:
    print(" -", c)

print(f"\nCurr cards ({len(curr_cards)}):")
for c in curr_cards:
    print(" -", c)
