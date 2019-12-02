import socket

HOST = '127.0.0.1'  # (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

#Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print('Ready to receive requests!')

#Establishing a connection 
conn, addr = s.accept()
print('Conected on ', addr)

#Listen to client
while 1:
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(data)
conn.close()