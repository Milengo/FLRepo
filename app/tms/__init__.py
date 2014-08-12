from flask import Blueprint
tms = Blueprint('tms', __name__)
from . import routes