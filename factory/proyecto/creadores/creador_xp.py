from models.fase import Fase
from models.rol import Rol
from models.proyecto import Proyecto
from .creador_proyecto import CreadorProyecto


class CreadorProyectoXP(CreadorProyecto):
    def crear_proyecto(self, data: dict) -> Proyecto:
        return Proyecto(
            nombre=data["nombre"],
            descripcion=data.get("descripcion", ""),
            fecha_inicio=data.get("fecha_inicio"),
            fecha_fin=data.get("fecha_fin"),
            metodologia="XP",
            repositorio=data.get("repositorio", ""),
            activo=True
        )

    def crear_fases(self):
        fases = [
            Fase(nombre="Planificación"),
            Fase(nombre="Diseño"),
            Fase(nombre="Codificación"),
            Fase(nombre="Pruebas")
        ]
        for fase in fases:
            fase.save()
        return fases

    def crear_roles(self):
        roles = [
            Rol(nombre="Cliente"),
            Rol(nombre="Desarrollador"),
            Rol(nombre="Coach"),
            Rol(nombre="Tracker"),
            Rol(nombre="Tester")
        ]
        for rol in roles:
            rol.save()
        return roles
