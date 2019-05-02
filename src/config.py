import os


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
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
