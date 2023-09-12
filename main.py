from fastapi import FastAPI

from api.api_v1 import api_v1_router
from db.base_class import Base
from db.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api_v1_router, prefix="/api/v1")
