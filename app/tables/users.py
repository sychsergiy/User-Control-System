from sqlalchemy import (
    Column, String, Integer, ForeignKey, DateTime, Text
)

from app.database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    phone_number = Column(String(255), nullable=False)
    profile_picture = Column(String(255), nullable=False)

    socialapp_id = Column(ForeignKey('socialapp.id'), nullable=False)


class SocialToken(Base):
    __tablename__ = 'socialtoken'

    id = Column(Integer, primary_key=True)
    access_token = Column(String(255))
    expires_at = Column(DateTime)

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)


class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)

    user_id = Column(ForeignKey('user.id'), nullable=False)
