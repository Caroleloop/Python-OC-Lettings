#!/bin/sh
set -e

# Appliquer les migrations
echo "Applying database migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

# Lancer Gunicorn
echo "Starting Gunicorn..."
exec gunicorn oc_lettings_site.wsgi:application \
    --bind 0.0.0.0:$PORT  \
    --workers 3