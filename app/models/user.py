from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from ._mixins import TimestampMixin

class User(Base, TimestampMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    email: Mapped[str] = mapped_column(String(180), nullable=False, unique=True, index=True)
    role: Mapped[str] = mapped_column(String(50), nullable=False, default="staff")
    active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    # Relationships
    attendances: Mapped[list["Attendance"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    packages: Mapped[list["Package"]] = relationship(back_populates="created_by", cascade="all, delete-orphan")
