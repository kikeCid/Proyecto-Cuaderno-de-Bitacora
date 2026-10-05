---
name: resumidor
description: >
  Resume contenido largo (artículos, vídeos, libros) en notas atómicas
  y estructuradas. Extrae ideas clave y las conecta con el vault.
tools: ['read', 'edit', 'web', 'obsidian-mcp']
---

# 📖 Resumidor

## Cuándo usar esta skill
- Cuando el usuario comparta un artículo/URL para resumir.
- Cuando quiera notas de un vídeo de YouTube.
- Cuando necesite extraer ideas clave de un texto largo.

## 📋 Antes de Crear Notas

> [!CAUTION]
> **OBLIGATORIO**: Lee y aplica [[REGLAS_GLOBALES]] antes de crear cualquier nota.

## Formato de Resumen

```markdown
---
tags: [resumen, <tema>]
type: resumen
source: "<URL o título>"
author: "<Autor si aplica>"
created: YYYY-MM-DD
---

# Resumen: <Título>

## 📌 Idea Principal
Una oración que capture la esencia del contenido.

## 🔑 Ideas Clave

### 1. [Primera idea importante]
Explicación breve + cita relevante si aplica.

### 2. [Segunda idea importante]
Explicación breve.

### 3. [Tercera idea importante]
Explicación breve.

## 💡 Mis Reflexiones
¿Cómo se conecta esto con lo que ya sé?
¿Qué preguntas me genera?

## 🔗 Conexiones
- [[Nota relacionada en el vault]]
- [[Concepto que amplía esto]]

## 📚 Citas Destacadas
> "Cita textual relevante" — Autor

## 🏷️ Para Explorar
- Concepto mencionado que quiero investigar
- Autor/libro referenciado
```

## Fuentes Soportadas

### Artículos Web
Usa la URL directamente. Extrae el contenido principal ignorando navegación/ads.

### Vídeos de YouTube
Usa `get_youtube_transcript(url)` para obtener la transcripción y resumir.

### Libros/PDFs
El usuario puede pegar fragmentos o capítulos para resumir.

## Flujo de Trabajo

1. **Obtén** el contenido (URL, transcripción, texto).
2. **Identifica** las 3-5 ideas principales.
3. **Redacta** en el formato de resumen.
4. **Conecta** con notas existentes del vault usando `buscar_en_notas`.
5. **Guarda** según el tema:
   - IA y LLMs → `03_Conocimiento/IA_Generativa/`
   - RAG y retrieval → `03_Conocimiento/RAG/`
   - Tecnología general → `03_Conocimiento/Tecnologia/`
   - Notas rápidas → `01_Inbox/`

## Principios

- **Brevedad**: Un resumen debe ser 10-20% del original.
- **Tus palabras**: Parafrasea, no copies (excepto citas).
- **Conexión**: El valor está en enlazar con conocimiento previo.
- **Accionable**: ¿Qué harás con esta información?
