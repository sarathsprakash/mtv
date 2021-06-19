""" Module for genres model.
"""

from .base import Base
from sqlalchemy import Column, Date, ForeignKey, Integer, String, Table
from sqlalchemy.orm import backref, relationship


movie_genres = Table('movie_genres',
     Base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.id', name="movie_fk", onupdate="CASCADE", ondelete="CASCADE"), nullable = False),
    Column('genre_id', Integer, ForeignKey('genres.id', name="genre_fk", onupdate="CASCADE", ondelete="CASCADE"), nullable = False)
)


class Genres(Base):
    __tablename__ = 'genres'
    _id = Column("id", Integer,  unique = True, primary_key=True)
    _type = Column("type", String(100), unique = True, nullable = False)

    def __init__(self, _type):
        self._type = _type
