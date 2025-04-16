from neomodel import StructuredNode, StringProperty, DateProperty, BooleanProperty, UniqueIdProperty, RelationshipTo, RelationshipFrom

class Rol(StructuredNode):
    uid = UniqueIdProperty()
    nombre = StringProperty(required=True)
    descripcion = StringProperty()

    asignado_a = RelationshipFrom('models.usuario.Usuario', 'CUMPLE_ROL')
    parte_de = RelationshipTo('models.proyecto.Proyecto', 'PARTE_DE')
