#!/bin/bash

# Wait for the database to be ready
/wait-for-it.sh db:5432 --timeout=30 --strict -- echo "Database is up and running"

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start Gunicorn server
exec gunicorn core.wsgi:application --bind 0.0.0.0:8000
