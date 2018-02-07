import socket
import sys

'''Simple utility used in various labs and projects to test connectivity of setup networks'''

while (1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)
    testtype = ""
    testtype = input("Would you like to test (l)ocal connectivity, (r)emote connectivity, or (D)NS resolution?")
    if (testtype == "l"):
        try:
            s.connect(("192.168.44.254", 5000))
            print("Local connection successful")
        except socket.error:
            print("Local connection unsuccessful")
    elif (testtype == "r"):
        try:
            s.connect(("8.8.8.8", 5000))
            print("Remote connection successful")
        except socket.error:
            print("Remote connection unsuccessful")
    elif (testtype == "D"):
        try:
            s.connect(("google.com", 5000))
            print("DNS resolution successful")
        except socket.error:
            print("DNS resolution unsuccessful")
    else:
    	print("given &test, need l, r, or D")
