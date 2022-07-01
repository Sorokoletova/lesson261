from flask import request, abort
from flask_restx import Resource, Namespace
from container import user_service
from project.schemas.user import UserSchema
from project.utils import auth_required, decode_tokens

user_ns = Namespace('users')
user_schema = UserSchema()


@user_ns.route("/")
class UserView(Resource):
    @auth_required
    def get(self):
        token = request.headers["Authorization"].split(" ")[-1]
        token_dec = decode_tokens(token)
        user = user_service.get_id(token_dec['id'])
        result = {"name": user.name, "surname": user.surname, "favorite_genre": user.favorite_genre}
        if user is None:
            abort(404)

        return user_schema.dump(result), 200

    @auth_required
    def patch(self):
        token = request.headers["Authorization"].split(" ")[-1]
        token_dec = decode_tokens(token)
        uid = token_dec['id']
        data = request.json
        user = user_service.get_id(uid)
        user_service.update(user=user, name=data['name'], surname=data['surname'],
                            favorite_genre=data['favorite_genre'])
        return "", 204


@user_ns.route("/password/")
class UserView(Resource):
    @auth_required
    def put(self):
        token = request.headers["Authorization"].split(" ")[-1]
        token_dec = decode_tokens(token)
        uid = token_dec['id']
        data = request.json
        user = user_service.get_id(uid)
        print(user)
        user_service.update_password(user=user, password_old=data['password_old'], password_new=data['password_new'])
        return "", 401
