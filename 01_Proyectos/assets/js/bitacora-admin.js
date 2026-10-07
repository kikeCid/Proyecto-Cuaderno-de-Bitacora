/**
 * MÓDULO DE ADMINISTRACIÓN REACTIVA DEL CUADERNO DE BITÁCORA
 * Línea Directa Aseguradora - Centro de Control
 * Persistencia en disco mediante Web File System Access API nativa e IndexedDB.
 * Gobernanza bifurcada:
 * - 📁 Proyectos e Iniciativas (fases, hitos, licitaciones y semáforos de salud operativa)
 * - 📋 Procedimientos y Operativas (estados documentales, versiones, revisiones y criticidad)
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
        settings: `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lda-svg-icon" style="color: var(--lda-red); vertical-align: -2px; margin-right: 5px;"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>`,
        docCheck: `<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="color: #059669; vertical-align: -1px; margin-right: 3px;"><polyline points="20 6 9 17 4 12"></polyline></svg>`,
        docClock: `<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="color: #d97706; vertical-align: -1px; margin-right: 3px;"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>`,
        folderProjects: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg>`,
        fileManuals: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>`
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
        operativas: [],
        fileHandle: null,
        isOpen: false,
        macroMode: 'projects', // 'projects' | 'operativas'
        activeTab: 'all',
        searchTerm: '',

        init: async function () {
            // Cargar catálogo de Proyectos
            if (window.BITACORA_PROJECTS_DATA && Array.isArray(window.BITACORA_PROJECTS_DATA)) {
                this.projects = JSON.parse(JSON.stringify(window.BITACORA_PROJECTS_DATA));
            } else if (window.BITACORA_CATALOG && Array.isArray(window.BITACORA_CATALOG.projects)) {
                this.projects = JSON.parse(JSON.stringify(window.BITACORA_CATALOG.projects));
            } else {
                this.projects = [];
            }

            // Cargar catálogo de Operativas / Manuales
            if (window.BITACORA_OPERATIVAS_DATA && Array.isArray(window.BITACORA_OPERATIVAS_DATA)) {
                this.operativas = JSON.parse(JSON.stringify(window.BITACORA_OPERATIVAS_DATA));
            } else if (window.BITACORA_CATALOG && Array.isArray(window.BITACORA_CATALOG.operativas)) {
                this.operativas = JSON.parse(JSON.stringify(window.BITACORA_CATALOG.operativas));
            } else {
                this.operativas = [];
            }

            // Recuperar handle físico guardado previamente de IndexedDB
            try {
                this.fileHandle = await getStoredHandle();
            } catch (_) {}

            // Aplicar reactividad al arrancar
            this.applyStateToUI();
            this.injectAdminTrigger();
        },

        // ==========================================
        // 1. INYECCIÓN DEL BOTÓN EN CABECERA Y ACCIONES RÁPIDAS
        // ==========================================
        injectAdminTrigger: function () {
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

            // Enlace contextual en el Modal de Licitaciones
            const modalFooter = document.querySelector('.licitaciones-modal-footer');
            if (modalFooter && !document.getElementById('link-admin-licitaciones')) {
                const adminLink = document.createElement('button');
                adminLink.id = 'link-admin-licitaciones';
                adminLink.className = 'licitaciones-admin-action-btn';
                adminLink.innerHTML = `${LDA_ICONS.settings}<span>Modificar qué proyectos están en Licitación</span>`;
                adminLink.onclick = () => {
                    if (typeof closeLicitacionesModal === 'function') closeLicitacionesModal();
                    BitacoraAdmin.openDrawer('licitacion', 'projects');
                };
                modalFooter.insertBefore(adminLink, modalFooter.firstChild);
            }

            // En la barra flotante de acciones rápidas (inferior derecha)
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
                        <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path>
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
            // A) RECALCULAR KPIS DE PROYECTOS
            const totalProj = this.projects.length;
            const strategics = this.projects.filter(p => p.carril === 'strategic').length;
            const directs = this.projects.filter(p => p.carril === 'direct').length;
            const licitaciones = this.projects.filter(p => p.licitacion === true).length;
            const facilitators = this.projects.filter(p => p.carril === 'facilitator').length;

            const kpiCards = document.querySelectorAll('.executive-stats-strip-projects .kpi-clean-card');
            if (kpiCards.length >= 4) {
                const valTotal = kpiCards[0].querySelector('.kpi-clean-value');
                if (valTotal) { valTotal.innerText = totalProj; valTotal.setAttribute('data-count', totalProj); }

                const valStrat = kpiCards[1].querySelector('.kpi-clean-value');
                if (valStrat) { valStrat.innerText = strategics; valStrat.setAttribute('data-count', strategics); }

                const valDir = kpiCards[2].querySelector('.kpi-clean-value');
                if (valDir) { valDir.innerText = directs; valDir.setAttribute('data-count', directs); }

                const valLic = kpiCards[3].querySelector('.kpi-clean-value');
                if (valLic) { valLic.innerText = licitaciones; valLic.setAttribute('data-count', licitaciones); }
            }

            // B) RECALCULAR KPIS DE OPERATIVAS / MANUALES
            const totalOp = this.operativas.length;
            const opVigentes = this.operativas.filter(o => o.estadoDoc === 'Vigente').length;
            const opRevision = this.operativas.filter(o => o.estadoDoc === 'En Revisión').length;
            const opCriticas = this.operativas.filter(o => o.criticidad === 'Crítica').length;

            const kpiCardsOp = document.querySelectorAll('.executive-stats-strip-operativas .kpi-clean-card');
            if (kpiCardsOp.length >= 4) {
                const valTotalOp = kpiCardsOp[0].querySelector('.kpi-clean-value');
                if (valTotalOp) { valTotalOp.innerText = totalOp; valTotalOp.setAttribute('data-count', totalOp); }

                const valVig = kpiCardsOp[1].querySelector('.kpi-clean-value');
                if (valVig) { valVig.innerText = opVigentes; valVig.setAttribute('data-count', opVigentes); }

                const valRev = kpiCardsOp[2].querySelector('.kpi-clean-value');
                if (valRev) { valRev.innerText = opRevision; valRev.setAttribute('data-count', opRevision); }

                const valCrit = kpiCardsOp[3].querySelector('.kpi-clean-value');
                if (valCrit) { valCrit.innerText = opCriticas; valCrit.setAttribute('data-count', opCriticas); }
            }

            // Actualizar filtros de carril de proyectos
            const closedProjects = this.projects.filter(p => p.carril === 'closed').length;
            const filterChipsProj = document.querySelectorAll('.filter-segments-projects .filter-chip');
            if (filterChipsProj.length >= 4) {
                const counts = [totalProj, directs, strategics, facilitators, closedProjects];
                filterChipsProj.forEach((chip, i) => {
                    const countEl = chip.querySelector('.filter-count');
                    if (countEl && counts[i] !== undefined) countEl.innerText = counts[i];
                });
            }

            // Actualizar contadores de cabeceras de sección
            const mapSecCount = {
                'seccion-directa': directs,
                'seccion-estrategicos': strategics,
                'seccion-facilitadores': facilitators,
                'seccion-cerrados': closedProjects
            };
            Object.keys(mapSecCount).forEach(secId => {
                const sec = document.getElementById(secId);
                if (sec) {
                    const counter = sec.querySelector('.section-counter');
                    if (counter) counter.innerText = mapSecCount[secId];
                }
            });

            // C) ACTUALIZAR TARJETAS EN LOS CARRUSELES DE PROYECTOS
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

                    const tagsContainer = card.querySelector('.card-tags');
                    if (tagsContainer) {
                        // Tag de Licitación
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

                        // Tag de Fase Especial (Parado / Decisión)
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

                        // Tag de Replanificación
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
                        'closed': 'seccion-cerrados'
                    }[p.carril] || 'seccion-estrategicos';

                    const targetTrack = document.querySelector(`#${targetSecId} .carousel-track`);
                    const currentTrack = card.closest('.carousel-track');
                    if (targetTrack && currentTrack && targetTrack !== currentTrack) {
                        targetTrack.appendChild(card);
                    }
                }
            });

            // D) ACTUALIZAR TARJETAS EN EL CATÁLOGO DE OPERATIVAS / MANUALES
            const trackOperativas = document.getElementById('track-operativas-sistemas');
            this.operativas.forEach(op => {
                const card = document.getElementById(`card-op-${op.id}`) ||
                             document.querySelector(`.apple-card[id*="${op.id}"]`) ||
                             document.querySelector(`.apple-card[href*="${op.id}"]`);
                if (card) {
                    // Si estaba en proyectos, moverla al carril de operativas
                    if (trackOperativas && card.closest('#container-bitacora-proyectos')) {
                        trackOperativas.appendChild(card);
                    }

                    // Actualizar badge de estado documental
                    const badgeEstado = card.querySelector('.badge-doc-estado, .badge-doc-vigente, .badge-doc-revision, .badge-doc-obsoleto');
                    if (badgeEstado) {
                        badgeEstado.className = `doc-badge badge-doc-estado ${
                            op.estadoDoc === 'Vigente' ? 'badge-doc-vigente' :
                            op.estadoDoc === 'En Revisión' ? 'badge-doc-revision' :
                            'badge-doc-obsoleto'
                        }`;
                        badgeEstado.innerHTML = op.estadoDoc === 'Vigente'
                            ? `${LDA_ICONS.docCheck}<span>Vigente</span>`
                            : op.estadoDoc === 'En Revisión'
                            ? `${LDA_ICONS.docClock}<span>En Revisión</span>`
                            : `<span>${op.estadoDoc}</span>`;
                    }

                    // Actualizar versión
                    const badgeVer = card.querySelector('.badge-doc-version');
                    if (badgeVer) badgeVer.innerText = op.version || 'v1.0';

                    // Actualizar fecha última revisión
                    const dateRev = card.querySelector('.doc-meta-date');
                    if (dateRev) dateRev.innerText = op.ultimaRevision || 'Revisión al día';
                }
            });

            // Actualizar contador en la sección de operativas
            const secOp = document.getElementById('seccion-operativas-sistemas');
            if (secOp) {
                const counterOp = secOp.querySelector('.section-counter');
                if (counterOp) counterOp.innerText = this.operativas.length;
            }

            // Actualizar Modal de Licitaciones y estadísticas del cajón
            this.renderLicitacionesModalContent();
            this.updateDrawerStats();
        },

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
                'closed': 'Histórico / Cerrado'
            };
            return map[carril] || 'Proyecto';
        },

        getAcronym: function (item) {
            if (item.id) {
                const parts = item.id.split('-');
                if (parts.length > 1) {
                    return (parts[0].substring(0, 2) + parts[1].substring(0, 2)).toUpperCase();
                }
                return item.id.substring(0, 4).toUpperCase();
            }
            return 'DOC';
        },

        // ==========================================
        // 3. CONSTRUCCIÓN DEL CAJÓN DE ADMINISTRACIÓN
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
                            <span class="admin-drawer-kicker">CENTRO DE CONTROL & GOBERNANZA</span>
                            <h3 class="admin-drawer-title" id="admin-drawer-title">Gestión de Estados del Ecosistema</h3>
                        </div>
                        <button class="admin-drawer-close" id="btn-admin-close" aria-label="Cerrar">&times;</button>
                    </div>

                    <!-- MACRO TABS: PROYECTOS VS OPERATIVAS -->
                    <div class="admin-macro-tabs">
                        <button class="admin-macro-tab is-active" id="btn-macro-drawer-projects" data-macro="projects">
                            ${LDA_ICONS.folderProjects}
                            <span>Proyectos e Iniciativas</span>
                            <span class="admin-doc-badge-pill" id="admin-macro-count-projects">${this.projects.length}</span>
                        </button>
                        <button class="admin-macro-tab" id="btn-macro-drawer-operativas" data-macro="operativas">
                            ${LDA_ICONS.fileManuals}
                            <span>Procedimientos y Manuales</span>
                            <span class="admin-doc-badge-pill" id="admin-macro-count-operativas">${this.operativas.length}</span>
                        </button>
                    </div>

                    <!-- BARRA DE BÚSQUEDA Y ESTADO DE ESCRITURA EN DISCO -->
                    <div class="admin-drawer-toolbar">
                        <div class="admin-search-wrap">
                            <svg class="admin-search-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                                <circle cx="11" cy="11" r="8"></circle>
                                <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                            </svg>
                            <input type="text" id="admin-search-input" placeholder="Buscar iniciativas, procedimientos o tags..." autocomplete="off">
                            <button id="admin-search-clear" class="admin-search-clear" title="Limpiar búsqueda" style="display: none;">&times;</button>
                        </div>

                        <!-- BOTÓN REACTIVO DE AUTORIZACIÓN / ESTADO -->
                        <button type="button" class="admin-auth-btn" id="btn-admin-auth" title="Autorizar o reactivar permisos de escritura directa en projects_data.js">
                            <span class="auth-dot" id="admin-auth-dot"></span>
                            <span id="admin-auth-text">Autorizar Escritura Directa</span>
                        </button>

                        <button type="button" class="admin-path-help-btn" id="btn-admin-path-help" title="Ver ruta exacta de projects_data.js y guía de guardado">
                            📁 ¿Dónde se guarda?
                        </button>
                    </div>

                    <!-- PESTAÑAS DE FILTRO RÁPIDO DENTRO DEL PANEL -->
                    <div class="admin-filter-tabs" id="admin-filter-tabs-container">
                        <!-- Se renderizan dinámicamente según macroMode -->
                    </div>

                    <!-- CUERPO PRINCIPAL CON TARJETAS ESPACIOSAS -->
                    <div class="admin-drawer-body" id="admin-drawer-body">
                        <!-- Renderizado dinámico de tarjetas -->
                    </div>

                    <!-- PIE CON ACCIONES Y PERSISTENCIA -->
                    <div class="admin-drawer-footer">
                        <div class="admin-footer-left">
                            <button class="admin-btn-secondary" id="btn-admin-download" title="Descargar archivo projects_data.js actualizado">
                                📥 Descargar projects_data.js
                            </button>
                            <button class="admin-btn-secondary" id="btn-admin-reset" title="Restablecer a valores iniciales">
                                ↺ Revertir
                            </button>
                        </div>
                        <div class="admin-footer-right">
                            <button class="admin-btn-primary" id="btn-admin-save" title="Escribir directamente en disco en projects_data.js">
                                💾 Guardar Cambios en Archivo
                            </button>
                        </div>
                    </div>
                </div>

                <!-- MODAL POPUP ASISTIDO: DÓNDE SE GUARDA Y DESCARGA DIRECTA -->
                <div class="admin-path-modal-backdrop" id="modal-admin-path-help" onclick="if(event.target===this) BitacoraAdmin.closePathHelpModal()">
                    <div class="admin-path-modal-dialog">
                        <div class="admin-path-modal-header">
                            <div>
                                <span class="admin-drawer-kicker">PERSISTENCIA & GOBERNANZA TÉCNICA</span>
                                <h3 style="margin: 0; font-size: 1.15rem; color: var(--text-main); font-weight: 800;">Destino de Guardado: projects_data.js</h3>
                            </div>
                            <button class="admin-drawer-close" onclick="BitacoraAdmin.closePathHelpModal()" aria-label="Cerrar">&times;</button>
                        </div>
                        <div class="admin-path-modal-body">
                            <div class="path-info-box">
                                <span class="path-info-box-label">Nombre exacto del archivo:</span>
                                <div class="path-code-line">
                                    <strong style="color: var(--lda-red); font-size: 0.95rem;">projects_data.js</strong>
                                    <span style="font-size: 0.72rem; color: var(--text-sec); font-family: sans-serif;">(Catálogo unificado de Proyectos y Operativas)</span>
                                </div>
                            </div>

                            <div class="path-info-box">
                                <span class="path-info-box-label">Ruta en este equipo (Directorio físico a sobrescribir):</span>
                                <div class="path-code-line">
                                    <span id="text-full-path">C:\\Proyectos_Claude\\Proyecto Cuaderno de Bitacora\\01_Proyectos\\assets\\js\\projects_data.js</span>
                                    <button type="button" class="path-copy-btn" id="btn-copy-full-path">Copiar Ruta</button>
                                </div>
                            </div>

                            <div class="path-info-box">
                                <span class="path-info-box-label">Ruta relativa dentro del repositorio:</span>
                                <div class="path-code-line">
                                    <span>01_Proyectos/assets/js/projects_data.js</span>
                                </div>
                            </div>

                            <div style="font-size: 0.84rem; color: var(--text-sec); line-height: 1.55; margin-top: 4px;">
                                <p style="margin: 0 0 6px 0;"><strong style="color: var(--text-main);">¿Cómo asegurar el guardado automático sin cuadro de diálogo?</strong></p>
                                <p style="margin: 0;">Haz clic en <strong>"Autorizar Escritura Directa"</strong> y selecciona tu archivo <code>projects_data.js</code> una sola vez. Tu navegador Edge/Chrome guardará el permiso para que todas las modificaciones se guarden en disco al instante.</p>
                            </div>
                        </div>
                        <div class="admin-path-modal-footer">
                            <button class="admin-btn-secondary" onclick="BitacoraAdmin.downloadMasterFile()">
                                📥 Descargar Archivo para Reemplazar
                            </button>
                            <button class="admin-btn-primary" onclick="BitacoraAdmin.authorizeOrReactivateAccess(true)">
                                🔑 Autorizar / Vincular en Disco
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

            // Handlers de Macro-Tabs (Proyectos vs Operativas)
            backdrop.querySelectorAll('.admin-macro-tab').forEach(tab => {
                tab.addEventListener('click', () => {
                    backdrop.querySelectorAll('.admin-macro-tab').forEach(t => t.classList.remove('is-active'));
                    tab.classList.add('is-active');
                    this.macroMode = tab.getAttribute('data-macro');
                    this.activeTab = 'all';
                    this.searchTerm = '';
                    const searchInput = backdrop.querySelector('#admin-search-input');
                    if (searchInput) searchInput.value = '';
                    this.renderFilterTabs();
                    this.renderList();
                });
            });

            // Handlers de búsqueda
            const searchInput = backdrop.querySelector('#admin-search-input');
            const searchClear = backdrop.querySelector('#admin-search-clear');

            searchInput?.addEventListener('input', (e) => {
                this.searchTerm = e.target.value.toLowerCase().trim();
                if (searchClear) searchClear.style.display = this.searchTerm ? 'block' : 'none';
                this.renderList();
            });

            searchClear?.addEventListener('click', () => {
                if (searchInput) searchInput.value = '';
                this.searchTerm = '';
                searchClear.style.display = 'none';
                searchInput?.focus();
                this.renderList();
            });

            // Handlers de persistencia y autorización
            backdrop.querySelector('#btn-admin-auth')?.addEventListener('click', () => this.authorizeOrReactivateAccess(false));
            backdrop.querySelector('#btn-admin-path-help')?.addEventListener('click', () => this.openPathHelpModal());
            backdrop.querySelector('#btn-admin-save')?.addEventListener('click', () => this.saveViaFileSystemAPI(false));
            backdrop.querySelector('#btn-admin-download')?.addEventListener('click', () => this.downloadMasterFile());
            backdrop.querySelector('#btn-admin-reset')?.addEventListener('click', () => this.resetToDefaults());

            backdrop.querySelector('#btn-copy-full-path')?.addEventListener('click', () => {
                const pathText = 'C:\\Proyectos_Claude\\Proyecto Cuaderno de Bitacora\\01_Proyectos\\assets\\js\\projects_data.js';
                if (navigator.clipboard) {
                    navigator.clipboard.writeText(pathText);
                    const btn = backdrop.querySelector('#btn-copy-full-path');
                    if (btn) {
                        btn.innerText = '✓ ¡Copiada!';
                        setTimeout(() => btn.innerText = 'Copiar Ruta', 2000);
                    }
                }
            });

            return backdrop;
        },

        renderFilterTabs: function () {
            const container = document.getElementById('admin-filter-tabs-container');
            if (!container) return;

            if (this.macroMode === 'projects') {
                const total = this.projects.length;
                const lic = this.projects.filter(p => p.licitacion === true).length;
                const dir = this.projects.filter(p => p.carril === 'direct').length;
                const strat = this.projects.filter(p => p.carril === 'strategic').length;
                const fac = this.projects.filter(p => p.carril === 'facilitator').length;
                const closed = this.projects.filter(p => p.carril === 'closed').length;

                container.innerHTML = `
                    <button class="admin-filter-tab ${this.activeTab === 'all' ? 'is-active' : ''}" data-tab="all">
                        <span>Todos</span>
                        <span class="tab-badge">${total}</span>
                    </button>
                    <button class="admin-filter-tab tab-amber ${this.activeTab === 'licitacion' ? 'is-active' : ''}" data-tab="licitacion">
                        ${LDA_ICONS.licitacion.replace('width="18" height="18"', 'width="14" height="14" style="vertical-align: -1px; margin-right: 4px;"')}
                        <span>En Licitación</span>
                        <span class="tab-badge">${lic}</span>
                    </button>
                    <button class="admin-filter-tab ${this.activeTab === 'direct' ? 'is-active' : ''}" data-tab="direct">
                        <span>Gestión Directa</span>
                        <span class="tab-badge">${dir}</span>
                    </button>
                    <button class="admin-filter-tab ${this.activeTab === 'strategic' ? 'is-active' : ''}" data-tab="strategic">
                        <span>Estratégicos</span>
                        <span class="tab-badge">${strat}</span>
                    </button>
                    <button class="admin-filter-tab ${this.activeTab === 'facilitator' ? 'is-active' : ''}" data-tab="facilitator">
                        <span>Facilitadores</span>
                        <span class="tab-badge">${fac}</span>
                    </button>
                    <button class="admin-filter-tab ${this.activeTab === 'closed' ? 'is-active' : ''}" data-tab="closed">
                        <span>Histórico / Cerrados</span>
                        <span class="tab-badge">${closed}</span>
                    </button>
                `;
            } else {
                const total = this.operativas.length;
                const vig = this.operativas.filter(o => o.estadoDoc === 'Vigente').length;
                const rev = this.operativas.filter(o => o.estadoDoc === 'En Revisión').length;
                const oth = this.operativas.filter(o => !['Vigente', 'En Revisión'].includes(o.estadoDoc)).length;

                container.innerHTML = `
                    <button class="admin-filter-tab ${this.activeTab === 'all' ? 'is-active' : ''}" data-tab="all">
                        <span>Todos</span>
                        <span class="tab-badge">${total}</span>
                    </button>
                    <button class="admin-filter-tab ${this.activeTab === 'vigente' ? 'is-active' : ''}" data-tab="vigente">
                        ${LDA_ICONS.docCheck}
                        <span>Vigentes</span>
                        <span class="tab-badge">${vig}</span>
                    </button>
                    <button class="admin-filter-tab ${this.activeTab === 'revision' ? 'is-active' : ''}" data-tab="revision">
                        ${LDA_ICONS.docClock}
                        <span>En Revisión</span>
                        <span class="tab-badge">${rev}</span>
                    </button>
                    <button class="admin-filter-tab ${this.activeTab === 'otros' ? 'is-active' : ''}" data-tab="otros">
                        <span>Otros / Obsoletos</span>
                        <span class="tab-badge">${oth}</span>
                    </button>
                `;
            }

            // Bindings de las pestañas
            container.querySelectorAll('.admin-filter-tab').forEach(tab => {
                tab.addEventListener('click', () => {
                    container.querySelectorAll('.admin-filter-tab').forEach(t => t.classList.remove('is-active'));
                    tab.classList.add('is-active');
                    this.activeTab = tab.getAttribute('data-tab');
                    this.renderList();
                });
            });
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
            const pCount = document.getElementById('admin-macro-count-projects');
            if (pCount) pCount.innerText = this.projects.length;
            const oCount = document.getElementById('admin-macro-count-operativas');
            if (oCount) oCount.innerText = this.operativas.length;
        },

        // ==========================================
        // 4. RENDERIZADO VISUAL SEGÚN MACRO-MODO
        // ==========================================
        renderList: function () {
            if (this.macroMode === 'projects') {
                this.renderProjectsList();
            } else {
                this.renderOperativasList();
            }
        },

        renderProjectsList: function () {
            const body = document.getElementById('admin-drawer-body');
            if (!body) return;

            const filtered = this.projects.filter(p => {
                if (this.activeTab === 'licitacion' && !p.licitacion) return false;
                if (this.activeTab === 'direct' && p.carril !== 'direct') return false;
                if (this.activeTab === 'strategic' && p.carril !== 'strategic') return false;
                if (this.activeTab === 'facilitator' && p.carril !== 'facilitator') return false;
                if (this.activeTab === 'closed' && p.carril !== 'closed') return false;

                if (!this.searchTerm) return true;
                const matchTitle = p.title.toLowerCase().includes(this.searchTerm);
                const matchSub = (p.subtitle || '').toLowerCase().includes(this.searchTerm);
                const matchId = (p.id || '').toLowerCase().includes(this.searchTerm);
                const matchTags = p.tags && p.tags.some(t => t.toLowerCase().includes(this.searchTerm));
                const matchEstado = (p.estado || '').toLowerCase().includes(this.searchTerm);
                return matchTitle || matchSub || matchId || matchTags || matchEstado;
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
                const isReplan = p.replanificado === true;
                const semaforo = p.semaforo || 'verde';

                return `
                    <div class="admin-card lane-card-${p.carril} ${semaforo === 'pausa' || p.estado === 'En Pausa / Parado' ? 'is-paused-card' : ''}" data-id="${p.id}">
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

                        <!-- CLASIFICACIÓN MACRO: PROYECTO VS OPERATIVA -->
                        <div class="admin-classifier-row">
                            <span class="admin-classifier-label">Tipo de Bitácora / Clasificación:</span>
                            <div class="admin-classifier-segmented" data-id="${p.id}">
                                <button type="button" class="admin-classifier-btn is-active" data-id="${p.id}" title="Clasificado en Bitácora de Proyectos">
                                    ${LDA_ICONS.folderProjects}
                                    <span>Iniciativa de Proyecto</span>
                                </button>
                                <button type="button" class="admin-classifier-btn btn-to-operativa" data-id="${p.id}" title="Mover este elemento a Procedimientos y Operativas">
                                    ${LDA_ICONS.fileManuals}
                                    <span>Mover a Procedimientos &rarr;</span>
                                </button>
                            </div>
                        </div>

                        <!-- FILA DE TOGGLES: LICITACIÓN Y REPLANIFICACIÓN -->
                        <div class="admin-toggles-row">
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
                                <label class="admin-switch" title="Marcar si ha tenido replanificación">
                                    <input type="checkbox" class="admin-toggle-replan" data-id="${p.id}" ${isReplan ? 'checked' : ''}>
                                    <span class="admin-switch-slider"></span>
                                </label>
                            </div>
                        </div>

                        <!-- CONTROLES DE CARRIL Y FASE -->
                        <div class="admin-fields-grid">
                            <div class="admin-field-group">
                                <label class="admin-field-label">Carril en el Portfolio</label>
                                <select class="admin-field-select admin-select-carril" data-id="${p.id}">
                                    <option value="direct" ${p.carril === 'direct' ? 'selected' : ''}>Gestión Directa (PO / PM)</option>
                                    <option value="strategic" ${p.carril === 'strategic' ? 'selected' : ''}>Estratégicos</option>
                                    <option value="facilitator" ${p.carril === 'facilitator' ? 'selected' : ''}>Facilitadores / Afectados</option>
                                    <option value="closed" ${p.carril === 'closed' ? 'selected' : ''}>Histórico / Cerrados</option>
                                </select>
                            </div>

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
                                    <option value="Cerrado / Completado" ${p.estado === 'Cerrado / Completado' || p.estado === 'Cerrado / Histórico' || p.estado === 'Cerrado' ? 'selected' : ''}>Cerrado / Histórico</option>
                                </select>
                            </div>
                        </div>

                        <!-- SEMÁFORO DE SALUD OPERATIVA -->
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

            // BINDING DE RECLASIFICACIÓN DE PROYECTO A OPERATIVA
            body.querySelectorAll('.btn-to-operativa').forEach(btn => {
                btn.addEventListener('click', (e) => {
                    const id = btn.getAttribute('data-id');
                    this.reclassifyItem(id, 'operativa');
                });
            });

            // BINDINGS DE PROYECTOS
            body.querySelectorAll('.admin-toggle-licitacion').forEach(chk => {
                chk.addEventListener('change', (e) => {
                    const id = e.target.getAttribute('data-id');
                    this.setProjectLicitacion(id, e.target.checked);
                });
            });

            body.querySelectorAll('.admin-toggle-replan').forEach(chk => {
                chk.addEventListener('change', (e) => {
                    const id = e.target.getAttribute('data-id');
                    this.setProjectReplan(id, e.target.checked);
                });
            });

            body.querySelectorAll('.admin-select-carril').forEach(sel => {
                sel.addEventListener('change', (e) => {
                    const id = e.target.getAttribute('data-id');
                    const proj = this.projects.find(x => x.id === id);
                    if (proj) {
                        proj.carril = e.target.value;
                        this.applyStateToUI();
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

            body.querySelectorAll('.admin-semaforo-pill').forEach(btn => {
                btn.addEventListener('click', (e) => {
                    const id = btn.getAttribute('data-id');
                    const val = btn.getAttribute('data-val');
                    const proj = this.projects.find(x => x.id === id);
                    if (proj) {
                        proj.semaforo = val;
                        const group = btn.closest('.admin-semaforo-segmented');
                        if (group) {
                            group.querySelectorAll('.admin-semaforo-pill').forEach(b => b.classList.remove('is-active'));
                            btn.classList.add('is-active');
                        }
                        const cardAdmin = body.querySelector(`.admin-card[data-id="${id}"]`);
                        if (cardAdmin) {
                            cardAdmin.classList.toggle('is-paused-card', val === 'pausa' || proj.estado === 'En Pausa / Parado');
                        }
                        this.applyStateToUI();
                    }
                });
            });
        },

        renderOperativasList: function () {
            const body = document.getElementById('admin-drawer-body');
            if (!body) return;

            const filtered = this.operativas.filter(op => {
                if (this.activeTab === 'vigente' && op.estadoDoc !== 'Vigente') return false;
                if (this.activeTab === 'revision' && op.estadoDoc !== 'En Revisión') return false;
                if (this.activeTab === 'otros' && ['Vigente', 'En Revisión'].includes(op.estadoDoc)) return false;

                if (!this.searchTerm) return true;
                const matchTitle = op.title.toLowerCase().includes(this.searchTerm);
                const matchSub = (op.subtitle || '').toLowerCase().includes(this.searchTerm);
                const matchArea = (op.area || '').toLowerCase().includes(this.searchTerm);
                const matchTipo = (op.tipoDoc || '').toLowerCase().includes(this.searchTerm);
                const matchTags = op.tags && op.tags.some(t => t.toLowerCase().includes(this.searchTerm));
                return matchTitle || matchSub || matchArea || matchTipo || matchTags;
            });

            if (filtered.length === 0) {
                body.innerHTML = `
                    <div class="admin-empty-state">
                        <div style="font-size: 2.2rem; margin-bottom: 10px;">📋</div>
                        <h4 style="color: var(--text-main); font-weight: 700; margin: 0 0 6px 0;">No se encontraron manuales</h4>
                        <p style="font-size: 0.85rem; color: var(--text-sec); margin: 0;">Prueba a seleccionar otra pestaña o limpia el término de búsqueda.</p>
                    </div>
                `;
                return;
            }

            body.innerHTML = filtered.map(op => {
                const acronym = this.getAcronym(op);
                const isVigente = op.estadoDoc === 'Vigente';
                const isRevision = op.estadoDoc === 'En Revisión';

                return `
                    <div class="admin-card lane-card-services" data-id="${op.id}">
                        <div class="admin-card-header">
                            <div class="admin-card-identity">
                                <span class="admin-card-badge">${acronym}</span>
                                <div>
                                    <h4 class="admin-card-title">${op.title}</h4>
                                    <span class="admin-card-subtitle">${op.subtitle || op.desc || ''}</span>
                                </div>
                            </div>
                            <span class="doc-badge badge-doc-version">${op.version || 'v1.0'}</span>
                        </div>

                        <!-- CLASIFICACIÓN MACRO: PROYECTO VS OPERATIVA -->
                        <div class="admin-classifier-row">
                            <span class="admin-classifier-label">Tipo de Bitácora / Clasificación:</span>
                            <div class="admin-classifier-segmented" data-id="${op.id}">
                                <button type="button" class="admin-classifier-btn btn-to-project" data-id="${op.id}" title="Mover este elemento a Iniciativas de Proyecto">
                                    ${LDA_ICONS.folderProjects}
                                    <span>Mover a Proyectos &rarr;</span>
                                </button>
                                <button type="button" class="admin-classifier-btn is-active" data-id="${op.id}" title="Clasificado en Procedimientos y Operativas">
                                    ${LDA_ICONS.fileManuals}
                                    <span>Procedimiento / Operativa</span>
                                </button>
                            </div>
                        </div>

                        <!-- CONTROLES DOCUMENTALES PROPIOS -->
                        <div class="admin-fields-grid" style="margin-top: 14px;">
                            <!-- Estado Documental -->
                            <div class="admin-field-group">
                                <label class="admin-field-label">Estado Documental</label>
                                <select class="admin-field-select admin-select-op-estado" data-id="${op.id}">
                                    <option value="Vigente" ${op.estadoDoc === 'Vigente' ? 'selected' : ''}>Vigente / Activo</option>
                                    <option value="En Revisión" ${op.estadoDoc === 'En Revisión' ? 'selected' : ''}>En Revisión / Auditoría</option>
                                    <option value="Borrador" ${op.estadoDoc === 'Borrador' ? 'selected' : ''}>Borrador en Redacción</option>
                                    <option value="Obsoleto" ${op.estadoDoc === 'Obsoleto' ? 'selected' : ''}>Obsoleto / Archivado</option>
                                </select>
                            </div>

                            <!-- Tipo de Procedimiento -->
                            <div class="admin-field-group">
                                <label class="admin-field-label">Tipo de Procedimiento</label>
                                <select class="admin-field-select admin-select-op-tipo" data-id="${op.id}">
                                    <option value="Manual Operativo" ${op.tipoDoc === 'Manual Operativo' ? 'selected' : ''}>Manual Operativo</option>
                                    <option value="Procedimiento Normativo" ${op.tipoDoc === 'Procedimiento Normativo' ? 'selected' : ''}>Procedimiento Normativo</option>
                                    <option value="Guía Técnica" ${op.tipoDoc === 'Guía Técnica' ? 'selected' : ''}>Guía Técnica</option>
                                    <option value="Protocolo de Sistemas" ${op.tipoDoc === 'Protocolo de Sistemas' ? 'selected' : ''}>Protocolo de Sistemas</option>
                                </select>
                            </div>
                        </div>

                        <div class="admin-fields-grid" style="margin-top: 10px;">
                            <!-- Versión -->
                            <div class="admin-field-group">
                                <label class="admin-field-label">Versión</label>
                                <input type="text" class="admin-field-select admin-input-op-version" data-id="${op.id}" value="${op.version || 'v1.0'}" placeholder="ej. v2.4">
                            </div>

                            <!-- Nivel de Criticidad -->
                            <div class="admin-field-group">
                                <label class="admin-field-label">Nivel de Criticidad</label>
                                <select class="admin-field-select admin-select-op-crit" data-id="${op.id}">
                                    <option value="Crítica" ${op.criticidad === 'Crítica' ? 'selected' : ''}>Crítica (Obligado Cumplimiento)</option>
                                    <option value="Alta" ${op.criticidad === 'Alta' ? 'selected' : ''}>Alta</option>
                                    <option value="Media" ${op.criticidad === 'Media' ? 'selected' : ''}>Media</option>
                                    <option value="Estándar" ${op.criticidad === 'Estándar' ? 'selected' : ''}>Estándar</option>
                                </select>
                            </div>
                        </div>

                        <div class="admin-fields-grid" style="margin-top: 10px;">
                            <!-- Última Revisión -->
                            <div class="admin-field-group">
                                <label class="admin-field-label">Última Revisión</label>
                                <input type="text" class="admin-field-select admin-input-op-ultimarevision" data-id="${op.id}" value="${op.ultimaRevision || ''}" placeholder="ej. Octubre 2026">
                            </div>

                            <!-- Próxima Revisión -->
                            <div class="admin-field-group">
                                <label class="admin-field-label">Próxima Revisión / Periodicidad</label>
                                <input type="text" class="admin-field-select admin-input-op-proximarevision" data-id="${op.id}" value="${op.proximaRevision || ''}" placeholder="ej. Octubre 2027">
                            </div>
                        </div>
                    </div>
                `;
            }).join('');

            // BINDING DE RECLASIFICACIÓN DE OPERATIVA A PROYECTO
            body.querySelectorAll('.btn-to-project').forEach(btn => {
                btn.addEventListener('click', (e) => {
                    const id = btn.getAttribute('data-id');
                    this.reclassifyItem(id, 'project');
                });
            });

            // BINDINGS DE OPERATIVAS
            body.querySelectorAll('.admin-select-op-estado').forEach(sel => {
                sel.addEventListener('change', (e) => {
                    const id = e.target.getAttribute('data-id');
                    const op = this.operativas.find(x => x.id === id);
                    if (op) {
                        op.estadoDoc = e.target.value;
                        this.applyStateToUI();
                    }
                });
            });

            body.querySelectorAll('.admin-select-op-tipo').forEach(sel => {
                sel.addEventListener('change', (e) => {
                    const id = e.target.getAttribute('data-id');
                    const op = this.operativas.find(x => x.id === id);
                    if (op) {
                        op.tipoDoc = e.target.value;
                        this.applyStateToUI();
                    }
                });
            });

            body.querySelectorAll('.admin-input-op-version').forEach(inp => {
                inp.addEventListener('input', (e) => {
                    const id = e.target.getAttribute('data-id');
                    const op = this.operativas.find(x => x.id === id);
                    if (op) {
                        op.version = e.target.value.trim();
                        this.applyStateToUI();
                    }
                });
            });

            body.querySelectorAll('.admin-select-op-crit').forEach(sel => {
                sel.addEventListener('change', (e) => {
                    const id = e.target.getAttribute('data-id');
                    const op = this.operativas.find(x => x.id === id);
                    if (op) {
                        op.criticidad = e.target.value;
                        this.applyStateToUI();
                    }
                });
            });

            body.querySelectorAll('.admin-input-op-ultimarevision').forEach(inp => {
                inp.addEventListener('input', (e) => {
                    const id = e.target.getAttribute('data-id');
                    const op = this.operativas.find(x => x.id === id);
                    if (op) {
                        op.ultimaRevision = e.target.value.trim();
                        this.applyStateToUI();
                    }
                });
            });

            body.querySelectorAll('.admin-input-op-proximarevision').forEach(inp => {
                inp.addEventListener('input', (e) => {
                    const id = e.target.getAttribute('data-id');
                    const op = this.operativas.find(x => x.id === id);
                    if (op) {
                        op.proximaRevision = e.target.value.trim();
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

            const card = document.querySelector(`.admin-card[data-id="${id}"]`);
            if (card) {
                const box = card.querySelector('.admin-licitacion-box');
                if (box) {
                    box.classList.toggle('is-active', isActive);
                    const statusText = box.querySelector('.admin-licitacion-status-text');
                    if (statusText) statusText.innerText = isActive ? 'En Licitación' : 'Sin Licitación';
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

            const card = document.querySelector(`.admin-card[data-id="${id}"]`);
            if (card) {
                const box = card.querySelector('.admin-replan-box');
                if (box) {
                    box.classList.toggle('is-active', isReplan);
                    const statusText = box.querySelector('.admin-replan-status-text');
                    if (statusText) statusText.innerText = isReplan ? 'Con Replanificación' : 'Plan Inicial';
                    const chk = box.querySelector('.admin-toggle-replan');
                    if (chk) chk.checked = isReplan;
                }
            }

            this.applyStateToUI();
        },

        reclassifyItem: function (id, toType) {
            if (toType === 'operativa') {
                const idx = this.projects.findIndex(x => x.id === id);
                if (idx === -1) return;
                const proj = this.projects[idx];
                this.projects.splice(idx, 1);

                const op = {
                    id: proj.id,
                    title: proj.title,
                    subtitle: proj.subtitle || proj.desc || '',
                    desc: proj.desc || '',
                    tipoDoc: 'Manual Operativo',
                    area: 'Sistemas & Identidades',
                    estadoDoc: 'Vigente',
                    version: 'v1.0',
                    ultimaRevision: 'Octubre 2026',
                    proximaRevision: 'Octubre 2027',
                    criticidad: 'Alta',
                    href: proj.href || '#',
                    tags: proj.tags || []
                };
                this.operativas.push(op);

                this.applyStateToUI();
                this.updateDrawerStats();
                this.renderFilterTabs();
                this.renderList();
                this.showToast(`✓ '${proj.title}' movido a Procedimientos y Operativas`);
            } else if (toType === 'project') {
                const idx = this.operativas.findIndex(x => x.id === id);
                if (idx === -1) return;
                const op = this.operativas[idx];
                this.operativas.splice(idx, 1);

                const proj = {
                    id: op.id,
                    title: op.title,
                    subtitle: op.subtitle || op.desc || '',
                    desc: op.desc || '',
                    carril: 'strategic',
                    estado: 'En Curso',
                    licitacion: false,
                    replanificado: false,
                    semaforo: 'verde',
                    href: op.href || '#',
                    tags: op.tags || []
                };
                this.projects.push(proj);

                this.applyStateToUI();
                this.updateDrawerStats();
                this.renderFilterTabs();
                this.renderList();
                this.showToast(`✓ '${op.title}' movido a Iniciativas de Proyecto`);
            }
        },

        getPermissionStatus: async function () {
            if (!this.fileHandle) return 'disconnected';
            try {
                if (typeof this.fileHandle.queryPermission === 'function') {
                    const q = await this.fileHandle.queryPermission({ mode: 'readwrite' });
                    return q; // 'granted' | 'prompt' | 'denied'
                }
                return 'prompt';
            } catch (_) {
                return 'prompt';
            }
        },

        updatePersistenceUI: async function () {
            const btnAuth = document.getElementById('btn-admin-auth');
            const dot = document.getElementById('admin-auth-dot');
            const text = document.getElementById('admin-auth-text');
            if (!btnAuth || !dot || !text) return;

            const status = await this.getPermissionStatus();

            btnAuth.classList.remove('is-connected', 'is-pending');
            dot.classList.remove('is-connected', 'is-pending');

            if (status === 'granted') {
                btnAuth.classList.add('is-connected');
                dot.classList.add('is-connected');
                text.innerText = '🟢 Escritura directa conectada';
                btnAuth.title = 'projects_data.js vinculado y con permisos de escritura activos en disco';
            } else if (status === 'prompt') {
                btnAuth.classList.add('is-pending');
                dot.classList.add('is-pending');
                text.innerText = '⚠️ Reactivar permiso de guardado';
                btnAuth.title = 'Haz clic para renovar el permiso de escritura directa sin volver a seleccionar el archivo';
            } else {
                text.innerText = '🔑 Autorizar Escritura Directa';
                btnAuth.title = 'Selecciona projects_data.js una sola vez para permitir guardado directo';
            }
        },

        authorizeOrReactivateAccess: async function (forcePicker = false) {
            try {
                if (this.fileHandle && !forcePicker) {
                    let perm = 'prompt';
                    if (typeof this.fileHandle.requestPermission === 'function') {
                        perm = await this.fileHandle.requestPermission({ mode: 'readwrite' });
                    }
                    if (perm === 'granted') {
                        await this.updatePersistenceUI();
                        this.showToast('✅ Permiso reactivado — guardado directo en disco activo');
                        this.closePathHelpModal();
                        return true;
                    }
                }

                if ('showOpenFilePicker' in window) {
                    const [handle] = await window.showOpenFilePicker({
                        id: 'bitacora-data-file',
                        types: [{
                            description: 'Archivo projects_data.js de Bitácora',
                            accept: { 'text/javascript': ['.js'] }
                        }],
                        multiple: false
                    });

                    if (handle) {
                        this.fileHandle = handle;
                        await storeHandle(handle);
                        let perm = 'prompt';
                        if (typeof handle.requestPermission === 'function') {
                            perm = await handle.requestPermission({ mode: 'readwrite' });
                        }
                        await this.updatePersistenceUI();
                        if (perm === 'granted') {
                            this.showToast('✅ projects_data.js vinculado. Escritura directa habilitada.');
                            this.closePathHelpModal();
                            return true;
                        }
                    }
                } else {
                    this.openPathHelpModal();
                }
            } catch (err) {
                if (err.name !== 'AbortError') {
                    console.warn('Error autorizando:', err);
                    this.showToast('⚠️ No se concedió el permiso de escritura');
                }
            }
            await this.updatePersistenceUI();
            return false;
        },

        openPathHelpModal: function () {
            const modal = document.getElementById('modal-admin-path-help');
            if (modal) {
                modal.classList.add('is-open');
            }
        },

        closePathHelpModal: function () {
            const modal = document.getElementById('modal-admin-path-help');
            if (modal) {
                modal.classList.remove('is-open');
            }
        },

        openDrawer: function (targetTab = null, targetMacro = null) {
            const drawer = this.buildDrawer();
            const currentMode = targetMacro || localStorage.getItem('bitacora-macro-mode') || 'projects';
            const effectiveMacro = (currentMode === 'operativas' || currentMode === 'manuales') ? 'operativas' : 'projects';
            this.macroMode = effectiveMacro;
            drawer.querySelectorAll('.admin-macro-tab').forEach(t => {
                t.classList.toggle('is-active', t.getAttribute('data-macro') === effectiveMacro);
            });
            if (targetTab) {
                this.activeTab = targetTab;
            }
            this.renderFilterTabs();
            this.renderList();
            this.updatePersistenceUI();
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
        // 5. PERSISTENCIA UNIVERSAL MEDIANTE FILE SYSTEM API Y AUTO-GUARDADO
        // ==========================================
        generateFileContent: function () {
            return `/**\n * CATÁLOGO MAESTRO DEL CUADERNO DE BITÁCORA - LÍNEA DIRECTA ASEGURADORA\n * Estructura bifurcada oficial:\n * 1. BITACORA_PROJECTS_DATA: Iniciativas de Transformación con ciclo de vida, fases, licitaciones y salud operativa.\n * 2. BITACORA_OPERATIVAS_DATA: Procedimientos, Manuales Técnicos y Operativas continuas (BAU) con gobernanza documental.\n * Persistencia en disco mediante File System Access API nativa e IndexedDB.\n * Fecha de sincronización: ${new Date().toISOString().split('T')[0]}\n */\n\n// 1. BITÁCORA DE GESTIÓN DE PROYECTOS\nwindow.BITACORA_PROJECTS_DATA = ${JSON.stringify(this.projects, null, 4)};\n\n// 2. BITÁCORA DE PROCEDIMIENTOS Y OPERATIVAS\nwindow.BITACORA_OPERATIVAS_DATA = ${JSON.stringify(this.operativas, null, 4)};\n\n// Contenedor global de catálogo unificado\nwindow.BITACORA_CATALOG = {\n    projects: window.BITACORA_PROJECTS_DATA,\n    operativas: window.BITACORA_OPERATIVAS_DATA\n};\n`;
        },

        saveViaFileSystemAPI: async function (forceNew = false) {
            const saveBtn = document.getElementById('btn-admin-save');
            if (saveBtn) {
                saveBtn.disabled = true;
                saveBtn.innerText = 'Guardando en disco...';
            }

            try {
                let savedDirectly = false;

                if (!this.fileHandle && !forceNew) {
                    this.fileHandle = await getStoredHandle();
                }

                if (this.fileHandle && !forceNew) {
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
                        hasPermission = false;
                    }

                    if (hasPermission) {
                        const writable = await this.fileHandle.createWritable();
                        await writable.write(this.generateFileContent());
                        await writable.close();
                        savedDirectly = true;
                        await this.updatePersistenceUI();
                        this.showToast('✅ Cambios guardados físicamente en projects_data.js');
                    }
                }

                if (!savedDirectly) {
                    // Si no tiene handle o no concedió permiso, ofrecer autorizar o descargar
                    if ('showOpenFilePicker' in window && !this.fileHandle) {
                        const authorized = await this.authorizeOrReactivateAccess(true);
                        if (authorized && this.fileHandle) {
                            const writable = await this.fileHandle.createWritable();
                            await writable.write(this.generateFileContent());
                            await writable.close();
                            this.showToast('✅ Cambios guardados físicamente en projects_data.js');
                            savedDirectly = true;
                        }
                    }

                    if (!savedDirectly) {
                        this.openPathHelpModal();
                        this.downloadMasterFile();
                    }
                }
            } catch (err) {
                if (err.name !== 'AbortError') {
                    console.warn('Error guardando en disco:', err);
                    this.openPathHelpModal();
                    this.downloadMasterFile();
                }
            } finally {
                if (saveBtn) {
                    saveBtn.disabled = false;
                    saveBtn.innerText = '💾 Guardar Cambios en Archivo';
                }
                await this.updatePersistenceUI();
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
            }
            if (window.BITACORA_OPERATIVAS_DATA) {
                this.operativas = JSON.parse(JSON.stringify(window.BITACORA_OPERATIVAS_DATA));
            }
            this.applyStateToUI();
            this.renderList();
            this.showToast('↺ Valores restaurados al catálogo base');
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
