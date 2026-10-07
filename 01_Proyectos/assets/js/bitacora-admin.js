/**
 * MÓDULO DE ADMINISTRACIÓN REACTIVA DEL PORTFOLIO
 * Línea Directa Aseguradora - Cuaderno de Bitácora
 * Persistencia en disco mediante File System Access API nativa (sin servidor de fondo).
 * Edición y gobernanza visual de iniciativas, carriles, estados y licitaciones.
 */

(function () {
    // ==========================================
    // HELPERS DE ICONOGRAFÍA LINEAL CORPORATIVA (LÍNEA DIRECTA ASEGURADORA)
    // ==========================================
    const LDA_ICONS = {
        licitacion: `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lda-svg-icon" style="color: var(--lda-red);"><path d="m16 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="m2 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="M7 21h10"/><path d="M12 3v18"/><path d="M3 7h2c2 0 5-1 7-2 2 1 5 2 7 2h2"/></svg>`,
        replan: `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lda-svg-icon" style="color: var(--lda-red);"><path d="M8 2v4"/><path d="M16 2v4"/><rect width="18" height="18" x="3" y="4" rx="2"/><path d="M3 10h18"/><path d="m9 16 2 2 4-4"/></svg>`,
        pausa: `<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" class="lda-svg-icon" style="color: var(--lda-red); vertical-align: -1px; margin-right: 4px;"><rect x="6" y="4" width="4" height="16" rx="1"/><rect x="14" y="4" width="4" height="16" rx="1"/></svg>`,
        decision: `<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" class="lda-svg-icon" style="color: var(--lda-red); vertical-align: -1px; margin-right: 4px;"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>`,
        settings: `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lda-svg-icon" style="color: var(--lda-red); vertical-align: -2px; margin-right: 5px;"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>`
    };

    // ==========================================
    // CAPA INDEXEDDB: AUTO-GUARDADO PERSISTENTE EN DISCO
    // ==========================================
    const DB_NAME = 'BitacoraStorageDB';
    const DB_VERSION = 1;
    const STORE_NAME = 'file_handles';
    const KEY_HANDLE = 'projects_data_js';

    function openBitacoraDB() {
        return new Promise((resolve, reject) => {
            const req = indexedDB.open(DB_NAME, DB_VERSION);
            req.onupgradeneeded = (e) => {
                const db = e.target.result;
                if (!db.objectStoreNames.contains(STORE_NAME)) {
                    db.createObjectStore(STORE_NAME);
                }
            };
            req.onsuccess = () => resolve(req.result);
            req.onerror = () => reject(req.error);
        });
    }

    async function getStoredHandle() {
        try {
            const db = await openBitacoraDB();
            return new Promise((resolve) => {
                const tx = db.transaction(STORE_NAME, 'readonly');
                const store = tx.objectStore(STORE_NAME);
                const req = store.get(KEY_HANDLE);
                req.onsuccess = () => resolve(req.result || null);
                req.onerror = () => resolve(null);
            });
        } catch (_) {
            return null;
        }
    }

    async function storeHandle(handle) {
        try {
            const db = await openBitacoraDB();
            return new Promise((resolve, reject) => {
                const tx = db.transaction(STORE_NAME, 'readwrite');
                const store = tx.objectStore(STORE_NAME);
                const req = store.put(handle, KEY_HANDLE);
                req.onsuccess = () => resolve(true);
                req.onerror = () => reject(req.error);
            });
        } catch (_) {
            return false;
        }
    }

    async function clearStoredHandle() {
        try {
            const db = await openBitacoraDB();
            return new Promise((resolve) => {
                const tx = db.transaction(STORE_NAME, 'readwrite');
                const store = tx.objectStore(STORE_NAME);
                const req = store.delete(KEY_HANDLE);
                req.onsuccess = () => resolve(true);
                req.onerror = () => resolve(false);
            });
        } catch (_) {
            return false;
        }
    }

    const BitacoraAdmin = {
        projects: [],
        fileHandle: null,
        isOpen: false,
        activeTab: 'all',
        searchTerm: '',

        init: async function () {
            // Cargar catálogo maestro inicial
            if (window.BITACORA_PROJECTS_DATA && Array.isArray(window.BITACORA_PROJECTS_DATA)) {
                this.projects = JSON.parse(JSON.stringify(window.BITACORA_PROJECTS_DATA));
            } else {
                this.projects = [];
            }

            // Recuperar handle físico guardado previamente de IndexedDB para auto-guardado
            try {
                this.fileHandle = await getStoredHandle();
            } catch (_) {}

            // Aplicar reactividad a la interfaz al arrancar
            this.applyStateToUI();
            this.injectAdminTrigger();
        },

        // ==========================================
        // 1. INYECCIÓN DEL BOTÓN EN CABECERA Y ACCIONES RÁPIDAS
        // ==========================================
        injectAdminTrigger: function () {
            // A) En la Cabecera Flotante (Island Actions)
            const islandActions = document.querySelector('.island-actions');
            if (islandActions && !document.getElementById('btn-admin-drawer')) {
                const adminBtn = document.createElement('button');
                adminBtn.id = 'btn-admin-drawer';
                adminBtn.className = 'island-admin-btn';
                adminBtn.title = 'Gestión de Estados y Portfolio (G)';
                adminBtn.setAttribute('aria-label', 'Centro de Gestión del Portfolio');
                adminBtn.innerHTML = `
                    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="12" cy="12" r="3"></circle>
                        <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path>
                    </svg>
                    <span>Gestión Estados</span>
                `;
                adminBtn.onclick = () => this.toggleDrawer();

                const themeBtn = document.getElementById('theme-toggle-btn');
                if (themeBtn) {
                    islandActions.insertBefore(adminBtn, themeBtn);
                } else {
                    islandActions.appendChild(adminBtn);
                }
            }

            // B) Enlace contextual dentro del Modal de Licitaciones
            const modalFooter = document.querySelector('.licitaciones-modal-footer');
            if (modalFooter && !document.getElementById('link-admin-licitaciones')) {
                const adminLink = document.createElement('button');
                adminLink.id = 'link-admin-licitaciones';
                adminLink.className = 'licitaciones-admin-action-btn';
                adminLink.innerHTML = `${LDA_ICONS.settings}<span>Modificar qué proyectos están en Licitación</span>`;
                adminLink.onclick = () => {
                    if (typeof closeLicitacionesModal === 'function') closeLicitacionesModal();
                    BitacoraAdmin.openDrawer('licitacion');
                };
                modalFooter.insertBefore(adminLink, modalFooter.firstChild);
            }

            // C) En la barra flotante de acciones rápidas (inferior derecha)
            const quickActions = document.getElementById('quick-actions-bar');
            if (quickActions && !document.getElementById('btn-admin-quick-action')) {
                const quickBtn = document.createElement('button');
                quickBtn.id = 'btn-admin-quick-action';
                quickBtn.className = 'quick-action-btn';
                quickBtn.title = 'Gestión de Estados y Portfolio (G)';
                quickBtn.setAttribute('aria-label', 'Gestión de Estados');
                quickBtn.innerHTML = `
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="12" cy="12" r="3"></circle>
                        <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path>
                    </svg>
                `;
                quickBtn.onclick = () => this.toggleDrawer();
                quickActions.insertBefore(quickBtn, quickActions.firstChild);
            }
        },

        // ==========================================
        // 2. MOTOR REACTIVO: ACTUALIZAR DOM EN TIEMPO REAL
        // ==========================================
        applyStateToUI: function () {
            if (!this.projects || this.projects.length === 0) return;

            // A) RECALCULAR INDICADORES (KPIS)
            const total = this.projects.length;
            const strategics = this.projects.filter(p => p.carril === 'strategic').length;
            const directs = this.projects.filter(p => p.carril === 'direct').length;
            const licitaciones = this.projects.filter(p => p.licitacion === true).length;
            const facilitators = this.projects.filter(p => p.carril === 'facilitator').length;
            const services = this.projects.filter(p => p.carril === 'services').length;
            const closed = this.projects.filter(p => p.carril === 'closed').length;

            // Actualizar tarjetas KPI
            const kpiCards = document.querySelectorAll('.executive-stats-strip .kpi-clean-card');
            if (kpiCards.length >= 4) {
                const valTotal = kpiCards[0].querySelector('.kpi-clean-value');
                if (valTotal) { valTotal.innerText = total; valTotal.setAttribute('data-count', total); }

                const valStrat = kpiCards[1].querySelector('.kpi-clean-value');
                if (valStrat) { valStrat.innerText = strategics; valStrat.setAttribute('data-count', strategics); }

                const valDir = kpiCards[2].querySelector('.kpi-clean-value');
                if (valDir) { valDir.innerText = directs; valDir.setAttribute('data-count', directs); }

                const valLic = kpiCards[3].querySelector('.kpi-clean-value');
                if (valLic) { valLic.innerText = licitaciones; valLic.setAttribute('data-count', licitaciones); }
                kpiCards[3].title = `Pulsar para ver los ${licitaciones} proyectos en licitación`;
            }

            // B) ACTUALIZAR CONTADORES DE LOS FILTROS DE LA PÁGINA
            const filterChips = document.querySelectorAll('.filter-segments .filter-chip');
            if (filterChips.length >= 6) {
                const counts = [total, directs, strategics, facilitators, services, closed];
                filterChips.forEach((chip, i) => {
                    const countEl = chip.querySelector('.filter-count');
                    if (countEl && counts[i] !== undefined) countEl.innerText = counts[i];
                });
            }

            // C) ACTUALIZAR CONTADORES DE CABECERA DE SECCIÓN
            const mapSecCount = {
                'seccion-directa': directs,
                'seccion-estrategicos': strategics,
                'seccion-facilitadores': facilitators,
                'seccion-servicios': services,
                'seccion-cerrados': closed
            };
            Object.keys(mapSecCount).forEach(secId => {
                const sec = document.getElementById(secId);
                if (sec) {
                    const counter = sec.querySelector('.section-counter');
                    if (counter) counter.innerText = mapSecCount[secId];
                }
            });

            // D) ACTUALIZAR TARJETAS EN LOS CARRUSELES
            this.projects.forEach(p => {
                const card = document.querySelector(`.apple-card[href*="${p.id}"]`) ||
                             document.querySelector(`.apple-card[id*="${p.id}"]`) ||
                             Array.from(document.querySelectorAll('.apple-card')).find(c => {
                                 const t = c.querySelector('.title');
                                 return t && t.innerText.toLowerCase().includes(p.title.toLowerCase());
                             });

                if (card) {
                    if (p.licitacion) {
                        card.setAttribute('data-licitacion', 'true');
                    } else {
                        card.removeAttribute('data-licitacion');
                    }

                    // Etiquetas visuales de la tarjeta
                    const tagsContainer = card.querySelector('.card-tags');
                    if (tagsContainer) {
                        let licTag = tagsContainer.querySelector('.tag-licitacion');
                        if (p.licitacion) {
                            if (!licTag) {
                                licTag = document.createElement('span');
                                licTag.className = 'tech-tag tag-licitacion';
                                licTag.style.background = 'rgba(228, 0, 43, 0.08)';
                                licTag.style.color = 'var(--lda-red)';
                                licTag.style.borderColor = 'rgba(228, 0, 43, 0.25)';
                                tagsContainer.insertBefore(licTag, tagsContainer.firstChild);
                            }
                            licTag.innerHTML = `${LDA_ICONS.licitacion.replace('width="18" height="18"', 'width="12" height="12" style="vertical-align: -1px; margin-right: 3px;"')}<span>Licitación</span>`;
                        } else if (licTag) {
                            licTag.remove();
                        }

                        // Etiqueta de fase especial (En Pausa / Parado o En Decisión)
                        let specialTag = tagsContainer.querySelector('.tag-fase-special');
                        const isPaused = p.estado === 'En Pausa / Parado' || p.estado === 'Parado' || p.semaforo === 'pausa';
                        if (isPaused) {
                            if (!specialTag) {
                                specialTag = document.createElement('span');
                                tagsContainer.appendChild(specialTag);
                            }
                            specialTag.className = 'tech-tag tag-fase-special tag-pausa';
                            specialTag.innerHTML = `${LDA_ICONS.pausa}<span>Parado</span>`;
                            card.classList.add('is-paused');
                        } else if (p.estado === 'En Decisión') {
                            if (!specialTag) {
                                specialTag = document.createElement('span');
                                tagsContainer.appendChild(specialTag);
                            }
                            specialTag.className = 'tech-tag tag-fase-special tag-decision';
                            specialTag.innerHTML = `${LDA_ICONS.decision}<span>En Decisión</span>`;
                            card.classList.remove('is-paused');
                        } else {
                            if (specialTag) specialTag.remove();
                            card.classList.remove('is-paused');
                        }

                        // Etiqueta de Replanificación
                        let replanTag = tagsContainer.querySelector('.tag-replanificado');
                        if (p.replanificado) {
                            if (!replanTag) {
                                replanTag = document.createElement('span');
                                replanTag.className = 'tech-tag tag-replanificado';
                                tagsContainer.appendChild(replanTag);
                            }
                            replanTag.innerHTML = `${LDA_ICONS.replan.replace('width="18" height="18"', 'width="12" height="12" style="vertical-align: -1px; margin-right: 3px;"')}<span>Replanificado</span>`;
                        } else if (replanTag) {
                            replanTag.remove();
                        }
                    }

                    // Reubicar de carril si el usuario cambió su sección
                    const targetSecId = {
                        'direct': 'seccion-directa',
                        'strategic': 'seccion-estrategicos',
                        'facilitator': 'seccion-facilitadores',
                        'services': 'seccion-servicios',
                        'closed': 'seccion-cerrados'
                    }[p.carril];

                    if (targetSecId) {
                        const targetTrack = document.querySelector(`#${targetSecId} .carousel-track`);
                        const currentTrack = card.closest('.carousel-track');
                        if (targetTrack && currentTrack && targetTrack !== currentTrack) {
                            targetTrack.appendChild(card);
                        }
                    }
                }
            });

            // E) ACTUALIZAR MODAL DE LICITACIONES Y CONTADORES DEL CAJÓN
            this.renderLicitacionesModalContent();
            this.updateDrawerStats();
        },

        // ==========================================
        // 3. ACTUALIZACIÓN DEL POPUP DE LICITACIONES
        // ==========================================
        renderLicitacionesModalContent: function () {
            const listContainer = document.querySelector('.licitaciones-projects-list');
            if (!listContainer) return;

            const licitados = this.projects.filter(p => p.licitacion === true);

            if (licitados.length === 0) {
                listContainer.innerHTML = `
                    <div style="text-align: center; padding: 40px 20px; color: var(--text-sec);">
                        <div style="margin-bottom: 12px; color: var(--lda-red);">${LDA_ICONS.licitacion.replace('width="18" height="18"', 'width="40" height="40"')}</div>
                        <h4 style="color: var(--text-main); font-weight: 700; margin-bottom: 6px;">No hay concursos activos</h4>
                        <p style="font-size: 0.9rem; margin: 0;">Actualmente no hay iniciativas en fase de licitación o pliegos abiertos.</p>
                    </div>
                `;
                return;
            }

            listContainer.innerHTML = licitados.map(item => `
                <div class="licitacion-project-item">
                    <div>
                        <div class="licitacion-item-header">
                            <span class="licitacion-item-carril">${this.getCarrilName(item.carril)}</span>
                            <span class="licitacion-item-badge">${item.estado || 'En Licitación'}</span>
                        </div>
                        <h4 class="licitacion-item-title">${item.title}</h4>
                        <p class="licitacion-item-desc">${item.desc}</p>
                    </div>
                    <div class="licitacion-item-footer">
                        <div class="licitacion-item-tags">
                            ${(item.tags || []).map(t => `<span class="licitacion-item-tag">${t}</span>`).join('')}
                        </div>
                        <a href="${item.href}" class="licitacion-item-btn">Ver Proyecto &rarr;</a>
                    </div>
                </div>
            `).join('');
        },

        getCarrilName: function (carril) {
            const map = {
                'direct': 'Gestión Directa',
                'strategic': 'Proyecto Estratégico',
                'facilitator': 'Facilitador / Afectado',
                'services': 'Servicios y Operativas',
                'closed': 'Histórico / Cerrados'
            };
            return map[carril] || 'Proyecto';
        },

        getAcronym: function (proj) {
            if (proj.id) {
                const parts = proj.id.split('-');
                if (parts.length > 1) {
                    return (parts[0].substring(0, 2) + parts[1].substring(0, 2)).toUpperCase();
                }
                return proj.id.substring(0, 4).toUpperCase();
            }
            return 'PROJ';
        },

        // ==========================================
        // 4. CONSTRUCCIÓN DEL CAJÓN DE ADMINISTRACIÓN
        // ==========================================
        buildDrawer: function () {
            let backdrop = document.getElementById('bitacora-admin-backdrop');
            if (backdrop) return backdrop;

            backdrop = document.createElement('div');
            backdrop.id = 'bitacora-admin-backdrop';
            backdrop.className = 'bitacora-admin-backdrop';
            backdrop.innerHTML = `
                <div class="bitacora-admin-drawer" role="dialog" aria-modal="true" aria-labelledby="admin-drawer-title">
                    <!-- HEADER DEL CAJÓN -->
                    <div class="admin-drawer-header">
                        <div>
                            <span class="admin-drawer-kicker">GOBERNANZA DEL PORTFOLIO</span>
                            <h3 class="admin-drawer-title" id="admin-drawer-title">Gestión de Estados y Carriles</h3>
                        </div>
                        <button class="admin-drawer-close" id="btn-admin-close" aria-label="Cerrar">&times;</button>
                    </div>

                    <!-- BARRA DE BÚSQUEDA Y PROTOCOLO -->
                    <div class="admin-drawer-toolbar">
                        <div class="admin-search-wrap">
                            <svg class="admin-search-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                                <circle cx="11" cy="11" r="8"></circle>
                                <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                            </svg>
                            <input type="text" id="admin-search-input" placeholder="Buscar por iniciativa, tag o tecnología..." autocomplete="off">
                            <button id="admin-search-clear" class="admin-search-clear" title="Limpiar búsqueda" style="display: none;">&times;</button>
                        </div>
                        <div class="admin-status-pill" id="admin-persistence-pill" title="Persistencia física directa en archivo projects_data.js">
                            <span class="admin-dot-live"></span>
                            <span id="admin-persistence-text">${this.fileHandle ? 'Auto-guardado activo' : 'Web File System API'}</span>
                            <button type="button" id="btn-admin-change-path" class="admin-link-change-path" title="Cambiar archivo destino en disco">Cambiar...</button>
                        </div>
                    </div>

                    <!-- PESTAÑAS DE FILTRO RÁPIDO DENTRO DEL PANEL -->
                    <div class="admin-filter-tabs">
                        <button class="admin-filter-tab is-active" data-tab="all">
                            <span>Todos</span>
                            <span class="tab-badge" id="admin-tab-count-all">14</span>
                        </button>
                        <button class="admin-filter-tab tab-amber" data-tab="licitacion">
                            ${LDA_ICONS.licitacion.replace('width="18" height="18"', 'width="14" height="14" style="vertical-align: -1px; margin-right: 4px;"')}
                            <span>En Licitación</span>
                            <span class="tab-badge" id="admin-tab-count-lic">1</span>
                        </button>
                        <button class="admin-filter-tab" data-tab="direct">
                            <span>Gestión Directa</span>
                            <span class="tab-badge" id="admin-tab-count-dir">3</span>
                        </button>
                        <button class="admin-filter-tab" data-tab="strategic">
                            <span>Estratégicos</span>
                            <span class="tab-badge" id="admin-tab-count-strat">8</span>
                        </button>
                        <button class="admin-filter-tab" data-tab="others">
                            <span>Otros</span>
                            <span class="tab-badge" id="admin-tab-count-oth">2</span>
                    </div>

                    <!-- CUERPO PRINCIPAL CON TARJETAS ESPACIOSAS -->
                    <div class="admin-drawer-body" id="admin-drawer-body">
                        <!-- Renderizado dinámico de tarjetas -->
                    </div>

                    <!-- PIE CON ACCIONES Y PERSISTENCIA -->
                    <div class="admin-drawer-footer">
                        <div class="admin-footer-left">
                            <button class="admin-btn-secondary" id="btn-admin-download" title="Descargar archivo projects_data.js actualizado">
                                📥 Descargar Copia
                            </button>
                            <button class="admin-btn-secondary" id="btn-admin-reset" title="Restablecer a valores iniciales">
                                ↺ Revertir
                            </button>
                        </div>
                        <div class="admin-footer-right">
                            <button class="admin-btn-primary" id="btn-admin-save" title="Escribir físicamente en projects_data.js en disco">
                                💾 Guardar Cambios en Archivo
                            </button>
                        </div>
                    </div>
                </div>
            `;
            document.body.appendChild(backdrop);

            // Handlers de cierre
            backdrop.querySelector('#btn-admin-close')?.addEventListener('click', () => this.closeDrawer());
            backdrop.addEventListener('click', (e) => {
                if (e.target === backdrop) this.closeDrawer();
            });

            // Handlers de búsqueda
            const searchInput = backdrop.querySelector('#admin-search-input');
            const searchClear = backdrop.querySelector('#admin-search-clear');

            searchInput?.addEventListener('input', (e) => {
                this.searchTerm = e.target.value.toLowerCase().trim();
                if (searchClear) searchClear.style.display = this.searchTerm ? 'block' : 'none';
                this.renderProjectsList();
            });

            searchClear?.addEventListener('click', () => {
                if (searchInput) searchInput.value = '';
                this.searchTerm = '';
                searchClear.style.display = 'none';
                searchInput?.focus();
                this.renderProjectsList();
            });

            // Handlers de pestañas de filtrado rápido
            backdrop.querySelectorAll('.admin-filter-tab').forEach(tab => {
                tab.addEventListener('click', () => {
                    backdrop.querySelectorAll('.admin-filter-tab').forEach(t => t.classList.remove('is-active'));
                    tab.classList.add('is-active');
                    this.activeTab = tab.getAttribute('data-tab');
                    this.renderProjectsList();
                });
            });

            // Handlers de guardado y descarga
            backdrop.querySelector('#btn-admin-save')?.addEventListener('click', () => this.saveViaFileSystemAPI(false));
            backdrop.querySelector('#btn-admin-change-path')?.addEventListener('click', () => this.saveViaFileSystemAPI(true));
            backdrop.querySelector('#btn-admin-download')?.addEventListener('click', () => this.downloadMasterFile());
            backdrop.querySelector('#btn-admin-reset')?.addEventListener('click', () => this.resetToDefaults());

            return backdrop;
        },

        updatePersistencePill: function (isBound) {
            const pillText = document.getElementById('admin-persistence-text');
            const pill = document.getElementById('admin-persistence-pill');
            if (pillText) {
                pillText.innerText = isBound ? 'Auto-guardado activo (projects_data.js)' : 'Web File System API';
            }
            if (pill) {
                pill.title = isBound 
                    ? 'Archivo vinculado en disco. Los cambios se guardan automáticamente sin volver a pedir la ruta.'
                    : 'Persistencia física directa en archivo mediante Chromium Web API.';
            }
        },

        updateDrawerStats: function () {
            const backdrop = document.getElementById('bitacora-admin-backdrop');
            if (!backdrop) return;

            const total = this.projects.length;
            const lic = this.projects.filter(p => p.licitacion === true).length;
            const dir = this.projects.filter(p => p.carril === 'direct').length;
            const strat = this.projects.filter(p => p.carril === 'strategic').length;
            const oth = this.projects.filter(p => ['facilitator', 'services', 'closed'].includes(p.carril)).length;

            const badgeAll = backdrop.querySelector('#admin-tab-count-all');
            if (badgeAll) badgeAll.innerText = total;

            const badgeLic = backdrop.querySelector('#admin-tab-count-lic');
            if (badgeLic) badgeLic.innerText = lic;

            const badgeDir = backdrop.querySelector('#admin-tab-count-dir');
            if (badgeDir) badgeDir.innerText = dir;

            const badgeStrat = backdrop.querySelector('#admin-tab-count-strat');
            if (badgeStrat) badgeStrat.innerText = strat;

            const badgeOth = backdrop.querySelector('#admin-tab-count-oth');
            if (badgeOth) badgeOth.innerText = oth;
        },

        // ==========================================
        // 5. RENDERIZADO VISUAL REDISEÑADO DE PROYECTOS
        // ==========================================
        renderProjectsList: function () {
            const body = document.getElementById('admin-drawer-body');
            if (!body) return;

            this.updateDrawerStats();

            // Filtrado combinado: Pestaña + Buscador
            const filtered = this.projects.filter(p => {
                // Filtro de Pestaña
                if (this.activeTab === 'licitacion' && !p.licitacion) return false;
                if (this.activeTab === 'direct' && p.carril !== 'direct') return false;
                if (this.activeTab === 'strategic' && p.carril !== 'strategic') return false;
                if (this.activeTab === 'others' && !['facilitator', 'services', 'closed'].includes(p.carril)) return false;

                // Filtro de Búsqueda
                if (!this.searchTerm) return true;
                const matchTitle = p.title.toLowerCase().includes(this.searchTerm);
                const matchSub = (p.subtitle || '').toLowerCase().includes(this.searchTerm);
                const matchId = (p.id || '').toLowerCase().includes(this.searchTerm);
                const matchTags = p.tags && p.tags.some(t => t.toLowerCase().includes(this.searchTerm));
                const matchEstado = (p.estado || '').toLowerCase().includes(this.searchTerm);
                const matchReplan = p.replanificado && (this.searchTerm.includes('replan') || this.searchTerm.includes('desv'));
                const matchSemaforo = (p.semaforo || '').toLowerCase().includes(this.searchTerm) || (p.semaforo === 'pausa' && (this.searchTerm.includes('parado') || this.searchTerm.includes('pausa')));
                return matchTitle || matchSub || matchId || matchTags || matchEstado || matchReplan || matchSemaforo;
            });

            if (filtered.length === 0) {
                body.innerHTML = `
                    <div class="admin-empty-state">
                        <div style="font-size: 2.2rem; margin-bottom: 10px;">🔍</div>
                        <h4 style="color: var(--text-main); font-weight: 700; margin: 0 0 6px 0;">No se encontraron iniciativas</h4>
                        <p style="font-size: 0.85rem; color: var(--text-sec); margin: 0;">Prueba a seleccionar otra pestaña o limpia el término de búsqueda.</p>
                    </div>
                `;
                return;
            }

            body.innerHTML = filtered.map(p => {
                const acronym = this.getAcronym(p);
                const isLicitacion = p.licitacion === true;
                const semaforo = p.semaforo || 'verde';

                const isReplan = p.replanificado === true;

                return `
                    <div class="admin-card lane-card-${p.carril} ${semaforo === 'pausa' || p.estado === 'En Pausa / Parado' ? 'is-paused-card' : ''}" data-id="${p.id}">
                        <!-- CABECERA DE IDENTIDAD -->
                        <div class="admin-card-header">
                            <div class="admin-card-identity">
                                <span class="admin-card-badge">${acronym}</span>
                                <div>
                                    <h4 class="admin-card-title">${p.title}</h4>
                                    <span class="admin-card-subtitle">${p.subtitle || p.desc || ''}</span>
                                </div>
                            </div>
                            <span class="admin-lane-pill lane-${p.carril}">
                                ${this.getCarrilName(p.carril)}
                            </span>
                        </div>

                        <!-- FILA DE TOGGLES OPERATIVOS: LICITACIÓN Y REPLANIFICACIÓN -->
                        <div class="admin-toggles-row">
                            <!-- Toggle 1: Concurso de Licitación -->
                            <div class="admin-licitacion-box ${isLicitacion ? 'is-active' : ''}" data-id="${p.id}">
                                <div class="admin-licitacion-left">
                                    <span class="admin-licitacion-icon">${LDA_ICONS.licitacion}</span>
                                    <div>
                                        <div class="admin-licitacion-status-text">
                                            ${isLicitacion ? 'En Licitación' : 'Sin Licitación'}
                                        </div>
                                        <div class="admin-licitacion-subtext">
                                            ${isLicitacion ? 'Concurso activo' : 'Contratación ordinaria'}
                                        </div>
                                    </div>
                                </div>
                                <label class="admin-switch" title="Activar/Desactivar Licitación">
                                    <input type="checkbox" class="admin-toggle-licitacion" data-id="${p.id}" ${isLicitacion ? 'checked' : ''}>
                                    <span class="admin-switch-slider"></span>
                                </label>
                            </div>

                            <!-- Toggle 2: Replanificación de Calendario -->
                            <div class="admin-replan-box ${isReplan ? 'is-active' : ''}" data-id="${p.id}">
                                <div class="admin-licitacion-left">
                                    <span class="admin-licitacion-icon">${LDA_ICONS.replan}</span>
                                    <div>
                                        <div class="admin-replan-status-text">
                                            ${isReplan ? 'Con Replanificación' : 'Plan Inicial'}
                                        </div>
                                        <div class="admin-licitacion-subtext">
                                            ${isReplan ? 'Desvío de cronograma' : 'Sin desvíos de fecha'}
                                        </div>
                                    </div>
                                </div>
                                <label class="admin-switch" title="Marcar si ha tenido replanificación del plan inicial">
                                    <input type="checkbox" class="admin-toggle-replan" data-id="${p.id}" ${isReplan ? 'checked' : ''}>
                                    <span class="admin-switch-slider"></span>
                                </label>
                            </div>
                        </div>

                        <!-- CONTROLES DE CARRIL Y FASE -->
                        <div class="admin-fields-grid">
                            <!-- Carril Organizativo -->
                            <div class="admin-field-group">
                                <label class="admin-field-label">Carril en el Portfolio</label>
                                <select class="admin-field-select admin-select-carril" data-id="${p.id}">
                                    <option value="direct" ${p.carril === 'direct' ? 'selected' : ''}>Gestión Directa (PO / PM)</option>
                                    <option value="strategic" ${p.carril === 'strategic' ? 'selected' : ''}>Estratégicos (8 Grandes)</option>
                                    <option value="facilitator" ${p.carril === 'facilitator' ? 'selected' : ''}>Facilitadores / Afectados</option>
                                    <option value="services" ${p.carril === 'services' ? 'selected' : ''}>Servicios y Operativas</option>
                                    <option value="closed" ${p.carril === 'closed' ? 'selected' : ''}>Histórico / Cerrados</option>
                                </select>
                            </div>

                            <!-- Fase de Ciclo de Vida (Limpia y Formal) -->
                            <div class="admin-field-group">
                                <label class="admin-field-label">Fase de Proyecto</label>
                                <select class="admin-field-select admin-select-fase" data-id="${p.id}">
                                    <option value="En Decisión" ${p.estado === 'En Decisión' ? 'selected' : ''}>En Decisión / Valoración</option>
                                    <option value="En Licitación" ${p.estado === 'En Licitación' ? 'selected' : ''}>En Licitación / Pliegos</option>
                                    <option value="En Planificación" ${p.estado === 'En Planificación' ? 'selected' : ''}>En Planificación</option>
                                    <option value="En Curso" ${p.estado === 'En Curso' || p.estado === 'En Desarrollo' ? 'selected' : ''}>En Curso</option>
                                    <option value="En Despliegue" ${p.estado === 'En Despliegue' ? 'selected' : ''}>En Despliegue / Piloto</option>
                                    <option value="En Producción" ${p.estado === 'En Producción' ? 'selected' : ''}>En Producción</option>
                                    <option value="En Pausa / Parado" ${p.estado === 'En Pausa / Parado' || p.estado === 'Parado' ? 'selected' : ''}>En Pausa / Parado</option>
                                    <option value="Cerrado / Histórico" ${p.estado === 'Cerrado / Histórico' ? 'selected' : ''}>Cerrado / Histórico</option>
                                </select>
                            </div>
                        </div>

                        <!-- SEMÁFORO DE SALUD OPERATIVA (4 BOTONES VISUALES DIRECTOS) -->
                        <div class="admin-semaforo-section">
                            <label class="admin-field-label">Semáforo de Salud Operativa</label>
                            <div class="admin-semaforo-segmented" data-id="${p.id}">
                                <button type="button" class="admin-semaforo-pill pill-verde ${semaforo === 'verde' ? 'is-active' : ''}" data-val="verde" data-id="${p.id}">
                                    <span class="semaforo-dot dot-verde"></span>
                                    <span>Saludable</span>
                                </button>
                                <button type="button" class="admin-semaforo-pill pill-ambar ${semaforo === 'ambar' ? 'is-active' : ''}" data-val="ambar" data-id="${p.id}">
                                    <span class="semaforo-dot dot-ambar"></span>
                                    <span>En Riesgo</span>
                                </button>
                                <button type="button" class="admin-semaforo-pill pill-rojo ${semaforo === 'rojo' ? 'is-active' : ''}" data-val="rojo" data-id="${p.id}">
                                    <span class="semaforo-dot dot-rojo"></span>
                                    <span>Crítico</span>
                                </button>
                                <button type="button" class="admin-semaforo-pill pill-pausa ${semaforo === 'pausa' || semaforo === 'parado' ? 'is-active' : ''}" data-val="pausa" data-id="${p.id}">
                                    <span class="semaforo-dot dot-pausa">${LDA_ICONS.pausa}</span>
                                    <span>Parado</span>
                                </button>
                            </div>
                        </div>
                    </div>
                `;
            }).join('');

            // BINDINGS DE EVENTOS REACTIVOS
            // 1. Toggle de Licitación
            body.querySelectorAll('.admin-toggle-licitacion').forEach(chk => {
                chk.addEventListener('change', (e) => {
                    const id = e.target.getAttribute('data-id');
                    this.setProjectLicitacion(id, e.target.checked);
                });
            });

            // Clic en la caja completa de licitación para mayor ergonomía
            body.querySelectorAll('.admin-licitacion-box').forEach(box => {
                box.addEventListener('click', (e) => {
                    if (e.target.closest('.admin-switch')) return; // dejar que el switch gestione
                    const chk = box.querySelector('.admin-toggle-licitacion');
                    if (chk) {
                        chk.checked = !chk.checked;
                        const id = box.getAttribute('data-id');
                        this.setProjectLicitacion(id, chk.checked);
                    }
                });
            });

            // Toggle de Replanificación
            body.querySelectorAll('.admin-toggle-replan').forEach(chk => {
                chk.addEventListener('change', (e) => {
                    const id = e.target.getAttribute('data-id');
                    this.setProjectReplan(id, e.target.checked);
                });
            });

            // Clic en la caja completa de replanificación
            body.querySelectorAll('.admin-replan-box').forEach(box => {
                box.addEventListener('click', (e) => {
                    if (e.target.closest('.admin-switch')) return;
                    const chk = box.querySelector('.admin-toggle-replan');
                    if (chk) {
                        chk.checked = !chk.checked;
                        const id = box.getAttribute('data-id');
                        this.setProjectReplan(id, chk.checked);
                    }
                });
            });

            // 2. Select de Carril
            body.querySelectorAll('.admin-select-carril').forEach(sel => {
                sel.addEventListener('change', (e) => {
                    const id = e.target.getAttribute('data-id');
                    const proj = this.projects.find(x => x.id === id);
                    if (proj) {
                        proj.carril = e.target.value;
                        this.applyStateToUI();
                        // Actualizar la píldora de carril en la tarjeta actual
                        const card = body.querySelector(`.admin-card[data-id="${id}"]`);
                        if (card) {
                            const pill = card.querySelector('.admin-lane-pill');
                            if (pill) {
                                pill.className = `admin-lane-pill lane-${proj.carril}`;
                                pill.innerText = this.getCarrilName(proj.carril);
                            }
                        }
                    }
                });
            });

            // 3. Select de Fase
            body.querySelectorAll('.admin-select-fase').forEach(sel => {
                sel.addEventListener('change', (e) => {
                    const id = e.target.getAttribute('data-id');
                    const proj = this.projects.find(x => x.id === id);
                    if (proj) {
                        proj.estado = e.target.value;
                        if (proj.estado === 'En Licitación' && !proj.licitacion) {
                            this.setProjectLicitacion(id, true);
                        } else {
                            this.applyStateToUI();
                        }
                    }
                });
            });

            // 4. Semáforo Segmented Pills
            body.querySelectorAll('.admin-semaforo-pill').forEach(btn => {
                btn.addEventListener('click', (e) => {
                    const id = btn.getAttribute('data-id');
                    const val = btn.getAttribute('data-val');
                    const proj = this.projects.find(x => x.id === id);
                    if (proj) {
                        proj.semaforo = val;
                        // Actualizar botones de este grupo
                        const group = btn.closest('.admin-semaforo-segmented');
                        if (group) {
                            group.querySelectorAll('.admin-semaforo-pill').forEach(b => b.classList.remove('is-active'));
                            btn.classList.add('is-active');
                        }
                        // Sincronizar estilo pausado en la tarjeta de administración
                        const cardAdmin = body.querySelector(`.admin-card[data-id="${id}"]`);
                        if (cardAdmin) {
                            cardAdmin.classList.toggle('is-paused-card', val === 'pausa' || proj.estado === 'En Pausa / Parado');
                        }
                        this.applyStateToUI();
                    }
                });
            });
        },

        setProjectLicitacion: function (id, isActive) {
            const proj = this.projects.find(x => x.id === id);
            if (!proj) return;

            proj.licitacion = isActive;
            if (proj.licitacion && proj.estado !== 'En Licitación') {
                proj.estado = 'En Licitación';
            }

            // Actualizar la caja visual
            const card = document.querySelector(`.admin-card[data-id="${id}"]`);
            if (card) {
                const box = card.querySelector('.admin-licitacion-box');
                if (box) {
                    box.classList.toggle('is-active', isActive);
                    const statusText = box.querySelector('.admin-licitacion-status-text');
                    if (statusText) {
                        statusText.innerText = isActive 
                            ? 'En Licitación' 
                            : 'Sin Licitación';
                    }
                    const subText = box.querySelector('.admin-licitacion-subtext');
                    if (subText) {
                        subText.innerText = isActive
                            ? 'Concurso activo'
                            : 'Contratación ordinaria';
                    }
                    const chk = box.querySelector('.admin-toggle-licitacion');
                    if (chk) chk.checked = isActive;
                }
                const selectFase = card.querySelector(`.admin-select-fase[data-id="${id}"]`);
                if (selectFase && isActive) selectFase.value = 'En Licitación';
            }

            this.applyStateToUI();
        },

        setProjectReplan: function (id, isReplan) {
            const proj = this.projects.find(x => x.id === id);
            if (!proj) return;

            proj.replanificado = isReplan;

            // Actualizar la caja visual en el panel
            const card = document.querySelector(`.admin-card[data-id="${id}"]`);
            if (card) {
                const box = card.querySelector('.admin-replan-box');
                if (box) {
                    box.classList.toggle('is-active', isReplan);
                    const statusText = box.querySelector('.admin-replan-status-text');
                    if (statusText) {
                        statusText.innerText = isReplan ? 'Con Replanificación' : 'Plan Inicial';
                    }
                    const subText = box.querySelector('.admin-licitacion-subtext');
                    if (subText) {
                        subText.innerText = isReplan ? 'Desvío de cronograma' : 'Sin desvíos de fecha';
                    }
                    const chk = box.querySelector('.admin-toggle-replan');
                    if (chk) chk.checked = isReplan;
                }
            }

            this.applyStateToUI();
        },

        openDrawer: function (targetTab = null) {
            const drawer = this.buildDrawer();
            if (targetTab) {
                this.activeTab = targetTab;
                drawer.querySelectorAll('.admin-filter-tab').forEach(t => {
                    t.classList.toggle('is-active', t.getAttribute('data-tab') === targetTab);
                });
            }
            this.renderProjectsList();
            this.updatePersistencePill(!!this.fileHandle);
            drawer.classList.add('is-open');
            document.body.style.overflow = 'hidden';
            this.isOpen = true;
        },

        closeDrawer: function () {
            const drawer = document.getElementById('bitacora-admin-backdrop');
            if (drawer) {
                drawer.classList.remove('is-open');
                document.body.style.overflow = '';
            }
            this.isOpen = false;
        },

        toggleDrawer: function () {
            if (this.isOpen) this.closeDrawer();
            else this.openDrawer();
        },

        // ==========================================
        // 6. PERSISTENCIA UNIVERSAL MEDIANTE FILE SYSTEM API Y AUTO-GUARDADO
        // ==========================================
        generateFileContent: function () {
            return `/**\n * CATÁLOGO MAESTRO DE PROYECTOS - LÍNEA DIRECTA ASEGURADORA\n * Base de datos central de estado, gobernanza y carriles del Portfolio.\n * Modificable interactivamente desde el Centro de Gestión del Portfolio mediante Web File System API.\n * Fecha de sincronización: ${new Date().toISOString().split('T')[0]}\n */\nwindow.BITACORA_PROJECTS_DATA = ${JSON.stringify(this.projects, null, 4)};\n`;
        },

        saveViaFileSystemAPI: async function (forceNew = false) {
            const saveBtn = document.getElementById('btn-admin-save');
            if (saveBtn) {
                saveBtn.disabled = true;
                saveBtn.innerText = 'Guardando...';
            }

            try {
                if ('showOpenFilePicker' in window || 'showSaveFilePicker' in window) {
                    // Si no tenemos handle en memoria y no forzamos nuevo, buscar en IndexedDB
                    if (!this.fileHandle && !forceNew) {
                        this.fileHandle = await getStoredHandle();
                    }

                    // Si todavía no hay handle o se forzó selección de nueva ubicación
                    if (!this.fileHandle || forceNew) {
                        if ('showOpenFilePicker' in window) {
                            const [handle] = await window.showOpenFilePicker({
                                types: [{
                                    description: 'Archivo projects_data.js de Bitácora',
                                    accept: { 'text/javascript': ['.js'] }
                                }],
                                multiple: false
                            });
                            this.fileHandle = handle;
                        } else {
                            this.fileHandle = await window.showSaveFilePicker({
                                suggestedName: 'projects_data.js',
                                types: [{
                                    description: 'Archivo JavaScript',
                                    accept: { 'text/javascript': ['.js'] }
                                }]
                            });
                        }

                        // Guardar en IndexedDB para no volver a pedir la ruta en las próximas sesiones
                        if (this.fileHandle) {
                            await storeHandle(this.fileHandle);
                            this.updatePersistencePill(true);
                        }
                    }

                    // Verificar permisos de escritura en el handle existente
                    let hasPermission = false;
                    try {
                        const q = await this.fileHandle.queryPermission({ mode: 'readwrite' });
                        if (q === 'granted') {
                            hasPermission = true;
                        } else {
                            const req = await this.fileHandle.requestPermission({ mode: 'readwrite' });
                            hasPermission = (req === 'granted');
                        }
                    } catch (_) {
                        hasPermission = true;
                    }

                    if (!hasPermission) {
                        throw new Error('Permiso de escritura no concedido');
                    }

                    // Escribir silenciosamente en el archivo predeterminado
                    const writable = await this.fileHandle.createWritable();
                    await writable.write(this.generateFileContent());
                    await writable.close();

                    this.updatePersistencePill(true);
                    this.showToast('✓ Guardado automáticamente en projects_data.js');
                } else {
                    this.downloadMasterFile();
                    this.showToast('ℹ Archivo generado. Descarga de copia lista.');
                }
            } catch (err) {
                if (err.name !== 'AbortError') {
                    console.warn('Error con File System API:', err);
                    if (this.fileHandle && !forceNew) {
                        this.fileHandle = null;
                        await clearStoredHandle();
                        this.updatePersistencePill(false);
                    }
                    this.downloadMasterFile();
                    this.showToast('ℹ Guardado mediante descarga de respaldo.');
                }
            } finally {
                if (saveBtn) {
                    saveBtn.disabled = false;
                    saveBtn.innerText = '💾 Guardar Cambios en Archivo';
                }
            }
        },

        downloadMasterFile: function () {
            const content = this.generateFileContent();
            const blob = new Blob([content], { type: 'text/javascript;charset=utf-8' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'projects_data.js';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
            this.showToast('✓ Descarga de projects_data.js generada');
        },

        resetToDefaults: function () {
            if (window.BITACORA_PROJECTS_DATA) {
                this.projects = JSON.parse(JSON.stringify(window.BITACORA_PROJECTS_DATA));
                this.applyStateToUI();
                this.renderProjectsList();
                this.showToast('↺ Valores restaurados al catálogo base');
            }
        },

        showToast: function (msg) {
            let toast = document.getElementById('bitacora-admin-toast');
            if (!toast) {
                toast = document.createElement('div');
                toast.id = 'bitacora-admin-toast';
                toast.className = 'bitacora-admin-toast';
                document.body.appendChild(toast);
            }
            toast.innerText = msg;
            toast.classList.add('is-visible');
            setTimeout(() => toast.classList.remove('is-visible'), 3200);
        }
    };

    window.BitacoraAdmin = BitacoraAdmin;

    // Inicializar al cargar el DOM
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => BitacoraAdmin.init());
    } else {
        BitacoraAdmin.init();
    }
})();
