# coding: utf8
from gino import Gino
from sqlalchemy import Boolean
from sqlalchemy import CheckConstraint
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Sequence
from sqlalchemy import SmallInteger
from sqlalchemy import String
from sqlalchemy import func
from sqlalchemy_utils import EmailType
from sqlalchemy_utils import PasswordType
from sqlalchemy_utils import UUIDType


db = Gino()
convention = {
  'ix': '%(column_0_label)s_idx',
  'uq': '%(table_name)s_%(column_0_name)s_uq',
  'ck': '%(table_name)s_%(constraint_name)s_ck',
  'fk': '%(table_name)s_%(column_0_name)s_%(referred_table_name)s_fk',
  'pk': '%(table_name)s_pk'
}

db.naming_convention = convention


class Author(db.Model):
    __tablename__ = 'authors'
    __table_args__ = (
        CheckConstraint(
            'registered_date <= visited_data', name='visited_datetime')
    )

    author_id = Column(UUIDType(binary=False), primary_key=True, index=True)
    email = Column(EmailType(), nullable=False, unique=True, index=True)
    password = Column(
        PasswordType(schemes=['pbkdf2_sha512']), nullable=False)

    first_name = Column(String(35), nullable=False)
    last_name = Column(String(35), nullable=False)

    registered_date = Column(
        DateTime(timezone=False), server_default=func.now(), nullable=False)
    visited_data = Column(
        DateTime(timezone=False), server_onupdate=func.now(), nullable=False)


class Category(db.Model):
    __tablename__ = 'categories'
    category_id = Column(SmallInteger(), primary_key=True, index=True)


class Algorithm(db.Model):
    __tablename__ = 'algorithms'
    __table_args__ = (
        CheckConstraint(
            'create_date <= publication_date', name='publication_date'),
        CheckConstraint('algorithm_id > 10000', name='algorithm_id'),
    )

    algorithm_id = Column(
        Integer(),
        Sequence('algorithm_id_seq', start=1000000, increment=1),
        primary_key=True, index=True
    )
    algorithm_name = Column(String(127), nullable=False)
    create_date = Column(
        DateTime(timezone=False), server_default=func.now(), nullable=False)
    publication_date = Column(
        DateTime(timezone=False), nullable=True)
    modify_date = Column(
        DateTime(timezone=False), nullable=True)
    publication_state = Column(Boolean(), default=False, nullable=False)
    category = Column(
        ForeignKey(
            'categories.category_id',
            onupdate='CASCADE',
            ondelete='RESTRICT'
        ), nullable=False)
    author = Column(
        ForeignKey(
            'authors.author_id',
            onupdate='CASCADE',
            ondelete='RESTRICT'
        ), nullable=False)
