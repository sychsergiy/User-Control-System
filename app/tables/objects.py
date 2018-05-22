from sqlalchemy import (
    Column, String, Integer, ForeignKey, Text
)
from sqlalchemy.orm import relationship

from app.database import Base


class Object(Base):
    __tablename__ = 'object'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)

    socialapp_id = Column(Integer, ForeignKey('socialapp.id'), nullable=False)
    socialapp = relationship('SocialApp')

    def __str__(self):
        return 'Object {}'.format(self.title)

    def __repr__(self):
        return 'Object {}'.format(self.title)


class Operation(Base):
    __tablename__ = 'operation'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)

    object_id = Column(ForeignKey('object.id'), nullable=False)
    object = relationship('Object', backref='operations')

    def __str__(self):
        return 'Operation: {}'.format(self.title)

    def __repr__(self):
        return 'Operation: {}'.format(self.title)
