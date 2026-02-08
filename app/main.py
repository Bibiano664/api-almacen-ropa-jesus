from fastapi import FastAPI

from app.routers.health import router as health_router
from app.routers.users import router as users_router
# Si ya tienes attendance/packages, déjalos como estaban:
# from app.routers.attendance import router as attendance_router
# from app.routers.packages import router as packages_router

app = FastAPI(title="API Almacén de Ropa")

@app.get("/")
def root():
    return {"message": "API Almacén de Ropa funcionando correctamente"}

app.include_router(health_router)
app.include_router(users_router)

# Si ya existen en tu proyecto, los vuelves a incluir:
# app.include_router(attendance_router)
# app.include_router(packages_router)
