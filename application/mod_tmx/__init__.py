from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import request
import os
from application.mod_tmx.tmx import Tmx

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'media')

mod_tmx = Blueprint('mod_tmx', __name__, template_folder='templates')

@mod_tmx.route('/upload')
def upload():
    if request.method == 'POST':
        new_file = request.files['file']
        if new_file and 'tmx' in new_file.filename:
            filename = secure_filename(new_file.filename)
            new_file.save(os.path.join(UPLOAD_FOLDER, filename))
            return redirect('upload')
    return render_template('upload_tm.html', tm_list=os.listdir(UPLOAD_FOLDER))