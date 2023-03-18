# -*- coding: utf-8 -*-

import anyio
import logging
from app.core.extensions import logger
from datetime import timedelta
from functools import wraps
from timeit import default_timer as timer

logger = logging.getLogger('cli')


def measure(func):
    """ Measure function execution time """

    @wraps(func)
    def _time_it(*args, **kwargs):
        start: float = timer()
        try:
            return func(*args, **kwargs)
        finally:
            elapsed: str = str(timedelta(seconds=timer() - start))
            logger.info('DONE. Elapsed: %s' % elapsed)

    return _time_it


def run_async(func):
    """ Wrapper around cli command that allows using async functions """

    @wraps(func)
    def wrapper(*args, **kwargs):
        async def coro_wrapper():
            return await func(*args, **kwargs)

        return anyio.run(coro_wrapper)

    return wrapper
