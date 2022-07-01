from flask import request
from flask_restx import Namespace, Resource

from container import auth_service, user_service

auth_ns = Namespace('auth')


@auth_ns.route("/register/")
class AuthView(Resource):
    def post(self):
        return user_service.create(request.json)


@auth_ns.route("/login/")
class AuthView(Resource):
    def post(self):
        return auth_service.auth_login(request.json)

    def put(self):
        return auth_service.get_refresh_token(request.json)
