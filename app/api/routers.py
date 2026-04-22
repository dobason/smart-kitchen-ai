from fastapi import APIRouter
from app.api.v1.api import api as v1_api

api = APIRouter()

api.include_router(v1_api, prefix="/v1")