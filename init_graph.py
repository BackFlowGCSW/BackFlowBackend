import os
from dotenv import load_dotenv
from neomodel import config, db

# Cargar variables desde el archivo .env
load_dotenv()

# Obtener credenciales desde el entorno
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

# Configurar la URL de conexión para Neo4j con cifrado (Aura usa neo4j+s)
config.DATABASE_URL = f"neo4j+s://{NEO4J_USER}:{NEO4J_PASSWORD}@{NEO4J_URI}"

# Importar modelos para instalar los constraints
from models.usuario import Usuario
from models.organizacion import Organizacion
from models.proyecto import Proyecto
from models.tarea import Tarea
from models.fase import Fase
from models.rol import Rol
from models.solicitud_cambio import SolicitudCambio


def init_graph():
    """📌 Crea los constraints para los modelos de BackFlow si no existen."""
    print("📌 Inicializando base de datos de grafos (Neo4j)...")
    try:
        from neomodel import install_all_labels
        install_all_labels()
        print("✅ ¡Constraints de los modelos instalados correctamente!")
    except Exception as e:
        print(f"❌ Error al instalar labels o constraints: {e}")


if __name__ == "__main__":
    init_graph()
