from flask import request

from project.dao.models.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        director_all = self.session.query(Director)
        args = request.args
        if 'page' in args:
            page = int(args.get('page'))
            directors = director_all.paginate(page, 12, False)
            return directors.items
        return director_all

    def get_id(self, nid):
        director = self.session.query(Director).filter(Director.id == nid).first()
        return director
