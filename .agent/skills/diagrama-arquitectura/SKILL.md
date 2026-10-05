---
name: diagrama-arquitectura
description: >
  Experto en Mermaid para generar diagramas en Obsidian. Crea flowcharts,
  secuencias, clases, estados, ER y git graphs a partir de código o descripciones.
tools: ['Read', 'Glob', 'Grep', 'obsidian-mcp']
---

# Mermaid Expert para Obsidian

Soy un experto en crear diagramas Mermaid optimizados para renderizar en Obsidian.

## Cuándo usar esta skill

- Visualizar flujos de datos o procesos
- Documentar arquitectura de sistemas
- Mostrar relaciones entre clases/módulos
- Crear diagramas de secuencia de APIs
- Modelar estados de una máquina de estados
- Documentar esquemas de base de datos

## Reglas Críticas para Obsidian

> **IMPORTANTE**: Obsidian tiene limitaciones con Mermaid. Sigue estas reglas.

### Caracteres a EVITAR dentro de nodos `[]`

| Evitar | Problema | Solución |
|--------|----------|----------|
| `()` | Rompe el parser | Mover a etiqueta de flecha o texto externo |
| `:` al inicio | Interpretado como directiva | Usar números: `1.` en lugar de `:00` |
| `"` escapadas | Inconsistente | Usar nodos sin comillas cuando sea posible |
| `<br/>` | No siempre funciona | Separar en múltiples nodos |
| Emojis | Algunos fallan | Probar antes o evitar |

### Sintaxis segura para nodos

```mermaid
%% CORRECTO - nodos simples
flowchart TD
    A[Inicio] --> B[Proceso]
    B --> C[Fin]

%% CORRECTO - detalles en etiquetas de flechas
flowchart TD
    A[API] -->|POST /users| B[Controller]
    B -->|query| C[Database]

%% INCORRECTO - paréntesis dentro del nodo
flowchart TD
    A[raw/ (audios)] --> B[process]
```

---

## Tipos de Diagramas

### 1. Flowchart (Diagrama de Flujo)

El más versátil. Usa para arquitectura, pipelines, flujos de datos.

**Direcciones:**
- `TD` / `TB` - Top to Down
- `LR` - Left to Right
- `RL` - Right to Left
- `BT` - Bottom to Top

**Formas de nodos:**

```mermaid
flowchart TD
    A[Rectángulo] --> B(Rectángulo redondeado)
    B --> C{Rombo - decisión}
    C --> D[(Base de datos)]
    C --> E((Círculo))
    E --> F[[Subrutina]]
    F --> G>Flag]
```

**Subgraphs:**

```mermaid
flowchart TD
    subgraph Backend
        A[API] --> B[Service]
        B --> C[(DB)]
    end
    subgraph Frontend
        D[React App]
    end
    D --> A
```

**Estilos:**

```mermaid
flowchart TD
    A[Nodo con estilo]
    style A fill:#f9f,stroke:#333,stroke-width:2px
```

---

### 2. Sequence Diagram (Diagrama de Secuencia)

Para documentar interacciones entre componentes, llamadas API, flujos de autenticación.

```mermaid
sequenceDiagram
    participant U as Usuario
    participant F as Frontend
    participant A as API
    participant D as Database

    U->>F: Click login
    F->>A: POST /auth/login
    A->>D: SELECT user
    D-->>A: User data
    A-->>F: JWT token
    F-->>U: Redirect dashboard
```

**Tipos de flechas:**

| Sintaxis | Significado |
|----------|-------------|
| `->>`    | Línea sólida con flecha |
| `-->>  ` | Línea punteada con flecha |
| `->`     | Línea sólida sin flecha |
| `-->`    | Línea punteada sin flecha |

**Bloques:**

```mermaid
sequenceDiagram
    participant A as Service A
    participant B as Service B

    loop Cada 5 minutos
        A->>B: Health check
        B-->>A: OK
    end

    alt Si error
        A->>A: Retry
    else Si OK
        A->>B: Continuar
    end

    opt Opcional
        A->>B: Log evento
    end
```

**Notas:**

```mermaid
sequenceDiagram
    participant A
    participant B
    A->>B: Request
    Note over A,B: Proceso async
    Note right of B: Validación
    B-->>A: Response
```

---

### 3. Class Diagram (Diagrama de Clases)

Para documentar modelos, schemas, estructuras de datos.

```mermaid
classDiagram
    class User {
        +String id
        +String email
        -String password
        +login()
        +logout()
    }

    class Order {
        +String id
        +Date created
        +List~Item~ items
        +calculate_total()
    }

    class Item {
        +String name
        +Float price
    }

    User "1" --> "*" Order : places
    Order "1" *-- "*" Item : contains
```

**Relaciones:**

| Sintaxis | Tipo |
|----------|------|
| `<\|--`  | Herencia |
| `*--`    | Composición |
| `o--`    | Agregación |
| `-->`    | Asociación |
| `--`     | Link |
| `..>`    | Dependencia |
| `..\|>`  | Realización |

**Cardinalidad:** `"1"`, `"*"`, `"0..1"`, `"1..*"`

---

### 4. State Diagram (Diagrama de Estados)

Para máquinas de estado, workflows, ciclos de vida.

```mermaid
stateDiagram-v2
    [*] --> Pending
    Pending --> Processing : start
    Processing --> Completed : success
    Processing --> Failed : error
    Failed --> Pending : retry
    Completed --> [*]
```

**Estados compuestos:**

```mermaid
stateDiagram-v2
    [*] --> Active

    state Active {
        [*] --> Idle
        Idle --> Running : start
        Running --> Idle : pause
    }

    Active --> Terminated : shutdown
    Terminated --> [*]
```

**Estados concurrentes:**

```mermaid
stateDiagram-v2
    state Processing {
        state fork_state <<fork>>
        [*] --> fork_state
        fork_state --> Validate
        fork_state --> Transform

        state join_state <<join>>
        Validate --> join_state
        Transform --> join_state
        join_state --> [*]
    }
```

---

### 5. ER Diagram (Entidad-Relación)

Para schemas de base de datos, modelos de datos.

```mermaid
erDiagram
    USER ||--o{ ORDER : places
    ORDER ||--|{ ORDER_ITEM : contains
    PRODUCT ||--o{ ORDER_ITEM : includes

    USER {
        string id PK
        string email UK
        string name
        date created_at
    }

    ORDER {
        string id PK
        string user_id FK
        date created_at
        float total
    }

    PRODUCT {
        string id PK
        string name
        float price
    }
```

**Cardinalidades:**

| Símbolo | Significado |
|---------|-------------|
| `\|\|`  | Exactamente uno |
| `o\|`   | Cero o uno |
| `}o`    | Cero o muchos |
| `}\|`   | Uno o muchos |

---

### 6. Git Graph

Para visualizar historial de git, estrategias de branching.

```mermaid
gitGraph
    commit id: "init"
    branch develop
    checkout develop
    commit id: "feat-1"
    commit id: "feat-2"
    checkout main
    merge develop id: "v1.0"
    branch hotfix
    commit id: "fix-1"
    checkout main
    merge hotfix id: "v1.0.1"
```

---

### 7. Gantt Chart

Para timelines, planificación de proyectos.

```mermaid
gantt
    title Proyecto MVP
    dateFormat YYYY-MM-DD
    section Diseño
        Wireframes     :done, d1, 2024-01-01, 7d
        UI Design      :active, d2, after d1, 14d
    section Desarrollo
        Backend API    :d3, after d2, 21d
        Frontend       :d4, after d2, 28d
    section Testing
        QA             :d5, after d4, 14d
```

---

## Flujo de Trabajo

```mermaid
flowchart TD
    A[Recibo solicitud] --> B{Tipo de diagrama}
    B -->|Flujo/Pipeline| C[flowchart]
    B -->|Interacciones| D[sequenceDiagram]
    B -->|Modelos/Clases| E[classDiagram]
    B -->|Estados| F[stateDiagram-v2]
    B -->|Base de datos| G[erDiagram]
    C --> H[Generar código Mermaid]
    D --> H
    E --> H
    F --> H
    G --> H
    H --> I[Validar sintaxis]
    I --> J[Insertar en nota]
```

### Pasos del agente:

1. **Analizar** - Entender qué se quiere visualizar
2. **Elegir tipo** - Seleccionar el diagrama más apropiado
3. **Extraer info** - Del código fuente o descripción
4. **Generar** - Código Mermaid válido para Obsidian
5. **Validar** - Revisar caracteres problemáticos
6. **Insertar** - En la nota correspondiente

---

## Ubicaciones en el Vault

| Contexto | Ubicación |
|----------|-----------|
| Proyecto específico | `02_Proyectos/<proyecto>/Diagramas/` |
| Embebido en doc | Directamente en la nota de documentación |
| Conocimiento técnico | `03_Conocimiento/<categoría>/` |

---

## Buenas Prácticas

1. **Simplicidad** - Máximo 15-20 nodos por diagrama
2. **Nombres claros** - Nodos descriptivos, sin abreviaturas crípticas
3. **Jerarquía** - Usar subgraphs para agrupar componentes relacionados
4. **Etiquetas** - Usar labels en flechas para dar contexto
5. **Comentarios** - `%%` para explicar partes complejas
6. **Dirección** - `TD` para jerarquías, `LR` para flujos lineales

---

## Debugging

Si un diagrama no renderiza en Obsidian:

1. Verificar que no hay paréntesis `()` dentro de nodos `[]`
2. Verificar que no hay `:` al inicio de texto en nodos
3. Probar quitando comillas de los nodos
4. Simplificar el texto de los nodos
5. Mover detalles a etiquetas de flechas o texto externo

```mermaid
%% Ejemplo de comentario explicativo
flowchart TD
    A[Nodo simple] --> B[Otro nodo]
```
