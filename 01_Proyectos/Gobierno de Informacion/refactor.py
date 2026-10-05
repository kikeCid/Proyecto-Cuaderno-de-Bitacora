import os

fp = r'c:\Users\ldaecc\.gemini\antigravity\scratch\Documentacion\02_Proyectos\Gobierno de Informacion\Lidia\estrategia_2026.html'
with open(fp, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace CSS
old_css_start = html.find('        /* Acordeón Premium */')
old_css_end = html.find('</style>')
new_css = """        /* Tabs Premium */
        .tab-nav {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin: 40px auto 30px auto;
            max-width: 900px;
            padding: 5px;
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 100px;
        }
        .tab-btn {
            flex: 1;
            padding: 16px 24px;
            border: none;
            background: transparent;
            color: var(--text-sec);
            font-size: 1.1rem;
            font-weight: 600;
            border-radius: 100px;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .tab-btn:hover {
            color: var(--text-main);
        }
        .tab-btn.active {
            background: var(--lda-red);
            color: white;
            box-shadow: 0 4px 15px rgba(228, 0, 43, 0.3);
        }
        .tab-pane {
            display: none;
            animation: fadeIn 0.4s ease;
        }
        .tab-pane.active {
            display: block;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-10px); }
            to { opacity: 1; transform: translateY(0); }
        }
"""
html = html[:old_css_start] + new_css + html[old_css_end:]

# Replace Hub
hub_start = html.find('            <!-- SUB-HUB: ECOSISTEMA DEL REENFOQUE -->')
hub_end = html.find('            </section>', hub_start) + len('            </section>\n')
hub_html = html[hub_start:hub_end]
html = html[:hub_start] + html[hub_end:]

# Replace Pilares
pil_start = html.find('            <details class="premium-accordion" open>')
pil_end = html.find('            </details>', pil_start) + len('            </details>\n')
pil_html = html[pil_start:pil_end]
pil_html_clean = '                <section class="editorial-section">\n                    <h2>Los 5 Pilares</h2>\n' + pil_html[pil_html.find('                    <div class="pilar-grid">'):pil_html.find('                    </section>')] + '                </section>\n'
html = html[:pil_start] + html[pil_end:]

# Replace Dana
dana_start = html.find('            <!-- SECCIÓN: QUÉ HEMOS APRENDIDO (DANA vs SALUD) -->')
dana_end = html.find('            </details>', dana_start) + len('            </details>\n')
dana_html = html[dana_start:dana_end]
dana_html_clean = '                <!-- SECCIÓN: QUÉ HEMOS APRENDIDO (DANA vs SALUD) -->\n                <section class="editorial-section">\n                    <h2>Qué hemos aprendido (Lo que funciona vs Lo que no)</h2>\n' + dana_html[dana_html.find('                    <div class="case-comparison">'):dana_html.find('                    </section>')] + '                </section>\n'
html = html[:dana_start] + html[dana_end:]

# Replace Estrategia
est_start = html.find('            <!-- REENFOQUE ESTRATÉGICO -->')
est_end = html.find('            </details>', est_start) + len('            </details>\n')
est_html = html[est_start:est_end]
est_html_clean = '                <!-- REENFOQUE ESTRATÉGICO -->\n                <section class="editorial-section">\n                    <h2>Reenfoque Estratégico</h2>\n' + est_html[est_html.find('                    <div style="display: flex; gap: 40px;'):est_html.find('                    </section>')] + '                </section>\n'
html = html[:est_start] + html[est_end:]

# Construct Tabs
tabs_html = """
            <!-- TAB NAV -->
            <nav class="tab-nav">
                <button class="tab-btn active" onclick="switchTab('tab-why', this)">1. El Por Qué</button>
                <button class="tab-btn" onclick="switchTab('tab-paradigm', this)">2. El Nuevo Paradigma</button>
                <button class="tab-btn" onclick="switchTab('tab-hub', this)">3. Ecosistema de Gobierno</button>
            </nav>

            <div id="tab-why" class="tab-pane active">
""" + pil_html_clean + dana_html_clean + """
            </div>

            <div id="tab-paradigm" class="tab-pane">
""" + est_html_clean + """
            </div>

            <div id="tab-hub" class="tab-pane">
""" + hub_html + """
            </div>
"""
inject_pos = html.find('            </header>') + len('            </header>')
html = html[:inject_pos] + tabs_html + html[inject_pos:]

# Clean up any duplicated newlines temporarily created by replacement
html = html.replace('\n\n\n\n', '\n\n')

# Inject JS
js_inject_pos = html.find('<script>') + len('<script>')
js_logic = """
        function switchTab(tabId, btn) {
            document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
            btn.classList.add('active');
            document.getElementById(tabId).classList.add('active');
        }
"""
html = html[:js_inject_pos] + js_logic + html[js_inject_pos:]

with open(fp, 'w', encoding='utf-8') as f:
    f.write(html)
