#!/usr/bin/env python
import cgi
 
form = cgi.FieldStorage()
bday = form.getvalue('birthday')
hobby = form.getvalue('hobby')
 
print "Content-type: text/html"
print
print"<body style =\"background-color: Moccasin;\">"
print"<h1 style = \"color: white; font-size: 40pt;\">Hello User!</h1>"
print"<h2 style = \"color: grey; font-size: 30pt;\">I recorded your birthday as %s and your main hobby as %s!</h2>" %(bday,hobby)
 

print"<form method=\"post\" action=\"page2.py\">"
print"<textarea name=\"name\" cols=\"40\" rows=\"1\" style =\"background-color: Peru; color: white; font-size: 25pt;\"> Enter name here...</textarea><br/>"
print"<textarea name=\"family\" cols=\"40\" rows=\"1\" style =\"background-color: Peru; color: white; font-size: 25pt;\"> Enter family here...</textarea><br/>"
print"<input type=\"submit\" value=\"Submit\">"
print"</form></body>"


