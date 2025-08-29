from uuid import UUID, uuid4

from sqlalchemy.ext.asyncio import AsyncSession

from src.app.application.wallets.errors import WalletNotFoundError
from src.app.application.wallets.repositories import IOperationRepository, IWalletRepository
from src.app.domain.entities import Operation, Wallet
from src.app.domain.value_objects import Money
from src.app.presentation.wallets.schemas import OperationInSchema


class WalletService:
    def __init__(
        self,
        session: AsyncSession,
        wallet_repo: IWalletRepository,
        operation_repo: IOperationRepository,
    ):
        self.session = session
        self.wallet_repo = wallet_repo
        self.operation_repo = operation_repo

    async def get_wallet(self, wallet_id: UUID) -> Wallet:
        wallet = await self.wallet_repo.get(id=wallet_id)
        if wallet is None:
            raise WalletNotFoundError(wallet_id)

        return wallet

    async def process_operation(
        self, wallet_id: UUID, operation_data: OperationInSchema
    ) -> Operation:
        async with self.session.begin():
            wallet = await self.wallet_repo.get(with_for_update=True, id=wallet_id)
            if wallet is None:
                raise WalletNotFoundError(wallet_id)

            operation = Operation(
                id=uuid4(),
                type=operation_data.operation_type,
                amount=Money(operation_data.amount),
                wallet_id=wallet.id,
            )

            wallet.apply_operation(operation)

            await self.wallet_repo.update(pk=wallet_id, update_entity=wallet)

            return operation
