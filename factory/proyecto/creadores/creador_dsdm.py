from models.fase import Fase
from models.rol import Rol
from models.proyecto import Proyecto
from .creador_proyecto import CreadorProyecto


class CreadorProyectoDSDM(CreadorProyecto):
    def crear_proyecto(self, data: dict) -> Proyecto:
        return Proyecto(
            nombre=data["nombre"],
            descripcion=data.get("descripcion", ""),
            fecha_inicio=data.get("fecha_inicio"),
            fecha_fin=data.get("fecha_fin"),
            metodologia="DSDM",
            repositorio=data.get("repositorio", ""),
            activo=True
        )

    def crear_fases(self):
        fases = [
            Fase(nombre="Preproyecto"),
            Fase(nombre="Estudio de viabilidad"),
            Fase(nombre="Estudio de negocio"),
            Fase(nombre="Iteración funcional"),
            Fase(nombre="Implementación"),
            Fase(nombre="Postproyecto")
        ]
        for fase in fases:
            fase.save()
        return fases

    def crear_roles(self):
        roles = [
            Rol(nombre="Facilitador"),
            Rol(nombre="Arquitecto de soluciones"),
            Rol(nombre="Desarrollador"),
            Rol(nombre="Probador"),
            Rol(nombre="Usuario visionario")
        ]
        for rol in roles:
            rol.save()
        return roles
