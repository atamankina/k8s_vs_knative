import os


class BaseConfig(object):
    DEBUG = False
    TESTING = False

    POSTGRES_USER = os.environ.get('POSTGRES_USER', 'galina')
    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', '')
    POSTGRES_DB = os.environ.get('POSTGRES_DB', 'restaurant_reviews')
    POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'localhost')

    POSTGRES_STRING = 'postgresql://{user}:{password}@{uri}:5432/{database}'.format(
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        uri=POSTGRES_HOST,
        database=POSTGRES_DB
    )

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', POSTGRES_STRING)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Development(BaseConfig):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False


class Production(BaseConfig):
    """
    Production environment configuration
    """
    DEBUG = False
    TESTING = False


class Testing(BaseConfig):
    """
    Testing environment configuration
    """
    DEBUG = True
    TESTING = True


app_config = {
    'development': Development,
    'production': Production,
    'testing': Testing,
}
