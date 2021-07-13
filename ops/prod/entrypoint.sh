#!/bin/sh


echo "Waiting for postgres..."

while ! nc -z $DB_HOST $DB_PORT; do
  sleep 0.1
done

echo "PostgreSQL started"
python manage.py collectstatic --no-input --clear
python manage.py migrate
python manage.py loaddata account_group.json

exec "$@"
