#!/usr/bin/env bash

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('${NEWSLETTER_ADMIN_USER}', '${NEWSLETTER_ADMIN_EMAIL}', '${NEWSLETTER_ADMIN_PASSWORD}') if len(User.objects.filter(username='${NEWSLETTER_ADMIN_USER}')) == 0 else print('superuser was already created')"

gunicorn NewsletterApplication.wsgi:application --bind 0.0.0.0:8000 --workers 3
