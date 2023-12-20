# -*- coding: utf-8 -*-

import logging
from app.core.config import logging_config, settings
from logging.config import dictConfig

{% if cookiecutter.use_celery|lower == 'yes' %}
from celery import Celery
{% endif %}

dictConfig(logging_config.dict())
logger = logging.getLogger(settings.PROJECT_NAME)

{% if cookiecutter.use_celery|lower == 'yes' %}
queue: Celery = Celery(
    f'celery-{settings.PROJECT_NAME}',
    broker=f'redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}/{settings.BROKER_DB}',
    backend=f'redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}/{settings.BACKEND_DB}',
)
{% endif %}
