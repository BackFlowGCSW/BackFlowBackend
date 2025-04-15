from fastapi import FastAPI
from routes.usuario_routes import router as usuarios_router
from routes.organizacion_routes import router as organizaciones_router
from routes.proyecto_routes import router as proyectos_router

import config.db

app = FastAPI()

app.include_router(usuarios_router)
app.include_router(organizaciones_router)
app.include_router(proyectos_router)