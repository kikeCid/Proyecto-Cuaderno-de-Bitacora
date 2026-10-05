import re

with open(r'01_Proyectos/Cuaderno de Bitacora (Proyectos)/index.html', encoding='utf-8') as f:
    content = f.read()

parts = content.split('class="apple-card')

for i, chunk in enumerate(parts[1:], 1):
    chunk = chunk[:chunk.find('</article>') if '</article>' in chunk else chunk.find('</div>\n                    </div>\n')]
    title_m = re.search(r'<h3 class="title"[^>]*>(.*?)</h3>', chunk)
    title = title_m.group(1).strip() if title_m else 'NO TITLE'
    svg_m = re.search(r'<svg[^>]*>(.*?)</svg>', chunk, re.DOTALL)
    svg_content = svg_m.group(0) if svg_m else 'NO SVG'
    
    print("=" * 60)
    print(f"CARD {i}: {title}")
    # print first 300 chars of svg
    print(svg_content[:250].replace('\n', ' '))
