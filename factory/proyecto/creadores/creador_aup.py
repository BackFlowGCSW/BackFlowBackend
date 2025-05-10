from models.fase import Fase
from models.rol import Rol
from models.proyecto import Proyecto
from .creador_proyecto import CreadorProyecto


class CreadorProyectoAUP(CreadorProyecto):
    def crear_proyecto(self, data: dict) -> Proyecto:
        return Proyecto(
            nombre=data["nombre"],
            descripcion=data.get("descripcion", ""),
            fecha_inicio=data.get("fecha_inicio"),
            fecha_fin=data.get("fecha_fin"),
            metodologia="AUP",
            repositorio=data.get("repositorio", ""),
            activo=True
        )

    def crear_fases(self):
        fases = [
            Fase(nombre="Inicio"),
            Fase(nombre="Elaboración"),
            Fase(nombre="Construcción"),
            Fase(nombre="Transición")
        ]
        for fase in fases:
            fase.save()
        return fases

    def crear_roles(self):
        roles = [
            Rol(nombre="Analista"),
            Rol(nombre="Diseñador"),
            Rol(nombre="Desarrollador"),
            Rol(nombre="Tester")
        ]
        for rol in roles:
            rol.save()
        return roles
