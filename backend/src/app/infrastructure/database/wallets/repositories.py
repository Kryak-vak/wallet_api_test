from sqlalchemy import Select
from sqlalchemy.orm import selectinload

from src.app.application.wallets.dto import (
    OperationCreateDTO,
    OperationDTO,
    OperationUpdateDTO,
    WalletCreateDTO,
    WalletDTO,
    WalletUpdateDTO,
)
from src.app.application.wallets.repositories import IOperationRepository, IWalletRepository
from src.app.infrastructure.database import AbstractSQLAlchemyRepository
from src.app.infrastructure.database.wallets.models import Operation, Wallet


class SQLAlchemyWalletRepository(
    AbstractSQLAlchemyRepository[Wallet, WalletDTO, WalletCreateDTO, WalletUpdateDTO],
    IWalletRepository,
):
    model = Wallet
    read_dto = WalletDTO

    def _apply_loader_options(self, stmt: Select) -> Select:
        return stmt.options(selectinload(Wallet.operations))


class SQLAlchemyOperationRepository(
    AbstractSQLAlchemyRepository[Operation, OperationDTO, OperationCreateDTO, OperationUpdateDTO],
    IOperationRepository,
):
    model = Operation
    read_dto = OperationDTO

    def _apply_loader_options(self, stmt: Select) -> Select:
        return stmt.options(selectinload(Wallet.operations))
