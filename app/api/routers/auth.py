from fastapi import APIRouter, Depends

from app.schemas.auth_schema import LoginRequest, LoginResponse, RegisterRequest
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    path="/login",
    summary="login",
)
async def login(
    request: LoginRequest, service: AuthService = Depends()
) -> LoginResponse:
    return service.login(request.username, request.password)


@router.post(
    path="/refresh",
    summary="refresh",
)
async def refresh():
    return {"message": "Token refreshed successfully"}


@router.post(
    path="/logout",
    summary="logout",
)
async def logout():
    return {"message": "User logged out successfully"}


@router.post(
    path="/register",
    summary="register",
)
async def register(request: RegisterRequest):
    return {"message": "User registered successfully"}
