from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://ucs_admin:adminpass@localhost/user_control_system')
Base = declarative_base()


def get_metadata():
    from app import tables
    return Base.metadata
