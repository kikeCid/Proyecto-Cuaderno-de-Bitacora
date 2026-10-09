---
trigger: always_on
---

# 📜 Reglas Globales del Vault

Este archivo define las directrices que **todos los agentes/skills deben seguir** al interactuar con este vault.

## Todos los documentos que generes de informacion tienen que estra escritos en Español, cualquier documento que regeneres informativo.


## 🎯 Filosofía General
- **Atomicidad**: Una nota = Un concepto.
- **Enlaces sobre carpetas**: Prefiere conexiones semánticas (`[[nota]]`) sobre jerarquías rígidas.
- **Consistencia**: Usa las plantillas y etiquetas definidas en el vault.

## 📝 Estándares de Formato

### YAML Frontmatter
Toda nota debe incluir al menos:
```yaml
---
tags: [etiqueta_relevante]
type: tipo_de_nota
status: borrador | en-curso | terminado
created: YYYY-MM-DD
---
```

### Estructura Markdown
1. Un solo título `# H1` por nota.
2. Usa `## H2` para secciones principales.
3. Sigue las guías de `[[Markdown]]` y `[[Callouts y Admonitions]]`.

## ⚠️ Regla de Oro de Edición
Cuando uses `editar_nota`:
- **SIEMPRE** envía el archivo completo.
- **NUNCA** dupliques el bloque `---` de YAML.
- **REEMPLAZA** la metadata anterior, no la añadas debajo.

## 🔒 Restricciones y Privacidad
- No accedas a archivos en `.forbidden_paths`.
- Respeta la privacidad de notas marcadas con `#privado`.

## 🛡️ Regla de Oro de Privacidad para Git y GitHub
Al interactuar con Git o subir cambios a GitHub (commits, PRs, changelogs, issues o descripciones públicas):
- **PROHIBIDO** incluir nombres reales de proyectos de la empresa, datos de clientes, proveedores directos o menciones explícitas a la organización.
- **OBLIGATORIO** hablar siempre de manera general y codificada:
  - Usa **"Proyecto 1"**, **"Proyecto 2"**, **"Iniciativa A"**, **"Iniciativa B"**, etc.
  - Usa **"Entidad"**, **"Organización"** o **"Compañía"** en vez de nombres corporativos.
- Los mensajes de commit deben ser técnicos y abstractos (ej. `feat(ui): nuevos filtros de salud en dashboard`, `refactor(core): optimización de estructura en Proyecto 1`).
- Aplica y consulta la skill `git-publisher` antes de cualquier operación de control de versiones.