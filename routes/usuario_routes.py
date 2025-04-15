from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
from services.usuario_service import UsuarioService
from utils.security import get_current_user
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

# ----------- MODELOS ----------


class UsuarioCreate(BaseModel):
    nombre: str
    correo: str
    password: str


class LoginRequest(BaseModel):
    correo: str
    password: str

# ----------- RUTAS ------------


@router.post("/registro")
def registrar_usuario(data: UsuarioCreate):
    try:
        usuario = UsuarioService.crear_usuario(data.dict())
        return {"mensaje": f"Usuario {usuario.nombre} creado con éxito"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/")
def listar_usuarios():
    return UsuarioService.listar_usuarios()


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    credentials = {
        "correo": form_data.username,
        "password": form_data.password
    }
    return UsuarioService.login(credentials)


@router.get("/me")
def obtener_usuario_actual(usuario=Depends(get_current_user)):
    return {
        "uid": usuario.uid,
        "nombre": usuario.nombre,
        "correo": usuario.correo,
        "fecha_registro": usuario.fecha_registro.isoformat()
    }


@router.post("/logout")
def cerrar_sesion():
    return UsuarioService.cerrar_sesion()
