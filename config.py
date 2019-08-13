import os

class Config:
    
    SECRET_KEY = 'ptex'
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://george:PTEXPTEX61@localhost/vlog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://george:PTEXPTEX61@localhost/vlog'
    pass
    DEBUG = True

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://george:PTEXPTEX61@localhost/vlog'
    DEBUG = True

class TestConfig(Config):

    DEBUG = True

config_options = {
    'production': ProdConfig,
    'development':DevConfig,
    'tests': TestConfig
}
