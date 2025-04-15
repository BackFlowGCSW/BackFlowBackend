from models.fase import Fase
from models.rol import Rol
from models.proyecto import Proyecto
from .creador_proyecto import CreadorProyecto


class CreadorProyectoSCRUM(CreadorProyecto):
    def crear_proyecto(self, data: dict) -> Proyecto:
        return Proyecto(
            nombre=data["nombre"],
            descripcion=data.get("descripcion", ""),
            fecha_inicio=data.get("fecha_inicio"),
            fecha_fin=data.get("fecha_fin"),
            metodologia="SCRUM",
            repositorio=data.get("repositorio", ""),
            activo=True
        )

    def crear_fases(self):
        fases = [
            Fase(nombre="Sprint Planning",
                 descripcion="Planificación del sprint"),
            Fase(nombre="Development", descripcion="Desarrollo del sprint"),
            Fase(nombre="Sprint Review", descripcion="Revisión del sprint"),
            Fase(nombre="Retrospective", descripcion="Retrospectiva del sprint"),
        ]
        for fase in fases:
            fase.save()
        return fases

    def crear_roles(self):
        roles = [
            Rol(nombre="Scrum Master", descripcion="Facilita el proceso SCRUM"),
            Rol(nombre="Product Owner",
                descripcion="Define requisitos del producto"),
            Rol(nombre="Developer", descripcion="Desarrolla funcionalidades"),
            Rol(nombre="QA", descripcion="Asegura calidad del producto"),
        ]
        for rol in roles:
            rol.save()
        return roles
