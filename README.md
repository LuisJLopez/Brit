# Brit

#### Useful links:
- [Heroku app is Live :rocket:](https://brit-app.herokuapp.com/)
- [Main app entrypoint](/app/main.py)
- [DB engine and session decorator](/app/db_utils.py)
- [Basic Response class](/app/api_utils.py)
- [App settings](/app/settings.py)


#### The chosen tech stack:
  - Cloud platform - Heroku :cloud:
  - Backend - FastAPI, one reason being it was mentioned to me as the framework of choice, good learning opportunity
  - Python version 3.9.15
  - SQLAlchemy / Alembic for ORM / DB / Migrations
  - Pip / Pipfile as package manager
  - Frontend - is Jinja 2 templates for simplicity
  - Database - PostgreSQL (Hosted on Heroku)
  - I've create a Dockerfile and docker-compose for development & portability reasons

#### You want to run it?
> Running it should be as simple as running the two cmds below:

```
$ docker-compose build && docker-compose up
```

```
$ alembic upgrade head
```

