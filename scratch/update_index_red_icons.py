import re

index_path = r'01_Proyectos/Cuaderno de Bitacora (Proyectos)/index.html'

with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace all data-accent="amber" and data-accent="purple" with data-accent="red"
html = html.replace('data-accent="amber"', 'data-accent="red"')
html = html.replace('data-accent="purple"', 'data-accent="red"')

# 2. Replace kicker inline styles: color: #f59e0b; -> color: var(--lda-red);
html = html.replace('style="color: #f59e0b;"', 'style="color: var(--lda-red);"')
html = html.replace('style="color: #2563eb;"', 'style="color: var(--lda-red);"')
html = html.replace('style="color: #8B5CF6;"', 'style="color: var(--lda-red);"')

# 3. Replace blue-card in Gestión de Usuarios
html = html.replace('class="apple-card blue-card"', 'class="apple-card" data-accent="red"')

# 4. Remove purple gradient border in Gestión de la Información
html = re.sub(
    r'<a href="\.\./Gobierno de Informacion/index\.html" class="apple-card" data-accent="red" style="border-color: rgba\(139, 92, 246, 0\.4\); background: linear-gradient\(135deg, var\(--bg-card\) 0%, rgba\(139, 92, 246, 0\.05\) 100%\);"',
    r'<a href="../Gobierno de Informacion/index.html" class="apple-card" data-accent="red"',
    html
)

# 5. Replace Gestión de Usuarios SVG with official Línea Directa icon-user.svg
user_svg_official = """<svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path fill-rule="evenodd" clip-rule="evenodd" d="M12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2ZM1 12C1 5.92487 5.92487 1 12 1C18.0751 1 23 5.92487 23 12C23 18.0751 18.0751 23 12 23C5.92487 23 1 18.0751 1 12ZM12 5.34091C10.6946 5.34091 9.63636 6.39915 9.63636 7.70455C9.63636 9.00995 10.6946 10.0682 12 10.0682C13.3054 10.0682 14.3636 9.00995 14.3636 7.70455C14.3636 6.39915 13.3054 5.34091 12 5.34091ZM8.63636 7.70455C8.63636 5.84686 10.1423 4.34091 12 4.34091C13.8577 4.34091 15.3636 5.84686 15.3636 7.70455C15.3636 9.56223 13.8577 11.0682 12 11.0682C10.1423 11.0682 8.63636 9.56223 8.63636 7.70455ZM12 12.9773C9.11306 12.9773 6.77273 15.3176 6.77273 18.2045C6.77273 18.4807 6.54887 18.7045 6.27273 18.7045C5.99658 18.7045 5.77273 18.4807 5.77273 18.2045C5.77273 14.7653 8.56077 11.9773 12 11.9773C15.4392 11.9773 18.2273 14.7653 18.2273 18.2045C18.2273 18.4807 18.0034 18.7045 17.7273 18.7045C17.4511 18.7045 17.2273 18.4807 17.2273 18.2045C17.2273 15.3176 14.8869 12.9773 12 12.9773Z" fill="currentColor"/>
</svg>"""

old_user_svg = re.search(r'<div class="card-visual" style="color: var\(--lda-red\);">\s*<svg width="96" height="96" viewBox="0 0 80 80".*?</svg>\s*</div>', html, re.DOTALL)
if old_user_svg:
    html = html.replace(old_user_svg.group(0), f'<div class="card-visual" style="color: var(--lda-red);">\n                            {user_svg_official}\n                        </div>')
    print("[+] Gestión de Usuarios SVG replaced with official Línea Directa icon-user.svg")

# 6. Standardize placeholder SVGs (Cards 8, 9, 10) to 24x24 viewBox, width 64 height 64
card8_svg = """<svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="3" y="3" width="7" height="7" rx="1.5" stroke="currentColor" stroke-width="1.2" fill="currentColor" fill-opacity="0.12"/>
    <rect x="14" y="3" width="7" height="7" rx="1.5" stroke="currentColor" stroke-width="1.2" stroke-dasharray="2 1.5"/>
    <rect x="3" y="14" width="7" height="7" rx="1.5" stroke="currentColor" stroke-width="1.2" stroke-dasharray="2 1.5"/>
    <rect x="14" y="14" width="7" height="7" rx="1.5" stroke="currentColor" stroke-width="1.2" fill="currentColor" fill-opacity="0.12"/>
    <circle cx="12" cy="12" r="1.5" fill="currentColor"/>
</svg>"""

card9_svg = """<svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <circle cx="12" cy="12" r="8" stroke="currentColor" stroke-width="1.2" stroke-dasharray="3 2"/>
    <circle cx="12" cy="12" r="2.5" stroke="currentColor" stroke-width="1.2" fill="currentColor" fill-opacity="0.15"/>
    <path d="M12 2V5M12 19V22M2 12H5M19 12H22" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/>
</svg>"""

card10_svg = """<svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M12 4L20 8.5L12 13L4 8.5L12 4Z" stroke="currentColor" stroke-width="1.2" fill="currentColor" fill-opacity="0.12" stroke-linejoin="round"/>
    <path d="M4 12.5L12 17L20 12.5" stroke="currentColor" stroke-width="1.2" stroke-linejoin="round"/>
    <path d="M4 16.5L12 21L20 16.5" stroke="currentColor" stroke-width="1.2" stroke-linejoin="round"/>
</svg>"""

# Replace Card 8 (Nuevo Servicio)
m8 = re.search(r'(<!-- Demo Card 3 -->\s*<div class="apple-card disabled-card">.*?<div class="card-visual"[^>]*>)\s*<svg width="96".*?</svg>(\s*</div>)', html, re.DOTALL)
if m8:
    html = html.replace(m8.group(0), f'{m8.group(1)}\n                            {card8_svg}{m8.group(2)}')
    print("[+] Card 8 placeholder SVG standardized")

# Replace Card 9 (Nueva Operativa)
m9 = re.search(r'(<!-- Demo Card 4 -->\s*<div class="apple-card disabled-card">.*?<div class="card-visual"[^>]*>)\s*<svg width="96".*?</svg>(\s*</div>)', html, re.DOTALL)
if m9:
    html = html.replace(m9.group(0), f'{m9.group(1)}\n                            {card9_svg}{m9.group(2)}')
    print("[+] Card 9 placeholder SVG standardized")

# Replace Card 10 (Próxima Operativa)
m10 = re.search(r'(<!-- Demo Card 5 -->\s*<div class="apple-card disabled-card">.*?<div class="card-visual"[^>]*>)\s*<svg width="96".*?</svg>(\s*</div>)', html, re.DOTALL)
if m10:
    html = html.replace(m10.group(0), f'{m10.group(1)}\n                            {card10_svg}{m10.group(2)}')
    print("[+] Card 10 placeholder SVG standardized")

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("[+] index.html updated successfully with all red corporate styling and official icons!")
