FROM python:3.7
ENV PYTHONUNBUFFERED 1

COPY . code
WORKDIR code

RUN rm -Rf migrations

RUN pip install --upgrade pip -r requirements.txt

CMD python manage.py db init && \
    python manage.py db migrate && \
    python manage.py db upgrade && \
    gunicorn --bind 0.0.0.0:$PORT --workers=6 wsgi:app
