class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    pass


config = {'Development': DevelopmentConfig,

        'default': DevelopmentConfig
        }