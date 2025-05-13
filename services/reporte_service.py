from fpdf import FPDF
from datetime import date
from io import BytesIO
from fastapi.responses import StreamingResponse
from models.proyecto import Proyecto
from models.solicitud_cambio import SolicitudCambio

class ReporteService:
    @staticmethod
    def generar_estadisticas() -> dict:
        total_proyectos = len(Proyecto.nodes.all())
        total_solicitudes = len(SolicitudCambio.nodes.all())
        solicitudes_pendientes = len(SolicitudCambio.nodes.filter(estado="Pendiente"))
        solicitudes_aprobadas = len(SolicitudCambio.nodes.filter(estado="Aprobada"))

        return {
            "fecha": str(date.today()),
            "total_proyectos": total_proyectos,
            "total_solicitudes": total_solicitudes,
            "pendientes": solicitudes_pendientes,
            "aprobadas": solicitudes_aprobadas,
        }

    @staticmethod
    def exportar_pdf(estadisticas: dict):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt="Reporte de Estadísticas de Sistema", ln=True, align="C")
        pdf.ln(10)
        for clave, valor in estadisticas.items():
            pdf.cell(200, 10, txt=f"{clave.replace('_', ' ').capitalize()}: {valor}", ln=True)

        pdf_output = BytesIO()
        pdf.output(pdf_output)
        pdf_output.seek(0)
        return StreamingResponse(pdf_output, media_type="application/pdf", headers={
            "Content-Disposition": "inline; filename=reporte_estadisticas.pdf"
        })
