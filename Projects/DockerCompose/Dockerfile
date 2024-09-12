FROM python:3.12

WORKDIR /app

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY . /app

RUN pip install -r requirements.txt
RUN pip install Werkzeug==0.16.1 



