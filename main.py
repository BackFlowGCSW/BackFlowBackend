import config.db

from services.usuario_service import UsuarioService

if __name__ == "__main__":
    user_data = {
        "nombre": "Carlos Gómez",
        "correo": "carlos@tekno.com",
        "password_hash": "hash789"
    }

    try:
        usuario = UsuarioService.crear_usuario(user_data)
        print(f"✅ Usuario creado: {usuario.nombre}")
    except Exception as e:
        print(f"❌ Error: {e}")
