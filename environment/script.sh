#!/usr/bin/env bash

pip install -r requirements.txt
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
python run.py