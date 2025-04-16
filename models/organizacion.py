from neomodel import StructuredNode, StringProperty, DateProperty, BooleanProperty, UniqueIdProperty, RelationshipTo, RelationshipFrom

class Organizacion(StructuredNode):
    uid = UniqueIdProperty()
    nombre = StringProperty(required=True)
    descripcion = StringProperty()
    fecha_creacion = DateProperty(required=True)
    creado_por = StringProperty(required=True)
    activa = BooleanProperty(default=True)

    tiene_proyecto = RelationshipTo('models.proyecto.Proyecto', 'TIENE')
    tiene_miembros = RelationshipFrom('models.usuario.Usuario', 'PERTENECE_A')
