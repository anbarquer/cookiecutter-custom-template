FROM python:3.11-alpine3.16

ENV PYTHONUNBUFFERED=1 \
    APP_HOME="/{{cookiecutter.project_slug}}/" \
    PIP_NO_CACHE_DIR="off" \
    PIP_DISABLE_PIP_VERSION_CHECK="on" \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_NO_INTERACTION=1 \
    POETRY_HOME="/opt/poetry" \
    PATH="/opt/poetry/bin:$PATH" \
    USER="{{cookiecutter.project_slug}}"

WORKDIR $APP_HOME

RUN apk add --no-cache make && \
    addgroup -g 1000 -S $USER && \
    adduser -u 1000 -S $USER -G $USER
RUN chown -R 1000:1000 .

COPY poetry.lock pyproject.toml $APP_HOME
ADD app app

RUN pip install --upgrade pip poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root --only main

EXPOSE 5000
USER $USER

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000", "--workers", "1"]

