from datetime import timedelta
from config.settings import get_settings

from fastapi import APIRouter, Depends, status, HTTPException
from fastapi_jwt_auth import AuthJWT
from account.models import UserCreate, UserRead, User, UserLogin
from account.utils import get_current_active_user, authenticate_user

settings = get_settings()


ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter(
    prefix="/account",
    tags=["account"],
)


@AuthJWT.load_config
def get_config():
    return [
        ('authjwt_secret_key', settings.SECRET_KEY),
        ('authjwt_token_location', {"cookies"}),
        ('authjwt_cookie_csrf_protect', False),
    ]


@router.get("/me/", response_model=UserRead)
async def me(current_user: User = Depends(get_current_active_user)):
    return current_user


@router.post("/", response_model=UserRead)
async def create_user(*, user: UserCreate):
    db_user: User = User(**user.dict())
    db_user.set_password(db_user.password)
    await db_user.save()
    return db_user


@router.post("/login/")
async def login(
    user: UserLogin,
    Authorize: AuthJWT = Depends(),
):
    db_user = await authenticate_user(user.email, user.password)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = access_token = Authorize.create_access_token(
        subject=db_user.email,
        expires_time=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    )
    refresh_token = Authorize.create_refresh_token(subject=db_user.email)

    Authorize.set_access_cookies(access_token)
    Authorize.set_refresh_cookies(refresh_token)
    return {
        'msg': 'Tokens set successfully.',
    }

@router.delete('/logout/')
def logout(Authorize: AuthJWT = Depends()):
    Authorize.unset_jwt_cookies()
    return {"msg":"Successful logout."}
