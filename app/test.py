from build_certs import *
from issue_certs import *
from shell_tools import * 
#issuer_email,
#issuer_name,
#issuer_id = "https://www.holbertonschool.com/",
#issuer_public_key,
#certificate_description,
#certificate_title,
#criteria_narrative,
#badge_id

pubkey = "1L9u9qjqTmK2B1qHUz1Xp46WRCK6BuqvuD"
privkey = "KxV4cM8rTtxgNqdFCKghZYJXGfKU9sSX86boGvogqck5htyEU2FY"
a = "madisononealburke@hotmail.com"
b = "madison"
c = "https://www.holbertonschool.com/"
d = pubkey
e = "Certificate for being my friend"
f = "Certificate of Friendship"
g = "This certificate suggests you are a Good Friend"
h = "182546fb-d151-4819-a1ed-c6a01096d1fc"
i = "https://www.holbertonschool.com/"

def test():
	run_cert_tools(a, b, c, d, e, f, g, h, i)
	run_batch_tools()
	change_issuer(pubkey)
	write_key(privkey)
	issue_certs()
