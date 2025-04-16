from neomodel import StructuredNode, StringProperty, DateProperty, BooleanProperty, UniqueIdProperty, RelationshipTo

class Usuario(StructuredNode):
    uid = UniqueIdProperty()
    nombre = StringProperty(required=True)
    correo = StringProperty(required=True, unique_index=True)
    password_hash = StringProperty(required=True)
    fecha_registro = DateProperty(required=True)
    activo = BooleanProperty(default=True)

    pertenece_a = RelationshipTo('models.organizacion.Organizacion', 'PERTENECE_A')
    miembro_de = RelationshipTo('models.proyecto.Proyecto', 'MIEMBRO_DE')
    cumple_rol = RelationshipTo('models.rol.Rol', 'CUMPLE_ROL')
    asignado_a = RelationshipTo('models.tarea.Tarea', 'ASIGNADO_A')
    asignado_a_solicitud = RelationshipTo('models.solicitud_cambio.SolicitudCambio', 'ASIGNADO_A')
