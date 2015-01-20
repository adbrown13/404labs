import socket
import sys
try:
    s=socket.socket(socket_AF_INET,socket.SOCKET_STREAM)
except:
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