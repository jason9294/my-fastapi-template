# JWT/金鑰/密碼雜湊策略
from datetime import timedelta
from typing import Any
from uuid import UUID

import jwt
from passlib.context import CryptContext

from app.core.setting import get_settings
from app.utils.time_utils import datetime_utcnow

settings = get_settings()

ALGORITHM = "HS256"
SECRET_KEY = settings.secret_key


# 密碼雜湊策略
_password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def validate_password(password: str, hashed_password: str) -> bool:
    """驗證密碼是否匹配"""
    return _password_context.verify(password, hashed_password)


def hash_password(password: str) -> str:
    """雜湊密碼"""
    return _password_context.hash(password)


# JWT


def encode_jwt(payload: dict[str, Any]) -> str:
    """將 dict 轉換為 JWT 字串"""
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def decode_jwt(token: str) -> Any:
    """將 JWT 字串轉換為 dict"""
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])


def create_access_token(
    *, user_id: UUID, expires_delta: timedelta = timedelta(minutes=15)
) -> str:
    """建立 access token"""
    return encode_jwt(
        {
            "sub": str(user_id),
            "exp": datetime_utcnow() + expires_delta,
        }
    )
