# 📋 Cuaderno de Bitácora — Portfolio de Iniciativas Estratégicas
### Dirección de Tecnología y Transformación · Entidad Aseguradora

Portal corporativo de alta dirección y gobernanza para el seguimiento integral, supervisión ejecutiva y consulta documental del portfolio de iniciativas tecnológicas y operativas de la Organización.

---

## 🎯 Propósito del Servicio

El **Cuaderno de Bitácora** centraliza y estandariza la información operativa y estratégica de todas las iniciativas que transforman la entidad. Proporciona una interfaz ejecutiva moderna (diseño *Liquid Glass*, vista *Bento Grid* y carruseles horizontales con navegación asistida) que permite a los comités de dirección, Product Owners, Project Managers y equipos técnicos:

1. **Monitorear el Estado y Salud en Tiempo Real**: Visualización reactiva de indicadores de portfolio (Total de iniciativas, Gestión Directa, Proyectos Estratégicos, Iniciativas en Plazo y Concursos de Licitación activos).
2. **Consultar la Doble Dimensión Documental**:
   - **Fichas Ejecutivas de Proyecto**: Hoja técnica de trabajo con diagnóstico inicial, pilares operativos, plan de gestión del cambio, cronograma consensuado e indicadores clave.
   - **Comunicados Oficiales**: Anuncio institucional con valor diferencial para el cliente, declaraciones directivas y batería de preguntas frecuentes (FAQ).
3. **Registro Formal de Decisiones (ADRs)**: Catálogo inmutable de Architecture Decision Records que proporciona trazabilidad auditable sobre elecciones tecnológicas, adjudicaciones y giros de arquitectura.
4. **Autonomía y Gobernanza sin Servidor**: Capacidad de actualizar fases, carriles, semáforos operativos (Saludable, En Riesgo, Crítico, Parado) y concursos de licitación directamente desde el navegador, con persistencia automática en disco a través de la Web File System API nativa respaldada por IndexedDB.

---

## 🧭 Estructura de Carriles del Portfolio

El portfolio se organiza en carriles semánticos normalizados según el modelo de gobernanza PMO, aplicando el estándar de privacidad de la skill `git-publisher`:

| Carril | Descripción | Iniciativas Principales |
| :--- | :--- | :--- |
| **Gestión Directa** | Proyectos bajo supervisión directa de PO / PM | • Proyecto 8 (Gestión de Accesos e Identidades)<br>• Histórico de Gobernanza Documental<br>• Proyecto 6 (Evolución Cloud de Personas) |
| **Proyectos Estratégicos** | Los 8 grandes pilares de transformación corporativa | • Proyecto 1 (Plataforma Omnicanal de Clientes)<br>• Proyecto 2 (Contact Center Cloud)<br>• Proyecto 3 (Reingeniería de Operaciones Core)<br>• Proyecto 4 (Plataforma Analítica & Lakehouse)<br>• Proyecto 5 (Agentes Conversacionales & IA)<br>• Iniciativa de Asistencia Doméstica Digital<br>• Iniciativa de Cuadro Médico y Salud<br>• Iniciativa de Transformación Ágil |
| **Facilitadores y Afectados** | Proyectos transversales y habilitadores tecnológicos | • Proyecto Facilitador (Speech Analytics & Calidad Operativa)<br>• Arquitectura Cloud y Sistemas Core |
| **Servicios y Operativas** | Plataformas continuas de servicio | • Soporte Operativo, Seguridad y Automatización |
| **Histórico / Cerrados** | Iniciativas concluidas y consolidadas en BAU | • Archivo histórico de proyectos completados |

---

## ⚡ Capacidades Técnicas y Experiencia de Usuario (UI/UX)

- **Centro de Control de Estados y Gobernanza (Tecla `G`)**:
  - Panel lateral deslizante para modificar de forma inmediata la fase, carril organizativo, estado de licitación y desvíos de cronograma (replanificación).
  - Persistencia automática en `projects_data.js` mediante la **Chromium File System Access API** vinculada en **IndexedDB**, eliminando la necesidad de volver a seleccionar la ruta del archivo en cada guardado.
  - Iconografía lineal corporativa y paleta de acento de alto contraste.
- **Filtros Facetados por Salud Operativa y Scorecards**:
  - Filtrado reactivo en un clic por estado de semáforo (Saludable / En Plazo, En Riesgo, En Pausa, En Licitación) combinado armónicamente con los carriles funcionales.
- **Navegador «En esta página» (Smart TOC)**:
  - Menú lateral flotante jerárquico que refleja las secciones del carrusel y permite saltar directamente a cada tarjeta de proyecto con desplazamiento dual automático (vertical en página y horizontal en carrusel).
  - Diseñado con anclaje visual superior que evita solapamientos con la botonera de acciones rápidas.
- **Barra de Acciones Rápidas y «Visitas Recientes» (Tecla `H`)**:
  - Botonera flotante en cápsula compacta inferior derecha.
  - Cajón de **Visitas Recientes**: Registro en sesión de las últimas páginas y fichas consultadas, con título completo, badge de categoría y tiempo relativo en español.
- **Buscador Spotlight Global (Tecla `Ctrl + K` / `⌘K`)**:
  - Búsqueda instantánea en milisegundos sobre más de 50 documentos indexados con resaltado de coincidencias y filtros por categoría.
- **Modo Presentación Zen (Tecla `Z` / `ESC`)**:
  - Vista a pantalla completa sin distracciones para presentaciones ejecutivas ante Dirección y comités.
- **Modo Oscuro / Claro (Tecla `D`)**:
  - Paleta cromática adaptativa validada bajo estándares WCAG AAA.

---

## 📂 Organización del Repositorio

```text
Proyecto Cuaderno de Bitacora/
├── 01_Proyectos/
│   ├── Cuaderno de Bitacora (Proyectos)/
│   │   ├── index.html                    # Portada principal del Cuaderno de Bitácora
│   │   └── styles_bitacora.css           # Hoja de estilos maestra
│   ├── ADRs/                             # Registro formal de Decisiones de Arquitectura
│   ├── CRM Operacional/                  # Proyecto 1: Hub, Ficha Ejecutiva y Comunicado Oficial
│   ├── Telefonia - Genesis CX/           # Proyecto 2: Hub, Ficha Ejecutiva y Comunicado Oficial
│   ├── Reingenieria Siniestros/          # Proyecto 3: Hub, Ficha Ejecutiva y Comunicado Oficial
│   ├── Gobierno del Dato/                # Proyecto 4: Hub, Ficha Ejecutiva y Comunicado Oficial
│   ├── IA Voz y Chat/                    # Proyecto 5: Hub, Ficha Ejecutiva y Comunicado Oficial
│   ├── HCM/                              # Proyecto 6: Hub y Documentación
│   ├── IA Area Personas/                 # Proyecto 7: Hub de Asistentes y Diagnóstico
│   ├── Gestion de Usuarios/              # Proyecto 8: Hub de Identidades y Accesos
│   ├── Transformacion Hogar/             # Hub, Ficha Ejecutiva y Comunicado Oficial Hogar
│   ├── Transformacion Salud/             # Hub, Ficha Ejecutiva y Comunicado Oficial Salud
│   ├── Transformacion Agile/             # Hub, Ficha Ejecutiva y Comunicado Oficial Agile
│   ├── Gobierno de Informacion/          # Hub Histórico de Gobernanza
│   └── assets/
│       ├── css/
│       │   └── bitacora-core.css         # Framework CSS compartido
│       └── js/
│           ├── projects_data.js          # Catálogo maestro de datos y estados
│           ├── bitacora-admin.js         # Motor reactivo de gobernanza y persistencia
│           ├── bitacora-core.js          # Suite de componentes UI/UX, TOC y Visitas Recientes
│           └── search_index_data.js      # Índice de búsqueda Spotlight
├── .agent/
│   ├── rules/                            # Reglas obligatorias de gobernanza y privacidad Git
│   └── skills/                           # Skills especializadas (git-publisher, standup, etc.)
├── ZZ_Plantillas/                        # Plantillas oficiales (ADRs, Bitácora Continua)
├── .gitignore                            # Exclusiones de Git (scratch, temporales, venv)
├── Índice del Vault.md                   # Mapa central del Vault de conocimiento anonimizado
└── README.md                             # Documentación oficial del servicio
```

---

## 🚀 Despliegue y Ejecución

Al estar desarrollado bajo arquitectura estática pura (*Jamstack* sin dependencias de backend):

1. **Ejecución Local**: Abrir directamente `01_Proyectos/Cuaderno de Bitacora (Proyectos)/index.html` en cualquier navegador moderno (Google Chrome o Microsoft Edge recomendados para la suite File System API).
2. **Uso de la Gobernanza**: Pulsar el botón **«Gestión Estados»** en la barra superior o presionar la tecla **`G`**. Al pulsar **Guardar Cambios**, se vinculará `projects_data.js` para persistencia automática directa.

---

## 🛡️ Política de Privacidad para Control de Versiones

Este repositorio adhiere al protocolo estricto de la skill `git-publisher`:
- Todas las referencias públicas a proyectos, iniciativas y participantes se encuentran codificadas y generalizadas.
- Queda prohibido el commit de datos de filiación comercial o corporativa concreta.

---

**Entidad Organizativa** · Todos los derechos reservados.
