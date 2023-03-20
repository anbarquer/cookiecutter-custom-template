# -*- coding: utf-8 -*-

import uvicorn
from app.api import health
from app.api.v1.router import v1_router
from app.core.config import settings
from app.core.extensions import logger
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(
    version='{{cookiecutter.version}}',
    title=settings.PROJECT_NAME,
    openapi_url=f'{settings.OPENAPI_URL}'
)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )

app.include_router(health.router, tags=['health'])
app.include_router(v1_router, prefix=settings.API_PREFIX)


@app.on_event('startup')
async def startup_event():
    logger.debug('Start up event')


@app.on_event('shutdown')
def shutdown_event():
    logger.debug('Shutdown event')


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=settings.API_PORT, reload=False)  # pragma: no cover
