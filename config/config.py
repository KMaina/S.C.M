import os


class Config:
    """Parent configuration class."""
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = True


class DevelopmentConfig(Config):
    """Configurations for Development."""
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


class TestingConfig(Config):
    """Configurations for Testing"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_TESTING')


class ProductionConfig(Config):
    """Configurations for Production."""
    TESTING = False
    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
