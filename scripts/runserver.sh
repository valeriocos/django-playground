dockerize -wait tcp://mariadb:3306 -timeout 1m &&
python helloworld/manage.py makemigrations polls
python helloworld/manage.py migrate

python helloworld/manage.py collectstatic --noinput
python helloworld/manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL
cd helloworld
gunicorn --name app --workers 2 --log-level info --reload --bind 0.0.0.0:8080 helloworld.wsgi:application