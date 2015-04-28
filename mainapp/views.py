from mainapp import app
from flask import render_template
from flask import request
from flask import redirect
from flask import send_from_directory
from mainapp.memoqtmclient import MemoqTMClient
from mainapp.tmx import Tmx
import os


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        new_file = request.files['file']
        if new_file and 'tmx' in new_file.filename:
            filename = secure_filename(new_file.filename)
            new_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect('upload')
    return render_template(
        'upload_tm.html',
        tm_list=os.listdir(app.config['UPLOAD_FOLDER']))


@app.route('/tm_list', methods=['GET', 'POST'])
def tm_list():
    tm_client = MemoqTMClient(app.config['MEMOQ_SERVER_URL'])
    tms = tm_client.get_tm_list("", "")
    with open('test.txt', 'w') as guid:
        for tm in tms:
            guid.write("Guid: {}, name: {}\r\n".format(tm.Guid, tm.Name))
    return render_template('tm_list.html', tms=tms, tm_count=len(tms))


@app.route('/tm_download/<guid>/<name>')
def tm_download(guid, name):
    tm_client = MemoqTMClient(app.config['MEMOQ_SERVER_URL'])
    filename = os.path.join(
            app.config['UPLOAD_FOLDER'],
            name + ".tmx")
    tmx_name = ".".join([name,'tmx'])
    tm_client.export_tmx(guid, filename)
    return send_from_directory(directory=app.config['UPLOAD_FOLDER'], filename=tmx_name)


@app.route('/read_tmx/<filename>')
def read_tm_data(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    tmx = Tmx(filepath)

    return render_template(
        'tm_display.html',
        segments=tmx.trans_units,
        attributes=tmx.attributes,
        custom_properties=tmx.properties,
        count=tmx.len())
