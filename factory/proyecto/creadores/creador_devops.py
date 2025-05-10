from models.fase import Fase
from models.rol import Rol
from models.proyecto import Proyecto
from .creador_proyecto import CreadorProyecto


class CreadorProyectoDevOps(CreadorProyecto):
    def crear_proyecto(self, data: dict) -> Proyecto:
        return Proyecto(
            nombre=data["nombre"],
            descripcion=data.get("descripcion", ""),
            fecha_inicio=data.get("fecha_inicio"),
            fecha_fin=data.get("fecha_fin"),
            metodologia="DevOps",
            repositorio=data.get("repositorio", ""),
            activo=True
        )

    def crear_fases(self):
        fases = [
            Fase(nombre="Planificación"),
            Fase(nombre="Desarrollo"),
            Fase(nombre="Integración y entrega continua"),
            Fase(nombre="Operaciones"),
            Fase(nombre="Monitoreo y feedback")
        ]
        for fase in fases:
            fase.save()
        return fases

    def crear_roles(self):
        roles = [
            Rol(nombre="Desarrollador"),
            Rol(nombre="Ingeniero DevOps"),
            Rol(nombre="QA"),
            Rol(nombre="Administrador de sistemas")
        ]
        for rol in roles:
            rol.save()
        return roles
