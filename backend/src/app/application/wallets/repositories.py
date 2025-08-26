from typing import Any, Protocol
from uuid import UUID

from src.app.application.wallets.dto import (
    OperationCreateDTO,
    OperationDTO,
    WalletCreateDTO,
    WalletDTO,
    WalletUpdateDTO,
)


class IWalletRepository(Protocol):
    async def create(self, create_dto: WalletCreateDTO) -> WalletDTO: ...
    async def get(self, *, with_related: bool = True, **kwargs: Any) -> WalletDTO | None: ...
    async def filter(self, *, with_related: bool = True, **kwargs: Any) -> list[WalletDTO] | None: ...  # noqa: E501
    async def update(self, pk: int | UUID, update_dto: WalletUpdateDTO) -> WalletDTO: ...
    async def delete(self, pk: int | UUID) -> None: ...


class IOperationRepository(Protocol):
    async def create(self, create_dto: OperationCreateDTO) -> OperationDTO: ...
    async def get(self, *, with_related: bool = True, **kwargs: Any) -> OperationDTO | None: ...
    async def filter(self, *, with_related: bool = True, **kwargs: Any) -> list[OperationDTO] | None: ...  # noqa: E501
    async def delete(self, pk: int | UUID) -> None: ...
