from datetime import datetime

from sqlmodel import Field, SQLModel

from app.utils import datetime_utcnow


class TimestampMixin(SQLModel):
    created_at: datetime = Field(
        default_factory=datetime_utcnow,
    )

    updated_at: datetime = Field(
        default_factory=datetime_utcnow,
        sa_column_kwargs={"onupdate": datetime_utcnow},
    )
