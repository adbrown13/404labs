#!/usr/bin/env python
 
import cgi
 
form = cgi.FieldStorage()
 
name = form.getvalue('name')
family = form.getvalue('family')
 
print "Content-type: text/html"
print
print"<body style =\"background-color: Peru;\">"
print"<h1 style = \"color: white; font-size: 40pt;\">Hello %s %s!</h1>" %(name,family)



print"<form method=\"post\" action=\"page1.py\">"
print"<textarea name=\"birthday\" cols=\"40\" rows=\"1\"  style =\"background-color: moccasin; color: grey; font-size: 25pt;\"> Enter birthday here...</textarea><br/>"
print"<textarea name=\"hobby\" cols=\"40\" rows=\"1\"  style =\"background-color: moccasin; color: grey; font-size: 25pt;\"> Enter main hobby here...</textarea><br/>"
print"<input type=\"submit\" value=\"Submit\">"
print"</form>"
