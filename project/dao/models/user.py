from project.dao.models.base import BaseMixin
from project.setup_db import db


class User(BaseMixin, db.Model):
    __tablename__ = 'user'
    name = db.Column(db.String)
    surname = db.Column(db.String)
    password = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    favorite_genre = db.Column(db.String)
