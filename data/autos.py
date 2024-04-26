import sqlalchemy
from .db_session import SqlAlchemyBase
from flask_login import UserMixin


class Auto(SqlAlchemyBase, UserMixin):
    __tablename__ = 'autos'

    auto = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    vin = sqlalchemy.Column(sqlalchemy.String, primary_key=True, nullable=False)
    request = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    status = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    creation_date = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    summ = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    loading_place = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    delivery_place = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    tk = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    type_carrier = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    confirmation_date = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    driver = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    warehouse_title = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    sender = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    receiver = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    

    def __repr__(self):
        return f"<Auto> {self.auto} {self.vin}"