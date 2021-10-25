from fastapi import APIRouter, Depends
from sqlmodel import Session
from db import get_session
from account.models import UserCreate, UserRead, User


router = APIRouter(
    prefix='/account',
    tags=['account'],
)

@router.get('/me')
async def me():
    return {'message': 'hello brian'}

@router.post('/', response_model=UserRead)
async def create_user(*, session: Session = Depends(get_session), user: UserCreate):
    db_user: User = User.from_orm(user)
    db_user.set_password(db_user.password)
    session.add(db_user)
    session.commit()
    return db_user
