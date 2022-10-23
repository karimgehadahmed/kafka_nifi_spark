from fastapi import APIRouter

from app.api.api_v1.endpoints import analysis_api

api_router = APIRouter()
api_router.include_router(analysis_api.router, prefix="/analysis", tags=["analysis"])
