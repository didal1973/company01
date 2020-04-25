import sqlalchemy

from .db_session import SqlAlchemyBase


class Country(SqlAlchemyBase):
    __tablename__ = 'countries'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    def __repr__(self):
        return f'<Country> {self.id} {self.name}'

