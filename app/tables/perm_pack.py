from sqlalchemy import (
    Table, Column, Integer, ForeignKey, String, Text, UniqueConstraint
)

from app.database import Base


class PermissionsPack(Base):
    __tablename__ = 'permpack'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)


permpack_operation = Table(
    'permpack_operation', Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('permpack_id', Integer, ForeignKey('permpack.id')),
    Column('operation_id', Integer, ForeignKey('operation.id')),

    UniqueConstraint('permpack_id', 'operation_id', name='UT_permpack_operation')
)
