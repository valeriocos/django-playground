FROM python:3.8-slim-buster

ARG app_name="helloworld"
ARG DOCKERIZE_VERSION="v0.6.1"

ENV APP_NAME $app_name

ENV DJANGO_SETTINGS_MODULE $django_settings

ARG pipenv_skip_lock=1
ENV PIPENV_SKIP_LOCK $pipenv_skip_lock

ENV PIPENV_MAX_SUBPROCESS=2
ENV PIPENV_MAX_DEPTH=1

RUN pip install pipenv==2020.6.2 && mkdir -p /code && chown -R 1000:1000 /code


RUN apt-get update && apt-get install -y build-essential wget libmariadb-dev-compat libcurl4-openssl-dev libssl-dev build-essential libpq-dev && wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz && rm -rf /var/lib/apt/lists/*

USER 1000

WORKDIR /code

COPY --chown=1000 ./Pipfile /code/Pipfile

ENV WORKON_HOME /tmp

RUN pipenv install --dev

USER 0

RUN apt-get remove -y build-essential

USER 1000

WORKDIR /code

COPY --chown=1000 ./helloworld /code

ENTRYPOINT ["pipenv"]
