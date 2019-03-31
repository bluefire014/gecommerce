FROM python:3.7.2-alpine3.9

ADD ./django/gecommerce /code
WORKDIR /code

VOLUME [ "/code" ]

RUN apk update && apk add bash python3-dev postgresql-dev postgresql-client build-base
RUN pip install --upgrade setuptools
RUN easy_install -U setuptools
RUN pip install -r requirements.txt