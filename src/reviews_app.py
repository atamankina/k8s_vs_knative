import os

from flask import Flask

from .config import app_config
from .models import db
from .views.UserView import user_api as user_blueprint
from .views.ReviewView import review_api as review_blueprint
from .views.RestaurantView import restaurant_api as restaurant_blueprint


app = Flask(__name__)

app.config.from_object(app_config[os.getenv('FLASK_ENV')])

db.init_app(app)

app.register_blueprint(user_blueprint, url_prefix='/users')
app.register_blueprint(review_blueprint, url_prefix='/reviews')
app.register_blueprint(restaurant_blueprint, url_prefix='/restaurants')


@app.route('/', methods=['GET'])
def index():
    """
    Index endpoint, no specific function
    """
    return 'This is the API to handle restaurant reviews.'
