import re
import sys

path = r'c:\personal\Proyectos Antigravity\Backup Proyecto Cuadrrno de Bitacora\Documentacion\02_Proyectos\IA Area Personas\plan_accion_m365.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

count = 0
def replacer(match):
    global count
    count += 1
    return '<div style="display: flex; flex-direction: column; min-width: 170px; gap: 4px;">\n                                        <div style="display: flex; justify-content: space-between; font-size: 0.65rem; color: var(--text-sec); padding: 0 4px; text-transform: uppercase; font-weight: bold;"><span>Poco</span><span>Mucho</span></div>\n                                        <div style="display: flex; gap: 5px;">'

new_content = re.sub(r'<div style="display: flex; gap: 5px; min-width: 170px;">', replacer, content)

def close_replacer(match):
    return match.group(1) + '\n                                    </div>' + match.group(2)

new_content = re.sub(r'(>5</span>\s*</div>)(\s*</div>)', close_replacer, new_content)

with open(path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f'Processed {count} blocks.')
