from fastapi import Depends

from src.app.application.wallets.repositories import IOperationRepository, IWalletRepository
from src.app.application.wallets.services import WalletService
from src.app.infrastructure.database.wallets.repositories import (
    SQLAlchemyOperationRepository,
    SQLAlchemyWalletRepository,
)
from src.app.presentation.deps import SessionDep


def get_wallet_repo(session: SessionDep) -> IWalletRepository:
    return SQLAlchemyWalletRepository(session=session)


def get_operation_repo(session: SessionDep) -> IOperationRepository:
    return SQLAlchemyOperationRepository(session=session)


def get_wallet_service(
    session: SessionDep,
    wallet_repo: IWalletRepository = Depends(get_wallet_repo),
    operation_repo: IOperationRepository = Depends(get_operation_repo),
) -> WalletService:
    return WalletService(session=session, wallet_repo=wallet_repo, operation_repo=operation_repo)
