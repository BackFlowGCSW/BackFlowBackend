from datetime import date
from fastapi import HTTPException
from models.solicitud_cambio import SolicitudCambio
from models.usuario import Usuario
from models.tarea import Tarea


class SolicitudCambioService:
    ELEMENTOS_VALIDOS = {"Requisito", "Diseño", "Código", "Prueba", "Otro"}
    IMPACTOS_VALIDOS = {"Alto", "Medio", "Bajo"}
    ESFUERZOS_VALIDOS = {"Alto", "Medio", "Bajo"}

    @staticmethod
    def agregar_solicitud(data: dict) -> dict:
        """
        Crea una nueva solicitud de cambio, la vincula a un usuario creador y opcionalmente a una tarea.
        """

        # Validar existencia del usuario creador
        usuario = SolicitudCambioService._validar_usuario(data["creada_por"])

        # Validar campos controlados
        elemento = data.get("elemento", "")
        impacto = data.get("impacto", "")
        esfuerzo = data.get("esfuerzo", "")

        if elemento not in SolicitudCambioService.ELEMENTOS_VALIDOS:
            raise HTTPException(status_code=400, detail=f"Elemento inválido. Valores permitidos: {', '.join(SolicitudCambioService.ELEMENTOS_VALIDOS)}")

        if impacto not in SolicitudCambioService.IMPACTOS_VALIDOS:
            raise HTTPException(status_code=400, detail=f"Impacto inválido. Valores permitidos: {', '.join(SolicitudCambioService.IMPACTOS_VALIDOS)}")

        if esfuerzo not in SolicitudCambioService.ESFUERZOS_VALIDOS:
            raise HTTPException(status_code=400, detail=f"Esfuerzo inválido. Valores permitidos: {', '.join(SolicitudCambioService.ESFUERZOS_VALIDOS)}")

        # Crear la solicitud
        solicitud = SolicitudCambio(
            fecha_creacion=date.today(),
            objetivo=data.get("objetivo", ""),
            descripcion=data.get("descripcion", ""),
            elemento=elemento,
            impacto=impacto,
            esfuerzo=esfuerzo,
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

        # Relacionar solicitud con el usuario que la creó
        solicitud.asignado_a.connect(usuario)

        return {"mensaje": "Solicitud creada exitosamente", "uid": solicitud.uid}

    @staticmethod
    def cambiar_estado(uid: str, nuevo_estado: str, observacion: str) -> dict:
        """
        Cambia el estado de la solicitud de cambio, actualiza la observación y la fecha de cierre si corresponde.
        """
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
