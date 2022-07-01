import base64
import hashlib
import json
from datetime import datetime, timedelta

import jwt
from flask import request
from flask_restx import abort

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS, SECRET_KEY, AlGORITM, PWD_HASH_NAME


def read_json(filename, encoding="utf-8"):
    with open(filename, encoding=encoding) as f:
        return json.load(f)


def get_hash(password):
    """Хешируем пароль"""
    new_password = hashlib.pbkdf2_hmac(
        hash_name=PWD_HASH_NAME,
        password=password.encode('utf-8'),
        salt=PWD_HASH_SALT,
        iterations=PWD_HASH_ITERATIONS)
    return base64.b64encode(new_password).decode('utf-8')


def generate_tokens(data):
    """Создаем пару токенов"""
    data['exp'] = datetime.utcnow() + timedelta(minutes=30)
    data['refresh_token'] = False
    access_token = jwt.encode(payload=data, key=SECRET_KEY, algorithm=AlGORITM)
    data['exp'] = datetime.utcnow() + timedelta(days=60)
    data['refresh_token'] = True
    refresh_token = jwt.encode(payload=data, key=SECRET_KEY, algorithm=AlGORITM)
    tokens_user = {"access_token": access_token, "refresh_token": refresh_token}

    return tokens_user, 201

#print(generate_tokens({"password": 'password',
             # "email": 'email',
             # "id": 1}))

def decode_tokens(token):
    """Раскодируем токен"""
    dec_token = {}
    try:
        dec_token = jwt.decode(jwt=token, key=SECRET_KEY, algorithms=[AlGORITM])
    except Exception as e:
        print("JWT Decode Exception", e)
        abort(401)

    return dec_token

#print(decode_tokens("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNzd29yZCI6InBhc3N3b3JkMTEiLCJlbWFpbCI6IlBldHJvdmFLQGluYm94LnJ1IiwiaWQiOjIsImV4cCI6MTY1MjU0NTc3NSwicmVmcmVzaF90b2tlbiI6ZmFsc2V9.JvSpX8St7k2fH13toE171iElaLulMn10QW20rrZ0oKY"))


def auth_required(func):
    """Декоратор проверки на аутентификацию"""
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)

        token = request.headers["Authorization"].split(" ")[-1]
        try:
            jwt.decode(jwt=token, key=SECRET_KEY, algorithms=[AlGORITM])
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)
        return func(*args, **kwargs)

    return wrapper