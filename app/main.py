#!/usr/bin/python3
from flask import Flask, render_template, request, send_file
from key_commands import *
from create_pair import create_addr
from issue_certs import *
from build_certs import *
from web_maker import *
from file_system import *
from update_verifier import *

app = Flask(__name__)
app.config['app_folder'] = '/home/blockchain/modules/'
ALLOWED = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv', 'tgz'])
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED

@app.route('/download')
def download():
    return send_file(app.config['app_folder'] + 'certs.tgz', as_attachment=True)

@app.route('/issuer.json')
def issuer_id():
    return app.send_static_file('issuer.json')

@app.route('/')
def index():
	# give index.html a return_message string
	return render_template('index.html' ,message = '')

@app.route('/registry')
def registry():
	# give registry.html a fetch all list
	info = fetch_all()
	return render_template('registry.html', info=info)

@app.route('/registry/register', methods=['POST'])
def register_usr():
	user = request.form.get('user')
	pw = request.form.get('pw')
	key = request.form.get('key')
	info = fetch_user(user)
	if len(info) > 0:
		return render_template('index.html', message = 'username taken')
	register_user(user, pw, key, ' ')
	print('{} {} {} registered'.format(user, pw, key))
	return render_template('registry.html')


@app.route('/registry/fetch', methods=['POST'])
def fetch_usr():
	usr = request.form.get('user')
	user_info = fetch_user(usr)
	print(user_info)
	return render_template('fetched.html', info=user_info)

@app.route('/new', methods=['POST'])
def new_usr():
	usr = request.form.get('user')
	pw = request.form.get('pw')
	res = fetch_user(usr)
	if (len(res) > 0):
		return render_template('index.html', message = 'username {} taken'.format(usr))
	addr = create_addr()
	register_user(usr, pw, addr[0], addr[1])
	m = 'Your public key is "{}" and it has been added to the registry under the name "{}"'.format(addr[0], usr)
	return render_template('index.html', message = m)

@app.route('/load', methods=['POST'])
def load_money():
	return render_template('index.html', message = 'paypal api not yet installed')

@app.route('/issue', methods=['POST'])
def issue():
	if 'csv' not in request.files or request.files['csv'].filename == '':
		return render_template('index.html', message = 'must load a csv file')
	csv = request.files['csv']
	if not allowed_file(csv.filename):
		return render_template('index.html', message = 'must load a .csv filetype')
	usr = request.form.get('user')
	info = fetch_user(usr)
	if len(info) == 0:
		return render_template('index.html', message = 'user: {} does not exist'.format(usr))
	info = info[0]
	pw = request.form.get('pw')
	if info[1] != pw or info[3] == ' ':
		return render_template('index.html', message = 'user or password doesnt match')
	name = request.form.get('issuer_name')
	web = request.form.get('issuer_url')
	email = request.form.get('issuer_email')
	iid = 'http://18.188.147.68/issuer.json'
	# 'https://api.myjson.com/bins/9jd6u' #Todo: make issuer.json
	desc = request.form.get('certificate_description')
	title = request.form.get('certificate_title')
	nar = request.form.get('criteria_narrative')
	guid = request.form.get('badge_id')
	# csv overwrite
	csv.save(app.config['app_folder'] + 'recipients.csv')
	# database queries - public key, private key
	pub = info[2]
	priv = info[3]
	# issue
	change_issuer(pub)
	write_key(priv)
	erase_certs() # clear blockchain_certificates and unsigned folders
	tools_status = run_cert_tools(issuer_url = web, issuer_email = email, 
			issuer_name = name, issuer_id = iid,
			issuer_public_key = pub, certificate_description = desc,
			certificate_title = title, criteria_narrative = nar,
			badge_id = guid)
	batch_status = run_batch_tools()
	if (tools_status != 0 or batch_status != 0):
		return render_template('index.html', message = 'bad issuer form data')
	issue_status = issue_certs()
	if (issue_status != 0):
		return render_template('index.html', message =  'Please load wallet with money')
	zipper('certs.tgz', 'blockchain_certificates')
	update_verifier() # update verifier folder
	msg = 'Success: certificates propogating\n'
	dl = 'Click Download to get a zip file of the issued certs.'
	#return send_file(app.config['app_folder'] + 'certs.tgz', as_attachment=True)
	return render_template('index.html', message = msg + dl)

@app.route('/verify', methods=['POST'])
def verify():
    if 'tgz' not in request.files or request.files['tgz'].filename == '':
        return render_template('index.html', message = 'must load a tgz file')
    tgz = request.files['tgz']
    if not allowed_file(tgz.filename):
        return render_template('index.html', message = 'must load a .tgz filetype')
    tgz.save(app.config['app_folder'] + 'certs.tgz')
    update_from_tgz()
    return render_template('index.html', message = 'Success: Open verifier to verify certs')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
