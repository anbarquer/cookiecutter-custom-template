# -*- coding: utf-8 -*-

import sys
from app.core.extensions import logger
from fastapi import HTTPException
from typing import Any, Optional


class WarningException(HTTPException):
    def __init__(
        self,
        status_code: int,
        detail: Any = None,
        headers: Optional[dict[str, Any]] = None,
    ) -> None:
        logger.warning('status_code: %s:detail: %s:headers: %s' % (status_code, detail, headers))
        super().__init__(status_code=status_code, detail=detail, headers=headers)


class ErrorException(HTTPException):
    def __init__(
        self,
        status_code: int,
        detail: Any = None,
        headers: Optional[dict[str, Any]] = None,
    ) -> None:
        logger.error('status_code: %s:detail: %s:headers: %s' % (status_code, detail, headers))
        super().__init__(status_code=status_code, detail=detail, headers=headers)


class CriticalException(HTTPException):
    def __init__(
        self,
        status_code: int,
        detail: Any = None,
        headers: Optional[dict[str, Any]] = None,
    ) -> None:
        logger.critical('status_code: %s:detail: %s:headers: %s' % (status_code, detail, headers))
        super().__init__(status_code=status_code, detail=detail, headers=headers)
        sys.exit(detail)
