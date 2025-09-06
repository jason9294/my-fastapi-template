from fastapi import APIRouter, Depends

from app.api.deps import JWTDependency
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["user"])


@router.get(
    path="",
    summary="...",
)
async def get_all(user_service: UserService = Depends()):
    return user_service.get_all()


@router.get(
    path="/me",
    summary="...",
)
async def get_me(
    jwt_payload: JWTDependency,
    user_service: UserService = Depends(),
):
    return jwt_payload
