format:
	uv run ruff format backend/src/

check:
	uv run ruff check backend/src/
	uv run mypy backend/src/

pip_fix:
	.\backend\.venv\Scripts\python.exe -m ensurepip --upgrade
	.\backend\.venv\Scripts\python.exe -m pip install --upgrade pip setuptools wheel