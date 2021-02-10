import os
import hashlib

from flask import (Flask, request,
                  send_from_directory, render_template, redirect)

from models import db, User
from datetime import datetime

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.app_context().push()

db.init_app(app)
db.create_all()


SECRET_KEY = '9e3d5c3bea7d493a84ded2788075350a'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password') # qwerty
    hashed_password = hashlib.sha512(password.encode() + SECRET_KEY.encode()).hexdigest()
    user = db.session.query(User).filter(User.username == username).first()

    if user is not None and user.password == hashed_password:
        return redirect('/admin')
    return 'Bad login', 400


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        hashed_password = hashlib.sha512(password.encode() + SECRET_KEY.encode()).hexdigest()

        user = User(username=username, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        print(user)
        return redirect('/')
    elif request.method == 'GET':
        return render_template('/register/index.html')

@app.route('/users')
def users_list():
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/admin')
def admin():
    return render_template('admin/index.html')

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)


if __name__ == '__main__':
    print(BASE_DIR)
    app.run(debug=True)
