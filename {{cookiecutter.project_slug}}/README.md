{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
# {{ cookiecutter.project_name }}


{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
{% endif %}

## Features

* TODO

## Credits

This project was highly inspirated by `audreyr/cookiecutter-pypackage` project template.

* [Cookiecutter](https://github.com/audreyr/cookiecutter)
* [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)

