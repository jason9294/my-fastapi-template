from sqlmodel import Session, select

from app.models import UserModel


class UserRepository:
    def __init__(self):
        ...

    def get_all(self, session: Session) -> list[UserModel]:
        return list(session.exec(select(UserModel)).all())
