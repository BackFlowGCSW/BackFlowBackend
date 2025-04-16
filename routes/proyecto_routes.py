from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
from datetime import date
from services.proyecto_service import ProyectoService
from utils.security import get_current_user

router = APIRouter(prefix="/proyectos", tags=["Proyectos"])

# ----------- SCHEMAS -----------

class ProyectoCreate(BaseModel):
    nombre: str
    descripcion: Optional[str] = ""
    fecha_inicio: Optional[date] = None
    fecha_fin: Optional[date] = None
    metodologia: str
    repositorio: Optional[str] = ""
    organizacion_id: str


class ProyectoUpdate(BaseModel):
    nombre: Optional[str]
    descripcion: Optional[str]
    fecha_inicio: Optional[date]
    fecha_fin: Optional[date]
    repositorio: Optional[str]

# ----------- RUTAS ------------

@router.post("/")
def crear_proyecto(data: ProyectoCreate, usuario=Depends(get_current_user)):
    try:
        payload = data.dict()
        payload["creado_por"] = usuario.uid
        proyecto = ProyectoService.crear_proyecto(payload)
        return {"mensaje": "Proyecto creado correctamente", "id": proyecto.uid}
    except HTTPException as e:
        raise e


@router.get("/")
def listar_proyectos():
    return ProyectoService.listar_proyectos()


@router.put("/{uid}")
def editar_proyecto(uid: str, data: ProyectoUpdate):
    return ProyectoService.editar_proyecto(uid, data.dict(exclude_unset=True))


@router.delete("/{uid}")
def deshabilitar_proyecto(uid: str):
    return ProyectoService.deshabilitar_proyecto(uid)
