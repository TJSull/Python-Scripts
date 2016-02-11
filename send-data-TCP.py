import socket
import sys

BUF = 'ABCDE' * (2500)		#Data to be sent - ABCDE * 2500
TCP_IP="74.125.224.72"		#Example IP - Google IP set in Example
TCP_PORT=80			#Example Port

try:
    #TCP Socket
    sc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sc.connect((TCP_IP, TCP_PORT))
    sc.send(BUF + "\n")
    print("Data sent")
    sc.close()

except:
    print("Can't send data")
    sys.exit()
