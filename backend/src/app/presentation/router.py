from fastapi import APIRouter

from src.app.presentation.wallets.router import router as wallets_router

router = APIRouter()
router.include_router(wallets_router)
