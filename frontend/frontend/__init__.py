from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__)

# Swagger
SWAGGER_URL = '/swagger'
API_URL = '/api/stream/docs'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "ALTV-Streaming"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


from frontend import api
