from abc import ABC, abstractmethod
from typing import List
from models.fase import Fase
from models.rol import Rol
from models.proyecto import Proyecto


class CreadorProyecto(ABC):
    @abstractmethod
    def crear_proyecto(self, data: dict) -> Proyecto:
        pass

    @abstractmethod
    def crear_fases(self) -> List[Fase]:
        pass

    @abstractmethod
    def crear_roles(self) -> List[Rol]:
        pass
