from models.fase import Fase
from models.rol import Rol
from models.proyecto import Proyecto
from .creador_proyecto import CreadorProyecto


class CreadorProyectoSafe(CreadorProyecto):
    def crear_proyecto(self, data: dict) -> Proyecto:
        return Proyecto(
            nombre=data["nombre"],
            descripcion=data.get("descripcion", ""),
            fecha_inicio=data.get("fecha_inicio"),
            fecha_fin=data.get("fecha_fin"),
            metodologia="SAFe",
            repositorio=data.get("repositorio", ""),
            activo=True
        )

    def crear_fases(self):
        fases = [
            Fase(nombre="Planificación del tren ágil"),
            Fase(nombre="Ejecución"),
            Fase(nombre="Inspección y adaptación")
        ]
        for fase in fases:
            fase.save()
        return fases

    def crear_roles(self):
        roles = [
            Rol(nombre="Release Train Engineer"),
            Rol(nombre="Product Owner"),
            Rol(nombre="Scrum Master"),
            Rol(nombre="Equipo Ágil")
        ]
        for rol in roles:
            rol.save()
        return roles
