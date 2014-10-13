from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect
from flask import request
from werkzeug import secure_filename
from suds.client import Client
import os
from MemoqTMClient import MemoqTMClient

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'media'
app.secret_key = "lasdjkfhfle8293ry"


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login", methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid username or password. Please jump at least three times and \
            try again.'
            
        else:
            session['logged_in'] = True
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect(url_for('about'))

@app.route("/upload", methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        new_file = request.files['file']
        if new_file and 'tmx' in new_file.filename:
            filename = secure_filename(new_file.filename)
            new_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect('upload')
    return render_template('upload_tm.html', tm_list=os.listdir(app.config['UPLOAD_FOLDER']))

@app.route('/tm_list', methods=['GET', 'POST'])
def tm_list():
    tm_client = MemoqTMClient("http://memoq-new.milengo.com")
    tms = tm_client.get_tm_list("","")
    return render_template('tm_list.html', tms=tms, tm_count= len(tms))

@app.route('/tm_download/<guid>') 
def tm_download(guid): 
    return guid 

if __name__ == "__main__":
    app.run(debug=True)