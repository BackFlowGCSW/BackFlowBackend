from .creadores.creador_scrum import CreadorProyectoSCRUM
from .creadores.creador_rup import CreadorProyectoRUP
from .creadores.creador_proyecto import CreadorProyecto


class ProyectoFactory:
    @staticmethod
    def get_creador(metodologia: str) -> CreadorProyecto:
        if metodologia.upper() == "SCRUM":
            return CreadorProyectoSCRUM()
        elif metodologia.upper() == "RUP":
            return CreadorProyectoRUP()
        else:
            raise ValueError("Metodología no soportada: debe ser SCRUM o RUP")
