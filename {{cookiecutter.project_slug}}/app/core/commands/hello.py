# -*- coding: utf-8 -*-


from app.core.commands import run_async, logger, measure
from app.core.config import settings

app = typer.Typer()


@app.command()
@measure
@run_async
async def say_hello() -> None:
    logger.info('Hello')
