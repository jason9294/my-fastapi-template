# my-fastapi-template

## 專案使用工具

- 專案管理工具
  - just
  - poetry
- 框架
  - FastAPI
  - sqlmodel

## 專案結構

```text
my-fastapi-template/
├─ pyproject.toml                     # 專案設定 (Poetry)
├─ README.md                          # 專案說明
├─ .env.example                       # 環境變數樣板
├─ .gitignore                         # 忽略檔案
├─ .pre-commit-config.yaml            # 格式/靜態檢查(ruff/black/isort/mypy)
├─ scripts/
│  ├─ dev.sh                          # 本地啟動/重載
│  ├─ lint.sh                         # Lint/型別檢查
│  ├─ test.sh                         # 測試
│  └─ seed_data.sh                    # 開發用資料灌入
├─ alembic/                           # 資料庫遷移
│  ├─ versions/                       # 版本腳本
│  ├─ script.py.mako                  # 遷移腳本模板
│  └─ env.py
├─ tests/
│  ├─ unit/                           # 單元測試(services/repositories/utils)
│  ├─ integration/                    # 整合測試(含DB/外部服務)
│  ├─ e2e/                            # 端對端(BDD/契約測試)
│  └─ fixtures/                       # 測試用資料/假件
└─ app/
   ├─ main.py                         # 進入點(組裝應用、掛載路由/中介層)
   ├─ core/                           # 核心橫切關注點
   │  ├─ setting.py                   # 設定載入(Pydantic Settings)
   │  ├─ logging.py                   # 日誌初始化
   │  ├─ security.py                  # JWT/金鑰/密碼雜湊策略
   │  └─ middleware/                  # 中介層
   │     ├─ request_id.py             # 追蹤ID
   │     ├─ timing.py                 # 請求耗時
   │     ├─ cors.py                   # CORS
   │     └─ exception_mapper.py       # 統一例外轉HTTP回應
   ├─ api/
   │  ├─ dependencies/                # 路由依賴項(權限/分頁/注入Service)
   │  ├─ routers/                     # 路由(按bounded context分群)
   │  └─ routers_registry.py          # 路由匯總/統一掛載位
   ├─ schemas/                        # API I/O模型(Pydantic)
   │  ├─ users.py
   │  ├─ auth.py
   │  └─ items.py
   ├─ repositories/                   # 資料存取抽象 + 實作
   ├─ services/                       # 應用服務(Use Cases)
   │  ├─ users_service.py
   │  ├─ auth_service.py
   │  └─ items_service.py
   ├─ db/
   │  ├─ session.py                   # Session/Engine管理
   │  ├─ base.py                      # Base metadata/匯入ORM models
   │  └─ seed.py                      # 初始資料/種子
   ├─ cache/
   │  ├─ redis.py                     # Redis連線/快取helpers
   │  └─ keys.py                      # 快取鍵規範
   ├─ storage/
   │  ├─ s3.py                        # S3/MinIO抽象
   │  └─ local.py
   ├─ messaging/
   │  ├─ broker.py                    # 事件匯流排(Kafka/RabbitMQ/Redis Streams)
   │  ├─ publishers/                  # 發佈端
   │  └─ consumers/                   # 消費端(如webhook/事件驅動)
   ├─ tasks/                          # 背景任務
   │  ├─ scheduler.py                 # APScheduler/Crontab
   │  ├─ celery_app.py                # Celery設定(若採用)
   │  └─ jobs/                        # 具體job定義
   ├─ errors/
   │  ├─ base.py                      # 自訂例外基底
   │  └─ mappings.py                  # 例外→HTTP狀態碼/錯誤碼
   ├─ utils/
   │  ├─ hashing.py                   # 雜湊/編碼工具
   │  ├─ time.py
   │  ├─ email_mask.py
   │  └─ validators.py
   ├─ auth/                           # 認證/授權策略模組化
   │  ├─ jwt_provider.py
   │  ├─ oauth_providers/             # Google/GitHub/OIDC
   │  └─ permissions.py               # RBAC
```
