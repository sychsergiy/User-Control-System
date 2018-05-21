from sqlalchemy import (
    Table, Column, Integer, ForeignKey, UniqueConstraint
)

from app.database import Base

role_permission = Table(
    'role_operation', Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('role_id', Integer, ForeignKey('role.id'), nullable=False),
    Column('operation_id', Integer, ForeignKey('operation.id'), nullable=False),

    UniqueConstraint('role_id', 'operation_id', name='UT_role_operation'),
)

user_extra_permission = Table(
    'user_operation', Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('user.id'), nullable=False),
    Column('operation_id', Integer, ForeignKey('operation.id'), nullable=False),

    UniqueConstraint('user_id', 'operation_id', name='UT_user_operation'),
)
