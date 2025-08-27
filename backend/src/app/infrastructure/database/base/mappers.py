from abc import ABC, abstractmethod
from typing import Any, Generic

from src.app.infrastructure.database.base.common_types import EntityType, ModelType


class AbstractMapper(ABC, Generic[ModelType, EntityType]):
    model: type[ModelType]
    entity_class: type[EntityType]

    @classmethod
    @abstractmethod
    def to_entity(cls, model: ModelType) -> EntityType: ...

    @classmethod
    @abstractmethod
    def to_model(cls, entity: EntityType) -> ModelType: ...

    @classmethod
    @abstractmethod
    def create_dump(cls, entity: EntityType) -> dict[str, Any]: ...
