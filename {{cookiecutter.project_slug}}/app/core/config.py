# -*- coding: utf-8 -*-

import os
from ast import literal_eval
from pydantic import BaseSettings, AnyHttpUrl, validator, BaseModel
from typing import Union


class Settings(BaseSettings):
    PROJECT_NAME: str = os.environ.get('PROJECT_NAME', '{{cookiecutter.project_slug}}')
    API_PREFIX: str = os.environ.get('API_PREFIX', '/api/v1')
    API_PORT: int = int(os.environ.get('API_PORT', '5000'))
    OPENAPI_URL: str = os.environ.get('OPENAPI_URL', '/openapi.json')
    BACKEND_CORS_ORIGINS: list[Union[AnyHttpUrl | str]] = literal_eval(os.environ.get('BACKEND_CORS_ORIGINS', '["*"]'))
    HEALTH_CHECK_ENDPOINT: str = os.environ.get('HEALTH_CHECK_ENDPOINT', '/health-check/')

{% if cookiecutter.use_celery|lower == 'yes' %}
    # Celery
    REDIS_HOST: str = os.environ.get(
        'REDIS_HOST',
        'redis',
    )
    REDIS_PORT: str = os.environ.get(
        'REDIS_PORT',
        '6379'
    )
    BACKEND_DB: str = os.environ.get('BACKEND_DB', '1')
    BROKER_DB: str = os.environ.get('BROKER_DB', '1')
    BROKER_URL: str = os.environ.get(
        'BROKER_URL',
        'redis://{host}/{database}'
    )

    MAX_RETRIES: int = int(os.environ.get('MAX_RETRIES', '5'))
    TASKS: list[str] = literal_eval(os.environ.get(
        'TASKS',
        '[]'
    ))
{% endif %}
    @validator(
        'BACKEND_CORS_ORIGINS',
        pre=True
    )
    def assemble_string_from_list(
        cls,
        v: Union[str, list[str]],
    ) -> Union[list[str], str]:  # noqa
        if isinstance(v, str) and not v.startswith('['):
            return [i.strip() for i in v.split(',')]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)


settings = Settings()


class LogConfig(BaseModel):
    LOGGER_NAME: str = settings.PROJECT_NAME
    LOG_FORMAT: str = '%(levelprefix)s%(name)s:%(asctime)s:%(filename)s:%(lineno)d:%(message)s'
    LOG_LEVEL: str = os.environ.get('LOG_LEVEL', 'DEBUG')

    # Logging config
    version: int = 1
    disable_existing_loggers: bool = False
    formatters = {
        'default': {
            '()': 'uvicorn.logging.DefaultFormatter',
            'fmt': LOG_FORMAT,
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    }
    handlers = {
        'default': {
            'formatter': 'default',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stderr',
        },
        'logfile': {
            'formatter': 'default',
            'class': 'logging.FileHandler',
            'filename': f'../{LOGGER_NAME}.log',
            'mode': 'a+',
            'delay': True,
        },
    }
    loggers: dict = {
        settings.PROJECT_NAME: {
            'handlers': [
                'default',
            ],
            'level': LOG_LEVEL
        },
{% if cookiecutter.command_line_interface|lower == 'typer' %}
        'cli': {
            'handlers': [
                'default',
                'logfile'
            ],
            'level': LOG_LEVEL
        },
{% endif %}
    }


logging_config = LogConfig()
