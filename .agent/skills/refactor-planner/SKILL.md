---
name: refactor-planner
description: >
  Planifica refactorizaciones complejas: analiza deuda técnica, propone
  plan de migración por fases, y documenta con ADRs.
tools: ['read', 'edit', 'run_command', 'obsidian-mcp']
---

# 🔧 Refactor Planner

## Cuándo usar esta skill
- Cuando identifiques deuda técnica significativa.
- Cuando planees una migración o reestructuración grande.
- Cuando necesites documentar el "por qué" de un refactor.

## 📋 Antes de Crear Notas

> [!CAUTION]
> **OBLIGATORIO**: Lee y aplica [[REGLAS_GLOBALES]] antes de crear cualquier nota.

## Proceso de Planificación

### 1. Análisis de Estado Actual

```markdown
## Estado Actual

### Problemas Identificados
1. **[Nombre del problema]**
   - Ubicación: `path/to/file.py`
   - Impacto: Alto/Medio/Bajo
   - Síntomas: Qué lo hace evidente

### Métricas Actuales
- Complejidad ciclomática: X
- Cobertura de tests: Y%
- Tiempo de build: Z min
```

### 2. Propuesta de Refactor

```markdown
## Propuesta

### Objetivo
Descripción clara del estado deseado.

### Enfoque
1. **Fase 1**: Preparación (tests, documentación)
2. **Fase 2**: Refactor incremental
3. **Fase 3**: Limpieza y verificación

### Riesgos
| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| Romper funcionalidad X | Media | Alto | Añadir tests primero |
```

### 3. Plan de Ejecución (Checklist)

```markdown
## Plan de Ejecución

### Fase 1: Preparación
- [ ] Añadir tests para funcionalidad afectada
- [ ] Documentar comportamiento actual
- [ ] Crear branch de refactor

### Fase 2: Refactor
- [ ] Paso 1: Extraer función X
- [ ] Paso 2: Renombrar módulo Y
- [ ] Paso 3: Consolidar Z

### Fase 3: Verificación
- [ ] Todos los tests pasan
- [ ] Review de código
- [ ] Actualizar documentación
```

## Integración con Vault

1. **Crea ADR**: Documenta la decisión en `02_Proyectos/<proyecto>/Documentación/Arquitectura/`.
2. **Crea Checklist**: Nota con el plan en `01_Inbox/` o en el proyecto.
3. **Enlaza**: Conecta con notas de módulos afectados.

### Proyectos Activos
- `02_Proyectos/LidIA/Documentación/Arquitectura/`
- `02_Proyectos/Siniestros/Documentación/Arquitectura/`
- `02_Proyectos/VoiceBot/Documentación/Arquitectura/`

## Principios

- **Pequeños pasos**: Commits atómicos y reversibles.
- **Tests primero**: No refactorices sin red de seguridad.
- **Documenta el "por qué"**: El código explica el qué, tú explicas el por qué.
- **Una cosa a la vez**: No mezcles refactor con nuevas features.
