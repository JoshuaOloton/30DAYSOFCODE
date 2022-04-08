import os

basedir = os.getcwd()

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{basedir}/test-dev.db'


config = {'Development': DevelopmentConfig,

        'default': DevelopmentConfig
        }