import re

with open(r"01_Proyectos\Cuaderno de Bitacora (Proyectos)\index.html", "r", encoding="utf-8") as f:
    c = f.read()

# Buscar bloques de tarjetas
cards = re.findall(r'(<(?:a|div)[^>]*class=[\'"][^\'"]*apple-card[^\'"]*[\'"].*?)(?=<(?:a|div)[^>]*class=[\'"][^\'"]*apple-card|</div>\s*<button|\Z)', c, re.DOTALL)
print(f"Total apple-cards in Hub: {len(cards)}")
for i, card in enumerate(cards):
    title_m = re.search(r'class=[\'"]title[\'"][^>]*>(.*?)</h3>', card)
    title = title_m.group(1).strip() if title_m else "No title"
    kicker_m = re.search(r'class=[\'"]kicker[\'"][^>]*>(.*?)</div>', card)
    kicker = kicker_m.group(1).strip() if kicker_m else ""
    svg_m = re.search(r'<svg[^>]*>(.*?)</svg>', card, re.DOTALL)
    svg_clean = re.sub(r'\s+', ' ', svg_m.group(0)) if svg_m else "No SVG"
    print(f"\n--- Card {i+1}: {title} [{kicker}] ---")
    print(f"SVG: {svg_clean[:180]}...")
