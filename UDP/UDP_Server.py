import socket

UDP_IP = "192.168.0.10"
UDP_PORT = 5005
buffer_size = 1024  # Maximum message size (bytes)

# Create a datagram socket
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

# Bind to address and ip
sock.bind((UDP_IP, UDP_PORT))

print "Waiting for client..."

while(True):
	# Recieve the request from client
	data, addr = sock.recvfrom(buffer_size)
	print "\n"

	print "Received Request From Client:"
	print "UDP origin IP:", addr[0]
	print "UDP origin port:", addr[1]
	print "message:", data
	if data=="fin":
		break
	print "\n"

	#Sending a reply to client
	Response = data.upper()
	print "Sended Reply to Client:"
	print "UDP target IP:", addr[0]
	print "UDP target port:", addr[1]
	print "message:", Response
	sock.sendto(Response, addr) #Function to send reply
sock.close()
	