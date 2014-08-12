from flask import render_template
from . import tms
from ..models import User


@tms.route('/')
def index():
    return render_template('tms/index.html')

@tms.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('tms/user.html', user=user)
