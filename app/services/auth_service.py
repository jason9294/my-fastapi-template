from fastapi import Depends, HTTPException

from app.core.security import create_access_token, validate_password
from app.db.sql import SessionDependency
from app.repositories.user_repo import UserRepository
from app.schemas.auth_schema import LoginResponse


class AuthService:
    def __init__(
        self, session: SessionDependency, user_repo: UserRepository = Depends()
    ):
        self.session = session
        self.user_repo = user_repo

    def login(self, username: str, password: str) -> LoginResponse:
        user = self.user_repo.get_by_username(self.session, username)
        if user is None:
            raise HTTPException(status_code=401, detail="Invalid username or password")
        if not validate_password(password, user.password):
            raise HTTPException(status_code=401, detail="Invalid username or password")
        access_token = create_access_token(user_id=user.id)
        return LoginResponse(access_token=access_token)
