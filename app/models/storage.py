from sqlalchemy import String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from ._mixins import TimestampMixin

class StorageLocation(Base, TimestampMixin):
    __tablename__ = "storage_locations"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    code: Mapped[str] = mapped_column(String(50), nullable=False, unique=True, index=True)  # e.g., A1, B2
    description: Mapped[str | None] = mapped_column(String(200), nullable=True)

    package_links: Mapped[list["PackageStorage"]] = relationship(back_populates="location", cascade="all, delete-orphan")

class PackageStorage(Base, TimestampMixin):
    __tablename__ = "package_storage"
    __table_args__ = (
        UniqueConstraint("package_id", "location_id", name="uq_package_location"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    package_id: Mapped[int] = mapped_column(ForeignKey("packages.id"), nullable=False, index=True)
    location_id: Mapped[int] = mapped_column(ForeignKey("storage_locations.id"), nullable=False, index=True)

    package: Mapped["Package"] = relationship(back_populates="storage_links")
    location: Mapped["StorageLocation"] = relationship(back_populates="package_links")
