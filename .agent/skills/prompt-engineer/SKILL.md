---
name: prompt-engineer
description: >
  Diseña, itera y versiona prompts de LLM. Documenta el proceso de
  optimización con métricas y variantes.
tools: ['read', 'edit', 'obsidian-mcp']
---

# 🧠 Prompt Engineer

## Cuándo usar esta skill
- Cuando diseñes un nuevo prompt para un LLM.
- Cuando iteres sobre un prompt existente para mejorar resultados.
- Cuando quieras documentar y versionar tus prompts.

## 📋 Antes de Crear Notas

> [!CAUTION]
> **OBLIGATORIO**: Lee y aplica [[REGLAS_GLOBALES]] antes de crear cualquier nota.

## Estructura de Documentación

Los prompts se guardan según su contexto:

### Por Proyecto
```text
02_Proyectos/
└── <proyecto>/
    └── Prompts/
        ├── 📖 Índice.md          # Mapa de prompts del proyecto
        ├── <prompt-name>.md      # Prompt documentado
        └── <prompt-name>-v2.md   # Versión iterada
```

### Conocimiento General de Prompting
```text
03_Conocimiento/
└── IA_Generativa/
    └── Prompts/
        └── <prompt-name>.md      # Prompts reutilizables
```

### Proyectos Activos
- `02_Proyectos/LidIA/Prompts/`
- `02_Proyectos/VoiceBot/Prompts/`

## Plantilla de Prompt

```markdown
---
tags: [prompt, <proyecto>]
type: prompt
project: <nombre-proyecto>
version: 1.0
status: draft | testing | production
created: YYYY-MM-DD
---

# Prompt: <Nombre Descriptivo>

## Objetivo
¿Qué debe lograr este prompt?

## Prompt

```text
<El prompt completo aquí>
```

## Variables
| Variable | Tipo | Descripción |
|----------|------|-------------|
| `{context}` | str | Contexto recuperado |
| `{question}` | str | Pregunta del usuario |

## Ejemplos de Uso

### Input
```text
context: "Machine learning es..."
question: "¿Qué es ML?"
```

### Output Esperado
```text
Machine learning es un subcampo de la IA...
```

## Historial de Versiones

| Versión | Fecha | Cambios | Resultado |
|---------|-------|---------|-----------|
| 1.0 | 2026-01-15 | Versión inicial | Baseline |
| 1.1 | 2026-01-16 | Añadido "cita fuentes" | +15% precisión |

## Notas de Optimización
- Observaciones sobre qué funciona y qué no.
- A/B tests realizados.
```

## Principios de Diseño de Prompts

1. **Sé específico**: Cuanto más concreto, mejor resultado.
2. **Da ejemplos**: Few-shot prompting mejora significativamente.
3. **Define el rol**: "Eres un experto en X..."
4. **Especifica formato**: "Responde en JSON/Markdown/lista..."
5. **Itera con datos**: Prueba con inputs reales, no imaginarios.

## Flujo de Trabajo

1. **Draft**: Escribe versión inicial.
2. **Test**: Prueba con varios inputs.
3. **Measure**: Documenta resultados (precisión, tono, etc.).
4. **Iterate**: Ajusta basándote en datos.
5. **Version**: Guarda cada iteración significativa.
