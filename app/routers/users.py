from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/")
def get_users():
    return {"message": "Endpoint de usuarios activo (placeholder)"}
