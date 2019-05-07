#!/usr/bin/env bash

pip install -r requirements.txt
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
gunicorn --bind 0.0.0.0:5000 -w 4 wsgi:app