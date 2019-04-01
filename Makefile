build:
	docker-compose build

up:
	docker-compose up

down:
	docker-compose down

exec:
	docker exec -ti django bash

owner:
	sudo chown -R $(USER) django/

clean-db:
	sudo chown -R $(USER) postgres-data/
	rm -drf postgres-data/

migrations:
	docker exec django ./manage.py makemigrations
	docker exec django ./manage.py makemigrations products

migrate:
	docker exec django ./manage.py migrate

migrations:
	docker exec django ./manage.py makemigrations
	docker exec django ./manage.py makemigrations products

createsu:
	docker exec -ti django ./manage.py createsuperuser --username admin --email ''