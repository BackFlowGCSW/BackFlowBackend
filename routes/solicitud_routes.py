from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
from datetime import date
from services.solicitud_service import SolicitudCambioService
from utils.security import get_current_user

router = APIRouter(prefix="/solicitudes-cambio", tags=["Solicitudes de Cambio"])

# ----------- SCHEMAS -----------

class SolicitudCambioCreate(BaseModel):
    objetivo: str
    descripcion: str
    elemento: str
    impacto: str
    esfuerzo: str
    proyecto_id: str
    tarea_id: Optional[str] = None


class SolicitudCambioUpdate(BaseModel):
    estado: str
    observacion: Optional[str] = None

# ----------- RUTAS ------------

@router.post("/")
def crear_solicitud(data: SolicitudCambioCreate, usuario=Depends(get_current_user)):
    try:
        payload = data.dict()
        payload["creada_por"] = usuario.uid
        return SolicitudCambioService.agregar_solicitud(payload)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{uid}")
def cambiar_estado(uid: str, data: SolicitudCambioUpdate, usuario=Depends(get_current_user)):
    try:
        return SolicitudCambioService.cambiar_estado(
            uid=uid,
            nuevo_estado=data.estado,
            observacion=data.observacion or ""
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
