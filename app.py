from flask import Flask, render_template, request, redirect, flash, url_for
from flask_mail import Mail, Message

from data import db_session
from data.users import User
from data.persons import Person
from data.notifications import Notification
from data.messages import Message
from data import db_session
from werkzeug.security import check_password_hash, generate_password_hash
from data.company_data import email_pass_data

import secrets
import string
from datetime import datetime
import sqlite3
import os
from pathlib import Path

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.static_folder = 'static'
db_session.global_init("database/owwl.db")
db_sess = db_session.create_session()

# for email transfering
app.config['MAIL_SERVER'] = 'smtp.yandex.ru'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = email_pass_data['email']
app.config['MAIL_PASSWORD'] = email_pass_data['password']
mail = Mail(app)

# for text messages
messages_lst = []


def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password


def main():
    pass


def authenticate_user(login, password):
    user = db_sess.query(User).filter(User.login == login).first()

    if not user or not check_password_hash(user.hashed_password, password):
        return False
    return True

# routes
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if 'login_form' in request.form:
            login = request.form.get('login')
            password = request.form.get('password')

            if authenticate_user(login, password):
                flash('Вход выполнен успешно!', 'success')
                return redirect(url_for('main_page'))
            else:
                flash('Неверный логин или пароль', 'error')
        elif 'reset_form' in request.form:
            email = request.form.get('email')
            # changing password in db
            user_to_update = db_sess.query(User).filter(User.login == email.split('@')[0]).first()
            if user_to_update:
                new_pass = generate_password()
                user_to_update.hashed_password = generate_password_hash(new_pass)

                msg = Message( 
                'OWWL Company', 
                sender = email_pass_data['email'],
                recipients = [email])
                msg.body = f'Ваш новый пароль: {new_pass}. Никому его не сообщайте!'
                mail.send(msg)
            else:
                print('There is no such user')
                flash('Такого пользователя не существует', 'error')
            db_sess.commit()

            return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/search')
def search():
    return render_template('search.html')


@app.route('/with_response')
def with_response():
    return render_template('with_response.html')


@app.route('/popup_window')
def popup_window():
    return render_template('popup_window.html')


@app.route('/popup_window_with_responses')
def popup_window_with_responses():
    return render_template('popup_window_with_responses.html')


@app.route('/popup_window_performer_selected')
def popup_window_performer_selected():
    return render_template('popup_window_performer_selected.html')


@app.route('/popup_window_awaiting_loading')
def popup_window_awaiting_loading():
    return render_template('popup_window_awaiting_loading.html')


@app.route('/popup_window_confirmed_by_customer')
def popup_window_confirmed_by_customer():
    return render_template('popup_window_confirmed_by_customer.html')


@app.route('/creating_application')
def creating_application():
    return render_template('creating_application.html')


@app.route('/add_recipient')
def add_recipient():
    return render_template('add_recipient.html')


@app.route('/creating_application_updated')
def creating_application_updated():
    return render_template('creating_application_updated.html')


@app.route('/auto')
def auto():
    return render_template('auto.html')


@app.route('/car_registration')
def car_registration():
    return render_template('car_registration.html')


@app.route('/car_editing')
def car_editing():
    return render_template('car_editing.html')


@app.route('/warehouses')
def warehouses():
    return render_template('warehouses.html')


@app.route('/warehouses_registration')
def warehouses_registration():
    return render_template('warehouses_registration.html')


@app.route('/warehouses_editing')
def warehouses_editing():
    return render_template('warehouses_editing.html')


@app.route('/adding_legal_entity')
def adding_legal_entity():
    return render_template('adding_legal_entity.html')


def max_id(table_name): # find out the largest id
    conn = sqlite3.connect('database/owwl.db')
    cursor = conn.cursor()
    cursor.execute(f'SELECT MAX(id) FROM {table_name}')
    return cursor.fetchone()[0]


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    # for showing data
    conn = sqlite3.connect('database/owwl.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM persons WHERE id = (SELECT MAX(id) FROM persons)')
    first_row_data = cursor.fetchone()
    first_row_data = first_row_data[1:]
    conn.close()
    dict_ = {
        'contact_person': first_row_data[0],
        'position': first_row_data[1],
        'work_phone_num': first_row_data[2],
        'mobile_phone_num': first_row_data[3],
        'mail': first_row_data[4],
        'accounting_work_phone_num': first_row_data[5],
        'accounting_mobile_phone_num': first_row_data[6],
        'accounting_mail': first_row_data[7],
        'full_name': first_row_data[8],
        'short_name': first_row_data[9],
        'general_manager': first_row_data[10],
        'chief_accountant': first_row_data[11],
        'legal_address': first_row_data[12],
        'postal_address': first_row_data[13],
        'phone': first_row_data[14],
        'email': first_row_data[15],
        'inn': first_row_data[16], 
        'kpp': first_row_data[17],
        'ogrn': first_row_data[18],
        'tax_system': first_row_data[19],
        'full_bank_name': first_row_data[20],
        'payment_account': first_row_data[21],
        'bik': first_row_data[22],
        'correspondent_account': first_row_data[23]
    }
    
    # methods processing
    if request.method == 'POST':
        try:
            person = Person(
                contact_person=request.form.get('contact_person'),
                position=request.form.get('position'),
                work_phone_num=request.form.get('work_phone_num'),
                mobile_phone_num=request.form.get('mobile_phone_num'),
                mail=request.form.get('mail'),
                accounting_work_phone_num=request.form.get('accounting_work_phone_num'),
                accounting_mobile_phone_num=request.form.get('accounting_mobile_phone_num'),
                accounting_mail=request.form.get('accounting_mail'),
                full_name=request.form.get('full_name'),
                short_name=request.form.get('short_name'),
                general_manager=request.form.get('general_manager'),
                chief_accountant=request.form.get('chief_accountant'),
                legal_address=request.form.get('legal_address'),
                postal_address=request.form.get('postal_address'),
                phone=request.form.get('phone'),
                email=request.form.get('email'),
                inn=request.form.get('inn'),
                kpp=request.form.get('kpp'),
                ogrn=request.form.get('ogrn'),
                tax_system=request.form.get('tax_system'),
                full_bank_name=request.form.get('full_bank_name'),
                payment_account=request.form.get('payment_account'),
                bik=request.form.get('bik'),
                correspondent_account=request.form.get('correspondent_account')
            )
            db_sess.add(person)
            db_sess.commit()
            print('Added to db successfully')

            avat_image = request.files['image']
            if avat_image.filename == '':
                print('No selected file')
            else:
                # downloading
                avat_image.save(f'static/user_avatars/id_{max_id('persons')}{os.path.splitext(avat_image.filename)[-1]}')
                print('File uploaded successfully')
        except Exception as e:
            print(e)

    # choose max id
    max_id_num, max_id_filename = 0, None
    for filename in os.listdir(Path('static/user_avatars')):
        id_int = int(filename.split('_')[1].split('.')[0])
        if id_int > max_id_num:
            max_id_num = id_int
            max_id_filename = filename
    print(max_id_num, max_id_filename)

    return render_template('profile.html', dict_=dict_, max_id_filename=max_id_filename)


@app.route('/main_page', methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        if 'chat_form' in request.form:
            text = request.form.get('text_input')

            # time
            now = datetime.now()
            time, day, month, year = now.time(), now.day, now.month, now.year
            string_for_db = f'{time} {day} {month} {year}'
            if text:
                message = Message()
                message.text = text
                message.timestamp = string_for_db
                messages_lst.append([text, string_for_db])
                
                db_sess = db_session.create_session()
                db_sess.add(message)
                db_sess.commit()
                
    return render_template('main_page.html', messages_lst=messages_lst)


@app.route('/documents')
def documents():
    return render_template('documents.html')


@app.route('/notifications_center')
def notifications_center():
    notif_for_html = []
    for i in db_sess.query(Notification).all():
        # defining type
        if 'Вы создали' in str(i).split('__')[-1]:
            icon_type = 'box'
            before, middle, after = str(i).split('__')[-1].replace('Вы создали', "").partition('на сумму')
        elif 'На вашу' in str(i).split('__')[-1]:
            icon_type = 'arrows'
            before, middle, after = str(i).split('__')[-1].replace('На вашу', "").partition('на сумму')
        elif 'Ваша' in str(i).split('__')[-1]:
            icon_type = 'message'
            before, middle, after = str(i).split('__')[-1].replace('Ваша', "").partition('на сумму')
        elif 'Вы удалили' in str(i).split('__')[-1]:
            icon_type = 'delete'
            before, middle, after = str(i).split('__')[-1].replace('Вы удалили', "").partition('на сумму')

        message_part_1 = before
        message_part_2 = middle + after

        notif_for_html.append([icon_type, str(i).split('__')[1], [message_part_1, message_part_2]])

    return render_template('notifications_center.html', notif_for_html=notif_for_html)


@app.route('/application_log')
def application_log():
    return render_template('application_log.html')


if __name__ == '__main__':
    main()
    app.run(host='0.0.0.0', debug=True)