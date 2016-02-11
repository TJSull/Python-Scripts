import socket
import sys

TCP_IP=""		#Host IP - Leave Blank - We are The Host
TCP_PORT=80		#Example Port
BUF_SIZE=1024		#Default Buffer Size

#Create TCP Socket
sc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#Bind to IP Number and Port Number
sc.bind((TCP_IP, TCP_PORT))
#Listen on Binding port - Allow one Connection
sc.listen(1)

#Create New Socket for Incoming Computer
client, address = sc.accept()
#Print Address
print 'Connection Address:', address

#Infinite Loop
while 1:
	data = client.recv(BUF_SIZE)
	#If Data is not received, Break Loop
	if not data: break
	#Print Received Data
	print "Received Data:", data
client.close()

#Demonstrate by typing http://127.0.0.1:80 into browser.
