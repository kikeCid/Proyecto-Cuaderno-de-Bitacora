import os
import re

file_path = 'C:/personal/Proyectos Antigravity/Proyecto Cuaderno de Bitacora/01_Proyectos/HCM/evaluacion_mercado.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# The file got broken after <!-- SERVICENOW -->
# Let's find <!-- SERVICENOW --> and <!-- BIZNEO --> (if it exists)
# Or we can just cut off at <!-- SERVICENOW --> and append the rest of the file correctly.

# We know that the content before <!-- SERVICENOW --> is fine.
parts = content.split('<!-- SERVICENOW -->')
head = parts[0]

# We need the tail part, which starts at `</main>` or similar. 
# Wait, Bizneo might be lost. Let's just append the entire ServiceNow block and Bizneo block.

tail = """            <!-- SERVICENOW -->
            <div class="vendor-card">
                <div class="vendor-header">
                    <div class="vendor-rank rank-4">4º</div>
                    <div class="vendor-title" style="color: #22C55E;">ServiceNow</div>
                </div>

                <div class="metric-group">
                    <div class="metric">
                        <div class="metric-icon">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                stroke-width="2">
                                <rect x="2" y="4" width="20" height="16" rx="2" ry="2"></rect>
                                <line x1="12" y1="8" x2="12" y2="16"></line>
                                <line x1="8" y1="12" x2="16" y2="12"></line>
                            </svg>
                        </div>
                        <div class="metric-content">
                            <span class="metric-label">Presupuesto Estimado</span>
                            <span class="metric-value" style="color: var(--text-sec); font-weight: 400;">Dato no
                                disponible</span>
                        </div>
                    </div>
                    <div class="metric">
                        <div class="metric-icon">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                stroke-width="2">
                                <circle cx="12" cy="12" r="10"></circle>
                                <polyline points="12 6 12 12 16 14"></polyline>
                            </svg>
                        </div>
                        <div class="metric-content">
                            <span class="metric-label">Tiempo Implantación</span>
                            <span class="metric-value" style="color: var(--text-sec); font-weight: 400;">Dato no
                                disponible</span>
                        </div>
                    </div>
                    <div class="metric">
                        <div class="metric-icon">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                stroke-width="2">
                                <polygon
                                    points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2">
                                </polygon>
                            </svg>
                        </div>
                        <div class="metric-content">
                            <span class="metric-label">Sesiones Presenciales</span>
                            <span class="metric-value" style="font-size: 0.95rem; color: var(--text-sec);">No
                                Requeridas</span>
                            <span class="metric-sub">No se consideró funcionalmente necesario mantener sesiones para
                                conocer todas las herramientas disponibles en el mercado.</span>
                        </div>
                    </div>
                </div>

                <div class="vendor-footer rank-4">
                    <span class="metric-label">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2">
                            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                            <polyline points="22 4 12 14.01 9 11.01"></polyline>
                        </svg>
                        VALORACIÓN EQUIPO
                    </span>
                    <p class="valoracion-text">Se desestima esta solución ya que no tiene un producto puro de HCM sino que es un orquestador de plataformas. Sería la mejor opción si fuéramos a un entorno de nichos (una herramienta para cada servicio), ya que lo que sí hacen es poner una capa de unificación de plataforma muy potente y garantizan una experiencia homogénea aunque sean herramientas diferentes.</p>
                </div>
            </div>

            <!-- BIZNEO -->
            <div class="vendor-card">
                <div class="vendor-header">
                    <div class="vendor-rank rank-5">5º</div>
                    <div class="vendor-title" style="color: #4B5563;">Bizneo</div>
                </div>

                <div class="metric-group">
                    <div class="metric">
                        <div class="metric-icon">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                stroke-width="2">
                                <rect x="2" y="4" width="20" height="16" rx="2" ry="2"></rect>
                                <line x1="12" y1="8" x2="12" y2="16"></line>
                                <line x1="8" y1="12" x2="16" y2="12"></line>
                            </svg>
                        </div>
                        <div class="metric-content">
                            <span class="metric-label">Presupuesto Estimado</span>
                            <span class="metric-value" style="color: var(--text-sec); font-weight: 400;">Dato no
                                disponible</span>
                        </div>
                    </div>
                    <div class="metric">
                        <div class="metric-icon">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                stroke-width="2">
                                <circle cx="12" cy="12" r="10"></circle>
                                <polyline points="12 6 12 12 16 14"></polyline>
                            </svg>
                        </div>
                        <div class="metric-content">
                            <span class="metric-label">Tiempo Implantación</span>
                            <span class="metric-value" style="color: var(--text-sec); font-weight: 400;">Dato no
                                disponible</span>
                        </div>
                    </div>
                    <div class="metric">
                        <div class="metric-icon">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                stroke-width="2">
                                <polygon
                                    points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2">
                                </polygon>
                            </svg>
                        </div>
                        <div class="metric-content">
                            <span class="metric-label">Sesiones Presenciales</span>
                            <span class="metric-value" style="font-size: 0.95rem; color: var(--text-sec);">No
                                Requeridas</span>
                            <span class="metric-sub">No se consideró funcionalmente necesario mantener sesiones para
                                conocer todas las herramientas disponibles en el mercado.</span>
                        </div>
                    </div>
                </div>

                <div class="vendor-footer rank-5">
                    <span class="metric-label">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2">
                            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                            <polyline points="22 4 12 14.01 9 11.01"></polyline>
                        </svg>
                        VALORACIÓN EQUIPO
                    </span>
                    <p class="valoracion-text">Solución ágil, pero con dudas sobre escalabilidad para cubrir
                        arquitecturas de nuestra complejidad.</p>
                </div>
            </div>

        </div>
    </main>

    <footer>
        <p>&copy; 2026 Portal de Gestión HCM Cloud | Memoria Corporativa Permanente</p>
    </footer>

    <script>
        function toggleTheme() {
            const checkbox = document.getElementById('theme-checkbox');
            const isDark = checkbox.checked;
            document.documentElement.setAttribute('data-theme', isDark ? 'dark' : 'light');
            localStorage.setItem('theme', isDark ? 'dark' : 'light');
        }

        function initTheme() {
            const savedTheme = localStorage.getItem('theme') || 'light';
            const checkbox = document.getElementById('theme-checkbox');
            document.documentElement.setAttribute('data-theme', savedTheme);
            if (checkbox) checkbox.checked = savedTheme === 'dark';
        }

        document.addEventListener('DOMContentLoaded', initTheme);
    </script>

<script>
// BREADCRUMB MANAGER - DYNAMIC ISLAND
function initDynamicBreadcrumb() {
    const wrapper = document.querySelector('.global-nav-wrapper');
    if (!wrapper) return;
    
    // Check initial scroll position
    if (window.scrollY > 50) wrapper.classList.add('compacted');

    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            wrapper.classList.add('compacted');
        } else {
            wrapper.classList.remove('compacted');
        }
    });

    // Handle touch devices to expand on tap if compacted
    wrapper.addEventListener('click', (e) => {
        if (wrapper.classList.contains('compacted') && window.innerWidth <= 768) {
            e.preventDefault();
            wrapper.classList.remove('compacted');
            // Give them time to click before it auto-compacts again
            setTimeout(() => {
                if (window.scrollY > 50) wrapper.classList.add('compacted');
            }, 3000);
        }
    });
}
document.addEventListener('DOMContentLoaded', initDynamicBreadcrumb);
</script>
</body>

</html>
"""

new_content = head + tail
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)
