SHELL := /bin/bash

.PHONY: runserver

.DEFAULT_GOAL := runserver

runserver:
	python manage.py runserver 8000
runserver_plus:
	python manage.py runserver_plus 8020
allmigrations:
	python manage.py makemigrations && python manage.py migrate
# Create a super user from env var
# You need to define an env var : DJANGO_DEV_ADMIN. Example below
# DJANGO_DEV_ADMIN=name:email:password
# DJANGO_DEV_ADMIN=user@test.api:user@test.api:123asX3?23
createsuperuser:
	echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser(*'${DJANGO_DEV_ADMIN}'.split(':'))" | python manage.py shell
# Create a SECRET_KEY for settings
createsecret:
	python manage.py shell -c 'from django.core.management import utils; print(utils.get_random_secret_key())'
