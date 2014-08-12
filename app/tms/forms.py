from flask.ext.wtf import Form
from wtforms import StringField, TextField, SubmitField



class ProfileForm(Form):
	name = StringField('Name')
	location = StringField('Location')
	bio = TextField('Bio')
	sumbit = SubmitField('Save changes')