SERVICE_NAME = web
DOCKER_RUN = docker compose run $(SERVICE_NAME)
DOCKER_EXEC = docker compose exec -it


build:
	docker compose build

clean:
	docker image prune -f

up: build
	docker compose up --watch

down:
	docker compose down --remove-orphans
	$(MAKE) clean

reload: down up

restart: 
	docker compose restart $(SERVICE_NAME)

logs:
	docker compose logs $(SERVICE_NAME)


test: build
	$(DOCKER_RUN) uv run pytest


migrations: build
	$(DOCKER_RUN) uv run alembic revision --autogenerate
	
migrate:
	$(DOCKER_RUN) uv run alembic upgrade head

auto_migrate: migrations migrate


shell:
	$(DOCKER_EXEC) web bash

dbshell:
	$(DOCKER_EXEC) db psql -U postgres


format:
	uv run ruff format backend/src/

check:
	uv run ruff check backend/src/
	uv run mypy backend/src/

pip_fix:
	.\backend\.venv\Scripts\python.exe -m ensurepip --upgrade
	.\backend\.venv\Scripts\python.exe -m pip install --upgrade pip setuptools wheel