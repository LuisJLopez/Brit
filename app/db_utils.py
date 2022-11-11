from sqlalchemy import create_engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker

from .settings import DATABASE_URL

# Engine & session creation
engine = create_engine(DATABASE_URL)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


def dbconnect(func):
    """Database decorator which takes in a function and provides a db session"""

    def inner(*args, **kwargs):
        session: session = Session()
        try:
            func(*args, **kwargs)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            Session.remove()

    return inner
