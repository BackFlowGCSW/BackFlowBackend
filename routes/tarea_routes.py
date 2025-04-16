from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional
from services.tarea_service import TareaService
from utils.security import get_current_user
from datetime import date

router = APIRouter(prefix="/tareas", tags=["Tareas"])

# ----------- SCHEMAS -----------


class TareaCreate(BaseModel):
    titulo: str
    descripcion: Optional[str] = ""
    fecha_inicio: Optional[date] = None
    fecha_fin: Optional[date] = None
    prioridad: Optional[str] = "Media"
    estado: Optional[str] = "Planificada"
    proyecto_id: str
    fase_id: str
    asignado_a: Optional[str] = None


class EstadoUpdate(BaseModel):
    estado: str


class TareaUpdate(BaseModel):
    titulo: Optional[str]
    descripcion: Optional[str]
    fecha_inicio: Optional[date]
    fecha_fin: Optional[date]
    prioridad: Optional[str]
    estado: Optional[str]
    asignado_a: Optional[str]
    fase_id: Optional[str]


# ----------- RUTAS ------------

@router.post("/")
def crear_tarea(data: TareaCreate, usuario=Depends(get_current_user)):
    return TareaService.crear_tarea(data.dict())


@router.put("/{uid}")
def actualizar_tarea(uid: str, data: TareaUpdate, usuario=Depends(get_current_user)):
    return TareaService.editar_tarea(uid, data.dict(exclude_unset=True))


@router.get("/por-prioridad/{prioridad}")
def tareas_por_prioridad(prioridad: str):
    return TareaService.filtrar_por_prioridad(prioridad)


@router.get("/por-proyecto/{proyecto_id}")
def listar_tareas_proyecto(proyecto_id: str):
    return TareaService.tareas_por_proyecto(proyecto_id)


@router.get("/por-fase/{fase_id}")
def tareas_por_fase(fase_id: str):
    return TareaService.tareas_por_fase(fase_id)


@router.patch("/{uid}/estado")
def actualizar_estado_tarea(uid: str, body: EstadoUpdate):
    return TareaService.actualizar_estado(uid, body.estado)
