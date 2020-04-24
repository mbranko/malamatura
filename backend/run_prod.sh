#!/bin/sh
export DJANGO_SETTINGS=prod
cd /app
python3 manage.py migrate
uwsgi --ini /app/config/uwsgi-prod.ini
