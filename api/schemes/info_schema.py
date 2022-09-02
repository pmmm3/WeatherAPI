import datetime as dt
import json
from marshmallow import Schema, fields, post_dump,EXCLUDE
from api.schemes.environment_schema import EnvironmentSchema
from api.schemes.coord_schema import CoordSchema
from api.schemes.weather_schema import WeatherSchema


class InfoWeatherSchema(Schema):
    coord = fields.Nested(CoordSchema, required=True, data_key='coordinates')
    weather = fields.Nested(WeatherSchema, many=True, required=True)
    main = fields.Nested(EnvironmentSchema, required=True, data_key='environment')
    name = fields.Str(required=True)

    class Meta:
        ordered = True
        unknown = EXCLUDE

    @post_dump
    def return_as_object(self, data, **kwargs):
        if data.get('weather') is not None:
            weather = data['weather']
            weather = weather[0]
            for i in weather:
                data['environment'][i]=weather[f'{i}']
            del(data['weather'])
        return data








