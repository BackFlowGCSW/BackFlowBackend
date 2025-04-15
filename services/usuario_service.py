from models.usuario import Usuario
from datetime import date
from neomodel.exceptions import UniqueProperty


class UsuarioService:
    @staticmethod
    def crear_usuario(usuario_data: dict) -> Usuario:
        """
        Crea un nuevo usuario en el sistema.
        Args:
            data(dict): Contiene 'nombre', 'correo', 'password_hash'.
        Returns:
            Usuario creado.
        Raises:
            Exception si ya existe el correo.
        """
        if( Usuario.nodes.get_or_none(correo=usuario_data["correo"])):
            raise Exception("Ya existe un usuario con ese correo.")
        
        try:
            usuario = Usuario(
                nombre = usuario_data["nombre"],
                correo = usuario_data["correo"],
                password_hash = usuario_data["password_hash"],
                fecha_registro = date.today(),
                activo = True
            ).save()
            print(f"Usuario {usuario.nombre} creado correctamente.")
            return usuario
        except UniqueProperty as e:
            raise Exception("Ya existe un usuario con ese correo.") from e
