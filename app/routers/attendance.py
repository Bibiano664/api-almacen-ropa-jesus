from fastapi import APIRouter, status
from pydantic import BaseModel

from app.controllers.attendance_controller import list_attendance, create_attendance

router = APIRouter(prefix="/attendance", tags=["attendance"])


class AttendanceCreate(BaseModel):
    user_id: int
    action: str  # e.g. "check-in" or "check-out"


@router.get("/", status_code=status.HTTP_200_OK)
def get_attendance():
    """Return attendance records (in-memory)."""
    items = list_attendance()
    return {"items": items, "count": len(items)}


@router.post("/", status_code=status.HTTP_201_CREATED)
def post_attendance(payload: AttendanceCreate):
    record = create_attendance(user_id=payload.user_id, action=payload.action)
    return {"message": "Attendance registered", "attendance": record}
