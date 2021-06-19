""" Module for movies model schema
"""

from marshmallow import Schema, fields
from .genres import GenresSchema


class MovieSchema(Schema):
    _id = fields.Int(dump_only=True)
    title = fields.Str()
    genres = fields.Nested(GenresSchema,  many=True)
    release_year = fields.Int()
    expiry_date = fields.Date()

class MovieInputSchema(Schema):
    title = fields.Str(required=True)
    release_year = fields.Int(required=True)
    expiry_date = fields.Date(required=True)
