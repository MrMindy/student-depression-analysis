from fastapi import APIRouter
from app.infrastructure.api.v1.endpoints import tweet, user

router = APIRouter()
router.include_router(tweet.router, tags=["tweet"])
router.include_router(user.router, tags=["user"])