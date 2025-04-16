from models.tarea import Tarea
from models.proyecto import Proyecto
from models.usuario import Usuario
from models.fase import Fase
from fastapi import HTTPException
from datetime import date
from neomodel import db


class TareaService:
    PRIORIDADES_VALIDAS = {"Alta", "Media", "Baja"}
    ESTADOS_VALIDOS = {"Planificada", "En proceso",
                       "En revisión", "Finalizada", "Cancelada"}

    @staticmethod
    def crear_tarea(data: dict) -> Tarea:
        prioridad = data.get("prioridad", "Media")
        estado = data.get("estado", "Planificada")

        if prioridad not in TareaService.PRIORIDADES_VALIDAS:
            raise HTTPException(status_code=400, detail="Prioridad inválida")

        if estado not in TareaService.ESTADOS_VALIDOS:
            raise HTTPException(status_code=400, detail="Estado inválido")

        proyecto = Proyecto.nodes.get_or_none(uid=data["proyecto_id"])
        if not proyecto:
            raise HTTPException(
                status_code=404, detail="Proyecto no encontrado")

        fase = Fase.nodes.get_or_none(uid=data["fase_id"])
        if not fase:
            raise HTTPException(status_code=404, detail="Fase no encontrada")

        tarea = Tarea(
            titulo=data["titulo"],
            descripcion=data.get("descripcion", ""),
            fecha_creacion=date.today(),
            fecha_inicio=data.get("fecha_inicio"),
            fecha_fin=data.get("fecha_fin"),
            prioridad=prioridad,
            estado=estado
        )
        tarea.save()
        proyecto.tareas.connect(tarea)
        fase.tareas.connect(tarea)

        if data.get("asignado_a"):
            usuario = Usuario.nodes.get_or_none(uid=data["asignado_a"])
            if not usuario:
                raise HTTPException(
                    status_code=404, detail="Usuario no encontrado")
            tarea.asignado_a.connect(usuario)

        print(f"✅ Tarea '{tarea.titulo}' creada correctamente")
        return tarea.__properties__
    

    @staticmethod
    def editar_tarea(uid: str, data: dict):
        tarea = Tarea.nodes.get_or_none(uid=uid)
        if not tarea:
            raise HTTPException(status_code=404, detail="Tarea no encontrada")

        for campo in ["titulo", "descripcion", "fecha_inicio", "fecha_fin", "prioridad", "estado"]:
            if campo in data:
                setattr(tarea, campo, data[campo])

        if "asignado_a" in data:
            usuario = Usuario.nodes.get_or_none(uid=data["asignado_a"])
            if not usuario:
                raise HTTPException(
                    status_code=404, detail="Usuario no encontrado")
            tarea.asignado_a.disconnect_all()
            tarea.asignado_a.connect(usuario)

        if "fase_id" in data:
            fase = Fase.nodes.get_or_none(uid=data["fase_id"])
            if not fase:
                raise HTTPException(
                    status_code=404, detail="Fase no encontrada")
            tarea.tiene.disconnect_all()
            fase.tiene.connect(tarea)

        tarea.save()
        return {"mensaje": "Tarea actualizada correctamente"}

    @staticmethod
    def filtrar_por_prioridad(prioridad: str):
        if prioridad not in TareaService.PRIORIDADES_VALIDAS:
            raise HTTPException(status_code=400, detail="Prioridad inválida")
        tareas = Tarea.nodes.filter(prioridad=prioridad)
        return [{"uid": t.uid, "titulo": t.titulo, "estado": t.estado, "prioridad": t.prioridad} for t in tareas]

    @staticmethod
    def tareas_por_proyecto(proyecto_id: str):
        query = """
        MATCH (p:Proyecto {uid: $proyecto_id})-[:TIENE]->(t:Tarea)
        RETURN t
        """
        results, _ = db.cypher_query(query, {"proyecto_id": proyecto_id})
        return [Tarea.inflate(row[0]).__properties__ for row in results]

    @staticmethod
    def tareas_por_fase(fase_id: str):
        query = """
        MATCH (f:Fase {uid: $fase_id})-[:TIENE]->(t:Tarea)
        RETURN t
        """
        results, _ = db.cypher_query(query, {"fase_id": fase_id})
        return [Tarea.inflate(row[0]).__properties__ for row in results]

    @staticmethod
    def actualizar_estado(uid: str, nuevo_estado: str):
        if nuevo_estado not in TareaService.ESTADOS_VALIDOS:
            raise HTTPException(status_code=400, detail="Estado inválido")

        tarea = Tarea.nodes.get_or_none(uid=uid)
        if not tarea:
            raise HTTPException(status_code=404, detail="Tarea no encontrada")

        tarea.estado = nuevo_estado
        tarea.save()
        return {"mensaje": f"Estado de la tarea actualizado a '{nuevo_estado}'"}
