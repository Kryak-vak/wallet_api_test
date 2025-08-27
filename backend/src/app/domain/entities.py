from dataclasses import dataclass, field
from typing import Protocol
from uuid import UUID

from src.app.domain.value_objects import Money, OperationType


class Entity(Protocol):
    id: UUID


@dataclass
class Wallet:
    id: UUID
    balance: Money
    operations: list["Operation"] = field(default_factory=list)

    def apply_operation(self, operation: "Operation") -> None:
        if operation.type == OperationType.DEPOSIT:
            self.deposit(operation.amount)
        else:
            self.withdraw(operation.amount)

    def deposit(self, money: Money) -> None:
        self.balance = Money(self.balance.amount + money.amount)

    def withdraw(self, money: Money) -> None:
        self.balance = Money(self.balance.amount - money.amount)


@dataclass
class Operation:
    id: UUID
    type: OperationType
    amount: Money

    wallet_id: UUID
