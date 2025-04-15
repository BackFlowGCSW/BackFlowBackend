from neomodel import StructuredNode, StringProperty, DateProperty, BooleanProperty, UniqueIdProperty, RelationshipTo, RelationshipFrom


class Fase(StructuredNode):
    uid = UniqueIdProperty()
    nombre = StringProperty(required=True)
    descripcion = StringProperty()
    fecha_inicio = DateProperty()
    fecha_fin = DateProperty()

    tareas = RelationshipTo('Tarea', 'TIENE')
    pertenece_a = RelationshipFrom('Proyecto', 'TIENE')
