import socket

UDP_SERVER_IP = "192.168.0.10" # Set this parameter with your server IP
UDP_PORT = 5005 # Set this parameter with the port
buffer_size = 1024 # Maximum message size (bytes)

# Create a datagram socket
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

# Bind to address and ip
sock.bind((socket.gethostname(), UDP_PORT))

MESSAGE = "Esta es la cadena de caracteres a transformar de minuscula a mayuscula"

print "Sended Request to Server: "
print "UDP target IP:", UDP_SERVER_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

# Send a request to server
sock.sendto(MESSAGE, (UDP_SERVER_IP, UDP_PORT))
sock.sendto("fin", (UDP_SERVER_IP, UDP_PORT))

# Recive the reply from server
data, addr = sock.recvfrom(buffer_size) # buffer size is 1024 bytes
print "\n"
print "Recieved Reply from Server: "
print "UDP origin IP:", addr[0]
print "UDP origin port:", addr[1]
print "message:", data

sock.close()