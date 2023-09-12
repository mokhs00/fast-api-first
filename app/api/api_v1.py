from fastapi import APIRouter

from api.v1 import sample

api_v1_router = APIRouter()
api_v1_router.include_router(sample.router, prefix="/sample")
