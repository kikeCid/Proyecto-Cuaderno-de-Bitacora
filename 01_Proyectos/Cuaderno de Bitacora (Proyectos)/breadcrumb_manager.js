/**
 * BREADCRUMB MANAGER - SMART COLLAPSE
 * Gestiona el colapso dinámico de las migas de pan para evitar solapamientos.
 */

function initBreadcrumbLogic() {
    const breadcrumb = document.querySelector('.nav-breadcrumb');
    if (!breadcrumb) return;

    const items = Array.from(breadcrumb.querySelectorAll('.nav-breadcrumb-item:not(.current)'));
    const separators = Array.from(breadcrumb.querySelectorAll('.nav-breadcrumb-sep'));
    const currentItem = breadcrumb.querySelector('.nav-breadcrumb-item.current');

    // Si hay más de 3 niveles navegables (sin contar el actual)
    if (items.length > 3) {
        // Elementos a colapsar (los intermedios entre el primero y el previo al actual)
        const toCollapse = items.slice(1, -1);

        // Crear el trigger de colapso (...)
        const trigger = document.createElement('span');
        trigger.className = 'nav-breadcrumb-item collapsed-trigger';
        trigger.innerHTML = '...';
        trigger.title = 'Ver más niveles';

        // Crear el menú desplegable
        const dropdown = document.createElement('div');
        dropdown.className = 'breadcrumb-dropdown';

        toCollapse.forEach((item, index) => {
            const link = document.createElement('a');
            link.href = item.href || '#';
            link.className = 'breadcrumb-dropdown-item';
            link.textContent = item.textContent || item.title || 'Nivel ' + (index + 2);
            dropdown.appendChild(link);

            // Ocultar el item original y su separador correspondiente
            item.style.display = 'none';
            // El separador correspondiente es el que está después del item
            const sepIndex = items.indexOf(item);
            if (separators[sepIndex]) {
                separators[sepIndex].style.display = 'none';
            }
        });

        // Insertar trigger y dropdown
        trigger.appendChild(dropdown);
        items[0].insertAdjacentElement('afterend', trigger);

        // Insertar un separador visible después del trigger si es necesario
        const newSep = document.createElement('span');
        newSep.className = 'nav-breadcrumb-sep';
        newSep.textContent = '›';
        trigger.insertAdjacentElement('afterend', newSep);

        // Lógica de apertura/cierre
        trigger.addEventListener('click', (e) => {
            e.stopPropagation();
            dropdown.classList.toggle('active');
        });

        // Cerrar al hacer clic fuera
        document.addEventListener('click', () => {
            dropdown.classList.remove('active');
        });
    }
}

// Ejecutar al cargar el DOM
document.addEventListener('DOMContentLoaded', initBreadcrumbLogic);
