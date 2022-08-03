FROM python:3.9.13 as base
LABEL maintainer="Instituto Xavier"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt ./tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
EXPOSE 8000

ARG DEV=false
RUN \
    # apk update &&\ 
    # apk add --virtual build-deps gcc python3-dev musl-dev &&\
    # apk add --no-cache mariadb-dev &&\
    python -m venv /py &&\
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt; \
    fi && \
    rm -rf /tmp && \
    adduser --disabled-password --no-create-home app-user

ENV PATH="/py/bin:$PATH"

USER app-user

FROM base as prod
WORKDIR /app
COPY ./app /app


FROM base as dev
WORKDIR /app
COPY ./sql_app /app
