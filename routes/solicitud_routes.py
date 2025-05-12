from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import date
from models.solicitud_cambio import SolicitudCambio
from models.tarea import Tarea

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
    fecha_cierre: Optional[date] = None


# ----------- RUTAS ------------

@router.post("/")
def crear_solicitud(data: SolicitudCambioCreate):
    try:
        solicitud = SolicitudCambio(
            fecha_creacion=date.today(),
            objetivo=data.objetivo,
            descripcion=data.descripcion,
            elemento=data.elemento,
            impacto=data.impacto,
            esfuerzo=data.esfuerzo,
            estado="Pendiente",
            observacion="",
            creada_por=data.creada_por,
            proyecto_id=data.proyecto_id
        ).save()

        # Si se especificó una tarea, se vincula
        if data.tarea_id:
            tarea = Tarea.nodes.get_or_none(uid=data.tarea_id)
            if not tarea:
                raise HTTPException(status_code=404, detail="Tarea no encontrada")
            solicitud.vinculada_a.connect(tarea)

        return {"mensaje": "Solicitud de cambio creada", "uid": solicitud.uid}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{uid}")
def cambiar_estado(uid: str, data: SolicitudCambioUpdate):
    solicitud = SolicitudCambio.nodes.get_or_none(uid=uid)
    if not solicitud:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")

    solicitud.estado = data.estado

    if data.observacion:
        solicitud.observacion = data.observacion
    if data.fecha_cierre:
        solicitud.fecha_cierre = data.fecha_cierre

    solicitud.save()
    return {"mensaje": "Estado actualizado correctamente"}
