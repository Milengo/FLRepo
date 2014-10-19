from flask import Blueprint
from flask import render_template
from flask import redirect
from MemoqTMClient import MemoqTMClient
import os

MEMOQ_SERVER_URL = "http://memoq-new.milengo.com"

mod_memoqclient = Blueprint('mod_memoqclient', __name__, template_folder='templates')


@mod_memoqclient.route('/tm_list', methods=['GET', 'POST'])
def tm_list():
    tm_client = MemoqTMClient(MEMOQ_SERVER_URL)
    tms = tm_client.get_tm_list("","")
    with open('test.txt', 'w') as guid:
        for tm in tms:
            guid.write("Guid: {}, name: {}\r\n".format(tm.Guid, tm.Name))
    return render_template('tm_list.html', tms=tms, tm_count= len(tms))

@mod_memoqclient.route('/tm_download/<guid>/<name>') 
def tm_download(guid, name): 
    tm_client = MemoqTMClient(MEMOQ_SERVER_URL)
    tm_client.export_tmx(guid, os.path.join(os.getcwd(), 'media',name + ".tmx"))
    return redirect('upload')