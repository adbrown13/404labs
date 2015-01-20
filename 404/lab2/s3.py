import socket
import sys
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as msg:
    print('failed to create socket')
    print('Error code: '+str(msg[0])+', Error message: '+msg[1])
    sys.exit()
print('socket created')
host = 'www.google.com'
port= 80
try:
    remote_ip=socket.gethostbyname(host)
except socket.gaierror:
    print('Host name could not be resolved')
    sys.exit()
print('IP adress of ' +host+' is '+remote_ip)
s.connect((remote_ip, port))
print('Socket is connected to '+host+ ' on ip '+remote_ip)

message= "GET / HTTP/1.1\r\n\r\n"
try:
    s.sendall(message.encode("UTF8"))
except:
    print('send failed')
    sys.exit()
print('Message sent successfully')
