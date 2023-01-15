FROM python:3.7-alpine

WORKDIR /app

COPY . .

RUN apk add -u zlib-dev jpeg-dev gcc musl-dev

RUN python3 -m pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8000
