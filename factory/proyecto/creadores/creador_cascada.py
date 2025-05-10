from models.fase import Fase
from models.rol import Rol
from models.proyecto import Proyecto
from .creador_proyecto import CreadorProyecto


class CreadorProyectoCascada(CreadorProyecto):
    def crear_proyecto(self, data: dict) -> Proyecto:
        return Proyecto(
            nombre=data["nombre"],
            descripcion=data.get("descripcion", ""),
            fecha_inicio=data.get("fecha_inicio"),
            fecha_fin=data.get("fecha_fin"),
            metodologia="Cascada",
            repositorio=data.get("repositorio", ""),
            activo=True
        )

    def crear_fases(self):
        fases = [
            Fase(nombre="Requisitos"),
            Fase(nombre="Diseño"),
            Fase(nombre="Implementación"),
            Fase(nombre="Verificación"),
            Fase(nombre="Mantenimiento")
        ]
        for fase in fases:
            fase.save()
        return fases

    def crear_roles(self):
        roles = [
            Rol(nombre="Analista"),
            Rol(nombre="Diseñador"),
            Rol(nombre="Programador"),
            Rol(nombre="Tester"),
            Rol(nombre="Gerente de Proyecto")
        ]
        for rol in roles:
            rol.save()
        return roles
