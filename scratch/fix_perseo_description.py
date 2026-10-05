import re

perseo_svg = """<svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
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

# Save asset
with open(r'01_Proyectos/assets/img/perseo-speech-analytics.svg', 'w', encoding='utf-8') as f:
    f.write(perseo_svg)
print("[+] Saved 01_Proyectos/assets/img/perseo-speech-analytics.svg")

index_path = r'01_Proyectos/Cuaderno de Bitacora (Proyectos)/index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Perseo card
old_perseo_card_pattern = r'<!-- Perseo.*?-->\s*<a href="\.\./Perseo/index\.html" class="apple-card" data-accent="red">.*?</a>'
new_perseo_card = f"""<!-- Perseo (Analítica con IA & Supervisión de Calidad) -->
                    <a href="../Perseo/index.html" class="apple-card" data-accent="red">
                        <div class="kicker" style="color: var(--lda-red);"><span class="kicker-dot"></span> FACILITADOR</div>
                        <h3 class="title">Perseo</h3>
                        <p class="desc">Analítica con IA para supervisar la calidad y la aplicación de operativas en todos los ramos y servicios (Comercial, Atención al Cliente y Siniestros), monitorizando y analizando las llamadas de clientes y operadores.</p>
                        <div class="card-tags">
                            <span class="tech-tag">Analítica con IA</span>
                            <span class="tech-tag">Supervisión de Calidad</span>
                            <span class="tech-tag">Monitorización de Llamadas</span>
                            <span class="tech-tag">Comercial & Siniestros</span>
                            <span class="tech-tag">Speech Analytics</span>
                        </div>
                        <div class="card-visual" style="color: var(--lda-red);">
                            {perseo_svg}
                        </div>
                    </a>"""

html = re.sub(old_perseo_card_pattern, new_perseo_card, html, flags=re.DOTALL)

# Replace footer link
html = html.replace('Core Perseo (Pólizas)', 'Perseo (IA & Calidad de Llamadas)')

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("[+] index.html updated successfully with authentic Perseo description and AI Voice Analytics icon!")
