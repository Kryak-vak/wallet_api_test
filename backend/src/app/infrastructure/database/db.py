from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src.config.database import database_config

engine = create_async_engine(str(database_config.SQLALCHEMY_DATABASE_URI))

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    autoflush=False,
)
