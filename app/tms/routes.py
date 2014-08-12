from flask import render_template
from . import tms


@tms.route('/')
def index():
    return render_template('tms/index.html')

@tms.route('/user/<username>')
def user(username):
    return render_template('tms/user.html', username=username)