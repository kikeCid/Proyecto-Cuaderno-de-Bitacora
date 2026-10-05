import os

directory = r'c:\personal\Proyectos Antigravity\Proyecto Cuadreno de Bitacora\01_Proyectos\IA Area Personas'
target = 'Transformación y Eficiencia'
replacement = 'Transformación y Eficiencia RRHH'

for filename in os.listdir(directory):
    if filename.endswith('.html'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace occurrences that don't already have RRHH
        new_content = content.replace(target + ' RRHH', target) # Normalize first
        new_content = new_content.replace(target, replacement)
        
        if content != new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
