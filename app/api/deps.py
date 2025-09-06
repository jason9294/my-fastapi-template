from typing import Annotated, Optional

from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jwt.exceptions import InvalidTokenError

from app.core.security import decode_jwt
from app.schemas.common.jwt import JWTPayload

http_bearer = HTTPBearer(auto_error=False)


def _provide_token(
    token: Optional[HTTPAuthorizationCredentials] = Depends(http_bearer),
) -> str:
    if token is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    return token.credentials


def _provide_jwt_payload(
    token: str = Depends(_provide_token),
) -> JWTPayload:
    try:
        data = decode_jwt(token)
        print(data)
        payload = JWTPayload.model_validate(data)
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    return payload


JWTDependency = Annotated[JWTPayload, Depends(_provide_jwt_payload)]
