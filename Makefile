deps:
	pip install -r requirements.txt

setup:
	./manage.py makemigrations
	./manage.py migrate

run:
	./manage.py runserver

restart:
	dropdb db
	createdb db
	./manage.py migrate
	./manage.py createsuperuser

reset:
	createdb db
	./manage.py migrate
	./manage.py createsuperuser

creatdb:
	dropdb db
	createdb db

merge:
	./manage.py makemigrations --merge

user:
	./manage.py createsuperuser

core:
	./manage.py startapp core

home:
		./manage.py startapp home

shell:
		./manage.py shell
