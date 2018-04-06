"""
File that creates an error log readable by other system admins based
on accesses to your webserver.

author: Shane Ogden

"""

import os

import string



def main():

    path = raw_input("Enter file path: ")

    file = open(path)

    f = open("adminreport.txt", "w+")


    f.write("ERROR REPORT FOR LOCALHOST APACHE WEBSERVER by S. OGDEN\n")

    f.write("=======================================================\n")

    f.write("DATE                              ERROR\n")
    
    for line in file:
        """
        if line.startswith('['):
            x = line.split()

            f.write(string.lstrip(x[0], '[')
            f.write(' ' + x[1] + ' ' + x[2] + ' ' + x[3] + ' ' + x[4] + string.strip(x[5], ['[', ']']) + '\n')
        """
        if line.startswith('['):
	    x = line.split()
	    f.write('[' + x[1] + ' ' + x[2] + ' ' + x[3] + ' ' + x[4] +  '     ' + x[5] + ' ')
	    count = 6
	    while count < len(x):
		if not x[count].startswith('['):
			f.write(x[count] +' ')
			count -= 1
		count += 2
	f.write('\n\n')

if __name__ == '__main__':

    main()
