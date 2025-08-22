# 使用 Python 3.12 官方映像
FROM python:3.12-slim

# 設定工作目錄
WORKDIR /app

# 安裝系統依賴 (用於 pyodbc 和 MSSQL 連接)
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    unixodbc \
    unixodbc-dev \
    && curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg \
    && curl https://packages.microsoft.com/config/debian/12/prod.list | tee /etc/apt/sources.list.d/mssql-release.list \
    && echo "deb [arch=amd64,arm64,armhf signed-by=/usr/share/keyrings/microsoft-prod.gpg] https://packages.microsoft.com/debian/12/prod bookworm main" > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql18 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 安裝 Poetry
RUN pip install poetry

# 設定 Poetry 不要建立虛擬環境（因為已經在容器中）
ENV POETRY_VENV_IN_PROJECT=false
ENV POETRY_NO_INTERACTION=1
ENV POETRY_CACHE_DIR=/tmp/poetry_cache

# 複製 Poetry 配置文件
COPY pyproject.toml poetry.lock* ./

# 安裝依賴（直接安裝到系統 Python）
RUN poetry config virtualenvs.create false \
    && poetry install --only=main \
    && rm -rf $POETRY_CACHE_DIR

# 複製應用程式代碼
COPY . .

# 暴露端口
EXPOSE 8000

# 設定環境變數
ENV PYTHONPATH=/app

# 啟動命令
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
