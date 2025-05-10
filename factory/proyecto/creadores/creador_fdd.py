from models.fase import Fase
from models.rol import Rol
from models.proyecto import Proyecto
from .creador_proyecto import CreadorProyecto


class CreadorProyectoFDD(CreadorProyecto):
    def crear_proyecto(self, data: dict) -> Proyecto:
        return Proyecto(
            nombre=data["nombre"],
            descripcion=data.get("descripcion", ""),
            fecha_inicio=data.get("fecha_inicio"),
            fecha_fin=data.get("fecha_fin"),
            metodologia="FDD",
            repositorio=data.get("repositorio", ""),
            activo=True
        )

    def crear_fases(self):
        fases = [
            Fase(nombre="Desarrollar modelo general"),
            Fase(nombre="Crear lista de funcionalidades"),
            Fase(nombre="Plan por funcionalidad"),
            Fase(nombre="Diseñar por funcionalidad"),
            Fase(nombre="Construir por funcionalidad")
        ]
        for fase in fases:
            fase.save()
        return fases

    def crear_roles(self):
        roles = [
            Rol(nombre="Propietario del dominio"),
            Rol(nombre="Arquitecto"),
            Rol(nombre="Desarrollador principal"),
            Rol(nombre="Desarrollador"),
            Rol(nombre="Tester")
        ]
        for rol in roles:
            rol.save()
        return roles
