import re

with open(r'01_Proyectos/Cuaderno de Bitacora (Proyectos)/index.html', encoding='utf-8') as f:
    content = f.read()

# Split by class="apple-card
parts = content.split('class="apple-card')
print(f"Total card chunks: {len(parts)-1}")

for i, chunk in enumerate(parts[1:], 1):
    # take up to the next card or end of track
    chunk = chunk[:chunk.find('</article>') if '</article>' in chunk else chunk.find('</div>\n                    </div>\n')]
    title_m = re.search(r'<h3 class="title"[^>]*>(.*?)</h3>', chunk)
    title = title_m.group(1).strip() if title_m else 'NO TITLE'
    kicker_m = re.search(r'<div class="kicker"[^>]*>(.*?)</div>', chunk)
    kicker = re.sub(r'<[^>]+>', '', kicker_m.group(1)).strip() if kicker_m else 'NO KICKER'
    svg_m = re.search(r'<svg[^>]*viewBox="([^"]+)"[^>]*>(.*?)</svg>', chunk, re.DOTALL)
    vb = svg_m.group(1) if svg_m else 'NO SVG'
    has_card_visual = 'class="card-visual"' in chunk
    color_m = re.search(r'class="card-visual"[^>]*style="([^"]+)"', chunk)
    style_color = color_m.group(1) if color_m else 'NO INLINE STYLE'
    
    # Check what kind of svg content
    svg_content = svg_m.group(2) if svg_m else ''
    first_tag = re.search(r'<([a-zA-Z]+)', svg_content)
    tag_name = first_tag.group(1) if first_tag else 'none'

    print(f"{i:02d}. [{kicker}] {title}")
    print(f"    Style: {style_color} | viewBox: {vb} | First tag: {tag_name}")
