# -*- coding: utf-8 -*-

import sys
import typer

from app.core.commands.hello import app as hello_commands

app = typer.Typer()

app.add_typer(hello_commands, name='hello')

if __name__ == '__main__':
    sys.exit(app())  # pragma: no cover
