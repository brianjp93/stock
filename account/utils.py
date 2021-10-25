from fastapi import HTTPException, status, Depends
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import MissingTokenError
from sqlmodel import Session, select
from db import engine
from account.models import User


def get_user(email: str) -> User | None:
    with Session(engine) as session:
        if user := session.exec(select(User).where(User.email==email)).first():
            return user


def authenticate_user(email: str, password: str) -> User | None:
    """Return User if email/password match."""
    if user := get_user(email):
        if user.check_password(password):
            return user


def refresh_token(Authorize: AuthJWT):
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    if isinstance(email, str):
        access_token = Authorize.create_access_token(email)
        Authorize.set_access_cookies(access_token)


def get_current_user(Authorize: AuthJWT = Depends()):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    try:
        Authorize.jwt_required()
    except:
        try:
            refresh_token(Authorize)
        except MissingTokenError:
            raise credentials_exception
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    user = None
    if isinstance(email, str):
        user = get_user(email=email)
    if user:
        return user
    raise credentials_exception


def get_current_active_user(current_user: User = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
