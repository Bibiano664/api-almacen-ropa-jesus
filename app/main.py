from fastapi import FastAPI
from app.routers import users, attendance, packages

app = FastAPI(
    title="API Almacén de Ropa",
    version="1.0.0",
    description="API REST para la gestión básica de un almacén de ropa"
)

app.include_router(users.router)
app.include_router(attendance.router)
app.include_router(packages.router)

@app.get("/")
def root():
    return {"message": "API Almacén de Ropa funcionando correctamente ✅"}