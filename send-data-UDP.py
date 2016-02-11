import socket
import sys

BUF = 'ABCDE' * (2500)		#Data to be sent - ABCDE * 2500
UDP_IP="74.125.224.72"		#Example IP - Google IP set in Example
UDP_PORT=53 				      #Example Port - DNS Port

try:
	#UDP Socket
    sc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sc.connect((UDP_IP, UDP_PORT))
    sc.send(BUF + "\n")
    print("Data sent")
    sc.close()

except:
    print("Can't send data")
    sys.exit()
