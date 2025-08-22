from typing import Annotated, Any

from fastapi import Depends
from sqlalchemy.orm import InstrumentedAttribute
from sqlmodel import Session, create_engine

from app.core.setting import get_settings

settings = get_settings()

engine = create_engine(settings.database_url, echo=True)


def provide_session():
    with Session(engine) as session:
        yield session


SessionDependency = Annotated[Session, Depends(provide_session)]


def attr(instance: Any) -> InstrumentedAttribute:
    return instance
