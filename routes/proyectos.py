from fastapi import APIRouter
from models.proyecto import ProyectoCreate
from services.proyecto_service import crear_proyecto

router = APIRouter()


@router.post("/")
def crear_proyecto_endpoint(proyecto: ProyectoCreate):
    return crear_proyecto(proyecto)
