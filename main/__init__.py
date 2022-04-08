from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config['config_filename'])
    config['config_filename'].init_app(app)

    db.init_app(app)

    from main.user import user as user_blueprint
    app.register_blueprint(user_blueprint)

    return app