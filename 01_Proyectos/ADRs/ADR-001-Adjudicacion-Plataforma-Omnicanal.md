---
tags: [adr, arquitectura, crm, omnicanalidad]
type: adr
status: terminado
created: 2026-03-15
---

# 🏛️ ADR-001: Adjudicación de Plataforma Omnicanal y Modelo de Integración

## 📌 Metadatos del Registro
- **Iniciativa / Proyecto**: Proyecto 1 (Gestión de Clientes y Asegurados)
- **Estado**: Aceptado
- **Fecha de Decisión**: 2026-03-15
- **Responsables / Decisores**: Comité de Dirección, Dirección de Tecnología, Product Owner

---

## 🎯 Contexto y Problema
El ecosistema requería evolucionar hacia un modelo unificado de cliente 360°, superando silos de información entre ramos (Autos, Hogar, Salud) y mejorando la productividad en la atención comercial y operativa.

- **Situación actual**: Múltiples aplicaciones satélite con duplicidad de datos de asegurados y fricción en la tramitación.
- **Necesidad / Desafío**: Disponer de una plataforma escalable en la nube con soporte nativo para servicios financieros y aseguradores.
- **Restricciones**: Cumplimiento regulatorio, alta disponibilidad y capacidad de integración en tiempo real con los sistemas core.

---

## ⚖️ Alternativas Evaluadas

### Opción 1: Plataforma Cloud Líder de Servicios Financieros con Partner Especializado
- **Descripción**: Adopción de plataforma CRM cloud para servicios financieros junto a integrador con amplia experiencia demostrada en el sector.
- **Ventajas (+)**: Modelo de datos preconfigurado para entidades aseguradoras, alta capacidad omnicanal y roadmap de innovación continuo con IA.
- **Desventajas (-)**: Coste de licencias por usuario y necesidad de adaptación organizativa.

### Opción 2: Desarrollo a Medida sobre Arquitectura Existente
- **Descripción**: Construcción de portal propio extendiendo aplicaciones legacy.
- **Ventajas (+)**: Control total del código fuente sin licencias de terceros.
- **Desventajas (-)**: Time-to-market inviable, alto coste de mantenimiento y deuda técnica recurrente.

---

## ✅ Decisión Adoptada
Se acordó seleccionar la **Opción 1**, adjudicando la implantación a la propuesta técnica y económica más sólida con la solución Cloud para Servicios Financieros.

**Justificación**:
1. Reduce el tiempo de puesta en producción de la visión cliente 360°.
2. Proporciona soporte nativo a casos de uso omnicanal complejos.
3. El socio integrador demostró solvencia técnica superior en las fases de licitación y defensa.

---

## 🚀 Consecuencias e Impacto

### Impactos Positivos
- Unificación de la ficha de cliente en un único punto de verdad.
- Reducción del tiempo medio de operación en canales de atención y ventas.
- Arquitectura desacoplada y orientada a eventos.

### Riesgos o Trade-offs Asumidos
- Curva de aprendizaje para operadores y tramitadores (mitigada mediante plan intensivo de gestión del cambio).
- Gestión del gobierno de integración para no sobrecargar los servicios legacy durante la coexistencia.

### Siguientes Pasos
- [x] Firma de adjudicación y formalización contractual.
- [x] Definición de arquitectura de integración con Lakehouse y Core.
- [ ] Fase de despliegue progresivo por colectivos.
