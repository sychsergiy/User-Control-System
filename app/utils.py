from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker

from .database import engine

Session = sessionmaker()
Session.configure(bind=engine)


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
