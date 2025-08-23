format:
	$(DOCKER_RUN) \
	uv run ruff format backend/src/

check:	
	$(DOCKER_RUN) \
	uv run ruff check src/ main.py;
	uv run mypy src/ main.py

pip_fix:
	.\backend\.venv\Scripts\python.exe -m ensurepip --upgrade
	.\backend\.venv\Scripts\python.exe -m pip install --upgrade pip setuptools wheel