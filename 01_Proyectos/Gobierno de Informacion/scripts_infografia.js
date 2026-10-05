/* 
    SCRIPTS COMPARTIDOS - INFOGRAFÍA LidIA
    Manejo de temas, navegación y animaciones comunes.
*/

/**
 * Cambia entre tema claro y oscuro
 */
function toggleTheme() {
    const checkbox = document.getElementById('theme-checkbox');
    const isDark = checkbox.checked;

    if (isDark) {
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('lda-theme', 'dark');
    } else {
        document.documentElement.setAttribute('data-theme', 'light');
        localStorage.setItem('lda-theme', 'light');
    }
}

/**
 * Inicializa el tema al cargar la página
 */
function initTheme() {
    const savedTheme = localStorage.getItem('lda-theme');
    const checkbox = document.getElementById('theme-checkbox');

    if (savedTheme === 'dark') {
        document.documentElement.setAttribute('data-theme', 'dark');
        if (checkbox) checkbox.checked = true;
    } else {
        document.documentElement.setAttribute('data-theme', 'light');
        if (checkbox) checkbox.checked = false;
    }
}

/**
 * Animación suave de entrada para elementos cuando entran en el viewport
 */
function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-reveal');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.process-card, .problem-card, .hub-card-premium, .insight-card').forEach(el => {
        el.style.opacity = "0";
        el.style.transform = "translateY(20px)";
        el.style.transition = "opacity 0.6s ease, transform 0.6s ease";
        observer.observe(el);
    });
}

// Estilo dinámico para animaciones de revelado
const style = document.createElement('style');
style.textContent = `
    .animate-reveal {
        opacity: 1 !important;
        transform: translateY(0) !important;
    }
`;
document.head.appendChild(style);

function updateCarouselButtons(track) {
    const container = track.parentElement;
    const btnLeft = container.querySelector('.carousel-btn.left');
    const btnRight = container.querySelector('.carousel-btn.right');

    if (btnLeft && btnRight) {
        if (track.scrollLeft <= 5) {
            btnLeft.classList.add('hidden');
        } else {
            btnLeft.classList.remove('hidden');
        }

        if (Math.ceil(track.scrollLeft) + track.clientWidth >= track.scrollWidth - 5) {
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
    });
}

window.addEventListener('resize', initCarousels);

// Ejecutar al cargar
document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    setTimeout(initCarousels, 100);
    // initScrollAnimations(); // Opcional, dependiendo de si queremos el efecto en todas las páginas
});
