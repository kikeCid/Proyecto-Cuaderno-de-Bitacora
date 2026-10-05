---
name: changelog-writer
description: >
  Redacta changelogs semánticos a partir de commits, PRs o descripciones
  de cambios. Sigue el formato Keep a Changelog.
tools: ['read', 'edit', 'run_command', 'obsidian-mcp']
---

# 📝 Changelog Writer

## Cuándo usar esta skill
- Cuando prepares una nueva versión/release.
- Cuando quieras documentar cambios importantes.
- Cuando necesites un resumen de lo que ha cambiado entre versiones.

## 📋 Antes de Crear Notas

> [!CAUTION]
> **OBLIGATORIO**: Lee y aplica [[REGLAS_GLOBALES]] antes de crear cualquier nota.

## Formato: Keep a Changelog

```markdown
# Changelog

Todos los cambios notables de este proyecto se documentan aquí.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es/1.1.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Nueva funcionalidad X.

### Changed
- Mejora en Y.

### Deprecated
- Funcionalidad Z será eliminada en próxima versión.

### Removed
- Eliminada funcionalidad obsoleta.

### Fixed
- Corregido bug en W.

### Security
- Actualizada dependencia vulnerable.

## [1.0.0] - 2026-01-15

### Added
- Primera versión estable.
```

## Categorías

| Categoría | Uso |
|-----------|-----|
| **Added** | Nuevas funcionalidades |
| **Changed** | Cambios en funcionalidades existentes |
| **Deprecated** | Funcionalidades que serán eliminadas |
| **Removed** | Funcionalidades eliminadas |
| **Fixed** | Corrección de bugs |
| **Security** | Vulnerabilidades corregidas |

## Flujo de Trabajo

1. **Obtén commits** desde última versión:
   ```bash
   git log v1.0.0..HEAD --oneline
   ```
2. **Agrupa** por categoría (Added, Fixed, etc.).
3. **Redacta** entradas claras y orientadas al usuario.
4. **Guarda** en `CHANGELOG.md` del proyecto o como nota en `02_Proyectos/<proyecto>/Documentación/`.

## Integración con el Vault

### Ubicaciones
- **Changelog del proyecto**: `02_Proyectos/<proyecto>/CHANGELOG.md`
- **Notas de release**: `02_Proyectos/<proyecto>/Documentación/Releases/`

### Proyectos Activos
Los proyectos del vault son: **LidIA**, **Siniestros**, **VoiceBot**.

## Consejos
- Escribe para el USUARIO, no para el desarrollador.
- Cada entrada debe ser autoexplicativa.
- Usa verbos en pasado: "Añadida", "Corregido", "Mejorada".
