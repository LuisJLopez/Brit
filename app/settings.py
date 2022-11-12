import os
from enum import Enum, auto

from fastapi.templating import Jinja2Templates


# Environments
class Env(Enum):
    DEVELOPMENT: str = auto()
    HEROKU: str = auto()


# App environment
APP_ENV: str = os.environ.get("APP_ENV", Env.DEVELOPMENT.name)

# Database settings
def get_database_url():
    if APP_ENV == Env.DEVELOPMENT.name:
        database_url = os.environ.get("DATABASE_URL")
    elif APP_ENV == Env.HEROKU.name:
        database_url = os.environ.get("DATABASE_URL")
        if database_url.startswith("postgres://"):
            database_url = database_url.replace("postgres://", "postgresql://", 1)
    if not database_url:
        raise Exception("No valid DATABASE_URL environemnt variable has been set!")
    return database_url


DATABASE_URL: str = get_database_url()

TEMPLATES = Jinja2Templates(directory="app/static")

STATIC_DIR: str = "app/static"

ROOT_PAGE: str = "index.html"
