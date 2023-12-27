# {{ cookiecutter.project_slug }}

## Contents

* [Prerequisites](#prerequisites)
* [Local development](#local-development)
* [CLI commands](#cli-commands)
* [Credits](#credits)
* [Swagger UI](#swagger-ui)
* [Code style](#code-style)
* [License](#license)
* [Versioning](#versioning)
* [Acknowledgments](#acknowledgments)

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

### Kubectl

Learn how to install and configure ``kubectl`` with [this guide](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)

## Local development

### Makefile

There is a ``Makefile`` with the following recipes that may help in your local development process:

```plaintext
* clean                          Remove all build, test, coverage and Python artifacts
* clean-build                    Remove build artifacts
* clean-pyc                      Remove Python file artifacts
* clean-test                     Remove test and coverage artifacts
* lint                           Analyze code with flake8
* coverage                       Code coverage
* test                           Run tests with pytest
* requirements                   Install requirements (main only)
* requirements-dev               Install all requirements
* docker-build                   Build Docker image for the API service
* docker-run                     Run Docker image for the API service
```

{% if cookiecutter.command_line_interface|lower == 'typer' %}
## CLI commands

### Add a new command

- Create a new file with the command name using underscores in ``app/core/commands`` folder.
- Write a ``Typer``command using ``@app.command()``, ``@measure`` and ``@run_async`` (this last one is only needed if your command uses async calls)
- Import the command group in ``manage.py``. e.g: ``from app.core.commands.users import app as user_commands``
- Add the new command in ``manage.py`` on a new line with ``app.add_typer(user_commands, name='users')``
{% endif %}

### Commands

The commands will log all the messages in the standard output (console) and in a file called ``command_logs.log`` that will be stored in the project root.

## Credits

This package was highly inspired in **Cookiecutter** project template.

* [Cookiecutter](https://github.com/audreyr/cookiecutter)
* **{{cookiecutter.full_name}}** - [Send mail](mailto:{{cookiecutter.email}})

## Swagger UI

If you have successfully built and run the project, you can check the API docs with [SwaggerUI](https://swagger.io/tools/swagger-ui/):

- ``/docs``
- ``/redoc``

## Code style

* This project follows the PEP8 coding style - [PEP8](https://www.python.org/dev/peps/pep-0008/)
* For the sake of convenience, there is an exception with the line length, extended to 120 characters. If this does not align with your code style standards, edit the ``setup.cfg`` file in the main project folder and remove the ``max-line-length`` line.

## License

This project is licensed under the MIT license - see the [LICENSE](LICENSE) file for details.

## Versioning

We use [SemVer](http://semver.org/) for versioning. The project is configured with [bump2version](https://pypi.org/project/bump2version/). When you bump a version for this project the tool changes the versioning for the ``pyproject.toml`` files and the Kubernetes for the prod environment. Also it's configured to push a new commit and tag with the version. Check the config in ``.bumpversion.cfg`` file.

## Acknowledgments

* Open source community
* [License chooser](https://choosealicense.com/)
* [Open Sourcing a Python Project the Right Way](https://jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/)
* [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)

