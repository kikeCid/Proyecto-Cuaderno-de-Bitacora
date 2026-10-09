---
name: git-publisher
description: >
  Gestiona de forma segura y automatizada las operaciones de Git y GitHub,
  garantizando la anonimización estricta de nombres de proyectos y relaciones
  de datos corporativos confidenciales antes de cualquier commit o push.
tools: ['run_command', 'read', 'edit']
---

# 🛡️ Git Publisher Seguro & Anonimizador

> [!CAUTION]
> **REGLA DE ORO DE PRIVACIDAD**: Todo lo que se comunique, prepare, comittee o suba a Git/GitHub debe estar **100% anonimizado**. NUNCA usar nombres reales de proyectos de la empresa, clientes, proveedores específicos vinculados o datos identificativos. Habla y documenta siempre de manera general: **"Proyecto 1"**, **"Proyecto 2"**, **"Iniciativa A"**, **"Iniciativa B"**, etc.

---

## 🎯 Propósito de la Skill
Esta skill rige todas las acciones de control de versiones (Git/GitHub):
1. Redacción de mensajes de commit semánticos y seguros.
2. Generación de resúmenes de pull requests y releases.
3. Creación y renombrado de ramas (branches).
4. Auditoría pre-commit y pre-push para evitar fugas de información interna.

---

## 📋 Diccionario de Anonimización Obligatorio

Al interactuar con Git o redactar textos públicos para GitHub, aplica estrictamente esta tabla de correspondencia:

| Concepto Real Interno | Nomenclatura Genérica para Git / GitHub |
|-----------------------|-----------------------------------------|
| Proyecto de Gestión de Clientes / CRM | `Proyecto 1` o `Iniciativa de Clientes` |
| Proyecto de Telefonía / Contact Center Cloud | `Proyecto 2` o `Iniciativa de Contact Center` |
| Proyecto de Tramitación / Siniestros | `Proyecto 3` o `Iniciativa Core de Operaciones` |
| Proyecto de Plataforma de Datos / Analytics | `Proyecto 4` o `Iniciativa de Plataforma de Datos` |
| Proyecto de Asistentes IA / Chatbot | `Proyecto 5` o `Iniciativa de Agentes Conversacionales` |
| Proyecto de RRHH / Personas | `Proyecto 6` o `Iniciativa de Gestión Interna` |
| Proyecto de Metodología / Agile | `Proyecto 7` o `Iniciativa de Transformación Organizativa` |
| Nombre de la Empresa / Entidad | `Entidad`, `Organización`, `Compañía` o `Entidad Aseguradora` |
| Proveedores o Consultoras | `Proveedor A`, `Proveedor B`, `Consultora Especializada` |
| Nombres de Personas / Empleados | Roles genéricos: `Product Owner`, `Project Manager`, `Líder Técnico` |

---

## ✍️ Estándar de Mensajes de Commit

Los mensajes deben ser profesionales, concisos y **100% neutros/anónimos**:

### ✅ Ejemplos Correctos:
```bash
# Formato semántico: tipo(ámbito): descripción neutra
feat(ui): añadir filtros de salud operativa y KPIs dinámicos en el dashboard
feat(arquitectura): incorporar registro formal de decisiones (ADRs) en Proyecto 1
fix(estilos): corregir alineación de tarjetas en carrusel y modo oscuro
chore(seguridad): implementar protocolo de anonimización y verificación pre-push
docs(bitacora): actualizar registro de eventos e hitos en Proyecto 2
refactor(datos): optimizar reactividad del catálogo en tiempo real
```

### ❌ Ejemplos Prohibidos:
```bash
# NUNCA uses nombres reales corporativos ni de iniciativas internas en commits
git commit -m "feat(modulo-interno): adjudicar proveedor real a contrato confidencial"   # ❌ PROHIBIDO
git commit -m "fix: actualizar modulo de telefonia interna para empleados con nombre"      # ❌ PROHIBIDO
git commit -m "docs: balance de operaciones internas con nombre de empresa"               # ❌ PROHIBIDO
```

---

## 🔍 Protocolo de Verificación Pre-Commit / Pre-Push

Antes de ejecutar `git commit` o `git push`:

1. **Auditar el mensaje de commit:**
   - Asegurarse de que no contiene palabras clave confidenciales.
   - Usar solo alias ("Proyecto 1", "Iniciativa 2") o descripciones técnicas abstractas.

2. **Auditar los archivos staged (`git diff --cached`):**
   - Comprobar que no se añaden claves API, credenciales ni documentos con datos identificativos no autorizados.

3. **Ejecutar el comprobador automático:**
   ```bash
   python .agent/skills/git-publisher/scripts/git_privacy_checker.py --check-staged
   ```

4. **Confirmación:**
   - Solo proceder si la verificación es exitosa (`0 alertas de privacidad detectadas`).
