from shell_tools import *

def change_issuer(public_key):
	delete_line("issuer_conf.ini")
	write('issuing_address = {}\n'.format(public_key), 'issuer_conf.ini')

def write_key(private_key):
	delete_line('key.txt')
	write(str(private_key), 'key.txt')

def issue_certs():
	return sh(["cert-issuer", "-c", "issuer_conf.ini"])
