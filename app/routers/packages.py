from fastapi import APIRouter, status
from pydantic import BaseModel
from typing import Optional

from app.controllers.packages_controller import list_packages, create_package

router = APIRouter(prefix="/packages", tags=["packages"])


class PackageCreate(BaseModel):
    description: str
    origin: Optional[str] = None


@router.get("/", status_code=status.HTTP_200_OK)
def get_packages():
    items = list_packages()
    return {"items": items, "count": len(items)}


@router.post("/", status_code=status.HTTP_201_CREATED)
def post_packages(payload: PackageCreate):
    pkg = create_package(description=payload.description, origin=payload.origin)
    return {"message": "Package created", "package": pkg}
