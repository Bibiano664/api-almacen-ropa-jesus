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
    """Return the current in-memory users list."""
    return {"items": list_users(), "count": len(list_users())}


@router.post("/", status_code=status.HTTP_201_CREATED)
def post_user(payload: UserCreate):
    """Create a new user (in-memory)."""
    user = create_user(
        name=payload.name,
        role=payload.role,
        active=payload.active
    )
    return {"message": "User created", "user": user}
