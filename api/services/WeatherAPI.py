import json
import os
import requests
import datetime as dt
from dotenv import load_dotenv
# To config .env file
load_dotenv()


class WeatherAPI:
    key = os.getenv("APIKEY")
# not used now
    def search(name):
        try:
            file = open(f'../bd/{name}.json')
            data = json.load(file)
            file.close()
            return data
        except:
            return None
# not used now
    def search_name(lat,lon):
        url = 'https://api.openweathermap.org/geo/1.0/reverse?'
        response = requests.get(
            url+f'lat={lat}&lon={lon}&appid={WeatherAPI.key}').json()
        result = response[0]
        name=result['name']
        return name

# not used now
    def store(name, data):

        try:
            file = open(f'../bd/{name}.json', 'w')
            json_string = json.dumps(data)
            file.write(json_string)
            file.close()
        except:
            raise('No se ha podido guardar el documento')

    def get_city(city_id):
        # Search city in bd
        # using local files as bd
        bd_id = WeatherAPI.search(city_id)
        if ((bd_id is not None) and
            (bd_id['created'] - dt.datetime.now()) < dt.timedelta(minutes=10)):
            # exist and  it's updated
            # openweathermap actualize data every 10 minutes
            print("Not implent yet")
        else:
            # Make the openweathermap api call

            url = f'https://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={WeatherAPI.key}&units=metric'
            response = requests.get(url).json()
            # return json to serialize with the schema in the route
            return response

    def get_cities(cities):
        # Separate cities that are separated by delimiter
        delimiter = ","
        cities = str(cities).split(delimiter)
        # Saving in a list
        total = []
        for id_c in cities:
            # For each city use the function and collect the result
            result = WeatherAPI.get_city(id_c)
            total.append(result)
        response = total
        # return a list with the results, if one fail its a empty item
        return response


    def get_historical(cities):
        # Separate cities that are separated by delimiter
        delimiter = ","
        cities = str(cities).split(delimiter)
        total = []
        for id_c in cities:
            # For each city
            # Make the openweathermap api call with cnt = 5 to save only 5 results and units in metric standard
            url = f'https://api.openweathermap.org/data/2.5/forecast?id={id_c}&appid={WeatherAPI.key}&units=metric&cnt=5'
            response = requests.get(url).json()
            total.append(response)

        return total




