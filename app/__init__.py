from flask import Flask
from config import config
from flask.ext.bootstrap import Bootstrap
bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from .tms import tms as tms_blueprint
    app.register_blueprint(tms_blueprint)
    bootstrap.init_app(app)
    return app