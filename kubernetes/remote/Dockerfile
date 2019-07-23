FROM python:3.7
ENV PYTHONUNBUFFERED 1

COPY . code
WORKDIR code

RUN rm -Rf migrations

RUN pip install --upgrade pip -r requirements.txt

EXPOSE 8080

CMD python manage.py db init && \
    python manage.py db migrate && \
    python manage.py db upgrade && \
    gunicorn --bind 0.0.0.0:8080 --workers=6 wsgi:app
