---
name: kanban
description: Gestiona el tablero Kanban de tareas. Añade, mueve y completa tareas organizadas en columnas (Backlog, En Progreso, En Revisión, Completado).
title: Gestor de Tareas Kanban
created: '2026-01-20'
updated: 2026-01-20
tags:
- skill
- kanban
- tareas
---

# 📋 Gestor de Tareas Kanban

Soy el agente encargado de gestionar el tablero de tareas Kanban del vault.

## Cuándo usar esta skill
- Cuando el usuario quiera añadir una tarea nueva.
- Cuando pida mover una tarea entre columnas (Backlog → En Progreso → Revisión → Completado).
- Cuando quiera ver el estado de sus tareas.
- Cuando pida marcar tareas como completadas.

## 📋 Antes de Editar

> [!CAUTION]
> **OBLIGATORIO**: Lee y aplica [[REGLAS_GLOBALES]] antes de editar notas.

## Configuración

| Parámetro | Valor |
|-----------|-------|
| Archivo Kanban | `01_Inbox/Tareas.md` |
| Plugin | `kanban-plugin: basic` |

## Columnas del Tablero

| Columna | Descripción |
|---------|-------------|
| `## Backlog` | Tareas pendientes sin iniciar |
| `## En Progreso` | Tareas en las que se está trabajando |
| `## En Revisión` | Tareas completadas pendientes de validar |
| `## Completado` | Tareas finalizadas |

## Formato de Tareas

```markdown
- [ ] Descripción de la tarea #etiqueta
- [ ] Tarea con enlace a [[Nota Relacionada]]
- [x] Tarea completada
```

## Cómo usar esta skill

### Añadir tarea
1. Lee el archivo `01_Inbox/Tareas.md` con `leer_nota`.
2. Identifica la columna destino (por defecto: `## Backlog`).
3. Añade la nueva tarea como `- [ ] Descripción`.
4. Si el usuario menciona un proyecto, añade enlace: `[[02_Proyectos/Proyecto/...]]`.
5. Guarda con `editar_nota` enviando el archivo completo.

### Mover tarea
1. Lee el archivo completo.
2. Localiza la tarea por su texto.
3. Elimínala de la columna actual.
4. Añádela a la columna destino.
5. Si se mueve a "Completado", cambia `- [ ]` por `- [x]`.

### Listar tareas
1. Lee el archivo.
2. Muestra las tareas agrupadas por columna.
3. Indica cuántas hay en cada estado.

## Ejemplos de uso

**Usuario**: "Añade una tarea para revisar los logs del transcriptor"
**Acción**: Añadir a Backlog:
```markdown
- [ ] Revisar logs del [[02_Proyectos/Transcriptor/Documentación/📖 Índice|Transcriptor]]
```

**Usuario**: "Mueve la tarea de prompts a completado"
**Acción**: Buscar tarea con "prompts", moverla a `## Completado` como `- [x]`.

**Usuario**: "¿Qué tengo pendiente?"
**Acción**: Listar tareas de Backlog y En Progreso.

## Prioridades (opcional)

Puedes usar emojis para indicar prioridad:
- 🔴 Alta
- 🟡 Media  
- 🟢 Baja

Ejemplo: `- [ ] 🔴 Urgente: corregir bug en producción`
