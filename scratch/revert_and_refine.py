# -*- coding: utf-8 -*-
"""
Script de Refinamiento y Corrección Radical basada en el feedback del usuario:
1. ELIMINAR el bloque de KPIs del banner (Hero limpio, sobrio y libre de mantenimiento).
2. ELIMINAR de las fichas las barras de progreso, porcentajes y estados ficticios.
   Mantener la esencia de BASE DE CONOCIMIENTO (Kicker, Título, Descripción funcional, Tags temáticas y Visual vectorial).
3. ELIMINAR por completo el Smart Auto-Hide (la barra superior se queda FIJA, serena, estable, sin parpadeos ni vaivén).
4. CORREGIR el filtro: al hacer clic en un filtro, NO hacer scroll que corte la barra de filtros por la mitad.
   La barra de filtros permanece 100% visible y accesible en todo momento.
"""

import os
import re
import subprocess

BASE_DIR = r"C:\Proyectos_Claude\Proyecto Cuaderno de Bitacora"
CORE_PY = os.path.join(BASE_DIR, "scratch", "build_unified_core_css.py")
INDEX_HTML = os.path.join(BASE_DIR, "01_Proyectos", "Cuaderno de Bitacora (Proyectos)", "index.html")

# ==============================================================================
# 1. RECOMPILAR CSS UNIFICADOS DIRECTAMENTE
# ==============================================================================
subprocess.run(["python", CORE_PY], check=True)
print("[+] CSS unificados recompilados exitosamente.")

# ==============================================================================
# 2. ACTUALIZAR index.html (HERO SOBRIO + CARDS LIMPIAS + FILTRO SIN SALTO BRUSCO)
# ==============================================================================
with open(INDEX_HTML, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Hero Sobrio y Limpio (Base de Conocimiento)
clean_hero = """        <!-- HERO SEGMENT (BASE DE CONOCIMIENTO) -->
        <header class="hero">
            <div class="hero-top-badges">
                <span class="hero-badge">Base de Conocimiento</span>
                <span class="hero-badge-local">Recurso en Local</span>
            </div>
            <h1>Cuaderno de <br><span>Bitácora</span></h1>
            <p>Ecosistema centralizado de documentación técnica, wikis funcionales y seguimiento de proyectos de Línea Directa Aseguradora.</p>
        </header>"""

hero_pattern = r"<!-- HERO SEGMENT.*?-->\s*<header class=\"hero\">.*?</header>"
html = re.sub(hero_pattern, clean_hero, html, flags=re.DOTALL)

# 2. SECCIÓN 1: GESTIÓN DIRECTA (CARDS LIMPIAS SIN PIPELINES NI PORCENTAJES)
sec1_cards = """                    <!-- Evolución HCM Cloud -->
                    <a href="../HCM/index.html" class="apple-card" data-accent="red">
                        <div class="kicker" style="color: var(--lda-red);"><span class="kicker-dot"></span> GESTIÓN DIRECTA</div>
                        <h3 class="title">Evolución HCM Cloud</h3>
                        <p class="desc">Núcleo integral de RR.HH. Migración estratégica de PeopleSoft a Oracle Cloud Fusion, optimizando la gestión del talento, nóminas y estructura organizativa.</p>
                        
                        <div class="card-tags">
                            <span class="tech-tag">Oracle Cloud</span>
                            <span class="tech-tag">HCM Fusion</span>
                            <span class="tech-tag">REST APIs</span>
                            <span class="tech-tag">PeopleSoft</span>
                        </div>

                        <div class="card-visual" style="color: var(--lda-red);">
                            <svg width="84" height="84" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M22 36 C16.5 36 12 31.5 12 26 C12 21 16 17 21 16.2 C23.5 9.5 30 5 38 5 C39 5 39.5 5.1 40 5.2 C40.5 5.1 41 5 42 5 C50 5 56.5 9.5 59 16.2 C64 17 68 21 68 26 C68 31.5 63.5 36 58 36 Z" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round" fill="currentColor" fill-opacity="0.10"/>
                                <circle cx="40" cy="40" r="5.5" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.3"/>
                                <path d="M31 52 C31 47 35 44 40 44 C45 44 49 47 49 52" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>
                                <circle cx="21" cy="59" r="4.5" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.2"/>
                                <path d="M14 69 C14 65 17 63 21 63 C25 63 28 65 28 69" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
                                <circle cx="59" cy="59" r="4.5" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.2"/>
                                <path d="M52 69 C52 65 55 63 59 63 C63 63 66 65 66 69" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
                                <line x1="34" y1="46" x2="26" y2="55" stroke="currentColor" stroke-width="1.8" stroke-dasharray="3 2"/>
                                <line x1="46" y1="46" x2="54" y2="55" stroke="currentColor" stroke-width="1.8" stroke-dasharray="3 2"/>
                                <line x1="28" y1="66" x2="52" y2="66" stroke="currentColor" stroke-width="1.8" stroke-dasharray="3 3"/>
                            </svg>
                        </div>
                    </a>

                    <!-- Transformación y Eficiencia RRHH -->
                    <a href="../IA Area Personas/index.html" class="apple-card" data-accent="red">
                        <div class="kicker" style="color: var(--lda-red);"><span class="kicker-dot"></span> PENDIENTE APROBACIÓN</div>
                        <h3 class="title">Eficiencia RRHH & IA</h3>
                        <p class="desc">Iniciativa estratégica para automatización de consultas internas, asistentes cognitivos con LidIA y optimización operativa en gestión de personas.</p>
                        
                        <div class="card-tags">
                            <span class="tech-tag">IA Generativa</span>
                            <span class="tech-tag">LidIA MCP</span>
                            <span class="tech-tag">Python</span>
                            <span class="tech-tag">FastAPI</span>
                        </div>

                        <div class="card-visual" style="color: var(--lda-red);">
                            <svg width="84" height="84" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M40 12 Q40 40 68 40 Q40 40 40 68 Q40 40 12 40 Q40 40 40 12 Z" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round" fill="currentColor" fill-opacity="0.14"/>
                                <circle cx="40" cy="40" r="22" stroke="currentColor" stroke-width="1.8" stroke-dasharray="4 3" stroke-linecap="round"/>
                                <circle cx="40" cy="40" r="5" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.35"/>
                                <circle cx="25" cy="25" r="2.5" fill="currentColor"/>
                                <circle cx="55" cy="25" r="2.5" fill="currentColor"/>
                                <circle cx="25" cy="55" r="2.5" fill="currentColor"/>
                                <circle cx="55" cy="55" r="2.5" fill="currentColor"/>
                            </svg>
                        </div>
                    </a>"""

sec1_pattern = r"(<div class=\"carousel-track\" id=\"track-direct\"[^>]*>).*?(</div>\s*<button class=\"carousel-btn right)"
html = re.sub(sec1_pattern, r"\1\n" + sec1_cards + r"\n                \2", html, flags=re.DOTALL)

# 3. SECCIÓN 2: FACILITADORES (CARDS LIMPIAS)
sec2_cards = """                    <!-- Perseo -->
                    <a href="../Perseo/index.html" class="apple-card" data-accent="amber">
                        <div class="kicker" style="color: #f59e0b;"><span class="kicker-dot"></span> FACILITADOR</div>
                        <h3 class="title">Perseo</h3>
                        <p class="desc">Plataforma estratégica core de tramitación y suscripción de pólizas. Arquitectura modular de alto rendimiento para el negocio asegurador.</p>
                        
                        <div class="card-tags">
                            <span class="tech-tag">Core Seguros</span>
                            <span class="tech-tag">Oracle DB</span>
                            <span class="tech-tag">Hexagonal</span>
                            <span class="tech-tag">Alta Disponibilidad</span>
                        </div>

                        <div class="card-visual" style="color: #f59e0b;">
                            <svg width="84" height="84" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <circle cx="40" cy="40" r="30" stroke="currentColor" stroke-width="2.4" fill="currentColor" fill-opacity="0.08"/>
                                <path d="M40 18 L58 40 L40 62 L22 40 Z" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round" fill="currentColor" fill-opacity="0.18"/>
                                <circle cx="40" cy="40" r="6" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.4"/>
                                <circle cx="40" cy="18" r="2.5" fill="currentColor"/>
                                <circle cx="58" cy="40" r="2.5" fill="currentColor"/>
                                <circle cx="40" cy="62" r="2.5" fill="currentColor"/>
                                <circle cx="22" cy="40" r="2.5" fill="currentColor"/>
                            </svg>
                        </div>
                    </a>

                    <!-- CRM Operacional -->
                    <a href="../CRM Operacional/index.html" class="apple-card" data-accent="amber">
                        <div class="kicker" style="color: #f59e0b;"><span class="kicker-dot"></span> FACILITADOR</div>
                        <h3 class="title">CRM Operacional</h3>
                        <p class="desc">Ecosistema integral de gestión comercial y atención omnicanal a asegurados con visión 360°, automatización y trazabilidad total.</p>
                        
                        <div class="card-tags">
                            <span class="tech-tag">Salesforce</span>
                            <span class="tech-tag">Omnicanal</span>
                            <span class="tech-tag">Event-Driven</span>
                            <span class="tech-tag">Kafka</span>
                        </div>

                        <div class="card-visual" style="color: #f59e0b;">
                            <svg width="84" height="84" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <circle cx="40" cy="40" r="14" stroke="currentColor" stroke-width="2.4" fill="currentColor" fill-opacity="0.22"/>
                                <circle cx="40" cy="40" r="5" fill="currentColor"/>
                                <circle cx="16" cy="24" r="7" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.12"/>
                                <circle cx="64" cy="24" r="7" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.12"/>
                                <circle cx="16" cy="56" r="7" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.12"/>
                                <circle cx="64" cy="56" r="7" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.12"/>
                                <line x1="22" y1="28" x2="30" y2="34" stroke="currentColor" stroke-width="1.8"/>
                                <line x1="58" y1="28" x2="50" y2="34" stroke="currentColor" stroke-width="1.8"/>
                                <line x1="22" y1="52" x2="30" y2="46" stroke="currentColor" stroke-width="1.8"/>
                                <line x1="58" y1="52" x2="50" y2="46" stroke="currentColor" stroke-width="1.8"/>
                            </svg>
                        </div>
                    </a>

                    <!-- Telefonía - Genesys Cloud CX -->
                    <a href="../Telefonia - Genesis CX/index.html" class="apple-card" data-accent="amber">
                        <div class="kicker" style="color: #f59e0b;"><span class="kicker-dot"></span> FACILITADOR</div>
                        <h3 class="title">Telefonía Genesys CX</h3>
                        <p class="desc">Transformación de la infraestructura de Contact Center a la nube pública de Genesys. Enrutamiento inteligente y analítica en tiempo real.</p>
                        
                        <div class="card-tags">
                            <span class="tech-tag">Genesys Cloud</span>
                            <span class="tech-tag">WebRTC</span>
                            <span class="tech-tag">VoIP</span>
                            <span class="tech-tag">IVR Inteligente</span>
                        </div>

                        <div class="card-visual" style="color: #f59e0b;">
                            <svg width="84" height="84" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <circle cx="40" cy="40" r="28" stroke="currentColor" stroke-width="2" stroke-dasharray="4 3" opacity="0.4"/>
                                <path d="M40 20 A20 20 0 0 1 60 40" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/>
                                <path d="M40 26 A14 14 0 0 1 54 40" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                                <path d="M26 32 C26 44 36 54 48 54 L52 50 L47 44 L42 46 C38 43 37 42 34 38 L36 33 L30 28 Z" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round" fill="currentColor" fill-opacity="0.25"/>
                            </svg>
                        </div>
                    </a>

                    <!-- Reingeniería de Siniestros -->
                    <a href="../Reingenieria Siniestros/index.html" class="apple-card" data-accent="amber">
                        <div class="kicker" style="color: #f59e0b;"><span class="kicker-dot"></span> FACILITADOR</div>
                        <h3 class="title">Reingeniería Siniestros</h3>
                        <p class="desc">Modernización integral del ciclo de vida del siniestro: peritación digital, detección de fraude y agilización del pago a clientes.</p>
                        
                        <div class="card-tags">
                            <span class="tech-tag">BPMN 2.0</span>
                            <span class="tech-tag">Automatización</span>
                            <span class="tech-tag">Workflow Engine</span>
                            <span class="tech-tag">Fraude</span>
                        </div>

                        <div class="card-visual" style="color: #f59e0b;">
                            <svg width="84" height="84" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M40 12 L64 24 V44 C64 57 53 66 40 70 C27 66 16 57 16 44 V24 Z" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round" fill="currentColor" fill-opacity="0.10"/>
                                <path d="M40 18 L58 28 V44 C58 53 49 61 40 64 C31 61 22 53 22 44 V28 Z" stroke="currentColor" stroke-width="1.6" fill="currentColor" fill-opacity="0.15"/>
                                <path d="M30 40 L37 47 L51 33" stroke="currentColor" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                        </div>
                    </a>"""

sec2_pattern = r"(<div class=\"carousel-track\" id=\"track-facilitator\"[^>]*>).*?(</div>\s*<button class=\"carousel-btn right)"
html = re.sub(sec2_pattern, r"\1\n" + sec2_cards + r"\n                \2", html, flags=re.DOTALL)

# 4. SECCIÓN 3: SERVICIOS TRANSVERSALES (CARDS LIMPIAS)
sec3_cards = """                    <!-- Gestión de Usuarios y Accesos -->
                    <a href="../Gestion de Usuarios/index.html" class="apple-card" data-accent="blue">
                        <div class="kicker" style="color: #2563eb;"><span class="kicker-dot"></span> SERVICIO TRANSVERSAL</div>
                        <h3 class="title">Gestión de Usuarios</h3>
                        <p class="desc">Plataforma transversal de control de accesos, autenticación multifactor, roles de usuario y gobierno de identidad corporativa.</p>
                        
                        <div class="card-tags">
                            <span class="tech-tag">Active Directory</span>
                            <span class="tech-tag">IAM / SSO</span>
                            <span class="tech-tag">RBAC</span>
                            <span class="tech-tag">Auditoría</span>
                        </div>

                        <div class="card-visual" style="color: #2563eb;">
                            <svg width="84" height="84" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <circle cx="33" cy="30" r="9" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.25"/>
                                <path d="M18 55 C18 46 25 43 33 43 C41 43 48 46 48 55" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>
                                <circle cx="53" cy="27" r="7" stroke="currentColor" stroke-width="1.8" fill="currentColor" fill-opacity="0.15"/>
                                <path d="M48 41 C52 41 62 43 62 51" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
                                <rect x="36" y="56" width="22" height="15" rx="3.5" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.3"/>
                                <path d="M41 56 V50 C41 47 43 45 47 45 C51 45 53 47 53 50 V56" stroke="currentColor" stroke-width="2"/>
                                <circle cx="47" cy="63" r="1.8" fill="currentColor"/>
                            </svg>
                        </div>
                    </a>

                    <!-- Arquitectura & Plataforma (Reservado) -->
                    <div class="apple-card disabled-card" data-accent="blue">
                        <div class="kicker" style="color: var(--text-muted);">INFRAESTRUCTURA</div>
                        <h3 class="title" style="color: var(--text-muted);">Arquitectura Base</h3>
                        <p class="desc">Estándares corporativos de integración, catálogos de APIs y directrices de seguridad técnica.</p>
                        
                        <div class="card-tags">
                            <span class="tech-tag">CI/CD</span>
                            <span class="tech-tag">Docker</span>
                            <span class="tech-tag">API Gateway</span>
                        </div>

                        <div class="card-visual" style="opacity: 0.5;">
                            <svg width="84" height="84" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <rect x="18" y="16" width="44" height="12" rx="3" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.25"/>
                                <rect x="18" y="34" width="44" height="12" rx="3" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.18"/>
                                <rect x="18" y="52" width="44" height="12" rx="3" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.10"/>
                                <circle cx="26" cy="22" r="2" fill="currentColor"/>
                                <circle cx="26" cy="40" r="2" fill="currentColor"/>
                                <circle cx="26" cy="58" r="2" fill="currentColor"/>
                            </svg>
                        </div>
                    </div>

                    <!-- Gobernanza de Datos (Reservado) -->
                    <div class="apple-card disabled-card" data-accent="blue">
                        <div class="kicker" style="color: var(--text-muted);">DATA OFFICE</div>
                        <h3 class="title" style="color: var(--text-muted);">Calidad de Datos</h3>
                        <p class="desc">Modelos maestros de datos, linaje analítico y catálogo para auditorías regulatorias.</p>
                        
                        <div class="card-tags">
                            <span class="tech-tag">Data Quality</span>
                            <span class="tech-tag">GDPR</span>
                            <span class="tech-tag">Linaje</span>
                        </div>

                        <div class="card-visual" style="opacity: 0.5;">
                            <svg width="84" height="84" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <ellipse cx="40" cy="22" rx="24" ry="9" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.25"/>
                                <path d="M16 22 V39 C16 44 27 48 40 48 C53 48 64 44 64 39 V22" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.15"/>
                                <path d="M16 39 V56 C16 61 27 65 40 65 C53 65 64 61 64 56 V39" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.08"/>
                            </svg>
                        </div>
                    </div>

                    <!-- Oficina Técnica QA (Reservado) -->
                    <div class="apple-card disabled-card" data-accent="blue">
                        <div class="kicker" style="color: var(--text-muted);">CALIDAD & TESTING</div>
                        <h3 class="title" style="color: var(--text-muted);">Oficina Técnica QA</h3>
                        <p class="desc">Automatización de pruebas funcionales, rendimiento y control de regresión antes de paso a producción.</p>
                        
                        <div class="card-tags">
                            <span class="tech-tag">Cypress</span>
                            <span class="tech-tag">SonarQube</span>
                            <span class="tech-tag">Testing</span>
                        </div>

                        <div class="card-visual" style="opacity: 0.5;">
                            <svg width="84" height="84" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <circle cx="40" cy="40" r="26" stroke="currentColor" stroke-width="2.2" fill="currentColor" fill-opacity="0.10"/>
                                <path d="M28 40 L36 48 L52 32" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                        </div>
                    </div>"""

sec3_pattern = r"(<div class=\"carousel-track\" id=\"track-services\"[^>]*>).*?(</div>\s*<button class=\"carousel-btn right)"
html = re.sub(sec3_pattern, r"\1\n" + sec3_cards + r"\n                \2", html, flags=re.DOTALL)

# 5. SECCIÓN 4: HISTÓRICO (CARDS LIMPIAS)
sec4_cards = """                    <!-- Gestión de la Información (Traspasado a Transformación) -->
                    <a href="../Gobierno de Informacion/index.html" class="apple-card" data-accent="purple" style="border-color: rgba(139, 92, 246, 0.4); background: linear-gradient(135deg, var(--bg-card) 0%, rgba(139, 92, 246, 0.05) 100%);">
                        <div class="kicker" style="color: #8B5CF6;"><span class="kicker-dot"></span> HISTÓRICO TRASPASADO</div>
                        <h3 class="title">Gestión de la Información</h3>
                        <p class="desc">Proyecto de Inteligencia LidIA y metodología GIN transferido al Área de Transformación. Conserva aquí todo el contexto, historial y wiki funcional.</p>
                        
                        <div class="card-tags">
                            <span class="tech-tag">Inteligencia LidIA</span>
                            <span class="tech-tag">Metodología GIN</span>
                            <span class="tech-tag">Data Governance</span>
                            <span class="tech-tag">Histórico</span>
                        </div>

                        <div class="card-visual" style="color: #8B5CF6;">
                            <svg width="84" height="84" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M40 13 L66 28 L40 43 L14 28 Z" stroke="#8B5CF6" stroke-width="2.2" stroke-linejoin="round" fill="#8B5CF6" fill-opacity="0.12"/>
                                <path d="M14 28 L40 43 L40 72 L14 58 Z" stroke="#8B5CF6" stroke-width="2.2" stroke-linejoin="round" fill="#8B5CF6" fill-opacity="0.18"/>
                                <path d="M40 43 L66 28 L66 58 L40 72 Z" stroke="#8B5CF6" stroke-width="2.2" stroke-linejoin="round" fill="#8B5CF6" fill-opacity="0.26"/>
                                <circle cx="40" cy="43" r="4.5" fill="#8B5CF6"/>
                                <circle cx="40" cy="13" r="3" fill="#8B5CF6"/>
                                <circle cx="66" cy="28" r="3" fill="#8B5CF6"/>
                                <circle cx="14" cy="28" r="3" fill="#8B5CF6"/>
                                <circle cx="40" cy="72" r="3" fill="#8B5CF6"/>
                            </svg>
                        </div>
                    </a>

                    <!-- Archivo Histórico Card 1 -->
                    <div class="apple-card disabled-card" data-accent="purple">
                        <div class="kicker" style="color: var(--text-muted);">HISTORIAL ARCHIVADO</div>
                        <h3 class="title" style="color: var(--text-muted);">Archivo de Porfolio</h3>
                        <p class="desc">Espacio reservado para almacenar el historial de proyectos concluidos en ciclos anteriores.</p>
                        
                        <div class="card-tags">
                            <span class="tech-tag">Ciclos Anteriores</span>
                            <span class="tech-tag">Auditoría</span>
                        </div>

                        <div class="card-visual" style="opacity: 0.5;">
                            <svg width="84" height="84" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <rect x="16" y="14" width="48" height="52" rx="6" stroke="currentColor" stroke-width="2.4" fill="currentColor" fill-opacity="0.12"/>
                                <circle cx="40" cy="40" r="13" stroke="currentColor" stroke-width="2.2"/>
                                <circle cx="40" cy="40" r="5" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.35"/>
                            </svg>
                        </div>
                    </div>

                    <!-- Archivo Histórico Card 2 -->
                    <div class="apple-card disabled-card" data-accent="purple">
                        <div class="kicker" style="color: var(--text-muted);">REPOSITORIO</div>
                        <h3 class="title" style="color: var(--text-muted);">Registro Histórico</h3>
                        <p class="desc">Conservación de memorias técnicas, lecciones aprendidas y acuerdos de gobernanza pasados.</p>
                        
                        <div class="card-tags">
                            <span class="tech-tag">Lecciones</span>
                            <span class="tech-tag">Memorias</span>
                        </div>

                        <div class="card-visual" style="opacity: 0.5;">
                            <svg width="84" height="84" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <rect x="18" y="16" width="44" height="48" rx="5" stroke="currentColor" stroke-width="2.4" fill="currentColor" fill-opacity="0.12"/>
                                <line x1="26" y1="16" x2="26" y2="64" stroke="currentColor" stroke-width="2"/>
                                <path d="M37 16 V34 L41 30 L45 34 V16" stroke="currentColor" stroke-width="2" fill="currentColor" fill-opacity="0.3"/>
                            </svg>
                        </div>
                    </div>"""

sec4_pattern = r"(<div class=\"carousel-track\" id=\"track-closed\"[^>]*>).*?(</div>\s*<button class=\"carousel-btn right)"
html = re.sub(sec4_pattern, r"\1\n" + sec4_cards + r"\n                \2", html, flags=re.DOTALL)

# ==============================================================================
# 3. JAVASCRIPT: ELIMINAR SMART AUTO-HIDE Y ARREGLAR FILTRADO SIN SALTO CORTADO
# ==============================================================================
# Buscamos la función filterPortfolio y la limpiamos
clean_filter_js = """        // ==========================================
        // 3. SEGMENTED CONTROL: FILTRADO POR CARRILES (SIN SALTOS BRUSCOS)
        // ==========================================
        function filterPortfolio(category, btn) {
            // Actualizar botones de filtro
            document.querySelectorAll('.filter-chip').forEach(c => c.classList.remove('active'));
            if (btn) btn.classList.add('active');

            const sections = document.querySelectorAll('.portfolio-section');
            sections.forEach(sec => {
                const secCat = sec.getAttribute('data-category');
                if (category === 'all' || secCat === category) {
                    sec.classList.remove('section-hidden');
                } else {
                    sec.classList.add('section-hidden');
                }
            });

            // NO forzamos scrollIntoView de la sección para evitar que la barra de filtros se corte
            // Si el usuario está scrolleado muy abajo, acomodamos suavemente la barra de filtros
            const filterBar = document.querySelector('.view-controls-bar');
            if (filterBar) {
                const barRect = filterBar.getBoundingClientRect();
                if (barRect.top < 70) {
                    filterBar.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            }
        }"""

filter_pattern = r"// ==========================================\s*// 3\. SEGMENTED CONTROL:.*?function filterPortfolio\(category, btn\) \{.*?\n        \}"
html = re.sub(filter_pattern, clean_filter_js, html, flags=re.DOTALL)

# Eliminamos la lógica de handleScrollDynamics (auto-hide que molestaba) y dejamos solo spotlight
clean_scripts_end = """        // ==========================================
        // SPOTLIGHT INTERACTIVO SUAVE EN TARJETAS
        // ==========================================
        function initCardSpotlights() {
            document.querySelectorAll('.apple-card').forEach(card => {
                card.addEventListener('mousemove', (e) => {
                    const rect = card.getBoundingClientRect();
                    const x = e.clientX - rect.left;
                    const y = e.clientY - rect.top;
                    card.style.setProperty('--mouse-x', `${x}px`);
                    card.style.setProperty('--mouse-y', `${y}px`);
                });
            });
        }

        // Inicialización
        document.addEventListener('DOMContentLoaded', () => {
            initCardSpotlights();
        });

        // Inicializar Lucide si hay iconos dinámicos
        if (window.lucide) {
            lucide.createIcons();
        }"""

# Reemplazamos la sección de handleScrollDynamics
scroll_dynamics_pattern = r"// ==========================================\s*// SMART AUTO-HIDE & LIQUID GLASS TOPBAR.*?if \(window\.lucide\) \{\s*lucide\.createIcons\(\);\s*\}"
html = re.sub(scroll_dynamics_pattern, clean_scripts_end, html, flags=re.DOTALL)

with open(INDEX_HTML, "w", encoding="utf-8") as f:
    f.write(html)

print("[+] index.html completamente refinado: Hero limpio, sin KPIs ficticios, sin Auto-Hide y filtros estables.")
print("[OK] Todo completado con éxito.")
