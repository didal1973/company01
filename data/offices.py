import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Office(SqlAlchemyBase):
    __tablename__ = 'offices'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    countryid = sqlalchemy.Column(sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey("countries.id"))
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    phone = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    contact = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    country = orm.relation('Country')

    def __repr__(self):
        return f'<Office> {self.id} {self.country_id} {self.title}'