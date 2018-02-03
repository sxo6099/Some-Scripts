import socket
import sys

'''Simple utility used in various labs and projects to test connectivity of setup networks'''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(1)

while (1):
    testtype = ""
    testtype = input("Would you like to test (l)ocal connectivity, (r)emote connectivity, or (D)NS resolution?")
    if (testtype == "l"):
        try:
            s.connect(("192.168.44.254", 50000))
            print("Local connection successful")
        except:
            print("Local connection unsuccessful")
    elif (testtype == "r"):
        try:
            s.connect(("8.8.8.8", 50000))
            print("Remote connection successful")
        except:
            print("Remote connection unsuccessful")
    elif (testtype == "D"):
        try:
            s.connect(("google.com", 50000))
            print("DNS resolution successful")
        except:
            print("DNS resolution unsuccessful")
    else:
    	print("given &test, need l, r, or D")
