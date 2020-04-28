#!/usr/bin/env bash

python manage.py migrate
gunicorn NewsletterApplication.wsgi:application --bind 0.0.0.0:8000 --workers 3
