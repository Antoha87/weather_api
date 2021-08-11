migrate:
	docker-compose run --rm django python3 weather_app/manage.py migrate

makemigrations:
	docker-compose run --rm django python3 weather_app/manage.py makemigrations

shell:
	docker-compose run --rm django python3 weather_app/manage.py shell

flush:
	docker-compose run --rm django python3 weather_app/manage.py flush

superuser:
	docker-compose run --rm django python3 weather_app/manage.py createsuperuser

fill_weather_db:
	docker-compose run --rm django python3 weather_app/manage.py fill_weather_db

fill_db:
	docker-compose run --rm django python3 weather_app/manage.py fill_db

fill_crypto_db:
	docker-compose run --rm django python3 weather_app/manage.py fill_crypto_db

fill_users_db:
	docker-compose run --rm django python3 weather_app/manage.py fill_users_db

fill_shawarma_db:
	docker-compose run --rm django python3 weather_app/manage.py fill_shawarma_db

process_parsed:
	docker-compose run --rm django python3 weather_app/manage.py process_parsed

export_to_excel:
	docker-compose run --rm django python3 weather_app/manage.py export_to_excel\

collectstatic:
	docker-compose run --rm django python3 weather_app/manage.py collectstatic

help:
	docker-compose run --rm django python3 weather_app/manage.py
