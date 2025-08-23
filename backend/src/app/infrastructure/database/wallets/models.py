from uuid import UUID, uuid4

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.app.infrastructure.database.base import Base, BaseTimeStamped


class Wallet(Base):
    __tablename__ = "wallets"

    id: Mapped[UUID] = mapped_column(default=uuid4, primary_key=True)

    operations: Mapped[list["Operation"]] = relationship(
        back_populates="wallet", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Wallet(id={self.id})>"


class Operation(BaseTimeStamped):
    __tablename__ = "operations"

    id: Mapped[UUID] = mapped_column(default=uuid4, primary_key=True)
    wallet_id: Mapped[UUID] = mapped_column(ForeignKey("wallets.id"))

    wallet: Mapped["Wallet"] = relationship(back_populates="operations")

    def __repr__(self):
        return f"<User(id={self.id})>"
