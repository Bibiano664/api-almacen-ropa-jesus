from fastapi import APIRouter

router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)

@router.get("/")
def get_attendance():
    return {"message": "Endpoint de asistencia activo (placeholder)"}