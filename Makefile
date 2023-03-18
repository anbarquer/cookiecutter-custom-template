.DEFAULT_GOAL := help
PYTHON := python3

help:
	@echo "* install-requirements 	Install project dependencies"
	@echo "* create 	        Generate project using defaults"

install-requirements:
	@$(PYTHON) -m venv env
	. env/bin/activate
	@$(PYTHON) -m pip install --upgrade pip
	@$(PYTHON) -m pip install --upgrade cookiecutter

create:
	cookiecutter . --overwrite-if-exists
