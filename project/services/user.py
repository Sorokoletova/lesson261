

from project.dao.user import UserDAO
from project.utils import get_hash


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_id(self, nid):
        return self.dao.get_id(nid)

    def create(self, data):
        data["password"] = get_hash(data["password"])
        self.dao.create(data)

    def update(self, user, name, surname, favorite_genre):
        self.dao.update(user, name, surname, favorite_genre)

    def update_password(self, user, password_old, password_new):
        self.dao.update_password(user, password_old, password_new)
