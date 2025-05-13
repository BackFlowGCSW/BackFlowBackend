from fastapi import APIRouter
from services.reporte_service import ReporteService

router = APIRouter(prefix="/reportes", tags=["Reportes"])

@router.get("/estadisticas/{uid_proyecto}")
def obtener_estadisticas(uid_proyecto: str):
    return ReporteService.generar_estadisticas(uid_proyecto)

@router.get("/pdf/{uid_proyecto}")
def exportar_estadisticas_pdf(uid_proyecto: str):
    estadisticas = ReporteService.generar_estadisticas(uid_proyecto)
    return ReporteService.exportar_pdf(estadisticas)
