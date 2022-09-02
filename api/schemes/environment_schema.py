import datetime as dt
from marshmallow import Schema, ValidationError, fields, validates


class EnvironmentSchema(Schema):
    temp = fields.Float(required=True)
    temp_max = fields.Float(required=True)
    temp_min = fields.Float(required=True)
    pressure= fields.Float(required=True)
    humidity= fields.Float(required=True)
