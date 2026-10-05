# Let's test different SVG representations for Perseo (AI Speech Analytics & Call Quality Monitoring)

svg1 = """<svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <!-- Diadema y Auriculares de Operador -->
    <path d="M4 12V10C4 5.58172 7.58172 2 12 2C16.4183 2 20 5.58172 20 10V12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
    <rect x="2" y="10" width="3.5" height="6.5" rx="1.75" stroke="currentColor" stroke-width="1.3" fill="currentColor" fill-opacity="0.12"/>
    <rect x="18.5" y="10" width="3.5" height="6.5" rx="1.75" stroke="currentColor" stroke-width="1.3" fill="currentColor" fill-opacity="0.12"/>
    <!-- Micrófono hacia la boca -->
    <path d="M19 16.5V18C19 19.6569 17.6569 21 16 21H13.5" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/>
    <circle cx="12" cy="21" r="1.2" fill="currentColor"/>
    <!-- Espectro de Ondas de Voz / Speech Analytics en el centro -->
    <path d="M7.5 12V14" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/>
    <path d="M9.75 10V16" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/>
    <path d="M12 8V18" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/>
    <path d="M14.25 10.5V15.5" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/>
    <path d="M16.5 11.5V14.5" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/>
</svg>"""

print("SVG 1 length:", len(svg1))
with open('scratch/perseo_icon_test.svg', 'w', encoding='utf-8') as f:
    f.write(svg1)
