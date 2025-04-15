from models.usuario import Usuario
from datetime import date
from neomodel.exceptions import UniqueProperty
from typing import List
from fastapi import HTTPException
from utils.security import hashear_password, verificar_password, crear_token


class UsuarioService:
    @staticmethod
    def crear_usuario(usuario_data: dict) -> Usuario:
        """
        Crea un nuevo usuario con el password hasheado.
        """
        if Usuario.nodes.get_or_none(correo=usuario_data["correo"]):
            raise HTTPException(status_code=400, detail="Ya existe un usuario con ese correo.")

        try:
            usuario = Usuario(
                nombre=usuario_data["nombre"],
                correo=usuario_data["correo"],
                password_hash=hashear_password(usuario_data["password"]),
                fecha_registro=date.today(),
                activo=True
            ).save()
            print(f"✅ Usuario {usuario.nombre} creado correctamente.")
            return usuario
        except UniqueProperty as e:
            raise HTTPException(status_code=400, detail="Error de duplicidad") from e

    @staticmethod
    def listar_usuarios() -> List[dict]:
        """
        Retorna todos los usuarios activos.
        """
        usuarios = Usuario.nodes.filter(activo=True)
        return [{
            "uid": u.uid,
            "nombre": u.nombre,
            "correo": u.correo,
            "fecha_registro": u.fecha_registro.isoformat(),
        } for u in usuarios]

    @staticmethod
    def login(data: dict) -> dict:
        """
        Autentica al usuario y retorna el JWT.
        """
        usuario = Usuario.nodes.get_or_none(correo=data["correo"])
        if not usuario or not verificar_password(data["password"], usuario.password_hash):
            raise HTTPException(status_code=401, detail="Credenciales inválidas")

        token = crear_token({"sub": usuario.correo})
        return {"access_token": token, "token_type": "bearer"}

    @staticmethod
    def cerrar_sesion():
        return {"mensaje": "Sesión cerrada exitosamente"}
