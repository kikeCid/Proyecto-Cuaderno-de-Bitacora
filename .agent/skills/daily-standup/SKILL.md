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

Usa la plantilla `ZZ_Plantillas/Daily Template.md` que incluye los equipos:
- **Equipo LidIA**: Gerson, Quique
- **Equipo Maldonado**: Kiko, Manu
- **Equipo Kitt**: Alex, Gabriel
- **Equipo Lupe**: Jonathan, Álvaro

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

## Equipo LidIA
- **Gerson**
  - Ayer:
  - Hoy:
- **Quique**
  - Ayer:
  - Hoy:

## Equipo Maldonado
- **Kiko**
  - Ayer:
  - Hoy:
- **Manu**
  - Ayer:
  - Hoy:

## Equipo Kitt
- **Alex**
  - Ayer:
  - Hoy:
- **Gabriel**
  - Ayer:
  - Hoy:

## Equipo Lupe
- **Jonathan**
  - Ayer:
  - Hoy:
- **Álvaro**
  - Ayer:
  - Hoy:

## Bloqueos


## Notas Adicionales
- [ ]
```

## Fuentes de Información

### 1. Notas Modificadas (MCP)
Usa `resumen_actividad_reciente(dias=1)` para obtener notas tocadas hoy.

### 2. Commits de Git
```bash
git log --since="1 day ago" --oneline --author="$(git config user.name)"
```

### 3. Tareas Completadas
Busca en notas marcadas con `[x]` modificadas hoy.

## Flujo de Trabajo

1. **Recopila** información de las fuentes.
2. **Agrupa** por proyecto (LidIA, Siniestros, VoiceBot).
3. **Redacta** entradas concisas y accionables.
4. **Guarda** en `04_Reuniones/Daily/` con la fecha como nombre.

## Integración con Proyectos

Enlaza las tareas mencionadas con sus proyectos correspondientes:
- [[LidIA]] - Proyecto de IA
- [[Siniestros]] - Gestión de siniestros
- [[VoiceBot]] - Asistente de voz
