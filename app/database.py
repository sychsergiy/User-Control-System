import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


def get_metadata():
    from app import tables
    return Base.metadata


def get_database_url():
    try:
        return os.environ['DATABASE_URL']
    except KeyError:
        raise EnvironmentError('Provide DATABASE_URL environment variable')


engine = create_engine(get_database_url())

Base = declarative_base()
