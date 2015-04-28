from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect
from flask import request
from werkzeug import secure_filename
from suds.client import Client
import os

import app.config


app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'media')
from app import views
