""" Module for genres model schema
"""

from marshmallow import Schema, fields


class GenresSchema(Schema):
    _id = fields.Int(dump_only=True)
    _type = fields.Str(required=True)


class GenreInputSchema(Schema):
    _type = fields.Str(required=True)