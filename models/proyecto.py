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

    fases = RelationshipTo('models.fase.Fase', 'TIENE')
    tareas = RelationshipTo('models.tarea.Tarea', 'TIENE')
    solicitudes = RelationshipFrom('models.solicitud_cambio.SolicitudCambio', 'PERTENECE_A')
    miembros = RelationshipFrom('models.usuario.Usuario', 'MIEMBRO_DE')
    pertenece_a = RelationshipFrom('models.organizacion.Organizacion', 'TIENE')
    tiene_rol = RelationshipFrom('models.rol.Rol', 'PARTE_DE')
