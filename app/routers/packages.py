from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from app.deps import get_db, get_current_user
from app.models.package import Package
from app.models.user import User

router = APIRouter(prefix="/packages", tags=["packages"])


class PackageCreate(BaseModel):
    tracking_number: str = Field(..., min_length=3, max_length=60)
    description: str | None = None
    status: str = Field(default="received", max_length=30)


@router.get("/", status_code=status.HTTP_200_OK)
def get_packages(db: Session = Depends(get_db), _: User = Depends(get_current_user)):
    items = db.query(Package).order_by(Package.id.asc()).all()
    return {
        "items": [
            {
                "id": pkg.id,
                "tracking_number": pkg.tracking_number,
                "description": pkg.description,
                "status": pkg.status,
                "created_by_user_id": pkg.created_by_user_id,
                "created_at": pkg.created_at.isoformat() if pkg.created_at else None,
            }
            for pkg in items
        ],
        "count": len(items),
    }


@router.post("/", status_code=status.HTTP_201_CREATED)
def post_packages(
    payload: PackageCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    existing = db.query(Package).filter(Package.tracking_number == payload.tracking_number).first()
    if existing:
        raise HTTPException(status_code=400, detail="El tracking_number ya existe")

    pkg = Package(
        tracking_number=payload.tracking_number,
        description=payload.description,
        status=payload.status,
        created_by_user_id=current_user.id,
    )
    db.add(pkg)
    db.commit()
    db.refresh(pkg)

    return {
        "message": "Package created",
        "package": {
            "id": pkg.id,
            "tracking_number": pkg.tracking_number,
            "description": pkg.description,
            "status": pkg.status,
            "created_by_user_id": pkg.created_by_user_id,
            "created_at": pkg.created_at.isoformat() if pkg.created_at else None,
        },
    }
