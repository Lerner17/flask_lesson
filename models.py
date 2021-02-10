import flask_sqlalchemy

from datetime import datetime


db = flask_sqlalchemy.SQLAlchemy()


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    created_at = db.Column(db.Date, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f'<User {self.id}>'


# class Article(db.Model):

#     __tablename__ = 'articles'
