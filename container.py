from project.dao import GenreDAO
from project.dao.auth import AuthDAO
from project.dao.director import DirectorDAO
from project.dao.movie import MovieDAO
from project.dao.user import UserDAO
from project.services import GenresService
from project.services.auth import AuthService
from project.services.director import DirectorService
from project.services.movie import MovieService
from project.services.user import UserService
from project.setup_db import db

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenresService(genre_dao)

user_dao = UserDAO(db.session)
user_service = UserService(user_dao)

auth_dao = AuthDAO(db.session)
auth_service = AuthService(auth_dao)
