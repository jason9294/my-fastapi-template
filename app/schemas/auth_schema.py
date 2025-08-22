from pydantic import BaseModel


class TokenSchema(BaseModel):
    refresh_token: str
