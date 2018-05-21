from sqlalchemy import (
    Column, String, Integer, ForeignKey, Text
)

from app.database import Base


class Object(Base):
    __tablename__ = 'object'
    id = Column(Integer, primary_key=True)

    title = Column(String(255), nullable=False)
    description = Column(Text)


class Operation(Base):
    __tablename__ = 'operation'
    id = Column(Integer, primary_key=True)

    object_id = Column(ForeignKey('object.id'), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text)
