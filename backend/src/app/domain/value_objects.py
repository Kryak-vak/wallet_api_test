from dataclasses import dataclass
from decimal import Decimal
from enum import Enum


@dataclass(frozen=True)
class Money:
    amount: Decimal

    def __post_init__(self):
        if self.amount < 0:
            raise ValueError("Amount can't be negative")


class OperationType(Enum):
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
