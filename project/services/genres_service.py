from project.dao import GenreDAO


class GenresService():
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_item_by_id(self, pk):
        genre = self.dao.get_by_id(pk)
        return genre

    def get_all_genres(self):
        genres = self.dao.get_all()
        return genres
