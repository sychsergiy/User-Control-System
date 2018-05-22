from sqlalchemy import (
    Column, String, Integer, ForeignKey, DateTime, Text,
)
from sqlalchemy.orm import relationship

from app.database import Base

from .permissions import role_permission, user_extra_permission


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    phone_number = Column(String(255), nullable=False)
    profile_picture = Column(String(255), nullable=False)

    role_id = Column(ForeignKey('role.id'), nullable=False)
    role = relationship('Role')

    social_token = relationship('SocialToken', uselist=False, back_populates="user")
    permission = relationship(
        'Operation', secondary=user_extra_permission, backref='users'
    )

    def __str__(self):
        return 'User: {} {}'.format(self.first_name, self.last_name)

    def __repr__(self):
        return 'User: {} {}'.format(self.first_name, self.last_name)


class SocialToken(Base):
    __tablename__ = 'socialtoken'
    id = Column(Integer, primary_key=True)
    access_token = Column(String(255))
    expires_at = Column(DateTime)

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship("User", back_populates="social_token")


class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)

    socialapp_id = Column(ForeignKey('socialapp.id'), nullable=False)
    socialapp = relationship('SocialApp')

    users = relationship('User', back_populates='role')
    permission = relationship(
        'Operation', secondary=role_permission, backref='roles'
    )

    def __str__(self):
        return 'Role: {}'.format(self.title)

    def __repr__(self):
        return 'Role: {}'.format(self.title)
