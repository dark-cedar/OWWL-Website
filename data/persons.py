import sqlalchemy
from .db_session import SqlAlchemyBase
from flask_login import UserMixin


class Person(SqlAlchemyBase, UserMixin):
    __tablename__ = 'persons'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    contact_person = sqlalchemy.Column(sqlalchemy.String)
    position = sqlalchemy.Column(sqlalchemy.String)
    work_phone_num = sqlalchemy.Column(sqlalchemy.String)
    mobile_phone_num = sqlalchemy.Column(sqlalchemy.String)
    mail = sqlalchemy.Column(sqlalchemy.String)
    accounting_work_phone_num = sqlalchemy.Column(sqlalchemy.String)
    accounting_mobile_phone_num = sqlalchemy.Column(sqlalchemy.String)
    accounting_mail = sqlalchemy.Column(sqlalchemy.String)

    # second column
    full_name = sqlalchemy.Column(sqlalchemy.String)
    short_name = sqlalchemy.Column(sqlalchemy.String)
    general_manager = sqlalchemy.Column(sqlalchemy.String)
    chief_accountant = sqlalchemy.Column(sqlalchemy.String)
    legal_address = sqlalchemy.Column(sqlalchemy.String)
    postal_address = sqlalchemy.Column(sqlalchemy.String)
    phone = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String)
    inn = sqlalchemy.Column(sqlalchemy.String)
    kpp = sqlalchemy.Column(sqlalchemy.String)
    ogrn = sqlalchemy.Column(sqlalchemy.String)
    tax_system = sqlalchemy.Column(sqlalchemy.String)
    full_bank_name = sqlalchemy.Column(sqlalchemy.String)
    payment_account = sqlalchemy.Column(sqlalchemy.String)
    bik = sqlalchemy.Column(sqlalchemy.String)
    correspondent_account = sqlalchemy.Column(sqlalchemy.String)

    def __repr__(self):
        return f"<Person> {self.contact_person} {self.position} \
        {self.work_phone_num} {self.mobile_phone_num} {self.mail} \
        {self.accounting_work_phone_num} {self.accounting_mobile_phone_num} {self.accounting_mail}"