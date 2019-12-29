FROM python:3.8.0-alpine

RUN adduser -D -g '' nahid

WORKDIR /home/nahid/app

RUN chown -R nahid /home/nahid/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /home/nahid/app/requirements.txt
RUN pip install -r requirements.txt

COPY ./.env.sample /home/nahid/app/.env

USER nahid
COPY . /app/
