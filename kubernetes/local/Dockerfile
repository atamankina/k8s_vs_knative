FROM python:3.7
ENV PYTHONUNBUFFERED 1

COPY . code
WORKDIR code

RUN rm -Rf migrations

RUN pip install -r requirements.txt

EXPOSE 5000

CMD python manage.py db init && \
    python manage.py db migrate && \
    python manage.py db upgrade && \
    gunicorn --bind 0.0.0.0:5000 --workers=4 wsgi:app
