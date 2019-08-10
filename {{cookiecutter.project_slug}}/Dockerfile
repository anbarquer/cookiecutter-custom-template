FROM python:latest-alpine

ARG BASE_DIR=./{ cookiecutter.project_slug }

COPY . $BASE_DIR
WORKDIR $BASE_DIR
RUN pip3 install -r requirements.txt
