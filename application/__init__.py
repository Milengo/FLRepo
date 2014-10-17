from flask import Flask
from flask import Blueprint
from config import Config, DevelopmentConfig
import os

app = Flask(__name__)
conf = DevelopmentConfig()
app.config.from_object(conf)
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(),'media')

from application.mod_auth import *
from application.mod_memoqclient import mod_memoqclient
from application.mod_tmx import *

app.register_blueprint(mod_memoqclient)