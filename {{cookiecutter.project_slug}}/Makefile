.PHONY: clean clean-test clean-pyc clean-build help lint coverage requirements requirements-dev docker-build docker-run
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z0-9_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("* %-30s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"
PYTHON=python
DOCKER_COMPOSE := docker compose
DOCKER := docker
SHELL := /bin/bash

help:
	@$(PYTHON) -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## Remove all build, test, coverage and Python artifacts

clean-build: ## Remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## Remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## Remove test and coverage artifacts
	rm -f .coverage; \
	rm -fr htmlcov/; \
	rm -fr .pytest_cache; \

lint:  ## Analyze code with flake8
	@$(PYTHON) -m poetry run flake8 app

coverage:  ## Code coverage
	@$(PYTHON) -m poetry run pytest --cov=app tests/

test:  ## Run tests with pytest
	@$(PYTHON) -m poetry run coverage run --source app -m pytest tests

requirements:  ## Install requirements (main only)
	@$(PYTHON) -m poetry install --no-root --only main

requirements-dev:  ## Install requirements
	@$(PYTHON) -m poetry install --no-root

docker-build: ## Build Docker image
	@(DOCKER) build -t {{cookiecutter.project_slug}} .

docker-run: ## Run Docker image
	@(DOCKER) run -t {{cookiecutter.project_slug}} -p 5000:5000


