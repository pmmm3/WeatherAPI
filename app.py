from flask import Flask
from api.routes.city import city
from api.routes.main import main
from flask_smorest import Api

# Define the API Configuration
class Config:
    OPENAPI_VERSION = "3.0.2"
    OPENAPI_JSON_PATH = "api-spec.json"
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_REDOC_PATH = "/redoc"
    OPENAPI_REDOC_URL = (
        "https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js"
    )
    OPENAPI_SWAGGER_UI_PATH = "/swagger"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    OPENAPI_RAPIDOC_PATH = "/rapidoc"
    OPENAPI_RAPIDOC_URL = "https://unpkg.com/rapidoc/dist/rapidoc-min.js"


def create_app():
    app = Flask(__name__)

    app.config["API_TITLE"] = "My Weather API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.2"

    app.config.from_object(Config())

    return app


if __name__ == '__main__':

    weather_app = create_app()
    api = Api(weather_app)
    api.register_blueprint(main)
    api.register_blueprint(city)
    weather_app.run(debug=True)
