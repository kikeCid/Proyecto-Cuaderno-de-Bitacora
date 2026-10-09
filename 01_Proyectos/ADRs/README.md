---
tags: [adr, arquitectura, decisiones, gobernanza]
type: doc-índice
status: en-curso
created: 2026-10-09
---

# 🏛️ Registro de Decisiones de Arquitectura y Proyectos (ADRs)

Este módulo centraliza todas las decisiones arquitecturales, metodológicas y tecnológicas tomadas a lo largo del ciclo de vida de las iniciativas del Portfolio.

Inspirado en el estándar de la industria [npryce/adr-tools](https://github.com/npryce/adr-tools) (>5.7k ⭐), cada registro documenta el contexto, las alternativas evaluadas, la decisión adoptada y sus consecuencias de manera inmutable.

---

## 📑 Catálogo de Decisiones Registradas

| Identificador | Título de la Decisión | Iniciativa / Proyecto | Estado | Fecha |
|:---:|---|---|:---:|:---:|
| [[ADR-001-Adjudicacion-Plataforma-Omnicanal\|ADR-001]] | Adjudicación de Plataforma Omnicanal y Modelo de Integración | Proyecto 1 (Gestión de Clientes) | `Aceptado` | 2026-03-15 |
| [[ADR-002-Arquitectura-Lakehouse-Analitica\|ADR-002]] | Adopción de Modelo Lakehouse para Plataforma Analítica | Proyecto 4 (Gobierno del Dato) | `Aceptado` | 2026-04-20 |
| [[ADR-003-Migracion-Contact-Center-Cloud\|ADR-003]] | Transición a Contact Center Cloud sobre Infraestructura AWS | Proyecto 2 (Telefonía CX) | `Aceptado` | 2026-05-10 |

---

## 🛠️ Procedimiento para Nuevas Decisiones

1. Copiar la plantilla desde `[[ZZ_Plantillas/Plantilla_ADR|Plantilla ADR]]`.
2. Asignar el siguiente identificador correlativo (`ADR-004`, etc.).
3. Completar las secciones de contexto, alternativas con pros/contras y justificación.
4. Para menciones en repositorios de control de versiones Git, aplicar estrictamente la convención anónima de la skill `git-publisher` (`Proyecto 1`, `Proyecto 2`, etc.).
