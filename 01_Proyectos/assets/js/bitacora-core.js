/**
 * BITÁCORA CORE JS - Motor Unificado del Cuaderno de Bitácora (v3.0)
 * Sistema de Diseño de Élite: Control de Temas, Carruseles con Rueda/Drag,
 * Barra de Progreso de Lectura, Quick Actions Flotantes, Toasts y Buscador Spotlight (Ctrl+K)
 */

// ==========================================
// 1. CONTROL DE TEMAS (DARK / LIGHT)
// ==========================================
function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme') || localStorage.getItem('theme') || 'light';
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';

    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    localStorage.setItem('bitacora-theme', newTheme);

    const checkbox = document.getElementById('theme-checkbox');
    if (checkbox) checkbox.checked = (newTheme === 'dark');

    if (window.BitacoraUI && window.BitacoraUI.toast) {
        window.BitacoraUI.toast(`Modo ${newTheme === 'dark' ? 'Oscuro' : 'Claro'} activado`, 'info', 1800);
    }
}

function initTheme() {
    const savedTheme = localStorage.getItem('theme') || localStorage.getItem('bitacora-theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
    const checkbox = document.getElementById('theme-checkbox');
    if (checkbox) checkbox.checked = (savedTheme === 'dark');
}

// ==========================================
// 2. SISTEMA DE TOAST NOTIFICATIONS (LIQUID FEEDBACK)
// ==========================================
window.BitacoraUI = {
    toast(message, type = 'info', duration = 2400) {
        let container = document.getElementById('bitacora-toast-container');
        if (!container) {
            container = document.createElement('div');
            container.id = 'bitacora-toast-container';
            container.className = 'bitacora-toast-container';
            document.body.appendChild(container);
        }
        const toast = document.createElement('div');
        toast.className = `bitacora-toast toast-${type}`;
        const icon = type === 'success' 
            ? '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>'
            : '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>';
        toast.innerHTML = `${icon}<span>${message}</span>`;
        container.appendChild(toast);

        setTimeout(() => {
            toast.style.opacity = '0';
            toast.style.transform = 'translateY(12px) scale(0.95)';
            toast.style.transition = 'all 0.25s cubic-bezier(0.16, 1, 0.3, 1)';
            setTimeout(() => toast.remove(), 250);
        }, duration);
    }
};

// ==========================================
// MOTOR CENTRALIZADO DE SCROLL (HIGH-PERFORMANCE RAF DISPATCHER)
// ==========================================
const _scrollSubscribers = [];
let _globalScrollTicking = false;

function subscribeScroll(fn) {
    if (typeof fn === 'function' && !_scrollSubscribers.includes(fn)) {
        _scrollSubscribers.push(fn);
    }
}

function initGlobalScrollEngine() {
    if (window._bitacoraScrollEngineInit) return;
    window._bitacoraScrollEngineInit = true;

    const onScrollTick = () => {
        const scrollY = window.scrollY || window.pageYOffset || document.documentElement.scrollTop || 0;
        for (let i = 0; i < _scrollSubscribers.length; i++) {
            try {
                _scrollSubscribers[i](scrollY);
            } catch (_) {}
        }
        _globalScrollTicking = false;
    };

    window.addEventListener('scroll', () => {
        if (!_globalScrollTicking) {
            window.requestAnimationFrame(onScrollTick);
            _globalScrollTicking = true;
        }
    }, { passive: true });
}

// ==========================================
// 3. BARRA DE PROGRESO DE LECTURA (READING PROGRESS)
// ==========================================
function initReadingProgressBar() {
    let bar = document.getElementById('bitacora-reading-bar');
    if (!bar) {
        bar = document.createElement('div');
        bar.id = 'bitacora-reading-bar';
        bar.className = 'bitacora-reading-bar';
        (document.documentElement || document.body).appendChild(bar);
    }

    let cachedTotalHeight = 0;
    function calcTotalHeight() {
        cachedTotalHeight = Math.max(
            document.body.scrollHeight,
            document.documentElement.scrollHeight,
            document.body.offsetHeight,
            document.documentElement.offsetHeight
        ) - window.innerHeight;
    }

    function updateProgress(scrollY) {
        if (cachedTotalHeight <= 0) {
            bar.style.transform = 'scaleX(0)';
            return;
        }
        const progress = Math.min(Math.max(scrollY / cachedTotalHeight, 0), 1);
        bar.style.transform = `scaleX(${progress})`;
    }

    subscribeScroll(updateProgress);

    window.addEventListener('resize', () => {
        calcTotalHeight();
        updateProgress(window.scrollY || window.pageYOffset || 0);
    }, { passive: true });

    calcTotalHeight();
    updateProgress(window.scrollY || window.pageYOffset || 0);
}

// ==========================================
// 4. BOTONES FLOTANTES DE ACCIÓN RÁPIDA (QUICK ACTIONS)
// ==========================================
function initQuickActions() {
    if (document.getElementById('bitacora-quick-actions')) return;
    const actions = document.createElement('div');
    actions.id = 'bitacora-quick-actions';
    actions.className = 'bitacora-quick-actions';
    actions.innerHTML = `
        <button class="quick-action-btn" id="btn-zen-mode" title="Modo Presentación Zen (Z)" aria-label="Modo Zen">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"/>
            </svg>
        </button>
        <button class="quick-action-btn" id="btn-recent-drawer" title="Visitas Recientes (H)" aria-label="Visitas Recientes">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="10"></circle>
                <polyline points="12 6 12 12 16 14"></polyline>
            </svg>
        </button>
        <button class="quick-action-btn" id="btn-shortcuts-help" title="Atajos de Teclado (?)" aria-label="Atajos de Teclado">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="10"></circle>
                <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path>
                <line x1="12" y1="17" x2="12.01" y2="17"></line>
            </svg>
        </button>
        <button class="quick-action-btn" id="btn-copy-url" title="Copiar enlace de esta página (C)" aria-label="Copiar enlace">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
            </svg>
        </button>
        <button class="quick-action-btn" id="btn-scroll-top" title="Volver arriba (Shift + ↑)" aria-label="Volver arriba">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="18 15 12 9 6 15"></polyline>
            </svg>
        </button>
    `;
    if (document.querySelector('.export-fab')) {
        actions.classList.add('has-export-fab');
    }
    document.body.appendChild(actions);

    actions.querySelector('#btn-zen-mode')?.addEventListener('click', () => {
        if (window.BitacoraUI && window.BitacoraUI.toggleZenMode) window.BitacoraUI.toggleZenMode();
    });
    actions.querySelector('#btn-recent-drawer')?.addEventListener('click', () => {
        if (window.BitacoraUI && window.BitacoraUI.toggleRecentDrawer) window.BitacoraUI.toggleRecentDrawer();
    });
    actions.querySelector('#btn-shortcuts-help')?.addEventListener('click', () => {
        const m = document.getElementById('bitacora-kbd-modal');
        if (m) {
            const isActive = m.classList.toggle('active');
            m.style.display = isActive ? 'flex' : 'none';
        }
    });
    actions.querySelector('#btn-scroll-top')?.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
    actions.querySelector('#btn-copy-url')?.addEventListener('click', () => {
        navigator.clipboard.writeText(window.location.href).then(() => {
            if (window.BitacoraUI && window.BitacoraUI.toast) {
                window.BitacoraUI.toast('Enlace copiado al portapapeles', 'success');
            }
        }).catch(() => {
            if (window.BitacoraUI && window.BitacoraUI.toast) {
                window.BitacoraUI.toast('No se pudo copiar el enlace', 'info');
            }
        });
    });

    let isVisible = false;
    function updateQuickActions(scrollY) {
        // Histeresis anti-rebote: visible > 320px, oculto < 200px
        if (!isVisible && scrollY > 320) {
            isVisible = true;
            actions.classList.add('is-visible');
        } else if (isVisible && scrollY < 200) {
            isVisible = false;
            actions.classList.remove('is-visible');
        }
    }

    subscribeScroll(updateQuickActions);
    updateQuickActions(window.scrollY || window.pageYOffset || 0);
}

// ==========================================
// 5. CONTROL DE CARRUSELES (CON RUEDA & DRAG)
// ==========================================
function updateCarouselButtons(track) {
    if (!track) return;
    const container = track.parentElement;
    if (!container) return;
    const btnLeft = container.querySelector('.carousel-btn.left');
    const btnRight = container.querySelector('.carousel-btn.right');

    if (btnLeft && btnRight) {
        if (track.scrollLeft <= 10) {
            btnLeft.classList.add('hidden');
        } else {
            btnLeft.classList.remove('hidden');
        }

        if (Math.ceil(track.scrollLeft) + track.clientWidth >= track.scrollWidth - 10) {
            btnRight.classList.add('hidden');
        } else {
            btnRight.classList.remove('hidden');
        }
    }
}

function scrollCarousel(btn, amount) {
    const container = btn.parentElement;
    const track = container.querySelector('.carousel-track');
    if (track) {
        track.scrollBy({ left: amount, behavior: 'smooth' });
    }
}

function initCarousels() {
    document.querySelectorAll('.carousel-track').forEach(track => {
        updateCarouselButtons(track);

        // Actualización eficiente de botones ante cualquier desplazamiento
        let scrollTicking = false;
        track.addEventListener('scroll', () => {
            if (!scrollTicking) {
                window.requestAnimationFrame(() => {
                    updateCarouselButtons(track);
                    scrollTicking = false;
                });
                scrollTicking = true;
            }
        }, { passive: true });

        // Arrastre suave con ratón (Drag-to-scroll fluido)
        // NOTA: Se respeta 100% el scroll vertical del usuario (sin 'wheel' hijacking ni bloqueos)
        let isDown = false;
        let startX = 0;
        let initialScroll = 0;
        let dragDistance = 0;

        const endDrag = () => {
            if (!isDown) return;
            isDown = false;
            track.classList.remove('active');
            track.style.scrollBehavior = '';
            track.style.scrollSnapType = '';
            // Reset de distancia tras un breve instante para no anular el click normal
            setTimeout(() => { dragDistance = 0; }, 50);
        };

        track.addEventListener('mousedown', (e) => {
            if (e.target.closest('button, input, select, textarea')) return;
            isDown = true;
            dragDistance = 0;
            startX = e.pageX;
            initialScroll = track.scrollLeft;
            track.classList.add('active');
            track.style.scrollBehavior = 'auto';
            track.style.scrollSnapType = 'none';
        });

        window.addEventListener('mouseup', endDrag);

        track.addEventListener('mouseleave', () => {
            if (isDown) endDrag();
        });

        track.addEventListener('mousemove', (e) => {
            if (!isDown) return;
            const deltaX = e.pageX - startX;
            dragDistance = Math.abs(deltaX);

            if (dragDistance > 6) {
                e.preventDefault();
                track.scrollLeft = initialScroll - deltaX;
            }
        });

        // Prevenir navegación accidental en tarjetas si el usuario estaba arrastrando
        track.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', (e) => {
                if (dragDistance > 6) {
                    e.preventDefault();
                    e.stopPropagation();
                }
            });
        });
    });
}

// ==========================================
// 6. BREADCRUMBS Y NAVEGACIÓN DINÁMICA
// ==========================================
function initBreadcrumbLogic() {
    const breadcrumb = document.querySelector('.nav-breadcrumb');
    if (!breadcrumb) return;

    if (breadcrumb.querySelector('.collapsed-trigger')) return;

    const items = Array.from(breadcrumb.querySelectorAll('.nav-breadcrumb-item:not(.current)'));
    const separators = Array.from(breadcrumb.querySelectorAll('.nav-breadcrumb-sep'));

    if (items.length > 3) {
        const toCollapse = items.slice(1, -1);

        const trigger = document.createElement('span');
        trigger.className = 'nav-breadcrumb-item collapsed-trigger';
        trigger.innerHTML = '...';
        trigger.title = 'Ver más niveles';

        const dropdown = document.createElement('div');
        dropdown.className = 'breadcrumb-dropdown';

        toCollapse.forEach((item, index) => {
            const link = document.createElement('a');
            link.href = item.href || '#';
            link.className = 'breadcrumb-dropdown-item';
            link.textContent = item.textContent || item.title || ('Nivel ' + (index + 2));
            dropdown.appendChild(link);

            item.style.display = 'none';
            const sepIndex = items.indexOf(item);
            if (separators[sepIndex]) {
                separators[sepIndex].style.display = 'none';
            }
        });

        trigger.appendChild(dropdown);
        items[0].insertAdjacentElement('afterend', trigger);

        const newSep = document.createElement('span');
        newSep.className = 'nav-breadcrumb-sep';
        newSep.textContent = '›';
        trigger.insertAdjacentElement('afterend', newSep);

        trigger.addEventListener('click', (e) => {
            e.stopPropagation();
            dropdown.classList.toggle('active');
        });

        document.addEventListener('click', () => {
            dropdown.classList.remove('active');
        });
    }
}

function initDynamicBreadcrumb() {
    const wrapper = document.querySelector('.global-nav-wrapper');
    if (!wrapper) return;

    let isCompacted = (window.scrollY || window.pageYOffset || 0) > 100;
    if (isCompacted) wrapper.classList.add('compacted');

    function updateBreadcrumb(scrollY) {
        // Histeresis robusta anti-rebote: compacta a > 130px, restaura a < 45px
        if (!isCompacted && scrollY > 130) {
            isCompacted = true;
            wrapper.classList.add('compacted');
        } else if (isCompacted && scrollY < 45) {
            isCompacted = false;
            wrapper.classList.remove('compacted');
        }
    }

    subscribeScroll(updateBreadcrumb);
}

// ==========================================
// 7. BUSCADOR SPOTLIGHT (CTRL + K / CMD + K)
// ==========================================
class BitacoraSearch {
    constructor() {
        this.index = window.BITACORA_SEARCH_INDEX || [];
        this.backdrop = null;
        this.input = null;
        this.resultsContainer = null;
        this.selectedIndex = -1;
        this.currentCategory = 'all';
        this.init();
    }

    init() {
        this.createModalDOM();
        this.bindEvents();
    }

    createModalDOM() {
        const backdrop = document.createElement('div');
        backdrop.className = 'bitacora-search-backdrop';
        backdrop.id = 'search-modal-backdrop';

        backdrop.innerHTML = `
            <div class="bitacora-search-modal" role="dialog" aria-modal="true">
                <div class="search-input-wrapper">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="11" cy="11" r="8"></circle>
                        <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                    </svg>
                    <input type="text" class="search-input-field" placeholder="Buscar proyectos, arquitecturas, actas, licitaciones..." aria-label="Buscar">
                    <button class="search-clear-btn" id="search-clear-btn" style="display: none; background: none; border: none; color: var(--text-muted); cursor: pointer; font-size: 1.2rem; padding: 0 4px;" title="Limpiar">×</button>
                    <span class="search-kbd-shortcut">ESC</span>
                </div>
                <div class="search-categories-bar">
                    <button class="search-cat-chip active" data-cat="all">Todos</button>
                    <button class="search-cat-chip" data-cat="Estratégico">Estratégicos</button>
                    <button class="search-cat-chip" data-cat="Gestión Directa">Gestión Directa</button>
                    <button class="search-cat-chip" data-cat="Servicios">Servicios</button>
                    <button class="search-cat-chip" data-cat="Licitación">Licitaciones</button>
                </div>
                <div class="search-results-list" id="search-results-list"></div>
                <div class="search-footer-info">
                    <span>Navega con <b>↑</b> <b>↓</b> y abre con <b>Enter</b> · Cierra con <b>Esc</b></span>
                    <span><b>${this.index.length}</b> documentos indexados</span>
                </div>
            </div>
        `;

        document.body.appendChild(backdrop);
        this.backdrop = backdrop;
        this.input = backdrop.querySelector('.search-input-field');
        this.resultsContainer = backdrop.querySelector('.search-results-list');
        this.clearBtn = backdrop.querySelector('#search-clear-btn');
    }

    bindEvents() {
        // Tecla de acceso rápido global (Ctrl + K o Cmd + K)
        window.addEventListener('keydown', (e) => {
            if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
                e.preventDefault();
                this.open();
            } else if (e.key === 'Escape' && this.isOpen()) {
                this.close();
            }
        });

        // Clic fuera para cerrar
        this.backdrop.addEventListener('click', (e) => {
            if (e.target === this.backdrop) {
                this.close();
            }
        });

        // Chips de categoría
        this.backdrop.querySelectorAll('.search-cat-chip').forEach(chip => {
            chip.addEventListener('click', () => {
                this.backdrop.querySelectorAll('.search-cat-chip').forEach(c => c.classList.remove('active'));
                chip.classList.add('active');
                this.currentCategory = chip.getAttribute('data-cat');
                this.handleSearch(this.input.value.trim());
            });
        });

        // Entrada de texto
        this.input.addEventListener('input', (e) => {
            const val = e.target.value.trim();
            if (this.clearBtn) this.clearBtn.style.display = val ? 'block' : 'none';
            this.handleSearch(val);
        });

        // Botón limpiar
        if (this.clearBtn) {
            this.clearBtn.addEventListener('click', () => {
                this.input.value = '';
                this.clearBtn.style.display = 'none';
                this.handleSearch('');
                this.input.focus();
            });
        }

        // Navegación con flechas en resultados
        this.input.addEventListener('keydown', (e) => {
            const items = this.resultsContainer.querySelectorAll('.search-result-item');
            if (items.length === 0) return;

            if (e.key === 'ArrowDown') {
                e.preventDefault();
                this.selectedIndex = (this.selectedIndex + 1) % items.length;
                this.updateSelection(items);
            } else if (e.key === 'ArrowUp') {
                e.preventDefault();
                this.selectedIndex = (this.selectedIndex - 1 + items.length) % items.length;
                this.updateSelection(items);
            } else if (e.key === 'Enter') {
                e.preventDefault();
                if (this.selectedIndex >= 0 && items[this.selectedIndex]) {
                    items[this.selectedIndex].click();
                } else if (items.length > 0) {
                    items[0].click();
                }
            }
        });

        // Conectar botones externos de apertura
        document.querySelectorAll('.open-search-trigger').forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                this.open();
            });
        });
    }

    updateSelection(items) {
        items.forEach((item, idx) => {
            if (idx === this.selectedIndex) {
                item.classList.add('selected');
                item.scrollIntoView({ block: 'nearest' });
            } else {
                item.classList.remove('selected');
            }
        });
    }

    open(initialQuery = '') {
        this.backdrop.classList.add('active');
        this.input.value = initialQuery;
        this.selectedIndex = -1;
        this.handleSearch(initialQuery);
        setTimeout(() => this.input.focus(), 50);
    }

    close() {
        this.backdrop.classList.remove('active');
        this.input.blur();
    }

    isOpen() {
        return this.backdrop.classList.contains('active');
    }

    handleSearch(query) {
        if (!query) {
            this.resultsContainer.innerHTML = `
                <div class="search-popular-wrapper">
                    <div class="search-popular-title">Búsquedas Frecuentes & Atajos</div>
                    <div class="search-tags-cloud">
                        <button class="search-quick-tag" onclick="window.bitacoraSearchInstance.open('CRM')">CRM Salesforce</button>
                        <button class="search-quick-tag" onclick="window.bitacoraSearchInstance.open('Genesys')">Genesys CX</button>
                        <button class="search-quick-tag" onclick="window.bitacoraSearchInstance.open('Siniestros')">Siniestros Motor</button>
                        <button class="search-quick-tag" onclick="window.bitacoraSearchInstance.open('Databricks')">Gobierno del Dato</button>
                        <button class="search-quick-tag" onclick="window.bitacoraSearchInstance.open('Lupe')">IA Lupe (Voz & Chat)</button>
                        <button class="search-quick-tag" onclick="window.bitacoraSearchInstance.open('Agile')">Transformación Agile</button>
                        <button class="search-quick-tag" onclick="window.bitacoraSearchInstance.open('HomeServe')">Hogar HomeServe</button>
                        <button class="search-quick-tag" onclick="window.bitacoraSearchInstance.open('HNA')">Salud HNA</button>
                        <button class="search-quick-tag" onclick="window.bitacoraSearchInstance.open('Perseo')">Perseo Speech Analytics</button>
                    </div>
                </div>
            `;
            return;
        }

        const q = query.toLowerCase();
        const terms = q.split(' ').filter(t => t.length > 0);

        // Filtro por relevancia y categoría
        let matches = this.index.filter(item => {
            if (this.currentCategory !== 'all') {
                const itemCat = (item.category || '').toLowerCase();
                const targetCat = this.currentCategory.toLowerCase();
                if (!itemCat.includes(targetCat)) return false;
            }
            const searchable = `${item.title} ${item.h1} ${item.desc} ${item.project} ${item.category} ${item.kicker}`.toLowerCase();
            return terms.every(term => searchable.includes(term));
        });

        // Ordenar con prioridad si el título coincide de lleno
        matches.sort((a, b) => {
            const aTitle = (a.title || '').toLowerCase();
            const bTitle = (b.title || '').toLowerCase();
            const aExact = aTitle.includes(q);
            const bExact = bTitle.includes(q);
            if (aExact && !bExact) return -1;
            if (!aExact && bExact) return 1;
            return 0;
        });

        if (matches.length === 0) {
            this.resultsContainer.innerHTML = `
                <div style="padding: 32px 24px; text-align: center; color: var(--text-muted);">
                    <p style="font-weight: 700; margin-bottom: 6px;">No se encontraron resultados para "${query}"</p>
                    <p style="font-size: 0.85rem;">Intenta con palabras clave como "CRM", "licitación", "Perseo", "Hogar" o "LidIA".</p>
                </div>
            `;
            this.selectedIndex = -1;
            return;
        }

        this.selectedIndex = 0;
        this.resultsContainer.innerHTML = matches.slice(0, 20).map((item, idx) => `
            <a href="${this.resolveUrl(item)}" class="search-result-item ${idx === 0 ? 'selected' : ''}">
                <div class="search-result-header">
                    <span class="search-result-badge">${item.category}</span>
                    <span style="font-size: 0.75rem; color: var(--text-muted); font-weight: 600;">${item.project}</span>
                </div>
                <div class="search-result-title">${this.highlightMatch(item.title, terms)}</div>
                ${item.desc ? `<div class="search-result-desc">${this.highlightMatch(item.desc, terms)}</div>` : ''}
            </a>
        `).join('');
    }

    getBasePath() {
        const coreScript = document.querySelector('script[src*="bitacora-core.js"]');
        if (!coreScript) return '..';
        const src = coreScript.getAttribute('src');
        const idx = src.indexOf('assets/');
        if (idx > 0) {
            return src.substring(0, idx - 1);
        } else if (idx === 0) {
            return '.';
        }
        return '..';
    }

    resolveUrl(item) {
        const base = this.getBasePath();
        const cleanId = (item.id || item.url).replace(/^(\.\.\/)+/, '');
        return `${base}/${cleanId}`;
    }

    highlightMatch(text, terms) {
        if (!text) return '';
        let escaped = text;
        terms.forEach(term => {
            const reg = new RegExp(`(${term})`, 'gi');
            escaped = escaped.replace(reg, '<b style="color: var(--lda-red); text-decoration: underline;">$1</b>');
        });
        return escaped;
    }
}

// ==========================================
// 8. MODAL DE ATAJOS DE TECLADO (?)
// ==========================================
function initKeyboardShortcutsModal() {
    let modal = document.getElementById('bitacora-kbd-modal');
    if (!modal) {
        modal = document.createElement('div');
        modal.id = 'bitacora-kbd-modal';
        modal.className = 'bitacora-kbd-modal';
        modal.style.display = 'none';
        modal.innerHTML = `
            <div class="bitacora-kbd-content" role="dialog" aria-modal="true">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                    <h3 style="margin: 0; font-size: 1.15rem; font-weight: 800; display: flex; align-items: center; gap: 8px;">
                        <span style="color: var(--primary-accent, #e4002b);">⌨</span> Atajos de Teclado
                    </h3>
                    <button onclick="const m = document.getElementById('bitacora-kbd-modal'); if(m){ m.classList.remove('active'); m.style.display='none'; }" style="background: none; border: none; font-size: 1.4rem; color: var(--text-sec); cursor: pointer;">×</button>
                </div>
                <div class="kbd-row">
                    <span>Buscar en toda la bitácora</span>
                    <span class="kbd-badge">Ctrl + K / ⌘K</span>
                </div>
                <div class="kbd-row">
                    <span>Modo Presentación Zen</span>
                    <span class="kbd-badge">Z</span>
                </div>
                <div class="kbd-row">
                    <span>Visitas recientes de navegación</span>
                    <span class="kbd-badge">H</span>
                </div>
                <div class="kbd-row">
                    <span>Alternar densidad de lectura</span>
                    <span class="kbd-badge">Alt + D</span>
                </div>
                <div class="kbd-row">
                    <span>Alternar modo claro / oscuro</span>
                    <span class="kbd-badge">D</span>
                </div>
                <div class="kbd-row">
                    <span>Volver al inicio de la página</span>
                    <span class="kbd-badge">Shift + ↑</span>
                </div>
                <div class="kbd-row">
                    <span>Copiar enlace de la página</span>
                    <span class="kbd-badge">C</span>
                </div>
                <div class="kbd-row">
                    <span>Alternar vista Carrusel / Mosaico / Tabla (Inicio)</span>
                    <span class="kbd-badge">V</span>
                </div>
                <div class="kbd-row">
                    <span>Alternar macro bitácora Proyectos / Operativas (Inicio)</span>
                    <span class="kbd-badge">B</span>
                </div>
                <div class="kbd-row">
                    <span>Gestión de Estados y Portfolio (Inicio)</span>
                    <span class="kbd-badge">G</span>
                </div>
                <div class="kbd-row">
                    <span>Cerrar modal o buscador</span>
                    <span class="kbd-badge">ESC</span>
                </div>
            </div>
        `;
        document.body.appendChild(modal);

        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                modal.classList.remove('active');
                modal.style.display = 'none';
            }
        });
    }

    if (window._bitacoraKeydownBound) return;
    window._bitacoraKeydownBound = true;

    window.addEventListener('keydown', (e) => {
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA' || e.target.isContentEditable) {
            if (e.key === 'Escape') e.target.blur();
            return;
        }

        // Ctrl + K o Cmd + K: Búsqueda rápida
        if ((e.ctrlKey || e.metaKey) && (e.key === 'k' || e.key === 'K')) {
            e.preventDefault();
            if (window.bitacoraSearchInstance && typeof window.bitacoraSearchInstance.open === 'function') {
                window.bitacoraSearchInstance.open();
            }
            return;
        }

        // ? : Ayuda de atajos de teclado
        if (e.key === '?' || (e.shiftKey && (e.key === '/' || e.key === '?'))) {
            e.preventDefault();
            const m = document.getElementById('bitacora-kbd-modal');
            if (m) {
                const isActive = m.classList.toggle('active');
                m.style.display = isActive ? 'flex' : 'none';
            }
            return;
        }

        // Alt + D: Alternar densidad
        if ((e.key === 'd' || e.key === 'D') && e.altKey) {
            e.preventDefault();
            if (window.BitacoraUI && typeof window.BitacoraUI.toggleDensity === 'function') {
                window.BitacoraUI.toggleDensity();
            }
            return;
        }

        // Si hay Ctrl / Meta / Alt no interceptamos las siguientes letras
        if (e.ctrlKey || e.metaKey || e.altKey) return;

        // Z: Modo Zen
        if (e.key === 'z' || e.key === 'Z') {
            e.preventDefault();
            if (window.BitacoraUI && typeof window.BitacoraUI.toggleZenMode === 'function') {
                window.BitacoraUI.toggleZenMode();
            }
        }
        // H: Historial reciente
        else if (e.key === 'h' || e.key === 'H') {
            e.preventDefault();
            if (window.BitacoraUI && typeof window.BitacoraUI.toggleRecentDrawer === 'function') {
                window.BitacoraUI.toggleRecentDrawer();
            }
        }
        // C: Copiar URL
        else if (e.key === 'c' || e.key === 'C') {
            e.preventDefault();
            navigator.clipboard.writeText(window.location.href).then(() => {
                if (window.BitacoraUI && typeof window.BitacoraUI.toast === 'function') {
                    window.BitacoraUI.toast('Enlace copiado al portapapeles', 'success');
                }
            }).catch(() => {
                if (window.BitacoraUI && typeof window.BitacoraUI.toast === 'function') {
                    window.BitacoraUI.toast('No se pudo copiar el enlace', 'info');
                }
            });
        }
        // D: Modo Claro / Oscuro
        else if (e.key === 'd' || e.key === 'D') {
            e.preventDefault();
            if (typeof toggleTheme === 'function') {
                toggleTheme();
            }
        }
        // B: Switcher Bento / Carrusel
        else if (e.key === 'b' || e.key === 'B') {
            const mainContent = document.getElementById('main-content');
            if (mainContent && typeof setViewMode === 'function') {
                e.preventDefault();
                const isGrid = mainContent.classList.contains('view-mode-grid');
                setViewMode(isGrid ? 'carousel' : 'grid');
            }
        }
        // G: Centro de Gestión de Estados (Home)
        else if (e.key === 'g' || e.key === 'G') {
            if (window.BitacoraAdmin && typeof window.BitacoraAdmin.toggleDrawer === 'function') {
                e.preventDefault();
                window.BitacoraAdmin.toggleDrawer();
            }
        }
        // Shift + Arriba: Top
        else if (e.key === 'ArrowUp' && e.shiftKey) {
            e.preventDefault();
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
        // Escape: Cerrar todos los overlays
        else if (e.key === 'Escape') {
            const m = document.getElementById('bitacora-kbd-modal');
            if (m) {
                m.classList.remove('active');
                m.style.display = 'none';
            }
            document.getElementById('bitacora-lightbox')?.classList.remove('is-open');
            document.getElementById('bitacora-drawer-backdrop')?.classList.remove('is-open');
            if (window.BitacoraAdmin && window.BitacoraAdmin.isOpen) {
                window.BitacoraAdmin.closeDrawer();
            }
            if (document.body.classList.contains('bitacora-zen-mode')) {
                if (window.BitacoraUI && typeof window.BitacoraUI.toggleZenMode === 'function') {
                    window.BitacoraUI.toggleZenMode();
                }
            }
        }
    });
}

// ==========================================
// 9. EFECTO APPLE LIQUID GLASS (SCROLL-AWARE GLASS)
// ==========================================
function initIslandLiquidGlass() {
    const island = document.querySelector('.app-header-island');
    if (!island) return;

    let isScrolled = (window.scrollY || window.pageYOffset || 0) > 75;
    if (isScrolled) island.classList.add('is-scrolled');

    function updateGlass(scrollY) {
        // Histeresis robusta anti-parpadeo y anti-bloqueo (Deadband amplio de 50px):
        // Se activa al descender > 75px y solo se desactiva al regresar a < 25px
        if (!isScrolled && scrollY > 75) {
            isScrolled = true;
            island.classList.add('is-scrolled');
        } else if (isScrolled && scrollY < 25) {
            isScrolled = false;
            island.classList.remove('is-scrolled');
        }
    }

    subscribeScroll(updateGlass);
    updateGlass(window.scrollY || window.pageYOffset || 0);
}

// ==========================================
// 10. TRANSICIONES DE PÁGINA Y NAVEGACIÓN FLUIDA
// ==========================================
function initPageTransitions() {
    if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    window.addEventListener('pageshow', () => {
        document.body.classList.remove('bitacora-page-leaving');
    });

    document.addEventListener('click', (e) => {
        const link = e.target.closest('a');
        if (!link) return;
        if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || e.button !== 0) return;

        const href = link.getAttribute('href');
        if (!href) return;

        if (href.startsWith('#') || href.startsWith('javascript:') || href.startsWith('mailto:') || href.startsWith('tel:') || link.target === '_blank' || link.hasAttribute('download')) {
            return;
        }

        try {
            const url = new URL(link.href, window.location.href);
            if (url.origin === window.location.origin) {
                if (url.pathname === window.location.pathname && url.hash) return;

                e.preventDefault();
                document.body.classList.add('bitacora-page-leaving');
                setTimeout(() => {
                    window.location.href = link.href;
                }, 120);
            }
        } catch (_) {}
    });
}

function initSmoothAnchors() {
    document.addEventListener('click', (e) => {
        const anchor = e.target.closest('a[href^="#"]');
        if (!anchor) return;
        const hash = anchor.getAttribute('href');
        if (!hash || hash === '#' || hash.length <= 1) return;

        try {
            const targetEl = document.querySelector(hash);
            if (!targetEl) return;

            e.preventDefault();

            // Detectar si el elemento objetivo pertenece a una macro-bitácora oculta
            const inOperativas = targetEl.closest('#container-bitacora-operativas') !== null;
            const inProyectos = targetEl.closest('#container-bitacora-proyectos') !== null;

            if (inOperativas && typeof window.switchMacroBitacora === 'function') {
                window.switchMacroBitacora('operativas', false);
            } else if (inProyectos && typeof window.switchMacroBitacora === 'function') {
                window.switchMacroBitacora('proyectos', false);
            }

            // Desplazamiento suave con retardo para permitir que el contenedor se haga visible
            setTimeout(() => {
                targetEl.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });

                // Destello visual de foco en la sección o tarjeta
                targetEl.classList.remove('bitacora-card-target-focus');
                void targetEl.offsetWidth;
                targetEl.classList.add('bitacora-card-target-focus');
                setTimeout(() => targetEl.classList.remove('bitacora-card-target-focus'), 1800);

                if (history.pushState) {
                    history.pushState(null, '', hash);
                }
            }, 70);
        } catch (_) {}
    });
}

// ==========================================================================
// 12. SUITE AVANZADA DE COMPONENTES UI/UX v4.0 (SISTEMA DE GOBERNANZA CORPORATIVA)
// ==========================================================================

// 1. SMART TOC FLOTANTE JERÁRQUICO (ON-THIS-PAGE NAVIGATOR)
function initSmartTOC() {
    const mainEl = document.querySelector('main') || document.querySelector('.container');
    if (!mainEl) return;

    const isPortfolioHome = document.querySelector('.portfolio-section') !== null;

    let tocContainer = document.getElementById('bitacora-toc-container');
    if (!tocContainer) {
        tocContainer = document.createElement('nav');
        tocContainer.id = 'bitacora-toc-container';
        tocContainer.className = 'bitacora-toc-container';
        tocContainer.setAttribute('aria-label', isPortfolioHome ? 'Secciones del Portfolio' : 'Índice de la página');
        tocContainer.innerHTML = `
            <div class="bitacora-toc-header">
                <span>En esta página</span>
                <span style="color: var(--lda-red); font-size: 0.9rem;">📑</span>
            </div>
            <ul class="bitacora-toc-list"></ul>
        `;
        document.body.appendChild(tocContainer);
    }

    const list = tocContainer.querySelector('.bitacora-toc-list');
    list.innerHTML = '';
    const sectionElements = [];

    if (isPortfolioHome) {
        // Mini Macro Switcher en la cabecera del TOC
        let miniSwitch = tocContainer.querySelector('.bitacora-toc-macro-switch');
        if (!miniSwitch) {
            miniSwitch = document.createElement('div');
            miniSwitch.className = 'bitacora-toc-macro-switch';
            const currentMode = localStorage.getItem('bitacora-macro-mode') || 'proyectos';
            miniSwitch.innerHTML = `
                <button class="bitacora-toc-switch-btn ${currentMode === 'proyectos' ? 'is-active' : ''}" data-mode="proyectos" title="Ver Bitácora de Proyectos">
                    📁 Proyectos
                </button>
                <button class="bitacora-toc-switch-btn ${currentMode === 'operativas' ? 'is-active' : ''}" data-mode="operativas" title="Ver Procedimientos y Operativas">
                    📋 Operativas
                </button>
            `;
            miniSwitch.querySelectorAll('.bitacora-toc-switch-btn').forEach(btn => {
                btn.addEventListener('click', (e) => {
                    e.preventDefault();
                    const targetMode = btn.getAttribute('data-mode');
                    if (typeof window.switchMacroBitacora === 'function') {
                        window.switchMacroBitacora(targetMode);
                    }
                });
            });
            const tocHeader = tocContainer.querySelector('.bitacora-toc-header');
            if (tocHeader) tocHeader.insertAdjacentElement('afterend', miniSwitch);
        } else {
            const currentMode = localStorage.getItem('bitacora-macro-mode') || 'proyectos';
            miniSwitch.querySelectorAll('.bitacora-toc-switch-btn').forEach(btn => {
                if (btn.getAttribute('data-mode') === currentMode) {
                    btn.classList.add('is-active');
                } else {
                    btn.classList.remove('is-active');
                }
            });
        }

        // MODO PORTFOLIO HOME: Jerarquía estricta Carril -> Proyectos
        const sections = Array.from(document.querySelectorAll('.portfolio-section'))
            .filter(sec => {
                const header = sec.querySelector('.section-header');
                const isHiddenContainer = sec.closest('[style*="display: none"]') !== null;
                return header !== null && !isHiddenContainer;
            });

        if (sections.length === 0) return;

        sections.forEach((sec, sIdx) => {
            const hTitle = sec.querySelector('.section-title, h2');
            let title = hTitle ? hTitle.innerText.trim() : `Sección ${sIdx + 1}`;
            title = title.replace(/\(\d+.*?\)/g, '').trim();

            let sectionId = sec.id || `bitacora-sec-${sIdx + 1}`;
            sec.id = sectionId;

            // Extraer tarjetas de proyectos dentro de este carril
            const cards = Array.from(sec.querySelectorAll('.apple-card, .project-card'))
                .filter(c => !c.classList.contains('disabled-card'));

            const liGroup = document.createElement('li');
            liGroup.className = 'bitacora-toc-group';

            let groupHtml = `
                <a href="#${sectionId}" class="bitacora-toc-link is-carrusel-header" data-target="${sectionId}">
                    <span class="bitacora-toc-title">${title}</span>
                    <span class="bitacora-toc-badge">${cards.length}</span>
                </a>
            `;

            if (cards.length > 0) {
                groupHtml += `<ul class="bitacora-toc-sublist">`;
                cards.forEach((card, cIdx) => {
                    const titleEl = card.querySelector('.title, h3, h4');
                    let cardTitle = titleEl ? titleEl.innerText.trim() : `Proyecto ${cIdx + 1}`;
                    if (cardTitle.length > 28) cardTitle = cardTitle.substring(0, 26) + '...';

                    let cardId = card.id;
                    if (!cardId) {
                        const slug = cardTitle.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
                        cardId = `card-${slug || (sIdx + '-' + cIdx)}`;
                        card.id = cardId;
                    }

                    sectionElements.push({ id: cardId, el: card, isCard: true, parentId: sectionId });

                    groupHtml += `
                        <li class="bitacora-toc-subitem">
                            <a href="#${cardId}" class="bitacora-toc-sublink" data-target="${cardId}" title="${titleEl ? titleEl.innerText.trim() : cardTitle}">
                                ${cardTitle}
                            </a>
                        </li>
                    `;
                });
                groupHtml += `</ul>`;
            }

            liGroup.innerHTML = groupHtml;
            list.appendChild(liGroup);
            sectionElements.push({ id: sectionId, el: sec, isCard: false });
        });
    } else {
        // MODO PÁGINAS GENERALES: Agrupación H2 -> H3 / Cards
        const h2Elements = Array.from(mainEl.querySelectorAll('h2, .macro-phase-card'))
            .filter(el => {
                if (el.closest('.hero, .app-header-island, .bitacora-lightbox, .bitacora-drawer, footer')) return false;
                return el.innerText.trim().length > 2;
            });

        if (h2Elements.length < 2) {
            tocContainer.remove();
            return;
        }

        h2Elements.forEach((h2, idx) => {
            let title = h2.querySelector('.macro-phase-title') ? h2.querySelector('.macro-phase-title').innerText.trim() : h2.innerText.trim().split('\n')[0];
            if (title.length > 36) title = title.substring(0, 34) + '...';

            let secId = h2.id || `bitacora-sec-${idx + 1}`;
            h2.id = secId;
            sectionElements.push({ id: secId, el: h2, isCard: false });

            // Buscar H3 hermanos antes del siguiente H2
            let subitems = [];
            let next = h2.nextElementSibling;
            while (next && next.tagName !== 'H2' && !next.classList.contains('macro-phase-card')) {
                if (next.tagName === 'H3') {
                    subitems.push(next);
                } else {
                    subitems.push(...Array.from(next.querySelectorAll('h3')));
                }
                next = next.nextElementSibling;
            }

            const liGroup = document.createElement('li');
            liGroup.className = 'bitacora-toc-group';

            let html = `
                <a href="#${secId}" class="bitacora-toc-link is-carrusel-header" data-target="${secId}">
                    <span class="bitacora-toc-title">${title}</span>
                </a>
            `;

            if (subitems.length > 0) {
                html += `<ul class="bitacora-toc-sublist">`;
                subitems.forEach((sub, sIdx) => {
                    let subTitle = sub.innerText.trim().split('\n')[0];
                    if (subTitle.length > 28) subTitle = subTitle.substring(0, 26) + '...';
                    let subId = sub.id || `${secId}-sub-${sIdx + 1}`;
                    sub.id = subId;
                    sectionElements.push({ id: subId, el: sub, isCard: true, parentId: secId });

                    html += `
                        <li class="bitacora-toc-subitem">
                            <a href="#${subId}" class="bitacora-toc-sublink" data-target="${subId}">
                                ${subTitle}
                            </a>
                        </li>
                    `;
                });
                html += `</ul>`;
            }

            liGroup.innerHTML = html;
            list.appendChild(liGroup);
        });
    }

    if (sectionElements.length < 2) {
        tocContainer.remove();
        return;
    }

    // INTERACCIÓN DE CLIC INTELIGENTE EN SUBLINKS (DESPLAZAMIENTO DUAL: HORIZONTAL EN TRACK + VERTICAL EN PÁGINA)
    list.addEventListener('click', (e) => {
        const sublink = e.target.closest('.bitacora-toc-sublink');
        if (sublink) {
            e.preventDefault();
            const targetId = sublink.getAttribute('data-target');
            const targetEl = document.getElementById(targetId);
            if (targetEl) {
                // Si la tarjeta está dentro de un carrusel horizontal, sincronizar desplazamiento horizontal
                const track = targetEl.closest('.carousel-track');
                if (track) {
                    const scrollOffset = (targetEl.offsetLeft - track.offsetLeft) - (track.clientWidth / 2) + (targetEl.clientWidth / 2);
                    track.scrollTo({ left: Math.max(0, scrollOffset), behavior: 'smooth' });
                }

                // Desplazamiento vertical suave
                targetEl.scrollIntoView({ behavior: 'smooth', block: 'center' });

                // Destello visual de foco en la tarjeta
                targetEl.classList.remove('bitacora-card-target-focus');
                void targetEl.offsetWidth; // force reflow
                targetEl.classList.add('bitacora-card-target-focus');
                setTimeout(() => targetEl.classList.remove('bitacora-card-target-focus'), 1800);

                // Estado activo
                list.querySelectorAll('.bitacora-toc-sublink').forEach(s => s.classList.remove('is-active'));
                sublink.classList.add('is-active');

                // Asegurar que el padre esté resaltado
                const group = sublink.closest('.bitacora-toc-group');
                if (group) {
                    list.querySelectorAll('.bitacora-toc-link').forEach(l => l.classList.remove('is-active'));
                    group.querySelector('.bitacora-toc-link')?.classList.add('is-active');
                }
            }
        }
    });

    const links = list.querySelectorAll('.bitacora-toc-link');
    const sublinks = list.querySelectorAll('.bitacora-toc-sublink');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.id;
                const matchObj = sectionElements.find(s => s.id === id);

                if (matchObj && matchObj.isCard) {
                    sublinks.forEach(sl => {
                        if (sl.getAttribute('data-target') === id) {
                            sl.classList.add('is-active');
                        } else {
                            sl.classList.remove('is-active');
                        }
                    });
                    if (matchObj.parentId) {
                        links.forEach(l => {
                            if (l.getAttribute('data-target') === matchObj.parentId) {
                                l.classList.add('is-active');
                            } else {
                                l.classList.remove('is-active');
                            }
                        });
                    }
                } else {
                    links.forEach(l => {
                        if (l.getAttribute('data-target') === id) {
                            l.classList.add('is-active');
                        } else {
                            l.classList.remove('is-active');
                        }
                    });
                }
            }
        });
    }, { rootMargin: '-10% 0px -65% 0px' });

    sectionElements.forEach(s => {
        if (s.el) observer.observe(s.el);
    });

    let isTocVisible = false;
    function updateToc(scrollY) {
        if (!isTocVisible && scrollY > 300) {
            isTocVisible = true;
            tocContainer.classList.add('is-visible');
        } else if (isTocVisible && scrollY < 190) {
            isTocVisible = false;
            tocContainer.classList.remove('is-visible');
        }
    }

    subscribeScroll(updateToc);
    updateToc(window.scrollY || window.pageYOffset || 0);
}
window.initSmartTOC = initSmartTOC;

// 2. SPECULAR SPOTLIGHT & 3D TILT EN TARJETAS
function initCardSpotlightTilt() {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    const cards = document.querySelectorAll('.apple-card, .project-card');
    cards.forEach(card => {
        let isHovered = false;

        card.addEventListener('mouseenter', () => { isHovered = true; }, { passive: true });
        card.addEventListener('mouseleave', () => {
            isHovered = false;
            card.style.transform = '';
            card.style.removeProperty('--mouse-x');
            card.style.removeProperty('--mouse-y');
        }, { passive: true });

        card.addEventListener('mousemove', (e) => {
            if (!isHovered) return;
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            card.style.setProperty('--mouse-x', `${x}px`);
            card.style.setProperty('--mouse-y', `${y}px`);

            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            const rotateX = ((y - centerY) / centerY) * -3;
            const rotateY = ((x - centerX) / centerX) * 3;
            card.style.transform = `perspective(1000px) rotateX(${rotateX.toFixed(2)}deg) rotateY(${rotateY.toFixed(2)}deg) translateY(-2px)`;
        }, { passive: true });
    });
}

// 3. CONTADORES PMO & KPI BADGE PULSE (COUNT-UP)
function initKPICounters() {
    const counters = document.querySelectorAll('.section-counter, .filter-count, [data-count]');
    if (!counters.length) return;

    const observer = new IntersectionObserver((entries, obs) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const el = entry.target;
                const rawVal = el.getAttribute('data-count') || el.innerText.trim();
                const targetVal = parseInt(rawVal, 10);
                if (!isNaN(targetVal) && targetVal > 0) {
                    const duration = 600;
                    const startTime = performance.now();

                    function updateCount(currentTime) {
                        const elapsed = currentTime - startTime;
                        const progress = Math.min(elapsed / duration, 1);
                        const current = Math.floor(targetVal * (progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress)));
                        el.innerText = current;
                        if (progress < 1) {
                            requestAnimationFrame(updateCount);
                        } else {
                            el.innerText = targetVal;
                        }
                    }
                    requestAnimationFrame(updateCount);
                } else if (!isNaN(targetVal) && targetVal === 0) {
                    el.innerText = '0';
                }
                obs.unobserve(el);
            }
        });
    }, { threshold: 0.1 });

    counters.forEach(el => observer.observe(el));
}

// 4. MODO PRESENTACIÓN ZEN (FULL-SCREEN FOCUS MODE)
function initZenMode() {
    let badge = document.getElementById('bitacora-zen-badge');
    if (!badge) {
        badge = document.createElement('div');
        badge.id = 'bitacora-zen-badge';
        badge.className = 'bitacora-zen-badge';
        badge.innerHTML = `
            <span style="color: var(--lda-red); font-size: 0.9rem;">🧘</span>
            <span>Modo Presentación Zen</span>
            <span style="padding: 2px 6px; background: var(--bg-page); border: 1px solid var(--border-color); border-radius: 4px; font-size: 0.7rem; font-family: monospace;">Z / ESC</span>
        `;
        badge.addEventListener('click', () => BitacoraUI.toggleZenMode());
        document.body.appendChild(badge);
    }
}

BitacoraUI.toggleZenMode = function() {
    const isZen = document.body.classList.toggle('bitacora-zen-mode');
    if (isZen) {
        BitacoraUI.toast('Modo Presentación Zen activado (Pulsa Z o ESC para salir)', 'info', 2400);
    } else {
        BitacoraUI.toast('Modo Presentación desactivado', 'info', 1600);
    }
};

// 5. FOCUS LIGHTBOX PARA DIAGRAMAS Y TABLAS
function initFocusLightbox() {
    let lightbox = document.getElementById('bitacora-lightbox');
    if (!lightbox) {
        lightbox = document.createElement('div');
        lightbox.id = 'bitacora-lightbox';
        lightbox.className = 'bitacora-lightbox';
        lightbox.innerHTML = `
            <div class="bitacora-lightbox-card" role="dialog" aria-modal="true">
                <div class="bitacora-lightbox-header">
                    <span id="bitacora-lightbox-title">Detalle de Análisis</span>
                    <button class="bitacora-lightbox-close" id="btn-close-lightbox" title="Cerrar (Esc)">×</button>
                </div>
                <div class="bitacora-lightbox-body" id="bitacora-lightbox-body"></div>
            </div>
        `;
        document.body.appendChild(lightbox);

        lightbox.querySelector('#btn-close-lightbox')?.addEventListener('click', () => {
            lightbox.classList.remove('is-open');
        });
        lightbox.addEventListener('click', (e) => {
            if (e.target === lightbox) lightbox.classList.remove('is-open');
        });
    }

    const tables = document.querySelectorAll('table:not(.no-expand)');
    tables.forEach(table => {
        if (table.rows.length >= 3 && table.parentElement) {
            const parent = table.parentElement;
            if (!parent.classList.contains('expandable-block') && !parent.classList.contains('bitacora-lightbox-body')) {
                parent.classList.add('expandable-block');
                const btn = document.createElement('button');
                btn.className = 'bitacora-expand-btn';
                btn.innerHTML = `<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg> Expandir Vista`;
                btn.addEventListener('click', (e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    const clone = table.cloneNode(true);
                    BitacoraUI.openLightbox(clone, 'Vista Ampliada • Tabla de Datos');
                });
                parent.appendChild(btn);
            }
        }
    });
}

BitacoraUI.openLightbox = function(nodeOrHtml, title = 'Vista Ampliada') {
    const lightbox = document.getElementById('bitacora-lightbox');
    if (!lightbox) return;
    const body = document.getElementById('bitacora-lightbox-body');
    const titleEl = document.getElementById('bitacora-lightbox-title');
    if (titleEl) titleEl.innerText = title;
    if (body) {
        body.innerHTML = '';
        if (typeof nodeOrHtml === 'string') {
            body.innerHTML = nodeOrHtml;
        } else {
            body.appendChild(nodeOrHtml);
        }
    }
    lightbox.classList.add('is-open');
};

// 6. MICRO-INTERACCIÓN QUICK COPY
function initQuickCopy() {
    const copyBlocks = document.querySelectorAll('pre, .spec-box, .kpi-copyable');
    copyBlocks.forEach(block => {
        if (block.querySelector('.bitacora-copy-badge')) return;
        block.style.position = 'relative';
        const badge = document.createElement('button');
        badge.className = 'bitacora-copy-badge';
        badge.innerHTML = `<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg> Copiar`;
        badge.addEventListener('click', (e) => {
            e.stopPropagation();
            const text = block.innerText.replace('Copiar', '').trim();
            navigator.clipboard.writeText(text).then(() => {
                BitacoraUI.toast('Copiado al portapapeles', 'success');
            });
        });
        block.appendChild(badge);
    });
}

// 7. ESTIMADOR DE TIEMPO DE LECTURA Y ESTADO DOCUMENTAL
function initReadingTimeMeta() {
    if (document.body.classList.contains('home-dashboard')) return;
    const hero = document.querySelector('.hero, header.app-hero');
    if (!hero || hero.querySelector('.bitacora-reading-meta')) return;

    const mainEl = document.querySelector('main') || document.body;
    const wordCount = mainEl.innerText.split(/\s+/).filter(Boolean).length;
    if (wordCount < 180) return;

    const minutes = Math.max(1, Math.ceil(wordCount / 220));
    const meta = document.createElement('div');
    meta.className = 'bitacora-reading-meta';
    meta.innerHTML = `
        <span class="bitacora-meta-pill">
            <span class="bitacora-meta-dot"></span> Octubre 2026 • Validado
        </span>
        <span style="opacity: 0.4;">|</span>
        <span class="bitacora-meta-pill">
            <span>⏱️</span> ~${minutes} min de lectura
        </span>
    `;
    hero.appendChild(meta);
}

// 8. SELECTOR DE DENSIDAD DE INTERFAZ
function initDensityPreference() {
    const saved = localStorage.getItem('bitacora-density') || 'comfortable';
    document.body.setAttribute('data-density', saved);
}

BitacoraUI.toggleDensity = function() {
    const current = document.body.getAttribute('data-density') || 'comfortable';
    const next = current === 'comfortable' ? 'compact' : 'comfortable';
    document.body.setAttribute('data-density', next);
    localStorage.setItem('bitacora-density', next);
    BitacoraUI.toast(`Densidad ${next === 'compact' ? 'Compacta' : 'Confortable'} activada`, 'info', 1800);
};

// 6b. FILTRO REACTIVO EN TIEMPO REAL EN HUBS
function initHubLiveFilter() {
    const filterBars = document.querySelectorAll('.hub-live-filter-bar');
    if (!filterBars.length) return;

    filterBars.forEach(bar => {
        const chips = bar.querySelectorAll('.hub-filter-chip');
        const container = bar.closest('.container, main') || document.body;
        const targetCards = container.querySelectorAll('.carousel-track .apple-card, .bento-grid .apple-card, .cards-grid .apple-card, .apple-grid .apple-card, .carousel-track > a, .carousel-track > div');

        chips.forEach(chip => {
            chip.addEventListener('click', () => {
                chips.forEach(c => c.classList.remove('active'));
                chip.classList.add('active');

                const filterKey = (chip.getAttribute('data-filter') || chip.innerText).toLowerCase().trim();

                let visibleCount = 0;
                targetCards.forEach(card => {
                    const text = (card.innerText || '').toLowerCase();
                    const tags = (card.getAttribute('data-tags') || '').toLowerCase();
                    const filterAttr = (card.getAttribute('data-filter') || '').toLowerCase();

                    const isMatch = filterKey === 'all' || filterKey === 'todos' ||
                                    text.includes(filterKey) ||
                                    tags.includes(filterKey) ||
                                    filterAttr.includes(filterKey);

                    if (isMatch) {
                        card.style.display = '';
                        card.style.opacity = '1';
                        visibleCount++;
                    } else {
                        card.style.display = 'none';
                    }
                });

                const track = container.querySelector('.carousel-track');
                if (track && typeof updateCarouselButtons === 'function') {
                    updateCarouselButtons(track);
                }
            });
        });
    });
}

// 9. DRAWER LATERAL DE VISITAS RECIENTES (NAVEGACIÓN RÁPIDA)
function formatRelativeTime(ts) {
    if (!ts) return 'Reciente';
    const diff = Math.floor((Date.now() - ts) / 1000);
    if (diff < 60) return 'Hace unos segundos';
    if (diff < 3600) return `Hace ${Math.floor(diff / 60)} min`;
    if (diff < 86400) return `Hace ${Math.floor(diff / 3600)} h`;
    const d = new Date(ts);
    return `Hoy ${d.getHours().toString().padStart(2, '0')}:${d.getMinutes().toString().padStart(2, '0')}`;
}

function detectPageCategory(url) {
    const u = (url || '').toLowerCase();
    if (u.includes('ficha_ejecutiva')) return 'Ficha Ejecutiva PMO';
    if (u.includes('press_release')) return 'Comunicado Oficial';
    if (u.includes('contexto_proyecto')) return 'Contexto Estratégico';
    if (u.includes('cuaderno de bitacora') && u.endsWith('index.html')) return 'Portada Portfolio';
    if (u.includes('gestion de usuarios') || u.includes('usuarios')) return 'Gestión Usuarios';
    if (u.includes('gobierno del dato') || u.includes('gobierno de informacion')) return 'Gobierno Dato';
    if (u.includes('siniestros')) return 'Siniestros Motor';
    if (u.includes('telefonia') || u.includes('genesis')) return 'Telefonía CX';
    if (u.includes('crm operacional')) return 'CRM Salesforce';
    if (u.includes('ia voz') || u.includes('lupe')) return 'IA Voz & Chat';
    if (u.includes('transformacion hog')) return 'Hogar HomeServe';
    if (u.includes('transformacion sal')) return 'Salud HNA';
    if (u.includes('transformacion agi')) return 'Transformación Agile';
    return 'Documento';
}

function initRecentProjectsDrawer() {
    try {
        const titleEl = document.querySelector('h1') || document.querySelector('title');
        let rawTitle = titleEl ? titleEl.innerText.replace(/<[^>]+>/g, '').trim().split('\n')[0] : document.title;
        rawTitle = rawTitle.replace(/^(Entidad Aseguradora|Organización)\s*[-·|]?\s*/i, '').trim();
        const currentUrl = window.location.pathname;

        if (currentUrl.endsWith('.html') && !currentUrl.includes('export_estatico')) {
            let history = JSON.parse(localStorage.getItem('bitacora-recent-history') || '[]');
            history = history.filter(item => item.url !== currentUrl);
            history.unshift({
                url: currentUrl,
                title: rawTitle,
                category: detectPageCategory(currentUrl),
                time: Date.now()
            });
            localStorage.setItem('bitacora-recent-history', JSON.stringify(history.slice(0, 10)));
        }
    } catch (_) {}

    let drawerBackdrop = document.getElementById('bitacora-drawer-backdrop');
    if (!drawerBackdrop) {
        drawerBackdrop = document.createElement('div');
        drawerBackdrop.id = 'bitacora-drawer-backdrop';
        drawerBackdrop.className = 'bitacora-drawer-backdrop';
        drawerBackdrop.innerHTML = `
            <div class="bitacora-drawer" role="dialog" aria-modal="true" aria-labelledby="recent-drawer-title">
                <div class="bitacora-drawer-header">
                    <div>
                        <span class="bitacora-drawer-kicker">HISTORIAL DE NAVEGACIÓN</span>
                        <div class="bitacora-drawer-title" id="recent-drawer-title">
                            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="color: var(--lda-red); vertical-align: -2px; margin-right: 6px;">
                                <circle cx="12" cy="12" r="10"></circle>
                                <polyline points="12 6 12 12 16 14"></polyline>
                            </svg>
                            <span>Visitas Recientes</span>
                        </div>
                        <div class="bitacora-drawer-subinfo">Acceso rápido a las últimas páginas consultadas en la sesión</div>
                    </div>
                    <button id="btn-close-drawer" class="bitacora-drawer-close" aria-label="Cerrar">&times;</button>
                </div>
                <div class="bitacora-drawer-body" id="bitacora-drawer-body"></div>
                <div class="bitacora-drawer-footer">
                    <button id="btn-clear-recent-history" class="bitacora-drawer-clear-btn" type="button">
                        Limpiar visitas recientes
                    </button>
                </div>
            </div>
        `;
        document.body.appendChild(drawerBackdrop);

        drawerBackdrop.querySelector('#btn-close-drawer')?.addEventListener('click', () => {
            drawerBackdrop.classList.remove('is-open');
        });
        drawerBackdrop.addEventListener('click', (e) => {
            if (e.target === drawerBackdrop) drawerBackdrop.classList.remove('is-open');
        });
        drawerBackdrop.querySelector('#btn-clear-recent-history')?.addEventListener('click', () => {
            localStorage.removeItem('bitacora-recent-history');
            BitacoraUI.renderRecentItems();
            BitacoraUI.toast('Historial de visitas limpiado', 'info', 1600);
        });
    }
}

BitacoraUI.renderRecentItems = function() {
    const body = document.getElementById('bitacora-drawer-body');
    if (!body) return;
    try {
        const history = JSON.parse(localStorage.getItem('bitacora-recent-history') || '[]');
        if (history.length === 0) {
            body.innerHTML = `
                <div class="bitacora-drawer-empty">
                    <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="color: var(--text-sec); margin-bottom: 12px;">
                        <circle cx="12" cy="12" r="10"></circle>
                        <polyline points="12 6 12 12 16 14"></polyline>
                    </svg>
                    <div style="font-weight: 700; color: var(--text-main); margin-bottom: 4px;">No hay visitas registradas</div>
                    <div style="font-size: 0.85rem; color: var(--text-sec); line-height: 1.4;">Las páginas que consultes en el portal se registrarán aquí para darte acceso directo instantáneo.</div>
                </div>
            `;
        } else {
            body.innerHTML = history.map(item => `
                <a href="${item.url}" class="bitacora-drawer-item">
                    <div class="bitacora-drawer-item-icon">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                            <polyline points="14 2 14 8 20 8"></polyline>
                            <line x1="16" y1="13" x2="8" y2="13"></line>
                            <line x1="16" y1="17" x2="8" y2="17"></line>
                        </svg>
                    </div>
                    <div class="bitacora-drawer-item-content">
                        <div class="bitacora-drawer-item-top">
                            <span class="bitacora-drawer-item-badge">${item.category || 'Página'}</span>
                            <span class="bitacora-drawer-item-time">${formatRelativeTime(item.time)}</span>
                        </div>
                        <div class="bitacora-drawer-item-title">${item.title}</div>
                    </div>
                    <div class="bitacora-drawer-item-arrow">&rarr;</div>
                </a>
            `).join('');
        }
    } catch (_) {}
};

BitacoraUI.toggleRecentDrawer = function() {
    let drawerBackdrop = document.getElementById('bitacora-drawer-backdrop');
    if (!drawerBackdrop) {
        initRecentProjectsDrawer();
        drawerBackdrop = document.getElementById('bitacora-drawer-backdrop');
    }
    if (!drawerBackdrop) return;
    BitacoraUI.renderRecentItems();
    drawerBackdrop.classList.toggle('is-open');
};

// ==========================================
// 13. INICIALIZACIÓN GLOBAL
// ==========================================
function bootstrapBitacora() {
    initTheme();
    initDensityPreference();
    setTimeout(initCarousels, 80);
    initBreadcrumbLogic();
    initDynamicBreadcrumb();
    initReadingProgressBar();
    initQuickActions();
    initIslandLiquidGlass();
    initKeyboardShortcutsModal();
    initPageTransitions();
    initSmoothAnchors();
    initSmartTOC();
    initCardSpotlightTilt();
    initKPICounters();
    initZenMode();
    initFocusLightbox();
    initQuickCopy();
    initReadingTimeMeta();
    initHubLiveFilter();
    initRecentProjectsDrawer();
    window.bitacoraSearchInstance = new BitacoraSearch();
    initGlobalScrollEngine();
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', bootstrapBitacora);
} else {
    bootstrapBitacora();
}

window.addEventListener('resize', initCarousels);
