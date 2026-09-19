from fastapi import APIRouter

from src.models.response_models import RootResponse

root_router = APIRouter()

@root_router.get("/",response_model=RootResponse ,tags=['root'])
async def root() -> RootResponse:
    response: RootResponse = RootResponse()
    return response