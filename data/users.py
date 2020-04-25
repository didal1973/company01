import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    officeid = sqlalchemy.Column(sqlalchemy.Integer,
                                  sqlalchemy.ForeignKey("offices.id"))
    roleid = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("roles.id"))
    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)
    password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    firstname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    lastname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    birthdate = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    active = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    role = orm.relation('Role')
    office = orm.relation('Office')

