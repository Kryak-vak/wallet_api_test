from sqlalchemy import Select
from sqlalchemy.orm import selectinload

from src.app.application.wallets.repositories import IOperationRepository, IWalletRepository
from src.app.domain.entities import Operation as OperationEntity
from src.app.domain.entities import Wallet as WalletEntity
from src.app.infrastructure.database import AbstractSQLAlchemyRepository
from src.app.infrastructure.database.wallets.mappers import OperationMapper, WalletMapper
from src.app.infrastructure.database.wallets.models import Operation, Wallet


class SQLAlchemyWalletRepository(
    AbstractSQLAlchemyRepository[Wallet, WalletEntity], IWalletRepository
):
    model = Wallet
    entity_class = WalletEntity
    mapper = WalletMapper

    def _apply_loader_options(self, stmt: Select) -> Select:
        return stmt.options(selectinload(Wallet.operations))


class SQLAlchemyOperationRepository(
    AbstractSQLAlchemyRepository[Operation, OperationEntity], IOperationRepository
):
    model = Operation
    entity_class = OperationEntity
    mapper = OperationMapper

    def _apply_loader_options(self, stmt: Select) -> Select:
        return stmt.options(selectinload(Wallet.operations))
