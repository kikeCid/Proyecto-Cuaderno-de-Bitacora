svg2 = """<svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <!-- Diadema y Auriculares de Operador (Monitorización de Llamadas) -->
    <path d="M4 11V10C4 5.58 7.58 2 12 2C16.42 2 20 5.58 20 10V11" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/>
    <rect x="2" y="10.5" width="3.2" height="6" rx="1.6" stroke="currentColor" stroke-width="1.3" fill="currentColor" fill-opacity="0.12"/>
    <rect x="18.8" y="10.5" width="3.2" height="6" rx="1.6" stroke="currentColor" stroke-width="1.3" fill="currentColor" fill-opacity="0.12"/>
    <!-- Micrófono hacia el centro -->
    <path d="M19 16.5V17.5C19 19.4 17.5 21 15.5 21H13.5" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/>
    <circle cx="12" cy="21" r="1.2" fill="currentColor"/>
    <!-- Ondas de Voz / Speech Analytics -->
    <path d="M7 11.5V14.5" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/>
    <path d="M9.2 9V17" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/>
    <path d="M11.5 7.5V18.5" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/>
    <path d="M13.8 9.5V16.5" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/>
    <path d="M16 11V15" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/>
    <!-- Chispa de Inteligencia Artificial (AI Sparkle en esquina superior) -->
    <path d="M19.5 2.5C19.5 4 21 4.5 21 4.5C21 4.5 19.5 5 19.5 6.5C19.5 5 18 4.5 18 4.5C18 4.5 19.5 4 19.5 2.5Z" fill="currentColor"/>
</svg>"""

with open('scratch/perseo_icon_v2.svg', 'w', encoding='utf-8') as f:
    f.write(svg2)

print("Created v2 with AI sparkle")
