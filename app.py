from flask import Flask, render_template

app = Flask(__name__)


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/main_page')
def main_page():
    return render_template('main_page.html')

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)