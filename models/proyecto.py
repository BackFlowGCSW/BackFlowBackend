from pydantic import BaseModel
from typing import Optional
from datetime import date

class ProyectoCreate(BaseModel):
    nombre: str
    descripcion: Optional[str]
    fechaInicio: Optional[date]
    fechaFin: Optional[date]
