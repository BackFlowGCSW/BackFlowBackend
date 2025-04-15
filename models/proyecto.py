from neomodel import StructuredNode, StringProperty, DateProperty, BooleanProperty, UniqueIdProperty, RelationshipTo, RelationshipFrom


class Proyecto(StructuredNode):
    uid = UniqueIdProperty()
    nombre = StringProperty(required=True)
    descripcion = StringProperty()
    fecha_creacion = DateProperty(required=True)
    fecha_inicio = DateProperty()
    fecha_fin = DateProperty()
    metodologia = StringProperty(required=True)
    repositorio = StringProperty()
    activo = BooleanProperty(default=True)
    creado_por = StringProperty(required=True)

    fases = RelationshipTo('Fase', 'TIENE')
    tareas = RelationshipTo('Tarea', 'TIENE')
    solicitudes = RelationshipFrom('SolicitudCambio', 'PERTENECE_A')
    miembros = RelationshipFrom('Usuario', 'MIEMBRO_DE')
    pertenece_a = RelationshipFrom('Organizacion', 'TIENE')
    tiene_rol = RelationshipFrom('Rol', 'PARTE_DE')
