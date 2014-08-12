import os
from app import create_app, db
from app.models import User
from flask.ext.script import Manager


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

@manager.command
def adduser(email, username, admin=False):
	from getpass import getpass
	password = getpass()
	password2 = getpass("Confirm password: ")
	if password !=password2:
		import sys
		sys.exit("Error: passwords should match")
	db.create_all()
	user = User(email=email, username=username,password=password, is_admin=admin)
	db.session.add(user)
	db.session.commit()

	print("User {0} registered successfully ".format(username))




if __name__ == '__main__':
    manager.run()