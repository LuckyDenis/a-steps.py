# coding: utf8
from gino import Gino
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Column
from sqlalchemy import CheckConstraint
from sqlalchemy import func
from sqlalchemy_utils import EmailType
from sqlalchemy_utils import UUIDType
from sqlalchemy_utils import PasswordType


db = Gino()
convention = {
  "ix": '%(column_0_label)s_idx',
  "uq": "%(table_name)s_%(column_0_name)s_uq",
  "ck": "%(table_name)s_%(constraint_name)s_ck",
  "fk": "%(table_name)s_%(column_0_name)s_%(referred_table_name)s_fk",
  "pk": "%(table_name)s_pk"
}

db.naming_convention = convention


class Author(db.Model):
    __tablename__ = 'authors'
    __table_args__ = [
        CheckConstraint('registered_date <= visited_data'),
        CheckConstraint('email LIKE %_@_%_.__%')
    ]

    author_id = Column(UUIDType(binary=False), primary_key=True, index=True)
    email = Column(EmailType(), nullable=False, unique=True, index=True)
    password = Column(
        PasswordType(length=20, schemes=['pbkdf2_sha512']), nullable=False)

    first_name = Column(String(35), nullable=False)
    last_name = Column(String(35), nullable=False)

    registered_date = Column(
        DateTime(timezone=False), server_default=func.now(), nullable=False)
    visited_data = Column(
        DateTime(timezone=False), server_onupdate=func.now(), nullable=False)
