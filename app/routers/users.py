from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy.orm import Session

from app.deps import get_db, get_current_user
from app.models.user import User
from app.security import hash_password

router = APIRouter(prefix="/users", tags=["users"])


class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=120)
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=100)
    role: str = Field(default="staff", max_length=50)
    active: bool = True


class UserUpdate(BaseModel):
    name: str = Field(..., min_length=2, max_length=120)
    role: str = Field(..., max_length=50)
    active: bool = True


@router.get("/", status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db), _: User = Depends(get_current_user)):
    items = db.query(User).order_by(User.id.asc()).all()
    return {
        "items": [
            {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "role": user.role,
                "active": user.active,
            }
            for user in items
        ],
        "count": len(items),
    }


@router.post("/", status_code=status.HTTP_201_CREATED)
def post_user(payload: UserCreate, db: Session = Depends(get_db), _: User = Depends(get_current_user)):
    existing = db.query(User).filter(User.email == payload.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="El correo ya está registrado")

    user = User(
        name=payload.name,
        email=payload.email,
        password_hash=hash_password(payload.password),
        role=payload.role,
        active=payload.active,
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return {
        "message": "User created",
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role,
            "active": user.active,
        },
    }


@router.put("/{user_id}", status_code=status.HTTP_200_OK)
def put_user(user_id: int, payload: UserUpdate, db: Session = Depends(get_db), _: User = Depends(get_current_user)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    user.name = payload.name
    user.role = payload.role
    user.active = payload.active
    db.commit()
    db.refresh(user)

    return {
        "message": "User updated",
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role,
            "active": user.active,
        },
    }


@router.delete("/{user_id}", status_code=status.HTTP_200_OK)
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db), _: User = Depends(get_current_user)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    db.delete(user)
    db.commit()
    return {"message": "User deleted", "id": user_id}
