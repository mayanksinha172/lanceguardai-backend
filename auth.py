import os
from datetime import datetime, timedelta, timezone

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError, jwt

SECRET = os.getenv("JWT_SECRET", "change-me")
ALGORITHM = "HS256"
EXPIRE_HOURS = 24

_bearer = HTTPBearer()


def create_token(username: str) -> str:
    exp = datetime.now(timezone.utc) + timedelta(hours=EXPIRE_HOURS)
    return jwt.encode({"sub": username, "exp": exp}, SECRET, algorithm=ALGORITHM)


def _verify(token: str) -> str | None:
    try:
        data = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        return data.get("sub")
    except JWTError:
        return None


def require_admin(creds: HTTPAuthorizationCredentials = Depends(_bearer)) -> str:
    username = _verify(creds.credentials)
    if not username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )
    return username
