import socket

HOST = '127.0.0.1'  # (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Connect to serv_socket
s.connect((HOST, PORT))
print('Client Conected!')

#receive
s.sendall('Hello world!')
data = s.recv(1024)
print('3-way handshake done!')

#close socket
s.close()
#Prints
print 'Received', repr(data)