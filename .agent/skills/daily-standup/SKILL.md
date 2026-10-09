---
name: daily-standup
description: >
  Genera resúmenes diarios de actividad basándose en notas modificadas,
  commits de Git, y tareas completadas. Adaptado para equipos de trabajo.
tools: ['read', 'run_command', 'obsidian-mcp']
---

# 📋 Daily Standup

## Cuándo usar esta skill
- Para preparar o documentar la daily del equipo.
- Cuando necesites un resumen de actividad reciente.
- Para generar notas de daily con la plantilla del vault.

## 📋 Antes de Crear Notas

> [!CAUTION]
> **OBLIGATORIO**: Lee y aplica [[REGLAS_GLOBALES]] antes de crear cualquier nota.

## Plantilla del Vault

Usa la plantilla `ZZ_Plantillas/Daily Template.md` estructurada por squads/roles genéricos:
- **Squad 1 (Iniciativas Core)**: Product Owner, Tech Lead
- **Squad 2 (Operaciones y Procesos)**: Product Owner, Líder Técnico
- **Squad 3 (Canales y Atención)**: PM, Especialista Técnico
- **Squad 4 (Datos y Analytics)**: Data Lead, Ingeniero

## Formato de Daily

```markdown
---
aliases:
  - "Daily YYYY-MM-DD"
created: "YYYY-MM-DD HH:mm"
tags:
  - Daily
  - Reunión
---

# Daily YYYY-MM-DD

## Squad 1
- **Rol A**
  - Ayer:
  - Hoy:
- **Rol B**
  - Ayer:
  - Hoy:

## Squad 2
- **Rol C**
  - Ayer:
  - Hoy:
- **Rol D**
  - Ayer:
  - Hoy:

## Bloqueos
- [ ] 

## Notas Adicionales
- [ ] 
```

## Fuentes de Información

### 1. Notas Modificadas (MCP)
Usa `resumen_actividad_reciente(dias=1)` para obtener notas tocadas hoy.

### 2. Commits de Git (Con Anonimización)
```bash
git log --since="1 day ago" --oneline --author="$(git config user.name)"
```

### 3. Tareas Completadas
Busca en notas marcadas con `[x]` modificadas hoy.

## Flujo de Trabajo

1. **Recopila** información de las fuentes.
2. **Agrupa** por iniciativa (Proyecto 1, Proyecto 2, Proyecto 3).
3. **Redacta** entradas concisas y accionables. Si la daily se sube a Git, aplica la skill `git-publisher` para asegurar anonimización.
4. **Guarda** en `04_Reuniones/Daily/` con la fecha como nombre.

## Integración con Proyectos

Enlaza las tareas mencionadas con sus iniciativas correspondientes manteniendo la privacidad:
- [[Proyecto 1]] - Gestión de Clientes
- [[Proyecto 2]] - Contact Center y Telefonía
- [[Proyecto 3]] - Operaciones Core y Siniestros
