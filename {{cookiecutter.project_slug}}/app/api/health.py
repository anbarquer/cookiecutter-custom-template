# -*- coding: utf-8 -*-

from app.core.config import settings
from fastapi import APIRouter, status
from fastapi.responses import Response

router = APIRouter()


@router.get(path=settings.HEALTH_CHECK_ENDPOINT)
async def health_check() -> Response:
    return Response(status_code=status.HTTP_200_OK)
