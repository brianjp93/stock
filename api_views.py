from fastapi import APIRouter
from account import views
from stock import views as stock_views

router = APIRouter(
    prefix='/api',
)

router.include_router(views.router)
router.include_router(stock_views.router)
