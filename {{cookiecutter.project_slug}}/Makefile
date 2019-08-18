include settings.mk

.PHONY: clean clean-test clean-pyc clean-build help
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

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

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

lint: ## Check style with flake8
	${LINTER} {{ cookiecutter.project_slug }} tests

test: ## Run tests quickly with the default Python
	{%- if cookiecutter.use_pytest == 'y' %}
		${TEST} ${PACKAGE_NAME}/tests
	{%- else %}
		python setup.py test
	{%- endif %}

coverage: ## Check code coverage quickly with the default Python
	{%- if cookiecutter.use_pytest == 'y' %}
		${COVERAGE} run --source {{ cookiecutter.project_slug }} -m ${TEST}; \
	{%- else %}
		${COVERAGE} run --source {{ cookiecutter.project_slug }} setup.py test; \
	{%- endif %}
		${COVERAGE} report -m; \

coverage-report: ## Check code coverage quickly with the default Python and generates a HTML report file
	{%- if cookiecutter.use_pytest == 'y' %}
		${COVERAGE} run --source {{ cookiecutter.project_slug }} -m ${TEST}; \
	{%- else %}
		${COVERAGE} run --source {{ cookiecutter.project_slug }} setup.py test; \
	{%- endif %}
		${COVERAGE} report -m; \
		${COVERAGE} html; \
		$(BROWSER) htmlcov/index.html; \

docker-build: ## Build Docker image
	docker build -t ${PACKAGE_NAME} .

docker-run: ## Run Docker image
	docker run -it ${PACKAGE_NAME} /bin/bash

install-requirements: ## Install  dependencies
	${PYTHON} -m venv .; \
	source bin/activate; \
	${PIP} install --upgrade pip; \
	${PIP} install -r ${REQUIREMENTS}; \
