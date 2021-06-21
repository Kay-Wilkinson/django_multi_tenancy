#!/bin/sh
# Points to variable in .env
if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."
    # While netstat tcp port scan not equal to postgres host and port vars, sleep
    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi
# These will run via the exec command below within Docker shell.
# Flush clears out the db
python manage.py flush --no-input
python manage.py migrate_schemas --shared
&& python manage.py create_superuser --username $USERNAME --email $EMAIL --no-input \
python manage.py collectstatic --no-input --clear
# Exec command useful to ensure that child processes from commands get shut down correctly. Proxies signals etc.
exec "$@"