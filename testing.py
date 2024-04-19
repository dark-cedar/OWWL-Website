from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data import db_session
from data.notifications import Notification
from datetime import datetime


db_session.global_init("database/owwl.db")
db_sess = db_session.create_session()

notifications = ['Вы создали заявку (марка модель  - VIN: 1452354243242323), Москва - Санкт-Петербург на сумму 5000 руб.',
                 'На вашу заявку (BMW 7 серии VI (G11/G12) 740d), Москва - Санкт-Петербург на сумму 5000 руб, откликнулась компания Легит Транс предложив свою сумму 6000 руб.',
                 'Ваша заявка (BMW 7 серии VI (G11/G12) 740d), Москва - Санкт-Петербург на сумму 5000 руб, изменила статус на “ожидает погрузку”.',
                 'Вы удалили заявку (BMW 7 серии VI (G11/G12) 740d), Москва - Санкт-Петербург на сумму 5000 руб.',
                 'На вашу заявку (BMW 7 серии VI (G11/G12) 740d), Москва - Санкт-Петербург на сумму 5000 руб, откликнулась компания Легит Транс предложив свою сумму 6000 руб. Смотреть все отклики',
                 'Вы удалили заявку (BMW 7 серии VI (G11/G12) 740d), Москва - Санкт-Петербург на сумму 5000 руб.',
                 'Ваша заявка (BMW 7 серии VI (G11/G12) 740d), Москва - Санкт-Петербург на сумму 5000 руб, изменила статус на “ожидает погрузку”.']

for value in notifications:
    notif = Notification(
        date=datetime.now(),
        content=value
    )
    db_sess.add(notif)
    db_sess.commit()

