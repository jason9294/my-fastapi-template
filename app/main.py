import os
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse
from fastapi.routing import APIRoute

from app.api import api_router
from app.core.problem import PROBLEM_CONTENT_TYPE, ProblemException
from app.core.setting import get_settings


def make_dirs():
    mk_dirs = []
    for mk_dir in mk_dirs:
        if not os.path.exists(mk_dir):
            os.makedirs(mk_dir)


@asynccontextmanager
async def lifespan(app: FastAPI):
    make_dirs()
    yield


def custom_generate_unique_id(route: APIRoute):
    """
    自定義生成唯一 ID 的函數
    將 endpoint 的第一個 tag + 名稱組成
    """
    return f"{route.tags[0]}-{route.name}"


def create_app():
    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        lifespan=lifespan,
        version="0.1.0",
        generate_unique_id_function=custom_generate_unique_id,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:9000",  # 本機端（指定端口，例如前端應用程式）
        ],
        allow_credentials=True,  # 若需要允許 cookies，設為 True
        allow_methods=["*"],  # 設定允許的方法，["*"] 代表所有方法
        allow_headers=["*"],  # 設定允許的 headers，["*"] 代表所有 headers
        expose_headers=["Content-Type", "Set-Cookie"],
    )
    app.include_router(api_router)

    @app.exception_handler(ProblemException)
    async def handle_problem_exc(request: Request, exc: ProblemException):
        problem_details = exc.problem
        return ORJSONResponse(
            content=problem_details.model_dump(),
            status_code=problem_details.status,
            media_type=PROBLEM_CONTENT_TYPE,
        )

    return app


app = create_app()
