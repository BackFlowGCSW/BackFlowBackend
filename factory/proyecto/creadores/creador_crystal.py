from models.fase import Fase
from models.rol import Rol
from models.proyecto import Proyecto
from .creador_proyecto import CreadorProyecto


class CreadorProyectoCrystal(CreadorProyecto):
    def crear_proyecto(self, data: dict) -> Proyecto:
        return Proyecto(
            nombre=data["nombre"],
            descripcion=data.get("descripcion", ""),
            fecha_inicio=data.get("fecha_inicio"),
            fecha_fin=data.get("fecha_fin"),
            metodologia="Crystal",
            repositorio=data.get("repositorio", ""),
            activo=True
        )

    def crear_fases(self):
        fases = [
            Fase(nombre="Charla de inicio"),
            Fase(nombre="Entrega incremental"),
            Fase(nombre="Revisión y adaptación")
        ]
        for fase in fases:
            fase.save()
        return fases

    def crear_roles(self):
        roles = [
            Rol(nombre="Líder técnico"),
            Rol(nombre="Desarrollador"),
            Rol(nombre="Usuario clave"),
            Rol(nombre="Facilitador"),
        ]
        for rol in roles:
            rol.save()
        return roles
