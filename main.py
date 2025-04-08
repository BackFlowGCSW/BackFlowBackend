from fastapi import FastAPI
from routes import proyectos

app = FastAPI()

app.include_router(proyectos.router, prefix="/proyectos", tags=["Proyectos"])
