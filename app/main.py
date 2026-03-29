from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ✅ DB
from app.database import Base, engine
from app.models import *  # noqa: F401,F403  (importa modelos para crear tablas)

# ✅ Routers
from app.routers.health import router as health_router
from app.routers.users import router as users_router
from app.routers.attendance import router as attendance_router
from app.routers.packages import router as packages_router
from app.routers.auth import router as auth_router  # ✅ nuevo

# ✅ Crear tablas en la base de datos (SQLite)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Almacén de Ropa",
    version="1.0.0",
    description="API REST para la gestión básica de un almacén de ropa"
)

# CORS (solo para desarrollo)
# Permite que tu página HTML/JS (por ejemplo: http://127.0.0.1:5500)
# consuma la API sin errores de "CORS policy".
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "API Almacén de Ropa funcionando correctamente"}

# Routers
app.include_router(health_router)
app.include_router(auth_router)       #  nuevo (register/login/me)
app.include_router(users_router)
app.include_router(attendance_router)
app.include_router(packages_router)