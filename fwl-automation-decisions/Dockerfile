FROM python:3.7.3-alpine

WORKDIR /app

COPY flask_app /app/flask_app

COPY application /app/application

COPY domain /app/domain

COPY infrastructure /app/infrastructure

COPY unicorno.py /app/

COPY req.txt /app/

RUN ls

RUN pip install -r req.txt

#CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "unicorno:app"]

CMD gunicorn --bind 0.0.0.0:$PORT unicorno:app