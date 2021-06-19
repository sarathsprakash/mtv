""" Module for Stream service.
"""
import os
import json

from datetime import datetime, timedelta

from nameko.rpc import rpc, RpcProxy
from nameko_sqlalchemy import Database as _Database
from stream.models import Base, Movies, Genres
from stream.schemas import GenresSchema, MovieSchema, MovieInputSchema, GenreInputSchema
from stream.utils import methods as _methods


class Stream(object):
    name = "stream"
    session =  RpcProxy('session')
    _db = _Database(Base)
    movies_schema = MovieSchema(many=True)
    movie_input_schema = MovieInputSchema()
    genres_schema = GenresSchema(many=True)
    genre_input_schema = GenreInputSchema()


    @_methods(['GET'])
    @rpc
    def docs(self):
        """ Gets Stream service docs
        """
        path = "{}{}".format(os.getcwd(), '/stream/docs/swagger.json')
        with open(path) as doc:
            return json.load(doc), 200

    @_methods(['GET'])
    @rpc
    def get_movie(self, movie_id):
        """ Gets movies by given movie_id.
        """
        with self._db.get_session() as db_session:
            movie = db_session.query(Movies).get(movie_id)
            if not movie:
                return {}, 404
            movie_schema = MovieSchema()
            result = movie_schema.dump(movie)
            return result, 200

    @_methods(['GET'])
    @rpc
    def get_movies(self):
        """ Get all available movies.
        """
        with self._db.get_session() as db_session:
            movies_obj = db_session.query(Movies).all()
            if not movies_obj:
                return {}, 404
            movies = self.movies_schema.dump(movies_obj)
            return movies, 200

    @_methods(['GET'])
    @rpc
    def get_genres(self):
        """ Gets all available genres
        """
        with self._db.get_session() as db_session:
            genres_obj = db_session.query(Genres).all()
            if not genres_obj:
                return {}, 404
            genres = self.genres_schema.dump(genres_obj)
            return genres, 200

    @_methods(['POST'])
    @rpc
    def add_movie(self, movie={}, genres=[]):
        """ Adds a new movie.
            kwargs:
                movie: <Dict> A dict of movie params
                        syntax:
                            {
                              title : <str>
                              release_year: <int(4)>
                              expiry_date: <Date[yyyy-mm-dd]>
                            }
                genres: (<List>) A list of acceptable genres
                        Refer methdo <get_genres>
            Returns:
                A <Dict> of added movie.
        """
        error = self.movie_input_schema.validate(movie)
        if error:
            return {'error': error }, 400
        movie_model = Movies(**movie)
        with self._db.get_session() as db_session:
            genres_obj = db_session.query(Genres).all()
            genre_types = [gen._type for gen in genres_obj]
            if set(genres).difference(genre_types):
                return {
                    'error': "Invalid genre types. Valid genre types are {}". format(genre_types)
                    }, 400
            movie_model = Movies(**movie)
            filter_genres = db_session.query(Genres).filter(Genres._type.in_(genres)).all()
            movie_model.genres=[filter_genre for filter_genre in filter_genres]
            db_session.add(movie_model)
            db_session.flush()

        with self._db.get_session() as db_session:
            movie_schema = MovieSchema()
            result = movie_schema.dump(
                db_session.query(Movies).get(movie_model._id)
            )

            return result, 201

    @_methods(['GET'])
    @rpc
    def delete_movie(self, movie_id):
        """ Deletes a new movie by id.

        """
        with self._db.get_session() as db_session:
            movie = db_session.query(Movies).get(movie_id)
            if not movie:
                return {
                    'error': "Invalid movie Id `{}`".format(movie_id)
                }, 400

            db_session.delete(movie)
            db_session.commit()
            return movie_id, 200


    @_methods(['GET'])
    @rpc
    def expiring_movies(self, days=30):
        """ Gets expriring movies by given days.
            kwargs:
                days: <int> days by which movies expires.
        """
        today = datetime.utcnow().date()
        expiry_date = today + timedelta(30)
        with self._db.get_session() as db_session:
            movies_obj = db_session.query(Movies).filter(
                Movies.expiry_date.between(today, expiry_date)
                ).all()
            if not movies_obj:
                return {}, 404
            movies = self.movies_schema.dump(movies_obj)
            return movies, 200
