set shell := ["powershell", "-c"]
set dotenv-load := true

dev:
    poetry run fastapi dev

lint:
    poetry run ruff check . # 檢查程式碼

lint-fix:
    poetry run ruff check . --fix  # 自動修復

typecheck:
    poetry run basedpyright # 類型檢查

format:
    poetry run ruff format . # 自動格式化

format-check:
    poetry run ruff format . --check # 檢查格式

db-recreate:
    poetry run python -m scripts.recreate_db

db-migrate message:
    poetry run alembic revision --autogenerate -m "{{message}}"

db-upgrade target="head":
    poetry run alembic upgrade "{{target}}"

db-reset: db-recreate db-upgrade

gen-router name:
    poetry run typer scripts/gen_router.py run "{{name}}"

gen-service name:
    poetry run typer scripts/gen_service.py run "{{name}}"
