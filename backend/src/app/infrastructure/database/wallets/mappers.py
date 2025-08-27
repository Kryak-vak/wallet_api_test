from decimal import Decimal
from uuid import UUID

from src.app.domain.entities import Operation as OperationEntity
from src.app.domain.entities import Wallet as WalletEntity
from src.app.domain.value_objects import Money, OperationType
from src.app.infrastructure.database.base.mappers import AbstractMapper
from src.app.infrastructure.database.wallets.models import Operation, Wallet


class OperationMapper(AbstractMapper[Operation, OperationEntity]):
    @classmethod
    def to_entity(cls, model: Operation) -> OperationEntity:
        return OperationEntity(
            id=model.id,
            type=model.type,
            amount=Money(amount=Decimal(model.amount)),
            wallet_id=model.wallet_id,
        )

    @classmethod
    def to_model(cls, entity: OperationEntity) -> Operation:
        return Operation(
            id=entity.id, type=entity.type, amount=entity.amount, wallet_id=entity.wallet_id
        )

    @classmethod
    def create_dump(cls, entity: OperationEntity) -> dict[str, UUID | OperationType | Decimal]:
        return {
            "id": entity.id,
            "type": entity.type,
            "amount": entity.amount.amount,
            "wallet_id": entity.wallet_id,
        }


class WalletMapper(AbstractMapper[Wallet, WalletEntity]):
    @classmethod
    def to_entity(cls, model: Wallet) -> WalletEntity:
        return WalletEntity(
            id=model.id,
            balance=Money(amount=Decimal(model.balance)),
            operations=[OperationMapper.to_entity(op) for op in model.operations],
        )

    @classmethod
    def to_model(cls, entity: WalletEntity) -> Wallet:
        return Wallet(
            id=entity.id,
            balance=Decimal(entity.balance.amount),
            operations=[OperationMapper.to_model(op) for op in entity.operations],
        )

    @classmethod
    def create_dump(cls, entity: WalletEntity) -> dict[str, UUID | Decimal]:
        return {
            "id": entity.id,
            "balance": entity.balance.amount,
        }
