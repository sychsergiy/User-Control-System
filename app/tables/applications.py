from sqlalchemy import (
    Table, Column, String, Integer, Boolean, ForeignKey
)

from app.database import Base


class SocialApp(Base):
    __tablename__ = 'socialapp'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    client_id = Column(String(255), nullable=False)
    secret_id = Column(String(255), nullable=False)


class Admin(Base):
    __tablename__ = 'admin'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)

    is_superuser = Column(Boolean, default=False)


application_admin = Table(
    'application_admin', Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('admin_id', Integer, ForeignKey('admin.id'), nullable=False),
    Column('socialapp_id', Integer, ForeignKey('socialapp.id'), nullable=False)
)