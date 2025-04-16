from neomodel import StructuredNode, StringProperty, DateProperty, BooleanProperty, UniqueIdProperty, RelationshipTo, RelationshipFrom


class SolicitudCambio(StructuredNode):
    uid = UniqueIdProperty()
    fecha_creacion = DateProperty(required=True)
    objetivo = StringProperty()
    descripcion = StringProperty()
    elemento = StringProperty()
    impacto = StringProperty()
    esfuerzo = StringProperty()
    estado = StringProperty(
        choices=[
            ("Pendiente", "Pendiente"),
            ("Aprobada", "Aprobada"),
            ("Rechazada", "Rechazada"),
            ("Cerrada", "Cerrada")
        ]
    )

    observacion = StringProperty()
    fecha_cierre = DateProperty()
    creada_por = StringProperty(required=True)
    proyecto_id = StringProperty(required=True)

    asignado_a = RelationshipFrom('models.usuario.Usuario', 'ASIGNADO_A')
    vinculada_a = RelationshipTo('models.tarea.Tarea', 'VINCULADA_A')
