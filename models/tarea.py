from neomodel import StructuredNode, StringProperty, DateProperty, BooleanProperty, UniqueIdProperty, RelationshipTo, RelationshipFrom


class Tarea(StructuredNode):
    uid = UniqueIdProperty()
    titulo = StringProperty(required=True)
    descripcion = StringProperty()
    fecha_creacion = DateProperty()
    fecha_inicio = DateProperty()
    fecha_fin = DateProperty()
    prioridad = StringProperty(choices=[("Alta", "Alta"), ("Media", "Media"), ("Baja", "Baja")])
    estado = StringProperty(choices=[("Planificada","Planificada"),("En proceso", "En proceso"), ("Finalizada", "Finalizada"),("En Revision", "En Revision"),("Cancelada", "Cancelada")])

    asignado_a = RelationshipFrom('models.usuario.Usuario', 'ASIGNADO_A')
    pertenece_a_fase = RelationshipFrom('models.fase.Fase', 'TIENE')
    pertenece_a_proyecto = RelationshipFrom('models.proyecto.Proyecto', 'TIENE')
    vinculada_a_solicitud = RelationshipFrom('models.solicitud_cambio.SolicitudCambio', 'VINCULADA_A')
