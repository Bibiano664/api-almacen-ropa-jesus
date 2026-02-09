from sqlalchemy import String, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from ._mixins import TimestampMixin

class Package(Base, TimestampMixin):
    __tablename__ = "packages"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tracking_number: Mapped[str] = mapped_column(String(60), nullable=False, unique=True, index=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(String(30), nullable=False, default="received")

    created_by_user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, index=True)

    # Relationships
    created_by: Mapped["User"] = relationship(back_populates="packages")
    items: Mapped[list["PackageItem"]] = relationship(back_populates="package", cascade="all, delete-orphan")

    tag_links: Mapped[list["PackageTag"]] = relationship(back_populates="package", cascade="all, delete-orphan")

    storage_links: Mapped[list["PackageStorage"]] = relationship(back_populates="package", cascade="all, delete-orphan")

class PackageItem(Base, TimestampMixin):
    __tablename__ = "package_items"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    package_id: Mapped[int] = mapped_column(ForeignKey("packages.id"), nullable=False, index=True)

    sku: Mapped[str | None] = mapped_column(String(60), nullable=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False, default=1)

    package: Mapped["Package"] = relationship(back_populates="items")
