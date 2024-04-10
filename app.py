from flask import Flask, render_template, request, redirect, flash, url_for
from flask_mail import Mail, Message

from data import db_session
from data.users import User
from data import db_session
from werkzeug.security import check_password_hash, generate_password_hash
from data.company_data import email_pass_data

import secrets
import string

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
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

@app.route('/main_page')
def main_page():
    return render_template('main_page.html')

@app.route('/with_response')
def with_response():
    return render_template('with_res.hponsetml')

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


if __name__ == '__main__':
    main()
    app.run(host='0.0.0.0', debug=True)