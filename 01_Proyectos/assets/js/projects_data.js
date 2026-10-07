/**
 * CATÁLOGO MAESTRO DEL CUADERNO DE BITÁCORA - LÍNEA DIRECTA ASEGURADORA
 * Estructura bifurcada oficial:
 * 1. BITACORA_PROJECTS_DATA: Iniciativas de Transformación con ciclo de vida, fases, licitaciones y salud operativa.
 * 2. BITACORA_OPERATIVAS_DATA: Procedimientos, Manuales Técnicos y Operativas continuas (BAU) con gobernanza documental.
 * Persistencia en disco mediante File System Access API nativa e IndexedDB.
 * Fecha de sincronización: 2026-10-07
 */

// =========================================================================
// 1. BITÁCORA DE GESTIÓN DE PROYECTOS (INICIATIVAS Y CICLO DE VIDA)
// =========================================================================
window.BITACORA_PROJECTS_DATA = [
    {
        "id": "hcm",
        "title": "Evolución HCM Cloud",
        "subtitle": "Oracle Cloud HCM",
        "desc": "Núcleo integral de RR.HH. Migración estratégica de PeopleSoft a Oracle Cloud Fusion, optimizando la gestión del talento, nóminas y estructura organizativa.",
        "carril": "direct",
        "estado": "En Licitación",
        "licitacion": true,
        "replanificado": false,
        "semaforo": "verde",
        "href": "../HCM/index.html",
        "tags": ["Oracle Cloud HCM", "Gestión Talento", "Nóminas"]
    },
    {
        "id": "ia-personas",
        "title": "Eficiencia RRHH & IA",
        "subtitle": "Copilot & Agentes LidIA",
        "desc": "Iniciativa estratégica para automatización de consultas internas, asistentes cognitivos con LidIA y optimización operativa en gestión de personas.",
        "carril": "direct",
        "estado": "En Decisión",
        "licitacion": false,
        "replanificado": false,
        "semaforo": "verde",
        "href": "../IA Area Personas/index.html",
        "tags": ["Inteligencia Artificial", "Copilot M365", "Asistente LidIA"]
    },
    {
        "id": "pmo-perscom",
        "title": "PMO PersCom",
        "subtitle": "Oficina de Proyectos Personas",
        "desc": "Oficina de Gestión de Proyectos desde Personas: anticipación de impactos organizativos, sincronización entre PMOs y modelo 360°.",
        "carril": "direct",
        "estado": "En Curso",
        "licitacion": false,
        "replanificado": false,
        "semaforo": "verde",
        "href": "../PMO Perscom/index.html",
        "tags": ["Metodología 360°", "Gobierno PMO", "Gestión del Cambio"]
    },
    {
        "id": "crm-operacional",
        "title": "CRM Operacional",
        "subtitle": "Salesforce Financial Services Cloud",
        "desc": "Nuevo modelo omnicanal 360° de cliente y asegurado. Unificación comercial, fidelización y tramitación en Salesforce FSC + OMEGA.",
        "carril": "strategic",
        "estado": "En Curso",
        "licitacion": false,
        "replanificado": false,
        "semaforo": "verde",
        "href": "../CRM Operacional/index.html",
        "tags": ["Salesforce FSC", "OMEGA", "Omnicanalidad"]
    },
    {
        "id": "telefonia-genesys",
        "title": "Telefonía Genesys CX",
        "subtitle": "Contact Center Cloud AWS",
        "desc": "Transición de telefonía local hacia Genesys Cloud sobre AWS. 15 millones de llamadas anuales, 2.000 operadores y enrutamiento inteligente.",
        "carril": "strategic",
        "estado": "En Curso",
        "licitacion": false,
        "replanificado": false,
        "semaforo": "verde",
        "href": "../Telefonia - Genesis CX/index.html",
        "tags": ["Genesys Cloud", "AWS Cloud", "Telefonía 360°"]
    },
    {
        "id": "reingenieria-siniestros",
        "title": "Reingeniería Siniestros",
        "subtitle": "Transformación Core Autos & Hogar",
        "desc": "Transformación de punta a punta del proceso de siniestros (>400K partes/año): triaje inteligente STP, red de talleres y peritación digital.",
        "carril": "strategic",
        "estado": "En Curso",
        "licitacion": false,
        "replanificado": false,
        "semaforo": "verde",
        "href": "../Reingenieria Siniestros/index.html",
        "tags": ["Triaje STP", "Peritación Digital", "Core Autos"]
    },
    {
        "id": "gobierno-dato",
        "title": "Gobierno del Dato",
        "subtitle": "Plataforma Analítica & Databricks",
        "desc": "Democratización y calidad analítica corporativa: Data Mesh por dominios, linaje automatizado y Lakehouse corporativo en Databricks.",
        "carril": "strategic",
        "estado": "En Curso",
        "licitacion": false,
        "replanificado": false,
        "semaforo": "verde",
        "href": "../Gobierno del Dato/index.html",
        "tags": ["Data Mesh", "Databricks", "Data Governance"]
    },
    {
        "id": "ia-voz-chat",
        "title": "IA en Voz & Chat",
        "subtitle": "Agentes Cognitivos & Lupe",
        "desc": "Asistentes conversacionales multicanal con IA generativa: gestión integral en lenguaje natural y resolución directa en primer contacto.",
        "carril": "strategic",
        "estado": "En Curso",
        "licitacion": false,
        "replanificado": false,
        "semaforo": "verde",
        "href": "../IA Voz y Chat/index.html",
        "tags": ["Agente Lupe", "Speech Analytics", "NLP"]
    },
    {
        "id": "transformacion-agile",
        "title": "Transformación Agile",
        "subtitle": "Evolución Organizacional",
        "desc": "Adopción de nuevas formas de trabajo basadas en squads multidisciplinares, foco en aportación de valor de negocio y reducción de ciclos.",
        "carril": "strategic",
        "estado": "En Curso",
        "licitacion": false,
        "replanificado": false,
        "semaforo": "verde",
        "href": "../Transformacion Agile/index.html",
        "tags": ["Agile Mindset", "Squads", "OKRs"]
    },
    {
        "id": "transformacion-hogar",
        "title": "Transformación Hogar",
        "subtitle": "Liderazgo en Calidad de Servicio",
        "desc": "Modelo de autoservicio digital y gestión ágil de asistencias domésticas con integración delegada en HomeServe y trazabilidad en tiempo real.",
        "carril": "strategic",
        "estado": "En Curso",
        "licitacion": false,
        "replanificado": false,
        "semaforo": "verde",
        "href": "../Transformacion Hogar/index.html",
        "tags": ["HomeServe", "Tracking Asistencias", "Hogar Digital"]
    },
    {
        "id": "transformacion-salud",
        "title": "Relanzamiento Salud",
        "subtitle": "Alianza HNA & Cuadro Médico",
        "desc": "Salto de escala para 75.000 asegurados: acceso digital a cuadro médico de primer nivel, copago optimizado y autorizaciones inmediatas.",
        "carril": "strategic",
        "estado": "En Despliegue",
        "licitacion": false,
        "replanificado": false,
        "semaforo": "verde",
        "href": "../Transformacion Salud/index.html",
        "tags": ["Alianza HNA", "Cuadro Médico", "Autorizaciones IA"]
    },
    {
        "id": "perseo",
        "title": "Perseo",
        "subtitle": "Speech Analytics & Calidad Operativa",
        "desc": "Plataforma de escucha masiva con IA generativa que audita el 100% de las conversaciones telefónicas de ventas, siniestros y atención.",
        "carril": "facilitator",
        "estado": "En Producción",
        "licitacion": false,
        "replanificado": false,
        "semaforo": "verde",
        "href": "../Perseo/index.html",
        "tags": ["Speech Analytics", "Calidad Operativa", "IA Supervisión"]
    },
    {
        "id": "gobierno-informacion",
        "title": "Gobierno de la Información",
        "subtitle": "Histórico & Metodología LidIA / GIN",
        "desc": "Marco metodológico, archivo documental y directrices de arquitectura funcional y gobierno de datos corporativo con LidIA.",
        "carril": "strategic",
        "estado": "En Curso",
        "licitacion": false,
        "replanificado": false,
        "semaforo": "verde",
        "href": "../Gobierno de Informacion/index.html",
        "tags": ["Metodología GIN", "Gobierno del Dato", "LidIA", "Normativa"]
    }
];

// =========================================================================
// 2. BITÁCORA DE PROCEDIMIENTOS, MANUALES Y OPERATIVAS (DOCUMENTACIÓN TÉCNICA Y BAU)
// =========================================================================
window.BITACORA_OPERATIVAS_DATA = [
    {
        "id": "gestion-usuarios",
        "title": "Gestión de Usuarios",
        "subtitle": "Servicios Transversales & Directorio",
        "desc": "Documentación técnica integral, flujo operativo y arquitectura del sistema de Gestión de Usuarios, Directorio Activo y ciclo de vida de accesos corporativos.",
        "tipoDoc": "Manual Operativo",
        "area": "Sistemas & Identidades",
        "estadoDoc": "Vigente",
        "version": "v2.4",
        "ultimaRevision": "Octubre 2026",
        "proximaRevision": "Octubre 2027",
        "criticidad": "Crítica",
        "href": "../Gestion de Usuarios/index.html",
        "tags": ["Directorio Activo", "IAM", "Control de Accesos", "SSO"]
    }
];

// Contenedor global de catálogo unificado
window.BITACORA_CATALOG = {
    projects: window.BITACORA_PROJECTS_DATA,
    operativas: window.BITACORA_OPERATIVAS_DATA
};
