from fastapi import APIRouter, Depends
from backend.dependencies import get_auth_key
from backend.app import urls

router = APIRouter(
    prefix="/api",
    tags = ["api"],
    dependencies=[Depends(get_auth_key)]
)

# include projects 
router.include_router(urls.router)