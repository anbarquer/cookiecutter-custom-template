#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.dirname(os.path.realpath(os.path.curdir))


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':

    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        cli_file = os.path.join('{{ cookiecutter.project_slug }}', 'manage.py')
        remove_file(cli_file)

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        license_file = os.path.join('{{ cookiecutter.project_slug }}', 'LICENSE')
        remove_file(license_file)

    if 'no' in '{{ cookiecutter.use_celery|lower }}':
        path = os.path.join(PROJECT_DIRECTORY, '{{ cookiecutter.project_slug }}', 'app', 'task')
        shutil.rmtree(os.path.join(PROJECT_DIRECTORY, '{{ cookiecutter.project_slug }}', 'app', 'task'))
