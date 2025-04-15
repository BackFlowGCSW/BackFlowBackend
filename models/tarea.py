from neomodel import StructuredNode, StringProperty, DateProperty, BooleanProperty, UniqueIdProperty, RelationshipTo, RelationshipFrom


class Tarea(StructuredNode):
    uid = UniqueIdProperty()
    titulo = StringProperty(required=True)
    descripcion = StringProperty()
    fecha_creacion = DateProperty()
    fecha_inicio = DateProperty()
    fecha_fin = DateProperty()
    prioridad = StringProperty(choices=[("Alta", "Alta"), ("Media", "Media"), ("Baja", "Baja")])
    estado = StringProperty(choices=[("En proceso", "En proceso"), ("Finalizada", "Finalizada")])

    asignado_a = RelationshipFrom('Usuario', 'ASIGNADO_A')
    pertenece_a_fase = RelationshipFrom('Fase', 'TIENE')
    pertenece_a_proyecto = RelationshipFrom('Proyecto', 'TIENE')
    vinculada_a_solicitud = RelationshipFrom('SolicitudCambio', 'VINCULADA_A')
