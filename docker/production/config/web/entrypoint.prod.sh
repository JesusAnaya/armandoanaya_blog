#!/bin/sh

python manage.py migrate --noinput
python manage.py collectstatic --no-input
gunicorn armandoanaya_blog.wsgi:application --bind 0.0.0.0:8000 -w 4
