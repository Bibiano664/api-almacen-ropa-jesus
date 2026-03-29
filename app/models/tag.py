from sqlalchemy import String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from ._mixins import TimestampMixin

class Tag(Base, TimestampMixin):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(80), nullable=False, unique=True, index=True)

    package_links: Mapped[list["PackageTag"]] = relationship(back_populates="tag", cascade="all, delete-orphan")

class PackageTag(Base, TimestampMixin):
    __tablename__ = "package_tags"
    __table_args__ = (
        UniqueConstraint("package_id", "tag_id", name="uq_package_tag"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    package_id: Mapped[int] = mapped_column(ForeignKey("packages.id"), nullable=False, index=True)
    tag_id: Mapped[int] = mapped_column(ForeignKey("tags.id"), nullable=False, index=True)

    package: Mapped["Package"] = relationship(back_populates="tag_links")
    tag: Mapped["Tag"] = relationship(back_populates="package_links")
