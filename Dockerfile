FROM python:3.7-alpine

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWEITEBYTECODE 1

COPY . .

RUN apk add -u zlib-dev jpeg-dev gcc musl-dev

RUN python3 -m pip install --upgrade pip

RUN pip install -r requirements.txt