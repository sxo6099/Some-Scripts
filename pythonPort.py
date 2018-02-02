import socket
import sys

'''Shane Ogden, sxo6099@rit.edu, CSEC.101.02'''

def main():
	'''Gets the command line args, creating the related
	variables and running the Scan with them'''
	target_ip = sys.argv[1]
	start_port = int(sys.argv[2])
	end_port = int(sys.argv[3])
	Scan(target_ip, start_port, end_port)
	

def Scan(target_ip, start_port, end_port):
	'''Creates a local variable that will change as we change
	ports, creates a socket with a timeout condition,
	then attempts to scan all of the ports within the range'''
	temp_port = start_port
	while temp_port <= end_port:
		x = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		x.settimeout(.5)
		try:
			x.connect((target_ip, temp_port))
			print("Port ",temp_port, "is open")
		except socket.timeout:
			print("Port ",temp_port, "is filtered")
		except socket.error:
			print("Port ",temp_port, "is closed")
		temp_port += 1

main()
