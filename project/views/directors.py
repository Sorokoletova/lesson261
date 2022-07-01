from flask import abort, request
from flask_restx import Resource, Namespace
from container import director_service
from project.schemas.director import DirectorSchema

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route("/")
class DirectorView(Resource):
    def get(self):
        all_director = director_service.get_all()
        return directors_schema.dump(all_director), 200


@director_ns.route("/<int:nid>")
class DirectorView(Resource):

    def get(self, nid):
        director = director_service.get_id(nid)
        if director is None:
            abort(404)
        return director_schema.dump(director), 200
