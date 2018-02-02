import socket

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while (1):
    testtype = ""
    testtype = raw_input("Would you like to test (l)ocal connectivity, (r)emote connectivity, or (D)NS resolution?")
    if (testtype == "l"):
    	s.connect(("192.168.44.254", 80))
    elif (testtype == "r"):
    	s.connect(("8.8.8.8", 80))
    elif (testtype == "D"):
    	s.connect(("google.com", 80))
    else:
    	print("given &test, need l, r, or D")
