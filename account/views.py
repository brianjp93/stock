from fastapi import APIRouter


router = APIRouter(
    prefix='/account',
    tags=['account'],
)

@router.get('/me')
async def me():
    return {'message': 'hello brian'}
