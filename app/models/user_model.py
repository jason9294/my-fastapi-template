from typing import TYPE_CHECKING
from uuid import UUID

from sqlmodel import Field, SQLModel
from uuid_extensions import uuid7

from .mixin.timestamp import TimestampMixin

if TYPE_CHECKING:
    ...


class UserModel(TimestampMixin, SQLModel, table=True):
    __tablename__ = "users"  # type: ignore

    # Primary Key
    id: UUID = Field(default_factory=uuid7, primary_key=True)

    username: str = Field(max_length=255, index=True, unique=True)  # 使用者帳號，需唯一
    password: str  # 密碼

    __table_args__ = ()
