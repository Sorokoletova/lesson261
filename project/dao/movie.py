from flask import request

from project.dao.models.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        movies_all = self.session.query(Movie)
        args = request.args
        if 'status' in args and args.get('status') == 'new' and 'page' in args:
            page = int(args.get('page'))
            movies = self.session.query(Movie).order_by(Movie.year.desc())
            movie = movies.paginate(page, 12, False)
            return movie.items
        elif 'status' in args and args.get('status') == 'new':
            movies_all = self.session.query(Movie).order_by(Movie.year.desc()).all()
        elif 'page' in args:
            page = int(args.get('page'))
            movies = movies_all.paginate(page, 12, False)
            return movies.items
        # if 'status' in args and args.get('status') == 'new' and 'page' in args:
        #     page = int(args.get('page'))
        #     movies = self.session.query(Movie).order_by(Movie.year.desc()).all()
        #     movie = movies.paginate(page, 12, False)
        #     return movie.items
        return movies_all

    def get_id(self, nid):
        movie = self.session.query(Movie).filter(Movie.id == nid).first()
        return movie
