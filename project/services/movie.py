from project.dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_id(self, nid):
        return self.dao.get_id(nid)

    def get_all_sort(self):
        return self.dao.get_all_sort()
