up:
	docker compose --env-file env up --build -d

down:
	docker compose --env-file env down 

sh:
	docker exec -ti loader bash

run-etl:
	docker exec loader python load_user_data.py

warehouse:
	docker exec -ti warehouse psql postgres://sdeuser:sdepassword1234@localhost:5432/warehouse

pytest:
	docker exec loader pytest -p no:warnings -v /opt/sde/test

format:
	docker exec loader python -m black -S --line-length 79 /opt/sde
	docker exec loader isort /opt/sde

type:
	docker exec loader mypy --ignore-missing-imports /opt/sde

lint:
	docker exec loader flake8 /opt/sde

ci: format type lint pytest
