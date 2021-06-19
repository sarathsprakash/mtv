""" Module for movies model.
"""

from .base import Base
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.orm import backref, relationship


class Movies(Base):
    __tablename__ = 'movies'
    _id = Column("id", Integer,  unique = True, primary_key=True, nullable=False)
    title = Column(String(200), nullable=False, index=True)
    release_year = Column(Integer, nullable = False)
    expiry_date = Column(Date, nullable = False)
    genres = relationship("Genres", secondary='movie_genres', backref=backref('movies', lazy='dynamic'))

    def __init__(self, title=None, release_year=None, expiry_date=None):
        self.title = title
        self.release_year = release_year
        self.expiry_date = expiry_date
