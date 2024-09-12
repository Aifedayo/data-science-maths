FROM python:3.8

WORKDIR /app

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["flask", "run"]
