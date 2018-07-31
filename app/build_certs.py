from subprocess import call
## These are module constants
home_path = "/home/blockchain/modules/"
data_dir = home_path
template_dir = "certificate_template"
template_file_name = "template.json"
unsigned_certificates_dir = "unsigned_certificates"
filename_format = "uuid"
no_clobber = "True"
roster = "recipients.csv"
issuer_logo_file = "images/logo.png"
cert_image_file = "images/certificate-image.png"
issuer_signature_file = "images/issuer-signature.png"

# not optional, but optional for now
revocation_list = "https://www.blockcerts.org/samples/2.0/revocation-list-testnet.json"
issuer_signature_lines = ('{"fields": [{"job_title": "University Issuer",'
'"signature_image": "images/issuer-signature.png",'
'"name": "Your signature"}]}')

#constants 
aa = "--data_dir={}".format(data_dir)
bb = "--template_dir={}".format(template_dir)
cc = "--template_file_name={}".format(template_file_name)
dz = "--unsigned_certificates_dir={}".format(unsigned_certificates_dir)
ez = "--issuer_logo_file={}".format(issuer_logo_file)
fz = "--cert_image_file={}".format(cert_image_file)
gz = "--issuer_signature_file={}".format(issuer_signature_file)
hy = "--revocation_list={}".format(revocation_list)
iy = "--issuer_signature_lines={}".format(issuer_signature_lines)

def run_cert_tools(
	issuer_url,
	issuer_email, 
	issuer_name,
	issuer_id,
	issuer_public_key,
	certificate_description,
	certificate_title,
	criteria_narrative,
	badge_id):
	# runs cert tools shell scripts
	# roster will be named after the public key
	
	a = "--issuer_email={}".format(issuer_email)
	b = "--issuer_name={}".format(issuer_name)
	c = "--issuer_id={}".format(issuer_id)
	d = "--issuer_public_key={}".format('ecdsa-koblitz-pubkey:' + issuer_public_key)
	e = "--certificate_description={}".format(certificate_description)
	f = "--certificate_title={}".format(certificate_title)
	g = "--criteria_narrative={}".format(criteria_narrative)
	h = "--badge_id={}".format(badge_id)
	i = "--issuer_url={}".format(issuer_url)
	return call(["create-certificate-template", a, b, c, d, e, f, g, h, i,
							bb, cc, aa, ez, fz, gz, hy, iy])

def run_batch_tools():
	r = '--roster={}'.format(roster)
	return call(["instantiate-certificate-batch", aa, bb, cc, dz, r])
