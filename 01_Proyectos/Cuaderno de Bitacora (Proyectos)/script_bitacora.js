/**
 * SCRIPT BITÁCORA - Cuaderno de Bitácora
 * Funcionalidades transversales compartidas
 */

// Theme Management
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

document.addEventListener('DOMContentLoaded', () => {
    initTheme();
});
