from fastapi import APIRouter

router = APIRouter(
    prefix="/packages",
    tags=["Packages"]
)

@router.get("/")
def get_packages():
    return {"message": "Endpoint de paquetes activo (placeholder)"}