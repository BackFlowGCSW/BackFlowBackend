from fastapi import APIRouter
from services.reporte_service import ReporteService

router = APIRouter(prefix="/reportes", tags=["Reportes"])

@router.get("/estadisticas")
def obtener_estadisticas():
    return ReporteService.generar_estadisticas()

@router.get("/pdf")
def exportar_estadisticas_pdf():
    estadisticas = ReporteService.generar_estadisticas()
    return ReporteService.exportar_pdf(estadisticas)
