#!/usr/bin/python3

def make_webpage(certs):
    file_start = '''
<!doctype html>
<html>
<head>
<title>blockchain-certificate demo</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, minimum-scale=1.0, initial-scale=1, user-scalable=yes">
<script src="../../webcomponentsjs/webcomponents-lite.js"></script>
<link rel="import" href="../../iron-demo-helpers/demo-pages-shared-styles.html">
<link rel="import" href="../../iron-demo-helpers/demo-snippet.html">
<link rel="import" href="../blockchain-certificate.html">
<link rel="import" href="../validate-certificate.html">
<style is="custom-style" include="demo-pages-shared-styles">
</style>
</head>
<body>
<div class="container">
'''
    cert_string = '''
<validate-certificate href="{}">
<blockchain-certificate href="{}"></blockchain-certificate>
</validate-certificate>
<br><hr><br>
'''
    file_end = '''
</div>
</body>
</html>
'''
    with open('blockcert.html', 'w') as f:
        f.write(file_start)
        for url in certs:
            print(cert_string.format(url, url), file=f)
        f.write(file_end)
