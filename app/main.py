#!/usr/bin/env python3

from fastapi import FastAPI
from app.settings import settings
from app.infrastructure.api.v1.router import router

app = FastAPI(
    title       = settings.PROJECT_NAME,
    openapi_url = f"{settings.BASE_URI}/openapi.json"
)

app.include_router(router, prefix=settings.BASE_URI)
