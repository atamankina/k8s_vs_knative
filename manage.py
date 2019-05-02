import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from src.models.UserModel import UserModel
from src.models.ReviewModel import ReviewModel
from src.models.RestaurantModel import RestaurantModel
from src.app import create_app, db

env_name = os.getenv('FLASK_ENV')
app = create_app(env_name)

migrate = Migrate(app=app, db=db, user=UserModel, review=ReviewModel, restaurant=RestaurantModel)

manager = Manager(app=app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()