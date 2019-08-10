include settings.mk

.DEFAULT_GOAL=help

help:
	@echo "* install-requirements 	Install project dependencies"
	@echo "* create 	        Generate project using defaults"

install-requirements:
	${PYTHON} -m venv .; \
	source bin/activate; \
	${PIP} install --upgrade pip; \
	${PIP} install -r ${REQUIREMENTS}; \

create:
	cookiecutter . --overwrite-if-exists
