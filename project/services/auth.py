from flask_restx import abort

# from function import get_hash, generate_tokens, decode_tokens
from project.dao.auth import AuthDAO
from project.utils import get_hash, generate_tokens, decode_tokens


class AuthService:
    def __init__(self, dao: AuthDAO):
        self.dao = dao

    def auth_login(self, data: dict):
        """ Проверяем пользователя при аутентификации хешируем пвроль и создаем токен """
        users = self.dao.get_find_username(data['email'])
        if users is None:
            abort(401, "Нет такого  пользователя")
        hash_password = get_hash(data['password'])
        if users['password'] != hash_password:
            abort(401, "Нет такого пароля")

        tok_user = generate_tokens(
            {"password": data['password'],
             "email": data['email'],
             "id": users['id']}
        )

        return tok_user

    def get_refresh_token(self, token: dict):
        """ обновляем пару токенов"""
        data = decode_tokens(token['refresh_token'])
        new_token = generate_tokens(
            {"password": data['password'],
             "email": data['email'],
             "id": data['id']}
        )
        return new_token
