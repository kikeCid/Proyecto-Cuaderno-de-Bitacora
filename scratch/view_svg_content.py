import glob

for name in ['asistencia-viaje-personas.svg', 'asistencias-informatica.svg', 'poliza-otros-seguros-1.svg', 'gestion-poliza-1.svg', 'taller.svg', 'contacto-telefonico-alt.svg']:
    path = f'01_Proyectos/assets/img/{name}'
    with open(path, encoding='utf-8') as f:
        print(f"=== {name} ===")
        print(f.read())
