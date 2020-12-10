#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi
/bin/sh ln -snf /usr/hare/zoneinfo/Asia/Seoul /etc/localtime && echo "Asia/Seoul" > /etc/timezone

python manage.py flush --no-input
python manage.py collectstatic --noinput
python manage.py createsuperuser --noinput \
        --username admin \
        --email a@a.com
python manage.py makemigrations
python manage.py migrate

exec "$@"
