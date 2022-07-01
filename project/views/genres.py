from flask_restx import Namespace, Resource

from container import genre_service
from project.schemas.genre import GenreSchema


genres_ns = Namespace("genres")
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genres_ns.route("/")
class GenresView(Resource):
    def get(self):
        all_genres = genre_service.get_all_genres()
        return genres_schema.dump(all_genres), 200


@genres_ns.route("/<int:genre_id>")
class GenreView(Resource):

    def get(self, genre_id: int):
        genre = genre_service.get_item_by_id(genre_id)
        return genre_schema.dump(genre), 200
