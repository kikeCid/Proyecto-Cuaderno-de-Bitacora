---
tags: [manual, documentacion, calidad, redacción]
type: referencia
status: terminado
created: 2026-02-03
---

# 📖 Manual de Redacción de Fichas Maestras: Proyecto de Inteligencia Documental 🚀

> [!IMPORTANT] El Principio de Oro de la Plataforma
> **"Si no está escrito, la IA no lo sabe".**  
> No resumas. Tu misión es **explicar el proceso completo**. Escribe como si el operador no supiera nada del negocio, porque así es como la IA podrá guiarle paso a paso con seguridad.

---

## 🎯 1. El Objetivo: Escribir para una IA
A diferencia de un humano, la IA no sobreentiende qué significa "consultar con el supervisor" o "marcar como Cross Caliente". Si omites los detalles del **por qué**, el **cuándo** y el **cómo exacto**, la IA dará respuestas vagas que obligarán al operador a preguntar a un compañero.

**Nuestro éxito depende de tu capacidad para detallar la lógica de negocio.**

---

## ⚖️ 2. Las 3 Reglas del Juego Operativo

### 🛑 Regla 1: Descomposición de la Acción
No uses una sola frase para describir un proceso complejo. Divide la operativa en: **Situación -> Comprobación -> Acción.** 

### 📝 Regla 2: Cero Ambigüedad "Negociable"
Evita palabras como "puede", "a veces", "según criterio". La IA necesita reglas: "Si ocurre A, haz B. Si ocurre C, haz D".

### 🧩 Regla 3: El Contexto es Rey
Antes de la instrucción, explica **por qué** se hace. Eso ayuda a la IA a entender la intención del proceso.

---

## 🛠️ 3. ¿Cómo redactar una "Operativa Perfecta"?

Usa siempre este esquema mental:
1.  **¿Cuándo se aplica?** (Ej: "Cuando el cliente pide la baja por precio").
2.  **¿Qué mirar primero?** (Ej: "Verificar en la pantalla de póliza si tiene marca de impago").
3.  **La instrucción directa**: (Ej: "Pulsar el botón 'Retención' y seleccionar 'Oferta 10%'").
4.  **El cierre**: (Ej: "Indicar al cliente que el descuento se aplicará en el próximo recibo").

---

## 🌓 4. Transformación de Ejemplos (Infografía)

Aquí tienes cómo debemos mejorar la documentación actual para que sea útil para la Plataforma:

### Ejemplo 1: Cancelaciones
*   ❌ **Redacción Actual:** "Antes de transferir a Cross-selling por técnica, es obligatorio consultar con el supervisor."
*   ✅ **Redacción la Plataforma:** "En solicitudes de cancelación de Hogar, antes de derivar al departamento de Cross-selling, el operador debe llamar por la línea interna al supervisor de turno para validar si existe una contraoferta técnica disponible. Solo si el supervisor autoriza, se procederá a la transferencia marcando el motivo 'Técnica Autorizada'."

### Fase 3: Redacción con Metadatos (La Ficha del Bibliotecario)

Imagina que la Base de Conocimiento es una biblioteca inmensa. El sistema de IA es un **Bibliotecario Experto**. Cuando un operador hace una pregunta, este bibliotecario no lee todos los libros página por página; busca en su **Fichero Maestro**.

Si tu documento no tiene la "ficha" (metadatos) bien rellena, el bibliotecario no sabrá dónde guardarlo ni cómo encontrarlo, aunque el contenido sea perfecto.

#### 📋 Estructura Obligatoria (YAML)

Copia y pega este bloque al inicio de tu nota y rellena TODOS los campos:

```yaml
---
# IDENTIFICACIÓN
caso_uso: [Nombre del Proceso, ej: "Gestión de Bajas"]
nombre_operativa: [Título exacto del documento, ej: "Devolución Prima"]
tipo_documento: [Argumentario / Normativa / Operativa / Paso a Paso]
ramo_producto: [Hogar / Motor / Salud / Diversos]

# CONTROL
estado: [Borrador / Vigente / Obsoleto]
vigencia: [Fecha inicio - Fecha fin o Indefinido]
autor: [Tu Nombre y Departamento]

# CEREBRO (Clave para la IA)
resumen: [Descripción breve de 1 línea sobre qué resuelve este doc]
tags: [Sinónimos clave que usa el operador. Ej: "extorno, dinero, pasta"]
relaciones: [Enlaces a otros docs. Ej: "[[Condicionado General]]"]
---
```

> [!TIP] ¿Por qué tantos datos?
> *   **Caso de Uso:** Le dice a la IA "en qué cajón" va el tema (¿Es Venta? ¿Es Siniestro?).
> *   **Vigencia:** Evita que la IA responda con normas antiguas de 2020.
> *   **Tags:** Son los "anzuelos". Si escribes "Desistimiento" pero el operador busca "Echarse atrás", la IA solo lo sabrá si lo pones aquí.


### Ejemplo 2: Cambio de Tomador
*   ❌ **Redacción Actual:** "NUNCA se debe inducir el cambio. Solo se tramitará nueva cotización a petición expresa del cliente."
*   ✅ **Redacción la Plataforma:** "Bajo ninguna circunstancia el operador sugerirá al cliente el cambio de tomador de la póliza para bajar el precio. Si el cliente pregunta directamente '¿puedo poner a otra persona como tomador?', el operador debe informar que eso requiere una nueva cotización desde cero y la pérdida de las bonificaciones actuales."

### Ejemplo 3: Gestión de Impagos
*   ❌ **Redacción Actual:** "En pólizas con marca de impago, validar con supervisor la eliminación de la marca antes de la transferencia."
*   ✅ **Redacción la Plataforma:** "Si al abrir la ficha del cliente aparece el aviso rojo de 'IMPAGO', el operador no podrá realizar ninguna transferencia a Cross-selling. Primero se debe verificar que el recibo ha sido abonado. Una vez confirmado el pago, se debe solicitar al supervisor que borre manualmente la marca en el sistema. Sin este borrado, el sistema de Cross-selling bloqueará la entrada de la llamada."

---

## ✅ 5. Checklist de Validación Final
Antes de dar tu ficha por terminada, comprueba:
- [ ] ¿He explicado qué tiene que **ver** el operador en pantalla antes de actuar?
- [ ] ¿He detallado qué tiene que **decir** exactamente si hay un problema?
- [ ] ¿He incluido el nombre de los **botones o pestañas** específicos de la aplicación?
- [ ] ¿He evitado asumir que el operador "ya sabe qué hacer" si algo falla?
- [ ] **¿La instrucción es tan clara que la IA podría leerla en voz alta y el operador no tendría dudas?**

---

> [!TIP] Tu compromiso con el Piloto
> Estás creando el conocimiento que salvará tiempo a cientos de compañeros. Si la IA falla, es porque a la ficha le falta un detalle. **¡Escribe con precisión!**
