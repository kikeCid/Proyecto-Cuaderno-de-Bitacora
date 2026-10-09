---
name: repo-benchmark
description: >
  Investiga y extrae sistemáticamente patrones de UI/UX, arquitectura y mejores
  prácticas de repositorios abiertos en GitHub (>1.000 estrellas) antes de diseñar,
  crear o evolucionar cualquier servicio, proyecto o componente.
tools: ['search_web', 'read', 'run_command']
---

# 🔎 Repo Benchmark & UI/UX Intelligence

> [!IMPORTANT]
> **PROTOCOLO OBLIGATORIO**: Antes de diseñar o implementar cualquier nuevo servicio, interfaz, flujo de interacción o módulo de proyecto, es **obligatorio** ejecutar esta skill para auditar repositorios de referencia en GitHub con más de 1.000 estrellas y transferir sus lecciones aprendidas al diseño local.

---

## 🎯 Propósito de la Skill
Evitar reinventar la rueda y garantizar que todo nuevo desarrollo alcance los estándares de usabilidad, ergonomía y diseño visual de los proyectos open-source más exitosos del mundo.

Esta skill establece un proceso en 5 pasos:
1. **Identificación del Dominio**: Qué problema, interfaz o servicio se va a construir.
2. **Scouting de Repositorios (>1.000 ⭐)**: Localización de los 3-5 repositorios líderes en esa materia.
3. **Auditoría de Usabilidad y UI**: Análisis de interacción, accesibilidad, ergonomía de teclado y respuesta visual.
4. **Matriz de Adopción**: Decisión fundada sobre qué elementos incorporar, adaptar o descartar.
5. **Anonimización y Cumplimiento**: Validación con `git-publisher` para que ningún dato interno confidencial se filtre.

---

## 📋 Dimensiones de Auditoría de Repositorios

Al evaluar repositorios líderes, analiza siempre estas 4 dimensiones:

| Dimensión | Aspectos Clave a Evaluar | Referencias Top (>1k ⭐) |
|---|---|---|
| **Ergonomía y Teclado** | Atajos globales, navegación con tabulador, paleta de comandos (Ctrl+K), atajos tipo Vim/Linear. | `twentyhq/twenty`, `calcom/cal.com`, `pacocoursey/cmdk` |
| **Diseño Visual & Microinteracciones** | Paleta cromática adaptativa (WCAG AAA), efectos glassmorphism, transiciones sutiles, estados hover. | `shadcn-ui/ui`, `tremorlabs/tremor`, `tabler/tabler` |
| **Feedback y Estados de Carga** | Notificaciones Toast no invasivas, skeletons limpios, empty states interactivos, feedback optimista. | `shadcn-ui/ui`, `hoppscotch/hoppscotch` |
| **Gobernanza y Documentación** | Estructura de metadatos YAML, registros ADR, changelogs semánticos, legibilidad de catálogos. | `spotify/backstage`, `logseq/logseq`, `npryce/adr-tools` |

---

## 🔄 Flujo de Trabajo Operativo

### Paso 1: Búsqueda Focalizada en GitHub
Usa consultas avanzadas para identificar los proyectos con mayor tracción y comunidad:
```text
site:github.com "[término o tipo de UI]" stars:>1000
```
*Ejemplo:* Para un portal de documentación interactiva:
`site:github.com "documentation" OR "developer portal" stars:>1000`

### Paso 2: Análisis de Componentes e Interacciones
Examina:
- ¿Cómo resuelven el filtrado y la navegación compleja?
- ¿Qué información muestran en sus tarjetas y resúmenes ejecutivos?
- ¿Cómo guían al usuario cuando no hay datos o la búsqueda no devuelve resultados?

### Paso 3: Elaboración de la Ficha de Benchmark
Toda sesión de benchmarking debe documentar:
1. **Repositorios analizados** con sus métricas reales de GitHub (estrellas, enfoque).
2. **Patrones ganadores** identificados.
3. **Propuesta de implementación directa** adaptada al ecosistema y diseño visual del proyecto.

### Paso 4: Validación de Privacidad
Antes de registrar o comitear cualquier documentación derivada de la investigación:
- Aplicar la skill `git-publisher`.
- Usar nomenclaturas neutras para casos de uso empresariales (`Proyecto 1`, `Iniciativa A`).
