from typing import Protocol
from uuid import UUID

from src.app.application.wallets.dto import WalletCreateDTO, WalletDTO, WalletUpdateDTO


class IWalletRepository(Protocol):
    async def create(self, create_dto: WalletCreateDTO) -> WalletDTO: ...
    async def update(self, pk: int | UUID, update_dto: WalletUpdateDTO) -> WalletDTO: ...