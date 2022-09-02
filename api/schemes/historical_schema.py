
from typing_extensions import Required
from marshmallow import Schema, fields
from api.schemes.city_schema import CitySchema
from api.schemes.info_schema import InfoWeatherSchema


class HistoricalSchema(Schema):
    city = fields.Nested(CitySchema, required=True)
    list = fields.Nested(InfoWeatherSchema, many=True, required=True, data_key='historical_weather')
