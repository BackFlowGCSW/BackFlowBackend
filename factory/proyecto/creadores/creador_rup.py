from models.fase import Fase
from models.rol import Rol
from models.proyecto import Proyecto
from .creador_proyecto import CreadorProyecto


class CreadorProyectoRUP(CreadorProyecto):
    def crear_proyecto(self, data: dict) -> Proyecto:
        return Proyecto(
            nombre=data["nombre"],
            descripcion=data.get("descripcion", ""),
            fecha_inicio=data.get("fecha_inicio"),
            fecha_fin=data.get("fecha_fin"),
            metodologia="RUP",
            repositorio=data.get("repositorio", ""),
            activo=True
        )

    def crear_fases(self):
        fases = [
            Fase(nombre="Inicio", descripcion="Fase de inicio"),
            Fase(nombre="Elaboración", descripcion="Fase de elaboración"),
            Fase(nombre="Construcción", descripcion="Fase de construcción"),
            Fase(nombre="Transición", descripcion="Fase de transición"),
        ]
        for fase in fases:
            fase.save()
        return fases

    def crear_roles(self):
        roles = [
            Rol(nombre="Arquitecto de Software",
                descripcion="Diseña la arquitectura"),
            Rol(nombre="Administrador de Configuración",
                descripcion="Gestiona configuración"),
            Rol(nombre="Miembro del Comité de Cambios",
                descripcion="Evalúa solicitudes"),
            Rol(nombre="Tester", descripcion="Verifica la calidad"),
            Rol(nombre="Desarrollador", descripcion="Programa las funcionalidades"),
        ]
        for rol in roles:
            rol.save()
        return roles
