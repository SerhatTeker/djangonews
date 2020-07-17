SHELL := /bin/bash

.PHONY: runserver

.DEFAULT_GOAL := runserver

runserver:
	python manage.py runserver_plus 8020
allmigrations:
	python manage.py makemigrations && python manage.py migrate
