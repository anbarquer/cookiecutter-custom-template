# -*- coding: utf-8 -*-

import typer
from app.core.commands import run_async, logger, measure

app = typer.Typer()


@app.command()
@measure
@run_async
async def say_hello() -> None:
    logger.info('Hello')
