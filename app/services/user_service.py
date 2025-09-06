from fastapi import Depends

from app.db.sql import SessionDependency
from app.repositories.user_repo import UserRepository
from app.schemas.user_schema import UserSchema


class UserService:
    def __init__(
        self,
        session: SessionDependency,
        user_repo: UserRepository = Depends(),
    ):
        self.session = session
        self.user_repo = user_repo

    def get_all(self) -> list[UserSchema]:
        users = self.user_repo.get_all(self.session)
        return [UserSchema(id=user.id, username=user.username) for user in users]
