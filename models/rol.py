from neomodel import StructuredNode, StringProperty, DateProperty, BooleanProperty, UniqueIdProperty, RelationshipTo, RelationshipFrom

class Rol(StructuredNode):
    uid = UniqueIdProperty()
    nombre = StringProperty(required=True)
    descripcion = StringProperty()

    asignado_a = RelationshipFrom('Usuario', 'CUMPLE_ROL')
    parte_de = RelationshipTo('Proyecto', 'PARTE_DE')
