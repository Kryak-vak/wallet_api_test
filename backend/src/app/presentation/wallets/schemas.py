from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel

from src.app.domain.value_objects import OperationType


class WalletOutSchema(BaseModel):
    id: UUID
    balance: Decimal


class OperationInSchema(BaseModel):
    operation_type: OperationType
    amount: Decimal


class OperationOutSchema(BaseModel):
    id: UUID
    operation_type: OperationType
    amount: Decimal
    wallet_id: UUID
