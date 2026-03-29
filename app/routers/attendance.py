from fastapi import APIRouter, Depends, status
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from app.deps import get_db, get_current_user
from app.models.attendance import Attendance
from app.models.user import User

router = APIRouter(prefix="/attendance", tags=["attendance"])


class AttendanceCreate(BaseModel):
    action: str = Field(..., description="Valores válidos: check-in, check-out, in, out")


@router.get("/", status_code=status.HTTP_200_OK)
def get_attendance(db: Session = Depends(get_db), _: User = Depends(get_current_user)):
    items = db.query(Attendance).order_by(Attendance.id.asc()).all()
    return {
        "items": [
            {
                "id": record.id,
                "user_id": record.user_id,
                "type": record.type,
                "timestamp": record.timestamp.isoformat() if record.timestamp else None,
            }
            for record in items
        ],
        "count": len(items),
    }


@router.post("/", status_code=status.HTTP_201_CREATED)
def post_attendance(
    payload: AttendanceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    normalized = payload.action.strip().lower()
    if normalized in {"check-in", "in", "entrada"}:
        normalized = "in"
    elif normalized in {"check-out", "out", "salida"}:
        normalized = "out"

    record = Attendance(user_id=current_user.id, type=normalized)
    db.add(record)
    db.commit()
    db.refresh(record)

    return {
        "message": "Attendance registered",
        "attendance": {
            "id": record.id,
            "user_id": record.user_id,
            "type": record.type,
            "timestamp": record.timestamp.isoformat() if record.timestamp else None,
        },
    }
