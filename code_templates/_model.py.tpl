from typing import TYPE_CHECKING, Optional
from uuid import UUID

from sqlmodel import Field, Relationship, SQLModel
from uuid_extensions import uuid7

if TYPE_CHECKING:
    ...


class Model(SQLModel, table=True):
    __tablename__ = ""  # type: ignore

    id: UUID = Field(default_factory=uuid7, primary_key=True)  # 主鍵 ID
