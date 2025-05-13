from datetime import date
from fastapi import HTTPException
from models.solicitud_cambio import SolicitudCambio
from models.usuario import Usuario
from models.tarea import Tarea
from models.proyecto import Proyecto


class SolicitudCambioService:
    IMPACTOS_VALIDOS = {"Alto", "Medio", "Bajo"}

    ELEMENTOS_POR_METODOLOGIA = {
        "SCRUM": {"Historias de Usuario", "Backlog", "Sprint", "Tarea", "Otro"},
        "RUP": {"Requisito", "Diseño", "Implementación", "Prueba", "Otro"},
    }

    @staticmethod
    def agregar_solicitud(data: dict) -> dict:
        # Validar el usuario que crea la solicitud
        creador = SolicitudCambioService._validar_usuario(data["creada_por"])

        # Validar proyecto y su metodología
        proyecto = Proyecto.nodes.get_or_none(uid=data["proyecto_id"])
        if not proyecto:
            raise HTTPException(status_code=404, detail="Proyecto no encontrado")

        metodologia = getattr(proyecto, "metodologia", None)
        if metodologia not in SolicitudCambioService.ELEMENTOS_POR_METODOLOGIA:
            raise HTTPException(status_code=400, detail="Metodología del proyecto no válida o no soportada")

        # Validar elemento
        elementos_validos = SolicitudCambioService.ELEMENTOS_POR_METODOLOGIA[metodologia]
        elemento = data.get("elemento", "")
        if elemento not in elementos_validos:
            raise HTTPException(
                status_code=400,
                detail=f"Elemento inválido para la metodología {metodologia}. Valores permitidos: {', '.join(elementos_validos)}"
            )

        # Validar impacto
        impacto = data.get("impacto", "")
        if impacto not in SolicitudCambioService.IMPACTOS_VALIDOS:
            raise HTTPException(
                status_code=400,
                detail=f"Impacto inválido. Valores permitidos: {', '.join(SolicitudCambioService.IMPACTOS_VALIDOS)}"
            )

        # Validar esfuerzo como número positivo
        esfuerzo = data.get("esfuerzo")
        try:
            esfuerzo_valor = float(esfuerzo)
            if esfuerzo_valor <= 0:
                raise ValueError
        except:
            raise HTTPException(
                status_code=400,
                detail="El esfuerzo debe ser un número positivo"
            )

        # Crear la solicitud
        solicitud = SolicitudCambio(
            fecha_creacion=date.today(),
            objetivo=data.get("objetivo", ""),
            descripcion=data.get("descripcion", ""),
            elemento=elemento,
            impacto=impacto,
            esfuerzo=esfuerzo_valor,
            estado="Pendiente",
            observacion="",
            creada_por=data["creada_por"],
            proyecto_id=data["proyecto_id"]
        ).save()

        # Relacionar con tarea si se proporciona
        tarea_id = data.get("tarea_id")
        if tarea_id:
            tarea = Tarea.nodes.get_or_none(uid=tarea_id)
            if not tarea:
                raise HTTPException(status_code=404, detail="Tarea no encontrada")
            solicitud.vinculada_a.connect(tarea)

        # Relacionar con el usuario asignado (distinto del creador)
        asignado_a_id = data.get("asignado_a")
        if not asignado_a_id:
            raise HTTPException(status_code=400, detail="Debe especificarse el usuario asignado")

        asignado_a = SolicitudCambioService._validar_usuario(asignado_a_id)
        solicitud.asignado_a.connect(asignado_a)

        return {"mensaje": "Solicitud creada exitosamente", "uid": solicitud.uid}

    @staticmethod
    def cambiar_estado(uid: str, nuevo_estado: str, observacion: str) -> dict:
        solicitud = SolicitudCambio.nodes.get_or_none(uid=uid)
        if not solicitud:
            raise HTTPException(status_code=404, detail="Solicitud no encontrada")

        if nuevo_estado not in ["Pendiente", "Aprobada", "Rechazada", "Cerrada"]:
            raise HTTPException(status_code=400, detail="Estado no válido")

        solicitud.estado = nuevo_estado
        solicitud.observacion = observacion

        if nuevo_estado in ["Aprobada", "Rechazada", "Cerrada"]:
            solicitud.fecha_cierre = date.today()

        solicitud.save()

        return {"mensaje": f"Estado actualizado a '{nuevo_estado}' correctamente"}

    # --------- Método privado ---------
    @staticmethod
    def _validar_usuario(uid: str) -> Usuario:
        usuario = Usuario.nodes.get_or_none(uid=uid)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no válido")
        return usuario
