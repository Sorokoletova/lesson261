from flask import request

from project.dao.models import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_by_id(self, pk):
        return self.session.query(Genre).filter(Genre.id == pk).one_or_none()

    def get_all(self):
        genre_all = self.session.query(Genre)
        args = request.args
        if 'page' in args:
            page = int(args.get('page'))
            genres = genre_all.paginate(page, 12, False)
            return genres.items
        return genre_all
