from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

from routes.usuario_routes import router as usuarios_router
from routes.organizacion_routes import router as organizaciones_router
from routes.proyecto_routes import router as proyectos_router
from routes.tarea_routes import router as tareas_router
from routes.solicitud_routes import router as solicitudes_cambio_router
from routes.reporte_routes import router as reporte_router

import config.db

app = FastAPI(
    title="Gestión de Proyectos API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS: en DEV puedes usar ["*"], en PROD especifica tus dominios
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/favicon.ico", include_in_schema=False)
async def ignore_favicon():
    return Response(status_code=204)

# Incluimos todos los routers
app.include_router(usuarios_router)
app.include_router(organizaciones_router)
app.include_router(proyectos_router)
app.include_router(tareas_router)
app.include_router(solicitudes_cambio_router)
app.include_router(reporte_router)

@app.get("/", tags=["Health"])
def root():
    return {"message": "API de Gestión de Proyectos corriendo"}
