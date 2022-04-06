#!/usr/bin/env python3

import cgi, hashlib, libs.functions
form = cgi.FieldStorage()

from libs.config import *

# Logindaten abfragen
# login = form.getvalue('login')
filepath = form.getvalue('filepath')
# password = hashlib.md5(str(form.getvalue('pass')).encode('utf-8')).hexdigest()

print(HEADER)

print("         <section>")
print("             <article>")
print(filepath)
print("             <article>")
print("         </section>")

print(FOOTER)