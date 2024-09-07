import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')

    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://store_x_user:LokiwHan12@localhost:5432/store_x_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JSON_SORT_KEYS = False
    TEMPLATES_AUTO_RELOAD = True
    DEBUG = os.environ.get('DEBUG', True)

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL', 'postgresql://store_x_user:LokiwHan12@localhost:5432/store_x_db')

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://store_x_user:LokiwHan12@localhost:5432/store_x_db')
