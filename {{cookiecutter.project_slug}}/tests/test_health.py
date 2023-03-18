# -*- coding: utf-8 -*-

import pytest
from fastapi import status
from httpx import AsyncClient

from app.core.config import settings
from app.main import app


@pytest.mark.asyncio
async def test_health():
    async with AsyncClient(app=app, base_url=f'http://{settings.PROJECT_NAME}') as test_client:
        response = await test_client.get(url=settings.HEALTH_CHECK_ENDPOINT)
    assert response.status_code == status.HTTP_200_OK
