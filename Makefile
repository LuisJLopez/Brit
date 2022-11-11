.SILENT: ;
.DEFAULT_GOAL := help

run: ## run app
	uvicorn app.main:app --reload

run-db-in-docker:
	docker run --name basic-postgres --rm -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=admin -e PGDATA=/var/lib/postgresql/data/pgdata -v /tmp:/var/lib/postgresql/data -p 5432:5432 -it postgres:14.1-alpine

db-reset: ## Destroy all migrations and re-run from zero to head
	pipenv run alembic downgrade base
	make db-migrate

db-migrate: ## Run migrations
	pipenv run alembic upgrade head

db-rollback: ## Rollback last migration
	pipenv run alembic downgrade -1

help: ## display cmds
	awk 'BEGIN {FS = ":.?## "} /^[a-zA-Z_-]+:.?## / \
	{printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)