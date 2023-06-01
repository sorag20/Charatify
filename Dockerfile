FROM python:3.9.10

WORKDIR /usr/src/app

ENV FLASK_APP=app.py
ENV FLACK_ENV=development
ENV FLASK_RUN_PORT=8000
ENV FLASK_DEBUG=1
COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

