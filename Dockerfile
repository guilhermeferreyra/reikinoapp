FROM python:3.10-alpine3.13
LABEL maintainer="Instituto Xavier"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt ./tmp/requirements.txt
COPY ./app /app
WORKDIR /app

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt

ENV PATH="/py/bin:$PATH"