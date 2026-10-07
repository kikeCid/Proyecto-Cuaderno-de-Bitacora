# 📋 Cuaderno de Bitacora — Portfolio de Iniciativas Estratégicas
### Línea Directa Aseguradora (LDA) · Dirección de Tecnología y Transformación

Portal corporativo de alta dirección y gobernanza para el seguimiento integral, supervisión ejecutiva y consulta documental del portfolio de proyectos tecnológicos y operativos de **Línea Directa Aseguradora**.

---

## 🎯 Propósito del Servicio

El **Cuaderno de Bitácora** centraliza y estandariza la información operativa y estratégica de todas las iniciativas que transforman la compañía. Proporciona una interfaz ejecutiva moderna (diseño *Apple Liquid Glass*, vista *Bento Grid* y carruseles horizontales con navegación asistida) que permite a los comités de dirección, Product Owners, Project Managers y equipos técnicos:

1. **Monitorear el Estado y Salud en Tiempo Real**: Visualización reactiva de indicadores de portfolio (Total de iniciativas, Gestión Directa, Proyectos Estratégicos y Licitaciones activas).
2. **Consultar la Doble Dimensión Documental**:
   - **Fichas Ejecutivas de Proyecto**: Hoja técnica de trabajo con diagnóstico inicial, pilares operativos, plan de gestión del cambio, cronograma consensuado e indicadores clave.
   - **Comunicados Oficiales**: Anuncio institucional con valor diferencial para el cliente, declaraciones directivas y batería de preguntas frecuentes (FAQ).
3. **Autonomía y Gobernanza sin Servidor**: Capacidad de actualizar fases, carriles, semáforos operativos (Saludable, En Riesgo, Crítico, Parado) y concursos de licitación directamente desde el navegador, con persistencia automática en disco a través de la Web File System API nativa respaldada por IndexedDB.

---

## 🧭 Estructura de Carriles del Portfolio

El portfolio se organiza en carriles semánticos normalizados según el modelo de gobernanza PMO:

| Carril | Descripción | Iniciativas Principales |
| :--- | :--- | :--- |
| **Gestión Directa** | Proyectos bajo supervisión directa de PO / PM | • Gestión de Usuarios (Fase I)<br>• Gobierno de Información<br>• HCM (Área de Personas) |
| **Proyectos Estratégicos** | Los 8 grandes pilares de transformación corporativa | • CRM Operacional (Salesforce)<br>• Telefonía Genesys CX<br>• Reingeniería Siniestros Motor<br>• Gobierno del Dato (Databricks)<br>• IA Voz y Chat (Lupe)<br>• Transformación Hogar (HomeServe)<br>• Transformación Salud (HNA)<br>• Transformación Agile |
| **Facilitadores y Afectados** | Proyectos transversales y habilitadores tecnológicos | • Perseo (Speech Analytics)<br>• Arquitectura Cloud y Core |
| **Servicios y Operativas** | Plataformas continuas de servicio | • Soporte Operativo y Automatización |
| **Histórico / Cerrados** | Iniciativas concluidas y consolidadas en BAU | • Archivo histórico de proyectos completados |

---

## ⚡ Capacidades Técnicas y Experiencia de Usuario (UI/UX)

- **Centro de Control de Estados y Gobernanza (Tecla `G`)**:
  - Panel lateral deslizante para modificar de forma inmediata la fase, carril organizativo, estado de licitación y desvíos de cronograma (replanificación).
  - Persistencia automática en `projects_data.js` mediante la **Chromium File System Access API** vinculada en **IndexedDB**, eliminando la necesidad de volver a seleccionar la ruta del archivo en cada guardado.
  - Iconografía lineal corporativa Línea Directa en rojo (`#e4002b`).
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
  - Paleta cromática corporativa adaptativa validada bajo estándares WCAG AAA.

---

## 📂 Organización del Repositorio

```text
Proyecto Cuaderno de Bitacora/
├── 01_Proyectos/
│   ├── Cuaderno de Bitacora (Proyectos)/
│   │   ├── index.html                    # Portada principal del Cuaderno de Bitácora
│   │   └── styles_bitacora.css           # Hoja de estilos maestra
│   ├── CRM Operacional/                  # Hub, Ficha Ejecutiva y Comunicado Oficial CRM
│   ├── Telefonia - Genesis CX/           # Hub, Ficha Ejecutiva y Comunicado Oficial Telefonía
│   ├── Reingenieria Siniestros/          # Hub, Ficha Ejecutiva y Comunicado Oficial Siniestros
│   ├── Gobierno del Dato/                # Hub, Ficha Ejecutiva y Comunicado Oficial Dato
│   ├── IA Voz y Chat/                    # Hub, Ficha Ejecutiva y Comunicado Oficial IA Lupe
│   ├── Transformacion Hogar/             # Hub, Ficha Ejecutiva y Comunicado Oficial Hogar
│   ├── Transformacion Salud/             # Hub, Ficha Ejecutiva y Comunicado Oficial Salud
│   ├── Transformacion Agile/             # Hub, Ficha Ejecutiva y Comunicado Oficial Agile
│   ├── Gestion de Usuarios/              # Hub de Gestión Directa
│   ├── Gobierno de Informacion/          # Hub de Gestión Directa
│   ├── HCM/                              # Hub de Gestión Directa
│   ├── IA Area Personas/                 # Hub de Copilot y M365
│   └── assets/
│       ├── css/
│       │   └── bitacora-core.css         # Framework CSS compartido
│       └── js/
│           ├── projects_data.js          # Catálogo maestro de datos y estados
│           ├── bitacora-admin.js         # Motor reactivo de gobernanza y persistencia
│           ├── bitacora-core.js          # Suite de componentes UI/UX, TOC y Visitas Recientes
│           └── search_index_data.js      # Índice de búsqueda Spotlight
├── .gitignore                            # Exclusiones de Git (scratch, temporales, venv)
├── Índice del Vault.md                   # Mapa central del Vault de conocimiento
└── README.md                             # Documentación oficial del servicio
```

---

## 🚀 Despliegue y Ejecución

Al estar desarrollado bajo arquitectura estática pura (*Jamstack* sin dependencias de backend):

1. **Ejecución Local**: Abrir directamente `01_Proyectos/Cuaderno de Bitacora (Proyectos)/index.html` en cualquier navegador moderno (Google Chrome o Microsoft Edge recomendados para la suite File System API).
2. **Uso de la Gobernanza**: Pulsar el botón **«Gestión Estados»** en la barra superior o presionar la tecla **`G`**. Al pulsar **Guardar Cambios**, se vinculará `projects_data.js` para persistencia automática directa.

---

**Línea Directa Aseguradora S.A.** · Todos los derechos reservados.
