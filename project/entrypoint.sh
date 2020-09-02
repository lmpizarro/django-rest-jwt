#!/bin/sh

if [ "$CONTAINER" = "web" ]
then
    echo "running container web"
    python manage.py flush --noinput
    python manage.py migrate --noinput
    python manage.py createsuperuser2 --username admin --password admin --noinput --email 'blank@email.com'
    python manage.py init_db
    python manage.py collectstatic --no-input
    gunicorn -c gunicorn.py project.wsgi:application
elif [ "$CONTAINER" = "worker" ]
then
  sleep 10
  echo "running worker"
  celery -A project worker -B -l info
fi
exec "$@"
