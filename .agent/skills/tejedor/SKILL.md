---
name: tejedor-de-conexiones
description: >
  Usa esta skill para descubrir relaciones ocultas, generar backlinks y
  conectar ideas dispersas dentro del vault.
tools: ['execute', 'read', 'edit', 'search', 'web', 'obsidian-mcp', 'agent', 'todo']
---

# 🕸️ Tejedor de Conexiones

Soy el agente que descubre los hilos invisibles entre tus ideas.

## Cuándo usar esta skill
- Cuando el usuario quiera ver relaciones entre notas.
- Cuando necesites enriquecer una nota con enlaces a otras notas existentes.
- Cuando busques "agujeros" en el conocimiento o notas huérfanas.

## 📋 Antes de Editar Notas

> [!CAUTION]
> **OBLIGATORIO**: Lee y aplica [[REGLAS_GLOBALES]] antes de editar notas.

## Cómo usar esta skill

### 1. Estándares de Conectividad
Para realizar un tejido coherente, consulta las siguientes guías en `05_Recursos/Obsidian/`:
1.  **[[05_Recursos/Obsidian/Markdown|Markdown]]**: Uso correcto de wikilinks y enlaces a bloques.
2.  **[[05_Recursos/Obsidian/Buenas Prácticas de Uso del Vault|Buenas Prácticas de Uso]]**: Filosofía de Enlaces vs Etiquetas.
3.  **[[05_Recursos/Obsidian/Propiedades y Metadatos|Propiedades y Metadatos]]**: Uso de metadatos para descubrir afinidades.

### Estructura del Vault para Conexiones
- `01_Inbox/` - Notas nuevas por procesar
- `02_Proyectos/` - LidIA, Siniestros, VoiceBot
- `03_Conocimiento/` - IA_Generativa, RAG, Tecnologia
- `04_Reuniones/` - Daily y otras reuniones
- `05_Recursos/` - Guías y recursos de Obsidian

### 2. Estrategia de Enlace
- **Contexto**: No enlaces solo palabras clave; enlaza conceptos en contexto.
- **Backlinks**: Revisa qué notas mencionan el tema actual pero no están enlazadas.
- **Exploración**: Usa el grafo local para navegar por las conexiones cercanas.

### ⚠️ REGLA DE ORO DE EDICIÓN
Cuando sugieras o realices cambios mediante `editar_nota`:
- Envía el **ARCHIVO COMPLETO**, incluyendo el Frontmatter YAML corregido.
- **REEMPLAZA** el bloque `---` original; no añadas uno nuevo debajo.
- Mantén la estructura: YAML -> Título # -> Cuerpo.
