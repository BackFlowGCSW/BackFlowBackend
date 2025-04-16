from neomodel import StructuredNode, StringProperty, DateProperty, BooleanProperty, UniqueIdProperty, RelationshipTo, RelationshipFrom


class Fase(StructuredNode):
    uid = UniqueIdProperty()
    nombre = StringProperty(required=True)
    descripcion = StringProperty()
    fecha_inicio = DateProperty()
    fecha_fin = DateProperty()

    tareas = RelationshipTo('models.tarea.Tarea', 'TIENE')
    pertenece_a = RelationshipFrom('models.proyecto.Proyecto', 'TIENE')
