#!/usr/bin/python36

print("content-type: text/html")
print("")

import  cgi
import subprocess as sp

form = cgi.FieldStorage()
cname = form.getvalue('cname')
imgname = form.getvalue('imgname')
portno = form.getvalue('portno')

print(cname , imgname ,)

docker_launch_output = sp.getstatusoutput("sudo ansible-playbook caas.yml --extra-vars='cname={c} portno={p}'".format (c=cname ,p=portno))
print(docker_launch_output)
if docker_launch_output[0]  == 0:
	print("container named {c} successfully launched ..".format(c=cname))
	print("<a href='docker-manage.py'>click here to manage Container</a>")
else:
	
	print("container named {c} failed ..".format(c=cname))






