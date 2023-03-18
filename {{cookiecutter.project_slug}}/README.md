# {{ cookiecutter.project_slug }}

## Prerequisites

### Python

You can use [pyenv](https://github.com/pyenv/pyenv) to cli multiple python interpreters. This project uses Python __
v3.11.X__

[Pyenv command examples](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md)

### Poetry

Before installing any dependencies is recommended to create a Python virtual environment first.

#### Install

``` python3 -m pip install -U poetry ```

[More info](https://python-poetry.org/docs/#installation)

#### Usage

* Activate the virualenv run: ``poetry shell``
* Deactivate virtualenv: ``exit``
* Install all dependencies: ``poetry install``
* Install only production dependencies: ``poetry install --only main``

### Docker

#### Install

Install Docker using this [guide](https://docs.docker.com/engine/install/).

#### Post installation steps (optional)

Is recommended to add Docker to sudoers group in order to be able to execute docker commands without
sudo [more info](https://docs.docker.com/engine/install/linux-postinstall/).


## CLI commands

### Add a new command

- Create a new file with the command name using underscores in ``app/core/commands`` folder.
- Write a ``Typer``command using ``@app.command()``, ``@measure`` and ``@run_async`` (this last one is only needed if your command uses async calls)
- Import the command group in ``cli.py``. e.g: ``from app.core.commands.users import app as user_commands``
- Add the new command in ``cli.py`` in a new line with ``app.add_typer(user_commands, name='users')
``

### Commands

The commands will log all the messages in the standard output (console) and in a file called ``command_logs.log`` that will be stored in the project root.

## Credits

This package was highly inspired in **Cookiecutter** project template.

* [Cookiecutter](https://github.com/audreyr/cookiecutter)
* **Antonio Diego Barquero Cuadrado** - [Send mail](mailto:anbarquer@gmail.com)

## License

This project is licensed under the MIT license - see the [LICENSE](LICENSE) file for details.

## Versioning

We use [SemVer](http://semver.org/) for versioning.

## Acknowledgments

* Open source community
* [License chooser](https://choosealicense.com/)
* [Open Sourcing a Python Project the Right Way](https://jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/)
* [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)

