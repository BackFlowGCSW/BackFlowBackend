from fpdf import FPDF
from datetime import date
from io import BytesIO
from fastapi.responses import StreamingResponse
from models.proyecto import Proyecto
from models.solicitud_cambio import SolicitudCambio
from models.tarea import Tarea

class ReporteService:
    @staticmethod
    def generar_estadisticas() -> dict:
        total_proyectos = len(Proyecto.nodes.all())
        total_solicitudes = len(SolicitudCambio.nodes.all())
        total_tareas = len(Tarea.nodes.all())

        solicitudes_por_estado = {
            estado: len(SolicitudCambio.nodes.filter(estado=estado))
            for estado in ["Pendiente", "Aprobada", "Rechazada", "Cerrada"]
        }

        tareas_por_estado = {
            estado: len(Tarea.nodes.filter(estado=estado))
            for estado in ["Planificada", "En proceso", "En Revision", "Finalizada", "Cancelada"]
        }

        tareas_por_prioridad = {
            prioridad: len(Tarea.nodes.filter(prioridad=prioridad))
            for prioridad in ["Alta", "Media", "Baja"]
        }

        return {
            "fecha": str(date.today()),
            "total_proyectos": total_proyectos,
            "total_solicitudes": total_solicitudes,
            "total_tareas": total_tareas,
            "solicitudes_por_estado": solicitudes_por_estado,
            "tareas_por_estado": tareas_por_estado,
            "tareas_por_prioridad": tareas_por_prioridad,
        }

    @staticmethod
    def exportar_pdf(estadisticas: dict):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt="📊 Reporte de Estadísticas del Sistema", ln=True, align="C")
        pdf.ln(10)

        def agregar_seccion(titulo, contenido):
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(200, 10, txt=titulo, ln=True)
            pdf.set_font("Arial", size=12)
            for k, v in contenido.items():
                pdf.cell(200, 10, txt=f"{k}: {v}", ln=True)
            pdf.ln(5)

        pdf.cell(200, 10, txt=f"Fecha del reporte: {estadisticas['fecha']}", ln=True)
        pdf.ln(5)

        pdf.cell(200, 10, txt=f"Total de Proyectos: {estadisticas['total_proyectos']}", ln=True)
        pdf.cell(200, 10, txt=f"Total de Solicitudes de Cambio: {estadisticas['total_solicitudes']}", ln=True)
        pdf.cell(200, 10, txt=f"Total de Tareas: {estadisticas['total_tareas']}", ln=True)
        pdf.ln(10)

        agregar_seccion("Solicitudes por Estado", estadisticas["solicitudes_por_estado"])
        agregar_seccion("Tareas por Estado", estadisticas["tareas_por_estado"])
        agregar_seccion("Tareas por Prioridad", estadisticas["tareas_por_prioridad"])

        pdf_output = BytesIO()
        pdf.output(pdf_output)
        pdf_output.seek(0)
        return StreamingResponse(pdf_output, media_type="application/pdf", headers={
            "Content-Disposition": "inline; filename=reporte_estadisticas.pdf"
        })
