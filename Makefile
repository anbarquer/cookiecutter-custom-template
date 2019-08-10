BAKE_OPTIONS=--no-input

help:
	@echo "create 	generate project using defaults"

create:
	cookiecutter . --overwrite-if-exists
