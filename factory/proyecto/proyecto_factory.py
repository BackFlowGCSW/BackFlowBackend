from .creadores.creador_scrum import CreadorProyectoSCRUM
from .creadores.creador_rup import CreadorProyectoRUP
from .creadores.creador_xp import CreadorProyectoXP
from .creadores.creador_kanban import CreadorProyectoKANBAN
from .creadores.creador_cascada import CreadorProyectoCascada
from .creadores.creador_lean import CreadorProyectoLean
from .creadores.creador_dsdm import CreadorProyectoDSDM
from .creadores.creador_fdd import CreadorProyectoFDD
from .creadores.creador_crystal import CreadorProyectoCrystal
from .creadores.creador_aup import CreadorProyectoAUP
from .creadores.creador_safe import CreadorProyectoSafe
from .creadores.creador_devops import CreadorProyectoDevOps
from .creadores.creador_proyecto import CreadorProyecto


class ProyectoFactory:
    @staticmethod
    def get_creador(metodologia: str) -> CreadorProyecto:
        metodologia = metodologia.upper()
        if metodologia == "SCRUM":
            return CreadorProyectoSCRUM()
        elif metodologia == "RUP":
            return CreadorProyectoRUP()
        elif metodologia == "XP":
            return CreadorProyectoXP()
        elif metodologia == "KANBAN":
            return CreadorProyectoKANBAN()
        elif metodologia == "CASCADA":
            return CreadorProyectoCascada()
        elif metodologia == "LEAN":
            return CreadorProyectoLean()
        elif metodologia == "DSDM":
            return CreadorProyectoDSDM()
        elif metodologia == "FDD":
            return CreadorProyectoFDD()
        elif metodologia == "CRYSTAL":
            return CreadorProyectoCrystal()
        elif metodologia == "AUP":
            return CreadorProyectoAUP()
        elif metodologia == "SAFE":
            return CreadorProyectoSafe()
        elif metodologia == "DEVOPS":
            return CreadorProyectoDevOps()
        else:
            raise ValueError(f"Metodología no soportada: {metodologia}")
