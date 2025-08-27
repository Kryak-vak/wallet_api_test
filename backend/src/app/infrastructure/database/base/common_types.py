from typing import TypeVar

from src.app.domain.entities import Entity
from src.app.infrastructure.database.base.models import Base

ModelType = TypeVar("ModelType", bound=Base)
EntityType = TypeVar("EntityType", bound=Entity)
