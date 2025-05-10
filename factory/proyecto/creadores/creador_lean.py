from models.fase import Fase
from models.rol import Rol
from models.proyecto import Proyecto
from .creador_proyecto import CreadorProyecto


class CreadorProyectoLean(CreadorProyecto):
    def crear_proyecto(self, data: dict) -> Proyecto:
        return Proyecto(
            nombre=data["nombre"],
            descripcion=data.get("descripcion", ""),
            fecha_inicio=data.get("fecha_inicio"),
            fecha_fin=data.get("fecha_fin"),
            metodologia="Lean",
            repositorio=data.get("repositorio", ""),
            activo=True
        )

    def crear_fases(self):
        fases = [
            Fase(nombre="Identificar valor"),
            Fase(nombre="Mapear flujo de valor"),
            Fase(nombre="Crear flujo continuo"),
            Fase(nombre="Establecer sistema pull"),
            Fase(nombre="Perfección continua")
        ]
        for fase in fases:
            fase.save()
        return fases

    def crear_roles(self):
        roles = [
            Rol(nombre="Líder de mejora continua"),
            Rol(nombre="Miembro del equipo"),
            Rol(nombre="Dueño del producto")
        ]
        for rol in roles:
            rol.save()
        return roles
