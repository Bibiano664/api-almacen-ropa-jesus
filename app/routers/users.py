from fastapi import APIRouter, status
from pydantic import BaseModel

from app.controllers.users_controller import list_users, create_user

router = APIRouter(prefix="/users", tags=["users"])


class UserCreate(BaseModel):
    name: str
    role: str
    active: bool = True


@router.get("/", status_code=status.HTTP_200_OK)
def get_users():
    return list_users()


@router.post("/", status_code=status.HTTP_201_CREATED)
def post_user(payload: UserCreate):
    return create_user(
        name=payload.name,
        role=payload.role,
        active=payload.active
    )
