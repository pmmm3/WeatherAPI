import datetime as dt
from marshmallow import Schema, ValidationError, fields, post_load, validates

from api.schemes.coord_schema import CoordSchema


class CitySchema(Schema):
    coord = fields.Nested(CoordSchema, required=True, data_key='coordinates')
    name = fields.Str(default=None)

