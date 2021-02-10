import os
from flask import (Flask, request,
                  send_from_directory, render_template, redirect)

from models import db


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.app_context().push()

db.init_app(app)
db.create_all()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    print(username, password)

    return redirect('/admin')


@app.route('/admin')
def admin():
    return render_template('admin/index.html')

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)


if __name__ == '__main__':
    print(BASE_DIR)
    app.run(debug=True)
