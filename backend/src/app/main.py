from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.app.application.wallets.errors import WalletNotFoundError
from src.app.presentation.router import router
from src.config.app import app_config

app = FastAPI(
    title=app_config.project_name,
    openapi_url=f"{app_config.api_v1_str}/openapi.json",
)

app.include_router(router, prefix=app_config.api_v1_str)


@app.exception_handler(WalletNotFoundError)
async def wallet_not_found_handler(request, exc: WalletNotFoundError):
    return JSONResponse(
        status_code=404,
        content={"detail": f"{exc.args[0]}"},
    )

