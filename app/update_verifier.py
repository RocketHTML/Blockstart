#!/usr/bin/python3

from web_maker import *
from file_system import *

flask_home = '/home/blockchain/modules/'
flask_unsigned = flask_home + 'unsigned_certificates/'
flask_certs = flask_home + 'blockchain_certificates/'
flask_webpage = flask_home + 'blockcert.html'
verifier_home = '/home/blockchain/cert-web-component/'
demo_home = verifier_home + 'demo/'
demo_certs = demo_home + 'demo_certs/'

def erase_certs():
    clean_folder(flask_unsigned)
    clean_folder(flask_certs)

def update_verifier():
    clean_folder(demo_certs)
    move_folder(flask_certs, demo_certs)
    filenames = ['./demo_certs/' + l for l in get_filenames(demo_certs)]
    filenames += ['./f9ee9b0a-26ca-4af2-bca5-2a7c571f0d93.json']
    make_webpage(filenames)
    move_file(flask_webpage, demo_home)

def update_from_tgz():
    clean_folder(demo_certs)
    unzipper('certs.tgz', demo_certs)
    filenames = ['./demo_certs/' + l for l in get_filenames(demo_certs)]
    make_webpage(filenames)
    move_file(flask_webpage, demo_home)

