from utils.db import run_query
from models.proyecto import ProyectoCreate


def crear_proyecto(proyecto: ProyectoCreate):
    print("Entrando al service")
    query = """
        CREATE (p:Proyecto {
            nombre: $nombre,
            descripcion: $descripcion,
            fechaInicio: $fechaInicio,
            fechaFin: $fechaFin
        })
        RETURN p
    """
    params = {k: v for k, v in proyecto.dict().items() if v is not None}
    result = run_query(query, params)
    return {"mensaje": "Proyecto creado con éxito"}
