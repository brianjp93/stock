from fastapi import APIRouter
from account import views

router = APIRouter(
    prefix='/api',
)

router.include_router(views.router)
