from flask import Flask
import os

import mainapp.config


app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'media')
import mainapp.views
