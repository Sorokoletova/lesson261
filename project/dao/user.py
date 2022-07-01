from flask_restx import abort

from project.dao.models.user import User
from project.utils import get_hash


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_id(self, nid):
        user = self.session.query(User).filter(User.id == nid).first()
        return user

    def create(self, data):
        user = User(**data)
        self.session.add(user)
        self.session.commit()
        return user

    def update(self, user,  name, surname, favorite_genre):
        user.name = name
        user.surname = surname
        user.favorite_genre = favorite_genre
        self.session.commit()

    def update_password(self, user, password_old, password_new):
        hash_password = get_hash(password_old)
        if user.password == hash_password:
            user.password = get_hash(password_new)
            self.session.commit()
        else:
            abort(401, "Нет такого пароля")
