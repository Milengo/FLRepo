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
    src_langs = set()
    targ_langs = set()
    clients = set()
    domains = set()
    for tm_info in tms:
    	src_langs.add(tm_info.SourceLanguageCode)
    	targ_langs.add(tm_info.TargetLanguageCode)
    	clients.add(tm_info.Client)
    	domains.add(tm_info.Domain)
    return render_template('tm_list.html', tms=tms, tm_count= len(tms), src=list(src_langs), trg=list(targ_langs), clients=list(clients),
    	 domains=list(domains))

@mod_memoqclient.route('/tm_download/<guid>/<name>') 
def tm_download(guid, name): 
    tm_client = MemoqTMClient(MEMOQ_SERVER_URL)
    tm_client.export_tmx(guid, os.path.join(os.getcwd(), 'media',name + ".tmx"))
    return redirect('upload')