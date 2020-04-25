import sqlalchemy

from .db_session import SqlAlchemyBase


class Role(SqlAlchemyBase):
    __tablename__ = 'roles'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String)

    def __repr__(self):
        return f'<Roles> {self.id} {self.title}'

