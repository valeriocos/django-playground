# Django/MariaDB playground

- Tutorial at https://docs.djangoproject.com/en/3.1/intro/ 

## Requirements

- Docker-compose
- Django

## Docker-compose
```
version: '2.2'

services:
    mariadb:
      restart: on-failure:5
      image: mariadb:10.0
      expose:
        - "3306"
      ports:
        - "3306:3306"
      environment:
        - MYSQL_ROOT_PASSWORD=
        - MYSQL_ALLOW_EMPTY_PASSWORD=yes
        - MYSQL_DATABASE=test_sh
      command: --wait_timeout=2592000 --interactive_timeout=2592000 --max_connections=300 --sql_mode="STRICT_ALL_TABLES"
```

## Execution

```
cd django-playground
django-admin startproject helloworld

cd helloworld
# start the server
python manage.py runserver

# create app "polls"
python manage.py startapp polls

# create the SQL commands (e.g., update the database schema)
python manage.py makemigrations polls

# execute the SQL commands
python manage.py migrate

# query the Django model via a shell
python manage.py shell

# create a superuser to enter to the admin site
python manage.py createsuperuser
```