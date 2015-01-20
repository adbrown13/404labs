import socket
import sys
try:
    import thread
except ImportError:
    import _thread as thread

def clientthread(conn):
    while 1:
        data= conn.recv(4048)
        data2=str(data)
        data2=data2[0:len(data2)-2]
        reply=data2+' Ashley'
        conn.sendall(reply)        



try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as msg:
    sys.exit()
host = ''
port= 8881
try:
    s.bind((host,port))
except socket.error as msg:
    sys.exit()
s.listen(5)

while 1:
    conn, addr =s.accept()
    thread.start_new_thread(clientthread,(conn,))

conn.close()
s.close()