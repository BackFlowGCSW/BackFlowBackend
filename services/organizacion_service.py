from models.organizacion import Organizacion
from models.usuario import Usuario
from datetime import date
from fastapi import HTTPException
from typing import List


class OrganizacionService:
    @staticmethod
    def crear_organizacion(data: dict) -> Organizacion:
        """
        Crea una nueva organización y la asocia al usuario creador.
        """
        usuario = OrganizacionService._validar_usuario(data["creado_por"])

        if Organizacion.nodes.get_or_none(nombre=data["nombre"]):
            raise HTTPException(
                status_code=400, detail="Ya existe una organización con ese nombre.")

        organizacion = Organizacion(
            nombre=data["nombre"],
            descripcion=data.get("descripcion", ""),
            fecha_creacion=date.today(),
            creado_por=data["creado_por"],
            activa=True
        ).save()

        organizacion.tiene_miembros.connect(usuario)
        print(f"✅ Organización '{organizacion.nombre}' creada correctamente")
        return organizacion

    @staticmethod
    def listar_organizaciones() -> List[dict]:
        """
        Lista todas las organizaciones activas.
        """
        organizaciones = Organizacion.nodes.filter(activa=True)
        return [{
            "uid": org.uid,
            "nombre": org.nombre,
            "descripcion": org.descripcion,
            "fecha_creacion": org.fecha_creacion.isoformat(),
            "creado_por": org.creado_por
        } for org in organizaciones]

    @staticmethod
    def editar_organizacion(uid: str, data: dict):
        """
        Edita nombre o descripción de una organización.
        """
        org = Organizacion.nodes.get_or_none(uid=uid)
        if not org:
            raise HTTPException(
                status_code=404, detail="Organización no encontrada")

        if "nombre" in data:
            org.nombre = data["nombre"]
        if "descripcion" in data:
            org.descripcion = data["descripcion"]

        org.save()
        return {"mensaje": "Organización actualizada correctamente"}

    @staticmethod
    def deshabilitar_organizacion(uid: str):
        """
        Deshabilita una organización (soft delete).
        """
        org = Organizacion.nodes.get_or_none(uid=uid)
        if not org:
            raise HTTPException(
                status_code=404, detail="Organización no encontrada")

        org.activa = False
        org.save()
        return {"mensaje": "Organización deshabilitada"}

    # --------- Método privado ---------
    @staticmethod
    def _validar_usuario(uid: str) -> Usuario:
        usuario = Usuario.nodes.get_or_none(uid=uid)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no válido")
        return usuario
