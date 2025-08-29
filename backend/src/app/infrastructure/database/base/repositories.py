from abc import ABC
from typing import Any, Generic
from uuid import UUID

from sqlalchemy import Select, delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.infrastructure.database.base.common_types import EntityType, ModelType
from src.app.infrastructure.database.base.mappers import AbstractMapper


class AbstractSQLAlchemyRepository(ABC, Generic[ModelType, EntityType]):
    model: type[ModelType]
    entity_class: type[EntityType]
    mapper: type[AbstractMapper[ModelType, EntityType]]

    def __init__(self, session: AsyncSession):
        self._session = session

    async def refresh(self, entity: EntityType) -> EntityType:
        model_instance = await self._session.get(self.model, entity.id)
        assert model_instance is not None
        await self._session.refresh(model_instance)

        return self.mapper.to_entity(model_instance)

    async def create(self, create_entity: EntityType) -> EntityType:
        create_data = self.mapper.create_dump(create_entity)
        stmt = insert(self.model).values(**create_data).returning(self.model)
        result = await self._session.scalars(stmt)
        return self.mapper.to_entity(result.one())

    async def update(self, pk: int | UUID, update_entity: EntityType) -> EntityType:
        update_data = self.mapper.create_dump(update_entity)

        stmt = (
            update(self.model)
            .where(self.model.id == pk)
            .values(**update_data)
            .returning(self.model)
        )
        result = await self._session.scalars(stmt)
        return self.mapper.to_entity(result.one())

    async def get(
            self, *,
            with_related: bool = True,
            with_for_update: bool = False,
            **kwargs: Any
        ) -> EntityType | None:
        stmt = select(self.model).filter_by(**kwargs)

        if with_related:
            stmt = self._apply_loader_options(stmt)
        
        if with_for_update:
            stmt = stmt.with_for_update()

        result = await self._session.scalars(stmt)
        model_instance = result.one_or_none()

        return self.mapper.to_entity(model_instance) if model_instance else None

    async def filter(
            self, *,
            with_related: bool = True,
            with_for_update: bool = False,
            **kwargs: Any
            ) -> list[EntityType]:
        stmt = select(self.model).filter_by(**kwargs)

        if with_related:
            stmt = self._apply_loader_options(stmt)
        
        if with_for_update:
            stmt = stmt.with_for_update()

        result = await self._session.scalars(stmt)
        return [self.mapper.to_entity(instance) for instance in result.all()]

    async def delete(self, pk: int | UUID) -> None:
        stmt = delete(self.model).where(self.model.id == pk)
        await self._session.execute(stmt)

    def _apply_loader_options(self, stmt: Select) -> Select:
        return stmt
