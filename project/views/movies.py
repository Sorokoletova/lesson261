from flask import request, abort
from flask_restx import Resource, Namespace

from container import movie_service
from project.schemas.movie import MovieSchema

movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route("/")
class MovieView(Resource):
    def get(self):
        mov = movie_service.get_all()
        return movies_schema.dump(mov), 200


@movie_ns.route("/<int:nid>")
class MovieView(Resource):
    def get(self, nid):
        movie = movie_service.get_id(nid)
        if movie is None:
            abort(404)
        return movie_schema.dump(movie), 200
