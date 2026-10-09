---
trigger: always_on
---

---
name: reglas-globales-agentes
description: >
  Protocolo obligatorio que TODOS los agentes deben seguir antes de crear
  o editar notas en el vault.
updated: 2026-01-15
---

# 🚨 Reglas Globales para Agentes

> [!CAUTION]
> **OBLIGATORIO**: Todo agente debe seguir este protocolo antes de crear o editar notas.

---

## 🗺️ Índice del Vault

> [!IMPORTANT] Mantén el Índice Actualizado
> El archivo `[[Índice del Vault]]` es el mapa central del vault. **Todos los agentes deben:**

### Al iniciar una sesión:
```python
# Lee el índice para entender la estructura actual:
leer_nota("Índice del Vault.md")
```

### Al crear notas importantes:
Si creas una nota que representa:
- Un **nuevo proyecto** → Añádelo a "Proyectos Activos"
- Una **nueva área de conocimiento** → Añádelo a "Conocimiento"
- Un **nuevo recurso importante** → Añádelo a "Recursos"

```python
# Después de crear la nota, actualiza el índice:
agregar_a_nota(
    nombre_archivo="Índice del Vault.md",
    contenido="- [[ruta/Nueva Nota|Nombre]] - Descripción breve",
    al_final=False  # Añadir en la sección correcta
)
# O usa editar_nota() para ubicarlo en la sección exacta
```

### Al mover/eliminar notas:
- Verifica si la nota aparece en el Índice
- Actualiza o elimina la referencia según corresponda
- Actualiza el campo `updated:` del Índice

---

## Protocolo Antes de Crear Notas

### Paso 1: Verificar Contexto del Vault
```python
# SIEMPRE ejecuta primero:
leer_contexto_vault()
leer_nota("Índice del Vault.md")  # Para visión global
```
Esto te dará la estructura de carpetas, plantillas disponibles y convenciones actuales.

### Paso 2: Verificar Ubicación Correcta
```python
# Usa esta tool para confirmar dónde debe ir la nota:
sugerir_ubicacion(
    titulo="Título de la nota",
    contenido="Breve descripción del contenido",
    etiquetas="etiqueta1, etiqueta2"
)
```

### Paso 3: Confirmar con el Usuario
**ANTES de crear cualquier nota**, comunica al usuario:
1. La ubicación propuesta
2. La estructura de archivos que crearás
3. **Espera confirmación explícita** ("sí", "ok", "adelante")

Ejemplo:
> "Voy a crear la nota en `02_Proyectos/NuevoProyecto.md`. ¿Confirmas?"

### Paso 4: Usar Frontmatter Real
- **NUNCA** inventes valores de frontmatter
- **NUNCA** dejes placeholders sin procesar (`2026-01-15`, `{{description}}`)
- **SIEMPRE** usa valores reales para `type`, `tags`, `created`
- **SIEMPRE** consulta las etiquetas existentes con `obtener_lista_etiquetas()`

---

## 📚 Guías de Referencia del Vault

> [!TIP] Documentación de Estilo
> Antes de crear o editar notas, consulta estas guías en `05_Recursos/Obsidian/`:

| Guía | Ruta | Contenido |
|------|------|-----------|
| **Markdown** | `[[05_Recursos/Obsidian/Markdown]]` | Sintaxis Markdown, enlaces, embebidos, bloques de código |
| **Callouts** | `[[05_Recursos/Obsidian/Callouts y Admonitions]]` | Tipos de callouts, bloques plegables, cuándo usarlos |
| **Propiedades YAML** | `[[05_Recursos/Obsidian/Propiedades y Metadatos]]` | Frontmatter estándar, campos obligatorios, reglas de edición |
| **Buenas Prácticas** | `[[05_Recursos/Obsidian/Buenas Prácticas de Uso del Vault]]` | Enlaces vs tags, MOCs, raíz vacía, interacción con IA |

---

## Ubicaciones Estándar del Vault

| Tipo de Contenido | Carpeta |
|-------------------|---------|
| Notas sin procesar | `01_Inbox/` |
| Proyectos activos | `02_Proyectos/` |
| Conocimiento permanente | `03_Conocimiento/` |
| Reuniones y dailies | `04_Reuniones/` |
| Recursos y referencias | `05_Recursos/` |
| Plantillas | `ZZ_Plantillas/` |

---

## Checklist Pre-Creación

Antes de llamar a `crear_nota()`:
- [ ] ¿Leí el `[[Índice del Vault]]` para entender la estructura?
- [ ] ¿Ejecuté `leer_contexto_vault()`?
- [ ] ¿Verifiqué la ubicación con `sugerir_ubicacion()`?
- [ ] ¿Confirmé con el usuario la ubicación propuesta?
- [ ] ¿El frontmatter usa valores reales, no placeholders?
- [ ] ¿El `type` corresponde al contenido real?
- [ ] ¿Las etiquetas existen o son coherentes con el vault?
- [ ] ¿Consulté las [[05_Recursos/Obsidian/Propiedades y Metadatos|guías de estilo]] si tengo dudas?

## Checklist Post-Creación

Después de crear notas importantes:
- [ ] ¿Debo añadir esta nota al `[[Índice del Vault]]`?
- [ ] ¿Actualicé el campo `updated:` del Índice si lo modifiqué?

---

## Regla de Oro de Edición

Cuando uses `editar_nota()`:
1. **PRIMERO** lee la nota con `leer_nota()`
2. El `nuevo_contenido` debe ser el **ARCHIVO COMPLETO**
3. **REEMPLAZA** el bloque YAML existente, no lo dupliques
4. Un solo bloque `---` al principio
5. Un solo título `#` después del YAML

> [!WARNING] Más detalles en [[05_Recursos/Obsidian/Propiedades y Metadatos#🤖 Reglas Críticas para Agentes]]

---

## Tipos de Contenido Válidos

| `type` | Uso |
|--------|-----|
| `diario` | Entradas de diario personal |
| `standup` | Resúmenes de actividad diaria |
| `semanario` | Revisiones semanales |
| `resumen` | Resúmenes de artículos/vídeos/libros |
| `reflexión` | Reflexiones personales |
| `doc-módulo` | Documentación de módulos Python |
| `doc-api` | Documentación de endpoints API |
| `adr` | Architecture Decision Records |
| `doc-índice` | Índices de documentación |
| `prompt` | Prompts de LLM |
| `changelog` | Historial de cambios |
| `todo` | Listas de tareas |
| `habit-tracker` | Seguimiento de hábitos |
| `nota` | Notas genéricas de conocimiento |
| `referencia` | Guías y documentación de referencia |
| `recurso` | Recursos externos y enlaces útiles |

---

## 🛡️ Protocolo Obligatorio de Anonimización para Git y GitHub

> [!CAUTION]
> **REGLA ABSOLUTA DE PRIVACIDAD PARA GIT**:
> Al preparar commits, ramas, PRs, changelogs o cualquier publicación en Git/GitHub:
> 1. **NUNCA** incluir nombres reales de proyectos, clientes, empleados ni marcas identificativas de la empresa.
> 2. **SIEMPRE** referirse a los proyectos de manera generalizada: **"Proyecto 1"**, **"Proyecto 2"**, **"Iniciativa A"**, **"Iniciativa B"**.
> 3. Referirse a la empresa únicamente como **"Entidad"**, **"Organización"** o **"Compañía Aseguradora"**.
> 4. Antes de hacer commit o push, ejecutar la auditoría de la skill `git-publisher`:
>    `python .agent/skills/git-publisher/scripts/git_privacy_checker.py --check-staged`

---

## 🌟 Protocolo Obligatorio de Benchmarking Open-Source (>1.000 ⭐)

> [!IMPORTANT]
> **REGLA OBLIGATORIA PARA NUEVOS PROYECTOS O SERVICIOS**:
> Antes de diseñar o generar cualquier nuevo servicio, interfaz de usuario o módulo:
> 1. **ACTIVAR OBLIGATORIAMENTE** la skill `repo-benchmark`.
> 2. Buscar en GitHub proyectos de código abierto con **más de 1.000 estrellas** relacionados con el objetivo técnico y funcional.
> 3. Extraer e implementar las mejores prácticas de **interfaz (UI)**, **usabilidad (UX)**, accesibilidad, retroalimentación al usuario y diseño ergonómico.
> 4. Documentar los aprendizajes y aplicarlos siempre respetando la privacidad de `git-publisher`.