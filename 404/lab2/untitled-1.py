import socket
import sys
try:
    s=socket.socket(socket_AF_INET,socket.SOCKET_STREAM)
except:
    print('failed to create socket')
    print('Error code: '+str(msg[0])+', Error message: '+str(msg[1]))
    sys.exit()
print('socket created')