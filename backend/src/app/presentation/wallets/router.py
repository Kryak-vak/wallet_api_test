from uuid import UUID

from fastapi import APIRouter, Depends

from src.app.application.wallets.services import WalletService
from src.app.presentation.wallets.deps import get_wallet_service
from src.app.presentation.wallets.schemas import (
    OperationInSchema,
    OperationOutSchema,
    WalletOutSchema,
)

router = APIRouter(prefix="/wallets", tags=["wallets"])


@router.post("/{wallet_id}/operation")
async def proccess_operation(
    wallet_id: UUID,
    operation_data: OperationInSchema,
    service: WalletService = Depends(get_wallet_service),
) -> OperationOutSchema:
    operation = await service.process_operation(wallet_id, operation_data)
    return OperationOutSchema(
        id=operation.id,
        operation_type=operation.type,
        amount=operation.amount.amount,
        wallet_id=operation.wallet_id,
    )


@router.get("/{wallet_id}/")
async def get_wallet(
    wallet_id: UUID, service: WalletService = Depends(get_wallet_service)
) -> WalletOutSchema:
    wallet = await service.get_wallet(wallet_id)
    return WalletOutSchema(id=wallet.id, balance=wallet.balance.amount)
