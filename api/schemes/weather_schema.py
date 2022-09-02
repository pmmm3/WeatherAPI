import datetime as dt
from marshmallow import Schema, ValidationError, fields, validates


class WeatherSchema(Schema):
    main = fields.Str(required=True, data_key='weather')
    description = fields.Str(required=True, data_key='weather_description')
