import os
import re

base_dir = r"c:\Users\ldaecc\.gemini\antigravity\scratch\Documentacion\02_Proyectos"
script_content = """
    <script>
        // BREADCRUMB MANAGER - SMART COLLAPSE
        function initBreadcrumbLogic() {
            const breadcrumb = document.querySelector('.nav-breadcrumb');
            if (!breadcrumb) return;

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
                    link.textContent = item.textContent || item.title || 'Nivel ' + (index + 2);
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
                newSep.textContent = '';
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
        document.addEventListener('DOMContentLoaded', initBreadcrumbLogic);
    </script>"""

count = 0
for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith(".html"):
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8") as file:
                content = file.read()
                
            if "nav-breadcrumb" in content and "initBreadcrumbLogic" not in content and "breadcrumb_manager.js" not in content:
                content = content.replace("</body>", script_content + "\n</body>")
                with open(path, "w", encoding="utf-8") as file:
                    file.write(content)
                count += 1

print(f"Updated {count} files.")
