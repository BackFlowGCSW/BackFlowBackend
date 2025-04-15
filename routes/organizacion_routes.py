from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
from services.organizacion_service import OrganizacionService
from utils.security import get_current_user

router = APIRouter(prefix="/organizaciones", tags=["Organizaciones"])

# ----------- SCHEMAS -----------


class OrganizacionCreate(BaseModel):
    nombre: str
    descripcion: Optional[str] = ""


class OrganizacionUpdate(BaseModel):
    nombre: Optional[str]
    descripcion: Optional[str]


# ----------- RUTAS ------------

@router.post("/")
def crear_organizacion(data: OrganizacionCreate, usuario=Depends(get_current_user)):
    try:
        nueva_org = OrganizacionService.crear_organizacion({
            "nombre": data.nombre,
            "descripcion": data.descripcion,
            "creado_por": usuario.uid
        })
        return {"mensaje": "Organización creada exitosamente", "id": nueva_org.uid}
    except HTTPException as e:
        raise e


@router.get("/")
def listar_organizaciones():
    return OrganizacionService.listar_organizaciones()


@router.put("/{uid}")
def editar_organizacion(uid: str, data: OrganizacionUpdate):
    return OrganizacionService.editar_organizacion(uid, data.dict(exclude_unset=True))


@router.delete("/{uid}")
def deshabilitar_organizacion(uid: str):
    return OrganizacionService.deshabilitar_organizacion(uid)
