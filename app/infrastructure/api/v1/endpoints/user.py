from fastapi import APIRouter

router = APIRouter()


@router.get("/user")
def search_user():
    pass