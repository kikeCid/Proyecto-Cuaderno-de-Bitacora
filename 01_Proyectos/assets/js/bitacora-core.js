/**
 * BITÁCORA CORE JS - Motor Unificado del Cuaderno de Bitácora
 * Incluye: Control de Temas, Carruseles Táctiles, Migas Dinámicas y Buscador Spotlight (Ctrl+K)
 */

// ==========================================
// 1. CONTROL DE TEMAS (DARK / LIGHT)
// ==========================================
function toggleTheme() {
    const checkbox = document.getElementById('theme-checkbox');
    if (!checkbox) return;
    const isDark = checkbox.checked;

    if (isDark) {
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('theme', 'dark');
    } else {
        document.documentElement.setAttribute('data-theme', 'light');
        localStorage.setItem('theme', 'light');
    }
}

function initTheme() {
    const savedTheme = localStorage.getItem('theme');
    const checkbox = document.getElementById('theme-checkbox');

    if (savedTheme === 'dark') {
        document.documentElement.setAttribute('data-theme', 'dark');
        if (checkbox) checkbox.checked = true;
    } else {
        document.documentElement.setAttribute('data-theme', 'light');
        if (checkbox) checkbox.checked = false;
    }
}

// ==========================================
// 2. CONTROL DE CARRUSELES Y DESPLAZAMIENTO
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

        // Soporte táctil / arrastre suave (Touch swipe)
        let isDown = false;
        let startX;
        let scrollLeft;

        track.addEventListener('mousedown', (e) => {
            isDown = true;
            track.classList.add('active');
            startX = e.pageX - track.offsetLeft;
            scrollLeft = track.scrollLeft;
        });

        track.addEventListener('mouseleave', () => { isDown = false; });
        track.addEventListener('mouseup', () => { isDown = false; });

        track.addEventListener('mousemove', (e) => {
            if (!isDown) return;
            e.preventDefault();
            const x = e.pageX - track.offsetLeft;
            const walk = (x - startX) * 1.5;
            track.scrollLeft = scrollLeft - walk;
        });
    });
}

// ==========================================
// 3. BREADCRUMBS Y NAVEGACIÓN DINÁMICA
// ==========================================
function initBreadcrumbLogic() {
    const breadcrumb = document.querySelector('.nav-breadcrumb');
    if (!breadcrumb) return;

    // Si ya fue inicializado, evitar duplicación
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

    if (window.scrollY > 50) wrapper.classList.add('compacted');

    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            wrapper.classList.add('compacted');
        } else {
            wrapper.classList.remove('compacted');
        }
    });
}

// ==========================================
// 4. BUSCADOR SPOTLIGHT (CTRL + K)
// ==========================================
class BitacoraSearch {
    constructor() {
        this.index = window.BITACORA_SEARCH_INDEX || [];
        this.backdrop = null;
        this.input = null;
        this.resultsContainer = null;
        this.selectedIndex = -1;
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
                    <input type="text" class="search-input-field" placeholder="Buscar en todos los proyectos y documentos..." aria-label="Buscar">
                    <span class="search-kbd-shortcut">ESC</span>
                </div>
                <div class="search-results-list" id="search-results-list">
                    <div style="padding: 24px; text-align: center; color: var(--text-muted); font-size: 0.9rem;">
                        Escribe para buscar proyectos, actas, licitaciones o arquitecturas...
                    </div>
                </div>
                <div class="search-footer-info">
                    <span>Navega con <b>↑</b> <b>↓</b> y abre con <b>Enter</b></span>
                    <span><b>${this.index.length}</b> documentos indexados</span>
                </div>
            </div>
        `;

        document.body.appendChild(backdrop);
        this.backdrop = backdrop;
        this.input = backdrop.querySelector('.search-input-field');
        this.resultsContainer = backdrop.querySelector('.search-results-list');
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

        // Entrada de texto
        this.input.addEventListener('input', (e) => {
            this.handleSearch(e.target.value.trim());
        });

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

    open() {
        this.backdrop.classList.add('active');
        this.input.value = '';
        this.selectedIndex = -1;
        this.handleSearch('');
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
                <div style="padding: 24px; text-align: center; color: var(--text-muted); font-size: 0.9rem;">
                    Escribe para buscar proyectos, actas, licitaciones o arquitecturas...
                </div>
            `;
            return;
        }

        const q = query.toLowerCase();
        const terms = q.split(' ').filter(t => t.length > 0);

        // Filtro por relevancia
        const matches = this.index.filter(item => {
            const searchable = `${item.title} ${item.h1} ${item.desc} ${item.project} ${item.category} ${item.kicker}`.toLowerCase();
            return terms.every(term => searchable.includes(term));
        });

        if (matches.length === 0) {
            this.resultsContainer.innerHTML = `
                <div style="padding: 32px 24px; text-align: center; color: var(--text-muted);">
                    <p style="font-weight: 700; margin-bottom: 6px;">No se encontraron resultados para "${query}"</p>
                    <p style="font-size: 0.85rem;">Intenta con palabras clave como "CRM", "licitación", "Perseo" o "LidIA".</p>
                </div>
            `;
            this.selectedIndex = -1;
            return;
        }

        this.selectedIndex = 0;
        this.resultsContainer.innerHTML = matches.slice(0, 15).map((item, idx) => `
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

// INICIALIZACIÓN GLOBAL
document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    setTimeout(initCarousels, 100);
    initBreadcrumbLogic();
    initDynamicBreadcrumb();
    window.bitacoraSearchInstance = new BitacoraSearch();
});

window.addEventListener('resize', initCarousels);
