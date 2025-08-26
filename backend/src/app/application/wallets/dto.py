from uuid import UUID

from pydantic import BaseModel

from src.app.application.wallets.enums import OperationType


class WalletDTO(BaseModel):
    id: UUID
    balance: float


class WalletCreateDTO(BaseModel):
    pass


class WalletUpdateDTO(BaseModel):
    balance: float




class OperationDTO(BaseModel):
    id: UUID
    type: OperationType
    amount: float
    
    wallet_id: UUID


class OperationCreateDTO(BaseModel):
    type: OperationType
    amount: float

    wallet_id: UUID


class OperationUpdateDTO(BaseModel):
    pass

