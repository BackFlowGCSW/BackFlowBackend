from fastapi import APIRouter, HTTPException
from typing import Dict
from pydantic import BaseModel
from services.reporte_service import ReporteService

router = APIRouter(prefix="/reportes", tags=["Reportes"])


# ----------- SCHEMA -----------
class EstadisticasReporte(BaseModel):
    fecha: str
    proyecto: str
    total_solicitudes: int
    total_tareas: int
    solicitudes_por_estado: Dict[str, int]
    tareas_por_estado: Dict[str, int]
    tareas_por_prioridad: Dict[str, int]


# ----------- RUTAS -----------
@router.get("/estadisticas/{uid_proyecto}", response_model=EstadisticasReporte)
def obtener_estadisticas(uid_proyecto: str):
    return ReporteService.generar_estadisticas(uid_proyecto)

@router.get("/pdf/{uid_proyecto}")
def exportar_estadisticas_pdf(uid_proyecto: str):
    estadisticas = ReporteService.generar_estadisticas(uid_proyecto)
    return ReporteService.exportar_pdf(estadisticas)
