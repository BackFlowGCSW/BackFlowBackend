from fastapi import FastAPI
from routes.usuario_routes import router as usuarios_router
from routes.organizacion_routes import router as organizaciones_router
from routes.proyecto_routes import router as proyectos_router
from routes.tarea_routes import router as tareas_router
from routes.solicitud_routes import router as solicitudes_cambio_router
import config.db

app = FastAPI()

app.include_router(usuarios_router)
app.include_router(organizaciones_router)
app.include_router(proyectos_router)
app.include_router(tareas_router)
app.include_router(solicitudes_cambio_router)

@app.get("/")
def root():
    return {"message": "API de Gestión de Proyectos"}
