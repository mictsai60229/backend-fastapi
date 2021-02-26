from fastapi import APIRouter, Depends
from backend.dependencies import handle_auth_key
from backend.app import urls

router = APIRouter(
    prefix="/api",
    tags = ["api"],
    dependencies=[Depends(handle_auth_key)]
)

# include projects 
router.include_router(urls.router)