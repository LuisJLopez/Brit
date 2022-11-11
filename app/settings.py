import os
from enum import Enum, auto

from fastapi.templating import Jinja2Templates


# Environments
class Env(Enum):
    DEVELOPMENT: str = auto()
    HEROKU: str = auto()


# App environment
APP_ENV: str = os.environ.get("APP_ENV", Env.DEVELOPMENT)

# Database settings
def get_database_url():

    if APP_ENV == Env.DEVELOPMENT.name:
        database_url = "postgresql://postgres:postgres@localhost:5432/brit"
    elif APP_ENV == Env.HEROKU.name:
        DATABASE_URL = os.environ.get("DATABASE_URL")
        if DATABASE_URL.startswith("postgres://"):
            database_url = DATABASE_URL.replace("postgres://", "postgresql://", 1)
    return database_url


DATABASE_URL: str = get_database_url()

TEMPLATES = Jinja2Templates(directory="app/static")

STATIC_DIR: str = "app/static"

ROOT_PAGE: str = "index.html"
