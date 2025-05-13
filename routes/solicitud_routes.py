from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import date
from services.solicitud_service import SolicitudCambioService

router = APIRouter(prefix="/solicitudes-cambio", tags=["Solicitudes de Cambio"])


# ----------- SCHEMAS -----------

class SolicitudCambioCreate(BaseModel):
    objetivo: str
    descripcion: str
    elemento: str
    impacto: str
    esfuerzo: str
    proyecto_id: str
    creada_por: str
    tarea_id: Optional[str] = None


class SolicitudCambioUpdate(BaseModel):
    estado: str
    observacion: Optional[str] = None


# ----------- RUTAS ------------

@router.post("/")
def crear_solicitud(data: SolicitudCambioCreate):
    try:
        return SolicitudCambioService.agregar_solicitud(data.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{uid}")
def cambiar_estado(uid: str, data: SolicitudCambioUpdate):
    try:
        return SolicitudCambioService.cambiar_estado(
            uid=uid,
            nuevo_estado=data.estado,
            observacion=data.observacion or ""
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
