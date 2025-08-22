from passlib.context import CryptContext

hash_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")


def validate_password(password: str, hashed_password: str) -> bool:
    return hash_ctx.verify(password, hashed_password)


def hash_password(password: str) -> str:
    return hash_ctx.hash(password)
