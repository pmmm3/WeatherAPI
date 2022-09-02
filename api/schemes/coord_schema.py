import datetime as dt
from marshmallow import Schema, ValidationError, fields, validates


class CoordSchema(Schema):
    lon = fields.Float(required = True)
    lat = fields.Float(required=True)
