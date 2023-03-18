# -*- coding: utf-8 -*-

import logging
from app.core.config import logging_config, settings
from logging.config import dictConfig

dictConfig(logging_config.dict())
logger = logging.getLogger(settings.PROJECT_NAME)
