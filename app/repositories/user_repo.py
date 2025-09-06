from uuid import UUID

from sqlmodel import Session, select

from app.models import UserModel

fake_db = []


class UserRepository:
    def __init__(self): ...

    def get_all(self, session: Session) -> list[UserModel]:
        return list(session.exec(select(UserModel)).all())

    def get_by_username(self, session: Session, username: str) -> UserModel | None:
        return session.exec(
            select(UserModel).where(UserModel.username == username)
        ).first()

    def get_by_id(self, session: Session, id: UUID) -> UserModel | None:
        # return session.exec(select(UserModel).where(UserModel.id == id)).first()
        return next((user for user in fake_db if user["id"] == id), None)
