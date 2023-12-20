FROM python:3.11-slim as builder

ENV PYTHONUNBUFFERED=1 \
    APP_HOME={{cookiecutter.project_slug}} \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_NO_INTERACTION=1 \
    POETRY_HOME="/opt/poetry" \
    PATH="/opt/poetry/bin:$PATH"

RUN apt-get update && \
    apt-get install -y curl git openssl build-essential && \
    mkdir $APP_HOME && useradd -m -s $(which bash) python && \
    chown -R python $APP_HOME

WORKDIR $APP_HOME
COPY poetry.lock pyproject.toml $APP_HOME

RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install poetry && \
    poetry export --without-hashes --only main --format=requirements.txt > requirements.txt

FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    APP_HOME={{cookiecutter.project_slug}} \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

WORKDIR $APP_HOME

COPY --from=builder {{cookiecutter.project_slug}}/requirements.txt $APP_HOME

RUN apt-get update && \
    apt-get install -y build-essential && \
    useradd -m -s $(which bash) python && \
    chown -R python $APP_HOME

USER python

RUN python3 -m pip install --no-cache-dir -r requirements.txt

ADD . $APP_HOME

EXPOSE 5000

CMD ["python3", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000", "--workers", "1"]
