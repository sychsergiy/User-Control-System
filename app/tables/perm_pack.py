from sqlalchemy import (
    Table, Column, Integer, ForeignKey, String, Text, UniqueConstraint
)
from sqlalchemy.orm import relationship

from app.database import Base

permpack_operation = Table(
    'permpack_operation', Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('permpack_id', Integer, ForeignKey('permpack.id')),
    Column('operation_id', Integer, ForeignKey('operation.id')),

    UniqueConstraint('permpack_id', 'operation_id', name='UT_permpack_operation')
)


class PermissionsPack(Base):
    __tablename__ = 'permpack'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)

    socialapp_id = Column(ForeignKey('socialapp.id'), nullable=False)
    socialapp = relationship('SocialApp')

    permission = relationship('Operation', secondary=permpack_operation)

    def __str__(self):
        return 'Permissions Pack: {}'.format(self.title)

    def __repr__(self):
        return 'Permissions Pack: {}'.format(self.title)
