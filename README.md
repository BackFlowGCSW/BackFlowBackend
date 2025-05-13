# 🧠 Gestión de Proyectos - Backend (BackFlow)

Este es el backend del sistema **BackFlow**, una solución para la gestión estructurada de proyectos de software utilizando las metodologías **agiles** y **estructuradas**. Desarrollado en **Python** usando **FastAPI** como framework web y **Neo4j** como base de datos orientada a grafos.

---

## ✅ Requisitos para ejecutar el proyecto

### Software necesario

- Python 3.10 o superior
- Neo4j (versión 5.x)
- Entorno virtual (recomendado)
- Editor de código (VSCode, PyCharm, etc.)

---

## ⚙️ Preparación del entorno

1. Clona el repositorio.
2. Crea un entorno virtual y activalo.
3. Instala las dependencias del archivo `requirements.txt`:
   pip install -r requirements.txt
4. Configura el archivo `.env` en la raíz del proyecto con:

   NEO4J_BOLT_URL=bolt://localhost:7687
   NEO4J_USERNAME=neo4j
   NEO4J_PASSWORD=tu_contraseña
   JWT_SECRET=una_clave_secreta (palabra cualquiera)

5. Asegurate de que Neo4j esté corriendo y accesible en tu máquina.

---

## ▶️ Iniciar la aplicación

Para iniciar el servidor de desarrollo:

   uvicorn main:app --reload

Accedé a la documentación interactiva:

   http://localhost:8000/docs
   http://localhost:8000/redoc

---

## 📦 Estructura del proyecto

- `main.py`: punto de entrada de la aplicación
- `models/`: definición de nodos (Usuario, Proyecto, etc.)
- `services/`: lógica de negocio de cada entidad
- `routes/`: definición de endpoints REST
- `factory/`: configuración automática por metodología
- `utils/`: autenticación y utilidades comunes
- `config/`: conexión a base de datos Neo4j
- `.env`: variables de entorno
- `requirements.txt`: librerías necesarias

---

## 🧪 Funcionalidades destacadas

- Registro y login con autenticación JWT
- Gestión de usuarios, organizaciones y proyectos
- Configuración de fases y roles por metodología
- Asignación de tareas con prioridad y estado
- Flujo completo de gestión de cambios
- Generación de reportes y exportación en PDF

---

## 🌐 Recomendaciones

- Usar Swagger (`/docs`) para probar los endpoints
- Mantener Neo4j corriendo antes de iniciar el backend
- Sincronizar el backend con el frontend React (si aplica)

---
