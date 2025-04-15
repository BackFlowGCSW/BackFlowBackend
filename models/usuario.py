from neomodel import StructuredNode, StringProperty, DateProperty, BooleanProperty, UniqueIdProperty, RelationshipTo
from .organizacion import Organizacion
from .proyecto import Proyecto
from .rol import Rol
from .tarea import Tarea
from .solicitud_cambio import SolicitudCambio

class Usuario(StructuredNode):
    uid = UniqueIdProperty()
    nombre = StringProperty(required=True)
    correo = StringProperty(required=True, unique_index=True)
    password_hash = StringProperty(required=True)
    fecha_registro = DateProperty(required=True)
    activo = BooleanProperty(default=True)

    pertenece_a = RelationshipTo('Organizacion', 'PERTENECE_A')
    miembro_de = RelationshipTo('Proyecto', 'MIEMBRO_DE')
    cumple_rol = RelationshipTo('Rol', 'CUMPLE_ROL')
    asignado_a = RelationshipTo('Tarea', 'ASIGNADO_A')
    asignado_a_solicitud = RelationshipTo('SolicitudCambio', 'ASIGNADO_A')
