#!/usr/bin/env python
import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable()  ## This line enables CGI error reporting
 
server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", 8006)
handler.cgi_directories = ["/cgi"]
 
httpd = server(server_address, handler)
print "starting server..."
httpd.serve_forever()
