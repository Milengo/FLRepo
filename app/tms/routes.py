from flask import render_template, redirect, request, url_for, flash
from flask.ext.login import login_required
from . import tms
from ..models import User
from .. import db
from .forms import ProfileForm


@tms.route('/')
def index():
    return render_template('tms/index.html')

@tms.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('tms/user.html', user=user)

@tms.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
	form = ProfileForm()
	if form.validate_on_submit():
		current_user.name = form.name.data
		current_user.location = form.location.data
		current_user.bio = form.bio.data
		db.session.add(current_user._get_current_object())
		db.session.commit()
		flash('Your profile has been updated!')
		return redirect(url_for('tms.user', username = current_user.username))
	form.name.data = current_user.name
	form.location.data = current_user.location
	form.bio.data = current_user.bio
	return render_template('tms/profile.html', form=form)