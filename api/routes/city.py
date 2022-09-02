
from flask import Response, abort
from flask_smorest import Blueprint
from api.schemes.historical_schema import HistoricalSchema

from api.schemes.info_schema import InfoWeatherSchema
from ..services.WeatherAPI import WeatherAPI as api
city = Blueprint('city', __name__)


@city.route('/city/<city_id>')
@city.response(200, InfoWeatherSchema)
def get_city(city_id):
    """
    Get the weather from city_id
    ---
    comentario interno
    """
    response = api.get_city(city_id)
    if response['cod'] == '404':
        response = (Response("City fault"))
        response.status_code = 404
        abort(response)
    elif response['cod'] == 200:
        return response

# cities ids examples : 2172797,833,2960
@city.route('/cities/<cities_ids>')
@city.response(200, InfoWeatherSchema(many=True))
def get_cities(cities_ids):
    """
        Split cities_id with commas and search each id in get_city()
        ---
        comentario interno
        """
    response = api.get_cities(cities_ids)
    return response

@city.route('/historical/<cities_ids>')
@city.response(200, HistoricalSchema(many=True))
def get_historical(cities_ids):
    """
         Split cities_id with commas and search the weather from last 5 days for each id
         ---
         comentario interno
         """
    response = api.get_historical(cities_ids)
    return response
